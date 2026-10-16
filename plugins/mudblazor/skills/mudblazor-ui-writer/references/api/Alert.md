# Alert components — API (generated from source)

## MudAlert : MudComponentBase

Displays an important message which is statically embedded in the page content.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ContentAlignment` | `HorizontalAlignment` | `HorizontalAlignment.Start` | Position of the text to the start (Left in LTR and right in RTL). Defaults to `Start`. |
| `CloseIconClicked` | `EventCallback<MudAlert>` | – | Occurs when the close button has been clicked. |
| `CloseIcon` | `string` | `Icons.Material.Filled.Close` | Icon used for the close button. Defaults to `Close`. This icon is only displayed when the `ShowCloseIcon` property is `true`. |
| `ShowCloseIcon` | `bool` | – | Displays a close icon. To customize which icon is displayed for the close icon, set the `CloseIcon` property. |
| `Elevation` | `int` | `0` | Size of the drop shadow. Defaults to `0`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Square` | `bool` | `false` | Disables rounded corners. Defaults to `false`. |
| `Dense` | `bool` | `false` | Uses compact padding. Defaults to `false`. |
| `NoIcon` | `bool` | `false` | Displays the alert without an icon. Defaults to `false`. To customize the icon, use the `Icon` property. |
| `Severity` | `Severity` | `Severity.Normal` | Severity of the alert. The severity determines the color and icon used. |
| `Variant` | `Variant` | `Variant.Text` | Display variant to use. Defaults to `Text`. The variant changes the appearance of the alert, such as `Text`, `Outlined`, or `Filled`. |
| `ChildContent` | `RenderFragment?` | – | Content within the alert. This property allows for custom content to displayed inside of the alert, but is not required. |
| `Icon` | `string?` | `null` | Icon displayed for this alert. Defaults to `null`. When set, the custom icon will be displayed. Otherwise, the icon will depend on the `Severity` property. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the alert has been clicked. |
