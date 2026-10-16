# Theming — MudTheme, palettes, typography, dark mode

All values below are the actual defaults from MudBlazor v9.7.0 source
(`src/MudBlazor/Themes/MudTheme.cs` and `Themes/Models/*`).

## MudTheme structure

```csharp
public class MudTheme
{
    public Palette PaletteLight { get; set; }        // defaults: new PaletteLight()
    public Palette PaletteDark { get; set; }         // defaults: new PaletteDark()
    public Shadow Shadows { get; set; }              // Elevation[0..25] box-shadows
    public Typography Typography { get; set; }
    public LayoutProperties LayoutProperties { get; set; }
    public ZIndex ZIndex { get; set; }
    public PseudoCss PseudoCss { get; set; }         // Scope, default ":root"
}
```

Apply a custom theme via the provider:

```razor
<MudThemeProvider Theme="@_theme" />

@code {
    private readonly MudTheme _theme = new()
    {
        PaletteLight = new PaletteLight { Primary = "#0d6efd" },
        PaletteDark = new PaletteDark { Primary = "#3a86ff" },
        LayoutProperties = new LayoutProperties { DefaultBorderRadius = "8px" },
    };
}
```

## Dark mode

`MudThemeProvider` parameters (full list in `api/ThemeProvider.md`):

- `IsDarkMode` (`bool`) — bindable: `<MudThemeProvider @bind-IsDarkMode="_dark" />`
- `ObserveSystemDarkModeChange` (`bool`, default `true`) — follows OS changes.
- `Theme` (`MudTheme`)
- Method `Task<bool> GetSystemDarkModeAsync()` (via `@ref`) reads the OS
  preference, e.g. in `OnAfterRenderAsync(firstRender)`.

## PaletteLight defaults (Palette base class)

| Property | Default |
|---|---|
| `Black` / `White` | `#272c34` / `#FFFFFF` |
| `Primary` / `PrimaryContrastText` | `#594AE2` / white |
| `Secondary` | `Colors.Pink.Accent2` (`#ff4081`) |
| `Tertiary` | `#1EC8A5` |
| `Info` | `Colors.Blue.Default` (`#2196f3`) |
| `Success` | `Colors.Green.Accent4` (`#00c853`) |
| `Warning` | `Colors.Orange.Default` (`#ff9800`) |
| `Error` | `Colors.Red.Default` (`#f44336`) |
| `Dark` | `Colors.Gray.Darken3` (`#616161`) |
| `TextPrimary` | `Colors.Gray.Darken3` |
| `TextSecondary` / `TextDisabled` | black @ 0.54 / 0.38 alpha |
| `ActionDefault` / `ActionDisabled` / `ActionDisabledBackground` | black @ 0.54 / 0.26 / 0.12 |
| `Background` / `Surface` | white / white |
| `BackgroundGray` | `Colors.Gray.Lighten4` |
| `DrawerBackground` / `DrawerText` / `DrawerIcon` | white / Gray.Darken3 / Gray.Darken2 |
| `AppbarBackground` / `AppbarText` | `#594AE2` / white |
| `LinesDefault` | black @ 0.12 |
| `LinesInputs` | `Colors.Gray.Lighten1` |
| `TableLines` / `TableStriped` / `TableHover` | Gray.Lighten2 / black @ 0.02 / black @ 0.04 |
| `Divider` / `DividerLight` | `Colors.Gray.Lighten2` / black @ 0.8 |
| `Skeleton` | `rgba(0,0,0,0.11)` |
| `HoverOpacity` / `RippleOpacity` / `RippleOpacitySecondary` | 0.06 / 0.1 / 0.2 |
| `BorderOpacity` | 1.0 |
| `GrayDefault/Light/Lighter/Dark/Darker` | Gray Default/L1/L2/D1/D2 |
| `OverlayDark` / `OverlayLight` | `#212121` @ 0.5 / white @ 0.5 |

Every palette property also carries a `*ContrastText` partner for the theme
colors (Primary, Secondary, Tertiary, Info, Success, Warning, Error, Dark).

## PaletteDark overrides

