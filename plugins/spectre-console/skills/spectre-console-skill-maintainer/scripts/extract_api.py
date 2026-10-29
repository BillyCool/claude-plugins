#!/usr/bin/env python3
"""Extract the public Spectre.Console API surface from C# source into markdown.

Usage:
    python extract_api.py <core-repo> <cli-repo> <writer-skill-dir>

    <core-repo>  checkout of spectreconsole/spectre.console   (tag, e.g. 0.57.2)
    <cli-repo>   checkout of spectreconsole/spectre.console.cli (tag)
    <writer-skill-dir>  .../skills/spectre-console-writer

Writes (replacing) in <writer-skill-dir>/references/:
    api/**.md        one file per widget / area, every public type with its
                     public members, XML-doc summaries, defaults, and the
                     extension methods that apply to it
    api/_index.md    every public type -> file
    colors.md, spinners.md, emoji-shortcodes.md   (from the repo's data files)

It is a purpose-built C# *declaration* scanner (comments / strings / braces
aware), not a full parser. Everything it prints comes straight from source.
Run with no changes to the writer afterwards and `git diff` shows exactly what
the library changed between two tags.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

# (label, repo key, path under repo, package id)
PROJECTS = [
    ("ansi", "core", "src/Spectre.Console.Ansi", "Spectre.Console.Ansi"),
    ("core", "core", "src/Spectre.Console", "Spectre.Console"),
    ("testing", "core", "src/Spectre.Console.Testing", "Spectre.Console.Testing"),
    ("json", "core", "src/Extensions/Spectre.Console.Json", "Spectre.Console.Json"),
    ("imagesharp", "core", "src/Extensions/Spectre.Console.ImageSharp", "Spectre.Console.ImageSharp"),
    ("cli", "cli", "src/Spectre.Console.Cli", "Spectre.Console.Cli"),
    ("cli-testing", "cli", "src/Spectre.Console.Cli.Testing", "Spectre.Console.Cli.Testing"),
]

SKIP_DIRS = {"obj", "bin", "Properties", "Internal", "Unsafe_"}
# Generated files worth reading. The Backport.* lock polyfills are noise.
GENERATED_OK = ("Spectre.Console.SourceGenerator",)

# Small helper widgets merged into their parent's file.
MERGE = {
    "GridColumn": "Grid", "GridRow": "Grid",
    "TreeNode": "Tree",
    "PanelHeader": "Panel",
    "CalendarEvent": "Calendar",
    "TableColumn": "Table", "TableRow": "Table", "TableTitle": "Table",
    "TextPathStyles": "TextPath",
}


# --------------------------------------------------------------------------
# Scanner
# --------------------------------------------------------------------------
@dataclass
class Member:
    kind: str            # ctor, method, property, field, event, enumvalue, indexer
    sig: str
    summary: str = ""
    default: str = ""
    inherit: bool = False


@dataclass
class TypeInfo:
    project: str
    name: str            # Outer.Inner, no generics suffix
    display: str         # with generics
    kind: str            # class struct interface enum record delegate
    mods: str
    bases: list = field(default_factory=list)
    summary: str = ""
    file: str = ""
    members: list = field(default_factory=list)
    is_static: bool = False
    constraints: str = ""
    primary_ctor: str = ""
    ext_methods: list = field(default_factory=list)  # (target, sig, summary, tparams)


def clean_doc(lines):
    text = "\n".join(lines)
    m = re.search(r"<summary>(.*?)</summary>", text, re.S)
    inherit = "<inheritdoc" in text and not m
    s = m.group(1) if m else ""
    s = re.sub(r'<see\s+(?:cref|langword|href)="([^"]+)"\s*/>', lambda x: "`" + x.group(1).split(":")[-1] + "`", s)
    s = re.sub(r'<paramref\s+name="([^"]+)"\s*/>', r"`\1`", s)
    s = re.sub(r'<typeparamref\s+name="([^"]+)"\s*/>', r"`\1`", s)
    s = re.sub(r"</?(?:c|code|para|b|i)>", lambda x: "`" if x.group(0) in ("<c>", "</c>", "<code>", "</code>") else " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    s = re.sub(r"\s+", " ", s).strip()
    return s, inherit


def scan_file(path: Path):
    """Yield declaration records: dict(kind_hint, head, body, init, doc, depth_path)."""
    src = path.read_text(encoding="utf-8-sig", errors="replace")
    n = len(src)
    i = 0
    out = []            # flat list of events
    head = []           # chars of current statement head
    doc = []            # pending /// lines
    stack = []          # scopes: dict(kind, name_info)
    line_start = True

    def flush_head():
        h = "".join(head)
        head.clear()
        return h

    def strip_attrs(h):
        h = h.strip()
        while h.startswith("["):
            depth = 0
            for j, c in enumerate(h):
                if c == "[":
                    depth += 1
                elif c == "]":
                    depth -= 1
                    if depth == 0:
                        h = h[j + 1:].strip()
                        break
            else:
                break
        return h

    while i < n:
        c = src[i]
        # comments
        if src.startswith("///", i):
            j = src.find("\n", i)
            j = n if j < 0 else j
            doc.append(src[i + 3:j])
            i = j + 1
            continue
        if src.startswith("//", i):
            j = src.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        if src.startswith("/*", i):
            j = src.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        # preprocessor
        if c == "#" and (src.rfind(chr(10), 0, i) + 1 == i or src[src.rfind(chr(10), 0, i) + 1:i].strip() == ""):
            j = src.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        # strings / chars
        if c == '"' or (c in "$@" and i + 1 < n and src[i + 1] in '"$@') or c == "'":
            # raw string
            if src.startswith('"""', i):
                j = src.find('"""', i + 3)
                i = n if j < 0 else j + 3
                head.append('""')
                continue
            verbatim = False
            k = i
            while k < n and src[k] in "$@":
                if src[k] == "@":
                    verbatim = True
                k += 1
            if k < n and src[k] == '"':
                k += 1
                while k < n:
                    if verbatim:
                        if src[k] == '"':
                            if k + 1 < n and src[k + 1] == '"':
                                k += 2
                                continue
                            break
                    else:
                        if src[k] == "\\":
                            k += 2
                            continue
                        if src[k] == '"':
                            break
                    k += 1
                lit = src[i:k + 1]
                head.append(lit if len(lit) <= 70 and chr(10) not in lit else '"..."')
                i = k + 1
                continue
            if c == "'":
                k = i + 1
                while k < n and src[k] != "'":
                    k += 2 if src[k] == "\\" else 1
                head.append(src[i:k + 1])
                i = k + 1
                continue
        if c == "{":
            h = strip_attrs(flush_head())
            ev = ("open", h, doc[:], len(stack))
            doc = []
            out.append(ev)
            stack.append(h)
            i += 1
            continue
        if c == "}":
            leftover = strip_attrs(flush_head())
            out.append(("close", leftover, [], len(stack) - 1))
            if stack:
                stack.pop()
            i += 1
            continue
        if c == ";":
            h = strip_attrs(flush_head())
            out.append(("stmt", h, doc[:], len(stack)))
            doc = []
            i += 1
            continue
        if src.startswith("=>", i) and not any(
                not (x.startswith("namespace") or TYPE_RE.match(x)) for x in stack):
            h = strip_attrs(flush_head())
            # expression body: capture until ';' at same nesting
            depth = 0
            j = i + 2
            expr = []
            while j < n:
                ch = src[j]
                if ch in "({[":
                    depth += 1
                elif ch in ")}]":
                    depth -= 1
                elif ch == ";" and depth <= 0:
                    break
                elif ch == '"':
                    k = j + 1
                    while k < n and src[k] != '"':
                        k += 2 if src[k] == "\\" else 1
                    j = k
                expr.append(ch)
                j += 1
            out.append(("expr", h, doc[:], len(stack), "".join(expr).strip()))
            doc = []
            i = j + 1
            continue
        head.append(c)
        i += 1
    return out


