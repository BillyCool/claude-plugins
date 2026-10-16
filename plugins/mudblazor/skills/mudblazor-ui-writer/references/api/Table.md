# Table components — API (generated from source)

## MudTable<T> : MudTableBase

A sortable, filterable table with multiselection, pagination, responsive layout, and child rows.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `RowTemplate` | `RenderFragment<T>?` | – | The columns for each row in this table. Use `MudTd` to define columns, and `context` to access item properties for each column. |
| `ChildRowContent` | `RenderFragment<T>?` | – | The optional nested content underneath each row. Use `MudTr` and `MudTd` to define the child content, and `context` to access item properties. |
| `RowEditingTemplate` | `RenderFragment<T>?` | – | The columns for each row when a row is being edited. Use `MudTd` to define columns, and `context` to access item properties for each column. Typically looks similar to rows in `RowTemplate` but with edit components. |
| `RowEditableFunc` | `Func<T, bool>?` | – | The function which determines if a row can be edited. Make the function return `true` to allow editing, and `false` to prevent it. When no value is set, all rows are considered editable. |
| `RowDisabledFunc` | `Func<T, bool>?` | – | The function which determines if a row is disabled. A disabled row ignores mouse events and uses `--mud-palette-text-disabled` as color. Make the function return `true` to diable the corresponding row. When no value is set, all rows are considered enabled. |
| `DisabledRowClass` | `string` | `"mud-table-row-disabled"` | The class to use for disabled rows. Defaults to `mud-table-row-disabled` |
| `Columns` | `RenderFragment<T?>?` | – | The columns for each row in this table. |
| `NoRecordsContent` | `RenderFragment?` | – | The content shown when there are no rows to display. No `MudTr` or `MudTd` is necessary. |
| `LoadingContent` | `RenderFragment?` | – | The content shown while `Loading` is `true` and the table has no rows. Rendered as a single table row containing one cell that spans the table width. Use this for simple messages or placeholders (for example "Loading…"). This content is displayed in addition to the table's loading animation. For multi-row or multi-column loading layouts, use `LoadingContentBody` instead. |
| `LoadingContentBody` | `RenderFragment?` | – | The content shown while `Loading` is `true` and the table has no rows. Rendered directly into the table body at the top. You must supply valid table row/cell markup (for example `&lt;MudTr&gt;` and `&lt;MudTd&gt;`). If you place plain text or non-table markup here most browsers will ignore it. Use this when you need to produce arbitrary rows and columns while the table is loading. This content is displayed in addition to the table's loading animation. For a single row column loading layout or text, use `LoadingContent` instead. This value is optional, and will override `LoadingContent` if not `null`. |
| `HorizontalScrollbar` | `bool` | `false` | Shows a horizontal scroll bar if the content exceeds the maximum width. Defaults to `false`. Typically `true` for tables with more columns than can fit on the screen. |
| `Filter` | `Func<T, bool>?` | – | The data to display. When set, `ServerData` should not be set. Use that property to get data from a back end. |
| `OnRowClick` | `EventCallback<TableRowClickEventArgs<T>>` | – | Occurs when a row has been clicked. |
| `OnRowMouseEnter` | `EventCallback<TableRowHoverEventArgs<T>>` | – | Occurs when the pointer hovers over a row. |
| `OnRowMouseLeave` | `EventCallback<TableRowHoverEventArgs<T>>` | – | Occurs when the pointer is no longer hovering over a row. |
| `RowClassFunc` | `Func<T, int, string>?` | – | The function which returns CSS classes for a row. The current item and row index are provided to the function. Multiple classes must be separated by spaces. |
| `RowStyleFunc` | `Func<T, int, string>?` | – | The function which returns CSS styles for a row. The current item and row index are provided to the function. |
| `SelectedItemChanged` | `EventCallback<T>` | – | The currently selected item when `MultiSelection` is `false`. When the selected item changes, the `SelectedItemChanged` event occurs. When `MultiSelection` is `true`, use the `SelectedItems` property. |
| `SelectedItemsChanged` | `EventCallback<HashSet<T>>` | – | The comparer used to determine selected items. Occurs when `MultiSelection` is `true`, otherwise `SelectedItemChanged` occurs. |
| `TableClass` | `string?` | – | Defines how rows are grouped together. Groups can be defined in multiple levels. |
| `GroupHeaderTemplate` | `RenderFragment<TableGroupData<object, T>>?` | – | The content for the header of each group when `GroupBy` is set. Use `MudTd` to define the cells in the group header. |
| `GroupHeaderClass` | `string?` | – | The custom CSS classes to apply to each group header row. Multiple classes must be separated by spaces. |
| `GroupHeaderStyle` | `string?` | – | The custom CSS styles to apply to each group header row. |
| `GroupFooterClass` | `string?` | – | The custom CSS classes to apply to each group footer row. Multiple classes must be separated by spaces. |
| `GroupFooterStyle` | `string?` | – | The custom CSS styles to apply to each group footer row. |
| `GroupFooterTemplate` | `RenderFragment<TableGroupData<object, T>>?` | – | The content for the footer of each group when `GroupBy` is set. Use `MudTd` to define the cells in the group footer. |
| `ServerData` | `Func<TableState, CancellationToken, Task<TableData<T>>>?` | – | Gets the sorted and paginated data for the table. Use the provided `TableState` to request items for a specific page index, page size, sort column, and sort order. Return a `TableData{T}` which contains the requested page of items and the total number of items (excluding pagination). Forward the `CancellationToken` to methods which support it such as `HttpClient` and `DbContext` to cancel ongoing requests. When this parameter is set, `Items` and `Filter` should not be set. |

