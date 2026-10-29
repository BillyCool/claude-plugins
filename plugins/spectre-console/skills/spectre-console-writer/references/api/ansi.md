# ansi — API (generated from source)

## `public class AnsiCapabilities : IReadOnlyAnsiCapabilities`

*ansi* · `src/Spectre.Console.Ansi/AnsiCapabilities.cs`

Represents ANSI capabilities.

**Properties**

- `ColorSystem ColorSystem { get; set; }` — Gets or sets the color system.
- `bool Ansi { get; set; }` — Gets or sets a value indicating whether or not the console supports VT/ANSI control codes.
- `bool Links { get; set; }` — Gets or sets a value indicating whether or not the console support links.
- `bool AlternateBuffer { get; set; }` — Gets or sets a value indicating whether or not the console supports alternate buffers.

**Methods**

- `static AnsiCapabilities Create(TextWriter writer)` — Creates a `AnsiCapabilities` instance from the provided arguments.
- `static AnsiCapabilities Create(TextWriter writer, AnsiWriterSettings settings)` — Creates a `AnsiCapabilities` instance from the provided arguments.

## `public sealed class AnsiMarkup`

*ansi* · `src/Spectre.Console.Ansi/AnsiMarkup.cs`

Utility used for working with markup text.

**Constructors**

- `AnsiMarkup(AnsiWriter writer)` — Initializes a new instance of the `AnsiMarkup` class.

**Methods**

- `void Write(string markup, Style? style = null)` — Outputs the specified markup.
- `void WriteLine(string markup)` — Outputs the specified markup, followed by the current line terminator
- `static IEnumerable<AnsiMarkupSegment> Parse(string markup, Style? style = null)` — Parses the specified markup text into segments that can be processed.
- `static string Escape(string? markup)` — Escapes the specified text so that it won’t be interpreted as markup.
- `static string Remove(string? markup)` — Removes markup from the specified text.
- `static string Highlight(string markup, string query, Style style)` — Highlights the first text match in provided markup.

## `public sealed class AnsiMarkupSegment`

*ansi* · `src/Spectre.Console.Ansi/AnsiMarkup.cs`

Represents a markup segment.

**Constructors**

- `AnsiMarkupSegment(string text, Style style, Link? link)` — Initializes a new instance of the `AnsiMarkupSegment` class.

**Properties**

- `string Text { get; internal set; }` — Gets the segment text.
- `Style Style { get; }` — Gets the segment style.
- `Link? Link { get; internal set; }` — Gets the segment link.

**Methods**

- `override string ToString()`

## `public sealed class AnsiWriter`

*ansi* · `src/Spectre.Console.Ansi/AnsiWriter.cs`

Represents an ANSI writer, capable of outputting ANSI/VT escape sequences.

**Constructors**

- `AnsiWriter(TextWriter output)` — Initializes a new instance of the `AnsiWriter` class.
- `AnsiWriter(TextWriter output, AnsiCapabilities capabilities)` — Initializes a new instance of the `AnsiWriter` class.

**Properties**

- `IReadOnlyAnsiCapabilities Capabilities { get; set; }` — Gets or sets the capabilities for the writer.

**Methods**

