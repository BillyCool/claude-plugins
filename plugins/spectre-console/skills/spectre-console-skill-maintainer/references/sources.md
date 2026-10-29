# Canonical Spectre.Console sources

Site: https://spectreconsole.net (generated from `spectreconsole/website`). Source is authoritative;
the site documents `main` and is partly stale.

## Repositories

| Repo | Contains | Tag style |
|---|---|---|
| `spectreconsole/spectre.console` | `Spectre.Console`, `.Ansi`, `.Json`, `.ImageSharp`, `.Testing`, source generator, tests | `0.57.2` (no `v`), GitHub releases flagged pre-release |
| `spectreconsole/spectre.console.cli` | `Spectre.Console.Cli`, `.Cli.Testing` (+ OpenCLI sources) | `0.57.2`, tags only |
| `spectreconsole/website` | docs markdown (`Spectre.Docs/Content/**`), compiled sample projects (`Spectre.Docs.Examples`, `Spectre.Docs.Cli.Examples`), blog | none (use HEAD) |
| `spectreconsole/analyzer` | `Spectre.Console.Analyzer` Roslyn analyzer (not extracted) | – |
| `spectreconsole/{errata,radline,terminfo,wcwidth,spectre.tui,open-cli}` | sibling libraries (out of scope unless the user asks) | – |

Versions: https://api.nuget.org/v3-flatcontainer/<package-id-lowercase>/index.json
(`spectre.console`, `spectre.console.ansi`, `spectre.console.cli`, `spectre.console.json`,
`spectre.console.imagesharp`, `spectre.console.testing`, `spectre.console.cli.testing`).
The website samples carry no license in the repo → the writer paraphrases and re-implements them,
it never vendors them.

## Source anchors (paths under `src/` of the named repo)

| Path | Confirms | Writer file |
|---|---|---|
| `Spectre.Console/**/*.cs` (public types), `Spectre.Console.Ansi`, `.Testing`, `Extensions/*` ; CLI: `Spectre.Console.Cli`, `.Cli.Testing` | every public member, XML summary, default, enum value, extension method | `references/api/**` via `scripts/extract_api.py` |
| `Spectre.Console.Ansi/Data/colors.json` | the 256 named colors + numbers + hex | `colors.md` |
| `Spectre.Console/Data/spinners_*.json` | spinner names, frames, intervals | `spinners.md` |
| `Spectre.Console/Generated/**/Emoji.Generated.g.cs` | emoji shortcodes (generated at build; committed at some tags) | `emoji-shortcodes.md` |
| `Spectre.Console.Ansi/AnsiMarkup.cs`, `AnsiMarkupTagParser.cs`, `DecorationTable.cs`, `ColorTable`, `Color.cs`, `Style.cs` | markup grammar, accepted tokens, errors | `markup-and-styling.md` |
| `Spectre.Console/AnsiConsole*.cs`, `AnsiConsoleFactory.cs`, `AnsiConsoleSettings.cs`, `Profile.cs`, `Capabilities.cs`, `InteractionDetector.cs`, `Enrichment/**`, `Internal/Default*.cs` | console creation, capability detection, CI enrichers, interactivity, exclusivity messages | `getting-started.md` |
| `Spectre.Console/Widgets/**`, `Rendering/Borders/**`, `BoxBorder.Known.cs`, `TableBorder.Known.cs`, `TreeGuide.Known.cs` | widget behaviour, border/guide lists | `widgets.md` |
| `Spectre.Console/Live/**` | Progress/Status/LiveDisplay semantics, fallback renderers, `ProgressContext.IsFinished` | `live-displays.md` |
| `Spectre.Console/Prompts/**`, `Extensions/AnsiConsoleExtensions.Prompt.cs` | prompt behaviour, defaults, validation, exceptions | `prompts.md` |
| `Spectre.Console/Rendering/**`, `Widgets/Renderable*.cs`, `Segment.cs` | rendering pipeline for custom widgets | `rendering-and-custom-widgets.md` |
| `Spectre.Console.Testing/**`; CLI `Spectre.Console.Cli.Testing/**` | TestConsole/TestConsoleInput/CommandAppTester | `testing.md` |
| CLI `Spectre.Console.Cli/{Command*.cs,Annotations/**,Internal/{CommandExecutor,Binding/**,Composition/**,Modelling/**}}` | command base classes, attributes, binding, DI, exit codes | `cli.md` |
| `Spectre.Console.Ansi/{AnsiWriter.cs,Utilities/ConsoleExtensions.cs}` | AnsiWriter fluent API, `Console.Markup` extension members | `ansi-and-console-extensions.md` |

## Method notes

- The member surface is ~3,600 entries — never diff it by eye; run `extract_api.py` and `git diff` the writer.
- `Color`, `Emoji`, `Spinner` members are produced by the source generator (`Spectre.Console.SourceGenerator`,
  data files above). The extractor prefers the `Ansi` project's `Color`; keep the `PROJECTS` order
  `ansi` before `core` so the complete type wins when a name appears in both.
- Extension methods are resolved to the types they apply to (direct target, or generic target constrained to
  an interface/base such as `IHasBoxBorder`, `IPaddable`, `IExpandable`). Shared ones are collected in
  `api/_shared-extensions.md`.
- C# 14 `extension(X) { ... }` blocks (`SystemConsoleExtensions`) are recorded as members of the enclosing
  static class, prefixed with `extension(X)`.
- Windows: use `git -c core.longpaths=true`; verify the tree is complete after cloning. Don't leave a shell
  `cd`'d inside `references/api` while the extractor runs (it clears that directory's contents).
- Heredoc-driven Python edits corrupt backslashes/`\b`/`\n` easily; edit scripts with the Edit tool and
  run `python -c "import ast; ast.parse(open('extract_api.py').read())"` plus a grep for stray `\x08`.
- When the docs and source disagree, write it into `version.md` → "Docs-vs-source discrepancies".
