# Progress components — API (generated from source)

## MudProgressCircular : MudComponentBase

Informs users about the status of ongoing processes, such as loading an app, submitting a form, or saving updates. Shows either the length of a process or unspecified wait time.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Color` | `Color` | `Color.Default` | The color of this component. Defaults to `Default`. |
| `Size` | `Size` | `Size.Medium` | The size of this component. Defaults to `Medium`. |
| `Indeterminate` | `bool` | `false` | Displays a constant animation without any value. Defaults to `false`. When `true`, the `Value` will be ignored. |
| `Rounded` | `bool` | `false` | Displays a rounded border. Defaults to `false`. When `true`, the CSS `stroke-linecap` is set to `round`. |
| `Min` | `double` | `0.0` | The lowest possible value. Defaults to `0.0`. Usually a percentage. Should be lower than `Max`. |
| `Max` | `double` | `100.0` | The highest possible value. Defaults to `100.0`. Usually a percentage. Should be higher than `Min`. |
| `Value` | `double` | `0` | The current progress amount. Defaults to `0`. Only applies when `Indeterminate` is `False`. Should be between `Min` and `Max`. |
| `StrokeWidth` | `int` | `3` | The thickness of the circle. Defaults to `3`. |
| `ChildContent` | `RenderFragment?` | – | RenderFragment for rendering custom content |

## MudProgressLinear : MudComponentBase

A line-shaped indicator of progress for an ongoing operation.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Color` | `Color` | `Color.Default` | The color of this component. Defaults to `Default`. |
| `Size` | `Size` | `Size.Small` | The size of this component. Defaults to `Medium`. |
| `Indeterminate` | `bool` | `false` | Displays a constant animation without any value. Defaults to `false`. When `true`, the `Value` will be ignored. |
| `Buffer` | `bool` | `false` | Displays an additional value ahead of `Value`. Defaults to `false`. When `true`, the value of `BufferValue` is displayed. |
| `Rounded` | `bool` | `false` | Displays a rounded border. Defaults to `false`. When `true`, the CSS `border-radius` is set to the theme's default value. |
| `Striped` | `bool` | `false` | Displays animated stripes for the value portion of this progress bar. Default to `false`. |
| `Vertical` | `bool` | `false` | Displays this progress bar vertically. Defaults to `false`. |
| `ChildContent` | `RenderFragment?` | – | The content within this progress bar. |
| `Min` | `double` | `0.0` | The lowest possible value. Defaults to `0.0`. Usually a percentage. Should be lower than `Max`. |
| `Max` | `double` | `100.0` | The highest possible value. Defaults to `100.0`. Usually a percentage. Should be higher than `Min`. |
| `Value` | `double` | `0` | The current progress amount. Defaults to `0`. Only applies when `Indeterminate` is `false`. Should be between `Min` and `Max`. |
| `BufferValue` | `double` | `0` | The amount to display ahead of the value. Defaults to `0`. Only shows when `Buffer` is `true` and `Indeterminate` is `false`. Typically a value greater than `Value`. |
| `ShowBackground` | `bool` | `true` | Shows a background for the portion of the progress bar that has not yet been filled. Defaults to `true`. |
