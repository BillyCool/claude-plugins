# Popover components — API (generated from source)

## MudPopover : MudPopoverBase

Displays content as a window over other content.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `MaxHeight` | `int?` | `null` | Sets the maximum height, in pixels, of this popover. |
| `Paper` | `bool` | `true` | Displays content within a `MudPaper`. Defaults to `true`. |
| `DropShadow` | `bool` | `true` | Shows a drop shadow to help this popover stand out. Defaults to `true`. |
| `Elevation` | `int` | `8` | The amount of drop shadow to apply. Defaults to 8. |
| `Square` | `bool` | `false` | Displays square borders around this popover. Defaults to `false`. When `true`, the CSS `border-radius` is set to `0`. |
| `Fixed` | `bool` | `False` | Displays this popover in a fixed position, even through scrolling. Defaults to `False`. |
| `Duration` | `double?` | `Duration` | The length of time that the opening transition takes to complete. Defaults to `Duration`. |
| `Delay` | `double?` | `Delay` | The amount of time, in milliseconds, from opening the popover to beginning the transition. Defaults to `Delay`. |
| `AnchorOrigin` | `Origin` | `Origin.TopLeft` | The location this popover will appear relative to its parent container. Defaults to `TopLeft`. Use `TransformOrigin` to control the direction of the popover from this point. |
| `TransformOrigin` | `Origin` | `Origin.TopLeft` | The direction this popover will appear relative to the `Origin`. Defaults to `TopLeft`. |
| `OverflowBehavior` | `OverflowBehavior?` | `OverflowBehavior` | The behavior applied when there is not enough space for this popover to be visible. Defaults to `OverflowBehavior`. |
| `RelativeWidth` | `DropdownWidth` | `DropdownWidth.Ignore` | Determines the width of this popover in relation the parent container. Defaults to `Ignore`. When `Relative`, restricts the max-width of the component to the width of the parent container When `Adaptive`, restricts the min-width of the component to the width of the parent container |

## MudPopoverBase : MudComponentBase

Base class for popover components such as `MudPopover`, handling creation and lifecycle through the `IPopoverService`.

*This class provides a base implementation for a Popover component. It implements the `IPopover` interface and utilizes the `IPopoverService` to handle the creation, updating, and destruction of the popover.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Open` | `bool` | – |  |
| `ChildContent` | `RenderFragment?` | – |  |

## MudPopoverProvider : IDisposable

A required component which manages all MudBlazor popovers.

*This component is required for MudBlazor components to display popovers properly. It is typically added to your main layout page.*

_No own parameters — see base class `IDisposable`._
