# testing — API (generated from source)

## `public sealed class TestCapabilities : IReadOnlyCapabilities`

*testing* · `src/Spectre.Console.Testing/TestCapabilities.cs`

Represents fake capabilities useful in tests.

**Properties**

- `ColorSystem ColorSystem { get; set; }` = `ColorSystem.TrueColor` — Gets or sets the color system.
- `bool Ansi { get; set; }` — Gets or sets a value indicating whether or not the console supports VT/ANSI control codes.
- `bool Links { get; set; }` — Gets or sets a value indicating whether or not the console support links.
- `bool Legacy { get; set; }` — Gets a value indicating whether or not this is a legacy console (cmd.exe) on an OS prior to Windows 10.
- `bool Interactive { get; set; }` — Gets a value indicating whether or not the console supports interaction.
- `bool Unicode { get; set; }` — Gets a value indicating whether or not the console supports Unicode.
- `bool AlternateBuffer { get; set; }` — Gets or sets a value indicating whether or not the console supports alternate buffers.

**Methods**

- `RenderOptions CreateRenderContext(IAnsiConsole console)` — Creates a `RenderOptions` with the same capabilities as this instance.

## `public sealed class TestConsole : IAnsiConsole, IDisposable`

*testing* · `src/Spectre.Console.Testing/TestConsole.cs`

A testable console.

**Constructors**

- `TestConsole()` — Initializes a new instance of the `TestConsole` class.

**Properties**

- `Profile Profile { get; }` — Gets the console profile.
- `IExclusivityMode ExclusivityMode { get; }` — Gets the exclusivity mode.
- `TestConsoleInput Input { get; }` — Gets the console input.
- `RenderPipeline Pipeline { get; }` — Gets the render pipeline.
- `IAnsiConsoleCursor Cursor { get; }` — Gets the console cursor.
- `string Output { get; }` — Gets the console output.
- `IReadOnlyList<string> Lines { get; }` — Gets the console output lines.
- `bool EmitAnsiSequences { get; set; }` — Gets or sets a value indicating whether or not VT/ANSI sequences should be emitted to the console.

**Methods**

- `void Dispose()`
- `void Clear(bool home)` — Clears the console.
- `void Write(IRenderable renderable)` — Writes a `IRenderable` to the console.
- `void WriteAnsi(Action<AnsiWriter> action)` — Writes ANSI/VT escapes sequences to the console.

**Extension methods on this type** (call as `x.Method(...)`)

- `Colors(ColorSystem colors) -> TestConsole` — Sets the console's color system.
- `SupportsAnsi(bool enable) -> TestConsole` — Sets whether or not ANSI is supported.
- `SupportsUnicode(bool enable) -> TestConsole` — Sets whether or not Unicode is supported.
- `Interactive() -> TestConsole` — Makes the console interactive.
- `Width(int width) -> TestConsole` — Sets the console width.
- `Height(int width) -> TestConsole` — Sets the console height.
- `Size(Size size) -> TestConsole` — Sets the console size.
- `EmitAnsiSequences() -> TestConsole` — Turns on emitting of VT/ANSI sequences.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IAnsiConsole`: `WriteAnsi`, `ToAnsi`, `Clear`, `WriteException`, `RunExclusive`, `Live`, `Markup`, `MarkupInterpolated`, `MarkupLine`, `MarkupLineInterpolated`, `Progress`, `Status`, `Prompt`, `Ask`, `Confirm`, `PromptAsync`, `AskAsync`, `ConfirmAsync`, `CreateRecorder`, `AlternateScreen`, `Write`, `WriteLine`

## `public sealed class TestConsoleInput : IAnsiConsoleInput`

*testing* · `src/Spectre.Console.Testing/TestConsoleInput.cs`

Represents a testable console input mechanism.

**Constructors**

- `TestConsoleInput()` — Initializes a new instance of the `TestConsoleInput` class.

**Methods**

- `void PushText(string input)` — Pushes the specified text to the input queue.
- `void PushTextWithEnter(string input)` — Pushes the specified text followed by 'Enter' to the input queue.
- `void PushCharacter(char input)` — Pushes the specified character to the input queue.
- `void PushKey(ConsoleKey input)` — Pushes the specified key to the input queue.
- `void PushKey(ConsoleKeyInfo consoleKeyInfo)` — Pushes the specified key to the input queue.
- `bool IsKeyAvailable()` — Gets a value indicating whether or not there is a key available.
- `ConsoleKeyInfo? ReadKey(bool intercept)` — Reads a key from the console.
- `Task<ConsoleKeyInfo?> ReadKeyAsync(bool intercept, CancellationToken cancellationToken)` — Reads a key from the console.

