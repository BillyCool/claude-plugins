# IAIMPUIButton

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIButton

## Properties

### AIMPUI_BUTTON_PROPID_CAPTION

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_BUTTON_PROPID_FOCUSABLE

Determines, if the button can be focused via mouse or keyboard.
The 0 means that button cannot be focused. 1 is default.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BUTTON_PROPID_DEFAULT

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BUTTON_PROPID_DOWN

Specifies whether the button is selected/down (1) or not (0) _((since v6.00))_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BUTTON_PROPID_DROPDOWNMENU

Actual for `AIMPUI_BUTTON_PROPID_STYLE` = `AIMPUI_FLAGS_BUTTON_STYLE_DROPDOWN` or `AIMPUI_FLAGS_BUTTON_STYLE_DROPDOWNBUTTON`.

- **Type:** IAIMPUIPopupMenu
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIPopupMenu, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIPopupMenu>)

### AIMPUI_BUTTON_PROPID_IMAGEINDEX

Index of image to draw in the IAIMPUIImageList

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BUTTON_PROPID_IMAGELIST

- **Type:** IAIMPUIImageList
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIImageList, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIImageList>)

### AIMPUI_BUTTON_PROPID_MODALRESULT

Actual for modal dialogs. Click the button with modal result different from NONE will close the modal dialog and set its result to value of this property.

Can be one of following values:
`
- AIMPUI_FLAGS_MODALRESULT_NONE
- AIMPUI_FLAGS_MODALRESULT_OK
- AIMPUI_FLAGS_MODALRESULT_CANCEL
- AIMPUI_FLAGS_MODALRESULT_ABORT
- AIMPUI_FLAGS_MODALRESULT_RETRY
- AIMPUI_FLAGS_MODALRESULT_IGNORE
- AIMPUI_FLAGS_MODALRESULT_YES
- AIMPUI_FLAGS_MODALRESULT_NO
- AIMPUI_FLAGS_MODALRESULT_CLOSE
- AIMPUI_FLAGS_MODALRESULT_HELP
- AIMPUI_FLAGS_MODALRESULT_TRYAGAIN
- AIMPUI_FLAGS_MODALRESULT_CONTINUE`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BUTTON_PROPID_STYLE

Button style, can be one of following values:

+ `AIMPUI_FLAGS_BUTTON_STYLE_NORMAL`
+ `AIMPUI_FLAGS_BUTTON_STYLE_DROPDOWN` - button with menu, the DropDownMenu is appears when click the button
+ `AIMPUI_FLAGS_BUTTON_STYLE_DROPDOWNBUTTON` - hybrid version of first two styles: left part is normal button, right part is drop down button

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_BUTTON_PROPID_TEXTSTYLE

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

## Methods

### ShowDropDownMenu

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## Events

IAIMPUIChangeEvents occurs when clicking the button

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
