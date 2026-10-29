---
name: spectre-console-skill-maintainer
description: >-
  Keep the `spectre-console-writer` skill in sync with new Spectre.Console and
  Spectre.Console.Cli releases. Use when the user says a new Spectre.Console version
  shipped, asks to update/refresh/audit the Spectre.Console skill, or wants to check
  whether its documented API, markup syntax, prompts, live displays or CLI behaviour
  are still accurate. Clones the tagged source of the core and CLI repos, re-runs the
  API extraction, compile-checks the writer's code samples against the new NuGet
  packages, re-runs behaviour probes, diffs, and applies concrete edits.
---

# Spectre.Console skill maintainer

Updates the sibling **`spectre-console-writer`** skill (`../spectre-console-writer/`) so its API
knowledge stays true to Spectre.Console. Manually invoked: run it when a new release lands or when the
writer's accuracy is in doubt.

Core principle: **everything the writer documents must be confirmed in the tagged source code or by
running the released packages.** The docs website (`spectreconsole.net`, repo `spectreconsole/website`)
tracks unreleased code and has samples that do not compile (e.g. `protected override Execute`), and
GitHub release notes are nearly empty — they point at what to re-check, they never replace reading
source. Work from release **tags**, never `main`.

Prerequisites: `git`, `gh` (authenticated), `python` 3, .NET SDK (10+) and nuget.org access.
Use the scratchpad directory for clones; on Windows clone with `git -c core.longpaths=true`.

## Workflow

### 1. Establish baseline
Read `../spectre-console-writer/references/version.md`: documented version, tag SHAs, extraction
counts, the "Not yet released" list and the docs-vs-source discrepancy list.

### 2. Find the current release
Three repos matter; all stable packages share one version number:
```
gh release list -R spectreconsole/spectre.console --limit 10      # core (all releases are flagged pre-release!)
gh api repos/spectreconsole/spectre.console.cli/tags --jq '.[].name' | head   # CLI repo: tags only, no releases
curl -s https://api.nuget.org/v3-flatcontainer/spectre.console/index.json     # NuGet: confirm the stable version exists
```
`/releases/latest` returns 404 here (every release is a pre-release) — do not use it. Take the highest
**stable** version present as a tag in both repos and on NuGet (`Spectre.Console`, `.Cli`, `.Json`,
`.ImageSharp`, `.Testing`, `.Cli.Testing`). If it equals the baseline, say the skill is current and stop
(unless asked for a full re-audit). Ignore `-alpha`/`-preview` NuGet builds (note them in `version.md`).

### 3. Clone the tags
```
git -c core.longpaths=true clone --depth 1 --branch <tag> https://github.com/spectreconsole/spectre.console.git     <scratch>/sc
git -c core.longpaths=true clone --depth 1 --branch <tag> https://github.com/spectreconsole/spectre.console.cli.git <scratch>/cli
git clone --depth 1 https://github.com/spectreconsole/website.git <scratch>/web     # secondary: docs + blog
```
Check each clone's file count against `git ls-tree -r HEAD | wc -l` — on Windows a path problem can silently
leave half a working tree. Also note repo layout changes (new/removed projects) — the extractor's
`PROJECTS` list is explicit; update it (and `references/sources.md`) when projects move.

### 4. Regenerate the mechanical references
```
python scripts/extract_api.py <scratch>/sc <scratch>/cli ../spectre-console-writer
python scripts/audit_api.py   <scratch>/sc <scratch>/cli
```
`extract_api.py` rewrites `references/api/**`, `colors.md`, `spinners.md`, `emoji-shortcodes.md` in the
writer. `git diff` the writer to see exactly what changed in the public surface: new/removed types,
members, defaults, enum values, extension methods, colors, spinners, emoji. `audit_api.py` lists
public/protected member lines that produced no extracted member; expect noise from public members of
*internal* types (JsonBuilder, ListPrompt*, TableMeasurer…) — a **new cluster in a public type** means the
scanner mis-parsed something (this has happened: C# 14 `extension(...)` blocks, `=>` inside method
bodies, operators, tuple return types). Fix `extract_api.py` and re-run before trusting the diff.

Sanity checks after extraction: counts vs previous run (in `version.md`), one changed file against its
source, `grep -r "{  }" ../spectre-console-writer/references/api` must be empty, and
`../spectre-console-writer/references/api/_index.md` still lists every widget.

### 5. Compile-check the hand-written samples
```
python scripts/check_snippets.py ../spectre-console-writer <scratch>/snip --version <new version>
```
Builds every ```` ```csharp ```` block in the writer's references against the released NuGet packages.
Every failure is either a breaking change (update the prose **and** the sample) or a bad sample. Blocks
marked `csharp-fragment` are skipped. Keep type names unique within one markdown file (blocks of a
file share a namespace).

### 6. Re-run behaviour probes
```
cd scripts/probes && dotnet run -p:SpectreVersion=<new version>
```
Prints the facts the writer states that signatures can't prove (CLI exit codes and error messages,
option binding rules, `TestConsole` interactivity, `AnsiWriter` output). Compare with the "CLAIMS UNDER
TEST" header; for any difference update `cli.md`, `testing.md`, `ansi-and-console-extensions.md` and the
failure→cause table in the writer's `SKILL.md`. Add a probe when you add a behavioural claim.

### 7. Re-verify the hand-written references
`../spectre-console-writer/references/version.md` maps each hand-written file to its source anchors;
`references/sources.md` (this skill) adds what to look for. For every changed anchor, read the code and
reconcile. Then trace what changed upstream and make sure each item is reflected or consciously ignored:
```
gh api repos/spectreconsole/spectre.console/compare/<old>...<new> --jq '.commits[].commit.message' | cut -d$'\n' -f1
gh api repos/spectreconsole/spectre.console.cli/compare/<old>...<new> ...
gh release view <new> -R spectreconsole/spectre.console          # usually near-empty
ls <scratch>/web/Spectre.Docs/Content/blog                        # breaking-change announcements land here
```
Also re-read the `web` docs for pages whose topic changed, **only to find claims to verify** — then confirm
in source; record any new docs-vs-source disagreement in `version.md`.

### 8. Propose, then apply
Summarize: what changed upstream, what the diff shows, which writer files will be edited. On approval
(or a standing "just update"):
- keep the regenerated generated files;
- edit hand-written references — change facts, keep the prose style; add new features/pitfalls where a
  newcomer would trip, remove anything that no longer exists;
- update `version.md` (version, tag SHAs, release date, sync date, counts, snippet count, "Not yet
  released" list, discrepancies);
- bump the version in the writer's `SKILL.md` description and "version honesty" bullet;
- update the plugin/marketplace description only if the scope changed.

### 9. Report
List updated files, breaking changes users of the old version will hit, and anything worth teaching in
the writer's guidance sections (a new widget family, a renamed concept, a changed default) — parameter
tables update themselves; guidance does not. Delete the scratch clones.

## Notes

- Source (at the tag) and executing the released package beat docs site, blog, release notes and memory.
- This skill edits only `../spectre-console-writer/` and its own `scripts/` + `references/`.
- Never hand-edit generated files; fix the script instead.
- The extractor is a purpose-built C# declaration scanner (comments, strings, braces aware), not Roslyn.
  If it ever becomes unreliable, the alternative is reflecting over the built assemblies + XML docs —
  but keep the output format so diffs stay readable.
