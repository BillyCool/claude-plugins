# IAIMPUIPanel

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIPanel

## Properties

### AIMPUI_PANEL_PROPID_AUTOSIZE

Calculate size of elements automatically during its content size. 0 - auto size is switched off (default value).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_PANEL_PROPID_BORDERS

0 or combination of following flags:
`+ AIMPUI_FLAGS_BORDER_LEFT
+ AIMPUI_FLAGS_BORDER_TOP
+ AIMPUI_FLAGS_BORDER_RIGHT
+ AIMPUI_FLAGS_BORDER_BOTTOM`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_PANEL_PROPID_TRANSPARENT

0 - background is opaque.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_PANEL_PROPID_PADDING

Padding between control's borders and children controls (children controls must be auto-aligned - the Alignment property must be set to value different from ualNone). Default: 0. _()_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

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
