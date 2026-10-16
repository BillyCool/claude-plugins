# IAIMPUIPageControl

## Description

IAIMPUIPageControl provides an ability to create multi-page groups. Each group can contains own children controls.

Note about the simple version of this control - the IAIMPUITabControl control.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIPageControl

## Properties

### AIMPUI_PAGECONTROL_PROPID_ACTIVE

Active Page

- **Type:** IAIMPUITabSheet
- **Read:** IAIMPPropertyList.GetValueAsObject
- **Write:** IAIMPPropertyList.SetValueAsObject

### AIMPUI_PAGECONTROL_PROPID_TABPOSITION

One from following values:

- `AIMPUI_TABS_POSITION_TOP` (default)
- `AIMPUI_TABS_POSITION_BOTTOM`

_(Since v6.00)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_PAGECONTROL_PROPID_STYLE

One from following values:

- `AIMPUI_TABS_STYLE_CLASSIC` (default)
- `AIMPUI_TABS_STYLE_BUTTONS`
- `AIMPUI_TABS_STYLE_HYBRID`

_(Since v6.00)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Methods

### Add

- `in` **Name** — `IAIMPString`
  Name of tab sheet control, is used for automatic localization
- `out` **Page** — `IAIMPUITabSheet`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Delete

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Delete2

- `in` **Page** — `IAIMPUITabSheet`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Get

- `out` **Index** — `Integer`
- `out` **Page** — `IAIMPUITabSheet`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetCount

- `out` **Result** — `Integer`

## Events

IAIMPUIPageControlEvents

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIPageControlEvents

### Description

IAIMPUIPageControlEvents provides an ability to handle page changing events from the IAIMPUIPageControl.

### Methods

#### OnActivating

Event occurs when page is activating

- `in` **Sender** — `IAIMPUIPageControl`
- `in` **Page** — `IAIMPUITabSheet`
  Page that will be activated
- `var` **Allow** — `LongBool`
  Set this parameter to False to prevent activating the page.

#### OnActivated

Event occurs after activating the page

- `in` **Sender** — `IAIMPUIPageControl`
- `in` **Page** — `IAIMPUITabSheet`
  Active page

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
