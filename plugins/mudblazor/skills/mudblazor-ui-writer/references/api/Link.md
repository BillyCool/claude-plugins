# Link components — API (generated from source)

## MudLink : MudComponentBase

A clickable link which can navigate to a URL.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Color` | `Color` | `Color.Primary` | The color of the link. Defaults to `Primary`. |
| `StartIcon` | `string?` | `null` | The icon displayed before the text. Defaults to `null`. |
| `EndIcon` | `string?` | `null` | The icon displayed after the text. Defaults to `null`. |
| `IconClass` | `string?` | `null` | The CSS classes applied to the icons. Defaults to `null`. You can use spaces to separate multiple classes. |
| `Typo` | `Typo` | `Typo.inherit` | The typography variant to use. Defaults to `inherit`. |
| `Underline` | `Underline` | `Underline.Hover` | Applies an underline to the link. Defaults to `Hover`. |
| `Href` | `string?` | `null` | The URL to navigate to upon click. Defaults to `null`. |
| `Target` | `string?` | `null` | The browser frame to open this link when `Href` is specified. Possible values include `_blank`, `_self`, `_parent`, `_top`, or a frame name . Defaults to `null`. |
| `Disabled` | `bool` | `false` | Prevents user interaction with this link. Defaults to `false`. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this link has been clicked. |
