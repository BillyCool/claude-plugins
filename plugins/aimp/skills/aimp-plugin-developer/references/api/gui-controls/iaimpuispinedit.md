# IAIMPUISpinEdit

## Description

IAIMPUISpinEdit provides an ability to input integer or floating-point values. Buttons that increments / decrements the editing value are placed at left and right sides.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUISpinEdit

## Properties

### AIMPUI_SPINEDIT_PROPID_DISPLAYMASK

Format string for displaying value. Format string must contains the `%s` macro.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_SPINEDIT_PROPID_VALUETYPE

Type of editing value:
`AIMPUI_SPINEDIT_VALUETYPE_INTEGER
AIMPUI_SPINEDIT_VALUETYPE_FLOAT`
Type of following methods are depended from this value.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SPINEDIT_PROPID_INCREMENT

The amount to increase / decrease the editing value by clicking at button at left or right side of control.

- **Type:** Integer / Double
- **Read:** IAIMPPropertyList.GetValueAsInt32 / IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsInt32 / IAIMPPropertyList.SetValueAsFloat

### AIMPUI_SPINEDIT_PROPID_MAXVALUE

- **Type:** Integer / Double
- **Read:** IAIMPPropertyList.GetValueAsInt32 / IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsInt32 / IAIMPPropertyList.SetValueAsFloat

### AIMPUI_SPINEDIT_PROPID_MINVALUE

- **Type:** Integer / Double
- **Read:** IAIMPPropertyList.GetValueAsInt32 / IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsInt32 / IAIMPPropertyList.SetValueAsFloat

### AIMPUI_SPINEDIT_PROPID_VALUE

Current value

- **Type:** Integer / Double
- **Read:** IAIMPPropertyList.GetValueAsInt32 / IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsInt32 / IAIMPPropertyList.SetValueAsFloat

## Events

IAIMPUIChangeEvents

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
