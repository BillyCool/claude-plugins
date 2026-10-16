# IAIMPUIBevel

## Description

IAIMPUIBevel is designed to draw frame around the some object or separate two objects groups via simple line

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIBevel

## Properties

### AIMPUI_BEVEL_PROPID_BORDERS

0 or combination of following flags:
`+ AIMPUI_FLAGS_BORDER_LEFT
+ AIMPUI_FLAGS_BORDER_TOP
+ AIMPUI_FLAGS_BORDER_RIGHT
+ AIMPUI_FLAGS_BORDER_BOTTOM`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
