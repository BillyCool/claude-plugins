# Virtualize components — API (generated from source)

## MudVirtualize<T> : ComponentBase

Renders a large list of items efficiently by creating DOM elements only for the rows currently in view. Wraps Blazor's `Virtualize{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Enabled` | `bool` | – | Set false to turn off virtualization |
| `ChildContent` | `RenderFragment<T>?` | – | Item template for the list. |
| `Placeholder` | `RenderFragment?` | – | Template for the items that have not yet been loaded in memory. |
| `NoRecordsContent` | `RenderFragment?` | – | The content shown when there are no rows to display. |
| `Items` | `ICollection<T>?` | – | Fixed item source. |
| `ItemsProvider` | `ItemsProviderDelegate<T>?` | – | Function providing items to the list. |
| `OverscanCount` | `int` | `3` | Gets or sets a value that determines how many additional items will be rendered before and after the visible region. This help to reduce the frequency of rendering during scrolling. However, higher values mean that more elements will be present in the page. |
| `ItemSize` | `float` | `50f` | Gets the size of each item in pixels. Defaults to 50px. |
| `MaxItemCount` | `int` | `100` | Gets or sets the maximum number of items that will be rendered, even if the client reports that its viewport is large enough to show more. The default value is 100. This should only be used as a safeguard against excessive memory usage or large data loads. Do not set this to a smaller number than you expect to fit on a realistic-sized window, because that will leave a blank gap below and the user may not be able to see the rest of the content. |
| `SpacerElement` | `string` | `"div"` | Gets or sets tag name of the HTML element that will be used as virtualization spacer. Default is div. |
