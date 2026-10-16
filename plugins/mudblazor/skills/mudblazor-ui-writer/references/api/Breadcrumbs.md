# Breadcrumbs components — API (generated from source)

## BreadcrumbLink

The clickable link rendered for each `BreadcrumbItem` in a `MudBreadcrumbs` trail.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Item` | `BreadcrumbItem?` | – | The item to display. |

## BreadcrumbSeparator

The divider rendered between items in a `MudBreadcrumbs` trail, showing the separator character or a custom template.

_No own parameters._

## MudBreadcrumbs : MudComponentBase

Breadcrumbs show a navigation trail of links marking the user's current location within a page hierarchy.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Items` | `IReadOnlyList<BreadcrumbItem>?` | – | The list of items to display. |
| `Separator` | `string` | `"/"` | The separator shown between items. Defaults to `/`. Will not be shown if `SeparatorTemplate` is set. |
| `SeparatorTemplate` | `RenderFragment?` | – | The content shown between items. |
| `ItemTemplate` | `RenderFragment<BreadcrumbItem>?` | – | The custom template used to display items. |
| `MaxItems` | `byte?` | `null` | The maximum number of items to display. Defaults to `null`. If `Collapsed` is `true` and the number of items exceeds this value, the breadcrumbs will automatically collapse. |
| `ExpanderIcon` | `string` | `Icons.Material.Filled.SettingsEthernet` | The icon to display when items are collapsed. Defaults to `SettingsEthernet`. Displays when `Collapsed` and the number of items exceeds `MaxItems`. |
