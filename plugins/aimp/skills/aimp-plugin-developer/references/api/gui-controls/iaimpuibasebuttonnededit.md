# IAIMPUIBaseButtonnedEdit

## Description

IAIMPUIBaseButtonnedEdit is base interface for all edit boxes that can contains in-place buttons.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIBaseEdit — IAIMPUIBaseButtonnedEdit

## Properties

### AIMPUI_BUTTONEDEDIT_BUTTONSIMAGES

List of images for in-place buttons

- **Type:** IAIMPUIImageList
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIImageList, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIImageList>)

## Methods

### AddButton

- `in` **EventsHandler** — `IUnknown`
  Events handler that must implement the IAIMPUIChangeEvents interface
- `out` **Button** — `IAIMPUIEditButton`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### DeleteButton

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### DeleteButton2

- `in` **Button** — `IAIMPUIEditButton`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetButton

- `in` **Index** — `Integer`
- `out` **Button** — `IAIMPUIEditButton`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetButtonCount

- `out` **Result** — `Integer`

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
