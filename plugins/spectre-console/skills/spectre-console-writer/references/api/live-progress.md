# live-progress — API (generated from source)

## `public sealed class DownloadedColumn : ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/Columns/DownloadedColumn.cs`

A column showing download progress.

**Properties**

- `CultureInfo? Culture { get; set; }` — Gets or sets the `CultureInfo` to use.
- `FileSizeBase Base { get; set; }` = `FileSizeBase.Binary` — Gets or sets the `FileSizeBase` to use.
- `bool ShowBits { get; set; }` — Gets or sets a value indicating whether to display the transfer speed in bits.

**Methods**

- `override IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.

## `public sealed class ElapsedTimeColumn : ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/Columns/ElapsedTimeColumn.cs`

A column showing the elapsed time of a task.

**Properties**

- `protected internal override bool NoWrap { get; }` — Gets a value indicating whether or not content should not wrap.
- `Style Style { get; set; }` = `Color.Blue` — Gets or sets the style of the remaining time text.

**Methods**

- `override IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.
- `override int? GetColumnWidth(RenderOptions options)` — Gets the width of the column.

## `public sealed class PercentageColumn : ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/Columns/PercentageColumn.cs`

A column showing task progress in percentage.

**Properties**

- `Style Style { get; set; }` = `Style.Plain` — Gets or sets the style for a non-complete task.
- `Style CompletedStyle { get; set; }` = `Color.Green` — Gets or sets the style for a completed task.

**Methods**

- `override IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.
- `override int? GetColumnWidth(RenderOptions options)` — Gets the width of the column.

**Extension methods on this type** (call as `x.Method(...)`)

- `Style(Style style) -> PercentageColumn` — Sets the style for a non-complete task.
- `CompletedStyle(Style style) -> PercentageColumn` — Sets the style for a completed task.

## `public sealed class Progress`

*core* · `src/Spectre.Console/Live/Progress/Progress.cs`

Represents a task list.

**Constructors**

- `Progress(IAnsiConsole console, TimeProvider? timeProvider = null)` — Initializes a new instance of the `Progress` class.

**Properties**

- `Func<IRenderable, IReadOnlyList<ProgressTask>, IRenderable> RenderHook { get; set; }` — Gets or sets a optional custom render function.
- `bool AutoRefresh { get; set; }` = `true` — Gets or sets a value indicating whether or not task list should auto refresh. Defaults to `true`.
- `bool AutoClear { get; set; }` — Gets or sets a value indicating whether or not the task list should be cleared once it completes. Defaults to `false`.
- `bool HideCompleted { get; set; }` — Gets or sets a value indicating whether or not the task list should only include tasks not completed Defaults to `false`.
- `bool ExcludeVerticalPadding { get; set; }` — Gets or sets a value indicating whether or not to exclude the vertical padding in the display. Defaults to `false`.
- `TimeSpan RefreshRate { get; set; }` = `TimeSpan.FromMilliseconds(100)` — Gets or sets the refresh rate if `AutoRefresh` is enabled. Defaults to 10 times/second.

**Methods**

- `void Start(Action<ProgressContext> action)` — Starts the progress task list.
- `T Start<T>(Func<ProgressContext, T> func)` — Starts the progress task list and returns a result.
- `async Task StartAsync(Func<ProgressContext, Task> action)` — Starts the progress task list.
- `async Task<T> StartAsync<T>(Func<ProgressContext, Task<T>> action)` — Starts the progress task list and returns a result.

**Extension methods on this type** (call as `x.Method(...)`)

- `Columns(params ProgressColumn[] columns) -> Progress` — Sets the columns to be used for an `Progress` instance.
- `UseRenderHook(Func<IRenderable, IReadOnlyList<ProgressTask>, IRenderable> renderHook) -> Progress` — Sets an optional hook to intercept rendering.
- `AutoRefresh(bool enabled) -> Progress` — Sets whether or not auto refresh is enabled. If disabled, you will manually have to refresh the progress.
- `AutoClear(bool enabled) -> Progress` — Sets whether or not auto clear is enabled. If enabled, the task tabled will be removed once all tasks have completed.
- `HideCompleted(bool enabled) -> Progress` — Sets whether or not hide completed is enabled. If enabled, the task tabled will be removed once it is completed.
- `ExcludeVerticalPadding(bool enabled) -> Progress` — Sets whether or not to exclude the vertical padding in the display. If enabled, the progress display will not include vertical padding.
- `ExcludeVerticalPadding() -> Progress` — Excludes the vertical padding in the display.
- `IncludeVerticalPadding() -> Progress` — Includes the vertical padding in the display.

## `public sealed class ProgressBarColumn : ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/Columns/ProgressBarColumn.cs`

A column showing task progress as a progress bar.

**Properties**

- `int? Width { get; set; }` = `40` — Gets or sets the width of the column.
- `Style CompletedStyle { get; set; }` = `Color.Yellow` — Gets or sets the style of completed portions of the progress bar.
- `Style FinishedStyle { get; set; }` = `Color.Green` — Gets or sets the style of a finished progress bar.
- `Style RemainingStyle { get; set; }` = `Color.Grey` — Gets or sets the style of remaining portions of the progress bar.
- `Style IndeterminateStyle { get; set; }` = `ProgressBar.DefaultPulseStyle` — Gets or sets the style of an indeterminate progress bar.

**Methods**

- `override IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.

