# IAIMPUIImageComboBox

## Description

IAIMPUIImageComboBox is combo box with an ability to specify image for each item. Custom values are not supported.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIBaseEdit — IAIMPUIBaseButtonnedEdit — IAIMPUIBaseComboBox — IAIMPUIImageComboBox

## Properties

### AIMPUI_IMAGECOMBOBOX_PROPID_IMAGELIST

Image list for items

- **Type:** IAIMPUIImageList
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIImageList, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIImageList>)

### AIMPUI_COMBOBOX_PROPID_ITEMINDEX

Index of selected item.
If nothing is selected - index will be set to `-1`.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Methods

### Add

- `in` **Obj** — `IUnknown`
  Object, should support the IAIMPString interface
- `in` **ExtraData** — `Integer`
  Index of image for the item
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetImageIndex

- `in` **Index** — `Integer`
- `out` **Result** — `Integer`

### SetImageIndex

- `in` **Index** — `Integer`
- `in` **Value** — `Integer`
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
