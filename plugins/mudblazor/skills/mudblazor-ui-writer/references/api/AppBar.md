# AppBar components — API (generated from source)

## MudAppBar : MudComponentBase

Displays actions, branding, navigation and screen titles. Keep the app bar persistent while browsing different pages to ease navigation and access to actions for users.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Bottom` | `bool` | – | Places the appbar at the bottom of the screen instead of the top. |
| `Contextual` | `bool` | `false` | Allows the app bar to be overridden with page specific actions Defaults to `false`. When `true`, can be overridden by `MudContextualActionBar` |
| `Elevation` | `int` | `4` | The size of the drop shadow. Defaults to `4`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Dense` | `bool` | `false` | Uses compact padding. Defaults to `false`. |
| `Gutters` | `bool` | `true` | Adds left and right padding to this appbar. Defaults to `true`. |
| `Color` | `Color` | `Color.Default` | The color of this appbar. Defaults to `Default`. Theme colors are supported. |
| `Fixed` | `bool` | `true` | Fixes this appbar in place as the page is scrolled. Defaults to `true`. When `false`, the appbar will scroll with other page content. |
| `WrapContent` | `bool` | `false` | Allows appbar content to wrap. Defaults to `false`. |
| `ToolBarClass` | `string?` | `null` | The CSS classes applied to the nested toolbar. Defaults to `null`. You can use spaces to separate multiple classes. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |

## MudContextualActionBar : MudAppBar

A contextual app bar.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Visible` | `bool` | `false` | Determines if the action bar is visible. Defaults to `false`. |
