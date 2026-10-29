---
name: spectre-console-writer
description: >-
  Expert Spectre.Console and Spectre.Console.Cli development for .NET, backed by a
  source-verified offline copy of the API and docs. Use for any rich-terminal work in C#:
  markup and colors, tables/panels/trees/layouts/charts/calendars, progress bars, spinners
  and live displays, prompts (text, select, multi-select, confirm), JSON/image widgets,
  custom renderables, unit-testing console output with TestConsole, and building
  command-line apps with commands/settings/options ("add a progress bar", "make this a
  table", "ask the user to pick", "parse command-line args with Spectre", "why does
  MarkupLine throw", "test my Spectre.Console output"). Covers Spectre.Console 0.57.2
  including the Ansi, Json, ImageSharp, Testing and Cli packages.
---

# Spectre.Console writer

Write correct, idiomatic Spectre.Console (rich console UI for .NET) and Spectre.Console.Cli
code. This skill is an **offline copy of the library's real API and behaviour**, extracted
from the 0.57.2 source (`references/version.md` has provenance) — prefer it over memory and
over the docs website: the 0.x API changes between minors, and the site documents unreleased
code and contains samples that don't compile against the released packages.

**Golden rule: never guess a member name, overload, enum value, color or markup token. Look it up.**

## How to find things

1. **Which type / which file?** → `references/api/_index.md` (every public type → file, kind, package).
   Widgets are one file each under `references/api/widgets/`; the rest are grouped
   (`console.md` = `AnsiConsole`, `IAnsiConsole`, settings, borders, enums, `Emoji`/`Spinner`; `prompts.md`;
   `live*.md`; `rendering.md`; `ansi.md`; `cli.md`; `testing.md`; `json.md`; `imagesharp.md`).
2. **Fluent methods** (`.Border(...)`, `.Header(...)`, `.Expand()`, `.PadLeft()`, `.Centered()`) are
   *extension methods*. Each type's api section has "Extension methods on this type" and a list
   of ones inherited via shared interfaces; full signatures of the shared ones are in
   `references/api/_shared-extensions.md`.
3. **Guides** (how to choose and combine; pitfalls; compile-checked samples):

| Topic | File |
|---|---|
| Packages, `AnsiConsole` vs `IAnsiConsole`, capabilities, CI/redirect, exclusivity, DI | `references/getting-started.md` |
| Markup grammar, escaping, `Style`/`Color`/`Decoration`, emoji, links | `references/markup-and-styling.md` |
| Table, Grid, Panel, Rule, Tree, Layout, charts, Calendar, Figlet, Canvas, JSON, exceptions | `references/widgets.md` |
| Progress, Status, LiveDisplay | `references/live-displays.md` |
| Text / selection / multi-selection / confirmation prompts | `references/prompts.md` |
| Custom widgets (`Renderable`, `JustInTimeRenderable`, segments) | `references/rendering-and-custom-widgets.md` |
| `TestConsole`, scripted input, `CommandAppTester` | `references/testing.md` |
| Command-line apps (commands, settings, options, DI, exit codes) | `references/cli.md` |
| `AnsiWriter`, `AnsiMarkup`, `Console.Markup` (.NET 10) | `references/ansi-and-console-extensions.md` |
| Named colors, spinners, emoji shortcodes | `references/colors.md`, `spinners.md`, `emoji-shortcodes.md` |

## Writing good Spectre.Console code

- **Accept `IAnsiConsole`, don't hard-wire `AnsiConsole`** in anything you'll test or reuse; use the
  static facade only at the app edge. Tests use `TestConsole`.
- **Escape anything dynamic that reaches markup.** `MarkupLine($"...{x}...")` with user/file/exception
  text is the #1 crash (`[`, `]` in data). Use `MarkupLineInterpolated`, `Markup.Escape(x)`, or
  `new Text(x)`. String arguments to `Panel`, `Table.AddRow`, `Rule`, prompt titles are parsed as markup too.
- **Closing tag is always `[/]`** (never `[/red]`). One foreground + one background color per tag.
- **`Write`/`WriteLine` don't parse markup; `Markup*` do.**
- **Only one interactive thing at a time**: prompts, `Status`, `Progress`, `LiveDisplay` share an
  exclusivity lock; never prompt or `Write*` inside them. Update the context objects instead.
- **Non-interactive/redirected output is normal** (CI, pipes): prompts throw there
  (`Capabilities.Interactive`), live displays fall back, widths come from `Profile.Width`.
  Guard prompts; don't assume a TTY.
- **Prefer widgets + composition over manual padding/ANSI**: `Grid` for label/value alignment,
  `Table` for data, `Panel`/`Rule` for structure, `Layout`+`LiveDisplay` for dashboards,
  `Columns`/`Rows` to flow things. Anything `IRenderable` nests inside anything else.
- **Use the CLI package for argument parsing** rather than hand-rolling: `Command<TSettings>`
  (`public override int Execute(CommandContext, TSettings, CancellationToken)`), settings class with
  `[CommandArgument]`/`[CommandOption]`/`[Description]`/`[DefaultValue]`, `Validate()` for cross-field
  checks, return exit codes, inject `IAnsiConsole` for testable output.
- **Pick values from the lookup tables**: named colors → `colors.md` (`orange` is *not* a color;
  `orange1`/`darkorange` are), spinners → `spinners.md`, borders → `widgets.md` lists.
- **Version honesty.** This skill documents 0.57.2. Check the project's `PackageReference`; if it pins an
  older/newer 0.x version, say which differences matter (e.g. `Execute` signature, `Spectre.Console.Ansi`
  split, `TableCell` spans, `SelectionPrompt` search) instead of assuming.

## Common failure → cause

| Symptom | Cause |
|---|---|
| `InvalidOperationException: Could not find color or style 'x'` | bad token in markup (typo, `[orange]`, user text with brackets) |
| `Encountered unescaped ']'` / `Unbalanced markup stack` / `Encountered closing tag when none was expected` | unescaped brackets, missing or extra `[/]` |
| `Trying to run one or more interactive functions concurrently` | prompt/progress/status/live nested or parallel |
| `Failed to read input in non-interactive mode` / `Cannot show selection prompt since the current terminal isn't interactive` | prompt on redirected/CI console |
| `Cannot add new columns to table with existing rows` | `AddColumn` after `AddRow` |
| `The number of row columns (including spans) are greater than the number of table columns` | row has more cells than columns |
| CS0507 on `protected override Execute` | CLI base `Execute` is `public` (docs samples are wrong) |
| `Failed to convert 'k=v' to Dictionary…` | CLI option property typed `Dictionary<,>`; use `IDictionary<,>` |
| Boxes/spinners show as `?` | non-UTF-8 output encoding or legacy console |
| Colors missing in logs | `NO_COLOR`, redirected output, or CI without ANSI (by design) |

## Answer style

- For "how do I…" give a minimal compilable snippet using verified members, then name the
  reference you used when correcting code ("per `api/widgets/Table.md`, columns must be added before rows").
- State the chosen widget and why when several fit (Table vs Grid, Status vs Progress, Selection vs Text prompt).
- If a requested feature isn't in 0.57.2 (check `references/version.md` "Not yet released"), say so
  and offer the closest released alternative.
