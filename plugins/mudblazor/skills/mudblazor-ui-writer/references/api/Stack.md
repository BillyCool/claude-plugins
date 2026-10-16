# Stack components — API (generated from source)

## MudStack : MudComponentBase

Manages layout of its child items along the vertical or horizontal axis with optional spacing.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Row` | `bool` | `false` | Displays items horizontally. Defaults to `false`. When `true`, items will be displayed horizontally. When `false`, items are displayed vertically. |
| `Reverse` | `bool` | `false` | Reverses the order of items. Defaults to `false`. When `true`, items will be reversed. |
| `Spacing` | `int` | `3` | The gap between items in increments of `4px`. Defaults to 3. Maximum is 20 (`80px`). |
| `Justify` | `Justify?` | `null` | Defines the distribution of child items. Defaults to `null`. |
| `AlignItems` | `AlignItems?` | `null` | Defines the vertical alignment of child items. Defaults to `null`. |
| `StretchItems` | `StretchItems?` | `null` | Defines the stretching behaviour of children along the main axis within a `MudStack` component. Defaults to `null`. |
| `Wrap` | `Wrap?` | `null` | Controls how items are wrapped. Defaults to `null`. |
| `Breakpoint` | `Breakpoint` | `Breakpoint.None` | The breakpoint at which the Stack should switch to a row or column layout. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |
| `HtmlTag` | `string` | `"div"` | The HTML tag rendered for this component. Defaults to `div`. |
