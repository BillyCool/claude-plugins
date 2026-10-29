# widgets/Align — API (generated from source)

## `public sealed class Align : Renderable`

*core* · `src/Spectre.Console/Widgets/Align.cs`

Represents a renderable used to align content.

**Constructors**

- `Align(IRenderable renderable, HorizontalAlignment horizontal, VerticalAlignment? vertical = null)` — Initializes a new instance of the `Align` class.

**Properties**

- `HorizontalAlignment Horizontal { get; set; }` = `HorizontalAlignment.Left` — Gets or sets the horizontal alignment.
- `VerticalAlignment? Vertical { get; set; }` — Gets or sets the vertical alignment.
- `int? Width { get; set; }` — Gets or sets the width.
- `int? Height { get; set; }` — Gets or sets the height.

**Methods**

- `static Align Left(IRenderable renderable, VerticalAlignment? vertical = null)` — Initializes a new instance of the `Align` class that is left aligned.
- `static Align Center(IRenderable renderable, VerticalAlignment? vertical = null)` — Initializes a new instance of the `Align` class that is center aligned.
- `static Align Right(IRenderable renderable, VerticalAlignment? vertical = null)` — Initializes a new instance of the `Align` class that is right aligned.
- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `Width(int? width) -> Align` — Sets the width.
- `Height(int? height) -> Align` — Sets the height.
- `VerticalAlignment(VerticalAlignment? vertical) -> Align` — Sets the vertical alignment.
- `TopAligned() -> Align` — Sets the `Align` object to be top aligned.
- `MiddleAligned() -> Align` — Sets the `Align` object to be middle aligned.
- `BottomAligned() -> Align` — Sets the `Align` object to be bottom aligned.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IRenderable`: `GetSegments`

