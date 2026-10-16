# MessageBox components — API (generated from source)

## MudMessageBox : MudComponentBase

A pop-up dialog with a simple message and button choices.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Title` | `string?` | `null` | The title of this message box. Defaults to `null`. When `null`, the title will be hidden. |
| `TitleContent` | `RenderFragment?` | – | The custom content within the title. When set, the `Title` property is ignored. |
| `Message` | `string?` | – | The content within this message box. When `MessageContent` is set, this property is ignored. |
| `MarkupMessage` | `MarkupString` | – | The markup content within this message box. When `MessageContent` is set, this property is ignored. |
| `MessageContent` | `RenderFragment?` | – | The custom content within this message box. When set, `Message` and `MarkupMessage` are ignored. |
| `CancelText` | `string?` | `null` | The text of the Cancel button. Defaults to `null`. When `null`, the `Cancel` button will be hidden. |
| `CancelButton` | `RenderFragment?` | – | The custom content for the Cancel button. Must be a `MudButton`. When set, `CancelText` is ignored. |
| `NoText` | `string?` | `null` | The text of the No button. Defaults to `null`. When `null`, the `No` button will be hidden. |
| `NoButton` | `RenderFragment?` | – | The custom content for the No button. Must be a `MudButton`. When set, `NoText` is ignored. |
| `YesText` | `string` | `"OK"` | The text of the Yes/OK button. Defaults to `OK`. When `null`, the `Yes` button will be hidden. |
| `YesButton` | `RenderFragment?` | – | The custom content for the Yes button. Must be a `MudButton`. When set, `YesText` is ignored. |
| `OnYes` | `EventCallback<bool>` | – | Occurs when the Yes button is clicked. |
| `OnNo` | `EventCallback<bool>` | – | Occurs when the No button is clicked. |
| `OnCancel` | `EventCallback<bool>` | – | Occurs when the Cancel button is clicked, or this message box is closed via the Close button. |
| `Visible` | `bool` | – | Shows this message box. Can be bound via `@bind-Visible` to show and hide an inlined MessageBox. Has no effect on previously opened message boxes. |
| `VisibleChanged` | `EventCallback<bool>` | – | Occurs when `Visible` has changed. |
