# ThemeProvider components — API (generated from source)

## MudThemeProvider : ComponentBaseWithState

Provides a standard set of colors, shapes, sizes and shadows to a layout.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Theme` | `MudTheme?` | – | The theme used by the application. |
| `DefaultScrollbar` | `bool` | `false` | Uses the browser default scrollbar instead of the MudBlazor scrollbar. Defaults to `false`. |
| `ObserveSystemDarkModeChange` | `bool` | `true` | Detects when the system theme has changed between Light Mode and Dark Mode. Defaults to `true`. When `true`, the theme will automatically change to Light Mode or Dark Mode as the system theme changes. |
| `IsDarkMode` | `bool` | `false` | Uses darker colors for all MudBlazor components. Defaults to `false`. When this value changes, `IsDarkModeChanged` occurs. |
| `IsDarkModeChanged` | `EventCallback<bool>` | – | Occurs when `IsDarkMode` has changed. |
| `CurrentPalette` | `Palette?` | – | Gets the currently active palette based on the `IsDarkMode` setting. Returns `PaletteDark` when `IsDarkMode` is `true`; otherwise, returns `PaletteLight`. When this value changes, `CurrentPaletteChanged` occurs. |
| `CurrentPaletteChanged` | `EventCallback<Palette?>` | – | Occurs when `CurrentPalette` has changed. |
