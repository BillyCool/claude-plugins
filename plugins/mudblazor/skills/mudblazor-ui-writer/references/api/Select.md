# Select components — API (generated from source)

## MudSelect<T> : MudBaseInput<T>

A dropdown input for selecting an item from a list of options.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Open` | `bool` | – | Whether this select dropdown is open and the options are visible. When this property changes, `OpenChanged` occurs. |
| `OpenChanged` | `EventCallback<bool>` | – | Occurs when `Open` has changed. |
| `PopoverFixed` | `bool` | `false` | Displays the dropdown popover in a fixed position, even while scrolling. Defaults to `false`. |
| `RelativeWidth` | `DropdownWidth` | `DropdownWidth.Relative` | Determines the width of this Popover dropdown in relation to the parent container. Defaults to `Relative`. When `Relative`, restricts the max-width of the component to the width of the parent container When `Adaptive`, restricts the min-width of the component to the width of the parent container |
| `FitContent` | `bool` | `false` | Sets the container width to match its contents. Defaults to `false`. Requires FullWidth to be `false` |
| `OuterClass` | `string?` | `null` | The CSS classes applied to the outer `div`. Defaults to `null`. Multiple classes must be separated by spaces. |
| `InputClass` | `string?` | `null` | The CSS classes applied to the input. Defaults to `null`. Multiple classes must be separated by spaces. |
| `OpenIcon` | `string` | `Icons.Material.Filled.ArrowDropDown` | The icon for opening the popover of items. Defaults to `ArrowDropDown`. |
| `CloseIcon` | `string` | `Icons.Material.Filled.ArrowDropUp` | The icon for closing the popover of items. Defaults to `ArrowDropUp`. |
| `ClearIcon` | `string` | `Icons.Material.Filled.Clear` | The icon displayed for the clear button when `Clearable` is `true`. Defaults to `Clear`. |
| `PopoverClass` | `string?` | `null` | The CSS classes applied to the popover. Defaults to `null`. Multiple classes must be separated by spaces. |
| `ListClass` | `string?` | `null` | The CSS classes applied to the internal list. Defaults to `null`. Multiple classes must be separated by spaces. |
| `Dense` | `bool` | `false` | Uses compact vertical padding for all items. Defaults to `false`. |
| `MaxHeight` | `int` | `300` | The maximum height, in pixels, of the popover of items. Defaults to `300`. |
| `AnchorOrigin` | `Origin` | `Origin.BottomLeft` | The location where the popover will open from. Defaults to `BottomLeft`. |
| `TransformOrigin` | `Origin` | `Origin.TopLeft` | The transform origin point for the popover. Defaults to `TopLeft`. |
| `SelectAllText` | `string` | `string.Empty` | The text of the "Select all" checkbox. Defaults to `"Select all"`. Only applies when `SelectAll` is `true`. |
| `CheckedIcon` | `string` | `Icons.Material.Filled.CheckBox` | The icon used for selected items. Defaults to `CheckBox`. Only applies when `MultiSelection` is `true`. |
| `UncheckedIcon` | `string` | `Icons.Material.Filled.CheckBoxOutlineBlank` | The icon used for unselected items. Defaults to `CheckBoxOutlineBlank`. Only applies when `MultiSelection` is `true`. |
| `IndeterminateIcon` | `string` | `Icons.Material.Filled.IndeterminateCheckBox` | The icon used when at least one, but not all, items are selected. Defaults to `IndeterminateCheckBox`. Only applies when `MultiSelection` is `true`. |
| `ChildContent` | `RenderFragment?` | – | The content within this component, typically a list of `MudSelectItem{T}` components. |
| `Modal` | `bool?` | `ModalOverlay` | Prevents interaction with background elements while this list is open. Defaults to `ModalOverlay`. |
| `MultiSelection` | `bool` | `false` | Allows multiple values to be selected via checkboxes. Defaults to `false`. When `false`, only one value can be selected at a time. |
| `SelectAll` | `bool` | `false` | Shows a "Select all" checkbox to select all items. Defaults to `false`. Only applies when `MultiSelection` is `true`. |
| `SelectionOnEnter` | `bool` | – | If `true`, navigating with arrow keys will only highlight items without updating the selected value. The selection must be confirmed by pressing Enter or clicking the item. |
| `LockScroll` | `bool` | `false` | Prevents scrolling while the dropdown is open. Defaults to `false`. |
| `ToStringFunc` | `Func<T?, string?>?` | – | The function for the `Text` in drop-down items. |
| `Comparer` | `IEqualityComparer<T?>?` | – | The comparer for testing equality of selected values. |
| `Delimiter` | `string` | `", "` | The string used to separate multiple selected values. Defaults to `", "`. Only applies when `MultiSelection` is `true`. |
| `MultiSelectionTextFunc` | `Func<IReadOnlyList<string?>?, string>?` | `null` | The custom function for setting the `Text` from a list of selected items. Defaults to `null`. |
| `QuickSearchInterval` | `TimeSpan` | `TimeSpan.Zero` | The `TimeSpan` interval for accepting characters for search input. Defaults to `Zero` for single-character searches. Set to a value greater than zero to enable multi-character searches within the specified interval. |
| `Strict` | `bool` | `false` | Restricts the selected values to the ones defined in `MudSelectItem{T}` items. Defaults to `false`. When `true`, any values not defined will not be displayed. |
| `Clearable` | `bool` | `false` | Shows a button for clearing any selected values. Defaults to `false`. When `true`, the `ClearIcon` can be used to control the icon, and `OnClearButtonClick` occurs when the clear button is clicked. |
| `SelectedValues` | `IReadOnlyCollection<T?>?` | `[]` | The currently selected values. When `MultiSelection` is `false`, only one value will be returned. When this value changes, `SelectedValuesChanged` occurs. |
| `SelectedValuesChanged` | `EventCallback<IReadOnlyCollection<T?>?>` | – | Occurs when `SelectedValues` has changed. |
| `OnClearButtonClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the clear button is clicked. Only occurs when `Clearable` is `true`. This event occurs after the `Text` and `Value` have been cleared. |

## MudSelectItem<T> : MudComponentBase

A selectable option displayed within a `MudSelect{T}` component.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Value` | `T?` | – | The custom value associated with this item. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this item. Defaults to `false`. |
| `ChildContent` | `RenderFragment?` | – | The custom content within this item. |
