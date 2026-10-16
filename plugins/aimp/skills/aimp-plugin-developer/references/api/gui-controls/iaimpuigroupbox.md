# IAIMPUIGroupBox

## Description

IAIMPUIGroupBox provides an ability to create group container for other controls.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIGroupBox

## Properties

### AIMPUI_GROUPBOX_PROPID_AUTOSIZE

Calculate size of elements automatically during its content size. 0 - auto size is switched off (default value).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_GROUPBOX_PROPID_BORDERS

0 or combination of following flags:
`+ AIMPUI_FLAGS_BORDER_LEFT
+ AIMPUI_FLAGS_BORDER_TOP
+ AIMPUI_FLAGS_BORDER_RIGHT
+ AIMPUI_FLAGS_BORDER_BOTTOM`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_GROUPBOX_PROPID_CAPTION

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_GROUPBOX_PROPID_TRANSPARENT

0 - background is opaque.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_GROUPBOX_PROPID_PADDING

Padding between control's borders and children controls (children controls must be auto-aligned - the Alignment property must be set to value different from ualNone). Default: 5. _(Since v6.0)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_GROUPBOX_PROPID_CHECKMODE

This property provides an ability to switch on the check box in the header of group.

- `AIMPUI_CHECKMODE_NONE` - check box is hidden
- `AIMPUI_CHECKMODE_CUSTOM` - check box is visible
- `AIMPUI_CHECKMODE_TOGGLE_ENABLED` - check box is visible, and switches the `AIMPUI_CONTROL_PROPID_ENABLED` property of children controls
- `AIMPUI_CHECKMODE_MINIMIZE` - check box is visible, changing the state shows/hide group's content and adjust it height automatically _((since 6.0))_ Changing the check box state can be processed via IAIMPUIChangeEvents.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_GROUPBOX_PROPID_CHECKED

State of check box in header of group box (if value of the AIMPUI_GROUPBOX_PROPID_CHECKMODE is different from 0):
Can be one of following values:
- `AIMPUI_CHECKSTATE_UNCHECKED`
- `AIMPUI_CHECKSTATE_CHECKED`
- `AIMPUI_CHECKSTATE_MIXED` Changing the check box state can be processed via IAIMPUIChangeEvents.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Events

IAIMPUIChangeEvents occurs when the `AIMPUI_GROUPBOX_PROPID_CHECKED` has been changed

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
