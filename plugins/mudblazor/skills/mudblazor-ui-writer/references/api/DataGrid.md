# DataGrid components — API (generated from source)

## Column<T> : MudComponentBase

Base class for columns in a `MudDataGrid{T}` such as `PropertyColumn{T, TProperty}`, `TemplateColumn{T}`, and `SelectColumn{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ValueChanged` | `EventCallback<T>` | – | The value stored in this column. |
| `Title` | `string?` | – | The display text for this column. |
| `HideSmall` | `bool` | `false` | Hides this column. Defaults to `false`. |
| `HeaderTemplate` | `RenderFragment<HeaderContext<T>>?` | `1` | The number of columns spanned by this column in the footer. Defaults to `1`. |
| `CellTemplate` | `RenderFragment<CellContext<T>>?` | – | The template used to display this column's value cells. |
| `FooterTemplate` | `RenderFragment<FooterContext<T>>?` | – | The template used to display this column's footer. |
| `GroupTemplate` | `RenderFragment<GroupDefinition<T>>?` | – | The template used to display this column's grouping. |
| `AggregateTemplate` | `RenderFragment<IEnumerable<T>>?` | – | The template used to display this column's aggregate. |
| `GroupBy` | `Func<T, object>?` | – | The function which groups values in this column. |
| `GroupByOrder` | `int` | `0` | The order in which values are grouped when there are more than one group Defaults to 0. |
| `GroupByOrderChanged` | `EventCallback<int>` | – | Occurs when the `GroupByOrder` property has changed. |
| `GroupIndented` | `bool` | `true` | Indents the column `48px` beyond its parent when grouped. |
| `GroupExpanded` | `bool` | `false` | Whether groups created from this column are expanded. Toggling the value will Toggle all grouped rows of this column. Defaults to `false`. |
| `GroupExpandedChanged` | `EventCallback<bool>` | – | Occurs when the `GroupExpanded` property has changed. |
| `Required` | `bool` | `true` | Requires a value to be set. Defaults to `true`. |
| `HeaderClass` | `string?` | `null` | The CSS class applied to the header. Defaults to `null`. Separate multiple classes with spaces. |
| `HeaderClassFunc` | `Func<IEnumerable<T>, string>?` | `null` | The function which calculates CSS classes for the header. Defaults to `null`. Separate multiple classes with spaces. |
| `HeaderStyle` | `string?` | – | The CSS style applied to this column's header. |
| `HeaderStyleFunc` | `Func<IEnumerable<T>, string>?` | – | The function which calculates CSS styles for the header. |
| `Sortable` | `bool?` | `null` | Sorts values in this column. Defaults to `null`. When set, this overrides the `SortMode` property. |
| `Resizable` | `bool?` | – | Allows this column's width to be changed. |
| `DragAndDropEnabled` | `bool?` | `null` | Allows this column to be reordered via drag-and-drop operations. Defaults to `null`. When set, this overrides the `DragDropColumnReordering` property. |
| `Filterable` | `bool?` | `null` | Allows filters to be used on this column. Defaults to `null`. When set, this overrides the `Filterable` property. |
| `ShowFilterIcon` | `bool?` | `null` | Shows the filter icon. Defaults to `null`. When set, this overrides the `ShowFilterIcons` property. |
| `Hideable` | `bool?` | `null` | Allows this column to be hidden. Defaults to `null`. When set, this overrides the `Hideable` property. |
| `Hidden` | `bool` | `false` | Hides this column. Defaults to `false`. |
| `HiddenChanged` | `EventCallback<bool>` | – | Occurs when the `Hidden` property has changed. |
| `Comparer` | `IComparer<object?>?` | `null` | Shows options for this column. Defaults to `null`. When set, this overrides the `ShowColumnOptions` property. |
| `InitialDirection` | `SortDirection` | `SortDirection.None` | The function used to sort values in this column. Defaults to `None`. |
| `InitialSortDirection` | `SortDirection` | `SortDirection.Ascending` | The sort direction applied when this column is unsorted and the header is clicked for the first time. Defaults to `Ascending`. |
| `SortIcon` | `string?` | `null`, which falls back to `SortIcon` | **[Obsolete]** The icon shown when `Sortable` is `true`. Defaults to `null`, which falls back to `SortIcon`. |
| `Groupable` | `bool?` | `null` | Allows values in this column to be grouped. Defaults to `null`. When set, this overrides the `Groupable` property. |
| `Grouping` | `bool` | – | Indicates whether this column is currently grouped. |
| `GroupingChanged` | `EventCallback<bool>` | – | Occurs when the `Grouping` property has changed. |
| `StickyLeft` | `bool` | – | Fixes this column to the left side. When `true`, this column will be visible even as the container is scrolled horizontally. |
| `StickyRight` | `bool` | – | Fixes this column to the right side. When `true`, this column will be visible even as the container is scrolled horizontally. |
| `FilterTemplate` | `RenderFragment<FilterContext<T>>?` | – | The template used to display this column's filter. |
| `FilterOperators` | `HashSet<string>` | `[]` | The operators to use for this column's filter. |
| `CellClass` | `string?` | `Culture` | The culture used to parse, filter, and display values in this column. Defaults to `Culture`. When neither value is set, formatting uses the current culture. |
| `CellClassFunc` | `Func<T, string>?` | – | The function used to determine CSS classes for this cell. Multiple classes must be separated by spaces. |
| `CellStyle` | `string?` | – | The CSS styles to apply to this cell. |
| `CellStyleFunc` | `Func<T, string>?` | – | The function which calculates CSS styles for this cell. |
| `Editable` | `bool` | `true` | Allows editing for this cell. Defaults to `true`. |
| `EditTemplate` | `RenderFragment<CellContext<T>>?` | – | The template for editing values in this cell. When `EditMode` is `Form`, the built-in Save button automatically invokes `CommittedItemChanges` — no extra handling is required. When `EditMode` is `Cell`, standard columns commit their value automatically on change. Custom controls inside an `EditTemplate` do not trigger `CommittedItemChanges` automatically. Track changes directly in a value-changed handler instead: <code> &lt;EditTemplate&gt; &lt;MudDatePicker Date="@context.Item.Date" DateChanged="@(d => { context.Item.Date = d; TrackChange(context.Item); })" /&gt; &lt;/EditTemplate&gt; </code> |
| `FooterClass` | `string?` | – | The CSS classes applied to this column's footer. Multiple classes must be separated by spaces. |
| `FooterClassFunc` | `Func<IEnumerable<T>, string>?` | – | The function which calculates CSS classes for this column's footer. Multiple classes must be separated by spaces. |
| `FooterStyle` | `string?` | – | The CSS styles to apply to this column's footer. |
| `FooterStyleFunc` | `Func<IEnumerable<T>, string>?` | – | The function which calculates CSS styles for this column's footer. |
| `EnableFooterSelection` | `bool` | – | Allows the footer to be selected. |
| `AggregateDefinition` | `AggregateDefinition<T>?` | – | The function which calculates aggregates for this column. |

