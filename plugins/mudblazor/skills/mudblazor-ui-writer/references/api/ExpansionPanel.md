# ExpansionPanel components — API (generated from source)

## MudExpansionPanel : MudComponentBase

Accordion-style collapsible panel within a `MudExpansionPanels` group that expands to reveal content or collapses to show only its header.

*This component is always inside a `MudExpansionPanels` component.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `MaxHeight` | `int?` | `null` | The maximum allowed height, in pixels. Defaults to `null`. When `null`, the CSS default is used for maximum height. |
| `HeaderClass` | `string?` | – | User class names, separated by space. |
| `TitleContent` | `RenderFragment?` | `null` | The content within the title area. Defaults to `null`. When set, overrides the `Text` property. |
| `Text` | `string?` | `null` | The text displayed in this panel, if `TitleContent` is not set. Defaults to `null`. |
| `HideIcon` | `bool` | `false` | Hides the expand icon. Defaults to `false`. |
| `Icon` | `string` | `Icons.Material.Filled.ExpandMore` | The icon for expanding this panel. Defaults to `ExpandMore`. |
| `Dense` | `bool` | `false` | Removes vertical padding from the panel. Defaults to `false`. |
| `Gutters` | `bool` | `true` | Adds left and right padding. Defaults to `true`. |
| `ExpandedChanged` | `EventCallback<bool>` | – | Occurs when `Expanded` has changed. |
| `Expanded` | `bool` | `false` | Displays the panel content. Defaults to `false`. |
| `Disabled` | `bool` | `false` | Disables user interaction and prevents `ToggleExpansionAsync`. Defaults to `false`. |
| `ChildContent` | `RenderFragment?` | – | The content within this panel. |
| `KeepContentAlive` | `bool` | `true` | When true, the content remains in the DOM even when the panel is collapsed. |

## MudExpansionPanels : MudComponentBase

A container which manages `MudExpansionPanel` components such that when one panel is expanded the others are collapsed automatically.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Square` | `bool` | `false` | Uses square corners for the panel. Defaults to `false`. |
| `MultiExpansion` | `bool` | `false` | Allows multiple panels to be expanded at the same time. Defaults to `false`. |
| `Elevation` | `int` | `1` | The size of the drop shadow. Defaults to `1`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Dense` | `bool` | `false` | Uses compact padding for all panels. Defaults to `false`. |
| `Gutters` | `bool` | `true` | Adds left and right padding to all panels. Defaults to `true`. |
| `Outlined` | `bool` | `true` | Shows borders around each panel. Defaults to `true`. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |
