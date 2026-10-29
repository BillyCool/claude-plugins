# widgets/Grid — API (generated from source)

## `public sealed class Grid : JustInTimeRenderable, IExpandable`

*core* · `src/Spectre.Console/Widgets/Grid.cs`

A renderable grid.

**Constructors**

- `Grid()` — Initializes a new instance of the `Grid` class.

**Properties**

- `IReadOnlyList<GridColumn> Columns { get; }` — Gets the grid columns.
- `IReadOnlyList<GridRow> Rows { get; }` — Gets the grid rows.
- `bool Expand { get; set; }` — Gets or sets a value indicating whether or not the object should expand to the available space. If `false`, the object's width will be auto calculated.
- `int? Width { get; set; }` — Gets or sets the width of the grid.

**Methods**

- `Grid AddColumn()` — Adds a column to the grid.
- `Grid AddColumn(GridColumn column)` — Adds a column to the grid.
- `Grid AddRow(params IRenderable[] columns)` — Adds a new row to the grid.
- `protected override bool HasDirtyChildren()` — Checks if there are any children that has changed. If so, the underlying renderable needs rebuilding.
- `protected override IRenderable Build()` — Builds the inner renderable.

**Extension methods on this type** (call as `x.Method(...)`)

- `AddColumns(int count) -> Grid` — Adds a column to the grid.
- `AddColumns(params GridColumn[] columns) -> Grid` — Adds a column to the grid.
- `AddEmptyRow() -> Grid` — Adds an empty row to the grid.
- `AddRow(params string[] columns) -> Grid` — Adds a new row to the grid.
- `Width(int? width) -> Grid` — Sets the grid width.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IExpandable`: `Collapse`, `Expand`
- via `IRenderable`: `GetSegments`

## `public sealed class GridColumn : IColumn, IHasDirtyState`

*core* · `src/Spectre.Console/Widgets/GridColumn.cs`

Represents a grid column.

**Properties**

- `int? Width { get; set; }` — Gets or sets the width of the column. If `null`, the column will adapt to its contents.
- `bool NoWrap { get; set; }` — Gets or sets a value indicating whether wrapping of text within the column should be prevented.
- `Padding? Padding { get; set; }` — Gets or sets the padding of the column. Vertical padding (top and bottom) is ignored.
- `Justify? Alignment { get; set; }` — Gets or sets the alignment of the column.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IAlignable`: `Alignment`, `LeftAligned`, `Centered`, `RightAligned`
- via `IColumn`: `NoWrap`, `Width`
- via `IPaddable`: `PadLeft`, `PadTop`, `PadRight`, `PadBottom`, `Padding`

## `public sealed class GridRow : IEnumerable<IRenderable>`

*core* · `src/Spectre.Console/Widgets/GridRow.cs`

Represents a grid row.

**Constructors**

- `GridRow(IEnumerable<IRenderable> items)` — Initializes a new instance of the `GridRow` class.

**Indexers**

- `IRenderable this[int index] { get; }` — Gets a row item at the specified grid column index.

**Methods**

- `IEnumerator<IRenderable> GetEnumerator()`