TYPE_RE = re.compile(
    r"^(?P<mods>(?:(?:public|internal|protected|private|static|sealed|abstract|partial|readonly|unsafe|new|file|ref)\s+)*)"
    r"(?P<kind>class|struct|interface|enum|record\s+struct|record\s+class|record|delegate)\s+(?P<rest>.*)$",
    re.S,
)


def split_top(s, sep=","):
    parts, depth, cur = [], 0, []
    for ch in s:
        if ch in "<([{":
            depth += 1
        elif ch in ">)]}":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if "".join(cur).strip():
        parts.append("".join(cur).strip())
    return parts


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def parse_type_head(h):
    m = TYPE_RE.match(h)
    if not m:
        return None
    mods = norm(m.group("mods"))
    kind = norm(m.group("kind"))
    rest = norm(m.group("rest"))
    if kind == "delegate":
        return dict(mods=mods, kind=kind, name=rest, display=rest, bases=[], constraints="", primary="")
    constraints = ""
    wm = re.search(r"\swhere\s", " " + rest)
    if wm:
        idx = (" " + rest).index(wm.group(0)) - 1
        constraints = rest[idx:].strip()
        rest = rest[:idx].strip()
    primary = ""
    # record primary ctor:  Name(params) [: bases]
    pm = re.match(r"^([A-Za-z_][\w]*(?:<[^>]*>)?)\s*(\(.*\))\s*(?::\s*(.*))?$", rest, re.S)
    if pm and kind.startswith("record"):
        display, primary, basestr = pm.group(1), pm.group(2), pm.group(3) or ""
    else:
        if ":" in rest:
            display, basestr = rest.split(":", 1)
        else:
            display, basestr = rest, ""
    display = norm(display)
    bases = [norm(b) for b in split_top(basestr)] if basestr else []
    name = re.sub(r"<.*>", "", display)
    return dict(mods=mods, kind=kind, name=name, display=display, bases=bases, constraints=constraints, primary=norm(primary))


