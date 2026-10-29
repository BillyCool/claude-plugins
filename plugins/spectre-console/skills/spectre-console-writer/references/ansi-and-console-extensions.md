# Spectre.Console.Ansi: AnsiWriter, AnsiMarkup, System.Console extensions

Since 0.55 the ANSI/VT layer is its own package, `Spectre.Console.Ansi` (a dependency of
`Spectre.Console`; also usable alone for tiny tools that want colors/markup without widgets).
Verified against `src/Spectre.Console.Ansi/**` (0.57.2). Members: `api/ansi.md`.

It contains: `AnsiWriter`, `AnsiMarkup`, `AnsiCapabilities` / `AnsiWriterSettings`, `AnsiSupport`,
`ColorSystem`, `Color`, `Style`, `Decoration`, `Link`, and `SystemConsoleExtensions`.

## AnsiWriter

```csharp
var writer = new AnsiWriter(Console.Out);      // detects capabilities from the writer/environment
writer
    .BeginLink("https://spectreconsole.net", linkId: 123)
    .Decoration(Decoration.Bold | Decoration.Italic)
    .Foreground(Color.Yellow)
    .Write("Spectre Console")
    .ResetStyle()
    .EndLink()
    .WriteLine();

writer.Write("styled", new Style(Color.Red, decoration: Decoration.Underline)).WriteLine();
writer.CursorUp(1).EraseInLine(2).Write("overwritten line").WriteLine();
```

- Fluent: each call returns the writer. Besides text/colors/links it exposes the VT cursor and
  screen primitives (`CursorPosition`, `CursorUp/Down/Left/Right`, `Save/RestoreCursor`,
  `Show/HideCursor`, `EnterAltScreen/ExitAltScreen`, `EraseInLine/EraseInDisplay`, `ClearScrollback`,
  `InsertLine/DeleteLine`, `ScrollUp/Down`, …).
- **Creating an `AnsiWriter` with auto-detection is expensive: create one and reuse it.**
- Capabilities-aware: with `Ansi = false` styling calls emit nothing (plain text only) and colors
  are down-converted to the `ColorSystem` (e.g. `EightBit` → `ESC[38;5;9m`). Note that a bare
  `StringWriter` is auto-detected as **ANSI-capable**, so pass explicit capabilities when you
  want deterministic output:

```csharp
var forced = new AnsiWriter(
    new StringWriter(),
    new AnsiCapabilities { Ansi = true, Links = true, ColorSystem = ColorSystem.TrueColor, AlternateBuffer = true });
```

- Inside a full console, reach the same thing through `console.WriteAnsi(w => w.Foreground(Color.Red).Write("x").ResetStyle())`
  (the console's own writer/capabilities; keeps output ordering with widgets).

## AnsiMarkup

```csharp
var writer = new AnsiWriter(Console.Out);
var markup = new AnsiMarkup(writer);
markup.Write("[yellow bold italic link=https://spectreconsole.net]Spectre.Console[/]");
markup.WriteLine("[green]done[/]");

IEnumerable<AnsiMarkupSegment> parts = AnsiMarkup.Parse("[red]a[/] b");  // text + Style + Link per run
string safe = AnsiMarkup.Escape("[not markup]");
string plain = AnsiMarkup.Remove("[red]a[/] b");
```

Same grammar as `markup-and-styling.md` (that file is the authoritative description — it is
implemented by `AnsiMarkup`/`AnsiMarkupTagParser` in this package).

## System.Console extensions (.NET 10 / C# 14)

`SystemConsoleExtensions` uses C# 14 *extension members* on the static `System.Console` class,
so no Spectre console instance is needed (shares one default `AnsiWriter` over `Console.Out`):

```csharp
Console.Markup("[yellow]Hello[/] ");
Console.MarkupLine("[blue]World[/]");
Console.Ansi(w => w.Foreground(Color.Aqua).Write("raw ansi").ResetStyle());
```

Requires the .NET 10 SDK with `<LangVersion>14</LangVersion>` (default on net10.0) and a
`using Spectre.Console;`. On older SDKs use `AnsiConsole` or your own `AnsiWriter`/`AnsiMarkup`.
These are minimal helpers: they have no widgets, no markup escaping helpers beyond
`AnsiMarkup.Escape`, and no interactive features.
