# IAIMPUIWinControl

## Description

The IAIMPUIWinControl unlike IAIMPUIControl has keyboard support and provides an ability to add children controls.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl

## Properties

### AIMPUI_WINCONTROL_PROPID_FOCUSED

1 - control is focused, 0 - otherwise

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

### AIMPUI_WINCONTROL_PROPID_TABORDER

Index in the list for navigation between controls via the Tab key

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Methods

### GetControl

Method provides an access to children controls

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
- `out` **Obj** — `IUnknown`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetControlCount

- `out` **Result** — `Integer`

### GetHandle

Method returns window handle for the control. If handle is not yet created - method will create it.

- `out` **Result** — `HWND`
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.

### HasHandle

Method check if window handle for the control is created.

- `out` **Result** — `LongBool`

### SetFocus

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## Events

IAIMPUIKeyboardEvents

IAIMPUIWndProcEvents

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIKeyboardEvents

### Description

IAIMPUIKeyboardEvents provides an ability to handle keyboard events

### Methods

#### OnEnter

Event occurs when control take focus

- `in` **Sender** — `IUnknown`
  Event sender

#### OnExit

Event occurs when control loose focus

- `in` **Sender** — `IUnknown`
  Event sender

#### OnKeyDown

- `in` **Sender** — `IUnknown`
  Event sender
- `var` **Key** — `Word`
  Virtual Key Code
- `in` **Modifiers** — `Word`
  0 or combination of following flags:
  - AIMPUI_FLAGS_MOD_ALT
  - AIMPUI_FLAGS_MOD_CTRL
  - AIMPUI_FLAGS_MOD_SHIFT

#### OnKeyPress

- `in` **Sender** — `IUnknown`
  Event sender
- `var` **Char** — `WideChar`
  Typed character in utf-16 encoding

#### OnKeyUp

- `in` **Sender** — `IUnknown`
  Event sender
- `var` **Key** — `Word`
  Virtual Key Code
- `in` **Modifiers** — `Word`
  0 or combination of following flags:
  - AIMPUI_FLAGS_MOD_ALT
  - AIMPUI_FLAGS_MOD_CTRL
  - AIMPUI_FLAGS_MOD_SHIFT

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
