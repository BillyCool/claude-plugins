# widgets/Canvas — API (generated from source)

## `public sealed class Canvas : Renderable`

*core* · `src/Spectre.Console/Widgets/Canvas.cs`

Represents a renderable canvas.

**Constructors**

- `Canvas(int width, int height)` — Initializes a new instance of the `Canvas` class.

**Properties**

- `int Width { get; }` — Gets the width of the canvas.
- `int Height { get; }` — Gets the height of the canvas.
- `int? MaxWidth { get; set; }` — Gets or sets the render width of the canvas.
- `bool Scale { get; set; }` = `true` — Gets or sets a value indicating whether or not to scale the canvas when rendering.
- `int PixelWidth { get; set; }` = `2` — Gets or sets the pixel width.

**Methods**

- `Canvas SetPixel(int x, int y, Color color)` — Sets a pixel with the specified color in the canvas at the specified location.
- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IRenderable`: `GetSegments`