MODS = {"public", "internal", "protected", "private", "static", "sealed", "abstract", "virtual",
        "override", "readonly", "partial", "async", "extern", "unsafe", "new", "const", "required",
        "volatile", "event", "implicit", "explicit", "operator", "ref"}


def visibility(h, in_interface):
    toks = re.findall(r"[A-Za-z_]+", h.split("(")[0].split("=")[0])
    ts = set(toks)
    if "private" in ts:
        return False
    if "public" in ts:
        return True
    if "protected" in ts:
        return True
    return in_interface


def parse_member(h, kind_hint, in_interface, type_name, body=None):
    """Return (kind, sig, name) or None."""
    h = norm(h)
    if not h:
        return None
    if not visibility(h, in_interface):
        return None
    sig = h
    sig = re.sub(r"^(?:(?:public)\s+)", "", sig)  # public is noise; keep protected/static/etc.
    paren = h.find("(")
    eq = h.find("=")
    if re.search(r"\boperator\b", h.split("(")[0]):
        return ("operator", sig, "operator")
    mm = re.search(r"([A-Za-z_]\w*)\s*(?:<[^()]*?>)?\s*\(", h)   # first `Name(` / `Name<T>(`; skips tuple return types
    if mm and (eq == -1 or mm.start() < eq):
        paren = mm.start()
        before = h[:mm.end(1)]
        name = mm.group(1)
        if name == type_name or name == type_name.split(".")[-1]:
            return ("ctor", sig, name)
        if "operator" in before:
            return ("method", sig, name)
        return ("method", sig, name)
    if re.search(r"\bthis\s*\[", h):
        return ("indexer", sig, "this")
    if "event " in h:
        return ("event", sig, h.split()[-1])
    if kind_hint in ("open", "expr"):
        name = h.split()[-1]
        return ("property", sig, name)
    # stmt: field / const
    left = h.split("=")[0].strip()
    name = left.split()[-1] if left.split() else ""
    return ("field", sig, name)


def accessor_text(sig, body_events):
    """Build `{ get; set; }` suffix from the accessor body we skipped."""
    return ""


