# Tooltip components — API (generated from source)

## MudTooltip : MudComponentBase

Displays additional context when users hover over or focus on an element.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Color` | `Color` | `Color.Default` | The tooltip color. Defaults to `Default`. |
| `Text` | `string?` | `string.Empty` | The tooltip text. |
| `Arrow` | `bool` | `false` | Displays an arrow pointing towards the tooltip content. Defaults to `false`. |
| `Duration` | `double` | `MudGlobal.TooltipDefaults.Duration.TotalMilliseconds` | The length of time to animate the opening transition. Defaults to 251ms in `Duration`. |
| `Delay` | `double` | `MudGlobal.TooltipDefaults.Delay.TotalMilliseconds` | The amount of time, in milliseconds, to wait from opening the popover before performing the transition. Defaults to 0ms in `Delay`. |
| `Placement` | `Placement` | `Placement.Bottom` | The location of the tooltip relative to its content. Defaults to `Bottom`. |
| `ChildContent` | `RenderFragment?` | – | The content described by this tooltip. |
| `TooltipContent` | `RenderFragment?` | – | The content of the tooltip. Can contain any valid HTML. |
| `Inline` | `bool` | `true` | Displays this tooltip inline with its container. Defaults to `true`. When `false`, the content will display as a block element. |
| `RootStyle` | `string?` | `null` | Any CSS styles applied to the tooltip. Defaults to `null`. |
| `RootClass` | `string?` | `null` | Any CSS classes applied to the tooltip. Defaults to `null`. |
| `ShowOnHover` | `bool` | `true` | Shows this tooltip when hovering over its content. Defaults to `true`. |
| `ShowOnFocus` | `bool` | `true` | Shows this tooltip when its content is focused. Defaults to `true`. |
| `ShowOnClick` | `bool` | `false` | Shows this tooltip when its content is clicked. Defaults to `false`. |
| `Visible` | `bool` | `false` | Shows this tooltip. Defaults to `false`. |
| `VisibleChanged` | `EventCallback<bool>` | – | Occurs when `Visible` has changed. |
| `Disabled` | `bool` | `false` | Prevents this tooltip from being displayed. Defaults to `false`. |

## MudTooltipChildContainer : IComponent

Renders its child content only when `UpdateCount` changes, so a host's internal state changes do not rebuild that content.

*`MudTooltip` and `MudSelect{T}` increment the count when their own parent renders them.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The child content to render. |
| `UpdateCount` | `int` | – | The update count of the parent component. |
