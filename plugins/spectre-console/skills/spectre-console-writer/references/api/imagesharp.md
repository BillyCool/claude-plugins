# imagesharp — API (generated from source)

## `public sealed class CanvasImage : Renderable`

*imagesharp* · `src/Extensions/Spectre.Console.ImageSharp/CanvasImage.cs`

Represents a renderable image.

**Constructors**

- `CanvasImage(string filename)` — Initializes a new instance of the `CanvasImage` class.
- `CanvasImage(ReadOnlySpan<byte> data)` — Initializes a new instance of the `CanvasImage` class.
- `CanvasImage(Stream data)` — Initializes a new instance of the `CanvasImage` class.

**Properties**

- `int Width { get; }` — Gets the image width.
- `int Height { get; }` — Gets the image height.
- `int? MaxWidth { get; set; }` — Gets or sets the render width of the canvas.
- `int PixelWidth { get; set; }` = `2` — Gets or sets the render width of the canvas.
- `IResampler? Resampler { get; set; }` — Gets or sets the `IResampler` that should be used when scaling the image. Defaults to bicubic sampling.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `MaxWidth(int? maxWidth) -> CanvasImage` — Sets the maximum width of the rendered image.
- `NoMaxWidth() -> CanvasImage` — Disables the maximum width of the rendered image.
- `PixelWidth(int width) -> CanvasImage` — Sets the pixel width.
- `Mutate(Action<IImageProcessingContext> action) -> CanvasImage` — Mutates the underlying image.
- `BicubicResampler() -> CanvasImage` — Uses a bicubic sampler that implements the bicubic kernel algorithm W(x).
- `BilinearResampler() -> CanvasImage` — Uses a bilinear sampler. This interpolation algorithm can be used where perfect image transformation with pixel matching is impossible, so that one can calculate and assign appropriate intensity values to pixels.
- `NearestNeighborResampler() -> CanvasImage` — Uses a Nearest-Neighbour sampler that implements the nearest neighbor algorithm. This uses a very fast, unscaled filter which will select the closest pixel to the new pixels position.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IRenderable`: `GetSegments`

