# TextField components — API (generated from source)

## MudTextField<T> : MudDebouncedInput<T>

An input for collecting text values.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `InputType` | `InputType` | `InputType.Text` | The type of input collected by this component. Defaults to `Text`. Represents a valid HTML5 input type. |
| `Clearable` | `bool` | `false` | Shows a button to clear this input's value. Defaults to `false`. |
| `ClearIcon` | `string` | `Icons.Material.Filled.Clear` | The icon to display when `Clearable` is `true`. Defaults to `Clear`. |
| `OnClearButtonClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the clear button is clicked. When clicked, the `Text` and `Value` properties are reset. |
| `Sizing` | `InputSizing` | `InputSizing.Fixed` | The mask to apply to text values. Typically set to common masks such as `PatternMask`, `MultiMask`, `RegexMask`, and `BlockMask`. When set, some properties will be ignored such as `MaxLines`, `Sizing`, and `HideSpinButtons`. |
| `MaxLines` | `int` | `0` | The maximum vertical lines to display when `Sizing` is `Auto`. Defaults to `0`. When `0`. this property is ignored. |
