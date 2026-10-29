# widgets/Table — API (generated from source)

## `public sealed class Table : Renderable, IHasTableBorder, IExpandable`

*core* · `src/Spectre.Console/Widgets/Table/Table.cs`

A renderable table.

**Constructors**

- `Table()` — Initializes a new instance of the `Table` class.

**Properties**

- `IReadOnlyList<TableColumn> Columns { get; }` — Gets the table columns.
- `TableRowCollection Rows { get; }` — Gets the table rows.
- `TableBorder Border { get; set; }` = `TableBorder.Square` — Gets or sets the border.
- `Style? BorderStyle { get; set; }` — Gets or sets the box style.
- `bool UseSafeBorder { get; set; }` = `true` — Gets or sets a value indicating whether or not to use a "safe" border on legacy consoles that might not be able to render non-ASCII characters.
- `bool ShowHeaders { get; set; }` = `true` — Gets or sets a value indicating whether or not table headers should be shown.
- `bool ShowRowSeparators { get; set; }` — Gets or sets a value indicating whether or not row separators should be shown.
- `bool ShowFooters { get; set; }` = `true` — Gets or sets a value indicating whether or not table footers should be shown.
- `bool Expand { get; set; }` — Gets or sets a value indicating whether or not the table should fit the available space. If `false`, the table width will be auto calculated. Defaults to `false`.
- `int? Width { get; set; }` — Gets or sets the width of the table.
- `TableTitle? Title { get; set; }` — Gets or sets the table title.
- `TableTitle? Caption { get; set; }` — Gets or sets the table footnote.

**Methods**

- `Table AddColumn(TableColumn column)` — Adds a column to the table.
- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `AddColumns(params TableColumn[] columns) -> Table` — Adds multiple columns to the table.
- `AddRow(IEnumerable<IRenderable> columns) -> Table` — Adds a row to the table.
- `AddRow(params IRenderable[] columns) -> Table` — Adds a row to the table.
- `AddEmptyRow() -> Table` — Adds an empty row to the table.
- `AddColumn(string column, Action<TableColumn>? configure = null) -> Table` — Adds a column to the table.
- `AddColumns(params string[] columns) -> Table` — Adds multiple columns to the table.
- `AddRow(params string[] columns) -> Table` — Adds a row to the table.
- `InsertRow(int index, IEnumerable<IRenderable> columns) -> Table` — Inserts a row in the table at the specified index.
- `UpdateCell(int rowIndex, int columnIndex, IRenderable cellData) -> Table` — Updates a tables cell.
- `UpdateCell(int rowIndex, int columnIndex, string cellData) -> Table` — Updates a tables cell.
- `InsertRow(int index, params IRenderable[] columns) -> Table` — Inserts a row in the table at the specified index.
- `InsertRow(int index, params string[] columns) -> Table` — Inserts a row in the table at the specified index.
- `RemoveRow(int index) -> Table` — Removes a row from the table with the specified index.
- `Width(int? width) -> Table` — Sets the table width.
- `ShowHeaders() -> Table` — Shows table headers.
- `HideHeaders() -> Table` — Hides table headers.
- `ShowRowSeparators() -> Table` — Shows row separators.
- `HideRowSeparators() -> Table` — Hides row separators.
- `ShowFooters() -> Table` — Shows table footers.
- `HideFooters() -> Table` — Hides table footers.
- `Title(string text, Style? style = null) -> Table` — Sets the table title.
- `Title(TableTitle title) -> Table` — Sets the table title.
- `Caption(string text, Style? style = null) -> Table` — Sets the table caption.
- `Caption(TableTitle caption) -> Table` — Sets the table caption.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IExpandable`: `Collapse`, `Expand`
- via `IHasBorder`: `SafeBorder`, `NoSafeBorder`, `BorderStyle`, `BorderColor`
- via `IHasTableBorder`: `NoBorder`, `SquareBorder`, `AsciiBorder`, `Ascii2Border`, `AsciiDoubleHeadBorder`, `RoundedBorder`, `MinimalBorder`, `MinimalHeavyHeadBorder`, `MinimalDoubleHeadBorder`, `SimpleBorder`, `SimpleHeavyBorder`, `HorizontalBorder`, `HeavyBorder`, `HeavyEdgeBorder`, `HeavyHeadBorder`, `DoubleBorder`, `DoubleEdgeBorder`, `MinimalistBorder`, `MarkdownBorder`, `Border`
- via `IRenderable`: `GetSegments`

## `public sealed class TableCell : IRenderable`

*core* · `src/Spectre.Console/Widgets/Table/TableCell.cs`

Represents a table cell that can span multiple columns.

**Constructors**

- `TableCell(IRenderable content)` — Initializes a new instance of the `TableCell` class.
- `TableCell(string markup) : this(new Markup(markup ?? string.Empty))` — Initializes a new instance of the `TableCell` class.

**Properties**

- `IRenderable Content { get; }` — Gets the cell content.
- `int ColumnSpan { get; set; }` — Gets the number of columns this cell spans.

**Operators / conversions**

- `static implicit operator TableCell(string markup)` — Implicitly converts a `string` to a `TableCell`.

**Methods**

- `TableCell Span(int span)` — Sets the number of columns this cell should span.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IRenderable`: `GetSegments`

