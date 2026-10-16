# IAIMPUICheckBox

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUICheckBox

## Properties

### AIMPUI_CHECKBOX_PROPID_AUTOSIZE

Calculate size of elements automatically during its content size. 0 - auto size is switched off (default value is 1).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_CHECKBOX_PROPID_CAPTION

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_CHECKBOX_PROPID_STATE

Can be one of following values:
- `AIMPUI_CHECKSTATE_UNCHECKED`
- `AIMPUI_CHECKSTATE_CHECKED`
- `AIMPUI_CHECKSTATE_MIXED`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_CHECKBOX_PROPID_WORDWRAP

0 - no word wrap.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Events

IAIMPUIChangeEvents occurs when state is changed

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
