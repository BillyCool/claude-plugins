# IAIMPUIControl

## Description

The IAIMPUIControl interface is base for all controls.

## Parent

IAIMPPropertyList — IAIMPUIControl

## Properties

### AIMPUI_CONTROL_PROPID_CUSTOM

This is a user data parameter, it allow you to bind custom data to the interface.

- **Type:** IUnknown
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IUnknown, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IUnknown>)

### AIMPUI_CONTROL_PROPID_ENABLED

0 - disabled

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_CONTROL_PROPID_HINT

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_CONTROL_PROPID_NAME

Name of control, can contains latin symbols and numbers only. Used for automatic localization.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_CONTROL_PROPID_PARENT

Container that contains the control

- **Type:** IAIMPUIWinControl
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIWinControl, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIWinControl>)

### AIMPUI_CONTROL_PROPID_POPUPMENU

Context menu for the control.

- **Type:** IAIMPUIPopupMenu
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIPopupMenu, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIPopupMenu>)

### AIMPUI_CONTROL_PROPID_VISIBLE

0 - hidden.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Methods

### GetPlacement

Provides information about the control placement.
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- `out` **Placement** — `TAIMPUIControlPlacement`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetPlacementConstraints

Provides information about constrains of the control placement
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- `out` **PlacementConstraints** — `TAIMPUIControlPlacementConstraints`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### SetPlacement

Provides an ability to set placement of control
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- `in` **Placement** — `TAIMPUIControlPlacement`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### SetPlacementConstraints

Provides an ability to set constrains of control placement
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- `in` **PlacementConstraints** — `TAIMPUIControlPlacementConstraints`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### ClientToScreen / ScreenToClient

Provides an ability to translate coordinates between local and global system of coordinates
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- `var` **P** — `TPoint`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Invalidate

Provides an ability to redraw control

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### PaintTo

Provides an ability to draw content of control to DC at specified position
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- `in` **DC** — `HCANVAS`
  Canvas Handle
- `in` **X** — `Integer`
- `in` **Y** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## DPI Aware

The IAIMPDPIAware interface are supported. It provides information about current DPI of the control.

## Events

IAIMPUIMouseEvents

IAIMPUIMouseWheelEvents

IAIMPUIPlacementEvents

IAIMPUIPopupMenuEvents

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## TAIMPUIControlPlacement

### Common

TAIMPUIControlPlacement contains a placement settings for the control.

Player's engine provides few ways to place the control:
1. Absolution positioning (used properties: `Bounds`)
2. Positioning via anchors (used properties: `Anchors, Bounds`)
3. Positioning with aligning (used properties: `Alignment, AlignmentMargins, Bounds`)

### Description

#### TAIMPUIControlPlacement

- `var` **Alignment** — `TAIMPUIControlAlignment`
  One of following values:
  `+ ualNone` - alignment is not used
  `+ ualTop` - aligning by top side
  `+ ualBottom` - aligning by bottom side
  `+ ualLeft` - aligning by left side
  `+ ualRight` - aligning by right side
  `+ ualClient` - control will use all free space for placement
- `var` **AlignmentMargins** — `TRect`
  Offsets from the neighbors, 0 or positive values only. Property is used when the Alignment property is different from ualNone.
- `var` **Anchors** — `TRect`
  Anchor state for each side. 0 - anchor is not used. Property is used when the Alignment is set to ualNone.
- `var` **Bounds** — `TRect`
  Absolute position of the control.

### Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## TAIMPUIControlPlacementConstraints

### Description

TAIMPUIControlPlacementConstraints provides an ability to specify minimal / maximal size of control. Set field to 0 to remove limitation.

### Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIChangeEvents

### Description

Events occurs when control content is changed

### Methods

#### OnChanged

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **DC** — `HCANVAS`
- `in` **R** — `TRect`
  Client area of the control

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIDrawEvents

### Description

Events occurs when control is drawing

### Methods

#### OnDraw

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **DC** — `HCANVAS`
- `in` **R** — `TRect`
  Client area of the control

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIMouseEvents

### Description

IAIMPUIMouseEvents provides an ability to handle mouse events

### Methods

#### OnMouseDoubleClick

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **Button** — `TAIMPUIMouseButton`
  Mouse button, can be on of following values: `umbLeft, umbRight, umbMiddle`;
- `in` **X/Y** — `Integer`
  Coordinates of mouse cursor in control's system of coordinates.
  (0, 0) - top-left corner of control.
- `in` **Modifiers** — `Word`
  0 or combination of following flags:
  - AIMPUI_FLAGS_MOD_ALT
  - AIMPUI_FLAGS_MOD_CTRL
  - AIMPUI_FLAGS_MOD_SHIFT

#### OnMouseDown

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **Button** — `TAIMPUIMouseButton`
  Mouse button, can be on of following values: `umbLeft, umbRight, umbMiddle`;
- `in` **X/Y** — `Integer`
  Coordinates of mouse cursor in control's system of coordinates.
  (0, 0) - top-left corner of control.
- `in` **Modifiers** — `Word`
  0 or combination of following flags:
  - AIMPUI_FLAGS_MOD_ALT
  - AIMPUI_FLAGS_MOD_CTRL
  - AIMPUI_FLAGS_MOD_SHIFT

#### OnMouseLeave

- `in` **Sender** — `IUnknown`
  Event sender

#### OnMouseMove

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **X/Y** — `Integer`
  Coordinates of mouse cursor in control's system of coordinates.
  (0, 0) - top-left corner of control.
- `in` **Modifiers** — `Word`
  0 or combination of following flags:
  - AIMPUI_FLAGS_MOD_ALT
  - AIMPUI_FLAGS_MOD_CTRL
  - AIMPUI_FLAGS_MOD_SHIFT

#### OnMouseUp

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **X/Y** — `Integer`
  Coordinates of mouse cursor in control's system of coordinates.
  (0, 0) - top-left corner of control.
- `in` **Modifiers** — `Word`
  0 or combination of following flags:
  - AIMPUI_FLAGS_MOD_ALT
  - AIMPUI_FLAGS_MOD_CTRL
  - AIMPUI_FLAGS_MOD_SHIFT

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIMouseWheelEvents

### Description

Event occurs when user scroll mouse wheel under the control

### Methods

#### OnMouseWheel

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **WheelDelta** — `Integer`
  Wheel speed. Usually equals to `120` for scroll up, and `-120` for scroll down.
- `in` **X/Y** — `Integer`
  Coordinates of mouse cursor in control's system of coordinates.
  (0, 0) - top-left corner of control.
- `in` **Modifiers** — `Word`
  0 or combination of following flags:
  - AIMPUI_FLAGS_MOD_ALT
  - AIMPUI_FLAGS_MOD_CTRL
  - AIMPUI_FLAGS_MOD_SHIFT

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIPlacementEvents

### Description

The event occurs when control's bounds are changed.

### Methods

#### OnBoundsChanged

- `in` **Sender** — `IUnknown`
  Event sender

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIPopupMenuEvents

### Description

IAIMPUIPopupMenuEvents provides an ability to handle context menu events.

Note that this handler is not requires to show IAIMPUIPopupMenu that already assigned to control.

### Methods

#### OnContextPopup

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **X/Y** — `Integer`
  Coordinates of mouse cursor in control's system of coordinates.
  (0, 0) - top-left corner of control.
- `out` **Result** — `LongBool`
  Plugin must return True to prevent showing of standard context menu for this control.

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