**Extension methods on this type** (call as `x.Method(...)`)

- `CompletedStyle(Style style) -> ProgressBarColumn` — Sets the style of completed portions of the progress bar.
- `FinishedStyle(Style style) -> ProgressBarColumn` — Sets the style of a finished progress bar.
- `RemainingStyle(Style style) -> ProgressBarColumn` — Sets the style of remaining portions of the progress bar.

## `public abstract class ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/ProgressColumn.cs`

Represents a progress column.

**Properties**

- `protected internal virtual bool NoWrap { get; }` — Gets a value indicating whether or not content should not wrap.

**Methods**

- `abstract IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.
- `virtual int? GetColumnWidth(RenderOptions options)` — Gets the width of the column.

## `public sealed class ProgressContext`

*core* · `src/Spectre.Console/Live/Progress/ProgressContext.cs`

Represents a context that can be used to interact with a `Progress`.

**Properties**

- `bool IsFinished { get; }` — Gets a value indicating whether or not all started tasks have completed.

**Methods**

- `ProgressTask AddTask(string description, bool autoStart = true, double maxValue = 100)` — Adds a task.
- `ProgressTask AddTaskAt(string description, int index, bool autoStart = true, double maxValue = 100)` — Adds a task.
- `ProgressTask AddTaskBefore(string description, ProgressTask referenceProgressTask, bool autoStart = true, double maxValue = 100)` — Adds a task before the reference task.
- `ProgressTask AddTaskAfter(string description, ProgressTask referenceProgressTask, bool autoStart = true, double maxValue = 100)` — Adds a task after the reference task.
- `ProgressTask AddTask(string description, ProgressTaskSettings settings)` — Adds a task.
- `ProgressTask AddTaskAt(string description, ProgressTaskSettings settings, int index)` — Adds a task at the specified index.
- `ProgressTask AddTaskBefore(string description, ProgressTaskSettings settings, ProgressTask referenceProgressTask)` — Adds a task before the reference task.
- `ProgressTask AddTaskAfter(string description, ProgressTaskSettings settings, ProgressTask referenceProgressTask)` — Adds a task after the reference task.
- `bool RemoveTask(ProgressTask task)` — Removes the task from the task collection.
- `void Refresh()` — Refreshes the current progress.

## `public sealed class ProgressTask : IProgress<double>`

*core* · `src/Spectre.Console/Live/Progress/ProgressTask.cs`

Represents a progress task.

**Constructors**

- `ProgressTask(int id, string description, double maxValue, bool autoStart = true, TimeProvider? timeProvider = null)` — Initializes a new instance of the `ProgressTask` class.

**Properties**

- `int Id { get; }` — Gets the task ID.
- `object? Tag { get; set; }` — Gets or sets optional user tag data.
- `bool? HideWhenCompleted { get; set; }` — Gets or sets a value indicating whether to override the default hiding behavior of this task when completed.
- `string Description { get; set; }` — Gets or sets the task description.
- `double MaxValue { get; set; }` — Gets or sets the max value of the task.
- `double Value { get; set; }` — Gets or sets the value of the task.
- `DateTime? StartTime { get; private set; }` — Gets the start time of the task.
- `DateTime? StopTime { get; private set; }` — Gets the stop time of the task.
- `ProgressTaskState State { get; }` — Gets the task state.
- `bool IsStarted { get; }` — Gets a value indicating whether or not the task has started.
- `bool IsFinished { get; }` — Gets a value indicating whether or not the task has finished.
- `double Percentage { get; }` — Gets the percentage done of the task.
- `double? Speed { get; }` — Gets the speed measured in steps/second.
- `TimeSpan? ElapsedTime { get; }` — Gets the elapsed time.
- `TimeSpan? RemainingTime { get; }` — Gets the remaining time.
- `TimeSpan MaxTimeForSpeedCache { get; set; }` = `TimeSpan.FromSeconds(1)` — Gets or sets the maximum time a calculated speed value is cached. When estimating speed, if the oldest sample is older than this value, the current time is used as the end of the timespan instead. This causes the predicted speed to naturally decay if no new samples are received.
- `bool IsIndeterminate { get; set; }` — Gets or sets a value indicating whether the ProgressBar shows actual values or generic, continuous progress feedback.
- `TimeSpan MaxSamplingAge { get; set; }` = `TimeSpan.FromSeconds(30)` — Gets or sets the maximum age of samples kept for calculating speed and estimated time remaining. Samples older than this value are discarded to more accurately reflect the current speed.
- `int MaxSamplesKept { get; set; }` = `1000` — Gets or sets the maximum number of samples to keep for calculating speed and estimated time remaining. If set to 0, no samples are kept.

**Methods**

- `void StartTask()` — Starts the task.
- `void StopTask()` — Stops and marks the task as finished.
- `void Increment(double value)` — Increments the task's value.

**Extension methods on this type** (call as `x.Method(...)`)

- `Description(string description) -> ProgressTask` — Sets the task description.
- `MaxValue(double value) -> ProgressTask` — Sets the max value of the task.
- `Value(double value) -> ProgressTask` — Sets the value of the task.
- `IsIndeterminate(bool indeterminate = true) -> ProgressTask` — Sets whether the task is considered indeterminate or not.
- `HideWhenCompleted(bool hideWhenCompleted = true) -> ProgressTask` — Sets whether to override the default hiding behavior of this task when completed.
- `Tag(object? tag) -> ProgressTask` — Sets the task's tag.

## `public sealed class ProgressTaskSettings`

*core* · `src/Spectre.Console/Live/Progress/ProgressTaskSettings.cs`

Represents settings for a progress task.

**Properties**

- `double MaxValue { get; set; }` = `100` — Gets or sets the task's max value. Defaults to `100`.
- `bool AutoStart { get; set; }` = `true` — Gets or sets a value indicating whether or not the task will be auto started. Defaults to `true`.

## `public sealed class ProgressTaskState`

*core* · `src/Spectre.Console/Live/Progress/ProgressTaskState.cs`

Represents progress task state.

**Constructors**

- `ProgressTaskState()` — Initializes a new instance of the `ProgressTaskState` class.

**Methods**

- `T Get<T>(string key) where T : struct` — Gets the state value for the specified key.
- `T Update<T>(string key, Func<T, T> func) where T : struct` — Updates a task state value.

## `public sealed class RemainingTimeColumn : ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/Columns/RemainingTimeColumn.cs`

A column showing the remaining time of a task. Displays "**:**:**" if the task is indeterminate or the remaining time is greater than 99 hours.

**Properties**

- `protected internal override bool NoWrap { get; }` — Gets a value indicating whether or not content should not wrap.
- `Style Style { get; set; }` = `Color.Blue` — Gets or sets the style of the remaining time text.

**Methods**

- `override IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.
- `override int? GetColumnWidth(RenderOptions options)` — Gets the width of the column.

