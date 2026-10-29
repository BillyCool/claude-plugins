# rendering — API (generated from source)

## `public sealed class Ascii2TableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/Ascii2TableBorder.cs`

Represents another old school ASCII border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class AsciiBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/AsciiBoxBorder.cs`

Represents an old school ASCII border.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class AsciiDoubleHeadTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/AsciiDoubleHeadTableBorder.cs`

Represents an old school ASCII border with a double header border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class AsciiTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/AsciiTableBorder.cs`

Represents an old school ASCII border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class AsciiTreeGuide : TreeGuide`

*core* · `src/Spectre.Console/Rendering/Tree/AsciiTreeGuide.cs`

An ASCII tree guide.

**Methods**

- `override string GetPart(TreeGuidePart part)` — Get the set of characters used to render the corresponding `TreeGuidePart`.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TreeGuide`: `GetSafeTreeGuide`

## `public sealed class BeveledBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/BeveledBoxBorder.cs`

Represents a beveled border using thin block edges and diagonal corners.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class BoldLineTreeGuide : TreeGuide`

*core* · `src/Spectre.Console/Rendering/Tree/BoldLineTreeGuide.cs`

A tree guide made up of bold lines.

**Properties**

- `override TreeGuide? SafeTreeGuide { get; }` — Gets the safe guide lines or `null` if none exist.

**Methods**

- `override string GetPart(TreeGuidePart part)` — Get the set of characters used to render the corresponding `TreeGuidePart`.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TreeGuide`: `GetSafeTreeGuide`

## `public sealed class DashedBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/DashedBoxBorder.cs`

Represents a dashed border with square corners.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class DashedWideBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/DashedWideBoxBorder.cs`

Represents a wide-dashed border with square corners.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class DottedBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/DottedBoxBorder.cs`

Represents a dotted border with square corners.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class DoubleBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/DoubleBoxBorder.cs`

Represents a double border.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class DoubleEdgeTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/DoubleEdgeTableBorder.cs`

Represents a border with a double edge.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class DoubleHorizontalBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/DoubleHorizontalBoxBorder.cs`

Represents a border with double horizontal edges and single vertical edges.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class DoubleLineTreeGuide : TreeGuide`

*core* · `src/Spectre.Console/Rendering/Tree/DoubleLineTreeGuide.cs`

A tree guide made up of double lines.

**Properties**

- `override TreeGuide? SafeTreeGuide { get; }` — Gets the safe guide lines or `null` if none exist.

**Methods**

- `override string GetPart(TreeGuidePart part)` — Get the set of characters used to render the corresponding `TreeGuidePart`.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TreeGuide`: `GetSafeTreeGuide`

## `public sealed class DoubleTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/DoubleTableBorder.cs`

Represents a double border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class DoubleVerticalBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/DoubleVerticalBoxBorder.cs`

Represents a border with double vertical edges and single horizontal edges.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class HeavyBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/HeavyBoxBorder.cs`

Represents a heavy border.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class HeavyDashedBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/HeavyDashedBoxBorder.cs`

Represents a heavy dashed border.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class HeavyDashedWideBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/HeavyDashedWideBoxBorder.cs`

Represents a heavy wide-dashed border.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class HeavyDottedBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/HeavyDottedBoxBorder.cs`

Represents a heavy dotted border.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class HeavyEdgeTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/HeavyEdgeTableBorder.cs`

Represents a border with a heavy edge.

**Properties**

- `override TableBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class HeavyHeadTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/HeavyHeadTableBorder.cs`

Represents a border with a heavy header.

**Properties**

- `override TableBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class HeavyHorizontalBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/HeavyHorizontalBoxBorder.cs`

Represents a border with heavy horizontal edges and light vertical edges.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class HeavyTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/HeavyTableBorder.cs`

Represents a heavy border.

**Properties**

- `override TableBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class HeavyVerticalBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/HeavyVerticalBoxBorder.cs`

Represents a border with heavy vertical edges and light horizontal edges.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class HorizontalTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/HorizontalTableBorder.cs`

