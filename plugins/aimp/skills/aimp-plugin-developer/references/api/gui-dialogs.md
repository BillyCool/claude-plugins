# Dialogs

## Dialogs

- IAIMPUIAuthDialog
- IAIMPUIBrowseFolderDialog
- IAIMPUIColorPickerDialog
- IAIMPUIFileDialogs
- IAIMPUIFontPickerDialog
- IAIMPUIMessageDialog
- IAIMPUIInputDialog
- IAIMPUIProgressDialog

## IAIMPUIAuthDialog

### Descriptions

IAIMPUIAuthDialog simplifies the OAuth2 (and like that) authorization process.

OAuth2-authorization assumes that the user will log in to the service in the browser, and the browser will already pass the authorization token to the application via the url callback. While the dialog is displayed, AIMP starts a local server at `localhost:8090` and waits for callback from the service, which will be passed to the plugin via IAIMPUIAuthDialogEvents.

The user can cancel the authorization process by simply closing the dialog box. In this case, the Execute function will end with the E_FAIL code.

### Methods

#### Execute

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Title** — `IAIMPString`
  Service title for which the dialog was called. Shown to user in the dialog.
- `in` **Text** — `IAIMPString`
  Authorization hints.
  Push the `nil/null` to use default authorization hints.
- `in` **EventsHandler** — `IAIMPUIAuthDialogEvents`
- `in` **Flags** — `DWORD`
  0, reserved for future usage
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to Interface

<IAIMPServiceUI>.QueryInterface(IID_IAIMPUIAuthDialog, <IAIMPUIAuthDialog>)

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 5.40.2660

### IAIMPUIAuthDialogEvents

#### Methods

##### OnParse

- `in` **Params** — `IAIMPString`
  Service answer, format description you will find in documentation for service's api.
- `out` **ErrorText** — `IAIMPString`
  If the service answer contains an error (or does not contain authorization data), plugins must return E_FAIL and fill the ErrorText output parameter.
- `out` **Result** — `HRESULT`
  Return S_OK on succeeded authorization, otherwise E_FAIL.

##### OnRequestUrl

- `out` **Url** — `IAIMPString`
  Authorization request url that will be opened in user's browser.
  Called after the AuthDialog initialization.
- `out` **Result** — `HRESULT`
  Return S_OK on succeeded, otherwise E_FAIL.

## IAIMPUIBrowseFolderDialog

### Description

IAIMPUIBrowseFolderDialog provides an access to the Browse Folder Dialog

### Methods

#### Execute

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Flags** — `DWORD`
  0 or combination of following flags:
  + AIMPUI_FLAGS_BROWSEFOLDER_CUSTOMPATHS - allow to user enter custom paths
  + AIMPUI_FLAGS_BROWSEFOLDER_MULTISELECT - allow to select few folders
- `in` **DefaultPath** — `IAIMPString`
  Default path, the dialog will be focused on it at start up. Optional, can be set to `nil / null`
- `out` **Selection** — `IAIMPObjectList`
  List of selected paths. Each item of the list is IAIMPString object.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to Interface

<IAIMPServiceUI>.QueryInterface(IID_IAIMPUIBrowseFolderDialog, <IAIMPUIBrowseFolderDialog>)

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIColorPickerDialog

### Description

IAIMPUIColorPickerDialog provides access to color pickers

### Method

#### Execute

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Caption** — `IAIMPString`
  Dialog Title
- `in` **Flags** — `DWORD`
  0 or combination of following flags:
  + AIMPUI_FLAGS_COLORPICKER_ALLOWALPHA - allow alpha-channel editing.
- `var` **Color** — `DWORD`
  Color in ARGB format.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread
  E_FAIL - user cancel the operation.

### Access to interface

<IAIMPServiceUI>.QueryInterface(IID_IAIMPUIColorPickerDialog, <IAIMPUIColorPickerDialog>)

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPUIFileDialogs

### Description

IAIMPUIFileDialogs provides an access for file open / save dialogs.

### Methods

#### ExecuteOpenDialog

Executes file open dialog for single file

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Caption** — `IAIMPString`
  Dialog Title
- `in` **Filter** — `IAIMPString`
  Filter for file formats in following format:

  ```
  <Format Name>|<List of extensions>|<Format Name>|<List of extensions>
  ```

  Example:

  ```
  All Files|*.mp3;*.ogg;|MPEG Audio|*.mp3;|OGG Vorbis Audio|*.ogg;
  ```
- `out` **FileName** — `IAIMPString`
  Full file name of selected by user file
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### ExecuteOpenDialog2

Executes file open dialog for multiple files

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Caption** — `IAIMPString`
  Dialog Title
- `in` **Filter** — `IAIMPString`
  Filter for file formats in following format:

  ```
  <Format Name>|<List of extensions>|<Format Name>|<List of extensions>
  ```

  Example:

  ```
  All Files|*.mp3;*.ogg;|MPEG Audio|*.mp3;|OGG Vorbis Audio|*.ogg;
  ```