**Extension methods on this type** (call as `x.Method(...)`)

- `Style(Style style) -> RemainingTimeColumn` — Sets the style of the remaining time text.

## `public sealed class SpinnerColumn : ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/Columns/SpinnerColumn.cs`

A column showing a spinner.

**Constructors**

- `SpinnerColumn() : this(Spinner.Known.Default)` — Initializes a new instance of the `SpinnerColumn` class.
- `SpinnerColumn(Spinner spinner)` — Initializes a new instance of the `SpinnerColumn` class.

**Properties**

- `protected internal override bool NoWrap { get; }` — Gets a value indicating whether or not content should not wrap.
- `Spinner Spinner { get; set; }` — Gets or sets the `Console.Spinner`.
- `string? CompletedText { get; set; }` — Gets or sets the text that should be shown instead of the spinner once a task completes.
- `string? PendingText { get; set; }` — Gets or sets the text that should be shown instead of the spinner before a task begins.
- `Style? CompletedStyle { get; set; }` — Gets or sets the completed style.
- `Style? PendingStyle { get; set; }` — Gets or sets the pending style.
- `Style? Style { get; set; }` = `Color.Yellow` — Gets or sets the style of the spinner.

**Methods**

- `override IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.
- `override int? GetColumnWidth(RenderOptions options)` — Gets the width of the column.

**Extension methods on this type** (call as `x.Method(...)`)

- `Style(Style? style) -> SpinnerColumn` — Sets the style of the spinner.
- `CompletedText(string? text) -> SpinnerColumn` — Sets the text that should be shown instead of the spinner once a task completes.
- `CompletedStyle(Style? style) -> SpinnerColumn` — Sets the completed style of the spinner.

## `public sealed class TaskDescriptionColumn : ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/Columns/TaskDescriptionColumn.cs`

A column showing the task description.

**Properties**

- `protected internal override bool NoWrap { get; }` — Gets a value indicating whether or not content should not wrap.
- `bool Wrap { get; set; }` — Gets or sets a value indicating whether the description should wrap onto multiple lines when it's wider than the available space. Defaults to `false`, which truncates the description with an ellipsis.
- `Justify Alignment { get; set; }` = `Justify.Right` — Gets or sets the alignment of the task description.

**Methods**

- `override IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.

## `public sealed class TransferSpeedColumn : ProgressColumn`

*core* · `src/Spectre.Console/Live/Progress/Columns/TransferSpeedColumn.cs`

A column showing transfer speed.

**Properties**

- `CultureInfo? Culture { get; set; }` — Gets or sets the `CultureInfo` to use.
- `FileSizeBase Base { get; set; }` = `FileSizeBase.Binary` — Gets or sets the `FileSizeBase` to use.
- `bool ShowBits { get; set; }` — Gets or sets a value indicating whether to display the transfer speed in bits.

**Methods**

- `override IRenderable Render(RenderOptions options, ProgressTask task, TimeSpan deltaTime)` — Gets a renderable representing the column.

