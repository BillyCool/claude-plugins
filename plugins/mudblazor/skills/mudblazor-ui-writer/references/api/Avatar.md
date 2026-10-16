# Avatar components — API (generated from source)

## MudAvatar : MudComponentBase

Represents a component which displays circular user profile pictures, icons or text.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Elevation` | `int` | `0` | The size of the drop shadow. Defaults to `0`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Square` | `bool` | `false` | Disables rounded corners. Defaults to `false`. |
| `Rounded` | `bool` | `false` | Uses rounded corners instead of a circle. Defaults to `false`. When `true`, the `border-radius` style is set to the theme's default value. |
| `Color` | `Color` | `Color.Default` | The color of the avatar. Defaults to `Default`. Theme colors are supported. |
| `Size` | `Size` | `Size.Medium` | The size of the avatar. Defaults to `Medium`. |
| `Variant` | `Variant` | `Variant.Filled` | The display variant to use. Defaults to `Filled`. The variant changes the appearance of the avatar, such as `Text`, `Outlined`, or `Filled`. |
| `ChildContent` | `RenderFragment?` | – | The content within the avatar. This property allows for custom content to displayed inside of the avatar, but is not required. |

## MudAvatarGroup : MudComponentBase

Represents a grouping of multiple `MudAvatar` components.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Spacing` | `int` | `3` | The amount of space between avatars, between `0` and `16`. Defaults to `3`. |
| `Outlined` | `bool` | `true` | Displays an outline for the group. Defaults to `true`. This property is useful to differentiate avatars which are the same color or use images. |
| `OutlineColor` | `Color` | `Color.Surface` | The color of the outline when `Outlined` is `true`. |
| `MaxElevation` | `int` | `0` | The size of the drop shadow when the number of avatars exceeds `Max`. Defaults to `0`. |
| `MaxSquare` | `bool` | `false` | Disables rounded corners when the number of avatars exceeds `Max`. Defaults to `false`. When `true`, the `border-radius` CSS style is set to `0`. |
| `MaxRounded` | `bool` | `false` | Shows rounded corners when the number of avatars exceeds `Max`. Defaults to `false`. When `true`, the `border-radius` style is set to the theme's default value. |
| `MaxColor` | `Color` | `Color.Default` | The color of the avatar when the number of avatars exceeds `Max`. Defaults to `Default`. Theme colors are supported. |
| `MaxSize` | `Size` | `Size.Medium` | The size of the avatar when the number of avatars exceeds `Max`. Defaults to `Medium`. |
| `MaxVariant` | `Variant` | `Variant.Filled` | The display variant to use when the number of avatars exceeds `Max`. Defaults to `Filled`. The variant changes the appearance of the avatar, such as `Text`, `Outlined`, or `Filled`. |
| `Max` | `int` | `int.MaxValue` | The maximum allowed avatars to display. Avatars above this limit are hidden, and a "+#" is shown for the number of avatars in excess. Defaults to `MaxValue`. |
| `MaxAvatarClass` | `string?` | `null` | The CSS class applied when the number of avatars exceeds `Max`. Defaults to `null`. |
| `MaxAvatarsTemplate` | `RenderFragment<int>?` | – | The template used to render avatars when the number of avatars exceeds `Max`. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |
