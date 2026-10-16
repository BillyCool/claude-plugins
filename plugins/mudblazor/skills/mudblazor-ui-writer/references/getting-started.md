# Getting started — installing and wiring MudBlazor

Verified against MudBlazor v9.7.0 source (`src/MudBlazor.Docs/Pages/Getting Started`
and `src/MudBlazor/Extensions/ServiceCollectionExtensions.cs`).

## 1. Install

```
dotnet add package MudBlazor
```

## 2. Imports

`_Imports.razor`:

```razor
@using MudBlazor
```

## 3. Static assets

In `App.razor` (Blazor Web App / .NET 8+) or `index.html` (WASM standalone),
inside `<head>`:

```html
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet" />
<link href="_content/MudBlazor/MudBlazor.min.css" rel="stylesheet" />
```

Before `</body>` (after the Blazor script):

```html
<script src="_content/MudBlazor/MudBlazor.min.js"></script>
```

With .NET 9+ static asset mapping the docs use `@Assets[...]`:

```razor
<script src="@Assets["_content/MudBlazor/MudBlazor.min.js"]"></script>
```

Remove Bootstrap references from the default template — MudBlazor replaces them
and Bootstrap's CSS conflicts with MudBlazor's.

## 4. Register services

`Program.cs`:

```csharp
using MudBlazor.Services;

builder.Services.AddMudServices();
```

`AddMudServices()` registers (chain confirmed in `ServiceCollectionExtensions.cs`):
dialog (`IDialogService`), snackbar (`ISnackbar`), resize listener/observer
(`IBrowserViewportService`), key interceptor, JS events, scroll manager /
listener / spy, popover service, JS API, pointer-events service, and
localization. An overload `AddMudServices(Action<MudServicesConfiguration>)`
lets you configure snackbar, resize, and popover options in one place.
Individual `AddMudBlazor*` extensions exist if you want a subset.

## 5. Add the providers

In your main layout (typically `MainLayout.razor`) — all four, once, at the top:

```razor
<MudThemeProvider />
<MudPopoverProvider />
<MudDialogProvider />
<MudSnackbarProvider />
```

- `MudThemeProvider` — required for theming/CSS variables; also controls dark mode.
- `MudPopoverProvider` — required by everything popover-based: Select, Autocomplete,
  Menu, Tooltip, DatePicker, etc.
- `MudDialogProvider` / `MudSnackbarProvider` — required for `IDialogService` /
  `ISnackbar` respectively.

Blazor Web App note: MudBlazor components need interactivity. Use an interactive
render mode (`InteractiveServer`, `InteractiveWebAssembly`, or `InteractiveAuto`);
components on static-SSR pages will render but not respond.

## 6. Minimal layout skeleton

```razor
@inherits LayoutComponentBase

<MudThemeProvider />
<MudPopoverProvider />
<MudDialogProvider />
<MudSnackbarProvider />

<MudLayout>
    <MudAppBar Elevation="1">
        <MudIconButton Icon="@Icons.Material.Filled.Menu" Color="Color.Inherit"
                       Edge="Edge.Start" OnClick="@ToggleDrawer" />
        My App
    </MudAppBar>
    <MudDrawer @bind-Open="_open" Elevation="1">
        <MudNavMenu>
            <MudNavLink Href="/" Match="NavLinkMatch.All">Home</MudNavLink>
        </MudNavMenu>
    </MudDrawer>
    <MudMainContent>
        <MudContainer MaxWidth="MaxWidth.Large" Class="my-4">
            @Body
        </MudContainer>
    </MudMainContent>
</MudLayout>

@code {
    private bool _open = true;
    private void ToggleDrawer() => _open = !_open;
}
```

See `api/Layout.md`, `api/AppBar.md`, `api/Drawer.md`, `api/Main.md`,
`api/Container.md` for the full parameter lists.