Represents a horizontal border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public interface IAnsiConsoleEncoder`

*core* · `src/Spectre.Console/Rendering/IAnsiConsoleEncoder.cs`

Represents a console encoder that can encode recorded segments into a string.

**Methods**

- `string Encode(IAnsiConsole console, IEnumerable<IRenderable> renderable)` — Encodes the specified `IRenderable` enumerator.

## `public interface IHasDirtyState`

*core* · `src/Spectre.Console/Rendering/IHasDirtyState.cs`

Represents something that can be dirty.

**Properties**

- `bool IsDirty { get; }` — Gets a value indicating whether the object is dirty.

## `public interface IRenderHook`

*core* · `src/Spectre.Console/Rendering/IRenderHook.cs`

Represents a render hook.

**Methods**

- `IEnumerable<IRenderable> Process(RenderOptions options, IEnumerable<IRenderable> renderables)` — Processes the specified renderables.

## `public interface IRenderable`

*core* · `src/Spectre.Console/Rendering/IRenderable.cs`

Represents something that can be rendered to the console.

**Methods**

- `Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `GetSegments(IAnsiConsole console) -> IEnumerable<Segment>` — Gets the segments for a renderable using the specified console.

## `public abstract class JustInTimeRenderable : Renderable`

*core* · `src/Spectre.Console/Rendering/JustInTimeRenderable.cs`

Represents something renderable that's reconstructed when its state change in any way.

**Methods**

- `protected sealed override Measurement Measure(RenderOptions context, int maxWidth)` — Measures the renderable object.
- `protected sealed override IEnumerable<Segment> Render(RenderOptions context, int width)` — Renders the object.
- `protected abstract IRenderable Build()` — Builds the inner renderable.
- `protected virtual bool HasDirtyChildren()` — Checks if there are any children that has changed. If so, the underlying renderable needs rebuilding.
- `protected void MarkAsDirty()` — Marks this instance as dirty.
- `protected void MarkAsDirty(Action action)` — Marks this instance as dirty.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IRenderable`: `GetSegments`

## `public sealed class LineTreeGuide : TreeGuide`

*core* · `src/Spectre.Console/Rendering/Tree/LineTreeGuide.cs`

A tree guide made up of lines.

**Methods**

- `override string GetPart(TreeGuidePart part)` — Get the set of characters used to render the corresponding `TreeGuidePart`.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TreeGuide`: `GetSafeTreeGuide`

## `public sealed class MarkdownTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/MarkdownTableBorder.cs`

Represents a Markdown border.

**Properties**

- `override bool SupportsRowSeparator { get; }` — Gets a value indicating whether the border supports row separators or not.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.
- `override string GetColumnRow(TablePart part, IReadOnlyList<int> widths, IReadOnlyList<IColumn> columns)` — Gets a whole column row for the specific column row part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class McGuganHorizontalBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/McGuganHorizontalBoxBorder.cs`

Represents the horizontal variant of the McGugan border, which draws thin block edges inside the content's bounds. Named after Will McGugan.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class McGuganVerticalBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/McGuganVerticalBoxBorder.cs`

Represents the vertical variant of the McGugan border, which draws thin block edges inside the content's bounds. Named after Will McGugan.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public readonly struct Measurement : IEquatable<Measurement>`

*core* · `src/Spectre.Console/Rendering/Measurement.cs`

Represents a measurement.

**Constructors**

- `Measurement(int min, int max)` — Initializes a new instance of the `Measurement` struct.

**Properties**

- `int Min { get; }` — Gets the minimum width.
- `int Max { get; }` — Gets the maximum width.

**Operators / conversions**

- `static bool operator ==(Measurement left, Measurement right)` — Checks if two `Measurement` instances are equal.
- `static bool operator !=(Measurement left, Measurement right)` — Checks if two `Measurement` instances are not equal.

