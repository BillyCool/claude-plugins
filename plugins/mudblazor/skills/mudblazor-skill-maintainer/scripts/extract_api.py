#!/usr/bin/env python3
"""Extract the MudBlazor component API from a MudBlazor source checkout.

Generates the machine-verified reference files consumed by the sibling
`mudblazor-ui-writer` skill:

  references/api/<Folder>.md   one file per component folder (parameters,
                               types, defaults, doc summaries, inheritance)
  references/api/_base-classes.md   shared base-class parameters
  references/components-index.md    one-line index of every component
  references/enums.md               every public enum + values + css names

Usage:
  python extract_api.py <path-to-mudblazor-checkout> <path-to-writer-skill>

Example:
  python extract_api.py ../mudblazor ../../mudblazor-ui-writer

The script is intentionally regex-based (no Roslyn dependency) and tuned to
MudBlazor's very consistent code style. If output looks truncated or garbled
after a new release, inspect the source file that broke the pattern and adjust.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------- doc cleanup

SEE_CREF = re.compile(r'<(?:see|seealso)\s+cref="(?:[A-Z]:)?([^"]+)"\s*/?>')
SEE_HREF = re.compile(r'<see\s+href="[^"]*">([^<]*)</see>')
SEE_LANG = re.compile(r'<see\s+langword="([^"]+)"\s*/>')
TAG_C = re.compile(r'</?c>')
TAG_PARA = re.compile(r'</?(?:para|remarks|summary|returns|b|i|em|strong)>')
TAG_BR = re.compile(r'<br\s*/?>')
TAG_PARAMREF = re.compile(r'<(?:param|type)ref\s+name="([^"]+)"\s*/>')
TAG_LIST = re.compile(r'</?(?:list|item|description|term)[^>]*>')
WS = re.compile(r'\s+')


def clean_doc(text: str) -> str:
    """Turn an XML doc fragment into one readable line."""
    text = SEE_CREF.sub(lambda m: '`%s`' % m.group(1).split('.')[-1].split('(')[0], text)
    text = SEE_HREF.sub(r'\1', text)
    text = SEE_LANG.sub(r'`\1`', text)
    text = TAG_PARAMREF.sub(r'`\1`', text)
    text = TAG_C.sub('`', text)
    text = TAG_BR.sub(' ', text)
    text = TAG_PARA.sub(' ', text)
    text = TAG_LIST.sub(' ', text)
    return WS.sub(' ', text).strip()


def doc_block(lines: list[str]) -> tuple[str, str]:
    """Split accumulated /// lines into (summary, remarks) single lines."""
    joined = '\n'.join(line.lstrip().lstrip('/').strip() for line in lines)
    def grab(tag: str) -> str:
        m = re.search(r'<%s>(.*?)</%s>' % (tag, tag), joined, re.S)
        return clean_doc(m.group(1)) if m else ''
    return grab('summary'), grab('remarks')


# ------------------------------------------------------------------- parsing

CLASS_RE = re.compile(
    r'^\s*(public\s+)?((?:abstract|sealed|partial|static)\s+)*(class|record)\s+'
    r'(\w+)(<[^>{:]*>)?\s*(?::\s*([^{\n]+?))?\s*(?:\{|$|where)')
ENUM_RE = re.compile(r'^\s*public\s+enum\s+(\w+)')
PARAM_ATTR_RE = re.compile(r'^\s*\[(Parameter|CascadingParameter)\b')
PROP_RE = re.compile(
    r'^\s*public\s+(?:override\s+|virtual\s+|new\s+|required\s+)*'
    r'([\w?<>,.\[\]() ]+?)\s+(\w+)\s*(\{.*|=>.*)$')
DEFAULT_RE = re.compile(r'\}\s*=\s*(.+?);\s*$')
DESC_ATTR_RE = re.compile(r'^\s*\[Description\("([^"]*)"\)\]')
ENUM_MEMBER_RE = re.compile(r'^\s*(\w+)\s*(?:=\s*[^,]+)?,?\s*$')
OBSOLETE_RE = re.compile(r'^\s*\[Obsolete')


@dataclass
class Param:
    name: str
    type: str
    default: str
    summary: str
    remarks: str
    cascading: bool = False
    obsolete: bool = False


@dataclass
class Cls:
    name: str
    generics: str
    bases: str
    summary: str
    remarks: str
    params: list[Param] = field(default_factory=list)

    @property
    def display(self) -> str:
        generics = re.sub(r'\[[^\]]*\]\s*', '', self.generics or '')
        return self.name + generics

    @property
    def first_base(self) -> str:
        """First base type, respecting commas inside generic arguments."""
        depth, out = 0, []
        for ch in self.bases:
            if ch == '<':
                depth += 1
            elif ch == '>':
                depth -= 1
            elif ch == ',' and depth == 0:
                break
            out.append(ch)
        return ''.join(out).strip()


