# Options Dialog

## Options Dialog

- IAIMPServiceOptionsDialog
- IAIMPOptionsDialogFrame
- IAIMPOptionsDialogFrameKeyboardHelper
- IAIMPOptionsDialogFrameKeyboardHelper2

## IAIMPServiceOptionsDialog

### Description

Service provides an ability to add custom sheets into the Options Dialog. Custom sheets will be displayed at the "Plugins" category.

### Methods

#### FrameModified

Call this method to notify an engine about the changes, if one of the settings on custom sheet has been changed by user.

- `in` **Frame** — `IAIMPOptionsDialogFrame`
  Custom sheet where changes has been made
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### FrameShow

Provides an ability to switch into specified sheet.

- `in` **Frame** — `IUnknown`
  IAIMPOptionsDialogFrame
- `in` **ForceShow** — `LongBool`
  Set this parameter to True to force show Options Dialog.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceOptionsDialog, ...);

### Example

Example is located on the `Demos \ OptionFrameDemo`

### Summary

- **Definitions:** apiOptions.pas / apiOptions.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPOptionsDialogFrame

### Description

Interface provides an information about custom sheet for Options Dialog.

### Methods

#### GetName

- `out` **S** — `IAIMPString`
  Displaying name, can be depended from current localization.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### CreateFrame

- `in` **ParentWindow** — `HWND`
  Handle of parent window, where frame must be placed.
  The frame will be automatically aligned to entire client area of the parent window.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `out` **Result** — `HWND`
  Handle of custom sheet window.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.

#### DestroyFrame

#### Notification

- `in` **ID** — `Integer`
  Notification ID, can be one of following values:
  - `AIMP_SERVICE_OPTIONSDIALOG_NOTIFICATION_LOAD` - custom sheet should initialize all settings with values from configuration file
  - `AIMP_SERVICE_OPTIONSDIALOG_NOTIFICATION_LOCALIZATION` - localization has been changed, custom sheet should update localization of embedded controls
  - `AIMP_SERVICE_OPTIONSDIALOG_NOTIFICATION_SAVE` - custom sheet should save all settings to configuration file
  - `AIMP_SERVICE_OPTIONSDIALOG_NOTIFICATION_CAN_SAVE` - notification occurs before saving to an ability to validate settings. If one of settings is not valid - plugin should raise the exception. Note that text of exception will not shown to user.
  - `AIMP_SERVICE_OPTIONSDIALOG_NOTIFICATION_RESET` - custom sheet should reset all settings to it defaults

### DPI Aware

The WM_DPICHANGED sent to frame handle (refer to the CreateFrame method) when scale factor for the Options Dialog has changed. Plugin must handle this message and scale content of the frame.

### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

### Example

Example is located on the `Demos \ OptionFrameDemo`

### Summary

- **Definitions:** apiOptions.pas / apiOptions.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

## IAIMPOptionsDialogFrameKeyboardHelper

### Description

Interface should be implemented on same to IAIMPOptionsDialogFrame level.

### Methods

#### DialogKey

- `in` **CharCode** — `Word`
- `in` **Unused** — `Integer`
  For future usage
- `out` **Result** — `LongBool`
  Returns True If plugin process the request.

#### SelectFirstControl

Method calls, when user entering to the plugin frame via keyboard from other control that is not located in the frame.

- `out` **Result** — `LongBool`
  If control for focusing was not found - method must return False.

#### SelectNextControl

Method calls, when user switching between controls in frame via keyboard.

- `in` **FindForward** — `LongBool`
- `in` **IsTabKeyAction** — `LongBool`
- `out` **Result** — `LongBool`
  If control for focusing was not found - method must return False.

### Summary

- **Definitions:** apiOptions.pas / apiOptions.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

## IAIMPOptionsDialogFrameKeyboardHelper2

### Description

Interface should be implemented on same to IAIMPOptionsDialogFrame level.

### Methods

#### SelectLastControl

Method calls, when user entering to the plugin frame via keyboard using backward navigation from other control that is not located in the frame.

- `out` **Result** — `LongBool`
  If control for focusing was not found - method must return False.

### Summary

- **Definitions:** apiOptions.pas / apiOptions.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455