## DataGridGroupRow<T> : MudComponentBase

Renders the collapsible header row for a group of items in a `MudDataGrid{T}` when grouping is enabled.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `DataGrid` | `MudDataGrid<T>` | `null!` | The data grid which contains this group row. |
| `RowClick` | `EventCallback<(MouseEventArgs args, T item, int index)>` | – | Occurs when a row is clicked. |
| `ContextRowClick` | `EventCallback<(MouseEventArgs args, T item, int index)>` | – | Occurs when a row is right-clicked. |
| `GroupDefinition` | `GroupDefinition<T>` | `null!` | The definition for this grouping level |
| `Items` | `IGrouping<object?, T>?` | – | The groups and items within this grouping. |
| `GroupClass` | `string?` | – | The CSS classes applied to the group row. |
| `GroupStyle` | `string?` | – | The CSS styles applied to the group row. |
| `GroupClassFunc` | `Func<GroupDefinition<T>, string>?` | – | The function used to compute CSS classes for the group row. |
| `GroupStyleFunc` | `Func<GroupDefinition<T>, string>?` | – | The function used to compute CSS styles for the group row. |
| `StyleClass` | `string?` | – | The CSS classes applied to this group row. |

## DataGridVirtualizeRow<T> : MudComponentBase

Renders the data rows of a `MudDataGrid{T}`, using virtualization to keep only the visible rows in the DOM for large data sets.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `DataGrid` | `MudDataGrid<T>` | `null!` | The data grid which contains this virtualized row. |
| `GroupedItems` | `IGrouping<object, T>?` | – | The grouped items rendered by this virtualized row. |
| `RowClick` | `EventCallback<(MouseEventArgs args, T item, int index)>` | – | Occurs when a row is clicked. |
| `ContextRowClick` | `EventCallback<(MouseEventArgs args, T item, int index)>` | – | Occurs when a row is right-clicked. |

## FilterHeaderCell<T> : MudComponentBase