| Property | Default |
|---|---|
| `Black` / `Dark` / `BackgroundGray` / `DrawerBackground` / `AppbarBackground` | `#27272f` |
| `Primary` | `#776be7` |
| `Info` / `Success` / `Warning` / `Error` | `#3299ff` / `#0bba83` / `#ffa800` / `#f64e62` |
| `Background` | `#32333d` |
| `Surface` | `#373740` |
| `TextPrimary` / `AppbarText` | `rgba(255,255,255,0.70)` |
| `TextSecondary` / `DrawerText` / `DrawerIcon` | `rgba(255,255,255,0.50)` |
| `TextDisabled` | `rgba(255,255,255,0.2)` |
| `ActionDefault` | `#adadb1` |
| `ActionDisabled` / `ActionDisabledBackground` | white @ 0.26 / 0.12 |
| `LinesDefault` / `TableLines` / `Divider` | `rgba(255,255,255,0.12)` |
| `LinesInputs` | white @ 0.3 |
| `TableStriped` | white @ 0.2 |
| `DividerLight` | white @ 0.06 |
| `Skeleton` | white @ 0.11 |

## Typography defaults

`Typography` has one `BaseTypography` per style; each exposes `FontFamily`,
`FontSize`, `FontWeight`, `LineHeight`, `LetterSpacing`, `TextTransform`.
`Default` sets the global font: Roboto, Helvetica, Arial, sans-serif.

| Style | Size | Weight | Line height | Letter spacing |
|---|---|---|---|---|
| Default | .875rem | 400 | 1.43 | .01071em |
| H1 | 6rem | 300 | 1.167 | -.01562em |
| H2 | 3.75rem | 300 | 1.2 | -.00833em |
| H3 | 3rem | 400 | 1.167 | 0 |
| H4 | 2.125rem | 400 | 1.235 | .00735em |
| H5 | 1.5rem | 400 | 1.334 | 0 |
| H6 | 1.25rem | 500 | 1.6 | .0075em |
| Subtitle1 | 1rem | 400 | | |
| Subtitle2 | .875rem | 500 | | |
| Body1 | 1rem | 400 | | |
| Body2 | .875rem | 400 | | |
| Button | .875rem | 500 | | |
| Caption | .75rem | 400 | | |
| Overline | .75rem | 400 | | |

Use with `<MudText Typo="Typo.h4">` — the `Typo` enum mirrors these names
(see `enums.md`).

## LayoutProperties defaults

| Property | Default |
|---|---|
| `DefaultBorderRadius` | 4px |
| `DrawerWidthLeft` / `DrawerWidthRight` | 240px |
| `DrawerMiniWidthLeft` / `DrawerMiniWidthRight` | 56px |
| `AppbarHeight` | 64px |

## ZIndex defaults

Drawer 1100 · Popover 1200 · AppBar 1300 · Dialog 1400 · Snackbar 1500 · Tooltip 1600.

## CSS variables

`MudThemeProvider` emits the whole theme as CSS variables on `:root`
(scope configurable via `PseudoCss.Scope`). Names confirmed by grepping
`src/MudBlazor/Styles` for `--mud-*` usages:

- Palette: `--mud-palette-<kebab-name>`, e.g. `--mud-palette-primary`,
  `--mud-palette-background-gray`, `--mud-palette-action-default`,
  `--mud-palette-appbar-background`; theme colors also get
  `-text` (contrast text) and `-hover` variants.
- Typography: `--mud-typography-<style>-{family,size,weight,lineheight,letterspacing,text-transform}`
  (styles: `default`, `h1`..`h6`, `subtitle1/2`, `body1/2`, `button`, `caption`, `overline`).
- Elevation: `--mud-elevation-0` … `--mud-elevation-25`.
- Layout: `--mud-default-borderradius`, `--mud-appbar-height`,
  `--mud-drawer-width-left/right`, `--mud-drawer-width-mini-left/right`.
- Z-index: `--mud-zindex-{drawer,popover,appbar,dialog,snackbar,tooltip,select}`.

Use them freely in custom CSS: `color: var(--mud-palette-primary);`.
