# Drawer components — API (generated from source)

## MudDrawer : MudComponentBase

Navigation drawers, or sidebars, dock to the side of the page to hold navigation links, menus, or other content.

*Supports temporary, persistent, mini, and responsive variants that adapt to the screen size.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Fixed` | `bool` | `true` | Shows the drawer in the same position even if the page is scrolled. Defaults to `true`. |
| `Elevation` | `int` | `1` | The size of the drop shadow. Defaults to `1`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Anchor` | `Anchor` | `Anchor.Start` | The edge of the container that the drawer will appear. Defaults to `Start`. |
| `Color` | `Color` | `Color.Default` | The color of the drawer. Defaults to `Default`. |
| `Variant` | `DrawerVariant` | `DrawerVariant.Responsive` | The display variant of this drawer. Defaults to `Responsive`. |
| `ChildContent` | `RenderFragment?` | – | The content within this drawer. |
| `Overlay` | `bool` | `true` | For responsive and temporary drawers, darkens the screen with an overlay when displaying this drawer. Defaults to `true`. Applies when `Variant` is `Responsive` or `Temporary`. Mini drawers also display the overlay while they behave like `Temporary` below their `Breakpoint`. |
| `OverlayAutoClose` | `bool` | `true` | Automatically closes the drawer when clicking on the overlay. If the `Variant` is set to `Temporary`, an overlay will be displayed. When this property is `true`, clicking on the overlay will close it automatically. When this property is `false`, the overlay will not close automatically. Defaults to `true`. |
| `OpenMiniOnHover` | `bool` | `false` | For mini drawers, opens this drawer when the pointer hovers over it. Defaults to `false`. Applies when `Variant` is set to `Mini`. |
| `Breakpoint` | `Breakpoint` | `Breakpoint.Md` | The browser width at which responsive drawers are hidden. Defaults to `Md`. Supported breakpoints are: `Xs` `Sm` `Md` `Lg` `Xl` `Xxl` Other breakpoint combinations are aliased as follows: `SmAndDown`: Aliases to `Sm` `MdAndDown`: Aliases to `Md` `LgAndDown`: Aliases to `Lg` `XlAndDown`: Aliases to `Xl` `SmAndUp`: Aliases to `Sm` `MdAndUp`: Aliases to `Md` `LgAndUp`: Aliases to `Lg` `XlAndUp`: Aliases to `Xl` Setting the value to `None` will always close the drawer, while `Always` will always keep it open. Applies when `Variant` is set to `Responsive` or `Mini`. Mini drawers behave like `Temporary` below this breakpoint. |
| `Open` | `bool` | `false` | Displays this drawer. Defaults to `false`. Raises the `OpenChanged` event upon change. When bound via `@bind-Open`, this property is updated when this drawer closes itself. |
| `OpenChanged` | `EventCallback<bool>` | – | Occurs when the `Open` value has changed. |
| `Width` | `string?` | `null` | For non-fixed or temporary drawers, the width of this drawer. Defaults to `null`. Values such as `300px` and `30%` are supported. Applies to non-fixed or `Temporary` drawers anchored to the left or right. |
| `MiniWidth` | `string?` | `null` | For mini drawers, the width of this drawer. Defaults to `null`. Values such as `300px` and `30%` are supported. Applies to `Mini` drawers achored to the left or right. |
| `Height` | `string?` | `null` | The height of this drawer. Defaults to `null`. Values such as `300px` and `30%` are supported. Applies to drawers achored to the top or bottom. |
| `ClipMode` | `DrawerClipMode` | – | The position of this drawer when opened, relative to a `MudAppBar` when inside a `MudLayout`. |

## MudDrawerContainer : MudComponentBase

A container for a `MudDrawer` component.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The custom content inside this drawer. |

## MudDrawerHeader

Represents content at the top of a `MudDrawer`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Dense` | `bool` | `false` | Uses compact padding. Defaults to `false`. |
| `LinkToIndex` | `bool` | `false` | Navigates to the index page on click. Defaults to `false`. When `true`, the component will link to index page upon click. |
| `ChildContent` | `RenderFragment?` | – | Custom content within this component. |
