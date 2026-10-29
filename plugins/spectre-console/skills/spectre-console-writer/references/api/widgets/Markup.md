# widgets/Markup — API (generated from source)

## `public sealed class Markup : Renderable, IHasJustification, IOverflowable`

*core* · `src/Spectre.Console/Widgets/Markup.cs`

A renderable piece of markup text.

**Constructors**

- `Markup(string text, Style? style = null)` — Initializes a new instance of the `Markup` class.

**Properties**

- `Justify? Justification { get; set; }` — Gets or sets the justification.
- `Overflow? Overflow { get; set; }` — Gets or sets the text overflow strategy.
- `int Length { get; }` — Gets the character count.
- `int Lines { get; }` — Gets the number of lines.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.
- `static Markup FromInterpolated(FormattableString value, Style? style = null)` — Returns a new instance of a Markup widget from an interpolated string.
- `static Markup FromInterpolated(IFormatProvider provider, FormattableString value, Style? style = null)` — Returns a new instance of a Markup widget from an interpolated string.
- `static string Escape(string text)` — Escapes text so that it won’t be interpreted as markup.
- `static string Remove(string text)` — Removes markup from the specified string.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasJustification`: `Justify`, `LeftJustified`, `Centered`, `RightJustified`
- via `IOverflowable`: `Fold`, `Crop`, `Ellipsis`, `Overflow`
- via `IRenderable`: `GetSegments`