## MudTableBase : MudComponentBase

Base class for `MudTable{T}` holding the type-independent table members such as paging, layout, and editing options.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `AriaLabel` | `string?` | `null` | **[Obsolete]** The aria-label for the HTML table element. Defaults to null. When set, renders as the table's `aria-label` attribute for accessibility. |
| `TableAttributes` | `Dictionary<string, object?>` | `[]` | Attributes for the HTML table element, such as `aria-label` and `aria-labelledby`. |
| `IsEditRowSwitchingBlocked` | `bool` | `false` | Forces a row being edited to be saved or canceled before a new row can be selected. Defaults to `false`. When `false`, a new row can be edited even if the previous one has not been saved or canceled. |
| `Elevation` | `int` | `1` | The size of the drop shadow. Defaults to `1`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Square` | `bool` | `false` | Uses square corners for the table. Defaults to `false`. |
| `Outlined` | `bool` | `true` | Shows borders around the table. Defaults to `true`. |
| `Bordered` | `bool` | – | Shows left and right borders for each table cell. |
| `Dense` | `bool` | `false` | Uses compact padding for all rows. Defaults to `false`. |
| `CellClass` | `string?` | – | The CSS classes applied to all cells of the table. Multiple classes must be separated by spaces. |
| `Hover` | `bool` | `false` | Highlights rows when hovering over them. Defaults to `false`. |
| `Striped` | `bool` | `false` | Uses alternating colors for table rows. Defaults to `false`. |
| `Breakpoint` | `Breakpoint` | `Breakpoint.Xs` | The screen width at which this table switches to small-device mode. Defaults to `Xs`. Allowed values are `None`, `Xs`, `Sm`, `Md`, `Lg`, and `Xl`. |
| `FixedHeader` | `bool` | `false` | Fixes the table header in place while the table is scrolled. Defaults to `false`. When set, `Height` must also be set. |
| `FixedFooter` | `bool` | `false` | Fixes the table footer in place while the table is scrolled. Defaults to `false`. When set, `Height` must also be set. |
| `Height` | `string?` | `null` | The fixed height of this table, as a CSS Value. Defaults to `null`. Accepts values such as `50%` or `500px`. When `null`, the table will try to grow to fit its content. When set, `FixedHeader` and `FixedFooter` can be enabled. |
| `SortLabel` | `string?` | `null` | The sort label shown when this table is in small-device mode and is sorting by a column. Defaults to `null`. |
| `AllowUnsorted` | `bool` | `true` | Allows a sort direction of `None` in addition to `Ascending` and `Descending`. Defaults to `true`. When `false`, the sort mode will only toggle between `Ascending` and `Descending`. |
| `RowsPerPageChanged` | `EventCallback<int>` | `null` | The maximum rows to display per page. Defaults to `null`. When set, rows beyond this number will overflow into separate pages. Requires a `MudTablePager` in the `PagerContent`. |
| `CurrentPageChanged` | `EventCallback<int>` | `0` (the first page)` | The index of the current page. Defaults to `0` (the first page). Requires a `MudTablePager` in the `PagerContent`. |
| `MultiSelection` | `bool` | `false` | Allows multiple rows to be selected with checkboxes. Defaults to `false`. |
| `SelectionChangeable` | `bool` | `true` | Disables the selection of rows but keep showing the selected rows. Defaults to `true`. Requires `MultiSelection` to be `true` and `Editable` to be `false`. |
| `SelectOnRowClick` | `bool` | `true` | Toggles the checkbox when a row is clicked. Defaults to `true`. Requires `MultiSelection` to be `true`, `SelectionChangeable` to be `true` and `Editable` to be `false`. |
| `ToolBarContent` | `RenderFragment?` | – | The custom content for the toolbar. |
| `Loading` | `bool` | `false` | Displays a loading animation while `ServerData` executes. Defaults to `false`. Becomes `true` before `ServerData` is called, then becomes `false`. When `true`, either a `MudProgressLinear` is displayed or custom content if `LoadingContent` or `LoadingContentBody` is set. |
| `LoadingProgressColor` | `Color` | `Color.Info` | The color of the `MudProgressLinear` while `Loading` is `true`. Defaults to `Info`. Has no effect if `LoadingContent` or `LoadingContentBody` is set. |
| `HeaderContent` | `RenderFragment?` | – | The content of this table's header. For basic headers, add `MudTh` components here to describe each column. For more customized headers (such as multi-row headers), set `CustomHeader` to `true` and use `MudTHeadRow` components here instead. |
| `CustomHeader` | `bool` | `false` | Enables customized headers beyond basic header columns. Defaults to `false`. When `true`, custom headers such as multiple-row headers can be used. |
| `HeaderClass` | `string?` | – | The CSS classes applied to the header. Multiple classes must be separated by spaces. |
| `ContainerStyle` | `string?` | `null` | The CSS styles applied to this table. Defaults to `null`. |
| `ContainerClass` | `string?` | `null` | The CSS classes applied to this table. Defaults to `null`. Multiple classes must be separated by spaces. |
| `FooterContent` | `RenderFragment?` | – | The content of this table's footer. For basic footers, add `MudTd` components here to describe each column. For more customized footers (such as multi-row footers), set `CustomFooter` to `true` and use `MudTFootRow` components here instead. |
| `CustomFooter` | `bool` | `false` | Enables customized footers beyond basic footer columns. Defaults to `false`. When `true`, custom footers such as multiple-row footers can be used. |
| `FooterClass` | `string?` | – | Add a class to the tfoot tag |
| `ColGroup` | `RenderFragment?` | `null` | Specifies formatting information for this table's columns such as size and style. Defaults to `null`. Add a set of `col` elements to style each column. For example: &lt;ColGroup&gt; &lt;col span="2" style="max-midth:120px; background-color:red"&gt; &lt;col style="background-color:yellow"&gt; &lt;/ColGroup&gt; |
| `PagerContent` | `RenderFragment?` | – | The custom pagination content for this table. Add a `MudTablePager` here to navigate multiple pages of data. |
| `ReadOnly` | `bool` | `false` | Prevents rows from being edited inline. Defaults to `false`. |
| `OnCommitEditClick` | `EventCallback<MouseEventArgs>` | – | Occurs when changes to a row being edited are committed. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `OnCancelEditClick` | `EventCallback<MouseEventArgs>` | – | Occurs when changes to a row being edited are canceled. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `OnPreviewEditClick` | `EventCallback<object?>` | – | Occurs before inline editing is enabled for a row. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `CommitEditTooltip` | `string?` | – | The tooltip shown next to the button which commits inline edits. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `CancelEditTooltip` | `string?` | – | The tooltip shown next to the button which cancels inline edits. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `CommitEditIcon` | `string` | `Icons.Material.Filled.Done` | The icon shown for the button which commits inline edits. Defaults to `Done`. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `CancelEditIcon` | `string` | `Icons.Material.Filled.Cancel` | The icon shown for the button which cancels inline edits. Defaults to `Cancel`. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `CanCancelEdit` | `bool` | – | Shows the cancel button during inline editing. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `ApplyButtonPosition` | `TableApplyButtonPosition` | `TableApplyButtonPosition.End` | The position of the button which commits inline edits. Defaults to `End`. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `EditButtonPosition` | `TableEditButtonPosition` | `TableEditButtonPosition.End` | The position of the button which begins inline editing. Defaults to `End`. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `EditTrigger` | `TableEditTrigger` | `TableEditTrigger.RowClick` | The behavior which begins inline editing. Defaults to `RowClick`. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `EditButtonContent` | `RenderFragment<EditButtonContext>?` | – | The content of the Edit button which starts inline editing. Requires `Editable` to be `true` and `ReadOnly` to be `false`. |
| `RowEditPreview` | `Action<object?>?` | – | Occurs before inline editing begins for a row. |
| `RowEditCommit` | `Action<object?>?` | – | Occurs when changes are committed for an row being edited. |
| `RowEditCancel` | `Action<object?>?` | – | Occurs when changed are canceled for a row being edited. |
| `TotalItems` | `int` | – | The total number of rows (excluding pages) when using `ServerData` for data. |
| `RowClass` | `string?` | – | The CSS classes applied to each row. Multiple classes must be separated by spaces. Some CSS classes will be overridden by `MudTd`. |
| `RowStyle` | `string?` | – | The CSS styles applied to each row. Some CSS styles will be overridden by `MudTd`. |
| `Virtualize` | `bool` | `false` | Uses virtualization to display large amounts of items efficiently. Defaults to `false`. Typically used for more than `1000` items. |
| `OverscanCount` | `int` | `3` | The number of additional items to render outside of view when `Virtualize` is `true`. Defaults to `3`. Can reduce the frequency of rendering during scrolling, but higher values can reduce performance. |
| `ItemSize` | `float` | `50f` | The height of each row, in pixels, when `Virtualize` is `true`. Defaults to `50`. |
| `PagerPosition` | `PagerPosition` | `PagerPosition.Bottom` | The position of the pager. Defaults to `Bottom`. |

