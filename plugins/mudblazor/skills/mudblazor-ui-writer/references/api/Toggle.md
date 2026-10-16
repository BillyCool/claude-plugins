# Toggle components — API (generated from source)

## MudToggleGroup<T> : MudComponentBase

Toggle buttons grouped to select one or multiple values.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Disabled` | `bool` | – | Prevents the user from interacting with this toggle group. |
| `Value` | `T?` | – | The currently selected value. Applies when `SelectionMode` is `SingleSelection` or `ToggleSelection`. |
| `ValueChanged` | `EventCallback<T?>` | – | Occurs when `Value` has changed. Applies when `SelectionMode` is `SingleSelection` or `ToggleSelection`. |
| `Values` | `IEnumerable<T?>?` | – | The currently selected values. Applies when `SelectionMode` is `MultiSelection`. |
| `ValuesChanged` | `EventCallback<IEnumerable<T?>?>` | – | Occurs when `Values` has changed. Applies when `SelectionMode` is `MultiSelection`. |
| `SelectedClass` | `string?` | `null` | The CSS classes applied to selected items. Defaults to `null`. Multiple classes must be separated by spaces. |
| `CheckMarkClass` | `string?` | `null` | The CSS classes applied to checkmark icons. Defaults to `null`. Applies when `CheckMark` is `true`. Classes are applied to the `SelectedIcon` and `UnselectedIcon` icons. Multiple classes must be separated by spaces. |
| `Vertical` | `bool` | `false` | Uses a vertical layout for items. Defaults to `false`. |
| `Outlined` | `bool` | `true` | Shows an outline border. Defaults to `true`. |
| `Delimiters` | `bool` | `true` | Shows a line delimiter between each item. Defaults to `true`. |
| `Ripple` | `bool` | `true` | Show a ripple effect when the user clicks an item. Defaults to `true`. |
| `Size` | `Size` | `Size.Medium` | The size of each toggle item. Defaults to `Medium`. |
| `SelectionMode` | `SelectionMode` | `SingleSelection` | The selection behavior for this group. Defaults to `SingleSelection`. * `SingleSelection`: Allows only one item to be selected at a time. * `MultiSelection`: Allows multiple items to be selected. * `ToggleSelection`: Allows only one item to be selected, but the current selection can be deselected. |
| `Color` | `Color` | `Color.Primary` | The color of borders and the current selections. Defaults to `Primary`. |
| `CheckMark` | `bool` | `false` | Shows a checkmark next to each item. Defaults to `false`. When `true`, the checkmark icons can be customized via `SelectedIcon` and `UnselectedIcon`. |
| `FixedContent` | `bool` | `false` | Reserves space for checkmarks even when `CheckMark` is `false`. Defaults to `false`. |
| `ChildContent` | `RenderFragment?` | – | Contains the `MudToggleItem{T}` components of this group. |

## MudToggleItem<T> : MudComponentBase

An item as part of a `MudToggleGroup{T}`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this item. Defaults to `false`. |
| `Value` | `T?` | – | The value associated with this item. |
| `UnselectedIcon` | `string?` | `null` (no icon)` | The icon shown for the unselected checkmark. Defaults to `null` (no icon). Applies when `CheckMark` is `true`. |
| `SelectedIcon` | `string?` | `Icons.Material.Filled.Check` | The icon shown for the selected checkmark. Defaults to `Check`. Applies when `CheckMark` is `true`. |
| `Text` | `string?` | `null` | The text shown for this item. Defaults to `null`. Should be set if the displayed text differs from `Value?.ToString()`. Only shows if `ChildContent` is not set. |
| `ChildContent` | `RenderFragment<bool>?` | – | The custom content shown for this item. The provided `boolean` parameter is `true` when this item is selected. When set, `Text` will not be displayed. |
