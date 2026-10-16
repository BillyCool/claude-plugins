# IAIMPUISlider

## Description

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUISlider

## Properties

### AIMPUI_SLIDER_PROPID_AUTOSIZE

Calculate size of elements automatically during its content size. 0 - auto size is switched off (default value is 1).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_HORIZONTAL

0 - slider has vertical orientation (default)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_MARKS

0 - marks are hidden

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_PAGESIZE

Distance between two marks, minimal value: 1.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_LABELPOSITION

One of following values:

- `AIMPUI_SLIDER_LABELPOSITION_ABOVE`
- `AIMPUI_SLIDER_LABELPOSITION_AROUND_EDGES` (default)
- `AIMPUI_SLIDER_LABELPOSITION_BELOW`

_(Since v6.00)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_LABELVALUE

Text for current value.
Allowed to use format string with the %f macro.

_(Since v6.00)_

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_SLIDER_PROPID_LABELVALUE_WIDTH

Text for minimal value.
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

_(Since v6.00)_

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_SLIDER_PROPID_LABELVALUEMIN

Width of current value label, use 0 for auto-size. _((since v6.00))_

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_SLIDER_PROPID_LABELVALUEMIN_WIDTH

Width of minimal value label, use 0 for auto-size
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

_(Since v6.00)_

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_SLIDER_PROPID_LABELVALUEMAX

Text for maximal value _((since v6.00))_

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_SLIDER_PROPID_LABELVALUEMAX_WIDTH

Width of maximal value label, use 0 for auto-size.
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

_(Since v6.00)_

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_SLIDER_PROPID_TRANSPARENT

0 - background is opaque.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_VALUE

Position of slider.

The IAIMPUIChangeEvents.OnChanged is called when changing the position

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_VALUEDEFAULT

Default Value.
User can reset the slider position to default value by clicking right mouse button.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_VALUEMAX

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_SLIDER_PROPID_VALUEMIN

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Events

IAIMPUIDrawEvents - provides an ability to draw custom background for tracking area

IAIMPUIChangeEvents - occurs when position of slider has been changed

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
