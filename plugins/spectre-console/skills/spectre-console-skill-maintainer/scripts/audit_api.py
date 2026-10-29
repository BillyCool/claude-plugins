#!/usr/bin/env python3
"""Cross-check extract_api.py against the raw source.

Usage:  python audit_api.py <core-repo> <cli-repo>

For every `public`/`protected` member-looking line in the scanned projects, check that a
member of that name was extracted somewhere. Names that are missing are listed per file.
Expect noise from public members of *internal* types (JsonBuilder, ListPrompt*, Table
measuring helpers, ...). What matters is a *new* cluster of misses in a public type: that
means the scanner mis-parsed something and extract_api.py needs a fix before its output
can be trusted.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import extract_api as e  # noqa: E402


def main():
    repos = {"core": Path(sys.argv[1]).resolve(), "cli": Path(sys.argv[2]).resolve()}
    names = set()
    for label, rk, rel, pkg in e.PROJECTS:
        for ti in e.extract_project(label, repos[rk] / rel, repos[rk], pkg).values():
            names.update(e.member_name(m) for m in ti.members)
    miss = {}
    for label, rk, rel, pkg in e.PROJECTS:
        root = repos[rk] / rel
        for f in root.rglob("*.cs"):
            parts = f.parts
            if any(p in e.SKIP_DIRS for p in parts):
                continue
            if "Generated" in parts and not any(g in str(f) for g in e.GENERATED_OK):
                continue
            for ln, line in enumerate(f.read_text(encoding="utf-8-sig", errors="replace").splitlines(), 1):
                if re.match(r"^\s+(public|protected)\s", line) and not re.search(r"\b(class|struct|interface|enum|record|delegate)\s+\w", line):
                    h = re.sub(r"<[^<>()]*>", "", line)
                    h = h.split("=>")[0].split("{")[0].split(";")[0]
                    h = h.split("(")[0] if "operator" not in h else h
                    h = h.split("=")[0]
                    w = re.findall(r"[A-Za-z_]\w*", h)
                    if not w:
                        continue
                    nm = "operator" if "operator" in line else w[-1]
                    if nm not in names and nm != "operator":
                        miss.setdefault(str(f.relative_to(root)), []).append((ln, line.strip()[:80]))
    total = sum(len(v) for v in miss.values())
    out = [f"{total} member lines with no extracted counterpart (internal-type noise expected)"]
    for k, v in sorted(miss.items(), key=lambda kv: -len(kv[1]))[:30]:
        out.append(f"  {k} ({len(v)})  e.g. line {v[0][0]}: {v[0][1]}")
    sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8", "replace"))


if __name__ == "__main__":
    main()
