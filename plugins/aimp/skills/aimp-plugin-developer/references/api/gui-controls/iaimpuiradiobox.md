# IAIMPUIRadioBox

## Description

Radio boxes present a set of mutually exclusive options to the user - that is, only one radio box in a set can be selected at a time. When the user selects a radio box, the previously selected box button becomes unselected.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUICheckBox — IAIMPUIRadioBox

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
