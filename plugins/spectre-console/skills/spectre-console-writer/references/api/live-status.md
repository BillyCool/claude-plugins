# live-status — API (generated from source)

## `public sealed class Status`

*core* · `src/Spectre.Console/Live/Status/Status.cs`

Represents a status display.

**Constructors**

- `Status(IAnsiConsole console)` — Initializes a new instance of the `Status` class.

**Properties**

- `Spinner? Spinner { get; set; }` — Gets or sets the spinner.
- `Style? SpinnerStyle { get; set; }` = `Color.Yellow` — Gets or sets the spinner style.
- `bool AutoRefresh { get; set; }` = `true` — Gets or sets a value indicating whether or not status should auto refresh. Defaults to `true`.

**Methods**

- `void Start(string status, Action<StatusContext> action)` — Starts a new status display.
- `T Start<T>(string status, Func<StatusContext, T> func)` — Starts a new status display.
- `async Task StartAsync(string status, Func<StatusContext, Task> action)` — Starts a new status display.
- `async Task<T> StartAsync<T>(string status, Func<StatusContext, Task<T>> func)` — Starts a new status display and returns a result.

**Extension methods on this type** (call as `x.Method(...)`)

- `AutoRefresh(bool enabled) -> Status` — Sets whether or not auto refresh is enabled. If disabled, you will manually have to refresh the progress.
- `Spinner(Spinner spinner) -> Status` — Sets the spinner.
- `SpinnerStyle(Style? style) -> Status` — Sets the spinner style.

## `public sealed class StatusContext`

*core* · `src/Spectre.Console/Live/Status/StatusContext.cs`

Represents a context that can be used to interact with a `Status`.

**Properties**

- `string Status { get; set; }` — Gets or sets the current status.
- `Spinner Spinner { get; set; }` — Gets or sets the current spinner.
- `Style? SpinnerStyle { get; set; }` — Gets or sets the current spinner style.

**Methods**

- `void Refresh()` — Refreshes the status.

**Extension methods on this type** (call as `x.Method(...)`)

- `Status(string status) -> StatusContext` — Sets the status message.
- `Spinner(Spinner spinner) -> StatusContext` — Sets the spinner.
- `SpinnerStyle(Style? style) -> StatusContext` — Sets the spinner style.

