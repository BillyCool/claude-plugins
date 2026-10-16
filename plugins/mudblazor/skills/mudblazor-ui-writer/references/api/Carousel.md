# Carousel components — API (generated from source)

## MudCarousel<TData> : MudBaseBindableItemsControl<MudCarouselItem, TData>

Carousels cycle through a set of slides or images, transitioning automatically or when the user swipes, clicks arrows, or selects a bullet.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ShowArrows` | `bool` | `true` | Displays "Next" and "Previous" arrows. |
| `ArrowsPosition` | `Position` | `Position.Center` | The position where the arrows are displayed, if `ShowArrows` is `true`. Defaults to `Center`. |
| `ShowBullets` | `bool` | `true` | Displays a bullet for each `MudCarouselItem`. Defaults to `true`. |
| `BulletsPosition` | `Position` | `Position.Bottom` | The location of the bullets when `ShowBullets` is `true`. Defaults to `Bottom`. |
| `ArrowsColor` | `Color?` | `null` | The color of arrows when `ShowArrows` is `true`. Defaults to `null`. When `null`, `Inherit` is used. |
| `BulletsColor` | `Color?` | `null` | The color of bullets when `ShowBullets` is `true`. Defaults to `null`. When `null` the `Color` property is used. |
| `AutoCycle` | `bool` | `true` | Automatically cycles items based on `AutoCycleTime`. Defaults to `false`. When `true`, the `MudCarouselItem` items will be rotated after the delay specified in `AutoCycleTime`. |
| `AutoCycleTime` | `TimeSpan` | `TimeSpan.FromSeconds(5)` | The delay before displaying the next `MudCarouselItem` when `AutoCycle` is `true`. Defaults to `Zero`. |
| `NavigationButtonsClass` | `string?` | `null` | The custom CSS classes for the "Next" and "Previous" icons when `ShowArrows` is `true`. Defaults to `null`. Separate each CSS class with spaces. |
| `BulletsClass` | `string?` | `null` | The custom CSS classes for bullets when `ShowBullets` is `true`. Defaults to `null`. Separate each CSS class with spaces. |
| `PreviousIcon` | `string` | `Icons.Material.Filled.NavigateBefore` | The "Previous" button icon when `ShowBullets` is `true` and no `PreviousButtonTemplate` is set. Defaults to `NavigateBefore`. |
| `CheckedIcon` | `string` | `Icons.Material.Filled.RadioButtonChecked` | The icon displayed for the current `MudCarouselItem` when no `BulletTemplate` is set. |
| `UncheckedIcon` | `string` | `Icons.Material.Filled.RadioButtonUnchecked` | The icon displayed for unselected `MudCarouselItem`s when no `BulletTemplate` is set. |
| `NextIcon` | `string` | `Icons.Material.Filled.NavigateNext` | The "Next" button icon when `ShowBullets` is `true` and no `NextButtonTemplate` is set. Defaults to `NavigateNext`. |
| `NextButtonTemplate` | `RenderFragment?` | – | The custom template for the "Next" button. |
| `PreviousButtonTemplate` | `RenderFragment?` | – | The custom template for the "Previous" button. |
| `BulletTemplate` | `RenderFragment<bool>?` | – | The custom template for bullets. When set, the template will be used and the `CheckedIcon` and `UncheckedIcon` properties will be ignored. |
| `EnableSwipeGesture` | `bool` | `true` | Allows swipe gestures for touch devices. Defaults to `true`. When `true`, swipe gestures on touch devices can be used to change the current `MudCarouselItem`. |

## MudCarouselItem : MudComponentBase

A single slide within a `MudCarousel{TData}`, holding the content shown while it is the selected item.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content displayed within this component. |
| `Color` | `Color` | `Color.Default` | The color of this item. Defaults to `Default`. Theme colors are supported. |
| `Transition` | `Transition` | `Transition.Slide` | The effect used to blend from this item to a different `MudCarouselItem`. Defaults to `Slide`. |
| `CustomTransitionEnter` | `string?` | – | The custom CSS transition used to blend into this carousel item. |
| `CustomTransitionExit` | `string?` | – | The custom CSS transition used to blend away from this carousel item. |
