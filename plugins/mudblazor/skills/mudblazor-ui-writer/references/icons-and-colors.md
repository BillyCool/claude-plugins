# Icons and color constants

Verified against v9.7.0 source (`src/MudBlazor/Icons`, `src/MudBlazor/Colors/Colors.cs`).

## Icons

Icons are SVG string constants passed to `Icon`/`StartIcon`/`EndIcon`-style
parameters:

```razor
<MudIcon Icon="@Icons.Material.Filled.Home" />
<MudButton StartIcon="@Icons.Material.Outlined.Save">Save</MudButton>
```

Namespaces (counts of `public const string` per class):

| Class | Count | Notes |
|---|---|---|
| `Icons.Material.Filled` | 2122 | default Material style |
| `Icons.Material.Outlined` | 2122 | |
| `Icons.Material.Rounded` | 2122 | |
| `Icons.Material.Sharp` | 2122 | |
| `Icons.Material.TwoTone` | 2122 | |
| `Icons.Custom.Brands` | 30 | GitHub, Twitter/X, LinkedIn, etc. |
| `Icons.Custom.FileFormats` | 8 | |
| `Icons.Custom.Uncategorized` | 19 | |

Icon names are PascalCase Material icon names (`Home`, `ArrowBack`,
`DeleteForever`, …). Names that start with a digit are prefixed, e.g.
`_360`-style — grep `Icons/Material/Filled.cs` if unsure a name exists.
`MudIcon` also accepts arbitrary SVG strings or font-icon class names
(via the `Icon` parameter, see `api/Icon.md`).

Related enums: `Color` (icon tint), `Size` (Small/Medium/Large).

## Colors — Material palette constants

`Colors` static class exposes the full Material color chart as strings:

```csharp
Colors.Red.Default      // "#F44336"
Colors.Blue.Lighten3
Colors.Green.Accent4
Colors.Shades.White     // "#FFFFFF"
Colors.Shades.Black     // "#000000"
Colors.Shades.Transparent
```

Palettes: `Red, Pink, Purple, DeepPurple, Indigo, Blue, LightBlue, Cyan, Teal,
Green, LightGreen, Lime, Yellow, Amber, Orange, DeepOrange, Brown, BlueGray,
Gray, Shades`.

Shades per palette: `Default`, `Lighten1`–`Lighten5`, `Darken1`–`Darken4`,
`Accent1`–`Accent4` (Brown, BlueGray, and Gray have no Accent shades;
Shades has only `White`, `Black`, `Transparent`).

These are plain strings — usable anywhere a CSS color string is accepted,
notably in theme palettes (`Primary = Colors.Indigo.Darken1`) or `Style`
attributes. For the matching CSS classes (`red-text text-darken-2` etc.) see
`css-utilities.md`.

## The `Color` enum (theme colors)

Component `Color` parameters take the `Color` enum: `Default`, `Primary`,
`Secondary`, `Tertiary`, `Info`, `Success`, `Warning`, `Error`, `Dark`,
`Transparent`, `Inherit`, `Surface`. Full list with CSS names in `enums.md`.
