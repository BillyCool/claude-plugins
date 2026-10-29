# widgets/Figlet — API (generated from source)

## `public sealed class FigletFont`

*core* · `src/Spectre.Console/Widgets/Figlet/FigletFont.cs`

Represents a Figlet font.

**Properties**

- `int Count { get; }` — Gets the number of characters in the font.
- `int Height { get; }` — Gets the height of the font.
- `int Baseline { get; }` — Gets the font's baseline.
- `int MaxWidth { get; }` — Gets the font's maximum width.
- `char Hardblank { get; }` — Gets the hardblank character used in this font's glyph definitions. Hardblanks are rendered as spaces in output but are treated as opaque (non-space) characters during fitting and smushing.
- `int SmushingRules { get; }` — Gets the horizontal smushing rules encoded as bit flags (bits 0–5, values 1–32). A value of 0 means universal smushing (any two non-space characters smush, right wins).
- `static FigletFont Default { get; }` — Gets the default Figlet font.

**Methods**

- `static FigletFont Load(Stream stream)` — Loads a Figlet font from the specified stream.
- `static FigletFont Load(string path)` — Loads a Figlet font from disk.
- `static FigletFont Parse(string source)` — Parses a Figlet font from the specified `string`.

## `public sealed class FigletText : Renderable, IHasJustification`

*core* · `src/Spectre.Console/Widgets/Figlet/FigletText.cs`

Represents text rendered with a Figlet font.

**Constructors**

- `FigletText(string text) : this(FigletFont.Default, text)` — Initializes a new instance of the `FigletText` class.
- `FigletText(FigletFont font, string text)` — Initializes a new instance of the `FigletText` class.

**Properties**

- `Color? Color { get; set; }` — Gets or sets the color of the text.
- `Justify? Justification { get; set; }` — Gets or sets the justification.
- `bool Pad { get; set; }` — Gets or sets a value indicating whether or not the right side should be padded.
- `FigletLayoutMode LayoutMode { get; set; }` — Gets or sets the Figlet layout mode.

**Methods**

- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `Color(Color? color) -> FigletText` — Sets the color of the Figlet text.
- `LayoutMode(FigletLayoutMode mode) -> FigletText` — Sets the Figlet layout mode.
- `FullSize() -> FigletText` — Sets the Figlet layout mode to `FullSize`.
- `Fitted() -> FigletText` — Sets the Figlet layout mode to `Fitted`.
- `Smushed() -> FigletText` — Sets the Figlet layout mode to `Smushed`.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasJustification`: `Justify`, `LeftJustified`, `Centered`, `RightJustified`
- via `IRenderable`: `GetSegments`

## `public enum FigletLayoutMode`

*core* · `src/Spectre.Console/Widgets/Figlet/FigletLayoutMode.cs`

Represents the different Figlet layout modes.

**Values**

- `FullSize = 0` — Represents each Figlet character occupying the full width or height of its arrangement of sub-characters as designed.
- `Fitted = 1` — Characters are rendered touching each other by removing trailing and leading spaces at character boundaries (kerning).
- `Smushed = 2` — Boundary characters are merged according to the standard Figlet smushing rules. Smushing implies fitting.

