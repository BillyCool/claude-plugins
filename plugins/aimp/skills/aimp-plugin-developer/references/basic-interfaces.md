# Basic Interfaces

## Basic Interfaces

- IAIMPCore
- IAIMPPlugin
- IAIMPExternalSettingsDialog

## IAIMPCore

### Description

IAIMPCore is main link between plugin and the application. This interface provides an ability to access to services and an ability to register custom services and extensions.

### Methods

#### CreateObject

Method provides an ability to create primitive objects

- `in` **IID** — `TGUID`
  Object GUID
- `out` **Obj** — `Untyped`
  Object instance
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_NOINTERFACE - object with specified GUID is not registered.

#### GetPath

Method returns a path to one of the "system" folders of player

- `in` **PathID** — `Integer`
  Folder ID, can be one of the following values:
  - `AIMP_CORE_PATH_AUDIOLIBRARY` - path to folder with data base of audio library for current user
  - `AIMP_CORE_PATH_HELP` - path to folder with help
  - `AIMP_CORE_PATH_ICONS` - path to folder with icon sets
  - `AIMP_CORE_PATH_LANGS` - path to folder with localizations
  - `AIMP_CORE_PATH_PLAYLISTS` - path to folder with current user playlists
  - `AIMP_CORE_PATH_PLUGINS` - path to folder with plugins
  - `AIMP_CORE_PATH_PROFILE` - path to profile folder of current user
  - `AIMP_CORE_PATH_SKINS` - path to folder with skins for current user
  - `AIMP_CORE_PATH_SKINS_COMMON` - path to folder with common (for all users) skins
- `out` **Value** — `IAIMPString`
  Full path
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### RegisterExtension

Method provides an ability to register extension.
An access to extensions provides by specified for it services. For example: IAIMPServiceAudioDecoders

All extensions will be automatically unregistered from the application before plugin finalization.

- `in` **ServiceIID** — `TGUID`
  Service IID
- `in` **Extension** — `IUnknown`
  Extension
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread
  E_NOINTERFACE - service with specified IID does not registered or does not support extensions.

#### RegisterService

Method provides an ability to register custom service.
All services will be automatically unregistered from the application before plugin finalization.

- `in` **Service** — `IUnknown`
  Service
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### UnregisterExtension

Method provides an ability to unregister specified extension manually.

Note 1: all extensions will be automatically unregistered from the application before plugin finalization. So, this method is optional.
Note 2: extension may be used at the current time, in this case it will be completely unregistered only the after release

- `in` **Extension** — `IUnknown`
  Extension
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Creating the instance

Instance of interface creates by the application and sends to plugin during initialization.

### Interface definition

Interface definition is located in the apiCore.pas / apiCore.h

### See also

- Access to services
- Guidelines for working with services
- Creating custom services

## IAIMPPlugin

### Methods

#### InfoGet

Method returns an information about the plugin.
Method must not require the plugin initialization.

- `in` **Index** — `Integer`
  One of the values:
  - AIMP_PLUGIN_INFO_NAME
  - AIMP_PLUGIN_INFO_AUTHOR
  - AIMP_PLUGIN_INFO_SHORT_DESCRIPTION
  - AIMP_PLUGIN_INFO_FULL_DESCRIPTION
- `out` **Result** — `PChar`
  Pointer to an char null-terminated array. Can be `nil/null`.

#### InfoGetCategories

Method returns an information about plugin categories.
This information is used by Plugins Manager only for grouping purposes in the list of plugins
Method must not require the plugin initialization.

- `out` **Result** — `DWORD`
  One or combination of following flags:
  - AIMP_PLUGIN_CATEGORY_ADDONS
  - AIMP_PLUGIN_CATEGORY_DECODERS
  - AIMP_PLUGIN_CATEGORY_VISUALS
  - AIMP_PLUGIN_CATEGORY_DSP

#### Initialize

- `in` **Core** — `IAIMPCore`
  Reference to the basic interface
- `out` **Result** — `HRESULT`
  S_OK - if success, other value otherwise.

  Note that plugin can be loaded by Audio Converter or Tag Editor tool. You should check on plugin initialization if all required built-in services are available. If some services are not available plugin may return an error code - AIMP will mark this plugin as unused.

  At this moment, the "current folder" of the OS refers to the plugin folder. You can use the "current folder" to determine where exactly your plugin is placed.

  Refer to the "Guidelines for working with services"

#### Finalize

This method will be called before unload the plugin library.
Note that method will not be called if the Initialize method return value different from S_OK.

#### SystemNotification

Handler of system notifications
Refer to the "Guidelines for working with services"

- `in` **NotifyID** — `Integer`
  Notification ID.
  Can be one of following values:
  - AIMP_SYSTEM_NOTIFICATION_SERVICE_ADDED
  - AIMP_SYSTEM_NOTIFICATION_SERVICE_REMOVED
  - AIMP_SYSTEM_NOTIFICATION_EXTENSION_REMOVED
- `in` **Data** — `IUnknown`
  Changing object. Can be `nil / null`;

### Remark

If plugin has external settings dialog, it should implement the IAIMPExternalSettingsDialog interface on same to IAIMPPlugin interface level.

### Creating the instance

```
function AIMPPluginGetHeader(out Header: IAIMPPlugin): HRESULT; stdcall;
```

### Interface definition

Interface definition is located in the apiPlugin.pas / apiPlugin.h

### See also

- Access to services
- Where plugin must store user settings?
- Guidelines for working with services

## IAIMPExternalSettingsDialog

### Description

If plugin has external settings dialog that not integrated in the application via Options Dialog API, it should implement this interface on same to IAIMPPlugin interface level.

### Methods

#### Show

This method should execute modal dialog.

- `in` **ParentWindow** — `HWND`
  Handle of calling window.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.

### Summary

- **Definition:** apiPlugin.pas / apiPlugin.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455
