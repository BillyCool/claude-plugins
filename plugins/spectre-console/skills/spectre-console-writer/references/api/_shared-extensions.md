# Shared extension methods (generated from source)

Extension methods that apply to every type implementing/deriving from the heading's interface or base. `-> T` means the call returns the same widget so calls chain.

## via `BoxBorder`

- `GetSafeBorder(bool safe) -> BoxBorder` — Gets the safe border for a border.

## via `Exception`

- `GetRenderable(ExceptionFormats format = ExceptionFormats.Default) -> IRenderable` — Gets a `IRenderable` representation of the exception.
- `GetRenderable(ExceptionSettings settings) -> IRenderable` — Gets a `IRenderable` representation of the exception.

## via `IAlignable`

- `Alignment<T>(Justify? alignment) -> T` — Sets the alignment for an `IAlignable` object.
- `Centered<T>() -> T` — Sets the `IAlignable` object to be centered.
- `LeftAligned<T>() -> T` — Sets the `IAlignable` object to be left aligned.
- `RightAligned<T>() -> T` — Sets the `IAlignable` object to be right aligned.

## via `IAnsiConsole`

- `AlternateScreen(Action action) -> void` — Switches to an alternate screen buffer if the terminal supports it.
- `Ask<T>(string prompt) -> T` — Displays a prompt to the user.
- `Ask<T>(string prompt, CultureInfo? culture) -> T` — Displays a prompt to the user.
- `AskAsync<T>(string prompt, CancellationToken cancellationToken = default) -> Task<T>` — Displays a prompt to the user.
- `AskAsync<T>(string prompt, CultureInfo? culture, CancellationToken cancellationToken = default) -> Task<T>` — Displays a prompt to the user.
- `Clear() -> void` — Clears the console.
- `Confirm(string prompt, bool defaultValue = true) -> bool` — Displays a prompt with two choices, yes or no.
- `ConfirmAsync(string prompt, bool defaultValue = true, CancellationToken cancellationToken = default) -> Task<bool>` — Displays a prompt with two choices, yes or no.
- `CreateRecorder() -> Recorder` — Creates a recorder for the specified console.
- `Live(IRenderable target) -> LiveDisplay` — Creates a new `LiveDisplay` instance for the console.
- `Markup(IFormatProvider provider, string format, params object[] args) -> void` — Writes the specified markup to the console.
- `Markup(string format, params object[] args) -> void` — Writes the specified markup to the console.
- `Markup(string value) -> void` — Writes the specified markup to the console.
- `MarkupInterpolated(FormattableString value) -> void` — Writes the specified markup to the console. All interpolation holes which contain a string are automatically escaped.
- `MarkupInterpolated(IFormatProvider provider, FormattableString value) -> void` — Writes the specified markup to the console. All interpolation holes which contain a string are automatically escaped.
- `MarkupLine(IFormatProvider provider, string format, params object[] args) -> void` — Writes the specified markup, followed by the current line terminator, to the console.
- `MarkupLine(string format, params object[] args) -> void` — Writes the specified markup, followed by the current line terminator, to the console.
- `MarkupLine(string value) -> void` — Writes the specified markup, followed by the current line terminator, to the console.
- `MarkupLineInterpolated(FormattableString value) -> void` — Writes the specified markup, followed by the current line terminator, to the console. All interpolation holes which contain a string are automatically escaped.
- `MarkupLineInterpolated(IFormatProvider provider, FormattableString value) -> void` — Writes the specified markup, followed by the current line terminator, to the console. All interpolation holes which contain a string are automatically escaped.
- `Progress() -> Progress` — Creates a new `Progress` instance for the console.
- `Prompt<T>(IPrompt<T> prompt) -> T` — Displays a prompt to the user.
- `PromptAsync<T>(IPrompt<T> prompt, CancellationToken cancellationToken = default) -> Task<T>` — Displays a prompt to the user.
- `RunExclusive<T>(Func<T> func) -> T` — Runs the specified function in exclusive mode.
- `RunExclusive<T>(Func<Task<T>> func) -> Task<T>` — Runs the specified function in exclusive mode asynchronously.
- `Status() -> Status` — Creates a new `Status` instance for the console.
- `ToAnsi(IRenderable renderable) -> string` — Gets the VT/ANSI control code sequence for a `IRenderable`.
- `Write(string text) -> void` — Writes the specified string value to the console.
- `Write(string text, Style? style) -> void` — Writes the specified string value to the console.
- `WriteAnsi(string sequence) -> void` — Writes a VT/Ansi control code sequence to the console (if supported).
- `WriteException(Exception exception, ExceptionFormats format = ExceptionFormats.Default) -> void` — Writes an exception to the console.
- `WriteException(Exception exception, ExceptionSettings settings) -> void` — Writes an exception to the console.
- `WriteLine() -> void` — Writes an empty line to the console.
- `WriteLine(string text) -> void` — Writes the specified string value, followed by the current line terminator, to the console.
- `WriteLine(string text, Style? style) -> void` — Writes the specified string value, followed by the current line terminator, to the console.

