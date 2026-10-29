# Progress, Status and LiveDisplay

Three "live" renderers redraw in place using ANSI cursor control. Verified against
`src/Spectre.Console/Live/**` (0.57.2). Exact members: `api/live-progress.md`, `api/live-status.md`,
`api/live.md`.

| Need | Use |
|---|---|
| Measurable work, one or many tasks, bars/ETA | `Progress` |
| "Working…" spinner + message, unknown duration | `Status` |
| Arbitrary re-rendered content (dashboard, table that grows, `Layout`) | `LiveDisplay` |

## Hard rules (these cause most bugs)

1. **One live thing at a time.** Progress/Status/LiveDisplay/prompts share an exclusivity lock;
   nesting or running concurrently throws `InvalidOperationException: Trying to run one or more
   interactive functions concurrently…`. Ask for input *before* or *after*, never inside.
2. **Don't write to the console from inside the callback** (`AnsiConsole.MarkupLine(...)`) — it
   corrupts the redraw. Update the task description / status text / target renderable instead,
   or collect messages and print them after the display finishes. (For log-style output above a
   running Progress, render the log lines in a `RenderHook` or show them as a task description.)
3. **`ctx.IsFinished` = "every *started* task is finished"** (`tasks.Where(IsStarted).All(IsFinished)`).
   So it is `true` immediately when no task has been started (e.g. all `autoStart: false`), and
   `while (!ctx.IsFinished)` spins forever if a started task never reaches `MaxValue`/`StopTask()`.
4. **Non-interactive consoles degrade, they don't crash**: `Progress` falls back to a simple
   line-based renderer when `Capabilities.Interactive && Capabilities.Ansi` is false (CI logs,
   redirected output); `Status` likewise. `LiveDisplay` just writes the target.
5. Callbacks run on the calling thread; use `StartAsync` when the work is `async`. The context
   objects are safe to update from `Task.Run`/`Parallel` workers you await inside the callback.

## Progress

Default columns (when you don't call `.Columns(...)`): `TaskDescriptionColumn`,
`ProgressBarColumn`, `PercentageColumn`. Others: `RemainingTimeColumn`, `ElapsedTimeColumn`,
`SpinnerColumn`, `DownloadedColumn`, `TransferSpeedColumn`. Custom columns derive from
`ProgressColumn` (`Render(RenderOptions, ProgressTask, TimeSpan)`).

```csharp
await AnsiConsole.Progress()
    .AutoClear(false)
    .HideCompleted(false)
    .Columns(
        new TaskDescriptionColumn(),
        new ProgressBarColumn(),
        new PercentageColumn(),
        new RemainingTimeColumn(),
        new SpinnerColumn())
    .StartAsync(async ctx =>
    {
        var download = ctx.AddTask("[green]Downloading[/]", maxValue: 100);
        var unpack   = ctx.AddTask("[blue]Unpacking[/]", autoStart: false);
        var scan     = ctx.AddTask("Scanning").IsIndeterminate();

        while (!download.IsFinished)
        {
            download.Increment(5);
            await Task.Delay(50);
        }

        unpack.StartTask();
        while (!unpack.IsFinished)
        {
            unpack.Increment(10);
            await Task.Delay(50);
        }

        scan.IsIndeterminate(false);
        scan.Value = scan.MaxValue;
    });
```

Useful bits (see api for the rest):
- `ctx.AddTask(description, autoStart = true, maxValue = 100)` or `AddTask(desc, new ProgressTaskSettings { MaxValue = …, AutoStart = … })`;
  `AddTaskBefore/After/At` control order; `ctx.RemoveTask(t)`.
- `task.Increment(x)`, `task.Value = x`, `task.MaxValue = x` (must be ≥ 0 — validated on `main`
  after 0.57.2), `task.Description = "..."` (markup OK), `task.StartTask()/StopTask()`.
- `ProgressTask` implements `IProgress<double>`: hand it to APIs that take
  `IProgress<double>` (e.g. `stream.CopyToAsync` helpers) and it updates `Value`.
- Time columns need a stable rate; they show `--:--:--` for indeterminate tasks.
- `Progress.AutoRefresh(false)` + `ctx.Refresh()` for manual redraw (e.g. in tight loops where
  you only want to repaint every N iterations). `RefreshRate` defaults to 100 ms.
- Multiple tasks update independently, so run parallel workers each owning one `ProgressTask`.
- Byte transfers: set `MaxValue` to the byte count and add `DownloadedColumn` / `TransferSpeedColumn`.

## Status (spinner + text)

```csharp
var result = await AnsiConsole.Status()
    .Spinner(Spinner.Known.Dots)
    .SpinnerStyle(Style.Parse("green bold"))
    .StartAsync("Connecting…", async ctx =>
    {
        await Task.Delay(500);
        ctx.Status("Authenticating");          // change text
        ctx.Spinner(Spinner.Known.Star);       // change spinner
        await Task.Delay(500);
        return 42;                              // StartAsync<T> returns a value
    });
```

Spinner names → `spinners.md` (`Spinner.Known.<Name>`). Status text supports markup and (since
0.57.2) wraps instead of truncating. Non-Unicode terminals fall back to `Spinner.Known.Ascii`.

## LiveDisplay

```csharp
var table = new Table().AddColumn("Time").AddColumn("Value");

await AnsiConsole.Live(table)
    .AutoClear(false)
    .Overflow(VerticalOverflow.Ellipsis)     // Ellipsis (default) | Crop | Visible
    .Cropping(VerticalOverflowCropping.Top)  // keep newest rows when it overflows
    .StartAsync(async ctx =>
    {
        for (var i = 0; i < 5; i++)
        {
            table.AddRow(DateTime.Now.ToString("T"), i.ToString());
            ctx.Refresh();                    // you mutated the same renderable
            await Task.Delay(300);
        }

        ctx.UpdateTarget(new Panel("Done").Expand());   // or swap the whole thing
    });
```

- Mutating a renderable that is already the target needs `ctx.Refresh()`; swapping needs
  `ctx.UpdateTarget(x)` (which refreshes).
- A target taller than the console triggers `Overflow` handling. For dashboards use `Layout`
  (it fills the window) with `Overflow(VerticalOverflow.Visible)` only if you accept scrolling.
- `AutoClear(true)` erases the display on completion; otherwise the final frame stays.

## Returning values, cancellation

`Start<T>(…)` / `StartAsync<T>(…)` return the callback's result. There is no built-in
cancellation token on these APIs — check your own `CancellationToken` inside the loop and
exit the callback normally (throwing out of the callback aborts the display and rethrows).

## Common failures

| Symptom | Cause / fix |
|---|---|
| Display "jumps"/repeats lines | Something else wrote to the console during the display |
| Nothing animates in CI/redirected | Non-interactive → fallback renderer by design |
| `InvalidOperationException … concurrently` | Nested/overlapping interactive operations |
| Progress never finishes | Started task never reached `MaxValue`; or `MaxValue` left at 100 while you increment by smaller amounts |
| Garbled bars on Windows | Console encoding is not UTF-8 / legacy console; set `Console.OutputEncoding = UTF8` |
