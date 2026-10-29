# Getting started, consoles and capabilities

Verified against `Spectre.Console` 0.57.2 source (`src/Spectre.Console/AnsiConsole*.cs`,
`AnsiConsoleFactory.cs`, `Profile.cs`, `InteractionDetector.cs`) unless noted.

## Packages

| Package | What it is | TFMs |
|---|---|---|
| `Spectre.Console` | The library: markup, widgets, prompts, live displays | net10/9/8, netstandard2.0 |
| `Spectre.Console.Ansi` | Low-level ANSI/VT writer + markup parser + `Color`/`Style`/`Decoration` (split out in 0.55; pulled in by `Spectre.Console`) | net10/9/8, netstandard2.0 |
| `Spectre.Console.Cli` | Command-line parsing/command framework. **Separate repo and package** (`spectreconsole/spectre.console.cli`), depends on `Spectre.Console` | net10/9/8, netstandard2.0 |
| `Spectre.Console.Json` | `JsonText` widget | net10/9/8, netstandard2.0 |
| `Spectre.Console.ImageSharp` | `CanvasImage` widget (uses SixLabors.ImageSharp) | net10/9/8 only |
| `Spectre.Console.Testing` | `TestConsole`, `TestConsoleInput` | net10/9/8, netstandard2.0 |
| `Spectre.Console.Cli.Testing` | `CommandAppTester` | net10/9/8, netstandard2.0 |
| `Spectre.Console.Analyzer` | Roslyn analyzer (separate repo `spectreconsole/analyzer`; not covered by this skill's API extraction) | – |

```bash
dotnet add package Spectre.Console
dotnet add package Spectre.Console.Cli      # only for command-line apps
```

All stable packages move in lockstep (0.57.2). The 0.x line is formally pre-release, so
**minor versions can break** — check the project's pinned version before trusting any API
here (see `version.md`). `Spectre.Console.Cli` is heading to 1.0 (alpha on NuGet) with its own
breaking changes.

`Spectre.Console` is trim/AOT-compatible; **`Spectre.Console.Cli` is not** (reflection;
`[RequiresDynamicCode]`).

## The two entry points

```csharp
// 1. Static facade over a shared global console. Fine for apps.
AnsiConsole.MarkupLine("[green]Hello[/] [bold]world[/]");
AnsiConsole.Write(new Panel("inside a panel"));

// 2. IAnsiConsole instance. Use this for anything you want to unit-test or redirect.
IAnsiConsole console = AnsiConsole.Create(new AnsiConsoleSettings
{
    Ansi = AnsiSupport.Detect,
    ColorSystem = ColorSystemSupport.Detect,
    Out = new AnsiConsoleOutput(Console.Out),
});
console.MarkupLine("[yellow]same API[/]");
```

`AnsiConsole` (static) mirrors `IAnsiConsole` + its extension methods. `AnsiConsole.Console`
is settable if you need to swap the global one (e.g. in tests). Prefer **accepting an
`IAnsiConsole` parameter** (constructor-inject it) rather than calling `AnsiConsole.*`
inside libraries/services — that is what makes code testable (`testing.md`).

Writing:

| Goal | Call |
|---|---|
| Styled text | `console.MarkupLine("[red]x[/]")` (see `markup-and-styling.md`) |
| Plain text, no markup parsing | `console.WriteLine("a [b] c")` or `console.Write(new Text("..."))` |
| Any widget | `console.Write(renderable)` |
| Exception | `console.WriteException(ex, ExceptionFormats.ShortenPaths \| ExceptionFormats.ShortenTypes)` |
| Blank line | `console.WriteLine()` |
| Clear | `console.Clear()` |
| Raw ANSI/VT | `console.WriteAnsi(w => w.Write(...))` — see `ansi-and-console-extensions.md` |

`Write(string)` / `WriteLine(string)` do **not** parse markup; `Markup*` do.

## Capabilities and what the console auto-detects

`console.Profile.Capabilities` (type `Capabilities`) holds:

| Capability | Meaning |
|---|---|
| `ColorSystem` | `NoColors`, `Legacy` (8), `Standard` (16), `EightBit` (256), `TrueColor` — colors are down-converted automatically |
| `Ansi` | terminal understands escape codes |
| `Links` | hyperlinks (`[link=...]`) |
| `Interactive` | someone can answer prompts / input available |
| `Unicode` | box-drawing / spinner glyphs OK; otherwise ASCII borders and spinners |
| `Legacy` | old Windows console |
| `AlternateBuffer` | alternate screen buffer available |

`Interactive` is `true` only if stdin, stdout **and** stderr are all non-redirected
(`InteractionDetector`). CI systems are detected (GitHub Actions: ANSI on, Links/Interactive
off; Azure Pipelines, GitLab, Jenkins, Travis, TeamCity, AppVeyor, Bitbucket, CircleCI, Bamboo,
Bitrise, GoCD, MyGet, Continua: Interactive off).

Env vars: `NO_COLOR` (any value → no colors), `COLORTERM=truecolor|24bit`, `TERM`,
`ConEmuANSI=On`. Override with `AnsiConsoleSettings` (`Ansi`, `ColorSystem`, `Interactive`,
`Out`, `EnvironmentVariables`, `Enrichment`, `ExclusivityMode`).

Consequences you must code for:

- **Prompts throw in non-interactive mode**: `InvalidOperationException: Failed to read
  input in non-interactive mode.` (text/confirm) or `NotSupportedException: Cannot show selection
  prompt since the current terminal isn't interactive.` (list prompts). Guard with
  `if (!console.Profile.Capabilities.Interactive) { /* use defaults or fail with a message */ }`.
- **Redirected output has no width**: use `console.Profile.Width` (explicitly settable) or
  `.Width(n)` on a widget if layout must be deterministic in logs.
- Unicode glyphs need a UTF-8 output encoding on Windows: set
  `Console.OutputEncoding = System.Text.Encoding.UTF8;` early if you see `?` or boxes.

```csharp
if (!AnsiConsole.Profile.Capabilities.Interactive)
{
    AnsiConsole.MarkupLine("[yellow]Non-interactive: using defaults.[/]");
}
AnsiConsole.Profile.Width = 100; // force a width (e.g. for log files)
```

## One interactive thing at a time (exclusivity)

Prompts, `Status`, `Progress` and `LiveDisplay` each take an exclusivity lock. Starting one
while another is running (including from another thread, or writing prompts from inside a
`Progress` callback) throws:

> `InvalidOperationException: Trying to run one or more interactive functions concurrently. Operations with dynamic displays (e.g. a prompt and a progress display) cannot be running at the same time.`

Rules of thumb: never prompt inside `Progress`/`Status`/`Live`; update the context
objects (`ProgressTask`, `StatusContext`, `LiveDisplayContext`) from tasks you `await`
inside the callback, and **do not write other output with `console.Write*` while a live
display is active** (it will tear the display). To run your own non-reentrant section:
`console.RunExclusive(() => ...)`.

## Dependency injection pattern

```csharp
public sealed class Reporter(IAnsiConsole console)
{
    public void Done(int count) =>
        console.MarkupLineInterpolated($"[green]Processed[/] {count} items");
}

// Registration (Microsoft.Extensions.DependencyInjection):
//   services.AddSingleton<IAnsiConsole>(_ => AnsiConsole.Console);
//   services.AddSingleton<Reporter>();
```

For tests, register a `TestConsole` instead (see `testing.md`).

## Recording / exporting output

```csharp
var recorder = AnsiConsole.Console.CreateRecorder(); // IAnsiConsole that also records
recorder.MarkupLine("[green]hello[/]");
string text = recorder.ExportText();   // plain text
string html = recorder.ExportHtml();   // styled HTML
```

`console.ToAnsi(renderable)` renders any widget to a string of ANSI text without writing it.

## Alternate screen / cursor

```csharp
AnsiConsole.AlternateScreen(() =>
{
    AnsiConsole.MarkupLine("Full-screen mode. Press any key.");
    Console.ReadKey(true);
});
AnsiConsole.Cursor.Hide();
AnsiConsole.Cursor.Show();
```

## Where to look next

- Styling text: `markup-and-styling.md`
- Widgets (tables, panels, trees, charts, layout): `widgets.md` + `api/widgets/*.md`
- Progress/status/live: `live-displays.md`; user input: `prompts.md`
- Custom widgets: `rendering-and-custom-widgets.md`
- Command-line apps: `cli.md`
- Exact signatures for anything: `api/_index.md` → file