## via `IColumn`

- `NoWrap<T>() -> T` — Prevents a column from wrapping.
- `Width<T>(int? width) -> T` — Sets the width of the column.

## via `IExpandable`

- `Collapse<T>() -> T` — Tells the specified object to not expand to the available area but take as little space as possible.
- `Expand<T>() -> T` — Tells the specified object to expand to the available area.

## via `IHasBorder`

- `BorderColor<T>(Color color) -> T` — Sets the border color.
- `BorderStyle<T>(Style style) -> T` — Sets the border style.
- `NoSafeBorder<T>() -> T` — Disables the safe border.
- `SafeBorder<T>() -> T` — Enables the safe border.

## via `IHasBoxBorder`

- `AsciiBorder<T>() -> T` — Display an ASCII border.
- `BeveledBorder<T>() -> T` — Display a beveled border using thin block edges and diagonal corners.
- `Border<T>(BoxBorder border) -> T` — Sets the border.
- `DashedBorder<T>() -> T` — Display a dashed border with square corners.
- `DashedWideBorder<T>() -> T` — Display a wide-dashed border with square corners.
- `DottedBorder<T>() -> T` — Display a dotted border with square corners.
- `DoubleBorder<T>() -> T` — Display a double border.
- `DoubleHorizontalBorder<T>() -> T` — Display a border with double horizontal edges and single vertical edges.
- `DoubleVerticalBorder<T>() -> T` — Display a border with double vertical edges and single horizontal edges.
- `HeavyBorder<T>() -> T` — Display a heavy border.
- `HeavyDashedBorder<T>() -> T` — Display a heavy dashed border.
- `HeavyDashedWideBorder<T>() -> T` — Display a heavy wide-dashed border.
- `HeavyDottedBorder<T>() -> T` — Display a heavy dotted border.
- `HeavyHorizontalBorder<T>() -> T` — Display a border with heavy horizontal edges and light vertical edges.
- `HeavyVerticalBorder<T>() -> T` — Display a border with heavy vertical edges and light horizontal edges.
- `McGuganHorizontalBorder<T>() -> T` — Display the horizontal variant of the McGugan border.
- `McGuganVerticalBorder<T>() -> T` — Display the vertical variant of the McGugan border.
- `NearBorder<T>() -> T` — Display a "near" border that hugs the content using thin block elements.
- `NoBorder<T>() -> T` — Do not display a border.
- `RoundedBorder<T>() -> T` — Display a rounded border.
- `RoundedDashedBorder<T>() -> T` — Display a dashed border with rounded corners.
- `RoundedDashedWideBorder<T>() -> T` — Display a wide-dashed border with rounded corners.
- `RoundedDottedBorder<T>() -> T` — Display a dotted border with rounded corners.
- `SquareBorder<T>() -> T` — Display a square border.

## via `IHasCulture`

- `Culture<T>(CultureInfo culture) -> T` — Sets the culture.
- `Culture<T>(int culture) -> T` — Sets the culture.
- `Culture<T>(string name) -> T` — Sets the culture.

## via `IHasJustification`