**Methods**

- `override bool Equals(object? obj)`
- `override int GetHashCode()`
- `bool Equals(Measurement other)`

## `public sealed class MinimalDoubleHeadTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/MinimalDoubleHeadTableBorder.cs`

Represents a minimal border with a double header border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class MinimalHeavyHeadTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/MinimalHeavyHeadTableBorder.cs`

Represents a minimal border with a heavy header.

**Properties**

- `override TableBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class MinimalTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/MinimalTableBorder.cs`

Represents a minimal border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class MinimalistTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/MinimalistTableBorder.cs`

Represents a minimalist border.

**Properties**

- `override bool SupportsRowSeparator { get; }` — Gets a value indicating whether the border supports row separators or not.
- `override bool UsePadding { get; }` — Gets a value indicating whether or not the border uses cell padding.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.
- `override string GetColumnRow(TablePart part, IReadOnlyList<int> widths, IReadOnlyList<IColumn> columns)` — Gets a whole column row for the specific column row part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class NearBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/NearBoxBorder.cs`

Represents a "near" border that hugs the content using thin block elements, drawn on the inside edges with empty corners.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class NoBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/NoBoxBorder.cs`

Represents an invisible border.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class NoTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/NoTableBorder.cs`

Represents an invisible border.

**Properties**

- `override bool Visible { get; }` — Gets a value indicating whether or not the border is visible.
- `override bool SupportsRowSeparator { get; }` — Gets a value indicating whether the border supports row separators or not.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class RenderHookScope : IDisposable`

*core* · `src/Spectre.Console/Rendering/RenderHookScope.cs`

Represents a render hook scope.

**Constructors**

- `RenderHookScope(IAnsiConsole console, IRenderHook hook)` — Initializes a new instance of the `RenderHookScope` class.

**Methods**

- `void Dispose()`

## `public record class RenderOptions(IReadOnlyCapabilities Capabilities, Size ConsoleSize)`

*core* · `src/Spectre.Console/Rendering/RenderOptions.cs`

Represents render options.

**Properties**

- `ColorSystem ColorSystem { get; }` — Gets the current color system.
- `bool Ansi { get; }` — Gets a value indicating whether or not VT/Ansi codes are supported.
- `bool Unicode { get; }` — Gets a value indicating whether or not unicode is supported.
- `Justify? Justification { get; init; }` — Gets the current justification.
- `int? Height { get; init; }` — Gets the requested height.

**Methods**

- `static RenderOptions Create(IAnsiConsole console, IReadOnlyCapabilities? capabilities = null)` — Creates a `RenderOptions` instance from a `IAnsiConsole`.

## `public sealed class RenderPipeline`

*core* · `src/Spectre.Console/Rendering/RenderPipeline.cs`

Represents the render pipeline.

**Constructors**

- `RenderPipeline()` — Initializes a new instance of the `RenderPipeline` class.

**Methods**

- `void Attach(IRenderHook hook)` — Attaches a new render hook onto the pipeline.
- `void Detach(IRenderHook hook)` — Detaches a render hook from the pipeline.
- `IEnumerable<IRenderable> Process(RenderOptions options, IEnumerable<IRenderable> renderables)` — Processes the specified renderables.

## `public abstract class Renderable : IRenderable`

*core* · `src/Spectre.Console/Rendering/Renderable.cs`

Base class for a renderable object implementing `IRenderable`.

**Methods**

- `protected virtual Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected abstract IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IRenderable`: `GetSegments`

## `public sealed class RoundedBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/RoundedBoxBorder.cs`

Represents a rounded border.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class RoundedDashedBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/RoundedDashedBoxBorder.cs`

Represents a dashed border with rounded corners.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class RoundedDashedWideBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/RoundedDashedWideBoxBorder.cs`

