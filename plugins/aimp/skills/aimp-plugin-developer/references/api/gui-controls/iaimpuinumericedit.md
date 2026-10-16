# IAIMPUINumericEdit

## Description

The numeric edit box provides an ability to input integer or floating-point values.
Unlike the IAIMPUISpinEdit, the control based on single-line text edit with fuzzy input mask, has no ability to specify value range.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIBaseEdit — IAIMPUIBaseButtonnedEdit — IAIMPUIEdit — IAIMPUINumericEdit

## Properties

### AIMPUI_NUMERICEDIT_PROPID_MASK

Specifies input mask for numbers.

0 or combination of following flags:

- `AIMPUI_NUMERICEDIT_MASK_DECIMALS` - allows to enter decimal part
- `AIMPUI_NUMERICEDIT_MASK_NEGATIVE` - allows to enter negative numbers
- `AIMPUI_NUMERICEDIT_MASK_ZERO` - allows to enter zero

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_NUMERICEDIT_PROPID_VALUE

Current numeric value.

- **Type:** Integer / Double
- **Read:** IAIMPPropertyList.GetValueAsInt32 / IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsInt32 / IAIMPPropertyList.SetValueAsFloat

## Events

IAIMPUIChangeEvents occurs when text has been changed

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000
