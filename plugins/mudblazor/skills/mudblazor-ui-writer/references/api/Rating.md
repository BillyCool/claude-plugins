# Rating components — API (generated from source)

## MudRating : MudComponentBase

Ratings provide insight regarding other's opinions and experiences with a product. Collecting user feedback via ratings is a simple analytic that can provide a lot of feedback to your product or application.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `RatingItemsClass` | `string?` | `null` | The CSS classes to apply to each `MudRatingItem`. Defaults to `null`. Multiple classes must be separated by spaces. |
| `RatingItemsStyle` | `string?` | `null` | **[Obsolete]** The CSS styles to apply to each `MudRatingItem`. Defaults to `null`. |
| `Name` | `string` | `Guid.NewGuid().ToString()` | The name of this input. Defaults to a new `Guid`. |
| `MaxValue` | `int` | `5` | The number of `MudRatingItem` items to display. Defaults to `5`. |
| `FullIcon` | `string` | `Icons.Material.Filled.Star` | The icon displayed for selected items. Defaults to `Star`. |
| `EmptyIcon` | `string` | `Icons.Material.Filled.StarBorder` | The icon displayed for unselected items. Defaults to `StarBorder`. |
| `FullIconColor` | `Color?` | `null` | The color of the `FullIcon` for selected items. Defaults to `null`. |
| `EmptyIconColor` | `Color?` | `null` | The color of the `EmptyIcon` for unselected items. Defaults to `null`. |
| `Color` | `Color` | `Color.Default` | The color of each item. Defaults to `Default`. |
| `Size` | `Size` | `Size.Medium` | The size of the `FullIcon` and `EmptyIcon` icons. Defaults to `Medium`. |
| `Ripple` | `bool` | `false` | Shows a ripple effect when an item is clicked. Defaults to `false`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this rating and shows a disabled color. Defaults to `false`. |
| `ReadOnly` | `bool` | `false` | Prevents this rating from being changed. Defaults to `false`. |
| `SelectedValueChanged` | `EventCallback<int>` | – | Occurs when `SelectedValue` has changed. |
| `SelectedValue` | `int` | `0` | The currently selected value. Defaults to `0`. Must be equal or less than `MaxValue`. |
| `HoveredValueChanged` | `EventCallback<int?>` | `null` | Occurs when `HoveredValue` has changed. Defaults to `null`. |

## MudRatingItem : MudComponentBase

A clickable item as part of a `MudRating`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ItemValue` | `int` | `the index of this item in the parent `MudRating` | The value for this item. Defaults to the index of this item in the parent `MudRating`. (e.g. The 3rd item has a value of `3`.) |
| `Size` | `Size` | `Size.Medium` | The size of this item. Defaults to `Medium`. When used within a `MudRating`, the value of `Size` is applied instead. |
| `Color` | `Color` | `Color.Default` | The color of this item. Defaults to `Default`. When used within a `MudRating`, the value of `Color` is applied instead. |
| `Ripple` | `bool` | `false` | Show a ripple effect when the user clicks the button. Defaults to `false`. When used within a `MudRating`, the value of `Ripple` is applied instead. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this item, and uses a disabled style. Defaults to `false`. |
| `ReadOnly` | `bool` | `false` | Prevents this item from being changed. Defaults to `false`. |
| `ItemClicked` | `EventCallback<int>` | – | Occurs when this item is clicked. When clicked, the `SelectedValue` is changed. |
| `ItemHovered` | `EventCallback<int?>` | – | Occurs when the user hovers over this item. When hovered, the `HoveredValue` is changed. |
