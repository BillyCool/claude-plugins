# widgets/ControlCode — API (generated from source)

## `public sealed class ControlCode : Renderable`

*core* · `src/Spectre.Console/Widgets/ControlCode.cs`

A control code.

**Constructors**

- `ControlCode(string control)` — Initializes a new instance of the `ControlCode` class.

**Methods**

- `static ControlCode Create( IReadOnlyCapabilities capabilities, Action<AnsiWriter> action)` — Creates a new `ControlCode` using a `AnsiWriter`.
- `static ControlCode Create( IAnsiConsole console, Action<AnsiWriter> action)` — Creates a new `ControlCode` using a `AnsiWriter`.
- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IRenderable`: `GetSegments`

