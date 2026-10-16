# List components — API (generated from source)

## MudList<T> : MudComponentBase

A scrollable list for displaying text, avatars, and icons. Use lists to help users find a specific item and act on it.

*This component contains an optional `MudListSubheader` and one or more `MudListItem{T}`.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Color` | `Color` | `Color.Primary` | The color of the selected list item. Defaults to `Primary`. |
| `CheckBoxColor` | `Color` | `Color.Default` | The color of checkboxes when `SelectionMode` is `MultiSelection`. Defaults to `Default`. |
| `ChildContent` | `RenderFragment?` | – | The content within this list. |
| `ReadOnly` | `bool` | `false` | Prevents list items from being selected. Defaults to `false`. |
| `Padding` | `bool` | `false` | Applies vertical padding to this list. Defaults to `false`. |
| `Dense` | `bool` | `false` | Uses less vertical space for list items. Defaults to `false`. |
| `Gutters` | `bool` | `true` | Applies left and right padding to all list items. Defaults to `true`. |
| `Disabled` | `bool` | `false` | Prevents any list item from being clicked. Defaults to `false`. |
| `SelectionMode` | `SelectionMode` | `SelectionMode.SingleSelection` | Controls how list items are selected. Defaults to `SingleSelection`. Use `SingleSelection` to select one list item at a time. Use `MultiSelection` to allow selecting multiple list items. Use `ToggleSelection` to toggle selections on and off when clicked. |
| `SelectedValue` | `T?` | – | The currently selected value. This value is updated when `SelectionMode` is `SingleSelection`. |
| `SelectedValueChanged` | `EventCallback<T?>` | – | Occurs when `SelectedValue` has changed. This event occurs when `SelectionMode` is `SingleSelection`. |
| `SelectedValues` | `IReadOnlyCollection<T>?` | – | The currently selected values. This value is updated when `SelectionMode` is `MultiSelection`. |
| `SelectedValuesChanged` | `EventCallback<IReadOnlyCollection<T>?>` | – | Occurs when `SelectedValues` has changed. This event occurs when `SelectionMode` is `MultiSelection`. |
| `Comparer` | `IEqualityComparer<T?>` | `EqualityComparer<T?>.Default` | The comparer used to see if two list items are equal. Defaults to `Default`. |
| `CheckedIcon` | `string` | `Icons.Material.Filled.CheckBox` | The icon to use for checked checkboxes when `SelectionMode` is `MultiSelection`. Defaults to `CheckBox`. |
| `UncheckedIcon` | `string` | `Icons.Material.Filled.CheckBoxOutlineBlank` | The icon to use for unchecked checkboxes when `SelectionMode` is `MultiSelection`. Defaults to `CheckBoxOutlineBlank`. |

## MudListItem<T> : MudComponentBase

An item within a `MudList{T}` component.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Text` | `string?` | – | The text to display. |
| `SecondaryText` | `string?` | – | The secondary text displayed. This text is displayed under `Text`, in a smaller size. |
| `Value` | `T?` | – | The value associated with this item. |
| `AvatarContent` | `RenderFragment?` | – | The custom `MudAvatar` to display to the left of `Text`. When a value is set, `Icon` is ignored. |
| `Href` | `string?` | – | The URL to navigate to upon click. |
| `Target` | `string?` | `null` | The browser frame to open this link when `Href` is specified. Possible values include `_blank`, `_self`, `_parent`, `_top`, or a frame name . Defaults to `null`. |
| `ForceLoad` | `bool` | `false` | Causes a full page refresh when this list item is clicked and `Href` is set. Defaults to `false`. When `true`, bypasses client-side routing and forces the browser to load the new page from the server, whether or not the URI would normally be handled by the client-side router. See: `NavigateTo` |
| `Disabled` | `bool` | `false` | Prevents this list item from being clicked. Defaults to `false`. This value can be overridden by `Disabled`. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when this item is clicked. Defaults to `true`. |
| `KeyboardEnabled` | `bool` | `true` | Allows this item to handle keyboard input. Defaults to `true`. Set to `false` when a parent component owns keyboard navigation, which avoids a key interceptor per item. |
| `Icon` | `string?` | – | The icon to display for this list item. When `AvatarContent` is set, this property is ignored. |
| `IconColor` | `Color` | `Color.Inherit` | The color of the `Icon`. Defaults to `Inherit`. When `AvatarContent` is set, this property is ignored. |
| `IconSize` | `Size` | `Size.Medium` | The size of the `Icon`. Defaults to `Medium`. When `AvatarContent` is set, this property is ignored. |
| `ExpandIconColor` | `Color` | `Color.Default` | The color of the `ExpandLessIcon` and `ExpandMoreIcon` icons. Defaults to `Default`. |
| `ExpandLessIcon` | `string` | `Icons.Material.Filled.ExpandLess` | The icon displayed when `Expanded` is `true`. Defaults to `ExpandLess`. |
| `ExpandMoreIcon` | `string` | `Icons.Material.Filled.ExpandMore` | The icon displayed when `Expanded` is `false`. Defaults to `ExpandMore`. |
| `Inset` | `bool` | – | Applies an indent to this list item. |
| `Dense` | `bool?` | `false` | Uses less vertical padding between items. Defaults to `false`. |
| `Gutters` | `bool?` | `the value of the parent `Gutters` | Applies left and right padding to this list items. Defaults to the value of the parent `Gutters`. When set, it overrides the list's setting. |
| `Expanded` | `bool` | – | Expand or collapse nested list. Two-way bindable. Note: if you directly set this to true or false (instead of using two-way binding) it will initialize the nested list's expansion state. |
| `ExpandedChanged` | `EventCallback<bool>` | – | Occurs when `Expanded` has changed. |
| `ChildContent` | `RenderFragment?` | – | Display content of this list item. If set, this overrides Text |
| `OnClickPreventDefault` | `bool` | – | If set, clicking the list item will only execute the OnClick handler and prevent all other functionality such as following Href or selection. |
| `NestedList` | `RenderFragment?` | – | Add child list items here to create a nested list. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | List click event. Also called when `Href` is set |

## MudListSubheader : MudComponentBase

A header displayed as part of a `MudList{T}`.

*Typically used to describe a list.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this header. |
| `Gutters` | `bool` | `true` | Applies left and right padding to all list items. Defaults to `true`. |
| `Inset` | `bool` | – | Applies an indent to this header. |
