# TreeView components — API (generated from source)

## MudTreeView<T> : MudComponentBase

An extensively customizable tree view component for displaying hierarchical data, featuring item selection, lazy-loading, and templating support.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Color` | `Color` | `Color.Primary` | The color of the selected item. Defaults to `Primary`. |
| `CheckBoxColor` | `Color` | `Default` | The color of checkboxes. Defaults to `Default`. Only applies when `SelectionMode` is `MultiSelection`. |
| `SelectionMode` | `SelectionMode` | `SelectionMode.SingleSelection` | Controls how many items can be selected at one time. Defaults to `SingleSelection`. |
| `TriState` | `bool` | `true` | Uses checkboxes which support an undetermined state. Defaults to `true`. Only applies when `SelectionMode` is `MultiSelection`. When set, an item's checkbox will be in the "undetermined" state if child items have a mix of checked and unchecked states. |
| `AutoSelectParent` | `bool` | `true` | Automatically checks an item if all children are selected. Defaults to `true`. Only applies when `SelectionMode` is `MultiSelection`. Items will also be deselected if any children are deselected. |
| `ExpandOnClick` | `bool` | `false` | Expands an item with children if it is clicked anywhere (not just the expand/collapse buttons). Defaults to `false`. |
| `ExpandOnDoubleClick` | `bool` | `false` | Expands an item with children if it is double-clicked anywhere (not just the expand/collapse buttons). Defaults to `false`. |
| `AutoExpand` | `bool` | `false` | Automatically expands items to show selected children. Defaults to `false`. |
| `Hover` | `bool` | `false` | Shows an effect when items are hovered over. Defaults to `false`. |
| `Dense` | `bool` | `false` | Uses compact vertical padding. Defaults to `false`. |
| `Height` | `string?` | `null` | Sets a fixed height. Defaults to `null`. Can be a CSS value such as `500px` or `30%`. When set, items can be scrolled vertically. Otherwise, the height will grow automatically. |
| `MaxHeight` | `string?` | `null` | Sets a maximum height. Defaults to `null`. Can be a CSS value such as `500px` or `30%`. When set, items can be scrolled vertically. Otherwise, the height will grow automatically. |
| `Width` | `string?` | `null` | Sets a fixed width. Defaults to `null`. Can be a CSS value such as `500px` or `30%`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with any items. Defaults to `false`. |
| `FilterFunc` | `Func<ITreeItemData<T>, Task<bool>>?` | `null` | Determines whether items are displayed. Defaults to `null`. The function provides an item and should return `true` to display the item, or `false` to hide it. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when an item is clicked. Defaults to `true`. |
| `Items` | `IReadOnlyCollection<ITreeItemData<T>>?` | `Array.Empty<ITreeItemData<T>>()` | The items being displayed. |
| `SelectedValue` | `T?` | – | The currently selected value. Applies when `SelectionMode` is `SingleSelection`. |
| `SelectedValueChanged` | `EventCallback<T?>` | – | Occurs when `SelectedValue` has changed. |
| `SelectedValues` | `IReadOnlyCollection<T>?` | – | The currently selected values. Applies when `SelectionMode` is `MultiSelection` or `ToggleSelection`. |
| `SelectedValuesChanged` | `EventCallback<IReadOnlyCollection<T>?>` | – | Occurs when `SelectedValues` has changed. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. Applies when `ItemTemplate` and `Items` are both not set. |
| `ItemTemplate` | `RenderFragment<ITreeItemData<T>>?` | – | The template for rendering each item. |
| `Comparer` | `IEqualityComparer<T?>` | `EqualityComparer<T?>.Default` | The comparer used to check if two items are equal. |
| `ServerData` | `Func<T?, Task<IReadOnlyCollection<TreeItemData<T>>>>?` | – | The function for asynchronously loading items. When set, the function will be called to load the children of a parent item. When the parent node is `null`, top-level items should be returned. |
| `ReadOnly` | `bool` | `false` | Prevents selections from being changed. Defaults to `false`. When `true`, selections cannot be changed, but the current selections will continue to be displayed. |
| `CheckedIcon` | `string` | `Icons.Material.Filled.CheckBox` | The icon displayed for checked items. Defaults to `CheckBox`. |
| `UncheckedIcon` | `string` | `Icons.Material.Filled.CheckBoxOutlineBlank` | The icon displayed for unchecked items. Defaults to `CheckBoxOutlineBlank`. |
| `IndeterminateIcon` | `string` | `Icons.Material.Filled.IndeterminateCheckBox` | The icon displayed for indeterminate items. Defaults to `IndeterminateCheckBox`. Only applies when `TriState` is `true`. |

## MudTreeViewItem<T> : MudComponentBase

An expandable branch of a `MudTreeView{T}`.

*Used as the data model of the tree.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Value` | `T?` | `null` | The value associated with this item. Defaults to `null`. Acts as the displayed text if no text is set. |
| `Text` | `string?` | `null` | The text to display. Defaults to `null`. When no value is set, the `Value` is used if it is a basic value such as `string` or `int`, etc. Ignored if `BodyContent` is set. |
| `TextTypo` | `Typo` | `Typo.body1` | The size of the text. Defaults to `body1`. |
| `TextClass` | `string?` | `null` | The CSS classes applied to the `Text` parameter. Defaults to `null`. Multiple values must be separated by spaces. |
| `EndText` | `string?` | – | The text at the end of the item. Ignored if `BodyContent` is set. |
| `EndTextTypo` | `Typo` | `Typo.body1` | The size of the end text. Defaults to `body1`. |
| `EndTextClass` | `string?` | `null` | The CSS classes applied to the `EndText` parameter. Defaults to `null`. Multiple values must be separated by spaces. |
| `Visible` | `bool` | `true` | Whether this item and its children are displayed. Defaults to `true`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this item. Defaults to `false`. |
| `ReadOnly` | `bool` | `false` | Prevents this item from being selected. Defaults to `false`. |
| `CanExpand` | `bool` | `true` | Allows this item to expand to display children. Defaults to `true`. A value of `false` is typically used for lazy-loaded items via `ServerData`. |
| `ChildContent` | `RenderFragment?` | – | The child items within this item. Must be one or more `MudTreeViewItem{T}` components. Only applies when `Content` is not set. |
| `Content` | `RenderFragment?` | – | The custom content within this item. When set, completely controls the rendering of child items. For `MudTreeViewItem{T}` children, use `Items` or `ChildContent`. |
| `BodyContent` | `RenderFragment<MudTreeViewItem<T>>?` | – | The custom content for the text, end text, and end icon. When set, the `Text`, `EndText`, and `EndIcon` properties are ignored. |
| `Items` | `IReadOnlyCollection<ITreeItemData<T>>?` | – | The child items underneath this item. |
| `ItemsChanged` | `EventCallback<IReadOnlyCollection<ITreeItemData<T>>?>` | – | Occurs when `Items` has changed. |
| `Expanded` | `bool` | `false` | Shows the children items underneath this item. Defaults to `false`. |
| `ExpandedChanged` | `EventCallback<bool>` | – | Occurs when `Expanded` has changed. |
| `Selected` | `bool` | `false` | Selects this item. Defaults to `false`. Can be set alongside other items if `SelectionMode` is `MultiSelection` or `ToggleSelection`. |
| `Icon` | `string?` | `null` | The item shown before the text. Defaults to `null`. |
| `IconExpanded` | `string?` | `null` | The icon shown when this item is expanded. Defaults to `null`. |
| `IconColor` | `Color` | `Color.Default` | The color of the icon when `Icon` is set. Defaults to `Default`. |
| `EndIcon` | `string?` | – | Icon placed after the text if set. Ignored if `BodyContent` is set. |
| `EndIconColor` | `Color` | `Color.Default` | The color of the end icon when `EndIcon` is set. Defaults to `Default`. |
| `ExpandButtonIcon` | `string` | `Icons.Material.Filled.ChevronRight` | The icon shown for the expand/collapse button. Defaults to `ChevronRight`. |
| `ExpandButtonIconColor` | `Color` | `Color.Default` | The color of the expand/collapse button. Defaults to `Default`. |
| `LoadingIcon` | `string` | `Icons.Material.Filled.Loop` | The icon shown while this item is loading. Defaults to `Loop`. |
| `LoadingIconColor` | `Color` | `Color.Default` | The color of the loading icon. Defaults to `Default`. |
| `SelectedChanged` | `EventCallback<bool>` | – | Occurs when `Selected` has changed. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this item has been clicked. |
| `OnDoubleClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this item has been double-clicked. |

## MudTreeViewItemToggleButton : MudComponentBase

Toggles the expansion state of a `MudTreeViewItem{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Visible` | `bool` | `false` | Shows this button. Defaults to `false`. |
| `Disabled` | `bool` | – | Prevents the user from interacting with this button. |
| `Expanded` | `bool` | `false` | Whether this button is in the "expanded" state. Defaults to `false`. |
| `Loading` | `bool` | `false` | Displays the loading icon. Defaults to `false`. Typically used when time is required to load child items. |
| `ExpandedChanged` | `EventCallback<bool>` | – | Occurs when `Expanded`. |
| `LoadingIcon` | `string` | `Icons.Material.Filled.Loop` | The icon shown when in the "loading" state. Defaults to `Loop`. |
| `LoadingIconColor` | `Color` | `Color.Default` | The color of the loading icon. Defaults to `Default`. |
| `ExpandedIcon` | `string` | `Icons.Material.Filled.ChevronRight` | The expand/collapse icon. Defaults to `ChevronRight`. |
| `ExpandedIconColor` | `Color` | `Color.Default` | The color of the expand/collapse icon. Defaults to `Default`. |