The filter row cell shown for a `MudDataGrid{T}` column when `FilterMode` is `ColumnFilterRow`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Column` | `Column<T>` | – | The column associated with this filter cell. |
| `ChildContent` | `RenderFragment?` | – | The content within this filter cell. |

## FooterCell<T> : MudComponentBase

The footer cell displayed at the bottom of a `MudDataGrid{T}` column, typically showing totals or aggregate values.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Column` | `Column<T>?` | – | The column related to this footer cell. |
| `ChildContent` | `RenderFragment?` | – | The content within this footer cell. |
| `CurrentItems` | `IEnumerable<T>?` | – | The current values related to this footer cell. |
| `GroupItems` | `IEnumerable<T>?` | `null`, which scopes the footer to the whole grid` | The rows of the group this footer cell belongs to. Defaults to `null`, which scopes the footer to the whole grid. It is set for the footer rendered underneath a single group of rows. |

## HeaderCell<T> : MudComponentBase

The header cell displayed at the top of a `MudDataGrid{T}` column, showing the title along with sorting, filtering, and resizing controls.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Column` | `Column<T>?` | – | The column associated with this header cell. |
| `ChildContent` | `RenderFragment?` | – | The content within this header cell. |
| `SortDirection` | `SortDirection` | `None` | The direction to sort values in this column. Defaults to `None`. |

## HierarchyColumn<T> : MudComponentBase

