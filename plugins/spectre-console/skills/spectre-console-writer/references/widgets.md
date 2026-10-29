# Widgets cookbook

Every widget is an `IRenderable` you pass to `console.Write(...)`. Exact members live in
`api/widgets/<Name>.md`; this file is the *how to choose and compose* layer. All snippets are
compile-checked against the released packages.

Fluent helpers (`.Border(...)`, `.Header(...)`, `.Expand()`, `.PadLeft(...)`) are **extension
methods**: each widget's api page lists which apply, and `api/_shared-extensions.md` lists the
shared ones (`IHasBoxBorder`, `IHasTableBorder`, `IPaddable`, `IExpandable`, `IHasJustification`,
`IOverflowable`, `IHasTreeNodes`, …). Property setters do the same job.

| Need | Widget | API file |
|---|---|---|
| Rows × columns with headers, borders | `Table` | `api/widgets/Table.md` |
| Borderless alignment of label/value pairs, layout cells | `Grid` | `api/widgets/Grid.md` |
| Boxed content with optional header | `Panel` | `api/widgets/Panel.md` |
| Horizontal divider with title | `Rule` | `api/widgets/Rule.md` |
| Hierarchy | `Tree` | `api/widgets/Tree.md` |
| Stack vertically / flow into columns | `Rows`, `Columns` | `api/widgets/Rows.md`, `Columns.md` |
| Split-screen regions (dashboards, live) | `Layout` | `api/widgets/Layout.md` |
| Whitespace / alignment around something | `Padder`, `Align` | `api/widgets/Padder.md`, `Align.md` |
| Charts | `BarChart`, `BreakdownChart` | `api/widgets/Charts.md` |
| Month calendar with marked days | `Calendar` | `api/widgets/Calendar.md` |
| ASCII-art banner | `FigletText` | `api/widgets/Figlet.md` |
| Pixel art / images | `Canvas`, `CanvasImage` (ImageSharp pkg) | `api/widgets/Canvas.md`, `api/imagesharp.md` |
| Pretty JSON | `JsonText` (Json pkg) | `api/json.md` |
| File path with truncation | `TextPath` | `api/widgets/TextPath.md` |
| Exception | `console.WriteException(ex)` / `ex.GetRenderable()` | `api/widgets/Exceptions.md` |
| Plain / styled text | `Text`, `Markup` | `markup-and-styling.md` |

## Table

```csharp
var table = new Table()
    .Title("[bold]Servers[/]")
    .Caption("updated just now")
    .Border(TableBorder.Rounded)
    .BorderColor(Color.Grey)
    .Expand()
    .AddColumn("[yellow]Name[/]")
    .AddColumn(new TableColumn("Status").Centered())
    .AddColumn(new TableColumn("Latency").RightAligned().NoWrap());

table.AddRow("web-01", "[green]up[/]", "12 ms");
table.AddRow(new Markup("[red]db-02[/]"), new Text("down"), new Text("—"));
table.AddRow(new Panel("any widget can be a cell"), new Text("x"), new Text("y"));
table.ShowRowSeparators();

AnsiConsole.Write(table);
```

Notes:
- `AddRow(params string[])` parses each string as **markup** (escape untrusted data!).
- Column count is fixed by the `AddColumn` calls and **columns can't be added once rows exist**
  (`InvalidOperationException: Cannot add new columns to table with existing rows.`). A row with
  more cells than columns (counting `TableCell` spans) throws `InvalidOperationException`; fewer
  cells are padded with empty text.
- `TableColumn.Width`, `.NoWrap()`, `.Padding(...)`, `.Alignment`/`.LeftAligned()/.Centered()/.RightAligned()`,
  `.Footer(...)` (shown if any column has a footer and `ShowFooters`).
- A cell can span columns: `table.AddRow(new TableCell("wide cell").Span(2), new Text("x"))`
  (`TableCell` also converts implicitly from a markup `string`).
- Mutate a table in place for live updates: `table.AddRow(...)`, `table.UpdateCell(row, col, "...")`,
  `table.RemoveRow(i)`, `table.Rows.Clear()` then `ctx.Refresh()` inside a `LiveDisplay`.
- `TableBorder.*` choices: `None, Ascii, Ascii2, AsciiDoubleHead, Square, Rounded, Minimal,
  MinimalHeavyHead, MinimalDoubleHead, Simple, SimpleHeavy, Horizontal, Heavy, HeavyEdge,
  HeavyHead, Double, DoubleEdge, Minimalist, Markdown`. Unicode borders fall back to ASCII on
  non-Unicode consoles unless `UseSafeBorder = false`.
