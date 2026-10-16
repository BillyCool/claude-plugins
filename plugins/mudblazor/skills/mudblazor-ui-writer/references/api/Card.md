# Card components — API (generated from source)

## MudCard : MudComponentBase

Cards contain actions, text, or media like images or graphics. Keeping a card to a single subject keeps the design clean.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Elevation` | `int` | `1` | The size of the drop shadow. Defaults to `1`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Square` | `bool` | `false` | Disables rounded corners. Defaults to `false`. |
| `Outlined` | `bool` | `false` | Displays an outline. Defaults to `false`. This property is useful to differentiate cards which are the same color or use images. |
| `ContentPadding` | `bool` | `true` | Adds visual padding to the content (`MudCardHeader`, `MudCardContent` or `MudCardActions`). Defaults to `true`. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |

## MudCardActions : MudComponentBase

The action bar of a `MudCard`, typically holding buttons that trigger the card's related actions.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this component. |

## MudCardContent : MudComponentBase

The primary content area of a `MudCard`, holding its text and body elements.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this component. |

## MudCardHeader : MudComponentBase

The header area of a `MudCard`, typically holding an avatar, title, and action buttons.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `CardHeaderAvatar` | `RenderFragment?` | – | The avatar to display within this header. |
| `CardHeaderContent` | `RenderFragment?` | – | The main content of this header. |
| `CardHeaderActions` | `RenderFragment?` | – | The actions displayed within this header. |
| `ChildContent` | `RenderFragment?` | – | The custom content within this header. |

## MudCardMedia : MudComponentBase

The media area of a `MudCard`, displaying an image or graphic sized to a set height.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Title` | `string?` | `null` | Text for the `title` attribute which provides a basic tooltip. Defaults to `null`. |
| `Image` | `string?` | – | The URL of the image to display. |
| `Height` | `int` | `300` | The height, in pixels, of the `Image`. Defaults to `300`. |
