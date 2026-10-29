# widgets/Padder — API (generated from source)

## `public sealed class Padder : Renderable, IPaddable, IExpandable`

*core* · `src/Spectre.Console/Widgets/Padder.cs`

Represents padding around a `IRenderable` object.

**Constructors**

- `Padder(IRenderable child, Padding? padding = null)` — Initializes a new instance of the `Padder` class.

**Properties**

- `Padding? Padding { get; set; }` = `new Padding(1, 1, 1, 1)` — Gets or sets the padding.
- `bool Expand { get; set; }` — Gets or sets a value indicating whether or not the padding should fit the available space. If `false`, the padding width will be auto calculated. Defaults to `false`.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IExpandable`: `Collapse`, `Expand`
- via `IPaddable`: `PadLeft`, `PadTop`, `PadRight`, `PadBottom`, `Padding`
- via `IRenderable`: `GetSegments`

