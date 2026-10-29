#!/usr/bin/env python3
"""Compile every ```csharp block in the writer skill's hand-written references.

Usage:
    python check_snippets.py <writer-skill-dir> <work-dir> [--version 0.57.2]

Needs the .NET SDK and nuget.org access. <work-dir> is a scratch folder (created
if missing). The script builds a throw-away project that references the *released*
NuGet packages for the given version and reports every snippet that fails to
compile. Run it after updating any reference file or after a version bump: it is
how stale or wrong sample code gets caught.

Block conventions in the reference markdown:
    ```csharp            statements (wrapped in a method; `await` is fine), OR a block
                         whose first non-blank line declares a type (class/record/
                         struct/enum/interface) -> compiled as declarations
    ```csharp-decl       force "declarations" (types and/or members; wrapped in a class
                         if it does not start with a type declaration)
    ```csharp-fragment   illustrative only (contains `...`, pseudo-code); skipped

All blocks of one markdown file share a namespace, so a later block may use a type declared
in an earlier one -- and type names must therefore be unique within a file.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

PACKAGES = [
    "Spectre.Console",
    "Spectre.Console.Cli",
    "Spectre.Console.Json",
    "Spectre.Console.Testing",
    "Spectre.Console.Cli.Testing",
]

USINGS = """\
global using System;
global using System.Collections.Generic;
global using System.ComponentModel;
global using System.IO;
global using System.Linq;
global using System.Threading;
global using System.Threading.Tasks;
global using Spectre.Console;
global using Spectre.Console.Cli;
global using Spectre.Console.Json;
global using Spectre.Console.Rendering;
global using Spectre.Console.Testing;
global using Spectre.Console.Cli.Testing;
"""

FENCE = re.compile(r"^```(csharp(?:-decl|-fragment)?)\s*$(.*?)^```\s*$", re.S | re.M)
TYPE_START = re.compile(
    r"^\s*(?:\[[^\]]*\]\s*)*(?:(?:public|internal|private|protected|sealed|static|abstract|partial|readonly|file)\s+)*"
    r"(?:class|record|struct|enum|interface)\s+\w+")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    version = "0.57.2"
    if "--version" in sys.argv:
        version = sys.argv[sys.argv.index("--version") + 1]
        args = [a for a in args if a != version]
    if len(args) != 2:
        print(__doc__)
        sys.exit(2)
    writer, work = Path(args[0]).resolve(), Path(args[1]).resolve()
    work.mkdir(parents=True, exist_ok=True)
    gen = work / "snippets"
    gen.mkdir(exist_ok=True)
    for old in gen.glob("*.cs"):
        old.unlink()

    refs = sorted((writer / "references").glob("*.md"))
    index = []   # (file, line, name)
    n = 0
    skipped = 0
    for md in refs:
        text = md.read_text(encoding="utf-8")
        for m in FENCE.finditer(text):
            kind, body = m.group(1), m.group(2).strip("\n")
            line = text.count("\n", 0, m.start()) + 2
            if kind == "csharp-fragment":
                skipped += 1
                continue
            n += 1
            name = f"S{n:04d}"
            index.append((md.name, line, name))
            using_lines = [l for l in body.splitlines() if re.match(r"^\s*using\s+[\w\.]+;\s*$", l)]
            rest = "\n".join(l for l in body.splitlines() if l not in using_lines)
            first = next((l for l in rest.splitlines() if l.strip() and not l.strip().startswith("//")), "")
            is_decl = kind == "csharp-decl" or bool(TYPE_START.match(first))
            if is_decl and TYPE_START.match(first):
                code = rest
            elif is_decl:
                code = f"static class {name}Members {{\n{rest}\n}}"
            else:
                async_ = bool(re.search(r"\bawait\b|\bawait foreach\b", rest))
                sig = "static async Task" if async_ else "static void"
                code = f"static class {name}Host {{\n#pragma warning disable CS8321\n{sig} Run() {{\n{rest}\n}}\n}}"
            ns = "F_" + re.sub(r"[^A-Za-z0-9]", "_", md.stem)
            src = "\n".join(using_lines) + f"\n// {md.name}:{line}\nnamespace {ns} {{\n{code}\n}}\n"
            (gen / f"{name}.cs").write_text(src, encoding="utf-8")

    proj = work / "snippets.csproj"
    refs_xml = "\n".join(f'    <PackageReference Include="{p}" Version="{version}" />' for p in PACKAGES)
    proj.write_text(f"""<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Library</OutputType>
    <TargetFramework>net10.0</TargetFramework>
    <Nullable>enable</Nullable>
    <LangVersion>latest</LangVersion>
    <ImplicitUsings>disable</ImplicitUsings>
    <NoWarn>$(NoWarn);CS8321;CS0168;CS0219;CS1998;CS8618;CS9113;CS0414;CS0649;CA1822</NoWarn>
    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="snippets/*.cs" />
    <Compile Include="GlobalUsings.cs" />
{refs_xml}
  </ItemGroup>
</Project>
""", encoding="utf-8")
    (work / "GlobalUsings.cs").write_text(USINGS, encoding="utf-8")

    r = subprocess.run(["dotnet", "build", str(proj), "-nologo", "-v", "q", "-clp:NoSummary;ErrorsOnly"],
                       capture_output=True, text=True)
    out = (r.stdout + r.stderr)
    errs = sorted(set(re.findall(r"snippets[\\/](S\d{4})\.cs\((\d+),\d+\): error (CS\d+): (.*?) \[", out)))
    by_name = {nm: (f, ln) for f, ln, nm in index}
    if not errs and r.returncode == 0:
        print(f"OK: {n} snippets compiled against Spectre.Console {version} ({skipped} fragments skipped)")
        return
    if not errs:
        print(out[-3000:])
        sys.exit(1)
    for nm, ln, code, msg in errs:
        f, line = by_name.get(nm, ("?", 0))
        print(f"{f}:{line}  (+{int(ln) - 4} in block)  {code}: {msg[:160]}")
    print(f"\nFAILED: {len({e[0] for e in errs})} of {n} snippets do not compile")
    sys.exit(1)


if __name__ == "__main__":
    main()