Adds an expand or collapse button to each `MudDataGrid{T}` row, revealing nested detail content when expanded.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ClosedIcon` | `string?` | `ChevronRight` or `ChevronLeft` if RightToLeft` | The icon to display for the close button. Defaults to `ChevronRight` or `ChevronLeft` if RightToLeft. |
| `OpenIcon` | `string?` | `ExpandMore` | The icon to display for the open button. Defaults to `ExpandMore`. |
| `IconSize` | `Size` | `Size.Medium` | The size of the open and close icons. |
| `ButtonDisabledFunc` | `Func<T, bool>` | `_ => false` | The function which determines whether buttons are disabled. |
| `DragAndDropEnabled` | `bool?` | `false` | Allows this column to be reordered via drag-and-drop operations. Defaults to `null`. When set, this overrides the `DragDropColumnReordering` property. |
| `Hideable` | `bool?` | `null` | Allows this column to be hidden. Defaults to `null`. When set, this overrides the `Hideable` property. |
| `Hidden` | `bool` | `false` | Hides this column. Defaults to `false`. |
| `HiddenChanged` | `EventCallback<bool>` | – | Occurs when the `Hidden` property has changed. |
| `EnableHeaderToggle` | `bool` | `false` | Whether or not to show a button in the header to expand/collapse all columns. Defaults to `false`. |
| `HeaderClass` | `string?` | `null` | The CSS class applied to the header. Defaults to `null`. Separate multiple classes with spaces. |
| `HeaderClassFunc` | `Func<IEnumerable<T>, string>?` | `null` | The function which calculates CSS classes for the header. Defaults to `null`. Separate multiple classes with spaces. |
| `HeaderStyle` | `string` | `"width:0%;"` | The CSS style applied to this column's header. |
| `HeaderStyleFunc` | `Func<IEnumerable<T>, string>?` | – | The function which calculates CSS styles for the header. |
| `HeaderTemplate` | `RenderFragment<HeaderContext<T>>?` | – | The template used to display this column's header. |
| `CellTemplate` | `RenderFragment<CellContext<T>>?` | – | The template used to display this column's value cells. |
| `CellClass` | `string?` | `null` | The CSS classes applied to this column's value cells. Defaults to `null`. Separate multiple classes with spaces. |
| `CellClassFunc` | `Func<T, string>?` | `null` | The function which calculates CSS classes for this column's value cells. Defaults to `null`. Separate multiple classes with spaces. |
| `CellStyle` | `string?` | `null` | The CSS styles applied to this column's value cells. Defaults to `null`. |
| `CellStyleFunc` | `Func<T, string>?` | `null` | The function which calculates CSS styles for this column's value cells. Defaults to `null`. |
| `InitiallyExpandedFunc` | `Func<T, bool>?` | `a function that always returns `false` | The function which determines whether the row should be initially expanded. This function takes an item of type <typeparamref name="T"/> as input and returns a boolean indicating whether the row should be expanded. Requires item to override the Equals and GetHashCode methods. Defaults to a function that always returns `false`. |
| `HierarchyVisibilityToggled` | `EventCallback<DataGridHierarchyVisibilityToggledEventArgs<T>>` | – | Occurs when hierarchy visibility is toggled for an item in this column. |

## MudDataGrid<T> : MudComponentBase

Displays rows of data in a sortable, filterable grid with multiselection, pagination, inline editing, grouping, and aggregation.

*Supports server-side sorting, filtering, and paging of large datasets, including through an `IQueryable{T}` source.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `SortChanged` | `EventCallback<Dictionary<string, SortDefinition<T>>>` | – | Occurs when the `SortDefinitions` have changed. This callback is raised when the grid's sort state is updated. When `ServerData` or `VirtualizeServerData` is used, it is invoked before the data reload triggered by the new sort completes. |
| `SelectedItemChanged` | `EventCallback<T?>` | – | Occurs when the `SelectedItem` has changed. This typically occurs when a row has been clicked. |
| `SelectedItemsChanged` | `EventCallback<HashSet<T>?>` | – | Occurs when the `SelectedItems` have changed. This typically occurs when one or more rows have been clicked when `MultiSelection` is `true`. |
| `RowClick` | `EventCallback<DataGridRowClickEventArgs<T>>` | – | Occurs when a row has been clicked. |
| `RowContextMenuClick` | `EventCallback<DataGridRowClickEventArgs<T>>` | – | Occurs when a row has been right-clicked. |
| `CellClick` | `EventCallback<DataGridCellClickEventArgs<T>>` | – | Occurs when a cell has been clicked. |
| `CellContextMenuClick` | `EventCallback<DataGridCellClickEventArgs<T>>` | – | Occurs when a cell has been right-clicked. |
| `StartedEditingItem` | `EventCallback<T>` | – | Occurs when edit mode begins for an item. Use this event to react when editing starts. For form field changes, use `FormFieldChanged`. For save and cancel notifications, use `CommittedItemChanges`, `CommittedItemChanged`, or `CanceledEditingItem`. |
| `CanceledEditingItem` | `EventCallback<T>` | – | Occurs when editing of an item has been canceled. This event is raised instead of `CommittedItemChanges` and `CommittedItemChanged` when the edit operation is canceled. |
| `CommittedItemChanges` | `Func<T, Task<DataGridEditFormAction>>?` | – | Invoked when the user saves changes to an item, allowing validation, persistence, or other pre-commit work. In `Form`, this callback receives the edited copy before values are applied to the source item. Return `Close` to continue or `KeepOpen` to leave the form open for corrections. Use `CommittedItemChanged` to react after the source item has been updated. |
| `CommittedItemChanged` | `EventCallback<T>` | – | Occurs after committed changes have been applied to the underlying item. Use this callback for post-commit logic. In `Form`, it runs after `CommittedItemChanges` completes and after values are copied to the source item. In `Cell`, it runs after `CommittedItemChanges` completes, with the already-updated item. |
| `FormFieldChanged` | `EventCallback<FormFieldChangedEventArgs>` | – | Occurs when a field changes in the edit dialog. This event only occurs in `Form` and fires for individual field changes before save. |
| `HierarchyVisibilityToggled` | `EventCallback<DataGridHierarchyVisibilityToggledEventArgs<T>>` | – | Occurs when hierarchy visibility toggled. |
| `FilterChanged` | `EventCallback<IReadOnlyCollection<IFilterDefinition<T>>>` | – | Occurs when the active filters have changed. This callback receives the current active filters after the change is applied. |
| `TableAttributes` | `Dictionary<string, object?>` | `[]` | Attributes for the HTML table element, such as `aria-label` and `aria-labelledby`. |
| `ColumnsPanelReordering` | `bool` | `false` | Allows columns to be reordered via the columns panel. Defaults to `false`. |
| `DragDropColumnReordering` | `bool` | `false` | Allows columns to be reordered via drag-and-drop. Defaults to `false`. Can be overridden for individual columns via `DragAndDropEnabled`. |
| `DragIndicatorIcon` | `string` | `Icons.Material.Filled.DragIndicator` | The icon displayed when hovering over a draggable column. Defaults to `DragIndicator`. Use the `DragIndicatorSize` property to control this icon's size. |
| `DragIndicatorSize` | `Size` | `Size.Small` | The size of the icon displayed when hovering over a draggable column. Defaults to `Small`. Use the `DragIndicatorIcon` property to control which icon is displayed. |
| `DropAllowedClass` | `string` | `"drop-allowed"` | The CSS class applied to columns where a dragged column can be dropped. Defaults to `drop-allowed`. |
| `DropNotAllowedClass` | `string` | `"drop-not-allowed"` | The CSS class applied to columns where a dragged column cannot be dropped. Defaults to `drop-not-allowed`. |
| `ApplyDropClassesOnDragStarted` | `bool` | `false` | Shows drop locations for columns even when not currently dragging a column. Defaults to `false`. |
| `SortMode` | `SortMode` | `SortMode.Multiple` | Sorts data in the grid. Defaults to `Multiple`. Can be overridden for individual columns via `Sortable`. |
| `SortIcon` | `string` | `Icons.Material.Filled.ArrowUpward` | The icon shown when a column is sortable. Defaults to `ArrowUpward`. |
| `Filterable` | `bool` | `false` | Allows filtering of data in this grid. Defaults to `false`. Can be overridden for individual columns via `Filterable`. |
| `Hideable` | `bool` | `false` | Allows columns to be hidden. Defaults to `false`. Can be overridden for individual columns via `Hideable`. |
| `ShowColumnOptions` | `bool` | `true` | Shows options for columns. Defaults to `true`. Can be overridden for individual columns via `ShowColumnOptions`. |
| `Breakpoint` | `Breakpoint` | `Breakpoint.Xs` | The breakpoint at which the grid switches to mobile layout. Defaults to `Xs`. Supported values are `None`, `Xs`, `Sm`, `Md`, `Lg` and `Xl`. |
| `Elevation` | `int` | `1` | The size of the drop shadow. Defaults to `1`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Square` | `bool` | `false` | Disables rounded corners. Defaults to `false`. |
| `Outlined` | `bool` | `false` | Shows an outline around this grid. Defaults to `false`. |
| `Bordered` | `bool` | `false` | Shows left and right borders for each column. Defaults to `false`. |
| `ColGroup` | `RenderFragment?` | – | The content for any column groupings. This property specifies a groupedColumns of one or more columns in a table for formatting. For example: table colgroup col span="2" style="background-color:red" col style="background-color:yellow" colgroup header body table |
| `Dense` | `bool` | `false` | Uses compact padding. Defaults to `false`. |
| `Hover` | `bool` | `false` | Highlights rows when hovering over them. Defaults to `false`. |
| `Striped` | `bool` | `false` | Shows alternating row styles. Defaults to `false`. |
| `FixedHeader` | `bool` | – | Fixes the header in place even as the grid is scrolled. Set the `Height` property to make this grid scrollable. |
| `FixedFooter` | `bool` | – | Fixes the footer in place even as the grid is scrolled. Set the `Height` property to make this grid scrollable. |
| `ShowFilterIcons` | `bool` | `true` | Shows icons for each column filter. Defaults to `true`. Can be overridden for individual columns via `ShowFilterIcon`. |
| `FilterIconEmpty` | `string` | `Icons.Material.Outlined.FilterAlt` | The empty filter icon shown on a column when `Filterable` is `true` and no filters are applied to this column. |
| `FilterIconFilled` | `string` | `Icons.Material.Filled.FilterAlt` | The filled filter icon shown on a column when `Filterable` is `true` and filters are applied to this column. |
| `FilterIconClear` | `string` | `Icons.Material.Filled.FilterAltOff` | The clear filter icon shown on a column when `Filterable` is `true` to remove filters applied to this column. |
| `ColumnOptionsIcon` | `string` | `Icons.Material.Filled.MoreVert` | The icon used for column options menus in header cells. Defaults to `MoreVert`. |
| `FilterMode` | `DataGridFilterMode` | `Simple` | The way that this grid filters data. Defaults to `Simple`. |
| `FilterCaseSensitivity` | `DataGridFilterCaseSensitivity` | `Default` | The case sensitivity setting for columns with `string` values. Defaults to `Default`. |
| `FilterTemplate` | `RenderFragment<MudDataGrid<T>>?` | – | The template used to display each filter. |
| `FilterDefinitions` | `List<IFilterDefinition<T>>` | `new List<IFilterDefinition<T>>()` | The filter definitions for all columns. When using a `FilterMode` of `Simple`, this property is managed automatically. |
| `SortDefinitions` | `Dictionary<string, SortDefinition<T>>` | `new Dictionary<string, SortDefinition<T>>()` | The sort definitions for all columns. When using a `FilterMode` of `Simple`, this property is managed automatically. |
| `Virtualize` | `bool` | `false` | Renders only visible items instead of all items. Defaults to `false`. Only works when `Height` is set. This feature can improve performance for large data sets. |
| `RowLoadingContent` | `RenderFragment?` | – | A RenderFragment that will be used as a placeholder when the Virtualize component is asynchronously loading data. This placeholder is displayed for each item in the data source that is yet to be loaded. Useful for presenting a loading indicator in a data grid row while the actual data is being fetched from the server. |
| `OverscanCount` | `int` | `3` | The number of additional items rendered outside the visible region when `Virtualize` is `true`. Defaults to `3`. This value can reduce the amount of rendering during scrolling, but higher values can affect performance. |
| `ItemSize` | `float` | `50f` | The height of each row, in pixels, when `Virtualize` is `true`. |
| `RowClass` | `string?` | – | The CSS class applied to each row. Multiple classes must be separated by spaces. Note that some CSS settings are overridden by other styles, such as those from `MudTd`. |
| `RowStyle` | `string?` | – | The CSS styles applied to each row. Some CSS settings are overridden by other styles, such as those from `MudTd`. |
| `RowClassFunc` | `Func<T, int, string>?` | – | The function which calculates CSS classes for each row. The function passes the current item and row index as parameters. |
| `MultiSelection` | `bool` | – | The function which calculates CSS styles for each row. The function passes the current item and row index as parameters. |
| `SelectOnRowClick` | `bool` | `true` | Selects or deselects a row when it is clicked. Defaults to `true`. When `false`, rows are only selected through a `SelectColumn{T}` checkbox or in code. `RowClick` is raised either way, so a click can still be handled without changing `SelectedItem` or `SelectedItems`. |
| `SelectionChangeable` | `bool` | `true` | Allows the selection to be changed by the user. Defaults to `true`. When `false`, `SelectedItem` and `SelectedItems` can still be set in code. |
| `EditMode` | `DataGridEditMode?` | `Cell` | Controls how cell values are edited. Defaults to `Cell`. Only works when `ReadOnly` is `false`. |
| `EditTrigger` | `DataGridEditTrigger?` | `DataGridEditTrigger.Manual` | The behavior which begins editing a cell when `EditMode` is `Form`. Defaults to `Manual`. |
| `EditDialogOptions` | `DialogOptions?` | – | Any options applied to the edit dialog when `EditMode` is `Form`. |
| `CloneStrategy` | `ICloneStrategy<T>` | `SystemTextJsonDeepCloneStrategy<T>.Instance` | The technique used to copy items for editing. During edit mode, a copy of the item is edited, in order to allow an edit to be canceled. This property controls how that copy is made. |
| `Items` | `IEnumerable<T>?` | – | The data for this grid when `ServerData` is not set. One row will be displayed per item. Use the `ServerData` function instead of this property to get data on demand. |
| `Loading` | `bool` | `false` | Shows a loading animation while querying data. Defaults to `false`. This property is `true` while the `ServerData` function is executing. |
| `CanCancelEdit` | `bool` | `true` | Shows a cancel button during inline editing when `EditMode` is `Cell`. Defaults to `true`. |
| `LoadingProgressColor` | `Color` | `Color.Info` | The color of the loading progress indicator while `Loading` is `true`. Defaults to `Info`. Theme colors are supported. |
| `ToolBarContent` | `RenderFragment?` | – | Any custom content to show in this grid's toolbar. |
| `ToolBarWrapContent` | `bool` | `false` | Allows the toolbar's content to wrap onto multiple lines. Defaults to `false`. See `WrapContent`. |
| `HorizontalScrollbar` | `bool` | `false` | Shows a horizontal scrollbar. Defaults to `false`. |
| `ColumnResizeMode` | `ResizeMode` | `None` | The column resizing behavior for this grid. Defaults to `None`. Other values include `Column` and `Container`. |
| `HeaderClass` | `string?` | – | The CSS classes applied to the grid header. These classes are applied to the `thead` tag of the grid. Multiple classes must be separated by spaces. |
| `Height` | `string?` | `null` | The height of this grid. Defaults to `null`. Values such as `30%` and `500px` are allowed. When `null`, the grid will try to grow in height. Must be set when `Virtualize` is `true`. |
| `FooterClass` | `string?` | – | The CSS classes applied to the grid footer. These classes are applied to the `tfoot` tag of the grid. Multiple classes must be separated by spaces. |
| `QuickFilter` | `Func<T, bool>?` | `null` | The function which determines visibility of each item in this grid. Defaults to `null`. This function is typically used to implement a custom search. |
| `Header` | `RenderFragment?` | – | Any custom content for this grid's header. |
| `Columns` | `RenderFragment?` | – | Any custom content for this grid's columns. |
| `Culture` | `CultureInfo?` | `null` | The culture used to format numeric and date values. Can be overridden by `Culture`. Defaults to `null`. When no culture is set, cells use the current culture via .NET's default formatting behavior. Set this to `InvariantCulture` when invariant numeric and date formatting is required. |
| `ChildRowContent` | `RenderFragment<CellContext<T>>?` | – | The content shown for each cell. |
| `ChildRowRenderer` | `RenderFragment<CellContext<T>>?` | – | The custom renderer function for child row content. This provides an alternative to `ChildRowContent` with more control over the rendering. |
| `NoRecordsContent` | `RenderFragment?` | – | The content shown when there are no rows to display. |
| `LoadingContent` | `RenderFragment?` | – | The content shown while `Loading` is `true`. |
| `PagerContent` | `RenderFragment?` | – | The content shown for pagination. A `MudTablePager` is typically added here to break up rows into multiple pages. |
| `ServerData` | `Func<GridState<T>, CancellationToken, Task<GridData<T>>>?` | – | The function which gets data for this grid. The function accepts a `GridState{T}` with current sorting, filtering, and pagination parameters. Then, return a `GridData{T}` with a page of values, and the total (unpaginated) items set in `TotalItems`. When set, the `Items` property cannot be set. |
| `VirtualizeServerData` | `Func<GridStateVirtualize<T>, CancellationToken, Task<GridData<T>>>?` | – | The function which gets data for this grid. The function accepts a `GridStateVirtualize{T}` with current sorting, filtering, and pagination parameters. Then, return a `GridData{T}` with a list of values, and the total (unpaginated) items count in `TotalItems`. This property is used when you need to display a list without a paginator, but with loading data from the server as the scroll position changes. |
| `RowsPerPageChanged` | `EventCallback<int>` | `10` | The number of rows displayed for each page. Defaults to `10`. Applies when the `PagerContent` section contains a `MudTablePager`. When this property changes, the `RowsPerPageChanged` event occurs. |
| `CurrentPageChanged` | `EventCallback<int>` | `0` | The current page being displayed. Defaults to `0`. Applies when the `PagerContent` section contains a `MudTablePager`. |
| `ReadOnly` | `bool` | `true` | Prevents values from being edited. Defaults to `true`. When `false`, the edit behavior is controlled via `EditMode`. |
| `SelectedItems` | `HashSet<T>?` | – | The currently selected rows when `MultiSelection` is `true`. This property can be bound (`@bind-SelectedItems`) to initially select rows. Use `SelectedItem` when `MultiSelection` is `false`. To change the selection from code, assign a new set. A change is detected by reference, so editing the bound set in place, such as calling `Clear()`, does not update the grid. |
| `SelectedItem` | `T?` | – | The currently selected row when `MultiSelection` is `false`. This property can be bound (`@bind-SelectedItem`) to initially select a row. Use `SelectedItems` when `MultiSelection` is `true`. |
| `GroupExpanded` | `bool` | `false` | Expands grouped columns by default. Overrides `GroupExpanded` Defaults to `false`. Applies when `Groupable` is `true`. |
| `GroupClass` | `string?` | – | The CSS classes applied to column groups. Applies when `Groupable` is `true`. Multiple classes must be separated by spaces. |
| `GroupStyle` | `string?` | – | The CSS styles applied to column groups. Applies when `Groupable` is `true`. |
| `GroupClassFunc` | `Func<GroupDefinition<T>, string>?` | – | The function which determines CSS classes for column groups. Applies when `Groupable` is `true`. |
| `GroupStyleFunc` | `Func<GroupDefinition<T>, string>?` | – | The function which determines CSS styles for column groups. Applies when `Groupable` is `true`. |
| `ShowMenuIcon` | `bool` | `false` | Shows the settings icon in the grid header. Defaults to `false`. When `true`, an icon will be displayed to control column visibility, collapse all columns, or expand all columns. |
| `ExpandSingleRow` | `bool` | `false` | Ensures the user can only expand one Hierarchy row at a time. This only has an effect if you are using a Hierarchy column. Defaults to `false`. |
| `Comparer` | `IEqualityComparer<T>?` | `EqualityComparer<T>.Default` | The comparer used to determine row selection. Defaults to `Default`. This comparer decides whether a row is selected and whether an expanded hierarchy row is still the same row after the data is refreshed. Pass a stable instance: a change is detected by reference, so an inline `Comparer="@(new MyComparer())"` creates a fresh instance on every render and rebuilds the selection set every time. |
| `GroupTemplate` | `RenderFragment<GroupDefinition<T>>?` | – | The default template used to display column grouping for any column that is grouped. Can be overridden by using the column level GroupTemplate, defaults to `null`. |
| `ColumnReorderMode` | `DataGridDragAndDropColumnReorderMode` | `DataGridDragAndDropColumnReorderMode.Swap` | The behavior of the grid when the user reorders column headers via drag and drop. Defaults to `DataGridDragAndDropColumnReorderMode.Swap`. This mode applies to header drag-and-drop reordering. Reordering from the columns panel uses insert-by-index behavior. |
| `AllowUnsorted` | `bool` | `false` | Determines whether an unsorted state (`None`) is allowed when toggling sort directions. Defaults to `false`. When `false`, the sort direction toggles only between `Ascending` and `Descending`. When `true`, a third toggle state, `None`, is included. |
| `Validator` | `Interfaces.IForm` | `new DataGridRowValidator()` | The validator which validates values in each row. Use to bind validation and touched handling to outer form. |

