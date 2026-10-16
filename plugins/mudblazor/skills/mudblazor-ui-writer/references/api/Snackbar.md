# Snackbar components — API (generated from source)

## SnackbarMessageMarkupString : ComponentBase

Renders a snackbar message supplied as an HTML `MarkupString`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Message` | `MarkupString` | – | Sets the message to be displayed as HTML content. This property allows you to pass an HTML-formatted message using `MarkupString`. |

## SnackbarMessageRenderFragment : ComponentBase

Renders a snackbar message supplied as a custom `RenderFragment`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Message` | `RenderFragment?` | – | Sets the message to be rendered as a custom fragment of UI. This property allows you to define a custom UI using `RenderFragment`. It can be used to pass in components, markup, or other content. |

## SnackbarMessageText : ComponentBase

Renders a snackbar message supplied as plain text.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Message` | `string?` | – | Plain text message to be displayed. This property is used to pass a plain string message. It does not support HTML or UI fragments. |

## MudSnackbarElement : MudComponentBase

Renders a single snackbar notification within a `MudSnackbarProvider`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Snackbar` | `Snackbar?` | – | The snackbar instance displayed by this component. |
| `CloseIcon` | `string` | `Icons.Material.Filled.Close` | Custom close icon. |

## MudSnackbarProvider : MudComponentBase

Displays snackbar notifications queued through the `ISnackbar` service, positioning and stacking them on the page.

_No own parameters — see base class `MudComponentBase`._
