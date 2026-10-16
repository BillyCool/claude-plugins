# ColorPicker components — API (generated from source)

## MudColorPicker : MudPicker<MudColor>

Picks a color from a spectrum, palette, or predefined grid, with RGB, HSL, and hexadecimal inputs and optional alpha transparency.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ShowAlpha` | `bool` | `true` | Shows alpha transparency options. Defaults to `true`. When `true`, alpha options will be displayed and color output will be `RGBA`, `HSLA` or `HEXA` instead of `RGB`, `HSL` or `HEX`. |
| `ShowColorField` | `bool` | `true` | Displays the color field. Defaults to `true`. |
| `ShowModeSwitch` | `bool` | `true` | Displays the switch to change the color mode. Defaults to `true`. |
| `ShowInputs` | `bool` | `true` | Displays the text inputs, current mode, and mode switch. Defaults to `true`. |
| `ShowSliders` | `bool` | `true` | Displays hue and alpha sliders. Defaults to `true`. |
| `ShowPreview` | `bool` | `true` | Displays a preview of the color. Defaults to `true`. When `true`, the preview color can be used as a button for collection colors. |
| `ColorPickerMode` | `ColorPickerMode` | `ColorPickerMode.RGB` | The initial color channels shown. Defaults to `RGB`. Other values are `HEX` for hexadecimal values and `HSL` for hue/saturation/lightness mode. |
| `ColorPickerView` | `ColorPickerView` | `ColorPickerView.Spectrum` | The initial view. Defaults to `Spectrum`. The view can be changed if `ShowToolbar` is `true`. |
| `UpdateBindingIfOnlyHSLChanged` | `bool` | `false` | Limits updates to the bound value to when HSL values change. Defaults to `false`. When `true`, the bound value changes when HSL values change, even if the RGB values have not changed. |
| `Value` | `MudColor?` | – | The currently selected color as a `MudColor`. You can use properties in `MudColor` to get color channel values such as `RGB`, `HSL`, `HEX` and more. When this value changes, the `ValueChanged` event occurs. |
| `Text` | `string?` | – | The currently selected value, as a string. |
| `ValueChanged` | `EventCallback<MudColor?>` | – | Occurs when the `Value` property has changed. |
| `Palette` | `IEnumerable<MudColor>` | `a list of `35` colors` | The list of quick colors to display. Defaults to a list of `35` colors. The first five colors show as the quick colors when the preview dot is clicked. |
| `DragEffect` | `bool` | `true` | Continues to update the selected color while the mouse button is down. Defaults to `true`. When `false`, conditions like long latency are better supported and can be adjusted via the `ThrottleInterval` property. |
| `CloseIcon` | `string` | `Icons.Material.Filled.Close` | The custom icon to display for the close button. Defaults to `Close`. |
| `SpectrumIcon` | `string` | `Icons.Material.Filled.Tune` | The icon to display for the spectrum mode button. Defaults to `Tune`. |
| `GridIcon` | `string` | `Icons.Material.Filled.Apps` | The icon to display for the grid mode button. Defaults to `Apps`. |
| `PaletteIcon` | `string` | `Icons.Material.Filled.Palette` | The icon to display for the custom palette button. Defaults to `Palette`. |
| `ImportExportIcon` | `string` | `Icons.Material.Filled.ImportExport` | The icon to display for the import/export button. Defaults to `ImportExport`. |
| `ThrottleInterval` | `int` | `50` | The delay, in milliseconds, between updates to the selected color when `DragEffect` is `true`. Defaults to `50` milliseconds between updates. |
| `ShowTooltips` | `bool` | `true` | Enables tooltips for icon buttons. |
