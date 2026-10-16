# ButtonGroup components — API (generated from source)

## MudButtonGroup : MudComponentBase

Groups related `MudButton` components together visually.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `OverrideStyles` | `bool` | `true` | Overrides individual button styles with this group's style. Defaults to `true`. When `true`, the button styles are defined by this group. |
| `ChildContent` | `RenderFragment?` | – | The custom content within this group. This property allows for custom content to displayed inside of the group, but is not required. |
| `Vertical` | `bool` | `false` | Displays buttons vertically. Defaults to `false`. When `true`, buttons will be displayed vertically, otherwise horizontally. |
| `DropShadow` | `bool` | `true` | Displays a shadow. Defaults to `true`. |
| `Color` | `Color` | `Color.Default` | The color of all buttons in this group. Defaults to `Default`. Theme colors are supported. |
| `Size` | `Size` | `Size.Medium` | The size of all buttons in the group. Defaults to `Medium`. |
| `Variant` | `Variant` | `Variant.Text` | The display variant of all buttons in the group. Defaults to `Text`. Other supported values are `Outlined` and `Filled`. |
| `FullWidth` | `bool` | – | If true, the button group will take up 100% of available width. |
