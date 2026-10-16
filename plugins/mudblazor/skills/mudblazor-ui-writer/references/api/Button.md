# Button components — API (generated from source)

## MudButton : MudBaseButton

Buttons trigger actions, submit forms, or navigate to a link.

*Creates a button element, or anchor if `Href` is set. You can directly add attributes like `title` or `aria-label`.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `StartIcon` | `string?` | `null` | The icon displayed before the text. Defaults to `null`. Use `EndIcon` to display an icon after the text. |
| `EndIcon` | `string?` | `null` | The icon displayed after the text. Defaults to `null`. Use `StartIcon` to display an icon before the text. |
| `IconColor` | `Color` | `Color.Inherit` | The color of icons. Defaults to `Inherit`. |
| `IconSize` | `Size?` | `null` | The size of icons. Defaults to `null`. When `null`, the value of `Size` is used. |
| `IconClass` | `string?` | `null` | The CSS classes applied to icons. Defaults to `null`. You can use spaces to separate multiple classes. |
| `Color` | `Color` | `Color.Default` | The color of the button. Defaults to `Default`. |
| `Size` | `Size` | `Size.Medium` | The size of the button. Defaults to `Medium`. Use the `IconSize` property to set the size of icons. |
| `Variant` | `Variant` | `Variant.Text` | The display variation to use. Defaults to `Text`. |
| `FullWidth` | `bool` | `false` | Expands the button to 100% of the container width. Defaults to `false`. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |

## MudFab : MudBaseButton

Floating action buttons (FABs) trigger the primary action on a page and float above content in a circular or extended shape.

*Creates a button element, or anchor if `Href` is set. You can directly add attributes like `title` or `aria-label`.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Variant` | `Variant` | `Variant.Filled` | The display variation to use. Defaults to `Filled`. |
| `Color` | `Color` | `Color.Default` | The color of the button. Defaults to `Default`. Theme colors are supported. |
| `Size` | `Size` | `Size.Large` | The size of the button. Defaults to `Large`. |
| `StartIcon` | `string?` | `null` | The icon shown before any text. Defaults to `null`. Use the `EndIcon` property to show an icon after text. |
| `EndIcon` | `string?` | `null` | The icon shown after any text. Defaults to `null`. Use the `StartIcon` property to show an icon before text. |
| `IconColor` | `Color` | `Color.Inherit` | The color of any icons. Defaults to `Inherit`. Controls the color of `StartIcon` and `EndIcon` icons. |
| `IconSize` | `Size` | `Size.Medium` | The size of the icon. Defaults to `Medium`. |
| `Label` | `string?` | `null` | The text displayed in the button. Defaults to `null`. |

## MudFabMenu : MudFab

A menu appearing from a `MudFab` that displays a list of items.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ButtonClass` | `string?` | – | The CSS classes applied to the menu button. Multiple classes must be separated by spaces. |
| `ButtonStyle` | `string?` | – | The CSS style applied to the menu button. |
| `MenuClass` | `string?` | – | The CSS classes applied to the item list. Multiple classes must be separated by spaces. |
| `MenuStyle` | `string?` | – | The CSS style applied to the item list. |
| `ChildContent` | `RenderFragment?` | – | The `MudFabMenuItem` components within this menu. Note that you can add any component you like as long as it has the `mud-fab-menu-item` class. |
| `Open` | `bool` | – | Whether this menu is open and the menu items are visible. When this property changes, `OpenChanged` occurs. |
| `OpenChanged` | `EventCallback<bool>` | – | Occurs when `Open` has changed. |
| `Fixed` | `bool` | `false` | Sets the menu to a fixed position. Use `Anchor` to specify the position. Defaults to `false`. |
| `Direction` | `Direction` | `Direction.Top` | The direction in which the menu should open. Defaults to `Top`. |
| `Anchor` | `Origin` | `Origin.BottomRight` | The anchor position of the menu when `Fixed` is `true`. Defaults to `BottomRight`. |
| `UseCloseIcon` | `bool` | `true` | Replaces the set icon with a close icon when the menu is open. Defaults to `true`. |
| `DampenItemsBackgroundColor` | `bool` | `true` | Dampens the background color of the menu items when set to true to increase the contrast between the menu FAB and the menu items to archive a similar effect as described in the <a href="https://m3.material.io/components/fab-menu/overview">Material Design guidelines</a>. Defaults to `true`. |
| `AlignItems` | `AlignItems` | `AlignItems.Center` | The alignment of the menu items in respect to the menu button. Defaults to `AlignItems.Center`. |
| `OpenOnMouseHover` | `bool` | `true` | Opens the menu on mouse hover. Defaults to `true`. |
| `CloseOnMenuItemClicked` | `bool` | `true` | Closes the menu when a menu item is clicked. Defaults to `true`. |

## MudFabMenuItem : MudFab

A floating action button shown as one of the selectable options within a `MudFabMenu`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Size` | `Size` | `Size.Medium` | The size of the menu item. Defaults to `Medium`. |

## MudIconButton : MudBaseButton

A clickable icon for actions and commands.

*Creates a button element, or anchor if `Href` is set. You can directly add attributes like `title` or `aria-label`.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Icon` | `string?` | `null` | The icon to display. Defaults to `null`. |
| `Color` | `Color` | `Color.Default` | The color of the button. Defaults to `Default`. |
| `Size` | `Size` | `Size.Medium` | The size of the button. Defaults to `Medium`. |
| `Edge` | `Edge` | `False` | The amount of negative margin applied. Defaults to `False`. Other values are `Start` and `End` |
| `Variant` | `Variant` | `Variant.Text` | The display variation to use. Defaults to `Text`. |
| `ChildContent` | `RenderFragment?` | `null` | The custom content within this button. Defaults to `null`. Only displays if `Icon` is not set. |

## MudToggleIconButton : MudComponentBase

An icon button that toggles between two distinct states, useful for on/off or favorite/unfavorite scenarios.

*Creates a button element, or anchor if `Href` is set. You can directly add attributes like `title` or `aria-label`.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Toggled` | `bool` | – | Whether the icon is in the toggled state. |
| `ToggledChanged` | `EventCallback<bool>` | – | Occurs when `Toggled` is changed. |
| `Icon` | `string?` | – | The icon to use. |
| `ToggledIcon` | `string?` | – | An alternative icon to use in the toggled state. |
| `Color` | `Color` | `Color.Default` | The color of the button. Defaults to `Default`. |
| `ToggledColor` | `Color?` | – | An alternative color to use in the toggled state. |
| `Size` | `Size` | `Size.Medium` | The size of the button. Defaults to `Medium`. |
| `ToggledSize` | `Size?` | – | An alternative size to use in the toggled state. |
| `Variant` | `Variant` | `Variant.Text` | The display variation to use. Defaults to `Text`. |
| `ToggledVariant` | `Variant?` | – | An alternative variant to use in the toggled state. |
| `Edge` | `Edge` | `False` | Applies a negative margin. Defaults to `False`. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when the user clicks the button. Defaults to `true`. |
| `DropShadow` | `bool` | `true` | Displays a shadow. Defaults to `true`. |
| `Disabled` | `bool` | `false` | Disables interaction with the button. Defaults to `false`. |
| `ClickPropagation` | `bool` | `false` | Allows the click event to bubble up to the parent component. Defaults to `false`. |
