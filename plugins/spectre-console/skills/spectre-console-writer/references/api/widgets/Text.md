# widgets/Text — API (generated from source)

## `public sealed class Text : Renderable, IHasJustification, IOverflowable`

*core* · `src/Spectre.Console/Widgets/Text.cs`

A renderable piece of text.

**Constructors**

- `Text(string text, Style? style = null)` — Initializes a new instance of the `Text` class.

**Properties**

- `static Text Empty { get; }` = `new Text(string.Empty)` — Gets an empty `Text` instance.
- `static Text NewLine { get; }` = `new Text(Environment.NewLine, Style.Plain)` — Gets an instance of `Text` containing a new line.
- `Justify? Justification { get; set; }` — Gets or sets the text alignment.
- `Overflow? Overflow { get; set; }` — Gets or sets the text overflow strategy.
- `int Length { get; }` — Gets the character count.
- `int Lines { get; }` — Gets the number of lines in the text.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasJustification`: `Justify`, `LeftJustified`, `Centered`, `RightJustified`
- via `IOverflowable`: `Fold`, `Crop`, `Ellipsis`, `Overflow`
- via `IRenderable`: `GetSegments`

