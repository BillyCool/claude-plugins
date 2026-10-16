# IAIMPUIBBCBox

## Description

IAIMPUIBBCBox provides an ability to display formatted text via BBCodes.
The following BBCodes are supported: B, I, U, S, COLOR, URL.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIBBCBox

## Properties

### AIMPUI_BBCBOX_PROPID_AUTOSCROLL

Determines behavior when text is not fully visible in the control:
0 - text will be cut off by end ellipsis
1 - scroll bars will appears (default)

_(Since v5.40)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BBCBOX_PROPID_BORDERS

0 or combination of following flags:
`+ AIMPUI_FLAGS_BORDER_LEFT
+ AIMPUI_FLAGS_BORDER_TOP
+ AIMPUI_FLAGS_BORDER_RIGHT
+ AIMPUI_FLAGS_BORDER_BOTTOM`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BBCBOX_PROPID_TEXT

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_BBCBOX_PROPID_TEXTALIGN

Horizontal text alignment. One of the following values:

- `AIMPUI_ALIGN_NEAR` - (left) (default)
- `AIMPUI_ALIGN_CENTER`
- `AIMPUI_ALIGN_FAR` - (right) _(Since v5.40)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BBCBOX_PROPID_TEXTCOLOR

Text color in RRGGBB format _((since v5.40))_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BBCBOX_PROPID_TRANSPARENT

0 - background is opaque.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BBCBOX_PROPID_PADDING

Padding between control's borders and content. From 0 to 100.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BBCBOX_PROPID_WORDWRAP

0 - no word wrap.

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
