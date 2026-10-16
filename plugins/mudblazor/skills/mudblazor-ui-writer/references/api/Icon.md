# Icon components — API (generated from source)

## MudIcon : MudComponentBase

A picture displayed via an SVG path or font.

*You can use the `Icons` class and Icons Reference for SVG paths, or a Font Awesome CSS Class.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Icon` | `string?` | – | The SVG path or Font Awesome font icon to display. You can use the `Icons` class and Icons Reference for SVG paths, or a Font Awesome CSS Class. |
| `Title` | `string?` | `null` | The text to display for the tooltip. Defaults to `null`. Sets the `title` HTML attribute. |
| `Size` | `Size` | `Size.Medium` | The size of this icon. Defaults to `Medium`. |
| `Disabled` | `bool` | `false` | Ignores any custom color. Defaults to `false`. When `true`, a disabled color will be used instead of the `Color`. |
| `Color` | `Color` | `Color.Inherit` | The color of this icon. Defaults to `Inherit`. When `Disabled` is `true`, this value is ignored. |
| `ViewBox` | `string` | `"0 0 24 24"` | For SVG icons, the size of the SVG viewbox. Defaults to `"0 0 24 24"`. Applies when using the `Icons` class to set the icon. |
| `ChildContent` | `RenderFragment?` | – | The content within this icon. |
