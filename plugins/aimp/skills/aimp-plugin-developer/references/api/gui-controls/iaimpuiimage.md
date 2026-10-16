# IAIMPUIImage

## Description

IAIMPUIImage provides an ability to display image from the IAIMPImage or the IAIMPUIImageList objects.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIImage

## Properties

### AIMPUI_IMAGE_PROPID_IMAGE

- **Type:** IAIMPImage
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPImage, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPImage>)

### AIMPUI_IMAGE_PROPID_IMAGESTRETCHMODE

Refer to description of the Flags variable from theIAIMPImage.Draw method.
Value of this property is used only for displaying image from IAIMPImage.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_IMAGE_PROPID_IMAGELIST

This value is used only if value of the `AIMPUI_IMAGE_PROPID_IMAGE` property is not set

- **Type:** IAIMPUIImageList
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIImageList, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIImageList>)

### AIMPUI_IMAGE_PROPID_IMAGEINDEX

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
