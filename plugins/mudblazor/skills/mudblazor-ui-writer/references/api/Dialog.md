# Dialog components — API (generated from source)

## MudDialog : MudComponentBase

Displays an overlay that prompts users to confirm an action or provide additional information.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `TitleContent` | `RenderFragment?` | – | The custom content for this dialog's title. When `null`, the `Title` will be used. |
| `DialogContent` | `RenderFragment?` | – | The main content for this dialog. |
| `DialogActions` | `RenderFragment?` | – | The custom actions for this dialog. |
| `Options` | `DialogOptions?` | – | The default options for this dialog. These options are used if none are provided during the `ShowAsync` method. This is typically used for inline dialogs. |
| `OnBackdropClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the area outside the dialog has been clicked if `BackdropClick` is `true`. When set, this event will be called instead of the default backdrop click behavior of closing the dialog. |
| `OnKeyDown` | `EventCallback<KeyboardEventArgs>` | – | Occurs when a key has been pressed down. |
| `OnKeyUp` | `EventCallback<KeyboardEventArgs>` | – | Occurs when a pressed key has been released. |
| `Gutters` | `bool` | `true` | Adds padding to the sides of this dialog. Defaults to `true`. |
| `TitleClass` | `string?` | – | The CSS classes to apply to the title. Multiple classes must be separated by spaces. |
| `ContentClass` | `string?` | – | The CSS classes applied to the main dialog content. Multiple classes must be separated by spaces. |
| `ActionsClass` | `string?` | – | The CSS classes applied to the action buttons content. Multiple classes must be separated by spaces. |
| `ContentStyle` | `string?` | – | **[Obsolete]** The CSS styles applied to the main dialog content. |
| `Visible` | `bool` | `false` | For inline dialogs, shows this dialog. Defaults to `false`. This can be bound via `@bind-Visible` to show or hide inline dialogs. For regular dialogs, use the `ShowAsync` and `Close` methods. |
| `VisibleChanged` | `EventCallback<bool>` | – | Occurs when `Visible` has changed. |
| `DefaultFocus` | `DefaultFocus?` | `null`, which will use the global default from `DefaultFocus` if set, otherwise `Element` | The element which will receive focus when this dialog is shown. Defaults to `null`, which will use the global default from `DefaultFocus` if set, otherwise `Element`. |
| `AriaLabel` | `string?` | `null`, which names the dialog by its title bar, or by the title text when the header is hidden` | The accessible name announced for this dialog. Defaults to `null`, which names the dialog by its title bar, or by the title text when the header is hidden. Set this when the header is hidden and no title is available, such as an inline dialog with `NoHeader`. |
| `AriaLabelledBy` | `string?` | `null` | The id of the element that names this dialog. Defaults to `null`. Takes precedence over `AriaLabel` and the title bar. Point it at a heading inside `DialogContent` when a custom header replaces the title bar. |

## MudDialogContainer : MudComponentBase

An instance of a `MudDialog`.

*When a `MudDialog` is shown, a new instance is created. This instance can then be used to perform actions such as hiding the dialog programmatically.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Options` | `DialogOptions` | `DialogOptions.Default` | The options used for this dialog. Defaults to the options in the `MudDialog` or options passed during `ShowAsync` methods. |
| `Title` | `string?` | – | The text displayed at the top of this dialog if `TitleContent` is not set. |
| `TitleContent` | `RenderFragment?` | – | The custom content at the top of this dialog. This content will display so long as `Title` is not set. |
| `Content` | `RenderFragment?` | `the content of the `MudDialog` being displayed` | The content within this dialog. Defaults to the content of the `MudDialog` being displayed. |
| `Id` | `Guid` | – |  |
| `CloseIcon` | `string` | `Icons.Material.Filled.Close` | The custom icon displayed in the upper-right corner for closing this dialog. Defaults to `Close`. |

## MudDialogProvider : IDisposable

A manager for `MudDialog` instances.

*Add this component to your layout page if your application needs to display dialogs.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `NoHeader` | `bool?` | `null` | Hides headers for all dialogs by default. Defaults to `null`. |
| `CloseButton` | `bool?` | `null` | Shows a close button in the top-right corner for all dialogs by default. Defaults to `null`. |
| `BackdropClick` | `bool?` | `true` | Allows dialogs to be closed by clicking outside of them by default. Defaults to `true`. |
| `CloseOnEscapeKey` | `bool?` | – | Allows dialogs to be closed by pressing the Escape key by default. |
| `FullWidth` | `bool?` | `null` | Sets the width of dialogs to the width of the screen by default. Defaults to `null`. |
| `Position` | `DialogPosition?` | `null` | The location of dialogs by default. Defaults to `null`. |
| `MaxWidth` | `MaxWidth?` | `null` | The maximum allowed with of the dialog. Defaults to `null`. |
| `BackgroundClass` | `string?` | – | The custom CSS classes to apply to dialogs by default. Multiple classes must be separated by spaces. |
| `DefaultFocus` | `DefaultFocus?` | `null` | The element which will receive focus when a dialog is shown by default. Defaults to `null`. |
| `ReverseMessageBoxButtonOrder` | `bool` | `false` | Reverses the button order in all `MudMessageBox` instances. This is primarily useful for Blazor Hybrid Windows applications where the native OS button order differs from standard Material Design guidelines. Defaults to `false`. |
