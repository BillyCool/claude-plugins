# IAIMPUICheckComboBox

## Description

IAIMPUICheckComboBox is combo box that allows to user to select few items. Custom values are not supported.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIBaseEdit — IAIMPUIBaseButtonnedEdit — IAIMPUIBaseComboBox — IAIMPUICheckComboBox

## Properties

### AIMPUI_CHECKCOMBOBOX_PROPID_TEXT

Selected values divided via the ";" symbol

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

## Methods

### Add

- `in` **Obj** — `IUnknown`
  Object, should support the IAIMPString interface
- `in` **ExtraData** — `Integer`
  Value for the Checked property. 0 is unchecked.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetChecked

- `in` **Index** — `Integer`
- `out` **Result** — `LongBool`

### SetChecked

- `in` **Index** — `Integer`
- `in` **Value** — `LongBool`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
