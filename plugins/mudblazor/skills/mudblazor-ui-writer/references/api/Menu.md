# Menu components — API (generated from source)

## MudMenu : MudComponentBase

Displays a list of options that users can select from. Make menus easy to open, close, and select. Menus can open from a variety of components.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Label` | `string?` | – | The text shown for this menu. |
| `AriaLabel` | `string?` | `null` | The `aria-label` for the menu button when `ActivatorContent` is not set. Defaults to `null`. |
| `ListClass` | `string?` | – | The CSS classes applied to items in this menu. Multiple classes must be separated by spaces. |
| `PopoverClass` | `string?` | – | The CSS classes applied to the popover for this menu. Multiple classes must be separated by spaces. |
| `Icon` | `string?` | – | The icon displayed for this menu. When set, this menu will display a `MudIconButton`. |
| `IconColor` | `Color` | `Color.Inherit` | The color of the `StartIcon` and `EndIcon` icons. Defaults to `Inherit`. |
| `StartIcon` | `string?` | `null` | The icon displayed before the text when `Icon` is not set. Also used for nested `MudMenu`. Defaults to `null`. |
| `EndIcon` | `string?` | `null` | The icon displayed after the text when `Icon` is not set. Defaults to `null`. |
| `Color` | `Color` | `Color.Default` | The color of this menu's button when `Icon` is not set, or the color of the `MudIconButton` when `Icon` is set. Defaults to `Default`. |
| `Size` | `Size` | `Size.Medium` | The size of this menu's button when `Icon` is not set, or the size of the `MudIconButton` when `Icon` is set. Defaults to `Medium`. |
| `Variant` | `Variant` | `Variant.Text` | The display variant to use. Defaults to `Text`. |
| `Dense` | `bool` | `false` | Applies compact vertical padding to all menu items. Defaults to `false`. |
| `FullWidth` | `bool` | `false` | Expands this menu to the same width as its parent. Defaults to `false`. |
| `MaxHeight` | `int?` | `null` | Sets the maximum allowed height for this menu, when open. Defaults to `null`. |
| `PositionAtCursor` | `bool` | `false` | Opens this menu at the cursor's location instead of the button's location. Defaults to `false`. Typically used for larger-sized activators. |
| `ActivatorContent` | `RenderFragment<MenuContext>?` | – | Overrides the default button with custom content that receives a `MenuContext`. The context provides methods to control the menu: `OpenAsync`, `CloseAsync`, `ToggleAsync`, and `CloseAllAsync`. For hover activation, set `ActivationEvent` to `MouseOver` and allow the menu to handle pointer enter and leave events. Example usage: <code> &lt;MudMenu&gt; &lt;ActivatorContent&gt; &lt;MudButton OnClick="@context.ToggleAsync"&gt;Open Menu&lt;/MudButton&gt; &lt;/ActivatorContent&gt; &lt;ChildContent&gt; &lt;MudMenuItem&gt;Item 1&lt;/MudMenuItem&gt; &lt;/ChildContent&gt; &lt;/MudMenu&gt; </code> |
| `ActivationEvent` | `MouseEvent` | `MouseEvent.LeftClick` | The mouse event which opens the menu. Defaults to `LeftClick`. Default activators are wired automatically. When using `ActivatorContent`, click and context menu activators should call the provided `MenuContext`. Hover activation is handled by the menu's built-in pointer handlers. |
| `AnchorOrigin` | `Origin?` | `null` | The origin point for the menu's anchor. If set, overrides Nested Menus, and PositionatCursor Anchor points. Defaults to `null`. |
| `TransformOrigin` | `Origin` | `Origin.TopLeft` | Sets the direction the menu will open from the anchor. Defaults to `TopLeft`. |
| `PopoverFixed` | `bool` | `false` | Displays the dropdown popover in a fixed position, even while scrolling. Defaults to `false`. |
| `RelativeWidth` | `DropdownWidth` | `DropdownWidth.Ignore` | Determines the width of the Popover dropdown in relation the parent container. Defaults to `Ignore`. When `Relative`, restricts the max-width of the component to the width of the parent container When `Adaptive`, restricts the min-width of the component to the width of the parent container |
| `LockScroll` | `bool` | `false` | Prevents the page from scrolling while this menu is open. Defaults to `false`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this menu. Defaults to `false`. |
| `Ripple` | `bool` | `true` | Shows a ripple animation when the user clicks the activator button. Defaults to `true`. |
| `DropShadow` | `bool` | `true` | Displays a drop shadow under the activator button. Defaults to `true`. |
| `Modal` | `bool?` | `ModalOverlay` | Prevents interaction with background elements while this menu is open. Defaults to `ModalOverlay`. |
| `ChildContent` | `RenderFragment?` | – | The `MudMenuItem` components within this menu. |
| `Open` | `bool` | – | Whether this menu is open and the menu items are visible. When this property changes, `OpenChanged` occurs. |
| `OpenChanged` | `EventCallback<bool>` | – | Occurs when `Open` has changed. |

## MudMenuItem : MudComponentBase

A choice displayed as part of a list within a `MudMenu` component.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Label` | `string?` | – | The text shown on this menu item if `ChildContent` is not set. |
| `ChildContent` | `RenderFragment?` | – | The content within this menu item. |
| `Disabled` | `bool` | – | Prevents the user from interacting with this item. |
| `Href` | `string?` | `null` | The URL to navigate to when this menu item is clicked. Defaults to `null`. When clicked, the browser will navigate to this URL. Use the `Target` property to target a specific tab. |
| `Target` | `string?` | `null` | The browser tab/window opened when a click occurs and `Href` is set. Defaults to `null`. This property allows navigation to open a new tab/window or to reuse a specific tab. Possible values are `_blank`, `_self`, `_parent`, `_top`, `noopener`, or the name of an `iframe` element. |
| `ForceLoad` | `bool` | `false` | Performs a full page load during navigation. Defaults to `false`. When `true`, client-side routing is bypassed and the browser is forced to load the new page from the server. |
| `Icon` | `string?` | – | The icon displayed at the start of this menu item. The size depends on whether or not the menu is using the dense variant. |
| `IconColor` | `Color` | `Color.Inherit` | The color of the icon when `Icon` is set. Defaults to `Inherit`. |
| `AutoClose` | `bool` | `true` | Closes the menu when this item is clicked. Defaults to `true`. When `false`, the menu will remain open after this item is clicked. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this menu item is clicked. |
| `HideSubMenuArrow` | `bool` | – | Hides the submenu arrow if the item is being populated from the activator content. |
