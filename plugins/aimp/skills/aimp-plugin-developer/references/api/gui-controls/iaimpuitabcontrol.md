# IAIMPUITabControl

## Description

Unlike the IAIMPUIPageControl, the IAIMPUITabControl has only one container for children controls. Tabs switches the data for this controls.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUITabControl

## Properties

### AIMPUI_TABCONTROL_PROPID_ACTIVETABINDEX

Index of active tab

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TABCONTROL_PROPID_TABPOSITION

One from following values:

- `AIMPUI_TABS_POSITION_TOP` (default)
- `AIMPUI_TABS_POSITION_BOTTOM`

_(Since v6.00)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TABCONTROL_PROPID_PADDING

Padding between control's borders and children controls (children controls must be auto-aligned - the Alignment property must be set to value different from ualNone). Default: 5. _(Since v6.0)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TABCONTROL_PROPID_STYLE

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

- `in` **Caption** — `IAIMPString`
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

### Get

- `in` **Index** — `Integer`
- `out` **Caption** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetCount

- `out` **Result** — `Integer`

## Events

IAIMPUITabControlEvents

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUITabControlEvents

### Description

IAIMPUITabControlEvents provides an ability to handle page changing events from the IAIMPUITabControl.

### Methods

#### OnActivating

Event occurs when page is activating

- `in` **Sender** — `IAIMPUITabControl`
- `in` **TabIndex** — `Integer`
  Index of page that will be activated
- `var` **Allow** — `LongBool`
  Set this parameter to False to prevent activating the page.

#### OnActivated

Event occurs after activating the page

- `in` **Sender** — `IAIMPUITabControl`
- `in` **TabIndex** — `Integer`
  Index of active page

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