def parse_razor(path: Path) -> Cls:
    """Parse a razor-only component (no .razor.cs code-behind)."""
    text = path.read_text(encoding='utf-8-sig', errors='replace')
    m = re.search(r'^@inherits\s+(\S+)', text, re.M)
    cls = Cls(path.stem, '', m.group(1) if m else 'ComponentBase', '', '')
    docs: list[str] = []
    pending = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith('///'):
            docs.append(line)
        elif PARAM_ATTR_RE.match(line):
            pending = True
        elif pending:
            pm = PROP_RE.match(line)
            if pm:
                default = ''
                dm = DEFAULT_RE.search(line)
                if dm:
                    default = dm.group(1).strip()
                summary, remarks = doc_block(docs)
                cls.params.append(Param(pm.group(2), pm.group(1).strip(),
                                        default, summary, remarks))
                docs, pending = [], False
        elif s and not s.startswith(('[', '//')):
            docs = []
    return cls


def parse_cs(path: Path) -> tuple[list[Cls], list[dict]]:
    """Return (classes-with-parameters, enums) found in one .cs file."""
    classes: list[Cls] = []
    enums: list[dict] = []
    cur: Cls | None = None
    cur_enum: dict | None = None
    docs: list[str] = []
    pending_attr: str | None = None       # Parameter | CascadingParameter
    pending_obsolete = False
    pending_desc: str | None = None

    for raw in path.read_text(encoding='utf-8-sig', errors='replace').splitlines():
        line = raw.rstrip()
        s = line.strip()

        if s.startswith('///'):
            docs.append(line)
            continue

        m = CLASS_RE.match(line)
        if m and 'internal' not in s and 'private' not in s and 'protected' not in s:
            # razor code-behind partials may omit `public` — accept public or partial
            if m.group(1) or (m.group(2) and 'partial' in m.group(2)) or \
                    (line.lstrip().startswith(('partial', 'abstract', 'sealed'))
                     and 'partial' in line):
                summary, remarks = doc_block(docs)
                bases = (m.group(6) or '').strip().rstrip(',')
                cur = Cls(m.group(4), m.group(5) or '', bases, summary, remarks)
                classes.append(cur)
                cur_enum = None
                docs, pending_attr, pending_obsolete, pending_desc = [], None, False, None
                continue

        m = ENUM_RE.match(line)
        if m:
            summary, _ = doc_block(docs)
            cur_enum = {'name': m.group(1), 'summary': summary, 'members': []}
            enums.append(cur_enum)
            cur = None
            docs, pending_attr, pending_obsolete, pending_desc = [], None, False, None
            continue

        if s.startswith('['):
            if PARAM_ATTR_RE.match(line):
                pending_attr = 'CascadingParameter' if 'Cascading' in s else 'Parameter'
            elif OBSOLETE_RE.match(line):
                pending_obsolete = True
            dm = DESC_ATTR_RE.match(line)
            if dm:
                pending_desc = dm.group(1)
            continue

        if cur_enum is not None:
            m = ENUM_MEMBER_RE.match(line)
            if m and s and not s.startswith(('{', '}', '//')):
                summary, _ = doc_block(docs)
                cur_enum['members'].append(
                    {'name': m.group(1), 'css': pending_desc, 'summary': summary})
                docs, pending_desc, pending_obsolete = [], None, False
            if s.startswith('}'):
                cur_enum = None
            continue

        if pending_attr and cur is not None:
            m = PROP_RE.match(line)
            if m:
                default = ''
                dm = DEFAULT_RE.search(line)
                if dm:
                    default = dm.group(1).strip()
                summary, remarks = doc_block(docs)
                if not default:
                    rd = re.search(r'Defaults to (`?[^.]+`?)\.', remarks)
                    if rd:
                        default = rd.group(1).strip('` ')
                cur.params.append(Param(
                    m.group(2), m.group(1).strip(), default, summary, remarks,
                    cascading=(pending_attr == 'CascadingParameter'),
                    obsolete=pending_obsolete))
                docs, pending_attr, pending_obsolete = [], None, False
            elif s and not s.startswith('//'):
                # attribute applied to something we don't track (field, private)
                if 'private' in s or 'internal' in s or 'protected' in s:
                    docs, pending_attr, pending_obsolete = [], None, False
            continue

        if s and not s.startswith(('//', '[')):
            docs = []
            pending_obsolete = False

    return classes, enums


# ------------------------------------------------------------------ emitting

def esc(text: str) -> str:
    return text.replace('|', '\\|')


def param_table(params: list[Param]) -> list[str]:
    out = ['| Parameter | Type | Default | Description |',
           '|---|---|---|---|']
    for p in params:
        if p.cascading:
            continue
        desc = p.summary
        if p.obsolete:
            desc = '**[Obsolete]** ' + desc
        if p.remarks and p.remarks != p.summary:
            desc = (desc + ' ' + p.remarks).strip()
        out.append('| `%s` | `%s` | %s | %s |' % (
            p.name, esc(p.type), '`%s`' % esc(p.default) if p.default else '–',
            esc(desc)))
    return out


