# Badge components — API (generated from source)

## MudBadge : MudComponentBase

Badges show notifications, counts, or status information on navigation items and icons.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Origin` | `Origin` | `Origin.TopRight` | The location of the badge. Defaults to `TopRight`. |
| `Elevation` | `int` | `0` | The size of the drop shadow. Defaults to `0`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Visible` | `bool` | `true` | Displays this badge. Defaults to `true`. |
| `Color` | `Color` | `Color.Default` | The color of the badge. Defaults to `Default`. Theme colors are supported. |
| `Dot` | `bool` | `false` | Displays a dot instead of any content. Defaults to `false`. |
| `Overlap` | `bool` | `false` | Displays `ChildContent` over the main badge content. Defaults to `false`. |
| `Bordered` | `bool` | `false` | Displays a border around the badge. Defaults to `false`. |
| `Icon` | `string?` | – | The icon to display in the badge. |
| `Max` | `int` | `99` | The maximum number allowed in the `Content` property. Defaults to `99`. |
| `Content` | `object?` | – | The `string` or `int` value to display inside the badge. Supported types are `string` and `int`. |
| `BadgeClass` | `string?` | `null` | The CSS classes applied to the badge. Defaults to `null`. You can use spaces to separate multiple classes. |
| `BadgeAriaLabel` | `string?` | `null` | The `aria-label` for the badge. Defaults to `null`. |
| `ChildContent` | `RenderFragment?` | – | The content within this badge. |
