# InputControl components — API (generated from source)

## MudInputControl : MudComponentBase

Wraps a form input with its label, helper text, and validation message.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this component. |
| `InputContent` | `RenderFragment?` | – | The input component within this component. |
| `Margin` | `Margin` | `Margin.None` | The spacing above and below this component. Defaults to `None`. |
| `Required` | `bool` | `false` | Displays an asterisk to indicate an input is required. Defaults to `false`. |
| `Error` | `bool` | `false` | Displays the `Label` in an error state. Defaults to `false`. When `true`, the error in `ErrorText` will be displayed. |
| `ErrorText` | `string?` | – | The description of the error to display when `Error` is `true`. |
| `ErrorId` | `string?` | – | The ID that will be used by aria-describedby if `ErrorText` is set. When set, the `aria-describedby` attribute is set to the ID. |
| `HelperText` | `string?` | `null` | The text which describes which kind of input is expected. Defaults to `null`. This text is be displayed below the text field. |
| `HelperId` | `string?` | – | The ID that will be used by aria-describedby if `HelperText` is set. |
| `HelperTextOnFocus` | `bool` | `false` | Displays the `HelperText` only when this input has focus. Defaults to `false`. |
| `CounterText` | `string?` | – | The current and maximum number of characters, displayed below the text field. Used to help users know when they are at a maximum character limit. |
| `FullWidth` | `bool` | `false` | Expands this input to the width of its container. Defaults to `false`. |
| `Label` | `string?` | – | The label for this input. When this input has no value, the label is displayed inside the text box. Otherwise, the label is scaled down to the top of the input. |
| `Variant` | `Variant` | `Variant.Text` | The display variant for this input. Defaults to `Text`. Other values include `Filled` and `Outlined`. |
| `Disabled` | `bool` | `false` | Prevents the user from changing this input's value. Defaults to `false`. |
| `ForId` | `string?` | `string.Empty` | The ID of the input component related to the label specified in `Label`. |
