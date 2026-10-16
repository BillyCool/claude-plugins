#!/usr/bin/env python3
"""Rebuild the `aimp-plugin-developer` skill's references from an AIMP SDK drop.

Everything the writer skill documents comes from two places inside the SDK:

  Help/AIMP-en.chm   the official API reference (interfaces, messages,
                     properties, "Minimal Version" / multi-threading notes)
  Sources/           the actual C++ headers and Delphi units

This script decompiles the CHM, converts every topic to Markdown, and lays the
topics out using the help file's own table of contents (TOC.hhc) as the
organising spine — so the reference tree tracks whatever structure the SDK
author ships, not a hand-maintained list. The SDK's own sources and demos are
copied in verbatim next to the prose, so signatures can be grepped exactly
rather than recalled.

Usage:
  python extract_sdk.py --sdk <path-to-sdk> --out ../../aimp-plugin-developer
  python extract_sdk.py --sdk ... --out ... --chm-html <already-decompiled-dir>

Decompiling needs `hh.exe` (Windows). On other platforms pass --chm-html with
a directory produced by `7z x AIMP-en.chm` or `chmlib`'s `extract_chmLib`.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chm2md
import rtf2md

# A group whose combined Markdown exceeds this is split into one file per
# sub-group; a sub-group over the same size becomes one file per topic.
SPLIT_BYTES = 60_000

# Source-tree files worth vendoring (skip compiled resources and IDE metadata).
SOURCE_SUFFIXES = {'.h', '.cpp', '.pas', '.inc', '.dpr', '.sh', '.lng', '.dfm'}

RTF_DOCS = {
    'AIMP Addon Package': 'packaging.md',
    'Integration of CLI-encoders': 'cli-encoders.md',
    'AIMP Playlist File Format v4': 'playlist-file-format.md',
    'AIMP Extensions for XSPF': 'xspf-extensions.md',
}


# --------------------------------------------------------------------- TOC

class Node:
    __slots__ = ('name', 'local', 'children', 'parent')

    def __init__(self, name: str, local: str = '', parent=None):
        self.name = name
        self.local = local
        self.children: list = []
        self.parent = parent

    def leaves(self):
        """Every node that has a topic page, including ones with children."""
        if self.local:
            yield self
        for c in self.children:
            yield from c.leaves()

    def find(self, name: str):
        if self.name == name:
            return self
        for c in self.children:
            hit = c.find(name)
            if hit:
                return hit
        return None


ENTRY = re.compile(
    r'<LI>\s*<OBJECT[^>]*>(.*?)</OBJECT>|<UL>|</UL>',
    re.I | re.S)
PARAM = re.compile(r'<PARAM\s+name="([^"]+)"\s+value="([^"]*)"', re.I)


def parse_toc(path: Path) -> Node:
    text = path.read_bytes().decode('windows-1250', errors='replace')
    root = Node('root')
    cur = root
    last = root
    for m in ENTRY.finditer(text):
        token = m.group(0)
        if token.upper() == '<UL>':
            cur = last
            continue
        if token.upper() == '</UL>':
            cur = cur.parent or root
            continue
        params = dict(PARAM.findall(m.group(1) or ''))
        name = params.get('Name', '').strip()
        local = urllib.parse.unquote(params.get('Local', '')).strip()
        node = Node(name, local, cur)
        cur.children.append(node)
        last = node
    return root


# ------------------------------------------------------------- topic render

def shift_headings(body: str, by: int) -> str:
    return re.sub(r'^(#{1,5}) ', lambda m: '#' * (len(m.group(1)) + by) + ' ',
                  body, flags=re.M)


def render_topic(node: Node, html_dir: Path, level: int) -> tuple:
    """Return (markdown, first_sentence) for one TOC leaf."""
    path = html_dir / node.local
    if not path.exists():
        return '', ''
    title, body = chm2md.convert(path)
    heading = node.name or title
    # Keep the help topic's own id alongside the TOC label when they differ,
    # so a name seen in the CHM still finds its page here. Auto-generated
    # container pages ("group_autocontent (3)") have no useful id.
    if title and title != heading and not path.stem.startswith('group_autocontent'):
        heading = '%s (%s)' % (heading, title)
    summary = first_sentence(body)
    md = '%s %s\n\n%s\n' % ('#' * level, heading, shift_headings(body, level - 1))
    return md, summary


SENT = re.compile(r'^(.+?[.!?])(?:\s|$)', re.S)


def first_sentence(body: str) -> str:
    """One-line gist of a topic, for the index."""
    fallback = ''
    for block in body.split('\n\n'):
        block = re.sub(r'\s+', ' ', block.strip())
        if not block or block.startswith('#'):
            continue
        if block.startswith('-'):
            # Topics with no prose at all (most AIMP_MSG_PROPERTY_* pages) —
            # the first parameter note is the only description there is.
            fallback = fallback or re.sub(r'[`*]', '', block).lstrip('- ')
            continue
        m = SENT.match(block)
        return (m.group(1) if m else block)[:200]
    return fallback[:200]


def slug(name: str) -> str:
    s = re.sub(r'[^A-Za-z0-9]+', '-', name).strip('-').lower()
    return s or 'misc'


# ------------------------------------------------------------------- writer

class Emitter:
    def __init__(self, html_dir: Path, out: Path):
        self.html_dir = html_dir
        self.out = out
        self.index: list = []       # (topic name, relative path, summary)
        self.files: list = []       # (relative path, bytes)

    def write(self, rel: str, text: str) -> None:
        path = self.out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'
        path.write_text(text, encoding='utf-8', newline='\n')
        self.files.append((rel, len(text)))

    def render_group(self, node: Node, level: int, rel: str) -> str:
        """Depth-first render of a TOC subtree into one Markdown string."""
        parts = []
        if node.local and (self.html_dir / node.local).exists():
            md, summary = render_topic(node, self.html_dir, level)
            if md.strip():
                parts.append(md)
                self.index.append((node.name, rel, summary))
        elif node.name and node.children:
            parts.append('%s %s\n' % ('#' * level, node.name))
        for child in node.children:
            parts.append(self.render_group(child, level + 1, rel))
        return '\n'.join(p for p in parts if p.strip())

    def size_of(self, node: Node) -> int:
        probe = Emitter(self.html_dir, self.out)
        return len(probe.render_group(node, 1, ''))

    def emit_chapter(self, node: Node, rel_dir: str) -> list:
        """Write a chapter, splitting it when it gets too big to read whole.

        Returns [(title, relative path)] for the pieces written.
        """
        name = slug(node.name)
        rel = '%s/%s.md' % (rel_dir, name)
        if self.size_of(node) <= SPLIT_BYTES or not node.children:
            body = self.render_group(node, 1, rel)
            self.write(rel, body)
            return [(node.name, rel)]

        # Too big: direct leaves stay in the chapter file, each sub-group
        # becomes its own file (or its own directory, one file per topic).
        written: list = []
        own_leaves = [c for c in node.children if c.local and not c.children]
        groups = [c for c in node.children if c.children]

        pieces: list = []
        for group in groups:
            gname = '%s-%s' % (name, slug(group.name))
            if self.size_of(group) <= SPLIT_BYTES:
                grel = '%s/%s.md' % (rel_dir, gname)
                self.write(grel, self.render_group(group, 1, grel))
                pieces.append((group.name, grel))
                written.append((group.name, grel))
                continue
            # One file per entry in the group, each carrying its own subtree
            # (e.g. IAIMPUITreeList keeps its node/column/event interfaces).
            for entry in group.children:
                lrel = '%s/%s/%s.md' % (rel_dir, gname, slug(entry.name))
                body = self.render_group(entry, 1, lrel)
                if not body.strip():
                    continue
                self.write(lrel, body)
                written.append((entry.name, lrel))
            pieces.append((group.name, '%s/%s/' % (rel_dir, gname)))

        head = ['# %s\n' % node.name]
        for leaf in own_leaves:
            md, summary = render_topic(leaf, self.html_dir, 2)
            if md.strip():
                head.append(md)
                self.index.append((leaf.name, rel, summary))
        head.append('\n## More in this chapter\n')
        for title, where in pieces:
            head.append('- **%s** — `%s`' % (title, where))
        self.write(rel, '\n'.join(head))
        written.insert(0, (node.name, rel))
        return written


# -------------------------------------------------------------------- main

def decompile_chm(chm: Path, dest: Path) -> Path:
    dest.mkdir(parents=True, exist_ok=True)
    local = dest / chm.name
    shutil.copy2(chm, local)
    subprocess.run(['hh.exe', '-decompile', str(dest), str(local)], check=False)
    if not (dest / 'TOC.hhc').exists():
        raise SystemExit(
            'hh.exe did not produce TOC.hhc in %s — decompile the CHM manually '
            'and pass --chm-html' % dest)
    return dest


def copy_sources(sdk: Path, out: Path) -> int:
    count = 0
    for sub in ('Sources', 'Demos'):
        src = sdk / sub
        if not src.is_dir():
            continue
        dst = out / 'references' / 'sdk' / sub
        if dst.exists():
            shutil.rmtree(dst)
        for path in sorted(src.rglob('*')):
            if not path.is_file() or path.suffix.lower() not in SOURCE_SUFFIXES:
                continue
            target = dst / path.relative_to(src)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            count += 1
    return count


def sdk_version(sdk: Path) -> str:
    header = sdk / 'Sources' / 'Cpp' / 'apiPlugin.h'
    if header.exists():
        m = re.search(r'Target:\s*(.+)', header.read_text(encoding='utf-8',
                                                          errors='replace'))
        if m:
            return m.group(1).strip()
    return 'unknown'


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--sdk', required=True, type=Path)
    ap.add_argument('--out', required=True, type=Path,
                    help='path to the aimp-plugin-developer skill directory')
    ap.add_argument('--chm-html', type=Path,
                    help='already-decompiled CHM directory (skips hh.exe)')
    args = ap.parse_args()

    sdk = args.sdk.resolve()
    out = args.out.resolve()
    if not (sdk / 'Sources').is_dir():
        raise SystemExit('%s does not look like an AIMP SDK (no Sources/)' % sdk)

    tmp = None
    if args.chm_html:
        html_dir = args.chm_html.resolve()
    else:
        tmp = Path(tempfile.mkdtemp(prefix='aimp-chm-'))
        html_dir = decompile_chm(sdk / 'Help' / 'AIMP-en.chm', tmp)

    toc = parse_toc(html_dir / 'TOC.hhc')
    em = Emitter(html_dir, out / 'references')

    written: list = []

    # Introduction + "Local API / Overview" subtree -> concepts.md
    intro = toc.find('Introduction')
    overview = toc.find('Overview')
    parts = ['# AIMP SDK concepts\n']
    if intro:
        md, summary = render_topic(intro, html_dir, 2)
        parts.append(md)
    if overview:
        parts.append(em.render_group(overview, 2, 'concepts.md'))
    em.write('concepts.md', '\n'.join(parts))
    written.append(('Concepts / overview', 'concepts.md'))

    for toc_name, rel in (('Basic Interfaces', 'basic-interfaces.md'),
                          ('Primitives', 'primitives.md'),
                          ('Whats new?', 'whats-new.md'),
                          ('Remote API', 'remote-api.md')):
        node = toc.find(toc_name)
        if node is None:
            print('warning: TOC has no "%s" node' % toc_name, file=sys.stderr)
            continue
        em.write(rel, em.render_group(node, 1, rel))
        written.append((toc_name, rel))

    chapters = toc.find('Chapters')
    if chapters is None:
        raise SystemExit('TOC has no "Chapters" node — the help layout changed')
    for chapter in chapters.children:
        written.extend(em.emit_chapter(chapter, 'api'))

    # index of every topic
    lines = ['# Topic index\n',
             'Every documented AIMP interface, message and property, and the '
             'reference file it lives in. Grep this first.\n',
             '| Topic | Reference file | Summary |',
             '|---|---|---|']
    for name, rel, summary in sorted(set(em.index)):
        summary = summary.replace('|', '/').strip()[:140]
        lines.append('| `%s` | `%s` | %s |' % (name, rel, summary))
    em.write('topics-index.md', '\n'.join(lines))

    # the SDK's loose RTF notes
    for stem, rel in RTF_DOCS.items():
        src = sdk / ('%s.rtf' % stem)
        if src.exists():
            em.write(rel, rtf2md.convert(src))
            written.append((stem, rel))

    # Drop reference files left over from a previous SDK drop, so a removed
    # interface does not linger as a stale page.
    stale = []
    written_paths = {(em.out / rel).resolve() for rel, _ in em.files}
    written_paths.add((em.out / 'version.md').resolve())
    for path in sorted(em.out.rglob('*.md')):
        parts = path.relative_to(em.out).parts
        # `sdk/` is the vendored copy; `guides/` is hand-written — neither is
        # this script's to delete.
        if 'sdk' in parts or 'guides' in parts:
            continue
        if path.resolve() not in written_paths:
            stale.append(path.relative_to(em.out).as_posix())
            path.unlink()

    n_sources = copy_sources(sdk, out)

    version = sdk_version(sdk)
    total = sum(size for _, size in em.files)
    em.write('version.md', VERSION_TMPL.format(
        version=version,
        n_topics=len({n for n, _, _ in em.index}),
        n_files=len(em.files),
        n_sources=n_sources,
        kb=total // 1024,
    ))

    print('SDK target      : %s' % version)
    print('topics indexed  : %d' % len({n for n, _, _ in em.index}))
    print('reference files : %d (%d KB)' % (len(em.files), total // 1024))
    print('vendored sources: %d' % n_sources)
    if stale:
        print('removed stale   : %s' % ', '.join(stale))
    print('\nlargest reference files:')
    for rel, size in sorted(em.files, key=lambda x: -x[1])[:10]:
        print('  %7d  %s' % (size, rel))
    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)


VERSION_TMPL = """# SDK version and provenance

