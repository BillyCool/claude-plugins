# GUI

## IAIMPServiceUI

### Description

GUI is API for creating an UI in style of standard for AIMP controls.

Service provides an access to common methods for creating windows, controls and objects.

### Methods

#### CreateForm

Method provides an ability to create child or top-level form. Form is a owner for all other controls and objects.

- `in` **OwnerWindow** — `HWND`
  Handle of Owner Window. The form will be placed over the Owner.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Flags** — `DWORD`
  One of the flags:

  - `AIMPUI_SERVICE_CREATEFORM_FLAGS_REGULAR`
  Creates a regular window

  - `AIMPUI_SERVICE_CREATEFORM_FLAGS_CHILD`
  Creates window that will behave as a child control of the owner window

  - `AIMPUI_SERVICE_CREATEFORM_FLAGS_LAYERED`
  Creates window with per-pixel semi-transparency support. This window cannot be used to place other controls, and all rendering is performed manually using IAIMPUIDrawEvents. To allow the user to resize the window using the mouse, set the `AIMPUI_FORM_PROPID_BORDERSTYLE` property to `AIMPUI_FLAGS_BORDERSTYLE_SIZEABLE` and specify `AIMPUI_FORM_PROPID_PADDING`.
- `in` **Name** — `IAIMPString`
  Name of control, can contains latin symbols and numbers only. Used for automatic localization.
- `in` **EventsHandler** — `IUnknown`
  Events handler, should be implemented on plugin side. Can be set to `nil / null`.
- `out` **Form** — `IAIMPUIForm`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### CreateControl

Method creates a control.

- `in` **Owner** — `IAIMPUIForm`
  All children controls and objects will be destroyed automatically when owner will be destroyed
- `in` **Parent** — `IAIMPUIWinControl`
  Parent for the control. Parent must be owned by same form.
- `in` **Name** — `IAIMPString`
  Name of control, can contains latin symbols and numbers only. Used for automatic localization.
- `in` **IID** — `TGUID`
  IID of the control
- `in` **EventsHandler** — `IUnknown`
  Events handler, should be implemented on plugin side. Can be set to `nil / null`.
- `out` **Control** — ``
  Interface for newly created control
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### CreateObject

Methods creates non-visual object with optional bind to a specified window.

- `in` **Owner** — `IAIMPUIForm`
  All children controls and objects will be destroyed automatically when owner will be destroyed
  Put `nil / null` if you not need to bind the object to a window. In this case, object will be destroyed as soon as all references to it will be released.
- `in` **EventsHandler** — `IUnknown`
  Events handler, should be implemented on plugin side. Can be set to `nil / null`
- `in` **IID** — `TGUID`
  IID of the object
- `out` **Obj** — ``
  Interface for newly created object
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceUI, ...);

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## Automatic Localization (IAIMPUIAutoLocalization)

### Overview

Engine of AIMP can localize all forms and controls automatically. If you want to use this feature of engine, you must setup your own localization file with following rules. And do not forget to set names for all forms and controls.

### Rules

1. Section name in localization file must be equals to name of IAIMPUIForm.

2. Key name must be equals to name of IAIMPUIControl, in this case the value of key will be applied to caption of the control.

3. To localize tool tip for control, create the key with name of control with `".h"` suffix.

```
[Form Name]
MyButton.h=Hint for the button
```

4. Separate section is used to localize list of Combobox controls that obeys to following rule:

```
[Form Name.Control Name]
i[0]=Item 1
i[1]=Item 2
```

5. Separate section is used to localize in-place buttons of IAIMPUIBaseButtonnedEdit descendants that obeys to following rule:

```
[Form Name.Control Name]
b[0]=Button 1
b[1]=Button 2
```

6. Same rule is used for columns of IAIMPUITreeList:

```
[Form Name.Control Name]
c[0]=Column 1
c[1]=Column 2
```

7. Separate section is used to localize the TextHint of IAIMPUIEdit that contains a "th" key:

```
[Form Name.Control Name]
th=hint for the editor
```

8. Separate global section is used to localize menu items and actions. Instead of name the ID field is used:

```
[Common]
<Action.ID>=Action 1
<Action.ID>.h=Hint for Action 1
<Action.ID>.g=Group name 1
<MenuItem.ID>=Menu Item 2
```

Since AIMP6, the Caption, GroupName and Hint properties can refers to built-in localizations, just set the value in following format:

```
@Section\Key
```

## Color accent support (IAIMPUIColorSchema)

### Description

Starting from AIMP 5, user able to change color accent of entire application (including all secondary windows). Color accent of elements based on GUI API changes automatically.
But, if your plugin uses custom draw or custom elements you need to use the IAIMPUIColorSchema interface to implement color accent support. IAIMPUIColorSchema implemented on the IAIMPServiceUI level.

### IAIMPUIColorSchema Methods

#### ApplyToARGB

- `var` **ARGB** — `DWORD`
  Applies color schema to color in ARGB format (the TAlphaColor type in Delphi terms).

#### ApplyToColor

- `var` **Color** — `DWORD`
  Applies color schema to color in BGR format (the TColor type in Delphi terms).

#### ApplyToColors

- `var` **Colors** — `PRGBQuad`
  Applies color schema to array of RGBQuad.
- `in` **NumberOfColors** — `Integer`
  number of colors in the array

#### ApplyToImage

- `var` **Image** — `IAIMPImage`
  Applies color schema to specified image.

### Creating the instance

You can take a reference to the interface via <IAIMPServiceUI>.QueryInterface.

### Notifications

On change the color accent, GUI framework will broadcast the AIMP_MSG_EVENT_UI_MODE message and call the IAIMPUIFormEvents3.OnStyleChanged event.

### See Also

- Hook broadcast messages
- IAIMPUIMode

## DPI Awareness (IAIMPUIDPIAwareness)

### Description

GUI-framework is already adapted for support of 100%-200% scale factors.

### Coordinates Translation

By default, GUI framework uses 96 dpi (independent from real scale factor) to define positions and sizes of controls - coordinates translation mode. Plugin can switch off the coordinates translation mode via the IAIMPUIDPIAwareness interface that implemented on the IAIMPUIForm side.

### The IAIMPUIDPIAwareness methods

#### IAIMPUIDPIAwareness.IsDPIAware

- `out` **Result** — `BOOL`
  True - means that plugin is dpi aware, coordinates translation mode is switched off.

#### IAIMPUIDPIAwareness.SetDPIAware

Method provides an ability to switch off / on the coordinates translation mode.

- `in` **Value** — `BOOL`
  True - means that plugin is dpi aware, coordinates translation mode is switched off.

### What changes are required on plugin side?

To make your plugin dpi aware - you should update all used images. Each image should be specified in few resolutions: for 100%, 125%, 150%, 175% and 200% scale factors. Of course, you can ignore some of these resolutions, in this case, frame work will scale images by itself. Use the IAIMPDPIAware interface to define source DPI of the IAIMPImage or IAIMPUIImageList.

The IAIMPUIFormEvents2.OnChangeScale event occurs when IAIMPUIForm scales. Plugin should handle this event and update glyphs and image list for all children controls by most suitable images. Current DPI value can be determined by IAIMPDPIAware manifest that has been implemented on IAIMPUIForm level. You need to update image resources in your plugins.

### See Also

- IAIMPUIMode

## More in this chapter

- **Non-visual objects** — `api/gui-non-visual-objects.md`
- **Dialogs** — `api/gui-dialogs.md`
- **Controls** — `api/gui-controls/`
