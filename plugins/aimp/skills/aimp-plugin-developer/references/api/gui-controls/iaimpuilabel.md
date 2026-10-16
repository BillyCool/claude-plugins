# IAIMPUILabel

## Description

IAIMPUILabel is simple text box element.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUILabel

## Properties

### AIMPUI_LABEL_PROPID_AUTOSIZE

Calculate size of elements automatically during its content size. 0 - auto size is switched off (default value).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_LABEL_PROPID_LINE

Visibility of separator line that located to the right of the text. 0 - line is hidden.

The AIMPUI_LABEL_PROPID_AUTOSIZE property must be set to 0.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_LABEL_PROPID_TEXT

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_LABEL_PROPID_TEXTALIGN

Horizontal text alignment. One of the following values:

- `AIMPUI_ALIGN_NEAR` - (left) (default)
- `AIMPUI_ALIGN_CENTER`
- `AIMPUI_ALIGN_FAR` - (right)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_LABEL_PROPID_TEXTALIGNVERT

Vertical text alignment. Can be set to one of following flags:

- `AIMPUI_ALIGN_NEAR` - (top)
- `AIMPUI_ALIGN_CENTER` - (Default)
- `AIMPUI_ALIGN_FAR` - (bottom)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_LABEL_PROPID_TEXTCOLOR

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_LABEL_PROPID_TEXTSIZE

Logical font height

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_LABEL_PROPID_TEXTSTYLE

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

### AIMPUI_LABEL_PROPID_TRANSPARENT

0 - background is opaque.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_LABEL_PROPID_URL

Link that will be opened in Internet browser when user click the label.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_LABEL_PROPID_WORDWRAP

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
