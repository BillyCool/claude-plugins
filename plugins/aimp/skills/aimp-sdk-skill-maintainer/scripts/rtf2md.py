#!/usr/bin/env python3
"""Minimal RTF -> Markdown-ish text converter for the AIMP SDK's .rtf documents.

The SDK ships four RTF notes (add-on package layout, playlist format, XSPF
extensions, CLI encoder integration) written by RichEdit with a very small
subset of RTF: paragraphs, bold, underline, hex/unicode escapes. That is all
this handles — it is not a general RTF reader.

    python rtf2md.py <file.rtf>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CONTROL = re.compile(r"\\(?:([a-zA-Z]+)(-?\d+)?|(['\\{}])(..)?|\*)")
BLANKS = re.compile(r'\n{3,}')


def rtf_to_text(data: str) -> str:
    out: list[str] = []
    depth = 0
    skip_group = None  # depth of a group we are discarding (fonttbl etc.)
    i = 0
    bold = False
    n = len(data)
    while i < n:
        ch = data[i]
        if ch == '{':
            depth += 1
            i += 1
            continue
        if ch == '}':
            if skip_group is not None and depth <= skip_group:
                skip_group = None
            depth -= 1
            i += 1
            continue
        if ch == '\\':
            m = CONTROL.match(data, i)
            if not m:
                i += 1
                continue
            i = m.end()
            word, arg, esc, hexdigits = m.group(1), m.group(2), m.group(3), m.group(4)
            if esc == "'":
                if skip_group is None and hexdigits:
                    try:
                        ch = bytes([int(hexdigits, 16)]).decode('cp1251')
                    except (ValueError, UnicodeDecodeError):
                        continue
                    # Symbol-font bullets and stray control codes are layout,
                    # not text.
                    if ch == '\xb7':
                        ch = '- '
                    elif ch < ' ':
                        ch = ''
                    out.append(ch)
                continue
            if esc in ('\\', '{', '}'):
                if skip_group is None:
                    out.append(esc)
                    if hexdigits:
                        i = m.end() - 2
                continue
            if word in ('fonttbl', 'colortbl', 'stylesheet', 'generator',
                        'info', 'pict', 'themedata', 'datastore',
                        'listtable', 'listoverridetable', 'latentstyles',
                        'rsidtbl', 'xmlnstbl', 'filetbl', 'objdata',
                        'pntext', 'pntxta', 'pntxtb', 'nonshppict',
                        'bkmkstart', 'bkmkend', 'fldinst'):
                skip_group = depth
                continue
            if skip_group is not None:
                continue
            if word == 'par' or word == 'line':
                out.append('\n')
            elif word == 'tab':
                out.append('    ')
            elif word == 'u' and arg is not None:
                code = int(arg)
                ch = chr(code if code >= 0 else code + 65536)
                out.append('' if ch < ' ' else ch)
                # skip the following replacement char
                if i < n and data[i] == '?':
                    i += 1
            elif word == 'b':
                bold = arg != '0'
                out.append('**')
            elif word == 'ul' and arg is None:
                out.append('')
            continue
        if ch == '\n' or ch == '\r':
            i += 1
            continue
        if skip_group is None:
            out.append(ch)
        i += 1
    text = ''.join(out)
    # RichEdit writes a literal NUL at the end of some documents; nothing in
    # the C0 range other than newline and tab is content here.
    text = re.sub(r'[\x00-\x08\x0b-\x1f]', '', text)
    # tidy the bold markers we sprayed in
    text = re.sub(r'\*\*(\s*)\*\*', r'\1', text)
    lines = []
    for line in text.split('\n'):
        line = line.strip()
        if line == '**':
            line = ''
        elif line.count('**') % 2:
            # RichEdit leaves \b spanning the \par; close it at end of line
            line = line + '**'
        line = line.replace('****', '')
        # a short, fully-bold line is a heading in these documents; a long or
        # sentence-shaped one is just a paragraph RichEdit left \b spanning
        if line.startswith('**') and line.endswith('**') and '**' not in line[2:-2]:
            inner = line[2:-2].strip()
            line = '## ' + inner if len(inner) < 60 and not inner.endswith('.') else inner
        lines.append(line)
    text = '\n'.join(lines)
    return BLANKS.sub('\n\n', text).strip()


def convert(path: Path) -> str:
    return rtf_to_text(path.read_text(encoding='latin-1'))


if __name__ == '__main__':
    print(convert(Path(sys.argv[1])))
