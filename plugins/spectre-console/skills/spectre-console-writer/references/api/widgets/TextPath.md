# widgets/TextPath — API (generated from source)

## `public sealed class TextPath : IRenderable, IHasJustification`

*core* · `src/Spectre.Console/Widgets/TextPath.cs`

Representation of a file system path.

**Constructors**

- `TextPath(string path)` — Initializes a new instance of the `TextPath` class.

**Properties**

- `Style? RootStyle { get; set; }` — Gets or sets the root style.
- `Style? SeparatorStyle { get; set; }` — Gets or sets the separator style.
- `Style? StemStyle { get; set; }` — Gets or sets the stem style.
- `Style? LeafStyle { get; set; }` — Gets or sets the leaf style.
- `Justify? Justification { get; set; }` — Gets or sets the alignment.

**Methods**

- `Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `SeparatorStyle(Style style) -> TextPath` — Sets the separator style.
- `SeparatorColor(Color color) -> TextPath` — Sets the separator color.
- `RootStyle(Style style) -> TextPath` — Sets the root style.
- `RootColor(Color color) -> TextPath` — Sets the root color.
- `StemStyle(Style style) -> TextPath` — Sets the stem style.
- `StemColor(Color color) -> TextPath` — Sets the stem color.
- `LeafStyle(Style style) -> TextPath` — Sets the leaf style.
- `LeafColor(Color color) -> TextPath` — Sets the leaf color.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasJustification`: `Justify`, `LeftJustified`, `Centered`, `RightJustified`
- via `IRenderable`: `GetSegments`

