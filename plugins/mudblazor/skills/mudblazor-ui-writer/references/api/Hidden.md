# Hidden components — API (generated from source)

## MudHidden : MudComponentBase

Conditionally renders its content based on the current screen-size breakpoint, showing or hiding it as the viewport changes.

*This component uses JavaScript to listen for browser window size changes. If you want a solution using only CSS, you can use the responsive display classes.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Breakpoint` | `Breakpoint` | – | The breakpoint at which component is not rendered, when `Invert` is `false`. When `Invert` is `true`, this property controls when the content is shown. |
| `Invert` | `bool` | `false` | Causes the `Breakpoint` to control when content is displayed. Defaults to `false`. |
| `Hidden` | `bool` | `true` | Hides the content within this component. Defaults to `true`. |
| `HiddenChanged` | `EventCallback<bool>` | – | Occurs when `Hidden` has changed. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |
