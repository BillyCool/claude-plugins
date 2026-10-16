# IAIMPUISplitter

## Description

Splitter can be used as a visual separator between two halves of your form and allows the user of your application to move it either vertically or horizontally.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUISplitter

## Properties

### AIMPUI_SPLITTER_PROPID_CANHIDE

Specifies whether you can hide the control via double-click on the splitter.
0 - cannot hide.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SPLITTER_PROPID_CONTROL

Managed control.

- **Type:** IAIMPUIControl
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIControl, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIControl>)

## Events

IAIMPUIDrawEvents

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