- `out` **Files** — `IAIMPObjectList`
  List of full file names of selected by user files. Each item of the list is IAIMPString object.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### ExecuteSaveDialog

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Caption** — `IAIMPString`
  Dialog Title
- `in` **Filter** — `IAIMPString`
  Filter for file formats in following format:

  ```
  <Format Name>|<List of extensions>|<Format Name>|<List of extensions>
  ```

  Example:

  ```
  All Files|*.mp3;*.ogg;|MPEG Audio|*.mp3;|OGG Vorbis Audio|*.ogg;
  ```
- `var` **FileName** — `IAIMPString`
  Full file name of selected by user file.
  Note that if you specify the FileName field before execute the dialog that name will be used as default selection.
- `out` **FilterIndex** — `Integer`
  Number of format filter that selected by user, begins with 0.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to interface

<IAIMPServiceUI>.QueryInterface(IID_IAIMPUIFileDialogs, <IAIMPUIFileDialogs>)

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIFontPickerDialog

### Description

IAIMPUIFontPickerDialog provides access to color pickers

### Method

#### Execute

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Caption** — `IAIMPString`
  Dialog Title
- `in` **Flags** — `DWORD`
  Reserved for future usage, set 0 for the argument.
- `var` **Font** — `IAIMPUIFont`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread
  E_FAIL - user cancel the operation.

### Access to interface

<IAIMPServiceUI>.QueryInterface(IID_IAIMPUIFontPickerDialog, <IAIMPUIFontPickerDialog>)

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPUIMessageDialog

### Description

IAIMPUIMessageDialog provides an access to message box dialog

### Methods

#### Execute

All parameters are similar to native MessageBox function.

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Caption** — `IAIMPString`
- `in` **Text** — `IAIMPString`
- `in` **Flags** — `DWORD`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

  Additionally, refer to the "Return value" section in article about the native MessageBoxes.

### Access to Interface

<IAIMPServiceUI>.<IAIMPServiceUI>.QueryInterface(IID_IAIMPUIMessageDialog, <IAIMPUIMessageDialog>)

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIInputDialog

### Description

IAIMPUIInputDialog provides an access to the Input Dialog. This dialog allows user to enter the Text, Integer or Float values. Multiple input is supported too. Type of the editor is depended from the initial type of value.

### Methods

#### Execute

Executes dialog to input single value

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Caption** — `IAIMPString`
- `in` **EventsHandler** — `IUnknown`
  Refer to the IAIMPUIInputDialogEvents
- `in` **Text** — `IAIMPString`
  Text for label that placed near the input box
- `var` **Value** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Execute2

Executes dialog to input few values

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `in` **Caption** — `IAIMPString`
- `in` **EventsHandler** — `IUnknown`
  Refer to the IAIMPUIInputDialogEvents
- `in` **TextForValues** — `IAIMPObjectList`
  Text for labels that placed near the input boxes. List size must be equal to ValueCount
- `in` **Values** — `PVarValue`
  Pointer to first element of array of VarValue values.
  The VarValue instance must be released by calling side using theVarValueFree method.
- `in` **ValueCount** — `Integer`
  Count of elements in Values array
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to Interface

<IAIMPServiceUI>.QueryInterface(IID_IAIMPUIInputDialog, <IAIMPUIInputDialog>)

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

### IAIMPUIInputDialogEvents

#### Description

IAIMPUIInputDialogEvents provides an ability to validate entered values without closing the dialog, and lock the "OK" button if needed.

#### Methods

##### OnValidate

- `in` **Value** — `VarValue`
  Text value in edit box.
- `in` **ValueIndex** — `Integer`
  Index of edit box.
- `out` **Result** — `HRESULT`
  Return E_FAIL if entered values is not valid. Otherwise - S_OK;

## IAIMPUIProgressDialog

### Description

The IAIMPUIProgressDialog interface is a progress dialog. Only this dialog supports the multi-threading from all GUI library.

### Properties

#### AIMPUI_PROGRESSDLG_PROPID_CAPTION

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMPUI_PROGRESSDLG_PROPID_MESSAGE

Default message text that will be displayed above of progress bar

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMPUI_PROGRESSDLG_PROPID_SHOW_PROGRESS_ON_TASKBAR

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### Methods

#### Started

Show the dialog

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Finished

Hide the dialog

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Progress

Update progress.
Method must be called after the Started method and before the Finished method call.

- `in` **Position** — `Int64`
- `in` **Total** — `Int64`
- `in` **Text** — `IAIMPString`
  Message text that will be displayed above the progress bar. Can be set to `nil / null`, in this case text from the `AIMPUI_PROGRESSDLG_PROPID_MESSAGE` property will be displayed.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to Interface

<IAIMPServiceUI>.CreateObject(.., .., IID_IAIMPUIProgressDialog, <IAIMPUIProgressDialog>)

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal version:** 4.00.1660

### IAIMPUIProgressDialogEvents

#### Methods

##### OnCanceled

Event occurs when user clicking the "Cancel" button.
If plugin does not implement this interface - the "cancel" button will not be available for user.

#### Creating the instance

Instance creating by plugin and puts to the <IAIMPServiceUI>.CreateObject method.