Represents a wide-dashed border with rounded corners.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class RoundedDottedBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/RoundedDottedBoxBorder.cs`

Represents a dotted border with rounded corners.

**Properties**

- `override BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class RoundedTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/RoundedTableBorder.cs`

Represents a rounded border.

**Properties**

- `override TableBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public class Segment`

*core* · `src/Spectre.Console/Rendering/Segment.cs`

Represents a renderable segment.

**Constructors**

- `Segment(string text) : this(text, Style.Plain)` — Initializes a new instance of the `Segment` class.
- `Segment(string text, Style style, Link? link = null) : this(text, style, link, false, false)` — Initializes a new instance of the `Segment` class.

**Properties**

- `string Text { get; }` — Gets the segment text.
- `bool IsLineBreak { get; }` — Gets a value indicating whether or not this is an explicit line break that should be preserved.
- `bool IsWhiteSpace { get; }` — Gets a value indicating whether or not this is a whitespace that should be preserved but not taken into account when layouting text.
- `bool IsControlCode { get; }` — Gets a value indicating whether or not this is a control code such as cursor movement.
- `Style Style { get; }` — Gets the segment style.
- `Link? Link { get; }` — Gets the segment link.
- `static Segment LineBreak { get; }` = `new Segment(Environment.NewLine, Style.Plain, null, true, false)` — Gets a segment representing a line break.
- `static Segment Empty { get; }` = `new Segment(string.Empty, Style.Plain, null, false, false)` — Gets an empty segment.

**Methods**

- `static Segment Padding(int size)` — Creates padding segment.
- `static Segment Control(string control)` — Creates a control segment.
- `int CellCount()` — Gets the number of cells that this segment occupies in the console.
- `static int CellCount(IEnumerable<Segment> segments)` — Gets the number of cells that the segments occupies in the console.
- `Segment StripLineEndings()` — Returns a new segment without any trailing line endings.
- `(Segment First, Segment? Second) Split(int offset)` — Splits the segment at the offset.
- `Segment Clone()` — Clones the segment.
- `static List<SegmentLine> SplitLines(IEnumerable<Segment> segments)` — Splits the provided segments into lines.
- `static List<SegmentLine> SplitLines(IEnumerable<Segment> segments, int maxWidth, int? height = null)` — Splits the provided segments into lines with a maximum width.
- `static List<Segment> SplitOverflow(Segment segment, Overflow? overflow, int maxWidth)` — Splits an overflowing segment into several new segments.
- `static List<Segment> Truncate(IEnumerable<Segment> segments, int maxWidth)` — Truncates the segments to the specified width.
- `static Segment? Truncate(Segment? segment, int maxWidth)` — Truncates the segment to the specified width.

## `public sealed class SegmentLine : List<Segment>`

*core* · `src/Spectre.Console/Rendering/SegmentLine.cs`

Represents a collection of segments.

**Constructors**

- `SegmentLine()` — Initializes a new instance of the `SegmentLine` class.
- `SegmentLine(IEnumerable<Segment> segments) : base(segments)` — Initializes a new instance of the `SegmentLine` class.

**Properties**

- `int Length { get; }` — Gets the width of the line.

**Methods**

- `int CellCount()` — Gets the number of cells the segment line occupies.
- `void Prepend(Segment segment)` — Preprends a segment to the line.

## `public sealed class SegmentLineEnumerator : IEnumerable<Segment>`

*core* · `src/Spectre.Console/Rendering/SegmentLineEnumerator.cs`

An enumerator for `SegmentLine` collections.

**Constructors**

- `SegmentLineEnumerator(IEnumerable<SegmentLine> lines)` — Initializes a new instance of the `SegmentLineEnumerator` class.

**Methods**

- `IEnumerator<Segment> GetEnumerator()`

## `public sealed class SegmentLineIterator : IEnumerator<Segment>`

*core* · `src/Spectre.Console/Rendering/SegmentLineIterator.cs`

An iterator for `SegmentLine` collections.

**Constructors**

- `SegmentLineIterator(IEnumerable<SegmentLine> lines)` — Initializes a new instance of the `SegmentLineIterator` class.

**Properties**

- `Segment Current { get; private set; }` — Gets the current segment.

**Methods**

- `void Dispose()`
- `bool MoveNext()`
- `void Reset()`

## `public sealed class SimpleHeavyTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/SimpleHeavyTableBorder.cs`

Represents a simple border with heavy lines.

**Properties**

- `override TableBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class SimpleTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/SimpleTableBorder.cs`

Represents a simple border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public sealed class SquareBoxBorder : BoxBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Boxes/SquareBoxBorder.cs`

