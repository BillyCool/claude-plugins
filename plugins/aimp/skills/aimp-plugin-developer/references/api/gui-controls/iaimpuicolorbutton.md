# IAIMPUIColorButton

## Description

Special version of Button control provides ability to user to select color.
Selected colors displays inside button next to it text.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIColorButton

## Properties

### AIMPUI_COLORBUTTON_PROPID_CAPTION

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_COLORBUTTON_PROPID_TEXTSTYLE

Font Styles.
0 or combination of following flags:
`
+ AIMPUI_FLAGS_FONT_BOLD
+ AIMPUI_FLAGS_FONT_ITALIC
+ AIMPUI_FLAGS_FONT_STRIKEOUT
+ AIMPUI_FLAGS_FONT_UNDERLINE`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_COLORBUTTON_PROPID_VALUE

Color in ARGB format.

- **Type:** Int64
- **Read:** IAIMPPropertyList.GetValueAsInt64
- **Write:** IAIMPPropertyList.SetValueAsInt64

### AIMPUI_COLORBUTTON_PROPID_VALUE_ALLOWALPHA

0 - disallow to edit the alpha-channel. Default: allowed.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Events

IAIMPUIChangeEvents occurs when user successfully has changed the color

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.
Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000