def extract_project(label, root: Path, relroot: Path, pkg):
    types: dict[str, TypeInfo] = {}
    files = sorted(root.rglob("*.cs"))
    for f in files:
        rel = f.relative_to(root)
        parts = rel.parts
        if any(p in SKIP_DIRS for p in parts[:-1]):
            continue
        if parts[0] == "Generated" and not any(g in str(rel) for g in GENERATED_OK):
            continue
        if f.name.endswith(".Designer.cs"):
            continue
        events = scan_file(f)
        rf = str(f.relative_to(relroot)).replace("\\", "/")
        scopes = []   # list of dict(kind, ti|None, skip)
        pending_prop = None
        for ev in events:
            typ = ev[0]
            h = ev[1]
            doc = ev[2]
            if typ == "close":
                if scopes:
                    sc = scopes.pop()
                    if sc["kind"] == "propbody" and sc["member"] is not None:
                        # accessors seen in the body text
                        acc = sc["acc"]
                        sc["member"].sig += " { " + acc.strip() + " }"
                    if sc["kind"] == "propbody":
                        pending_prop = sc["member"]
                continue
            depth = ev[3]
            in_skip = any(s["kind"] in ("body", "propbody") for s in scopes)
            if in_skip:
                # accessor names directly inside a property body: get / set / init
                if scopes and scopes[-1]["kind"] == "propbody" and typ in ("stmt", "expr", "open"):
                    hh = norm(h)
                    m = re.match(r"^((?:(?:public|private|protected|internal)\s+)*)(get|set|init)\b", hh)
                    if m:
                        scopes[-1]["acc"] += (m.group(1) + m.group(2)).strip() + "; "
                if typ == "open":
                    scopes.append({"kind": "body", "member": None, "acc": ""})
                continue
            # --- we're at namespace / type level ---
            if typ == "open":
                if h.startswith("namespace"):
                    scopes.append({"kind": "ns", "member": None})
                    continue
                if re.match(r"^extension\s*\(", h) and scopes and scopes[-1]["kind"] == "type" and scopes[-1]["ti"]:
                    # C# 14 `extension(Target) { ... }` block: members belong to the enclosing static class
                    scopes.append({"kind": "type", "ti": scopes[-1]["ti"], "ext": h[len("extension"):].strip()})
                    continue
                td = parse_type_head(h)
                if td and td["kind"] != "delegate":
                    full = (scopes[-1]["ti"].name + "." if scopes and scopes[-1]["kind"] == "type" and scopes[-1]["ti"] else "") + td["name"]
                    vis_ok = "public" in td["mods"] or "protected" in td["mods"]
                    outer_hidden = any(s["kind"] == "type" and s["ti"] is None for s in scopes)
                    if not vis_ok and not (scopes and scopes[-1]["kind"] == "type" and scopes[-1]["ti"] and scopes[-1]["ti"].kind == "interface"):
                        scopes.append({"kind": "type", "ti": None})
                        continue
                    if outer_hidden:
                        scopes.append({"kind": "type", "ti": None})
                        continue
                    key = full + (re.search(r"<.*>", td["display"]).group(0) if "<" in td["display"] else "")
                    ti = types.get(key)
                    summ, _ = clean_doc(doc)
                    if ti is None:
                        ti = TypeInfo(label, full, td["display"], td["kind"], td["mods"], td["bases"], summ, rf,
                                      constraints=td["constraints"], primary_ctor=td["primary"])
                        types[key] = ti
                    else:
                        if summ and not ti.summary:
                            ti.summary = summ
                        for b in td["bases"]:
                            if b not in ti.bases:
                                ti.bases.append(b)
                        if "static" in td["mods"]:
                            ti.mods = ti.mods or td["mods"]
                    ti.is_static = ti.is_static or "static" in td["mods"].split()
                    scopes.append({"kind": "type", "ti": ti})
                    continue
                # member with body
                cur = scopes[-1]["ti"] if scopes and scopes[-1]["kind"] == "type" else None
                if cur is None:
                    scopes.append({"kind": "body", "member": None, "acc": ""})
                    continue
                if cur.kind == "enum":
                    scopes.append({"kind": "body", "member": None, "acc": ""})
                    continue
                pm = parse_member(h, "open", cur.kind == "interface", cur.name)
                if pm and scopes[-1].get("ext"):
                    pm = (pm[0], scopes[-1]["ext"] + " " + pm[1], pm[2])
                if pm and pm[0] == "property":
                    summ, inh = clean_doc(doc)
                    mem = Member("property", pm[1], summ, inherit=inh)
                    cur.members.append(mem)
                    scopes.append({"kind": "propbody", "member": mem, "acc": ""})
                elif pm and pm[0] == "indexer":
                    summ, inh = clean_doc(doc)
                    mem = Member("indexer", pm[1], summ, inherit=inh)
                    cur.members.append(mem)
                    scopes.append({"kind": "propbody", "member": mem, "acc": ""})
                elif pm:
                    summ, inh = clean_doc(doc)
                    cur.members.append(Member(pm[0], pm[1], summ, inherit=inh))
                    scopes.append({"kind": "body", "member": None, "acc": ""})
                else:
                    scopes.append({"kind": "body", "member": None, "acc": ""})
                pending_prop = None
                continue
            if typ in ("stmt", "expr"):
                cur = scopes[-1]["ti"] if scopes and scopes[-1]["kind"] == "type" else None
                # property initializer after `}`:  "= value"
                if pending_prop is not None and typ == "stmt" and norm(h).startswith("="):
                    pending_prop.default = norm(h)[1:].strip()
                    pending_prop = None
                    continue
                pending_prop = None
                if cur is None:
                    # delegate at namespace level
                    td = parse_type_head(h) if h else None
                    if td and td["kind"] == "delegate" and ("public" in td["mods"]):
                        summ, _ = clean_doc(doc)
                        full = td["name"].split("(")[0].split()[-1]
                        types[full] = TypeInfo(label, full, td["name"], "delegate", td["mods"], [], summ, rf)
                    continue
                if cur.kind == "enum":
                    # enum members come as "A = 1, B, C" chunks terminated by '}' leftover
                    continue
                pm = parse_member(h, typ, cur.kind == "interface", cur.name)
                if pm is None:
                    continue
                kind, sig, name = pm
                if scopes[-1].get("ext"):
                    sig = scopes[-1]["ext"] + " " + sig
                summ, inh = clean_doc(doc)
                default = ""
                if typ == "expr":
                    if kind == "property":
                        sig += " { get; }"
                    pass
                if kind == "field" and "=" in sig:
                    sig, default = [x.strip() for x in sig.split("=", 1)]
                cur.members.append(Member(kind, sig, summ, default, inherit=inh))
            elif typ == "stmt" and not scopes:
                pass
        # enum members: re-scan with simple approach (enum bodies are leftovers on close)
    # enum values: separate pass using regex on enum bodies
    for f in files:
        rel = f.relative_to(root)
        if any(p in SKIP_DIRS for p in rel.parts[:-1]):
            continue
        txt = f.read_text(encoding="utf-8-sig", errors="replace")
        for em in re.finditer(r"(?P<doc>(?:[ \t]*///[^\n]*\n)*)[ \t]*(?:\[[^\]]*\]\s*)*public\s+enum\s+(?P<name>\w+)[^{]*\{(?P<body>.*?)\n\s*\}", txt, re.S):
            ti = types.get(em.group("name"))
            if ti is None or ti.kind != "enum" or ti.members:
                continue
            body = em.group("body")
            docbuf = []
            for line in body.split("\n"):
                s = line.strip()
                if s.startswith("///"):
                    docbuf.append(s[3:])
                    continue
                if not s or s.startswith("//") or s.startswith("#"):
                    continue
                if s.startswith("["):
                    # attribute-only lines (e.g. [Description("...")]) – ignore, but inline ones precede the value
                    s = re.sub(r"^(\[[^\]]*\]\s*)+", "", s)
                    if not s:
                        continue
                for part in split_top(s.rstrip(",")):
                    if not part:
                        continue
                    summ, _ = clean_doc(docbuf)
                    ti.members.append(Member("enumvalue", part, summ))
                    docbuf = []
    return types