- `AnsiWriter Write(string text)` — Writes the specified text.
- `AnsiWriter Write(int value)` — Writes an integer.
- `AnsiWriter Write(string text, Style style, Link? link = null)` — Writes the specified text with the specified style.
- `AnsiWriter WriteLine()` — Writes an empty line.
- `AnsiWriter WriteLine(string text)` — Writes the specified text, followed by the current line terminator.
- `AnsiWriter WriteLine(string text, Style style, Link? link = null)` — Writes the specified text with the specified style, followed by the current line terminator.
- `AnsiWriter Style(Style style, Link? link = null)` — Writes a `Style` by emitting `SGR`.
- `AnsiWriter ResetStyle()` — Resets any foreground, background, decoration, or style by emitting `SGR(0)`.
- `AnsiWriter Decoration(Decoration decoration)` — Sets the current decoration by emitting `SGR`.
- `AnsiWriter Background(Color color)` — Sets the current background color by emitting `SGR`.
- `AnsiWriter Foreground(Color color)` — Sets the current foreground color by emitting `SGR`.
- `AnsiWriter BeginLink(Link link)` — Begins a link by emitting `OSC 8`.
- `AnsiWriter BeginLink(string link, int? linkId = null)` — Begins a link by emitting `OSC 8`.
- `AnsiWriter EndLink()` — Ends a link by emitting `OSC 8`.
- `AnsiWriter CursorPosition(int row, int column)` — This control function moves the cursor to the specified line and column (1-indexed) by emitting `CSI row;column H`.
- `AnsiWriter CursorHome()` — Moves the cursor to position 1,1 (top left corner) by emitting `CSI H`.
- `AnsiWriter CursorUp(int steps)` — Moves the cursor up a specified number of lines in the same column by emitting `CSI n A`. The cursor stops at the top margin. If the cursor is already above the top margin, then the cursor stops at the top line.
- `AnsiWriter CursorDown(int steps)` — This control function moves the cursor down a specified number of lines in the same column by emitting `CSI n B`. The cursor stops at the bottom margin. If the cursor is already below the bottom margin, then the cursor stops at the bottom line.
- `AnsiWriter CursorRight(int steps)` — This control function moves the cursor to the right by a specified number of columns by emitting `CSI n C`. The cursor stops at the right border of the page.
- `AnsiWriter CursorForward(int steps)` — This control function moves the cursor to the right by a specified number of columns by emitting `CSI n C`. The cursor stops at the right border of the page.
- `AnsiWriter CursorLeft(int steps)` — This control function moves the cursor to the left by a specified number of columns by emitting `CSI n D`. The cursor stops at the left border of the page.
- `AnsiWriter CursorBackward(int steps)` — This control function moves the cursor to the left by a specified number of columns by emitting `CSI n D`. The cursor stops at the left border of the page.
- `AnsiWriter ShowCursor()` — Shows the cursor by emitting `CSI ? 25 h`.
- `AnsiWriter HideCursor()` — Hides the cursor by emitting `CSI ? 25 l`.
- `AnsiWriter SaveCursor(bool stayOnPage = true)` — Saves current cursor position for SCO console mode by emitting `CSI s` (SCOSC) if staying on page, otherwise `ESC 7` (DECSC).
- `AnsiWriter RestoreCursor(bool stayOnPage = true)` — Moves cursor to the position saved by save cursor command in SCO console mode by emitting `CSI u` (SCORC) if staying on page, otherwise `ESC 8` (DECRC).
- `AnsiWriter CursorHorizontalAbsolute(int position)` — Moves the active position to the n-th character of the active line by emitting `CSI n G`
- `AnsiWriter EnterAltScreen()` — Enters the alternative screen buffer by emitting `CSI ? 1049 h`.
- `AnsiWriter ExitAltScreen()` — Exits the alternative screen buffer by emitting `CSI ? 1049 l`.
- `AnsiWriter EraseInLine(int mode = 0)` — This control function erases characters on the line that has the cursor. EL clears all character attributes from erased character positions. EL works inside or outside the scrolling margins.
- `AnsiWriter EraseInDisplay(int mode = 0)` — This control function erases characters from part or all of the display. When you erase complete lines, they become single-height, single-width lines, with all visual character attributes cleared. ED works inside or outside the scrolling margins.
- `AnsiWriter ClearScrollback()` — Clears the scrollback buffer by emitting `CSI 3J`.
- `AnsiWriter CursorBackwardTabulation(int tabs = 1)` — Move the active position n tabs backward by emitting `CSI n Z`.
- `AnsiWriter CursorHorizontalTabulation(int tabs = 1)` — Move the active position n tabs forward by emitting `CSI n I`.
- `AnsiWriter CursorNextLine(int lines = 1)` — Move the cursor to the next line by emitting `CSI n E`.
- `AnsiWriter CursorPreviousLine(int lines = 1)` — Move the cursor to the preceding line by emitting `CSI n F`.
- `AnsiWriter Index()` — Moves the cursor down one line in the same column by emitting `ESC D`. If the cursor is at the bottom margin, then the screen performs a scroll-up.
- `AnsiWriter ReverseIndex()` — Moves the cursor up one line in the same column by emitting `ESC M`. If the cursor is at the top margin, then the screen performs a scroll-down.
- `AnsiWriter DeleteCharacter(int characters = 1)` — This control function deletes one or more characters from the cursor position to the right by emitting `CSI n P`.
- `AnsiWriter SetCursorStyle(int style = 0)` — Select the style of the cursor on the screen by emitting `CSI n SP q`
- `AnsiWriter DeleteLine(int lines = 0)` — This control function deletes one or more lines in the scrolling region by emitting `CSI n M`, starting with the line that has the cursor. As lines are deleted, lines below the cursor and in the scrolling region move up. The terminal adds blank lines with no visual character attributes at the bottom of the scrolling region. If `lines` is greater than the number of lines remaining on the page, DL deletes only the remaining lines. DL has no effect outside the scrolling margins.
- `AnsiWriter EraseCharacter(int characters = 1)` — Erases one or more characters from the cursor position to the right by emitting `CSI n X` (ECH). ECH clears character attributes from erased character positions. ECH works inside or outside the scrolling margins.
- `AnsiWriter InsertCharacter(int characters = 1)` — inserts one or more space (SP) characters starting at the cursor position by emitting `CSI n @` (ICH). The ICH sequence inserts blank characters with the normal character attribute. The cursor remains at the beginning of the blank characters. Text between the cursor and right margin moves to the right. Characters scrolled past the right margin are lost. ICH has no effect outside the scrolling margins.
- `AnsiWriter InsertLine(int lines = 1)` — Inserts one or more blank lines, starting at the cursor by emitting `CSI n L` (IL). As lines are inserted, lines below the cursor and in the scrolling region move down. Lines scrolled off the page are lost. IL has no effect outside the page margins.
- `AnsiWriter ScrollDown(int lines = 1)` — Moves the user window up a specified number of lines in page memory by emitting `CSI n T`.
- `AnsiWriter ScrollUp(int lines = 1)` — Moves the user window down a specified number of lines in page memory by emitting `CSI n S`.

