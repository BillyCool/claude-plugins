# SwipeArea components — API (generated from source)

## MudSwipeArea : MudComponentBase

Detects and responds to swipe gestures for navigation or actions.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this swipe area. |
| `OnSwipeMove` | `EventCallback<MultiDimensionSwipeEventArgs>` | – | Occurs when a swipe has on progress. Ignores sensitivity. |
| `OnSwipeEnd` | `EventCallback<SwipeEventArgs>` | – | Occurs when a swipe has ended. |
| `OnSwipeLeave` | `EventCallback<PointerEventArgs>` | – | Occurs when a swipe leaves the area. |
| `OnSwipeCancel` | `EventCallback<PointerEventArgs>` | – | Occurs when a swipe cancelled. |
| `Sensitivity` | `int` | `100` | The amount of pixels which must be swiped to raise the `OnSwipeEnd` event. Defaults to `100` (100 pixels). |
| `PreventDefault` | `bool` | `false` | Prevents the default behavior of the browser when swiping. Defaults to `false`. Typically `true` when swiping up or down, which will prevent the whole page from scrolling. |