- **AIMP SDK target:** {version}
- **Generated by:** `aimp-sdk-skill-maintainer/scripts/extract_sdk.py`

## What was extracted

| | |
|---|---|
| Documented topics | {n_topics} |
| Reference files | {n_files} ({kb} KB) |
| Vendored SDK source files | {n_sources} |

## Provenance

Everything under `references/` is generated from the SDK drop itself:

- `references/api/`, `concepts.md`, `primitives.md`, `basic-interfaces.md`,
  `remote-api.md`, `whats-new.md`, `topics-index.md` — converted from
  `Help/AIMP-en.chm`, laid out along that file's own `TOC.hhc`.
- `references/sdk/Sources/`, `references/sdk/Demos/` — copied verbatim from
  the SDK. These are the authority for exact signatures, GUIDs and constant
  values; the prose is the authority for semantics.
- `packaging.md`, `cli-encoders.md`, `playlist-file-format.md`,
  `xspf-extensions.md` — converted from the SDK's loose `.rtf` notes.

`references/guides/` is the one hand-written layer — the extraction script
never writes or deletes anything there. It is the place for judgement
(decision tables, idioms, scaffolds) that the SDK does not state directly, and
it must be re-verified against each new drop by hand.

Nothing here is written from memory. When the docs and the headers disagree,
the headers win and the disagreement is worth noting here.

## Known conversion caveats

- The CHM is HTML generated by a doc tool; deeply nested lists inside a
  parameter note flatten into indented lines. Signatures and constant names
  survive exactly; wrap-around prose can read slightly ragged.
- The `.rtf` notes are converted by a minimal RichEdit-subset reader. Treat
  their exact layout tables as approximate and check the original `.rtf` in
  the SDK if a byte-level detail matters.
"""


if __name__ == '__main__':
    main()
