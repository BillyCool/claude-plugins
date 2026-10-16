# SplitPanel components — API (generated from source)

## MudSplitPanel : MudComponentBase

Allows users to dynamically resize content with a draggable splitter.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ClassFirstPanel` | `string?` | `null` | The CSS classes applied to the first panel. Defaults to `null`. |
| `ClassSecondPanel` | `string?` | `null` | The CSS classes applied to the second panel. Defaults to `null`. |
| `ClassDivider` | `string?` | `null` | The CSS classes applied to the divider. Defaults to `null`. |
| `Horizontal` | `bool` | `false` | Whether the panels should be divided horizontally instead of vertically. Defaults to `false`. |
| `UseAsOverlay` | `bool` | `false` | Positions this panel absolute and above other content. Note that you have to set `position: relative` on the parent element. Defaults to `false`. |
| `Rounded` | `bool` | `false` | Whether to use rounded corners for the panels. Defaults to `false`. |
| `Elevation` | `int` | `0` | The size of the drop shadow. Defaults to `0`. A higher number creates a heavier drop shadow. Set to `0` to disable the drop shadow. |
| `FirstPanelInitialSize` | `int?` | `null` | Sets the initial height or width of the first panel in pixels. Defaults to `null`. |
| `MinPanelSize` | `int` | `50` | The height and width in pixel each panel can't be made smaller than. Defaults to `50`. |
| `PanelGap` | `int` | `4` | The height or width of the divider between the panels in pixel. Defaults to `4`. |
| `Padding` | `int` | `0` | The padding of the panels. Defaults to `0`. |
| `ResetOnDoubleClick` | `bool` | `true` | If enabled resets the panel sizes to their initial values on double-clicking the divider. Defaults to `true`. |
| `Transparent` | `bool` | `false` | Makes the panels backgrounds transparent. Defaults to `false`. |
| `FirstPanel` | `RenderFragment?` | `null` | The contents of the first i.e. left/upper panel. Defaults to `null`. |
| `SecondPanel` | `RenderFragment?` | `null` | The contents of the second i.e. right/lower panel. Defaults to `null`. |
