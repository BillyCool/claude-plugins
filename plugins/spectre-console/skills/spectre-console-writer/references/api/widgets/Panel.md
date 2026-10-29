# widgets/Panel — API (generated from source)

## `public sealed class Panel : Renderable, IHasBoxBorder, IHasBorder, IExpandable, IPaddable`

*core* · `src/Spectre.Console/Widgets/Panel.cs`

A renderable panel.

**Constructors**

- `Panel(string text) : this(new Markup(text))` — Initializes a new instance of the `Panel` class.
- `Panel(IRenderable content)` — Initializes a new instance of the `Panel` class.

**Properties**

- `BoxBorder Border { get; set; }` = `BoxBorder.Square` — Gets or sets the box.
- `bool UseSafeBorder { get; set; }` = `true` — Gets or sets a value indicating whether or not to use a "safe" border on legacy consoles that might not be able to render non-ASCII characters.
- `Style? BorderStyle { get; set; }` — Gets or sets the box style.
- `bool Expand { get; set; }` — Gets or sets a value indicating whether or not the panel should fit the available space. If `false`, the panel width will be auto calculated. Defaults to `false`.
- `Padding? Padding { get; set; }` = `new Padding(1, 0, 1, 0)` — Gets or sets the padding.
- `PanelHeader? Header { get; set; }` — Gets or sets the header.
- `int? Width { get; set; }` — Gets or sets the width of the panel.
- `int? Height { get; set; }` — Gets or sets the height of the panel.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `Header(string text, Justify? alignment = null) -> Panel` — Sets the panel header.
- `HeaderAlignment(Justify alignment) -> Panel` — Sets the panel header alignment.
- `Header(PanelHeader header) -> Panel` — Sets the panel header.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IExpandable`: `Collapse`, `Expand`
- via `IHasBorder`: `SafeBorder`, `NoSafeBorder`, `BorderStyle`, `BorderColor`
- via `IHasBoxBorder`: `Border`, `NoBorder`, `SquareBorder`, `AsciiBorder`, `RoundedBorder`, `HeavyBorder`, `DoubleBorder`, `HeavyHorizontalBorder`, `HeavyVerticalBorder`, `DoubleHorizontalBorder`, `DoubleVerticalBorder`, `DashedBorder`, `RoundedDashedBorder`, `HeavyDashedBorder`, `DottedBorder`, `RoundedDottedBorder`, `HeavyDottedBorder`, `DashedWideBorder`, `RoundedDashedWideBorder`, `HeavyDashedWideBorder`, `NearBorder`, `BeveledBorder`, `McGuganHorizontalBorder`, `McGuganVerticalBorder`
- via `IPaddable`: `PadLeft`, `PadTop`, `PadRight`, `PadBottom`, `Padding`
- via `IRenderable`: `GetSegments`

## `public sealed class PanelHeader : IHasJustification`

*core* · `src/Spectre.Console/Widgets/PanelHeader.cs`

Represents a panel header.

**Constructors**

- `PanelHeader(string text, Justify? alignment = null)` — Initializes a new instance of the `PanelHeader` class.

**Properties**

- `string Text { get; }` — Gets the panel header text.
- `Justify? Justification { get; set; }` — Gets or sets the panel header alignment.

**Methods**

- `PanelHeader SetStyle(Style? style)` — Sets the panel header style.
- `PanelHeader SetStyle(string style)` — Sets the panel header style.
- `PanelHeader SetAlignment(Justify alignment)` — Sets the panel header alignment.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasJustification`: `Justify`, `LeftJustified`, `Centered`, `RightJustified`

