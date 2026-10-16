# IAIMPUIValidationLabel

## Description

IAIMPUIValidationLabel unlike the IAIMPUILabel has an ability to display status glyph to the left of the text.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUILabel — IAIMPUIValidationLabel

## Properties

### AIMPUI_VALIDATIONLABEL_PROPID_GLYPH

Glyph index, can be set to one of the following values:

- `AIMPUI_VALIDATIONLABEL_GLYPH_OK`
- `AIMPUI_VALIDATIONLABEL_GLYPH_WARNING`
- `AIMPUI_VALIDATIONLABEL_GLYPH_ERROR`
- `AIMPUI_VALIDATIONLABEL_GLYPH_CRITICAL_WARNING`

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