## `public sealed class AnsiWriterSettings`

*ansi* · `src/Spectre.Console.Ansi/AnsiWriterSettings.cs`

Represents settings for `AnsiWriter`.

**Properties**

- `AnsiSupport Ansi { get; init; }` = `AnsiSupport.Detect` — Gets or sets a value indicating whether or not ANSI escape sequences are supported.
- `ColorSystemSupport ColorSystem { get; init; }` = `ColorSystemSupport.Detect` — Gets or sets the color system to use.

## `public readonly partial struct Color : IEquatable<Color>`

*ansi* · `src/Spectre.Console.Ansi/Color.cs`

Represents a color.

**Constructors**

- `Color(byte red, byte green, byte blue)` — Initializes a new instance of the `Color` struct.

**Properties**

294 members like `static Color Default { get; }`: `Default`, `R`, `G`, `B`, `Black`, `Maroon`, `Green`, `Olive`, `Navy`, `Purple`, `Teal`, `Silver`, `Grey`, `Gray`, `Red`, `Lime`, `Yellow`, `Blue`, `Fuchsia`, `Magenta`, `Aqua`, `Cyan`, `White`, `Grey0`, `Gray0`, `NavyBlue`, `DarkBlue`, `Blue3`, `Blue3_1`, `Blue1`, `DarkGreen`, `DeepSkyBlue4`, `DeepSkyBlue4_1`, `DeepSkyBlue4_2`, `DodgerBlue3`, `DodgerBlue2`, `Green4`, `SpringGreen4`, `Turquoise4`, `DeepSkyBlue3`, `DeepSkyBlue3_1`, `DodgerBlue1`, `Green3`, `SpringGreen3`, `DarkCyan`, `LightSeaGreen`, `DeepSkyBlue2`, `DeepSkyBlue1`, `Green3_1`, `SpringGreen3_1`, `SpringGreen2`, `Cyan3`, `DarkTurquoise`, `Turquoise2`, `Green1`, `SpringGreen2_1`, `SpringGreen1`, `MediumSpringGreen`, `Cyan2`, `Cyan1`, `DarkRed`, `DeepPink4`, `Purple4`, `Purple4_1`, `Purple3`, `BlueViolet`, `Orange4`, `Grey37`, `Gray37`, `MediumPurple4`, `SlateBlue3`, `SlateBlue3_1`, `RoyalBlue1`, `Chartreuse4`, `DarkSeaGreen4`, `PaleTurquoise4`, `SteelBlue`, `SteelBlue3`, `CornflowerBlue`, `Chartreuse3`, `DarkSeaGreen4_1`, `CadetBlue`, `CadetBlue_1`, `SkyBlue3`, `SteelBlue1`, `Chartreuse3_1`, `PaleGreen3`, `SeaGreen3`, `Aquamarine3`, `MediumTurquoise`, `SteelBlue1_1`, `Chartreuse2`, `SeaGreen2`, `SeaGreen1`, `SeaGreen1_1`, `Aquamarine1`, `DarkSlateGray2`, `DarkRed_1`, `DeepPink4_1`, `DarkMagenta`, `DarkMagenta_1`, `DarkViolet`, `Purple_1`, `Orange4_1`, `LightPink4`, `Plum4`, `MediumPurple3`, `MediumPurple3_1`, `SlateBlue1`, `Yellow4`, `Wheat4`, `Grey53`, `Gray53`, `LightSlateGrey`, `MediumPurple`, `LightSlateBlue`, `Yellow4_1`, `DarkOliveGreen3`, `DarkSeaGreen`, `LightSkyBlue3`, `LightSkyBlue3_1`, `SkyBlue2`, `Chartreuse2_1`, `DarkOliveGreen3_1`, `PaleGreen3_1`, `DarkSeaGreen3`, `DarkSlateGray3`, `SkyBlue1`, `Chartreuse1`, `LightGreen`, `LightGreen_1`, `PaleGreen1`, `Aquamarine1_1`, `DarkSlateGray1`, `Red3`, `DeepPink4_2`, `MediumVioletRed`, `Magenta3`, `DarkViolet_1`, `Purple_2`, `DarkOrange3`, `IndianRed`, `HotPink3`, `MediumOrchid3`, `MediumOrchid`, `MediumPurple2`, `DarkGoldenrod`, `LightSalmon3`, `RosyBrown`, `Grey63`, `Gray63`, `MediumPurple2_1`, `MediumPurple1`, `Gold3`, `DarkKhaki`, `NavajoWhite3`, `Grey69`, `Gray69`, `LightSteelBlue3`, `LightSteelBlue`, `Yellow3`, `DarkOliveGreen3_2`, `DarkSeaGreen3_1`, `DarkSeaGreen2`, `LightCyan3`, `LightSkyBlue1`, `GreenYellow`, `DarkOliveGreen2`, `PaleGreen1_1`, `DarkSeaGreen2_1`, `DarkSeaGreen1`, `PaleTurquoise1`, `Red3_1`, `DeepPink3`, `DeepPink3_1`, `Magenta3_1`, `Magenta3_2`, `Magenta2`, `DarkOrange3_1`, `IndianRed_1`, `HotPink3_1`, `HotPink2`, `Orchid`, `MediumOrchid1`, `Orange3`, `LightSalmon3_1`, `LightPink3`, `Pink3`, `Plum3`, `Violet`, `Gold3_1`, `LightGoldenrod3`, `Tan`, `MistyRose3`, `Thistle3`, `Plum2`, `Yellow3_1`, `Khaki3`, `LightGoldenrod2`, `LightYellow3`, `Grey84`, `Gray84`, `LightSteelBlue1`, `Yellow2`, `DarkOliveGreen1`, `DarkOliveGreen1_1`, `DarkSeaGreen1_1`, `Honeydew2`, `LightCyan1`, `Red1`, `DeepPink2`, `DeepPink1`, `DeepPink1_1`, `Magenta2_1`, `Magenta1`, `OrangeRed1`, `IndianRed1`, `IndianRed1_1`, `HotPink`, `HotPink_1`, `MediumOrchid1_1`, `DarkOrange`, `Salmon1`, `LightCoral`, `PaleVioletRed1`, `Orchid2`, `Orchid1`, `Orange1`, `SandyBrown`, `LightSalmon1`, `LightPink1`, `Pink1`, `Plum1`, `Gold1`, `LightGoldenrod2_1`, `LightGoldenrod2_2`, `NavajoWhite1`, `MistyRose1`, `Thistle1`, `Yellow1`, `LightGoldenrod1`, `Khaki1`, `Wheat1`, `Cornsilk1`, `Grey100`, `Gray100`, `Grey3`, `Gray3`, `Grey7`, `Gray7`, `Grey11`, `Gray11`, `Grey15`, `Gray15`, `Grey19`, `Gray19`, `Grey23`, `Gray23`, `Grey27`, `Gray27`, `Grey30`, `Gray30`, `Grey35`, `Gray35`, `Grey39`, `Gray39`, `Grey42`, `Gray42`, `Grey46`, `Gray46`, `Grey50`, `Gray50`, `Grey54`, `Gray54`, `Grey58`, `Gray58`, `Grey62`, `Gray62`, `Grey66`, `Gray66`, `Grey70`, `Gray70`, `Grey74`, `Gray74`, `Grey78`, `Gray78`, `Grey82`, `Gray82`, `Grey85`, `Gray85`, `Grey89`, `Gray89`, `Grey93`, `Gray93`