## MudDataGridPager<T> : MudComponentBase

Pagination controls for navigating pages of a `MudDataGrid{T}`, with page-size selection and next and previous buttons.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `PageSizeSelector` | `bool` | `true` | Shows the page-size drop-down list. Defaults to `true`. Use `PageSizeOptions` to control the allowed page sizes. |
| `Disabled` | `bool` | `false` | Disables the back button, forward button, and page-size drop-down list. Defaults to `false`. |
| `PageSizeOptions` | `int[]` | `new int[] { 10, 25, 50, 100 }` | The allowed page sizes when `PageSizeSelector` is `true`. Defaults to `10`, `25`, `50`, `100`. |
| `InfoFormat` | `string` | `string.Empty` | The format for the first item, last item, and number of total items. Defaults to `{first_item}-{last_item} of {all_items}` (e.g. `0-25 of 77`). Available values are `{first_item}`, `{last_item}`, and `{all_items}`. |
| `RowsPerPageString` | `string` | `string.Empty` | The text to show for the "Rows per page:" label. Defaults to `Rows per page:`. Can be localized to other languages. |
| `ShowNavigation` | `bool` | `true` | Shows the pagination buttons. Defaults to `true`. |
| `ShowPageNumber` | `bool` | `true` | Shows the current page number. Defaults to `true`. |
| `AllItemsText` | `string` | `string.Empty` | Defines the text shown in the items per page dropdown when a user provides int.MaxValue as an option |

