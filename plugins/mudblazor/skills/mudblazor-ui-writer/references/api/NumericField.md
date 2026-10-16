# NumericField components — API (generated from source)

## MudNumericField<T> : MudDebouncedInput<T>

A field for numeric values from users.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Clearable` | `bool` | `false` | Shows a button to clear the value. |
| `ClearIcon` | `string` | `Icons.Material.Filled.Clear` | The icon of the clear button when `Clearable` is `true`. Defaults to `Clear`. |
| `HideSpinButtons` | `bool` | `the minimum value of the numeric type, such as `MinValue` | The minimum allowed value. Defaults to the minimum value of the numeric type, such as `MinValue`. |
| `InputMode` | `InputMode` | `InputMode.numeric` | The type of value collected by this field. Defaults to `numeric`. |
| `Pattern` | `string?` | `null` | The regular expression used to constrain values. Defaults to `null`, which will show a numerical keyboard on Safari. Must be a valid JavaScript regular expression. To allow only numbers (with no signs or commas), you can use `[0-9.]`. |
