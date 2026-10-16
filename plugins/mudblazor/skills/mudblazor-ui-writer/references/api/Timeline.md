# Timeline components — API (generated from source)

## MudTimeline : MudBaseItemsControl<MudTimelineItem>

Displays items in chronological order.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `TimelineOrientation` | `TimelineOrientation` | `TimelineOrientation.Vertical` | The orientation of the timeline and its items. Defaults to `Vertical`. When set to `Vertical`, `TimelinePosition` can be set to `Left`, `Right`, `Alternate`, `Start`, or `End`. When set to `Horizontal`, `TimelinePosition` can be set to `Top`, `Bottom`, or `Alternate`. |
| `TimelinePosition` | `TimelinePosition` | `TimelinePosition.Alternate` | The position the timeline and how its items are displayed. Defaults to `Alternate`. Can be set to `Left`, `Right`, `Alternate`, `Start`, or `End` when `TimelineOrientation` is `Vertical`. Can be set to `Top`, `Bottom`, or `Alternate` when `TimelineOrientation` is `Horizontal`. |
| `TimelineAlign` | `TimelineAlign` | `TimelineAlign.Default` | The position of each item's dot relative to its text. Defaults to `Default`. |
| `Reverse` | `bool` | `false` | Reverses the order of items when `TimelinePosition` is `Alternate`. Defaults to `false`. |
| `Modifiers` | `bool` | `true` | Enables modifiers for items, such as adding a caret for a `MudCard`. Defaults to `true`. |

## MudTimelineItem : MudComponentBase

A chronological item displayed as part of a `MudTimeline`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Icon` | `string?` | `null` | The icon displayed inside the dot. Defaults to `null`. Ignored when `ItemDot` is set. |
| `Variant` | `Variant` | `Variant.Outlined` | The display variant for the dot. Defaults to `Outlined`. |
| `DotClass` | `string?` | `null` | The CSS classes applied to the dot. Defaults to `null`. Multiple classes must be separated by spaces. |
| `DotStyle` | `string?` | `null` | **[Obsolete]** The CSS styles applied to the dot. Defaults to `null`. Styles such as `background-color` can be applied (e.g. `background-color:red;`). |
| `Color` | `Color` | `Color.Default` | The color of the dot. Defaults to `Default`. |
| `Size` | `Size` | `Size.Small` | The size of the dot. Defaults to `Small`. |
| `Elevation` | `int` | `1` | The size of the dot's drop shadow. Defaults to `1`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `TimelineAlign` | `TimelineAlign` | `Default` | Overrides `TimelineAlign` with a custom value. Defaults to `Default`. |
| `HideDot` | `bool` | `false` | Hides the dot for this item. Defaults to `false`. |
| `ItemOpposite` | `RenderFragment?` | `null` | The custom content for the opposite side of this item. Defaults to `null`. |
| `ItemContent` | `RenderFragment?` | `null` | The custom content for this item. Defaults to `null`. Only applies if `ChildContent` is `null`. |
| `ItemDot` | `RenderFragment?` | `null` | The custom content for the dot. Defaults to `null`. |
| `ChildContent` | `RenderFragment?` | `null` | The custom content for the entire item. Defaults to `null`. When set, `ItemContent` will not be displayed. |
