# widgets/Calendar — API (generated from source)

## `public sealed class Calendar : JustInTimeRenderable, IHasCulture, IHasTableBorder`

*core* · `src/Spectre.Console/Widgets/Calendar.cs`

A renderable calendar.

**Constructors**

- `Calendar(DateTime date) : this(date.Year, date.Month, date.Day)` — Initializes a new instance of the `Calendar` class.
- `Calendar(int year, int month) : this(year, month, 1)` — Initializes a new instance of the `Calendar` class.
- `Calendar(int year, int month, int day)` — Initializes a new instance of the `Calendar` class.

**Properties**

- `int Year { get; set; }` — Gets or sets the calendar year.
- `int Month { get; set; }` — Gets or sets the calendar month.
- `int Day { get; set; }` — Gets or sets the calendar day.
- `TableBorder Border { get; set; }` — Gets or sets the border.
- `bool UseSafeBorder { get; set; }` — Gets or sets a value indicating whether or not to use a "safe" border on legacy consoles that might not be able to render non-ASCII characters.
- `Style? BorderStyle { get; set; }` — Gets or sets the box style.
- `CultureInfo? Culture { get; set; }` — Gets or sets the calendar's `CultureInfo`.
- `Style HighlightStyle { get; set; }` — Gets or sets the calendar's highlight `Style`.
- `bool ShowHeader { get; set; }` — Gets or sets a value indicating whether or not the calendar header should be shown.
- `Style? HeaderStyle { get; set; }` — Gets or sets the header style.
- `IList<CalendarEvent> CalendarEvents { get; }` — Gets a list containing all calendar events.

**Methods**

- `protected override IRenderable Build()` — Builds the inner renderable.

**Extension methods on this type** (call as `x.Method(...)`)

- `AddCalendarEvent(DateTime date, Style? customEventHighlightStyle = null) -> Calendar` — Adds a calendar event.
- `AddCalendarEvent(string description, DateTime date, Style? customEventHighlightStyle = null) -> Calendar` — Adds a calendar event.
- `AddCalendarEvent(int year, int month, int day, Style? customEventHighlightStyle = null) -> Calendar` — Adds a calendar event.
- `AddCalendarEvent(string description, int year, int month, int day, Style? customEventHighlightStyle = null) -> Calendar` — Adds a calendar event.
- `HighlightStyle(Style? style) -> Calendar` — Sets the calendar's highlight `Style`.
- `HeaderStyle(Style? style) -> Calendar` — Sets the calendar's header `Style`.
- `ShowHeader() -> Calendar` — Shows the calendar header.
- `HideHeader() -> Calendar` — Hides the calendar header.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasBorder`: `SafeBorder`, `NoSafeBorder`, `BorderStyle`, `BorderColor`
- via `IHasCulture`: `Culture`
- via `IHasTableBorder`: `NoBorder`, `SquareBorder`, `AsciiBorder`, `Ascii2Border`, `AsciiDoubleHeadBorder`, `RoundedBorder`, `MinimalBorder`, `MinimalHeavyHeadBorder`, `MinimalDoubleHeadBorder`, `SimpleBorder`, `SimpleHeavyBorder`, `HorizontalBorder`, `HeavyBorder`, `HeavyEdgeBorder`, `HeavyHeadBorder`, `DoubleBorder`, `DoubleEdgeBorder`, `MinimalistBorder`, `MarkdownBorder`, `Border`
- via `IRenderable`: `GetSegments`

## `public sealed class CalendarEvent`

*core* · `src/Spectre.Console/Widgets/CalendarEvent.cs`

Represents a calendar event.

**Constructors**

- `CalendarEvent(int year, int month, int day, Style? customHighlightStyle = null) : this(string.Empty, year, month, day, customHighlightStyle)` — Initializes a new instance of the `CalendarEvent` class.
- `CalendarEvent(string description, int year, int month, int day, Style? customHighlightStyle = null)` — Initializes a new instance of the `CalendarEvent` class.

**Properties**

- `string Description { get; }` — Gets the description of the calendar event.
- `int Year { get; }` — Gets the year of the calendar event.
- `int Month { get; }` — Gets the month of the calendar event.
- `int Day { get; }` — Gets the day of the calendar event.
- `Style? CustomHighlightStyle { get; }` — Gets the custom highlight style of the calendar event.

