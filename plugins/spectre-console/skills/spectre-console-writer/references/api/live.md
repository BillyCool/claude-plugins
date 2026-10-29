# live — API (generated from source)

## `public sealed class LiveDisplay`

*core* · `src/Spectre.Console/Live/LiveDisplay.cs`

Represents a live display.

**Constructors**

- `LiveDisplay(IAnsiConsole console, IRenderable target)` — Initializes a new instance of the `LiveDisplay` class.

**Properties**

- `bool AutoClear { get; set; }` — Gets or sets a value indicating whether or not the live display should be cleared when it's done. Defaults to `false`.
- `VerticalOverflow Overflow { get; set; }` = `VerticalOverflow.Ellipsis` — Gets or sets the vertical overflow strategy.
- `VerticalOverflowCropping Cropping { get; set; }` = `VerticalOverflowCropping.Top` — Gets or sets the vertical overflow cropping strategy.

**Methods**

- `void Start(Action<LiveDisplayContext> action)` — Starts the live display.
- `T Start<T>(Func<LiveDisplayContext, T> func)` — Starts the live display.
- `async Task StartAsync(Func<LiveDisplayContext, Task> func)` — Starts the live display.
- `async Task<T> StartAsync<T>(Func<LiveDisplayContext, Task<T>> func)` — Starts the live display.

**Extension methods on this type** (call as `x.Method(...)`)

- `AutoClear(bool enabled) -> LiveDisplay` — Sets whether or not auto clear is enabled. If enabled, the live display will be cleared when done.
- `Overflow(VerticalOverflow overflow) -> LiveDisplay` — Sets the vertical overflow strategy.
- `Cropping(VerticalOverflowCropping cropping) -> LiveDisplay` — Sets the vertical overflow cropping strategy.

## `public sealed class LiveDisplayContext`

*core* · `src/Spectre.Console/Live/LiveDisplayContext.cs`

Represents a context that can be used to interact with a `LiveDisplay`.

**Methods**

- `void UpdateTarget(IRenderable? target)` — Updates the live display target.
- `void Refresh()` — Refreshes the live display.

