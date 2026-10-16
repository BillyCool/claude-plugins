# IAIMPUIEdit

## Description

IAIMPUIEdit is single line text editor

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIBaseEdit — IAIMPUIBaseButtonnedEdit — IAIMPUIEdit

## Properties

### AIMPUI_EDIT_PROPID_PASSWORDCHAR

Use this property to create an edit control that displays a special character in place of any entered text. If it is set to the null character, the edit control displays its text normally.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_EDIT_PROPID_TEXTHINT

Use TextHint to cue the user on what kind of entry is expected in the text field.
Only for Windows Vista and newer.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

## Events

IAIMPUIChangeEvents occurs when text has been changed

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