# --------------------------------------------------------------------------
# Extension method resolution
# --------------------------------------------------------------------------
EXT_RE = re.compile(r"\bthis\s+(?:in\s+|ref\s+)?([A-Za-z_][\w\.]*(?:<[^()]*?>)?(?:\?)?)\s+\w+")


def collect_extensions(types):
    exts = []
    for ti in types.values():
        if ti.kind != "class" or not ti.is_static:
            continue
        for m in ti.members:
            if m.kind != "method":
                continue
            em = EXT_RE.search(m.sig)
            if not em:
                continue
            target = em.group(1).rstrip("?")
            tparams = re.search(r"\b\w+\s*<([^()]*?)>\s*\(", m.sig)
            tpl = [x.strip() for x in split_top(tparams.group(1))] if tparams else []
            base_target = re.sub(r"<.*>", "", target)
            targets = [base_target]
            if base_target in tpl:   # generic target: use constraints
                cm = re.search(r"where\s+" + re.escape(base_target) + r"\s*:\s*([^{]*?)(?=\swhere\s|$)", m.sig)
                targets = []
                if cm:
                    for c in split_top(cm.group(1)):
                        c = re.sub(r"<.*>", "", c.strip())
                        if c not in ("class", "struct", "notnull", "new()", "unmanaged"):
                            targets.append(c)
            exts.append((ti.name, targets, m))
    return exts


def type_closure(name, by_name, seen=None):
    """name + all transitive bases/interfaces (generic args stripped)."""
    seen = seen if seen is not None else set()
    if name in seen:
        return seen
    seen.add(name)
    ti = by_name.get(name)
    if ti:
        for b in ti.bases:
            type_closure(re.sub(r"<.*>", "", b), by_name, seen)
    return seen


def resolve_inherit(types_by_name):
    def lookup(ti, mname, depth=0):
        if depth > 6:
            return ""
        for b in ti.bases:
            bt = types_by_name.get(re.sub(r"<.*>", "", b))
            if not bt:
                continue
            for m in bt.members:
                if member_name(m) == mname and m.summary:
                    return m.summary
            r = lookup(bt, mname, depth + 1)
            if r:
                return r
        return ""
    for ti in types_by_name.values():
        for m in ti.members:
            if (m.inherit or not m.summary) and m.kind in ("property", "method", "indexer", "event"):
                r = lookup(ti, member_name(m))
                if r:
                    m.summary = r