**Operators / conversions**

- `static bool operator ==(Color left, Color right)` — Checks if two `Color` instances are equal.
- `static bool operator !=(Color left, Color right)` — Checks if two `Color` instances are not equal.
- `static implicit operator Color(int number)` — Converts a `int` to a `Color`.
- `static implicit operator Color(ConsoleColor color)` — Converts a `ConsoleColor` to a `Color`.
- `static implicit operator ConsoleColor(Color color)` — Converts a `Color` to a `ConsoleColor`.

**Methods**

- `Color Blend(Color other, float factor)` — Blends two colors.
- `string ToHex()` — Gets the hexadecimal representation of the color.
- `Color ExactOrClosest(ColorSystem system)` — Gets the exact or closest color in the specified `ColorSystem`.
- `override int GetHashCode()`
- `override bool Equals(object? obj)`
- `bool Equals(Color other)`
- `static ConsoleColor ToConsoleColor(Color color)` — Converts a `Color` to a `ConsoleColor`.
- `static Color FromInt32(int number)` — Converts a color number into a `Color`.
- `static Color FromHex(string hex)` — Creates a color from a hexadecimal string representation.
- `static bool TryFromHex(string hex, out Color color)` — Tries to convert a hexadecimal color code to a `Color` object.
- `static Color? FromName(string name)` — Gets a `Color` from its name.
- `static Color FromConsoleColor(ConsoleColor color)` — Converts a `ConsoleColor` to a `Color`.
- `string ToMarkup()` — Converts the color to a markup string.
- `override string ToString()`

