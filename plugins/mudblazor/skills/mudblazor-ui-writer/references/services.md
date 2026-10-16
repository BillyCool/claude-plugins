# Services — dialogs, snackbars, viewport, global defaults

Signatures verified against v9.11.0 source (`src/MudBlazor/Services`,
`src/MudBlazor/Components/Snackbar/SnackbarService.cs`,
`src/MudBlazor/Services/MudGlobal.cs`). All are registered by
`AddMudServices()` (see `getting-started.md`).

## IDialogService

Requires `<MudDialogProvider />` in the layout. Inject and show a component
that contains a `MudDialog`:

```csharp
@inject IDialogService DialogService

var parameters = new DialogParameters<MyDialog> { { x => x.Item, item } };
var options = new DialogOptions { CloseButton = true, MaxWidth = MaxWidth.Small };
var dialog = await DialogService.ShowAsync<MyDialog>("Edit item", parameters, options);
var result = await dialog.Result;
if (result is { Canceled: false })
{
    var value = result.Data;   // whatever the dialog passed to Close()
}
```

Key members (from `IDialogService.cs`):

- `Task<IDialogReference> ShowAsync<TComponent>()` — overloads with
  `(string? title)`, `(DialogOptions options)`, `(string? title, DialogOptions options)`,
  `(DialogParameters parameters)`, `(DialogParameters parameters, DialogOptions options)`,
  `(string? title, DialogParameters parameters)`,
  `(string? title, DialogParameters parameters, DialogOptions? options)`;
  plus the same set taking `Type component`.
- `Task<bool?> ShowMessageBoxAsync(string? title, string message, string yesText = "OK", string? noText = null, string? cancelText = null, DialogOptions? options = null)`
  — also `(string? title, MarkupString markupMessage, ...)` and
  `(MessageBoxOptions messageBoxOptions, DialogOptions? options = null)`.
  Returns `true` (yes), `false` (no), or `null` (cancel).
- `void Close(DialogReference dialog)` / `Close(DialogReference, DialogResult?)`.

Inside the dialog component, take `[CascadingParameter] IMudDialogInstance MudDialog`
and call `MudDialog.Close(DialogResult.Ok(value))` or `MudDialog.Cancel()`.
`DialogOptions` (all nullable, `init`-only): `Position`, `MaxWidth`,
`BackdropClick`, `CloseOnEscapeKey`, `CloseOnNavigation`, `NoHeader`,
`CloseButton`, `FullScreen`, `FullWidth`, `BackgroundClass`, `DefaultFocus`
(see `api/Dialog.md` for the provider/dialog parameters).

## ISnackbar

Requires `<MudSnackbarProvider />`. From `SnackbarService.cs`:

```csharp
@inject ISnackbar Snackbar

Snackbar.Add("Saved!", Severity.Success);
Snackbar.Add("Careful…", Severity.Warning, config =>
{
    config.ShowCloseIcon = true;
    config.VisibleStateDuration = 5000;
});
```

Overloads of `Add(...)` accept `string`, `MarkupString`, `RenderFragment`, or a
component type `Add<T>(Dictionary<string, object>? componentParameters, ...)`.
All take `Severity severity = Severity.Normal`,
`Action<SnackbarOptions>? configure = null`, `string? key = null` (a key makes
duplicate prevention possible). Global behavior comes from
`SnackbarConfiguration` (position class, max displayed, prevent duplicates,
etc.) set in `AddMudServices(c => c.SnackbarConfiguration...)`.

## IBrowserViewportService (breakpoints / resize)

From `IBrowserViewportService.cs`:

- `Task<Breakpoint> GetCurrentBreakpointAsync()`
- `Task<bool> IsMediaQueryMatchAsync(string mediaQuery)` /
  `IsBreakpointWithinWindowSizeAsync` / `IsBreakpointWithinReferenceSizeAsync(Breakpoint, Breakpoint reference)`
- `Task SubscribeAsync(IBrowserViewportObserver observer, bool fireImmediately = true)`
  and lambda overloads `SubscribeAsync(Guid observerId, Action<BrowserViewportEventArgs> lambda, ResizeOptions? options = null, ...)`;
  matching `UnsubscribeAsync`.
- `Task<BrowserWindowSize> GetCurrentBrowserWindowSizeAsync()`

For markup-only responsive behavior prefer `MudHidden` (`api/Hidden.md`) or
CSS utilities (`css-utilities.md`) over service subscriptions.

## MudGlobal — global component defaults

`MudGlobal` (static class, `Services/MudGlobal.cs`) holds process-wide
defaults grouped in nested static classes per component, e.g.
`MudGlobal.TooltipDefaults.Delay`, `MudGlobal.MenuDefaults.HoverDelay`,
plus `MudGlobal.UnhandledExceptionHandler` (default writes to console).
Set them once at startup. Grep the file for the current list of groups.

## Other registered services

`IScrollManager`, `IScrollListenerFactory`, `IScrollSpyFactory`,
`IKeyInterceptorService`, `IJsEventFactory`, `IJsApiService`
(clipboard/open-window helpers), `IResizeObserverFactory`, popover services,
and `ILocalizationInterceptor` (replace via
`services.AddLocalizationInterceptor<T>()` for custom translations).