def emit_folder(folder: str, classes: list[Cls], out_dir: Path) -> None:
    lines = ['# %s components — API (generated from source)' % folder, '']
    for c in classes:
        base = c.first_base
        head = c.display + (' : %s' % base if base else '')
        lines.append('## %s' % head)
        if c.summary:
            lines.append('')
            lines.append(c.summary)
        if c.remarks and c.remarks != c.summary:
            lines.append('')
            lines.append('*%s*' % c.remarks)
        own = [p for p in c.params if not p.cascading]
        lines.append('')
        if own:
            lines.extend(param_table(own))
        else:
            lines.append('_No own parameters%s._' % (
                ' — see base class `%s`' % base if base else ''))
        lines.append('')
    (out_dir / ('%s.md' % folder)).write_text('\n'.join(lines), encoding='utf-8')


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src_root = Path(sys.argv[1]) / 'src' / 'MudBlazor'
    writer = Path(sys.argv[2]) / 'references'
    api_dir = writer / 'api'
    api_dir.mkdir(parents=True, exist_ok=True)

    all_enums: list[dict] = []
    index: list[tuple[str, str, str]] = []   # (component, folder, summary)

    # ---- base classes -------------------------------------------------
    base_classes: list[Cls] = []
    for f in sorted((src_root / 'Base').glob('*.cs')):
        cs, en = parse_cs(f)
        base_classes.extend(cs)
        all_enums.extend(en)

    lines = ['# Shared base classes — API (generated from source)', '',
             'Every `Mud*` component ultimately inherits `MudComponentBase`, so all',
             'components accept these parameters in addition to their own.', '']
    for c in base_classes:
        base = c.first_base
        lines.append('## %s%s' % (c.display, ' : %s' % base if base else ''))
        if c.summary:
            lines += ['', c.summary]
        lines.append('')
        own = [p for p in c.params if not p.cascading]
        lines += param_table(own) if own else ['_No own parameters._']
        lines.append('')
    (api_dir / '_base-classes.md').write_text('\n'.join(lines), encoding='utf-8')

    # ---- components ---------------------------------------------------
    comp_root = src_root / 'Components'
    for folder in sorted(p for p in comp_root.iterdir() if p.is_dir()):
        classes: list[Cls] = []
        for f in sorted(folder.rglob('*.cs')):
            cs, en = parse_cs(f)
            classes.extend(cs)
            all_enums.extend(en)
        for f in sorted(folder.rglob('Mud*.razor')):
            if not f.with_suffix('.razor.cs').exists():
                classes.append(parse_razor(f))
        keep = [c for c in classes if c.params or c.name.startswith('Mud')]
        if not keep:
            continue
        emit_folder(folder.name, keep, api_dir)
        for c in keep:
            if c.name.startswith('Mud'):
                index.append((c.display, folder.name, c.summary))

    # ---- index --------------------------------------------------------
    lines = ['# MudBlazor component index (generated from source)', '',
             'Component → API reference file `references/api/<Folder>.md`.', '',
             '| Component | Folder | Purpose |', '|---|---|---|']
    for name, folder, summary in sorted(index):
        lines.append('| `%s` | %s | %s |' % (name, folder, esc(summary)))
    (writer / 'components-index.md').write_text('\n'.join(lines), encoding='utf-8')

    # ---- enums --------------------------------------------------------
    for sub in ('Enums', 'Services', 'Utilities'):
        for f in sorted((src_root / sub).rglob('*.cs')):
            _, en = parse_cs(f)
            all_enums.extend(en)
    seen: set[str] = set()
    lines = ['# MudBlazor enums (generated from source)', '',
             'Every public enum with its values. "CSS name" is the string emitted',
             'into CSS classes (the `[Description]` attribute value).', '']
    for e in sorted(all_enums, key=lambda e: e['name']):
        if e['name'] in seen or not e['members']:
            continue
        seen.add(e['name'])
        lines.append('## %s' % e['name'])
        if e['summary']:
            lines += ['', e['summary']]
        lines += ['', '| Value | CSS name | Meaning |', '|---|---|---|']
        for m in e['members']:
            lines.append('| `%s` | %s | %s |' % (
                m['name'], '`%s`' % m['css'] if m['css'] else '–',
                esc(m['summary'])))
        lines.append('')
    (writer / 'enums.md').write_text('\n'.join(lines), encoding='utf-8')

    print('classes(base)=%d folders indexed=%d components=%d enums=%d'
          % (len(base_classes), len(set(i[1] for i in index)), len(index),
             len(seen)))


if __name__ == '__main__':
    main()
