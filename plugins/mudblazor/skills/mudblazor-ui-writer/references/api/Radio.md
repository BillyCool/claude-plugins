# Radio components — API (generated from source)

## MudRadio<T> : MudBooleanInput<T>

Allows the user to select a single choice from a group of options. Use radio buttons (not switches) when only one item can be selected from a list.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `UncheckedColor` | `Color?` | `null` | The color to use when in an unchecked state. Defaults to `null`. |
| `AriaLabel` | `string?` | `null` | The Aria Label to be assigned to the radio button. Defaults to `null`. Used to improve accessibility for screen readers. Adds an `aria-labelledby` to the `input` element. |
| `Dense` | `bool` | `false` | Uses compact vertical padding. Defaults to `false`. |
| `CheckedIcon` | `string` | `Icons.Material.Filled.RadioButtonChecked` | The icon displayed when in a checked state. Defaults to `RadioButtonChecked`. |
| `UncheckedIcon` | `string` | `Icons.Material.Filled.RadioButtonUnchecked` | The icon displayed when in an unchecked state. Defaults to `RadioButtonUnchecked`. |
| `IndeterminateIcon` | `string` | `Icons.Material.Filled.IndeterminateCheckBox` | The icon to display for an indeterminate state. Defaults to `IndeterminateCheckBox`. |

## MudRadioGroup<T> : MudFormComponent<T, T>

A group of `MudRadio{T}` components.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `InputClass` | `string?` | – | The CSS classes for this button group. Multiple classes must be separated by spaces. |
| `InputStyle` | `string?` | – | **[Obsolete]** The CSS styles for this button group. |
| `ChildContent` | `RenderFragment?` | – | The content within this button group. Usually a set of `MudRadio{T}` components. |
| `Name` | `string` | `Guid.NewGuid().ToString()` | The unique name for this button group. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this group. Defaults to `false`. |
| `ReadOnly` | `bool` | `false` | Prevents the selected value from being changed. Defaults to `false`. |
| `ValueChanged` | `EventCallback<T>` | – | The current value. When this value changes, the `ValueChanged` event occurs. |