## MudTableGroupRow<T> : MudComponentBase

A grouping of values for a column in a `MudTable{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `GroupDefinition` | `TableGroupDefinition<T>?` | – | The definition for this grouping level. Group definitions can be recursive. |
| `HeaderTemplate` | `RenderFragment<TableGroupData<object, T>>?` | – | The groups and items within this grouping. |
| `FooterTemplate` | `RenderFragment<TableGroupData<object, T>>?` | – | The custom content for this group's footer. |
| `Checkable` | `bool` | `false` | Displays a checkbox which selects or unselects all items within this group. Defaults to `false`. |
| `SelectionChangeable` | `bool` | `true` | Prevents the change of the current selection of all items withing this group. Defaults to `true`. Requires `Checkable` to be `true`. |
| `HeaderClass` | `string?` | – | The CSS classes applied to this group's header. Multiple classes must be separated by spaces. |
| `FooterClass` | `string?` | – | The CSS classes applied to this group's footer. Multiple classes must be separated by spaces. |
| `HeaderStyle` | `string?` | – | The CSS styles applied to this group's header. |
| `FooterStyle` | `string?` | – | The CSS styles applied to this group's footer. |
| `ExpandIcon` | `string` | `Icons.Material.Filled.ExpandMore` | The icon of the expand button when `Expandable` is `true`. Defaults to `ExpandMore`. |
| `CollapseIcon` | `string` | `Icons.Material.Filled.ChevronRight` | The icon of the collapse button when `Expandable` is `true`. Defaults to `ChevronRight`. |
| `OnRowClick` | `EventCallback<MouseEventArgs>` | – | Occurs when a grouping row is clicked. |

## MudTablePager : MudComponentBase

Pagination controls for a `MudTable{T}` that navigate between pages and change the number of rows shown per page.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `HideRowsPerPage` | `bool` | `false` | Hides the list of page sizes. Defaults to `false`. |
| `HidePageNumber` | `bool` | `false` | Hides the current page number. Defaults to `false`. |
| `HidePagination` | `bool` | `false` | Hides the list of page numbers. Defaults to `false`. |
| `HorizontalAlignment` | `HorizontalAlignment` | `HorizontalAlignment.Right` | The location of this pager relative to the parent `MudTable{T}`. Defaults to `Right`. |
| `PageSizeOptions` | `int[]` | `new[] { 10, 25, 50, 100 }` | The list of page sizes. Defaults to `10`, `25`, `50`, and `100`. Requires `HideRowsPerPage` to be `false`. |
| `InfoFormat` | `string` | `string.Empty` | The format of the text label. Defaults to `"{first_item}-{last_item} of {all_items}"` (e.g. `0-25 of 77`). You can use any of the following values: `{first_item}`: The index of the first row being displayed. `{last_item}`: The index of the last row being displayed. `{all_items}`: The total number of rows in all pages. |
| `AllItemsText` | `string` | `string.Empty` | The text displayed in the page-size dropdown when `PageSizeOptions` contains `MaxValue`. |
| `RowsPerPageString` | `string` | `string.Empty` | The text label for the current rows per page. |
| `FirstIcon` | `string` | `Icons.Material.Filled.FirstPage` | The icon for the "First Page" button. Defaults to `FirstPage`. |
| `BeforeIcon` | `string` | `Icons.Material.Filled.NavigateBefore` | The icon for the "Previous Page" button. Defaults to `NavigateBefore`. |
| `NextIcon` | `string` | `Icons.Material.Filled.NavigateNext` | The icon for the "Next Page" button. Defaults to `NavigateNext`. |
| `LastIcon` | `string` | `Icons.Material.Filled.LastPage` | The icon for the "Last Page" button. Defaults to `LastPage`. |

## MudTableSortLabel<T> : MudComponentBase

A clickable column which toggles the sort column and direction for a `MudTable{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this sort label. |
| `InitialDirection` | `SortDirection` | `SortDirection.None` | The sort direction when the `MudTable{T}` is first displayed. Defaults to `None`. When using multiple sort labels, the table will sort by the first sort label with a value other than `None`. |
| `InitialSortDirection` | `SortDirection` | `SortDirection.Ascending` | The sort direction applied when this label is unsorted and clicked for the first time. Defaults to `Ascending`. |
| `Enabled` | `bool` | `true` | Allows sorting by this column. Defaults to `true`. |
| `FullWidth` | `bool` | `false` | Expands this sort label to fill the available header width. Defaults to `false`. |
| `SortIcon` | `string` | `Icons.Material.Filled.ArrowUpward` | The icon for the sort button. Defaults to `ArrowUpward`. |
| `AppendIcon` | `bool` | `false` | Displays the icon before the label text. Defaults to `false`. |
| `SortDirectionChanged` | `EventCallback<SortDirection>` | – | Occurs when `SortDirection` has changed. |
| `SortBy` | `Func<T, object>?` | `null` | The custom function for sorting rows for this sort label. Defaults to `null`. When using `ServerData`, this function is not necessary. |
| `SortLabel` | `string?` | – | The text for this sort label. |

## MudTd : MudComponentBase

A cell within a `MudTr`, `MudTHeadRow`, or `MudTFootRow` row component.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this cell. |
| `DataLabel` | `string?` | – | The label for this cell when the table is in small-device mode. |
| `HideSmall` | `bool` | `false` | Hides this cell if the breakpoint is smaller than `Breakpoint`. Defaults to `false`. |

## MudTFootRow : MudComponentBase

A footer row displayed at the bottom of a `MudTable{T}` and each group.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this footer row. |
| `Checkable` | `bool` | `false` | Shows a checkbox which selects or deselects every row in the group. Defaults to `false`. |
| `SelectionChangeable` | `bool` | `true` | Prevents the change of the current selection of rows in the group. Defaults to `true`. Requires `Checkable` to be `true`. |
| `IgnoreCheckbox` | `bool` | `false` | Hides the extra column displayed when `MultiSelection` is `true`. Defaults to `false`. |
| `IgnoreEditable` | `bool` | `false` | Hides the extra column displayed when `Editable` is `true`. Defaults to `false`. |
| `Expandable` | `bool` | `false` | Shows an additional left and right margin when the parent group is expandable. Defaults to `false`. Managed automatically by table groups. |
| `OnRowClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this footer row is clicked. |

## MudTh : MudComponentBase

A header cell which labels a column of data for a `MudTable{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this header cell. |

## MudTHeadRow : MudComponentBase

A header row displayed at the top of a `MudTable{T}` and each group.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this header row. |
| `Checkable` | `bool` | `false` | Shows a checkbox which selects or deselects every row in the group. Defaults to `false`. |
| `SelectionChangeable` | `bool` | `true` | Prevents the change of the current selection of rows in the group. Defaults to `true`. Requires `Checkable` to be `true`. |
| `IgnoreCheckbox` | `bool` | `false` | Hides the extra column displayed when `MultiSelection` is `true`. Defaults to `false`. |
| `IgnoreEditable` | `bool` | `false` | Hides the extra column displayed when `Editable` is `true`. Defaults to `false`. |
| `Expandable` | `bool` | `false` | Shows an additional left and right margin when the parent group is expandable. Defaults to `false`. Managed automatically by table groups. |
| `OnRowClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this header row is clicked. |

## MudTr : MudComponentBase

A row of data within a `MudTable{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this data row. |
| `RowId` | `string?` | – | Optional ID for the row, used for programmatic scrolling and focusing. |
| `Item` | `object?` | – | The data being displayed for this row. |
| `Checkable` | `bool` | `false` | Displays a checkbox at the start of this row. Defaults to `false`. Managed automatically by the parent `MudTable{T}`. |
| `SelectionChangeable` | `bool` | `true` | Prevents the change of the current selection. Defaults to `true`. Requires `Checkable` to be `true`. Managed automatically by the parent `MudTable{T}`. |
| `Editable` | `bool` | `false` | Allows this row to be edited. Defaults to `false`. Managed automatically by the parent `MudTable{T}`. |
| `Expandable` | `bool` | `false` | Allows this row to expand to display nested content. Defaults to `false`. Managed automatically by the parent `MudTable{T}`. |
| `CheckedChanged` | `EventCallback<bool>` | – | Occurs when `Checked` has changed. |
| `Disabled` | `bool` | `false` | Disables mouse events and sets the color to `--mud-palette-text-disabled`. Defaults to `false`. Managed automatically by the parent `MudTable{T}`. |
| `DisabledClass` | `string` | `"mud-table-row-disabled"` | The class to use if `Disabled` is `true`. Defaults to `mud-table-row-disabled` |
