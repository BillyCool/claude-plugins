# Mask components — API (generated from source)

## MudMask : MudBaseInput<string>

A text input which conforms user input to a specific format while typing. Note that MudMask is recommended to be used in WASM projects only because it has known problems in BSS, especially with high network latency.

*Note that MudMask is recommended to be used in WASM projects only because it has known problems in BSS, especially with high network latency.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this input. Only displays when `InputType` is `Hidden`. |
| `InputType` | `InputType` | `InputType.Text` | The mask to apply to text values. Typically set to common masks such as `PatternMask`, `MultiMask`, `RegexMask`, and `BlockMask`. When set, some properties will be ignored such as `MaxLines`, `Sizing`, and `HideSpinButtons`. |
| `Clearable` | `bool` | `false` | Shows the clear button. |
| `OnClearButtonClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the clear button is clicked. |
| `ClearIcon` | `string` | `Icons.Material.Filled.Clear` | The icon displayed when `Clearable` is `true`. |
