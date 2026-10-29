# widgets/Rows — API (generated from source)

## `public sealed class Rows : Renderable, IExpandable`

*core* · `src/Spectre.Console/Widgets/Rows.cs`

Renders things in rows.

**Constructors**

- `Rows(params IRenderable[] items) : this((IEnumerable<IRenderable>)items)` — Initializes a new instance of the `Rows` class.
- `Rows(IEnumerable<IRenderable> children)` — Initializes a new instance of the `Rows` class.

**Properties**

- `bool Expand { get; set; }` — Gets or sets a value indicating whether or not the object should expand to the available space. If `false`, the object's width will be auto calculated.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IExpandable`: `Collapse`, `Expand`
- via `IRenderable`: `GetSegments`

