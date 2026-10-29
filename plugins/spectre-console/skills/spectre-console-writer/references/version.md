# Provenance and sync state

| Field | Value |
|---|---|
| Documented version | **0.57.2** (all stable packages move together) |
| Core repo | `spectreconsole/spectre.console` @ tag `0.57.2` = `bbbb5729dde27b58deee44f447a788eea46ee451` (released 2026-07-02) |
| CLI repo | `spectreconsole/spectre.console.cli` @ tag `0.57.2` = `9c88a343b8ce622e9fda4e4334b2057d773d90c9` (no GitHub *release* objects, tags only) |
| Docs repo (secondary) | `spectreconsole/website` @ `70844af` — site https://spectreconsole.net |
| Last sync | 2026-10-30 |
| Extraction | 327 public types, 3,615 members, 423 extension methods across 7 projects; 269 types indexed (extension-only static classes are listed separately); 21 widget pages |
| Snippet check | 47 `csharp` blocks in the hand-written references compile against NuGet 0.57.2 (`check_snippets.py`); 2 `csharp-fragment` blocks are illustrative only |

## What is generated vs hand-written

| Files | Origin |
|---|---|
| `api/**`, `colors.md`, `spinners.md`, `emoji-shortcodes.md` | **Generated** by `spectre-console-skill-maintainer/scripts/extract_api.py` from source (and the repo's `Data/*.json`). Never hand-edit; re-run the script. |
| `getting-started.md`, `markup-and-styling.md`, `widgets.md`, `live-displays.md`, `prompts.md`, `rendering-and-custom-widgets.md`, `testing.md`, `ansi-and-console-extensions.md`, `cli.md` | **Hand-written**, each statement traced to source and/or verified by compiling/running against the 0.57.2 NuGet packages |

## Source anchors for hand-written files

| File | Verified against |
|---|---|
| `getting-started.md` | `AnsiConsole*.cs`, `AnsiConsoleFactory.cs`, `AnsiConsoleSettings.cs`, `Profile.cs`, `InteractionDetector.cs`, `Internal/DefaultInput.cs`, `Internal/DefaultExclusivityMode.cs`, `Enrichment/CI/*.cs`, `Spectre.Console*.csproj` (TFMs, AOT flags) |
| `markup-and-styling.md` | `Spectre.Console.Ansi/AnsiMarkup.cs` (tokenizer, parse, escape, remove), `AnsiMarkupTagParser.cs`, `DecorationTable.cs`, `Color.cs`, `Style.cs`; `Spectre.Console/Widgets/Markup.cs`; `Extensions/AnsiConsoleExtensions.Markup.cs` |
| `widgets.md` | `Widgets/**`, `Rendering/Borders/**`, `BoxBorder.Known.cs`, `TableBorder.Known.cs`, `TreeGuide.Known.cs`, `Widgets/Table/TableRowCollection.cs` |
| `live-displays.md` | `Live/**` (Progress renderer selection, `ProgressContext.IsFinished`, status fallback) |
| `prompts.md` | `Prompts/*.cs`, `Extensions/AnsiConsoleExtensions.Prompt.cs`, `AnsiConsole.Prompt.cs` |
| `testing.md` | `Spectre.Console.Testing/*.cs`; CLI repo `Spectre.Console.Cli.Testing/*.cs`; behaviour confirmed by running a probe app |
| `cli.md` | CLI repo `src/Spectre.Console.Cli/**` (`CommandOfT.cs`, `CommandApp.cs`, `Internal/CommandExecutor.cs`, `Internal/Binding/*`, `Internal/Composition/*`, `Annotations/*`); exit codes/messages confirmed by running a probe app |
| `ansi-and-console-extensions.md` | `Spectre.Console.Ansi/AnsiWriter.cs`, `Utilities/ConsoleExtensions.cs` |

## Docs-vs-source discrepancies found while building this (source wins)

1. Docs samples use `protected override … Execute`; released CLI base classes are `public abstract`
   → must be `public override` (CS0507 otherwise). Some CLI tutorials also omit the 0.57
   `CancellationToken` parameter.
2. Markup docs list only long decoration names; source also accepts `b i u s`, `strike`, `reverse`,
   `blink`, `none`, and numeric colors `[0..255]` and `#RGB`.
3. Docs describe `Remaining.Parsed["unknown-option"]`; keys actually keep the leading dashes.
4. `GitHub releases/latest` returns 404 for every repo here (all releases are flagged pre-release)
   → find versions via `gh release list` / tags / NuGet.
5. `Dictionary<,>` option properties fail to bind; docs gloss over needing `IDictionary<,>`.
6. Prompts: `TestConsole` is non-interactive by default but text/confirm prompts still work with queued
   input; only selection prompts need `.Interactive()`.
7. `Color`, `Emoji` and `Spinner` members are source-generated; the generated `.g.cs` files happen to be
   committed under `src/*/Generated/` at this tag, and `extract_api.py` reads them (emoji shortcodes) plus
   `Data/colors.json` / `spinners_*.json`. If a future tag stops committing them, build the project
   with `EmitCompilerGeneratedFiles` (the csproj already sets it) to regenerate.

## Not yet released (on `main`, 30 commits after 0.57.2; do not use against 0.57.2)

`CalendarExtensions.RemoveCalendarEvent`, tab-cycling through search results in `SelectionPrompt`,
`ProgressTask.MaxValue` validation (≥ 0), fallback to default console size when the reported
size is non-positive, a `TableMeasurer.CollapseWidths` infinite-loop fix, `TestConsoleInput`
no longer producing characters for navigation keys. NuGet has `0.57.3-alpha.*` builds of the
packages and `Spectre.Console.Cli` `1.0.0-alpha.*`.

## Version honesty

The 0.x line has broken APIs between minors (e.g. 0.55 split the ANSI layer into
`Spectre.Console.Ansi`; `Spectre.Console.Cli` now lives in its own repo; older releases had a
two-parameter `Command<T>.Execute`). Check the user's
`PackageReference` before applying anything here, and say so when they pin an older version.
