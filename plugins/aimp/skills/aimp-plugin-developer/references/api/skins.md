# Skins

## Skins

- IAIMPServiceSkinsManager
- IAIMPSkinInfo

## IAIMPServiceSkinsManager

### Methods

#### EnumSkins

Method returns list with all installed skins (without path, file names only)

- `in` **List** — `IAIMPObjectList`
  List of IAIMPString
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetSkinInfo

Method returns information about specified skin

- `in` **FileName** — `IAIMPString`
  If FileName does not contains Path - skin engine will search it among of the installed.
- `out` **Info** — `IAIMPSkinInfo`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Select

- `in` **FileName** — `IAIMPString`
  Can be one of the following values:
  - `nil / null` - re-apply current skin
  - File name of installed skin (without path) - apply specified skin
  - An empty string - apply default skin
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Install

Method installs specified skin (but does not select it)

- `in` **FileName** — `IAIMPString`
  Full file name
- `in` **Flags** — `DWORD`
  Combination of following flags:
  - AIMP_SERVICE_SKINSMAN_FLAGS_INSTALL_FOR_ALL_USERS Warning! Administrator rights can be required for an ability to install skin for all users
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Uninstall

Method deletes installed skin.

Warning! This action requires administrator rights.

- `in` **FileName** — `IAIMPString`
  File name of installed skin (without path)
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### HSLToRGB / RGBToHSL

This is tool methods for an ability to translate color values from RGB and HSL color spaces.

### Properties

#### AIMP_SERVICE_SKINSMAN_PROPID_SKIN

File name (without path) of installed skin

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

#### AIMP_SERVICE_SKINSMAN_PROPID_HUE

Current hue (from 0 to 255). 0 - hue is not set.
Call the `Select` to apply changes of this parameter.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_SERVICE_SKINSMAN_PROPID_HUE_INTENSITY

Current hue intensity (from 0 to 100%). 0 - hue intensity is not set.
Call the `Select` to apply changes of this parameter.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_SERVICE_SKINSMAN_PROPID_HUE_BRIGHTNESS

Current brightness adjustment for color pixels (from 0 to 200%). 100% means no adjustments.
Call the `Select` to apply changes of this parameter.

_(Since v6.00)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceSkinsManager, ...);

### Summary

- **Definitions:** apiSkins.pas / apiSkins.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- AIMP_MSG_EVENT_SKIN
- Path to the local / common skins folders
- Property name conversion

## IAIMPSkinInfo

### Description

This interface provides an extended information about the skin.

### Properties

#### AIMP_SKININFO_PROPID_NAME

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_SKININFO_PROPID_AUTHOR

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_SKININFO_PROPID_DESCRIPTION

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_SKININFO_PROPID_PREVIEW

- **Type:** IAIMPImage
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPImage, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPImage>)

### Summary

- **Definitions:** apiSkins.pas / apiSkins.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455