def member_name(m):
    s = m.sig
    paren = s.find("(")
    head = s[:paren] if paren != -1 else s.split("{")[0]
    head = head.strip().split()
    if not head:
        return ""
    nm = head[-1]
    return re.sub(r"<.*>$", "", nm)


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------
def group_for(ti: TypeInfo):
    p = ti.file.replace("\\", "/")
    proj = ti.project
    if proj == "core":
        sub = p.split("src/Spectre.Console/", 1)[-1].split("/")
        if sub[0] == "Widgets":
            if len(sub) > 2:
                return f"widgets/{sub[1]}"
            stem = Path(sub[1]).stem
            top = ti.name.split(".")[0]
            return f"widgets/{MERGE.get(top, stem if stem == top else MERGE.get(stem, stem))}"
        if sub[0] == "Prompts":
            return "prompts"
        if sub[0] == "Live":
            if len(sub) > 2:
                return f"live-{sub[1].lower()}"
            return "live"
        if sub[0] == "Rendering":
            return "rendering"
        if sub[0] == "Enrichment":
            return "console"
        if sub[0] == "Generated":
            return "console"
        if sub[0] == "Extensions":
            return "console"
        return "console"
    return proj


def ext_display(m):
    """`T Border<T>(this T obj, BoxBorder b) where ...` -> `Border(BoxBorder b)` fluent form."""
    sig = re.sub(r"\s+where\s.*$", "", m.sig)
    sig = re.sub(r"^static\s+", "", sig)
    pm = re.match(r"^(.*\s)?(\w+)(<[\w,\s?]*>)?\((.*)\)\s*$", sig, re.S)
    if not pm:
        return sig
    ret, name, tp, params = (pm.group(1) or "").strip(), pm.group(2), pm.group(3) or "", pm.group(4)
    ps = split_top(params)
    rest = ", ".join(ps[1:])
    return f"{name}{tp}({rest}) -> {ret}" if ret else f"{name}{tp}({rest})"


def compact_names(ms):
    seen, names = set(), []
    for m in ms:
        n = member_name(m)
        if n not in seen:
            seen.add(n)
            names.append(n)
    return ", ".join(f"`{n}`" for n in names)


def render_type(ti: TypeInfo, ext_for, out, shared):
    full = ti.name
    head = f"{ti.mods + ' ' if ti.mods else ''}{ti.kind} {full if '.' in full else ti.display}"
    if "." in full and "<" in ti.display:
        head = f"{ti.mods + ' ' if ti.mods else ''}{ti.kind} {full.rsplit('.', 1)[0]}.{ti.display}"
    if ti.primary_ctor:
        head += ti.primary_ctor
    if ti.bases:
        head += " : " + ", ".join(ti.bases)
    if ti.constraints:
        head += " " + ti.constraints
    out.append(f"## `{head}`\n")
    out.append(f"*{ti.project}* · `{ti.file}`\n")
    if ti.summary:
        out.append(ti.summary + "\n")
    groups = [("ctor", "Constructors"), ("property", "Properties"), ("indexer", "Indexers"), ("operator", "Operators / conversions"), ("field", "Fields / constants"),
              ("method", "Methods"), ("event", "Events"), ("enumvalue", "Values")]
    for kind, title in groups:
        ms = [m for m in ti.members if m.kind == kind]
        if not ms:
            continue
        out.append(f"**{title}**\n")
        if kind in ("property", "field") and len(ms) > 40:
            # big generated tables (Color, Emoji.Known, Spinner.Known ...): names only
            sample = ms[0].sig
            out.append(f"{len(ms)} members like `{sample}`: " + compact_names(ms))
        elif kind == "enumvalue":
            for m in ms:
                out.append(f"- `{m.sig}`" + (f" — {m.summary}" if m.summary else ""))
        else:
            for m in ms:
                line = f"- `{m.sig}`"
                if m.default:
                    line += f" = `{m.default}`"
                if m.summary:
                    line += f" — {m.summary}"
                out.append(line)
        out.append("")
    own, via = ext_for(ti)
    if own:
        out.append("**Extension methods on this type** (call as `x.Method(...)`)\n")
        for owner, m in own:
            out.append(f"- `{ext_display(m)}`" + (f" — {m.summary}" if m.summary else ""))
        out.append("")
    if via:
        out.append("**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)\n")
        for target, ms in via.items():
            out.append(f"- via `{target}`: " + compact_names(ms))
            shared.setdefault(target, {})
            for owner, m in ms_pairs(ms):
                shared[target][ext_display(m)] = m.summary
        out.append("")


