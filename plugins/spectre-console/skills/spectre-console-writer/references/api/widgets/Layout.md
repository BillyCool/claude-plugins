# widgets/Layout — API (generated from source)

## `public sealed class Layout : Renderable, IRatioResolvable, IHasVisibility`

*core* · `src/Spectre.Console/Widgets/Layout/Layout.cs`

Represents a renderable to divide a fixed height into rows or columns.

**Constructors**

- `Layout(string name) : this(name, null)` — Initializes a new instance of the `Layout` class.
- `Layout(IRenderable renderable) : this(null, renderable)` — Initializes a new instance of the `Layout` class.
- `Layout(string? name = null, IRenderable? renderable = null)` — Initializes a new instance of the `Layout` class.

**Properties**

- `string? Name { get; set; }` — Gets or sets the name.
- `int Ratio { get; set; }` — Gets or sets the ratio.
- `int MinimumSize { get; set; }` — Gets or sets the minimum width.
- `int? Size { get; set; }` — Gets or sets the width.
- `bool IsVisible { get; set; }` = `true` — Gets or sets a value indicating whether or not the layout should be visible or not.

**Indexers**

- `Layout this[string name] { get; }` — Gets a child layout by it's name.

**Methods**

- `Layout GetLayout(string name)` — Gets a child layout by it's name.
- `Layout SplitRows(params Layout[] children)` — Splits the layout into rows.
- `Layout SplitColumns(params Layout[] children)` — Splits the layout into columns.
- `Layout Update(IRenderable renderable)` — Updates the containing `IRenderable`.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `Ratio(int ratio) -> Layout` — Sets the ratio of the layout.
- `Size(int size) -> Layout` — Sets the size of the layout.
- `MinimumSize(int size) -> Layout` — Sets the minimum width of the layout.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasVisibility`: `Invisible`, `Visible`
- via `IRenderable`: `GetSegments`

