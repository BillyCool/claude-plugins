# Multi-Language UI

## Multi-Language UI

- IAIMPServiceMUI
- Custom localizations

## IAIMPServiceMUI

### Description

The IAIMPServiceMUI services provides an access to current localization

### Methods

#### GetName

Name of localization file without path and extension.
Friendly name of localization can be retrieved via the GetValue method with `"File\Name"` key;

- `out` **Value** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetValue

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `out` **Value** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_FAIL - The value was not found at specified path
  E_UNEXPECTED - An unexpected failure occurred

#### GetValuePart

Some variables can contains few values.
For example:

```
Form.DockToEdges=to left screen side|to right screen side|to top screen side|to bottom screen side
```

This method provides an access to each part by index.

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `in` **Part** — `Integer`
  Null-based Part index.
- `out` **Value** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_FAIL - The value was not found at specified path
  E_UNEXPECTED - An unexpected failure occurred

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceMUI, ...);

### Summary

- **Definitions:** apiMUI.pas / apiMUI.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### See also

- Notification about the localization changes
- An access to custom localizations

## Custom localizations (CustomLang)

### Description

Plugin must place all custom localization files in the "`Langs`" sub folder of own work folder in the `*.lng` format. The LNG format is simple INI-file.

All localizations automatically loads by engine and merges with base localization. You can get an access to merged localization via IAIMPServiceMUI service.

Automatic loading is performed by the following rules:
**1.** Engine trying to load file with same name as base localization from the `<PluginWorkPath>\Langs` folder.
**2.** If file is not found - engine trying to load `English.lng`
**3.** If file is not found - engine trying to load `Russian.lng`
**4.** Content of custom localization merges in memory (content of files will not changed) with base localization without replacing the identical keys.