def ms_pairs(ms):
    return [(None, m) for m in ms]


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    repos = {"core": Path(sys.argv[1]).resolve(), "cli": Path(sys.argv[2]).resolve()}
    writer = Path(sys.argv[3]).resolve()
    refs = writer / "references"
    apidir = refs / "api"
    apidir.mkdir(parents=True, exist_ok=True)
    for child in apidir.iterdir():      # clear contents but keep the dir (a shell may be sitting in it on Windows)
        shutil.rmtree(child) if child.is_dir() else child.unlink()

    all_types: dict[str, TypeInfo] = {}
    per_project = {}
    for label, rk, rel, pkg in PROJECTS:
        root = repos[rk] / rel
        if not root.exists():
            print(f"!! missing project {rel}")
            continue
        t = extract_project(label, root, repos[rk], pkg)
        per_project[label] = t
        for k, v in t.items():
            all_types.setdefault(k, v)
    by_name = {}
    for _ti in all_types.values():
        by_name.setdefault(_ti.name, _ti)
    resolve_inherit(by_name)

    exts = collect_extensions(all_types)
    ext_classes = {o for o, _, _ in exts}

    closure_cache = {}

    def ext_for(ti):
        if ti.name not in closure_cache:
            closure_cache[ti.name] = type_closure(ti.name, by_name)
        cl = closure_cache[ti.name]
        own, via = [], {}
        for owner, targets, m in exts:
            hit = [t for t in targets if t in cl]
            if not hit:
                continue
            if ti.name in hit or ti.name.split(".")[-1] in hit:
                own.append((owner, m))
            else:
                via.setdefault(hit[0], []).append(m)
        return own, via

    shared = {}

    # group
    groups = defaultdict(list)
    for ti in all_types.values():
        if "." in ti.name and ti.name.split(".")[0] in by_name:
            continue  # nested rendered with outer? keep simple: emit nested separately below
        if ti.name in ext_classes and not [m for m in ti.members if "this " not in m.sig and m.kind == "method"]:
            groups["extension-classes"].append(ti)
            continue
        groups[group_for(ti)].append(ti)
    # nested types
    for ti in all_types.values():
        if "." in ti.name and ti.name.split(".")[0] in by_name:
            groups[group_for(ti)].append(ti)

    counts = {}
    index_rows = []
    for g, tis in sorted(groups.items()):
        if g == "extension-classes":
            continue
        tis.sort(key=lambda t: (t.kind == "enum", t.name))
        out = [f"# {g} — API (generated from source)\n"]
        for ti in tis:
            render_type(ti, ext_for, out, shared)
            index_rows.append((ti.name, ti.kind, g, ti.project, ti.summary))
        path = apidir / f"{g}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
        counts[g] = len(tis)

    # extension-class catalogue
    ext_out = ["# Extension classes (generated from source)\n",
               "Each extension method is listed on the *target type's* page under \"Extension methods that apply\"; "
               "this file lists the static classes that hold them.\n"]
    for ti in sorted(groups.get("extension-classes", []), key=lambda t: t.name):
        n = sum(1 for m in ti.members if m.kind == "method")
        ext_out.append(f"- `{ti.name}` ({ti.project}, {n} methods) — {ti.summary}")
    (apidir / "_extension-classes.md").write_text("\n".join(ext_out) + "\n", encoding="utf-8")

    # index
    index_rows.sort(key=lambda r: r[0].lower())
    idx = ["# Public type index (generated from source)\n",
           "Type → file under `references/api/`. Open the file for members and applicable extension methods.\n",
           "| Type | Kind | File | Package | Summary |", "|---|---|---|---|---|"]
    pkgs = {l: p for l, _, _, p in PROJECTS}
    for name, kind, g, proj, summ in index_rows:
        idx.append(f"| `{name}` | {kind} | `api/{g}.md` | {pkgs[proj]} | {summ[:110].replace('|', '/')} |")
    (apidir / "_index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    sh = ["# Shared extension methods (generated from source)\n",
          "Extension methods that apply to every type implementing/deriving from the heading's interface or base. "
          "`-> T` means the call returns the same widget so calls chain.\n"]
    for target in sorted(shared):
        sh.append(f"## via `{target}`\n")
        for sig, summ in sorted(shared[target].items()):
            sh.append(f"- `{sig}`" + (f" — {summ}" if summ else ""))
        sh.append("")
    (apidir / "_shared-extensions.md").write_text("\n".join(sh) + "\n", encoding="utf-8")

    # ---- data-driven references ----
    core = repos["core"] / "src"
    write_colors(core, refs)
    write_spinners(core, refs)
    write_emoji(core, refs)

    total = len(all_types)
    nmem = sum(len(t.members) for t in all_types.values())
    nexts = len(exts)
    print(f"types: {total}  members: {nmem}  extension methods: {nexts}")
    for l, t in per_project.items():
        print(f"  {l}: {len(t)} types, {sum(len(x.members) for x in t.values())} members")
    print("files:", len(list(apidir.rglob('*.md'))))


