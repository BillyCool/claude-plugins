# Overlay components — API (generated from source)

## MudOverlay : MudComponentBase

Renders a translucent layer over content, typically used for modals, popovers, progress bars, or blocking interactions.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | `null` | Child content of the component. Defaults to `null`. |
| `Visible` | `bool` | `false` | Makes the overlay visible. Defaults to `false`. |
| `VisibleChanged` | `EventCallback<bool>` | – | Occurs when `Visible` changes. This event is triggered when the visibility of the overlay changes. |
| `AutoClose` | `bool` | `false` | Sets `Visible` to `false` when the overlay is clicked and calls `OnClosed`. Defaults to `false`. This is preferred over the previously used `OnClick` event. |
| `LockScroll` | `bool` | `true` | Prevents the `Document.body` element from scrolling. Defaults to `true`. |
| `LockScrollClass` | `string` | `"scroll-locked"` | The css class that will be added to body if lockscroll is used. Defaults to `"scroll-locked"`. |
| `Modal` | `bool` | `true` | Prevents interaction with background elements. Defaults to `true`. |
| `DarkBackground` | `bool` | `false` | Applies the theme's dark overlay color. Defaults to `false`. |
| `LightBackground` | `bool` | `false` | Applies the theme's light overlay color. Defaults to `false`. |
| `Absolute` | `bool` | `false` | Uses absolute positioning for the overlay. Defaults to `false`. |
| `ZIndex` | `int` | `5` | Sets the z-index of the overlay. Defaults to `5`. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the overlay is clicked. If you need to close the overlay automatically, you can use `AutoClose` and `OnClosed` instead. |
| `OnClosed` | `EventCallback` | – | Occurs when the overlay is closed due to `AutoClose`. |