- `Table.Width(n)` / `Expand()`; without either the table shrinks to content and wraps when wider
  than the console.

## Grid (no borders; best for aligned key/value or multi-column layout)

```csharp
var grid = new Grid()
    .AddColumn(new GridColumn().NoWrap().PadRight(4))
    .AddColumn()
    .AddRow("[bold]Name:[/]", "Spectre")
    .AddRow("[bold]Version:[/]", "0.57.2");
AnsiConsole.Write(grid);

// A header row spanning the width, then two panels side by side:
var layoutGrid = new Grid().AddColumns(2);
layoutGrid.AddRow(new Panel("Left").Expand(), new Panel("Right").Expand());
AnsiConsole.Write(layoutGrid.Expand());
```

`Grid.AddRow` requires **at most** `Columns.Count` cells; add columns first (`AddColumn()` /
`AddColumns(n)`).

## Panel

```csharp
var panel = new Panel(new Markup("[green]All systems nominal[/]"))
    .Header("Status", Justify.Center)
    .Border(BoxBorder.Double)
    .BorderColor(Color.Blue)
    .Padding(2, 1)          // horizontal, vertical (also Padding(left, top, right, bottom))
    .Expand();
AnsiConsole.Write(panel);
```

`new Panel("text")` takes markup. Without `.Expand()` the panel is as wide as its content.
`BoxBorder.*` choices: `None, Ascii, Double, Heavy, Rounded, Square, HeavyHorizontal,
HeavyVertical, DoubleHorizontal, DoubleVertical, Dashed, RoundedDashed, HeavyDashed, Dotted,
RoundedDotted, HeavyDotted, DashedWide, RoundedDashedWide, HeavyDashedWide, Near, Beveled,
McGuganHorizontal, McGuganVertical`. Each has a shortcut extension in `api/_shared-extensions.md`
(`.RoundedBorder()`, `.DoubleBorder()`, `.NoBorder()`, …).

## Rule

```csharp
AnsiConsole.Write(new Rule("[yellow]Section[/]").RuleStyle("grey").LeftJustified());
AnsiConsole.Write(new Rule());                   // plain line
AnsiConsole.Write(new Rule("heavy").HeavyBorder());
```

## Tree

```csharp
var tree = new Tree("[bold]solution[/]").Guide(TreeGuide.Line);
var src = tree.AddNode("src");
src.AddNode("Program.cs");
var lib = src.AddNode("[blue]Lib[/]");
lib.AddNode("Thing.cs");
tree.AddNode(new Table().AddColumn("any renderable").AddRow("works as node"));
AnsiConsole.Write(tree);
```

`TreeGuide.Line`, `.Ascii`, `.DoubleLine`, `.BoldLine` (see `api/console.md`). `node.Expanded = false`
hides children. A node instance may appear only once (cycle detection throws `CircularTreeException`).

## Rows, Columns, Padder, Align

```csharp
AnsiConsole.Write(new Rows(new Text("one"), new Rule(), new Panel("two")));

var cards = Enumerable.Range(1, 6).Select(i => new Panel($"Card {i}").Expand());
AnsiConsole.Write(new Columns(cards));               // flows to console width

AnsiConsole.Write(new Padder(new Panel("indented"), new Padding(4, 1, 0, 1)));
AnsiConsole.Write(Align.Center(new Markup("[bold]centered[/]")));
AnsiConsole.Write(new Align(new Panel("bottom right"), HorizontalAlignment.Right, VerticalAlignment.Bottom));
```

`Align` vertical alignment only matters when the host has a height (e.g. inside `Layout`).
`Columns` wraps items to the next line when they don't fit; set `.Collapse()` to size to content
instead of expanding.

## Layout (fixed-height split regions; pair with `LiveDisplay`)

```csharp
var layout = new Layout("Root").SplitColumns(
    new Layout("Left"),
    new Layout("Right").SplitRows(
        new Layout("Top"),
        new Layout("Bottom")));

layout["Left"].Update(new Panel("Left").Expand());
layout["Right"]["Top"].Update(new Panel("Top-right").Expand());
layout["Right"]["Bottom"].Update(new Panel("Bottom-right").Expand());
layout["Left"].Size(30);          // fixed width; others share the rest by .Ratio(n)
AnsiConsole.Write(layout);
```