## `public interface IReadOnlyAnsiCapabilities`

*ansi* · `src/Spectre.Console.Ansi/AnsiCapabilities.cs`

Represents read-only ANSI capabilities.

**Properties**

- `ColorSystem ColorSystem { get; }` — Gets or sets the color system.
- `bool Ansi { get; }` — Gets or sets a value indicating whether or not the console supports VT/ANSI control codes.
- `bool Links { get; }` — Gets or sets a value indicating whether or not the console support links.
- `bool AlternateBuffer { get; }` — Gets or sets a value indicating whether or not the console supports alternate buffers.

## `public sealed class Link(string url) : IEquatable<Link>`

*ansi* · `src/Spectre.Console.Ansi/Link.cs`

Represents a link.

**Properties**

- `int? Id { get; }` = `Random.Shared.Next(0, int.MaxValue)` — Gets the link ID.
- `string Url { get; }` = `url` — Gets the url.

**Methods**

- `bool Equals(Link? other)`
- `override bool Equals(object? obj)`
- `override int GetHashCode()`

## `public readonly record struct Style`

*ansi* · `src/Spectre.Console.Ansi/Style.cs`

Represents color and text decoration.

**Constructors**

- `Style()` — Initializes a new instance of the `Style` class.
- `Style(Color? foreground = null, Color? background = null, Decoration? decoration = null)` — Initializes a new instance of the `Style` class.

**Properties**