## `public sealed class TableColumn : IColumn`

*core* · `src/Spectre.Console/Widgets/Table/TableColumn.cs`

Represents a table column.

**Constructors**

- `TableColumn(string header) : this(new Markup(header).Overflow(Overflow.Ellipsis))` — Initializes a new instance of the `TableColumn` class.
- `TableColumn(IRenderable header)` — Initializes a new instance of the `TableColumn` class.

**Properties**

- `IRenderable Header { get; set; }` — Gets or sets the column header.
- `IRenderable? Footer { get; set; }` — Gets or sets the column footer.
- `int? Width { get; set; }` — Gets or sets the width of the column. If `null`, the column will adapt to its contents.
- `Padding? Padding { get; set; }` — Gets or sets the padding of the column. Vertical padding (top and bottom) is ignored.
- `bool NoWrap { get; set; }` — Gets or sets a value indicating whether wrapping of text within the column should be prevented.
- `Justify? Alignment { get; set; }` — Gets or sets the alignment of the column.

**Extension methods on this type** (call as `x.Method(...)`)

- `Header(string header) -> TableColumn` — Sets the table column header.
- `Header(IRenderable header) -> TableColumn` — Sets the table column header.
- `Footer(string footer) -> TableColumn` — Sets the table column footer.
- `Footer(IRenderable footer) -> TableColumn` — Sets the table column footer.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IAlignable`: `Alignment`, `LeftAligned`, `Centered`, `RightAligned`
- via `IColumn`: `NoWrap`, `Width`
- via `IPaddable`: `PadLeft`, `PadTop`, `PadRight`, `PadBottom`, `Padding`

## `public sealed class TableRow : IEnumerable<IRenderable>`

*core* · `src/Spectre.Console/Widgets/Table/TableRow.cs`

Represents a table row.

**Constructors**

- `TableRow(IEnumerable<IRenderable> items) : this(items, false, false)` — Initializes a new instance of the `TableRow` class.

**Properties**

- `int Count { get; }` — Gets the number of columns in the row.

**Indexers**

- `IRenderable this[int index] { get; }` — Gets a row item at the specified table column index.

**Methods**

- `IEnumerator<IRenderable> GetEnumerator()`

## `public sealed class TableRowCollection : IReadOnlyList<TableRow>`

*core* · `src/Spectre.Console/Widgets/Table/TableRowCollection.cs`

Represents a collection holding table rows.

**Properties**

- `int Count { get; }` — Gets the number of rows in the collection.

**Methods**

- `int Add(IEnumerable<IRenderable> columns)` — Adds a new row.
- `int Insert(int index, IEnumerable<IRenderable> columns)` — Inserts a new row at the specified index.
- `void Update(int row, int column, IRenderable cellData)` — Update a table cell at the specified index.
- `void RemoveAt(int index)` — Removes a row at the specified index.
- `void Clear()` — Clears all rows.
- `IEnumerator<TableRow> GetEnumerator()`

## `public sealed class TableTitle`

*core* · `src/Spectre.Console/Widgets/Table/TableTitle.cs`

Represents a table title such as a heading or footnote.

**Constructors**

- `TableTitle(string text, Style? style = null)` — Initializes a new instance of the `TableTitle` class.

**Properties**

- `string Text { get; }` — Gets the title text.
- `Style? Style { get; set; }` — Gets or sets the title style.

**Methods**

- `TableTitle SetStyle(Style? style)` — Sets the title style.
- `TableTitle SetStyle(string style)` — Sets the title style.

