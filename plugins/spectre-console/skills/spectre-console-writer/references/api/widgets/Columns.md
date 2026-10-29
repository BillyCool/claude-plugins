# widgets/Columns — API (generated from source)

## `public sealed class Columns : Renderable, IPaddable, IExpandable`

*core* · `src/Spectre.Console/Widgets/Columns.cs`

Renders things in columns.

**Constructors**

- `Columns(params IRenderable[] items) : this((IEnumerable<IRenderable>)items)` — Initializes a new instance of the `Columns` class.
- `Columns(IEnumerable<IRenderable> items)` — Initializes a new instance of the `Columns` class.
- `Columns(IEnumerable<string> items)` — Initializes a new instance of the `Columns` class.

**Properties**

- `Padding? Padding { get; set; }` = `new Padding(0, 0, 1, 0)` — Gets or sets the padding.
- `bool Expand { get; set; }` = `true` — Gets or sets a value indicating whether or not the columns should expand to the available space. If `false`, the column width will be auto calculated. Defaults to `true`.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IExpandable`: `Collapse`, `Expand`
- via `IPaddable`: `PadLeft`, `PadTop`, `PadRight`, `PadBottom`, `Padding`
- via `IRenderable`: `GetSegments`