Represents a square border.

**Methods**

- `override string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `BoxBorder`: `GetSafeBorder`

## `public sealed class SquareTableBorder : TableBorder`

*core* · `src/Spectre.Console/Rendering/Borders/Tables/SquareTableBorder.cs`

Represents a square border.

**Methods**

- `override string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `TableBorder`: `GetSafeBorder`

## `public enum BoxBorderPart`

*core* · `src/Spectre.Console/Rendering/Borders/BoxBorderPart.cs`

Represents the different parts of a box border.

**Values**

- `TopLeft` — The top left part of a box.
- `Top` — The top part of a box.
- `TopRight` — The top right part of a box.
- `Left` — The left part of a box.
- `Right` — The right part of a box.
- `BottomLeft` — The bottom left part of a box.
- `Bottom` — The bottom part of a box.
- `BottomRight` — The bottom right part of a box.

## `public enum TableBorderPart`

*core* · `src/Spectre.Console/Rendering/Borders/TableBorderPart.cs`

Represents the different parts of a table border.

**Values**

- `HeaderTopLeft` — The top left part of a header.
- `HeaderTop` — The top part of a header.
- `HeaderTopSeparator` — The top separator part of a header.
- `HeaderTopRight` — The top right part of a header.
- `HeaderLeft` — The left part of a header.
- `HeaderSeparator` — A header separator.
- `HeaderRight` — The right part of a header.
- `HeaderBottomLeft` — The bottom left part of a header.
- `HeaderBottom` — The bottom part of a header.
- `HeaderBottomSeparator` — The bottom separator part of a header.
- `HeaderBottomRight` — The bottom right part of a header.
- `FooterTopLeft` — The top left part of a footer.
- `FooterTop` — The top part of a footer.
- `FooterTopSeparator` — The top separator part of a footer.
- `FooterTopRight` — The top right part of a footer.
- `CellLeft` — The left part of a cell.
- `CellSeparator` — A cell separator.
- `CellRight` — The right part of a cell.
- `FooterBottomLeft` — The bottom left part of a footer.
- `FooterBottom` — The bottom part of a footer.
- `FooterBottomSeparator` — The bottom separator part of a footer.
- `FooterBottomRight` — The bottom right part of a footer.
- `RowLeft` — The left part of a row.
- `RowCenter` — The center part of a row.
- `RowSeparator` — The separator part of a row.
- `RowRight` — The right part of a row.

## `public enum TablePart`

*core* · `src/Spectre.Console/Rendering/TablePart.cs`

Represents different parts of a table.

**Values**

- `Top` — The top of a table.
- `HeaderSeparator` — The separator between the header and the cells.
- `RowSeparator` — The separator between the rows.
- `FooterSeparator` — The separator between the footer and the cells.
- `Bottom` — The bottom of a table.

## `public enum TreeGuidePart`

*core* · `src/Spectre.Console/Rendering/TreeGuidePart.cs`

Defines the different rendering parts of a `Tree`.

**Values**

- `Space` — Represents a space.
- `Continue` — Connection between siblings.
- `Fork` — Branch from parent to child.
- `End` — Branch from parent to child for the last child in a set.

