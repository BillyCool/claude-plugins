# Visuals

## Visuals

- IAIMPServiceVisualizations
- IAIMPExtensionCustomVisualization
- IAIMPExtensionEmbeddedVisualization
- Structures

## IAIMPServiceVisualizations

### Description

The IAIMPServiceVisualizations service have no any methods and properties, its required to provide ability to register custom extensions.

Usage example:

```
<IAIMPCore>.RegisterExtension(IID_IAIMPServiceVisualizations, TMyVisualExtension.Create);
```

### Summary

- **Definitions:** apiVisuals.pas / apiVisuals.h
- **Multi-threading:** Not supported
- **Extensions:** IAIMPExtensionCustomVisualization, IAIMPExtensionEmbeddedVisualization
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- AIMP_MSG_CMD_VISUAL_NEXT
- AIMP_MSG_CMD_VISUAL_PREV
- AIMP_MSG_EVENT_VISUAL_PLUGIN
- Registering extension

## IAIMPExtensionCustomVisualization

### Description

This is extension for the IAIMPServiceVisualizations service. This type of visualization provides an ability to render visualization outside of the visual display of player, and not depended from user choice.

### Methods

#### GetFlags

- `out` **Result** — `Integer`
  Returns zero or combination of followed flags:
  - `AIMP_VISUAL_FLAGS_RQD_DATA_WAVEFORM` - Plugin required WaveForm data for rendering
  - `AIMP_VISUAL_FLAGS_RQD_DATA_SPECTRUM` - Plugin required Spectrum data for rendering
  - `AIMP_VISUAL_FLAGS_NOT_SUSPEND` - Rendering must not be suspended even if the VisualDisplay window is hidden or inaccessible

#### Draw

- `in` **Data** — `PAIMPVisualData`
  Pointer to the visual data (see TAIMPVisualData).
  Read only

### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

### Summary

- **Definitions:** apiVisuals.pas / apiVisuals.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

## IAIMPExtensionEmbeddedVisualization

### Description

This is extension for the IAIMPServiceVisualizations service. This type visualization displays on visual display of player only and can be chosen by user.

### Methods

#### GetFlags

- `out` **Result** — `Integer`
  Returns zero or combination of followed flags:
  - `AIMP_VISUAL_FLAGS_RQD_DATA_WAVEFORM` - Plugin required WaveForm data for rendering
  - `AIMP_VISUAL_FLAGS_RQD_DATA_SPECTRUM` - Plugin required Spectrum data for rendering
  - `AIMP_VISUAL_FLAGS_NOT_SUSPEND` - Rendering must not be suspended even if the VisualDisplay window is hidden or inaccessible

#### GetMaxDisplaySize

Method returns a maximal resolution supported by the extension. If current resolution is not supported by extension, player will automatically stretch output.

- `out` **Width** — `Integer`
  Maximal width
- `out` **Height** — `Integer`
  Maximal height
- `out` **Result** — `HRESULT`
  S_OK - if success
  E_FAIL - if extension have no maximal size limitation

#### GetName

- `out` **S** — `IAIMPString`
  Friendly name
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Initialize

- `in` **Width** — `Integer`
  Width of visualization display.
  Note that display size can be changing via IAIMPExtensionEmbeddedVisualization.Resize method.
- `in` **Height** — `Integer`
  Height of visualization display.
  Note that display size can be changing via IAIMPExtensionEmbeddedVisualization.Resize method.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Finalize

Visualization should free all unneeded resources, but note that visualization can be initialized again - you must not finalize the plugin at all.

This method called when user switched to other visualization or switch off visualizations

#### Click

- `in` **X** — `Integer`
- `in` **Y** — `Integer`
- `in` **Button** — `Integer`
  - `AIMP_VISUAL_CLICK_BUTTON_LEFT`
  - `AIMP_VISUAL_CLICK_BUTTON_MIDDLE`
  - Right mouse button is reserved

#### Draw

- `in` **DC** — `HCANVAS`
  Visualization display canvas.
