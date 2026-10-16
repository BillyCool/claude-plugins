# Field components — API (generated from source)

## MudField : MudComponentBase

Displays custom content inside a form field with the same label, adornment, and border styling as a `MudTextField{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this field. |
| `Margin` | `Margin` | `Margin.None` | The vertical spacing for this field. Defaults to `None`. |
| `Typo` | `Typo` | `Typo.subtitle1` | Typography for the field text. |
| `Error` | `bool` | `false` | Displays the error in `ErrorText`. Defaults to `false`. |
| `ErrorText` | `string?` | – | A description of this field's error that is displayed under the field when `Error` is `true`. |
| `HelperText` | `string?` | – | The text displayed below the text field. Typically used to help the user understand what kind of input is allowed. |
| `FullWidth` | `bool` | `false` | Sets the width of the field to the width of the container. Defaults to `false`. |
| `Label` | `string?` | – | The label for this input. If no value is specified, the label will be displayed in the input. Otherwise, it will be scaled down to the top of the input. |
| `Variant` | `Variant` | `Variant.Text` | The display variant of the field. Defaults to `Text`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this field. Defaults to `false`. |
| `AdornmentIcon` | `string?` | `null` | The icon displayed for the adornment. Defaults to `null`. This icon will be displayed when `Adornment` is `Start` or `End`, and no value for `AdornmentText` is set. |
| `AdornmentText` | `string?` | `null` | The text displayed for the adornment. Defaults to `null`. This text will be displayed when `Adornment` is `Start` or `End`. The `AdornmentIcon` property will be ignored if this property is set. |
| `Adornment` | `Adornment` | `Adornment.None` | The location of the adornment icon or text. Defaults to `None`. When set to `Start` or `End`, the `AdornmentText` will be displayed, or `AdornmentIcon` if no adornment text is specified. |
| `AdornmentColor` | `Color` | `Color.Default` | The color of `AdornmentText` or `AdornmentIcon`. Defaults to `Default`. |
| `AdornmentAriaLabel` | `string?` | `null` | The `aria-label` for the adornment. Defaults to `null`. |
| `IconSize` | `Size` | `Size.Medium` | The size of the icon. Defaults to `Medium`. |
| `OnAdornmentClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the adornment icon (but not the text) has been clicked. |
| `InnerPadding` | `bool` | `true` | Displays padding for the content within this field. Defaults to `true`. |
| `Underline` | `bool` | `true` | Displays an underline for this field. Defaults to `true`. |
| `ShrinkLabel` | `bool` | `false` | Controls whether the label is displayed inside the field or shrinks above it when the field does not have focus. Defaults to `false`. When `false`, the label behaves like a placeholder and shrinks only if there is content or an adornment at the start. When `true`, the label does not shrink and remains as a placeholder regardless of content, which may result in overlap. |