def write_colors(core: Path, refs: Path):
    p = core / "Spectre.Console.Ansi/Data/colors.json"
    if not p.exists():
        print("!! colors.json not found")
        return
    data = json.loads(p.read_text(encoding="utf-8-sig"))
    seen = defaultdict(int)
    rows = []
    for c in data:
        seen[c["name"]] += 1
    dup = {k for k, v in seen.items() if v > 1}
    idx = defaultdict(int)
    for c in data:
        nm = c["name"]
        if nm in dup:
            idx[nm] += 1
            suffix = "" if idx[nm] == 1 else str(idx[nm] - 1)
            nm_code = nm + suffix
        else:
            nm_code = nm
        rows.append((c["number"], nm, nm_code, c["hex"]))
    out = ["# Colors (generated from `Spectre.Console.Ansi/Data/colors.json`)\n",
           "The 256-color palette. `Color.<Name>` and markup names (`[red]`, `[darkorange3]`) come from this table. "
           "When a name repeats in the palette, the generated member gets a numeric suffix for the later entries "
           "(`Color.Grey`, `Color.Grey1`…); the markup parser resolves the first entry for a bare name. "
           "Verify a suffixed name against `api/ansi.md` (`Color` members) before using it.\n",
           "Numbers 0–15 are the standard 16 ANSI colors. `Color.Default` means \"terminal default\".\n",
           "| # | Name | Hex |", "|---|---|---|"]
    for num, nm, code, hx in rows:
        label = nm if nm == code else f"{nm} (`Color.{code}`)"
        out.append(f"| {num} | {label} | {hx} |")
    (refs / "colors.md").write_text("\n".join(out) + "\n", encoding="utf-8")


def write_spinners(core: Path, refs: Path):
    out = ["# Spinners (generated from `Spectre.Console/Data/spinners_*.json`)\n",
           "Use as `Spinner.Known.<Name>` (e.g. `.Spinner(Spinner.Known.Dots)`). `Default` and `Ascii` come from "
           "`spinners_default.json`; the rest are from sindresorhus/cli-spinners. `unicode: true` means the spinner "
           "needs a Unicode-capable terminal (Spectre falls back to `Spinner.Known.Ascii` otherwise).\n",
           "| Name | Interval (ms) | Unicode | Frames (first 6) |", "|---|---|---|---|"]
    for fn in ("spinners_default.json", "spinners_sindresorhus.json"):
        p = core / "Spectre.Console/Data" / fn
        if not p.exists():
            print("!! missing", fn)
            continue
        data = json.loads(p.read_text(encoding="utf-8-sig"))
        for name, v in data.items():
            frames = " ".join(v["frames"][:6]).replace("|", "\\|")
            out.append(f"| {name} | {v['interval']} | {v.get('unicode', True)} | `{frames}` |")
    (refs / "spinners.md").write_text("\n".join(out) + "\n", encoding="utf-8")


def write_emoji(core: Path, refs: Path):
    g = list((core / "Spectre.Console/Generated").glob("**/Emoji.Generated.g.cs"))
    if not g:
        print("!! Emoji.Generated.g.cs not found (build the project with EmitCompilerGeneratedFiles to produce it)")
        return
    txt = g[0].read_text(encoding="utf-8-sig")
    names = re.findall(r'\{\s*"([a-z0-9_\-\+\'\.]+)",\s*Emoji\.Known\.', txt)
    out = ["# Emoji shortcodes (generated from source)\n",
           f"{len(names)} shortcodes. Use as `:name:` in markup (`[green]:check_mark_button:[/]`), "
           "`Emoji.Replace(\"...\")`, or the constant `Emoji.Known.<PascalCaseName>`. Case-insensitive.\n",
           ", ".join(names)]
    (refs / "emoji-shortcodes.md").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