- `in` **Data** — `PAIMPVisualData`
  Pointer to the visual data (see TAIMPVisualData).
  Read only

#### Resize

- `in` **NewWidth** — `Integer`
- `in` **NewHeight** — `Integer`

### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

### Summary

- **Definitions:** apiVisuals.pas / apiVisuals.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPVisualizationDirectOutput

#### Description

Indicates to the player engine that the plugin supports direct output to the pixel buffer.
The interface must be implemented by the plugin at the same level as IAIMPExtensionEmbeddedVisualization.
Direct output takes precedence over regular output through DC.

#### Methods

##### Draw

- `var` **Buffer** — `PRGBQuad`
  Pointer to the first element of the ARGB array. The array dimension = `width` * `height` of the visualization screen.
  Width and Height are passed to the plugin via IAIMPExtensionEmbeddedVisualization.Initialize and IAIMPExtensionEmbeddedVisualization.Resize
- `in` **Data** — `PAIMPVisualData`
  Pointer to the visual data (see TAIMPVisualData).
  Read only

#### Summary

- **Definitions:** apiVisuals.pas / apiVisuals.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 6.00.3061

## Structures

### Structures

- TAIMPVisualData
- TAIMPVisualDataSpectrum
- TAIMPVisualDataWaveform

### TAIMPVisualData

##### TAIMPVisualData

This structure contains visualization data that needed for frame rendering
Note: data was calculated before the volume, balance and anti-clipping filters were applied.

- `in` **Peaks(2)** — `Single`
  An array of two elements of Single (32-bit floating point value) type.
  Current signal level in left and right channels [0.0 .. 1.0 .. infinity], where 1.0 is equals to 0 dB
- `in` **Spectrum(3)** — `TAIMPVisualDataSpectrum`
  An array of three elements of TAIMPVisualDataSpectrum type.
  0 - spectrum of left channel
  1 - spectrum of right channel
  2 - spectrum of both channels

  This field is populated only if the extension returns the `AIMP_VISUAL_FLAGS_RQD_DATA_SPECTRUM` flag in the GetFlags method.
- `in` **WaveForm(2)** — `TAIMPVisualDataWaveform`
  An array of two elements of TAIMPVisualDataWaveform type.
  Source data of left and right channels in wave-form.

  This field is populated only if the extension returns the `AIMP_VISUAL_FLAGS_RQD_DATA_WAVEFORM` flag in the GetFlags method.

### TAIMPVisualDataSpectrum

##### TAIMPVisualDataSpectrum

**array** [0..AIMP_VISUAL_SPECTRUM_MAX - 1] **of** Single;

Values range is `[0.0 .. 1.0 .. infinity]`

Here is short table of relationships between array index and freq of the signal:
0 ~ 20 Hz
10 ~ 200 Hz
20 ~ 400 Hz
30 ~ 630 Hz
40 ~ 870 Hz
50 ~ 1.1 KHz
60 ~ 1.4 KHz
70 ~ 1.7 KHz
80 ~ 2.1 KHz
90 ~ 2.5 KHz
100 ~ 3.0 KHz
110 ~ 3.5 KHz
120 ~ 4.0 KHz
130 ~ 4.5 KHz
140 ~ 5.2 KHz
150 ~ 6.0 KHz
160 ~ 6.7 KHz
170 ~ 7.6 KHz
180 ~ 8.5 KHz
190 ~ 9.6 KHz
200 ~ 11.0 KHz
210 ~ 12.0 KHz
220 ~ 13.5 KHz
230 ~ 15.0 KHz
240 ~ 16.8 KHz
255 ~ 20.0 KHz

### TAIMPVisualDataWaveform

##### TAIMPVisualDataWaveform

**array** [0..AIMP_VISUAL_WAVEFORM_MAX - 1] **of** Single;

32-bit float per sample.
Sample range is `[-infinity .. -1.0 .. 0.0 .. 1.0 .. infinity]`, where |1.0| is equals to 0 dbFS.