## PropertyColumn<T, TProperty> : Column<T>

Binds a `MudDataGrid{T}` column to an object property, with automatic sorting, filtering, and formatting of its values.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Property` | `Expression<Func<T, TProperty>>` | `Expression.Lambda<Func<T, TProperty>>(Expression.Default(typeof(TProperty)), Expression.Parameter(typeof(T)))` | The property whose values are displayed in the column. |
| `Format` | `string?` | `null` | The format applied to property values. Defaults to `null`. |

## SelectColumn<T> : TemplateColumn<T>

Checkboxes for selecting rows in a `MudDataGrid{T}`, with an optional header checkbox to select or clear all rows.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ShowInHeader` | `bool` | `true` | Shows a checkbox in the header. When `true`, all rows can be checked by selecting this checkbox. |
| `ShowInFooter` | `bool` | `false` | Shows a checkbox in the footer. When `true`, all rows can be checked by selecting this checkbox. |
| `Size` | `Size` | `Size.Medium` | The size of the checkbox icon. Defaults to `Medium`. |
| `DisabledFunc` | `Func<T, bool>?` | – | Determines if the checkbox for a specific row should be disabled. When set, this function is called for each row to determine if the checkbox should be disabled. |
| `AriaLabelFunc` | `Func<T, string?>?` | – | Provides a custom `aria-label` for a row selection checkbox. This function is evaluated for each row item. When the returned value is `null`, empty, or whitespace, the checkbox falls back to the default row selection label. |

