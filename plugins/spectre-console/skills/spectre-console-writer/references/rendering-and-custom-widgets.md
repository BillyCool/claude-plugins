# Rendering model and custom widgets

Verified against `src/Spectre.Console/Rendering/**` and `Widgets/**` (0.57.2). Members:
`api/rendering.md`.

## How output happens

`console.Write(renderable)` → `RenderPipeline` (render hooks) → `renderable.Render(options, maxWidth)`
yields `Segment`s (text + `Style` + optional `Link`, or a line break / control code) → the
console backend turns segments into ANSI (or plain text if ANSI is unsupported), down-converting
colors to the detected `ColorSystem`. Layout is **width driven**: a parent calls
`Measure(options, maxWidth)` on children to learn their `Measurement(min, max)` and then renders
each with the width it allotted. Height is whatever the segments produce (except `Layout`,
`Align` with a height, and live displays which constrain it).

```
IRenderable
  Measurement Measure(RenderOptions options, int maxWidth)      // min/max cell widths
  IEnumerable<Segment> Render(RenderOptions options, int maxWidth)
```

Prefer deriving from `Renderable` (protected `Measure` is optional and defaults to
`Measurement(maxWidth, maxWidth)`; `Render` is abstract). `JustInTimeRenderable` (implement
`Build()` returning other renderables; call `MarkAsDirty()` in setters) is the easiest way to build
a *composite* widget — `Grid`, `Calendar`, `JsonText` are made this way.

## Easiest custom widget: compose existing ones

```csharp
public sealed class StatusCard : JustInTimeRenderable
{
    private string _title = "";
    private bool _ok;

    public string Title { get => _title; set => MarkAsDirty(() => _title = value); }
    public bool Ok { get => _ok; set => MarkAsDirty(() => _ok = value); }

    protected override IRenderable Build()
    {
        var color = _ok ? Color.Green : Color.Red;
        return new Panel(new Markup(_ok ? "[green]healthy[/]" : "[red]failing[/]"))
            .Header(Markup.Escape(_title))
            .BorderColor(color)
            .RoundedBorder();
    }
}
```

Use it like any other: `AnsiConsole.Write(new StatusCard { Title = "api", Ok = true });` — it also
works as a cell in a `Table`, a node in a `Tree`, or a `LiveDisplay` target.

## From scratch: emit segments

```csharp
public sealed class Meter : Renderable
{
    private readonly double _fraction;
    public Meter(double fraction) => _fraction = Math.Clamp(fraction, 0, 1);

    protected override Measurement Measure(RenderOptions options, int maxWidth)
        => new Measurement(10, maxWidth);               // can be as narrow as 10 cells

    protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)
    {
        var filled = (int)Math.Round(maxWidth * _fraction);
        var bar = options.Unicode ? '█' : '#';          // respect capabilities
        yield return new Segment(new string(bar, filled), new Style(Color.Green));
        yield return new Segment(new string('░', maxWidth - filled), new Style(Color.Grey));
        yield return Segment.LineBreak;                  // renderables end each line explicitly
    }
}
```

Rules for `Render`:
- Never emit more than `maxWidth` cells per line; use `Segment.CellCount()` (not `string.Length`) —
  wide characters/emoji occupy 2 cells. `Segment.Truncate(segments, maxWidth)` and
  `Segment.SplitLines(segments, maxWidth)` help.
- Emit `Segment.LineBreak` between lines (and typically after the last one).
- Honor `options.Unicode` / `options.Ansi` / `options.ColorSystem` for glyph and color choices.
- Wrap text with `Paragraph` (`p.Append("text", style)`) or `Text`, then
  `((IRenderable)p).Render(options, width)`, rather than hand-wrapping.
- To embed other widgets: `foreach (var seg in child.Render(options, width)) yield return seg;`
  or measure first with `child.Measure(options, width)`.
- `RenderOptions.Height` is non-null only when a host (Layout/Align/Live) gives you a fixed height.
- Set `Expand`-style behaviour by returning `Measurement(min, maxWidth)`; shrink-to-content by
  returning the true max.

## Rendering to strings / segments

```csharp
IAnsiConsole console = AnsiConsole.Console;
string ansi = console.ToAnsi(new Panel("hi"));                 // with escape codes
IEnumerable<Segment> segs = new Panel("hi").GetSegments(console); // IRenderable.GetSegments
```

For plain text in tests use `TestConsole` (`testing.md`) or `console.CreateRecorder().ExportText()`.

## Render hooks

`IRenderHook.Process(options, renderables)` lets you intercept everything written while a scope
is active (this is how live displays keep their frame on top). `RenderHookScope` /
`console.Pipeline.Attach(hook)` is the extension point — advanced; see `api/rendering.md`.
`Progress.UseRenderHook((renderable, tasks) => …)` is the supported way to wrap a progress display
(e.g. add a header panel).

## Style helpers inside renderables

`style.Combine(other)` merges two styles (the `other` wins where it's set). `Style` has
`Foreground/Background/Decoration` (init-only record struct) and `ToMarkup()`.
