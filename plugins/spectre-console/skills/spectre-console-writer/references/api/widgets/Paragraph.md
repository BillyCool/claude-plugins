# widgets/Paragraph — API (generated from source)

## `public sealed class Paragraph : Renderable, IHasJustification, IOverflowable`

*core* · `src/Spectre.Console/Widgets/Paragraph.cs`

A paragraph of text where different parts of the paragraph can have individual styling.

**Constructors**

- `Paragraph()` — Initializes a new instance of the `Paragraph` class.
- `Paragraph(string text, Style? style = null, Link? link = null) : this()` — Initializes a new instance of the `Paragraph` class.

**Properties**

- `Justify? Justification { get; set; }` — Gets or sets the alignment of the whole paragraph.
- `Overflow? Overflow { get; set; }` — Gets or sets the text overflow strategy.
- `int Length { get; }` — Gets the character count of the paragraph.
- `int Lines { get; }` — Gets the number of lines in the paragraph.

**Methods**

- `Paragraph Append(string text, Style? style = null, Link? link = null)` — Appends some text to this paragraph.
- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasJustification`: `Justify`, `LeftJustified`, `Centered`, `RightJustified`
- via `IOverflowable`: `Fold`, `Crop`, `Ellipsis`, `Overflow`
- via `IRenderable`: `GetSegments`

