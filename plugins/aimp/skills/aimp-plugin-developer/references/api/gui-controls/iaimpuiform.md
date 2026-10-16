# IAIMPUIForm

## Description

IAIMPUIForm is top-level window, that used as container for all another controls and non-visual objects.

**Note** that unlike to other API interfaces, the ARC is not used here. Form will be destroyed automatically when user close it, or if plugin call Close or Release methods of the form's interface. Make sure that all references to the form is cleared before destroy the form, otherwise - plugin can be crashed.

Form has two display modes: top-level / children window.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUIForm

## Properties

### AIMPUI_FORM_PROPID_CAPTION

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### AIMPUI_FORM_PROPID_BORDERICONS

0 or combination of following flags:

- `AIMPUI_FLAGS_BORDERICON_SYSTEMMENU` - show the system buttons and application icon
- `AIMPUI_FLAGS_BORDERICON_MINIMIZE` - allow to minimize window
- `AIMPUI_FLAGS_BORDERICON_MAXIMIZE` - allow to maximize window

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_FORM_PROPID_BORDERSTYLE

Style of form's border. One of following flags:

- `AIMPUI_FLAGS_BORDERSTYLE_SIZEABLE` - normal window
- `AIMPUI_FLAGS_BORDERSTYLE_SINGLE` - normal window without an ability to resize it
- `AIMPUI_FLAGS_BORDERSTYLE_DIALOG` - dialog window without an ability to resize it, does not have application icon and minimize / maximize buttons
- `AIMPUI_FLAGS_BORDERSTYLE_TOOLWINDOW` - tool window without an ability to resize it
- `AIMPUI_FLAGS_BORDERSTYLE_TOOLWINDOWSIZABLE` - tool window with an ability to resize it
- `AIMPUI_FLAGS_BORDERSTYLE_NONE` - window without the borders and captionForm with the AIMPUI_FLAGS_BORDERSTYLE_NONE border style will be display like a banner, without activation the window.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_FORM_PROPID_ICON

Pass the `nil/null` as argument to use app icon (default)

- **Type:** IAIMPImage, IAIMPImageContainer, IAIMPStream
- **Read:** Unavailable
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, ..)

### AIMPUI_FORM_PROPID_CLOSEBYESCAPE

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_FORM_PROPID_PADDING

Padding from borders to children controls that is placed via alignment (the Alignment property is different from ualNone value)
From 0 to 100

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_FORM_PROPID_STYLE

Current Style (read only), can be presented by one of following values: `AIMPUI_STYLE_LIGHT` / `AIMPUI_STYLE_DARK`.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

### AIMPUI_FORM_PROPID_SHOWONTASKBAR

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_FORM_PROPID_STAYONTOP

Pins the window to topmost. 0 is for regular mode _((since v6.00))_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_FORM_PROPID_MODALRESULT

Setting the property to value different from None will close the modal form and pass the value to modal result.
One of following flags:
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

_(Since v6.00)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_FORM_PROPID_CLIENTWIDTH/HEIGHT

Unlike the SetPlacement method, provides an ability to change client width / height (ignoring borders) without changing window position.
May be useful for secondary windows that displays at center of it owner.

_(Since v6.00)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Methods

### Close

Closes the form. Operation can be aborted by the IAIMPUIFormEvents.OnCloseQuery event.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetFocusedControl

Method provides an access to focused control in the form.

- `out` **Control** — `IAIMPUIWinControl`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Localize

Method to force apply the localization

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Destroy

Method destroys the form without calling the IAIMPUIFormEvents.OnCloseQuery event.

- `in` **Postponed** — `LongBool`
  True - form will be destroyed when current operation will be done.

  Must be used, if you release the form from any event handler.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### ShowModal

- `out` **Result** — `Integer`
  One of following values:
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

## Events

IAIMPUIFormEvents

IAIMPUIFormEvents2

IAIMPUIFormEvents3

## Create the instance

Instance must be created via <IAIMPServiceUI>.CreateForm.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## See Also

- Automatic localization

## IAIMPUIFormEvents

### Description

IAIMPUIFormEvents provides an ability to handle events from top-level window (refer to the IAIMPUIForm)

### Methods

#### OnActivated / OnDeactivated

This events occurs when activity of window has been changed.

For top-level windows only.

- `in` **Sender** — `IUnknown`
  Event sender

#### OnCreated / OnDestroyed

This events occurs when window is creating / destroying.

- `in` **Sender** — `IUnknown`
  Event sender

#### OnCloseQuery

Event occurs when user trying to close the window.

For top-level windows only.

- `in` **Sender** — `IUnknown`
  Event sender
- `var` **CanClose** — `LongBool`
  Plugin can set this flag to False to prevent window from closing.

#### OnLocalize

Event occurs when window should be localized.

Refer to the automatic localization help topic for more information.

- `in` **Sender** — `IUnknown`
  Event sender

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

### See Also

- Automatic localization

## IAIMPUIFormEvents2

### Description

IAIMPUIFormEvents2 provides an ability to handle events from top-level window (refer to the IAIMPUIForm)

### Methods

#### OnChangeScale

Event occurs when window has been scaled. You can receive current DPI via the IAIMPDPIAware interface.

For top-level windows only.

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **Multiplier** — `Integer`
- `in` **Divider** — `Integer`

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.50.2000

## IAIMPUIFormEvents3

### Description

IAIMPUIFormEvents3 provides an ability to handle events from top-level window (refer to the IAIMPUIForm)

### Methods

#### OnStyleChanged

Event occurs on change window style between light / dark mode or change it color scheme.

You can retrieve current style at any time via the AIMPUI_FORM_PROPID_STYLE property.

For top-level windows only.

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **Style** — `Integer`
  Can be one of following values: `AIMPUI_STYLE_LIGHT` / `AIMPUI_STYLE_DARK`.

### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateControl method.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.60.2130
