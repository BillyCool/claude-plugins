# widgets/Exceptions — API (generated from source)

## `public class ExceptionInfoResolver`

*core* · `src/Spectre.Console/Widgets/Exceptions/ExceptionInfoResolver.cs`

Used to resolve information from an `Exception`.

**Methods**

- `virtual string GetMethodName(MethodBase method)` — Gets the name of a method.
- `virtual string GetParameterName(ParameterInfo parameter)` — Gets the name of a parameter.
- `virtual string? GetFileName(StackFrame frame)` — Gets the file name of a `StackFrame`.
- `virtual int GetFileLineNumber(StackFrame frame)` — Gets the line number of a `StackFrame`.

## `public sealed class ExceptionSettings`

*core* · `src/Spectre.Console/Widgets/Exceptions/ExceptionSettings.cs`

Exception settings.

**Constructors**

- `ExceptionSettings()` — Initializes a new instance of the `ExceptionSettings` class.

**Properties**

- `ExceptionFormats Format { get; init; }` — Gets or sets the exception format.
- `ExceptionStyle Style { get; init; }` — Gets or sets the exception style.
- `ExceptionInfoResolver Resolver { get; init; }` — Gets or sets the exception scrubber. Useful for removing sensitive data and for testing.

## `public sealed class ExceptionStyle`

*core* · `src/Spectre.Console/Widgets/Exceptions/ExceptionStyle.cs`

Represent an exception style.

**Properties**

- `Style Message { get; set; }` = `new Style(Color.Red, Color.Default, Decoration.Bold)` — Gets or sets the message color.
- `Style Exception { get; set; }` = `Color.White` — Gets or sets the exception color.
- `Style Method { get; set; }` = `Color.Yellow` — Gets or sets the method color.
- `Style ParameterType { get; set; }` = `Color.Blue` — Gets or sets the parameter type color.
- `Style ParameterName { get; set; }` = `Color.Silver` — Gets or sets the parameter name color.
- `Style Parenthesis { get; set; }` = `Color.Silver` — Gets or sets the parenthesis color.
- `Style Path { get; set; }` = `new Style(Color.Yellow, Color.Default, Decoration.Bold)` — Gets or sets the path color.
- `Style LineNumber { get; set; }` = `Color.Blue` — Gets or sets the line number color.
- `Style Dimmed { get; set; }` = `Color.Grey` — Gets or sets the color for dimmed text such as "at" or "in".
- `Style NonEmphasized { get; set; }` = `Color.Silver` — Gets or sets the color for non emphasized items.

## `public enum ExceptionFormats`

*core* · `src/Spectre.Console/Widgets/Exceptions/ExceptionFormat.cs`

Represents how an exception is formatted.

**Values**

- `Default = 0` — The default formatting.
- `ShortenPaths = 1` — Whether or not paths should be shortened.
- `ShortenTypes = 2` — Whether or not types should be shortened.
- `ShortenMethods = 4` — Whether or not methods should be shortened.
- `ShowLinks = 8` — Whether or not to show paths as links in the terminal.
- `ShortenEverything = ShortenMethods | ShortenTypes | ShortenPaths` — Shortens everything that can be shortened.
- `NoStackTrace = 16` — Whether or not to show the exception stack trace.

