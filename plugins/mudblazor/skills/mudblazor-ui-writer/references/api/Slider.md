# Slider components — API (generated from source)

## MudSlider<T> : MudComponentBase

Allows users to select a value within a specified range. Sliders should present the full range of available values and the value should take effect immediately.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Min` | `T` | `T.Zero` | The minimum allowed value. Defauls to `0`. Must be less than `Max`. |
| `Max` | `T` | `T.CreateTruncating(100)` | The maximum allowed value. Defaults to `100`. Must be greater than `Min`. |
| `Step` | `T` | `T.One` | How much the value changes on each move. Defaults to `1`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this slider. Defaults to `false`. |
| `ChildContent` | `RenderFragment?` | – | The option content rendered above the slider. Typically used for displaying text. When the slider is vertical, content is displayed to the left of the slider. |
| `ValueChanged` | `EventCallback<T>` | – | Occurs when `Value` has changed. |
| `NullableValueChanged` | `EventCallback<T?>` | – | Occurs when `NullableValue` has changed. |
| `Value` | `T` | `T.Zero` | The value of this slider. Defaults to `0`. When this value changes, `ValueChanged` occurs. |
| `NullableValue` | `T?` | `default` | The nullable value of this slider. When this value changes, `NullableValueChanged` occurs. |
| `Color` | `Color` | `Color.Primary` | The color of this slider. Defaults to `Primary`. `Primary`, `Secondary` and `Tertiary` colors are supported. |
| `Immediate` | `bool` | `true` | Controls when the value is updated. Defaults to `true`. When `true`, dragging the slider changes `Value` (or `NullableValue`) immediately. When `false`, `Value` (or `NullableValue`) changes when releasing the handle. |
| `Vertical` | `bool` | `false` | Displays this slider vertically. Defaults to `false`. When `true`, the slider is displayed like a horizontal slider, but rotated 90° counterclockwise. |
| `TickMarks` | `bool` | `false` | Displays tick marks along the track. Defaults to `false`. |
| `TickMarkLabels` | `string[]?` | `null` | The tick mark labels for each step. Defaults to `null`. Only applies when `TickMarks` is `true`. |
| `Size` | `Size` | `Size.Small` | The size of this slider. Defaults to `Small`. |
| `Variant` | `Variant` | `Variant.Text` | The display variant to use. Defaults to `Text`. |
| `ValueLabel` | `bool` | `false` | Displays the value over the slider thumb. Defaults to `false`. |
| `Culture` | `CultureInfo` | `CultureInfo.InvariantCulture` | The culture used to format the value label. Defaults to `InvariantCulture`. Only applied when `ValueLabel` is `true`. |
| `ValueLabelFormat` | `string?` | `null` | The format of the value label. Defaults to `null`. Only applies when `ValueLabelContent` is not set. See: Standard Numeric Format Strings. |
| `ValueLabelContent` | `RenderFragment<SliderContext<T>>?` | – | The custom content for value labels. Use the supplied context to access the current value. Only applies when `ValueLabel` is `true` and `ValueLabelFormat` is not set. |
