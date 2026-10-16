# ScrollToTop components — API (generated from source)

## MudScrollToTop : IAsyncDisposable

A button to quickly return to the top of the page.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this button. |
| `Selector` | `string?` | – | The CSS selector to which the scroll event will be attached. |
| `Visible` | `bool` | `false` | Displays this button. Defaults to `false`. When `false`, this will become `true` once the user scrolls down the number of pixels in `TopOffset`. |
| `VisibleCssClass` | `string?` | – | The CSS classes applied when `Visible` becomes `true`. This is typically set to transition and animation CSS classes. Multiple classes must be separated by spaces. |
| `HiddenCssClass` | `string?` | – | The CSS classes applied when `Visible` becomes `false`. This is typically set to transition and animation CSS classes. Multiple classes must be separated by spaces. |
| `TopOffset` | `int` | `300` | The number of pixels scrolled before the scroll-to-top button becomes visible. Defaults to `300` (300 pixels). |
| `ScrollBehavior` | `ScrollBehavior` | `ScrollBehavior.Smooth` | The scroll behavior when the scroll-to-top button is clicked. Defaults to `Smooth`. |
| `OnScroll` | `EventCallback<ScrollEventArgs>` | – | Occurs when the page is scrolled. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the scroll-to-top button is clicked. |