- `Centered<T>() -> T` — Sets the `IHasJustification` object to be centered.
- `Justify<T>(Justify? alignment) -> T` — Sets the justification for an `IHasJustification` object.
- `LeftJustified<T>() -> T` — Sets the `IHasJustification` object to be left justified.
- `RightJustified<T>() -> T` — Sets the `IHasJustification` object to be right justified.

## via `IHasTableBorder`

- `Ascii2Border<T>() -> T` — Display another ASCII border.
- `AsciiBorder<T>() -> T` — Display an ASCII border.
- `AsciiDoubleHeadBorder<T>() -> T` — Display an ASCII border with a double header border.
- `Border<T>(TableBorder border) -> T` — Sets the border.
- `DoubleBorder<T>() -> T` — Display a double border.
- `DoubleEdgeBorder<T>() -> T` — Display a border with a double edge.
- `HeavyBorder<T>() -> T` — Display a heavy border.
- `HeavyEdgeBorder<T>() -> T` — Display a border with a heavy edge.
- `HeavyHeadBorder<T>() -> T` — Display a border with a heavy header.
- `HorizontalBorder<T>() -> T` — Display a simple border.
- `MarkdownBorder<T>() -> T` — Display a markdown border.
- `MinimalBorder<T>() -> T` — Display a minimal border.
- `MinimalDoubleHeadBorder<T>() -> T` — Display a minimal border with a double header border.
- `MinimalHeavyHeadBorder<T>() -> T` — Display a minimal border with a heavy head.
- `MinimalistBorder<T>() -> T` — Display a minimalist border.
- `NoBorder<T>() -> T` — Do not display a border.
- `RoundedBorder<T>() -> T` — Display a rounded border.
- `SimpleBorder<T>() -> T` — Display a simple border.
- `SimpleHeavyBorder<T>() -> T` — Display a simple border with heavy lines.
- `SquareBorder<T>() -> T` — Display a square border.

## via `IHasTreeNodes`

- `AddNode<T>(IRenderable renderable) -> TreeNode` — Adds a tree node.
- `AddNode<T>(TreeNode node) -> TreeNode` — Adds a tree node.
- `AddNode<T>(string markup) -> TreeNode` — Adds a tree node.
- `AddNodes<T>(IEnumerable<IRenderable> nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(IEnumerable<TreeNode> nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(IEnumerable<string> nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(params IRenderable[] nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(params TreeNode[] nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(params string[] nodes) -> void` — Add multiple tree nodes.

## via `IHasVisibility`

- `Invisible<T>() -> T` — Marks the specified object as being invisible.
- `Visible<T>() -> T` — Marks the specified object as being visible.

## via `IOverflowable`

- `Crop<T>() -> T` — Crops any overflowing text.
- `Ellipsis<T>() -> T` — Crops any overflowing text and adds an ellipsis to the end.
- `Fold<T>() -> T` — Folds any overflowing text.
- `Overflow<T>(Overflow overflow) -> T` — Sets the overflow strategy.

## via `IPaddable`

- `PadBottom<T>(int bottom) -> T` — Sets the bottom padding.
- `PadLeft<T>(int left) -> T` — Sets the left padding.
- `PadRight<T>(int right) -> T` — Sets the right padding.
- `PadTop<T>(int top) -> T` — Sets the top padding.
- `Padding<T>(Padding padding) -> T` — Sets the padding.
- `Padding<T>(int horizontal, int vertical) -> T` — Sets the horizontal and vertical padding.
- `Padding<T>(int left, int top, int right, int bottom) -> T` — Sets the left, top, right and bottom padding.

## via `IRenderable`

- `GetSegments(IAnsiConsole console) -> IEnumerable<Segment>` — Gets the segments for a renderable using the specified console.

## via `IUnsafeConfigurator`

- `SafetyOn() -> IConfigurator` — Converts an `IUnsafeConfigurator` to a configurator with type safety.

## via `TableBorder`

- `GetSafeBorder(bool safe) -> TableBorder` — Gets the safe border for a border.

## via `TreeGuide`

- `GetSafeTreeGuide(bool safe) -> TreeGuide` — Gets the safe border for a border.

