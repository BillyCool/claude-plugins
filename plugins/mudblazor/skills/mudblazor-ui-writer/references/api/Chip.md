# Chip components — API (generated from source)

## MudChip<T> : MudComponentBase

Compact elements used to enter information, select a choice, filter content, or trigger an action.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Color` | `Color?` | `null` | The color of this chip. Defaults to `null`. When `SelectedColor` is set, this color is used when the chip is unselected. |
| `SelectedColor` | `Color?` | `null` | The color of the chip when it is selected. Defaults to `null`. When set, this color is used for a selected chip, otherwise `Color` is used. |
| `Size` | `Size?` | `null` | The size of the chip. Defaults to `null`. |
| `Variant` | `Variant?` | `null` | The display variation to use. Defaults to `null`. |
| `AvatarContent` | `RenderFragment?` | – | The avatar content to display inside the chip. |
| `Label` | `bool?` | `null` | Uses the theme border radius for chip edges. Defaults to `null`. When `true`, the `DefaultBorderRadius` is used for chip edges. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this chip. Defaults to `false`. When `true`, the chip is visibly disabled and interaction is not allowed. |
| `Icon` | `string?` | `null` | The icon to display within the chip. Defaults to `null`. Use the `IconColor` to control the color of this icon. |
| `CheckedIcon` | `string?` | `null` | The icon to display when `Selected` is `true`. Defaults to `null`. |
| `IconColor` | `Color?` | `null` | The color of the `Icon`. Defaults to `null`. |
| `CloseIcon` | `string?` | – | The close icon to display when `OnClose` is set. |
| `Ripple` | `bool?` | `null` | Displays a ripple effect when this chip is clicked. Defaults to `null`. |
| `ChildContent` | `RenderFragment?` | – | The content within this chip. |
| `Href` | `string?` | `null` | The URL to navigate to when the chip is clicked. Defaults to `null`. Use `Target` to control where the URL is opened. When set, the chip renders as a link and the browser handles the click, so `OnClick` is not raised and the chip cannot be selected in a `MudChipSet{T}`. Note: The close button cannot be enabled if this is set because interactive content violates the HTML spec. |
| `Target` | `string?` | `null` | The target to open URLs if `Href` is set. Defaults to `null`. This value is typically `_blank`, `_self`, `_parent`, `_top`, or the name of an `iframe`. |
| `Rel` | `string?` | – | The relationship between the current document and the linked document when `Href` is set. This property is typically used by web crawlers to get more information about a link. Common values can be found here: <see href="https://www.w3schools.com/tags/att_a_rel.asp" /> |
| `Text` | `string?` | `null` | The text label for the chip. Defaults to `null`. This will be shown so long as `ChildContent` is not set. |
| `Value` | `T?` | – | The value applied when the chip is selected. When part of a `MudChipSet{T}`, the `SelectedValue` is set to this value when the chip is selected. Once set, the value should not change. |
| `Default` | `bool?` | `null` | Selects this chip by default when part of a `MudChipSet{T}`. Defaults to `null`. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this chip is clicked. If an `Href` is set, this callback will not be triggered and the browser will handle the click. |
| `OnClose` | `EventCallback<MudChip<T>>` | – | Occurs when this chip has been closed. Subscribing to this event enables the close button, unless `Href` is also set. |
| `Selected` | `bool` | – | Selects this chip. When `true`, the chip is displayed in a selected state. |
| `SelectedChanged` | `EventCallback<bool>` | – | Occurs when the `Selected` property has changed. |
