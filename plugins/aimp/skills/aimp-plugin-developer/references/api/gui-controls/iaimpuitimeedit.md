# IAIMPUITimeEdit

## Parent

Represents a single-line editable text box containing a time.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUITimeEdit

## Properties

### AIMPUI_TIMEEDIT_PROPID_VALUE

Current value.

Integer part is days, fractional part is milliseconds.
Time format is fully compatible with TDateTime type from Delphi language

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

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
