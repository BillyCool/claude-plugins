# NavMenu components — API (generated from source)

## MudNavGroup : MudComponentBase

A deeper level of navigation links as part of a `MudNavMenu`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `HeaderClass` | `string?` | `null` | The CSS classes applied to this nav group title. Defaults to `null`. You can use spaces to separate multiple classes. |
| `TitleContent` | `RenderFragment?` | `null` | The content within the title area. Defaults to `null`. When set, overrides the `Title` property for display purposes only. The `Title` property is still used for the `aria-label` attribute of the underlying button for accessibility. |
| `Title` | `string?` | – | The text shown for this group. |
| `Icon` | `string?` | `null` | The icon displayed next to the `Title`. Defaults to `null`. |
| `IconColor` | `Color` | `Color.Default` | The color of the icon when `Icon` is set. Defaults to `Default`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this group. Defaults to `false`. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when the user clicks this group. Defaults to `true`. |
| `Expanded` | `bool` | `false` | Displays the items within this group. Defaults to `false`. When this value changes, `ExpandedChanged` occurs. Can be bound via `@bind-Expanded`. |
| `HideExpandIcon` | `bool` | `false` | Hides the expand/collapse icon. Defaults to `false`. |
| `MaxHeight` | `int?` | `null` | The maximum height, in pixels, of this group. Defaults to `null`. When set, it will override the CSS default. |
| `ExpandIcon` | `string` | `Icons.Material.Filled.ArrowDropDown` | The icon for expanding and collapsing this group. Defaults to `ArrowDropDown`. Only shows when `HideExpandIcon` is `false`. |
| `ChildContent` | `RenderFragment?` | – | The content within this group. Typically contains `MudNavGroup` and `MudNavLink` components. |
| `ExpandedChanged` | `EventCallback<bool>` | – | Occurs when `Expanded` has changed. |

## MudNavLink : MudComponentBase

A navigation link as part of a `MudNavMenu`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Icon` | `string?` | `null` | The icon displayed for this link. Defaults to `null`. |
| `IconColor` | `Color` | `Color.Default` | The color of the icon when `Icon` is set. Defaults to `Default`. |
| `Match` | `NavLinkMatch` | `NavLinkMatch.Prefix` | Controls when this link is highlighted. Defaults to `Prefix`. This link is compared against the current URL to determine whether it is highlighted. |
| `Target` | `string?` | `null` | The browser frame to open this link when `Href` is specified. Possible values include `_blank`, `_self`, `_parent`, `_top`, or a frame name . Defaults to `null`. |
| `Rel` | `string?` | `null`, which applies `noopener noreferrer` whenever `Target` is set` | The relationship between the current document and the linked document when `Href` is set. Defaults to `null`, which applies `noopener noreferrer` whenever `Target` is set. Setting this replaces that default. Common values can be found here: <see href="https://www.w3schools.com/tags/att_a_rel.asp" /> |
| `ActiveClass` | `string` | `"active"` | The CSS applied when this link is active. Defaults to `active`. Multiple classes must be separated by spaces. |
| `Disabled` | `bool` | – | Prevents the user from interacting with this link. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when the user clicks this link. Defaults to `true`. |
| `Href` | `string?` | – | The URL to navigate to when this link is clicked. |
| `ForceLoad` | `bool` | `false` | Performs a full page load during navigation. Defaults to `false`. When `true`, client-side routing is bypassed and the browser is forced to load the new page from the server. |
| `ChildContent` | `RenderFragment?` | – | The content within this link. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this link has been clicked. This event only occurs when the `Href` property has not been set. |

## MudNavMenu : MudComponentBase

A list of navigation links with support for groups.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `MultiExpansion` | `bool` | `true` | When `true`, multiple top-level `MudNavGroup` can be expanded at a time. Defaults to `true`. When set to `false`, expanding one group collapses the other top-level groups; nested groups are unaffected. Only applies when a group is expanded by the user; setting `Expanded` programmatically bypasses this. |
| `Color` | `Color` | `Color.Default` | The color of the active `MudNavLink`. Defaults to `Default`. |
| `Bordered` | `bool` | `false` | Shows a border on the active `MudNavLink`. Defaults to `false`. |
| `Rounded` | `bool` | `false` | Shows a rounded border for all `MudNavLink` items. Defaults to `false`. When `true`, the theme `border-radius` value will be used. Only takes affect if `Bordered` is `true`. |
| `Margin` | `Margin` | `Margin.None` | The vertical spacing between `MudNavLink` items. Defaults to `None`. |
| `Dense` | `bool` | `false` | Uses compact vertical padding to all `MudNavLink` items. Defaults to `false`. Will be overridden if `Margin` is not `None`. |
| `ChildContent` | `RenderFragment?` | – | The content within this menu. Typically contains `MudNavLink`, `MudNavGroup`, `MudText`, and `MudDivider` components. |