- `Color Foreground { get; init; }` — Gets the foreground color.
- `Color Background { get; init; }` — Gets the background color.
- `Decoration Decoration { get; init; }` — Gets the text decoration.
- `static Style Plain { get; }` = `new Style(null, null, null)` — Gets a `Style` with the default colors and without text decoration.

**Operators / conversions**

- `static implicit operator Style(string style)` — Implicitly converts `string` into a `Style`.
- `static implicit operator Style(Color color)` — Implicitly converts `Color` into a `Style` with a foreground color.

**Methods**

- `Style Combine(Style other)` — Combines this style with another one.
- `static Style Parse(string text)` — Converts the string representation of a style to its `Style` equivalent.
- `static bool TryParse(string text, out Style result)` — Converts the string representation of a style to its `Style` equivalent. A return value indicates whether the operation succeeded.
- `override int GetHashCode()`
- `string ToMarkup()` — Returns the markup representation of this style.

**Extension methods on this type** (call as `x.Method(...)`)

- `Foreground(Color color) -> Style` — Creates a new style from the specified one with the specified foreground color.
- `Background(Color color) -> Style` — Creates a new style from the specified one with the specified background color.
- `Decoration(Decoration decoration) -> Style` — Creates a new style from the specified one with the specified text decoration.

## `public static class SystemConsoleExtensions`

*ansi* · `src/Spectre.Console.Ansi/Utilities/ConsoleExtensions.cs`

Contains extension methods for `System.Console`.

**Methods**

- `(System.Console) static void Ansi(Action<AnsiWriter> action)` — Write ANSI, using the default `AnsiWriter` instance.
- `(System.Console) static void Markup(string markup)` — Writes the specified markup to the console, using the default `AnsiWriter` instance.
- `(System.Console) static void MarkupLine(string markup)` — Writes the specified markup to the console, followed by the current line terminator, using the default `AnsiWriter` instance.

## `public enum AnsiSupport`

*ansi* · `src/Spectre.Console.Ansi/AnsiSupport.cs`

Determines ANSI escape sequence support.

**Values**

- `Detect = 0` — ANSI escape sequence support should be detected by the system.
- `Yes = 1` — ANSI escape sequences are supported.
- `No = 2` — ANSI escape sequences are not supported.

## `public enum ColorSystem`

*ansi* · `src/Spectre.Console.Ansi/ColorSystem.cs`

Represents a color system.

**Values**

- `NoColors = 0` — No colors.
- `Legacy = 1` — Legacy, 3-bit mode.
- `Standard = 2` — Standard, 4-bit mode.
- `EightBit = 3` — 8-bit mode.
- `TrueColor = 4` — 24-bit mode.

## `public enum ColorSystemSupport`

*ansi* · `src/Spectre.Console.Ansi/ColorSystemSupport.cs`

Determines what color system should be used.

**Values**

- `Detect = -1` — Try to detect the color system.
- `NoColors = 0` — No colors.
- `Legacy = 1` — Legacy, 3-bit mode.
- `Standard = 2` — Standard, 4-bit mode.
- `EightBit = 3` — 8-bit mode.
- `TrueColor = 4` — 24-bit mode.

## `public enum Decoration`

*ansi* · `src/Spectre.Console.Ansi/Decoration.cs`

Represents text decoration.

**Values**

- `None = 0` — No text decoration.
- `Bold = 1 << 0` — Bold text. Not supported in every environment.
- `Dim = 1 << 1` — Dim or faint text. Not supported in every environment.
- `Italic = 1 << 2` — Italic text. Not supported in every environment.
- `Underline = 1 << 3` — Underlined text. Not supported in every environment.
- `Invert = 1 << 4` — Swaps the foreground and background colors. Not supported in every environment.
- `Conceal = 1 << 5` — Hides the text. Not supported in every environment.
- `SlowBlink = 1 << 6` — Makes text blink. Normally less than 150 blinks per minute. Not supported in every environment.
- `RapidBlink = 1 << 7` — Makes text blink. Normally more than 150 blinks per minute. Not supported in every environment.
- `Strikethrough = 1 << 8` — Shows text with a horizontal line through the center. Not supported in every environment.

