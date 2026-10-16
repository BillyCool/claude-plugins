# CheckBox components — API (generated from source)

## MudCheckBox<T> : MudBooleanInput<T>

A form input for boolean values or selecting multiple items in a list. Use checkboxes (instead of switches or radio buttons) if multiple options can be selected from a list.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `UncheckedColor` | `Color?` | `null` | The color of the checkbox when its `Value` is `false` or `null`. Defaults to `null`. Theme colors are supported. |
| `AriaLabel` | `string?` | `null` | The Aria Label to be assigned to the checkbox. Defaults to `null`. Used to improve accessibility for screen readers. Adds an aria-labelledby to `UserAttributes`. |
| `KeyboardEnabled` | `bool` | `true` | Allows this checkbox to be controlled via the keyboard. Defaults to `true`. The `Space` key cycles through true and false values (or true/false/null states if `TriState` is `true`). `Delete` will clear the checkbox. `Enter` (or `NumPadEnter`) will set the checkbox. `Backspace` will set an indeterminate value. |
| `Dense` | `bool` | `false` | Uses compact padding. Defaults to `false`. |
| `CheckedIcon` | `string` | `Icons.Material.Filled.CheckBox` | The icon to display for a checked state. Defaults to `CheckBox`. |
| `UncheckedIcon` | `string` | `Icons.Material.Filled.CheckBoxOutlineBlank` | The icon to display for an unchecked state. Defaults to `CheckBoxOutlineBlank`. |
| `IndeterminateIcon` | `string` | `Icons.Material.Filled.IndeterminateCheckBox` | The icon to display for an indeterminate state. Defaults to `IndeterminateCheckBox`. |
| `TriState` | `bool` | `false` | Allows the checkbox to have an indeterminate state. Defaults to `false`. When `true`, the checkbox can support an indeterminate state such as a `null` value, in addition to `true` and `false`. |