## TemplateColumn<T> : Column<T>

Renders custom template content in a `MudDataGrid{T}` column instead of binding to a data property, useful for action buttons or computed cells.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Filterable` | `bool?` | `false` | Allows filters to be used on this column. Defaults to `false`. When set, this overrides the `Filterable` property. |
| `Sortable` | `bool?` | `false` | Sorts values in this column. Defaults to `false`. When set, this overrides the `SortMode` property. |
| `DragAndDropEnabled` | `bool?` | `false` | Allows this column to be reordered via drag-and-drop operations. Defaults to `false`. When set, this overrides the `DragDropColumnReordering` property. |
| `Resizable` | `bool?` | `false` | Allows this column's width to be changed. |
| `ShowColumnOptions` | `bool?` | `false` | Shows options for this column. Defaults to `false`. When set, this overrides the `ShowColumnOptions` property. |
| `InitiallyExpandedFunc` | `Func<T, bool>?` | – | Sets the initial expansion state of this column if used as a Hierarchy Column. Used internally for Hierarchy Columns, toggling will have no effect. |
| `HierarchyVisibilityToggled` | `EventCallback<DataGridHierarchyVisibilityToggledEventArgs<T>>` | – | Occurs when hierarchy visibility is toggled if used as a Hierarchy Column. |
| `ButtonDisabledFunc` | `Func<T, bool>` | `_ => false` | Sets the function which determines whether buttons are disabled if used in a Hierarchy Column. Used internally for Hierarchy Columns, setting this will have no effect. |