A `Layout` fills the **console height** (use `layout.Ratio`, `.Size`, `.MinimumSize`, `IsVisible`).
When written to a non-live console it takes up the entire window height — normally it's the target
of a `LiveDisplay` (see `live-displays.md`).

## Charts

```csharp
AnsiConsole.Write(new BarChart()
    .Width(60)
    .Label("[green bold underline]Downloads[/]")
    .CenterLabel()
    .AddItem("net8", 120, Color.Yellow)
    .AddItem("net9", 340, Color.Green)
    .AddItem("net10", 80, Color.Red));

AnsiConsole.Write(new BreakdownChart()
    .Width(60)
    .AddItem("C#", 70, Color.Green)
    .AddItem("Razor", 20, Color.Blue)
    .AddItem("Other", 10, Color.Grey));
```

`BarChart.WithMaxValue(n)` pins the scale (otherwise the largest value fills the width).
`BreakdownChart.ShowTags()/HideTags()/ShowTagValues()`, `.FullSize()`/`.Compact`.

## Calendar

```csharp
var cal = new Calendar(2026, 10)
    .AddCalendarEvent(2026, 10, 15)
    .AddCalendarEvent("Release", 2026, 10, 30)
    .HighlightStyle(Style.Parse("yellow bold"))
    .Border(TableBorder.Rounded);
AnsiConsole.Write(cal);
```

`Calendar.Culture` controls month/day names and first day of week. (`RemoveCalendarEvent` exists on
`main` after 0.57.2 — not in the release.)

## FigletText, Canvas, TextPath

```csharp
AnsiConsole.Write(new FigletText("Spectre").Centered().Color(Color.Aqua));
// custom font: new FigletText(FigletFont.Load("doom.flf"), "text")

var canvas = new Canvas(16, 8);
for (var x = 0; x < 16; x++)
    canvas.SetPixel(x, x / 2, Color.Red);
AnsiConsole.Write(canvas);

AnsiConsole.Write(new TextPath("/usr/local/share/very/long/path/to/file.txt")
    .RootColor(Color.Red).SeparatorColor(Color.Grey).StemColor(Color.Blue).LeafColor(Color.Green));
```

`FigletText` is fixed to ASCII glyphs of the font; wide text overflows narrow consoles — use
`.Fitted()` / `.Smushed()` layout modes or a shorter string. Default font is the embedded
"Standard".

## JsonText (package `Spectre.Console.Json`)

```csharp
AnsiConsole.Write(new JsonText("""{ "name": "spectre", "tags": ["a","b"], "n": 1, "ok": true }""")
    .MemberColor(Color.Aqua)
    .StringColor(Color.Green)
    .NumberColor(Color.Yellow));
```

## CanvasImage (package `Spectre.Console.ImageSharp`)

```csharp-fragment
var image = new CanvasImage("logo.png").MaxWidth(40);
AnsiConsole.Write(image);
```

## Exceptions

```csharp
try { throw new InvalidOperationException("boom"); }
catch (Exception ex)
{
    AnsiConsole.WriteException(ex, ExceptionFormats.ShortenPaths | ExceptionFormats.ShortenTypes);
    // or compose: AnsiConsole.Write(new Panel(ex.GetRenderable()).Header("Error"));
}
```

`ExceptionFormats` is `[Flags]`: `Default=0, ShortenPaths=1, ShortenTypes=2, ShortenMethods=4,
ShowLinks=8, ShortenEverything (=Methods|Types|Paths), NoStackTrace=16`. For per-part styling use
`ExceptionSettings` (`api/widgets/Exceptions.md`).

## Cross-cutting behaviour worth remembering

- **Width resolution**: widgets measure against the console width (`Profile.Width`), shrink-wrap
  unless `Expand`/`Width` is set, and wrap/ellipsize text per `Overflow`. Test with a narrow
  `TestConsole().Width(40)` to catch layout bugs.
- **Nesting is free**: anything `IRenderable` can be a cell, panel body, tree node, layout region.
- **Mutable vs immutable**: `Table`, `Tree`, `Grid`, `Layout`, charts are mutable; `Markup`/`Text` are
  not. For live updates either mutate + `ctx.Refresh()` or swap with `ctx.UpdateTarget(newRenderable)`.
- **`JustInTimeRenderable`** types (`Grid`, `Calendar`, `JsonText`) rebuild their inner renderable
  lazily when a child changes.
