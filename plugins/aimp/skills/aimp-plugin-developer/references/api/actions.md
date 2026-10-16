# Actions

## Actions

- IAIMPServiceActionManager
- IAIMPAction
- IAIMPActionEvent

## IAIMPServiceActionManager

### Description

The service provides an access to actions.

### Methods

#### GetByID

- `in` **ID** — `IAIMPString`
  Action ID, see IAIMPAction
- `out` **Action** — `IAIMPAction`
  Action
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### MakeHotkey

This is tool method that helps you to create hotkey code

- `in` **Modifiers** — `Word`
  Combination of following flags:
  - AIMP_ACTION_HOTKEY_MODIFIER_CTRL
  - AIMP_ACTION_HOTKEY_MODIFIER_ALT
  - AIMP_ACTION_HOTKEY_MODIFIER_SHIFT
  - AIMP_ACTION_HOTKEY_MODIFIER_WIN Warning! The AIMP_ACTION_HOTKEY_MODIFIER_WIN modifier is supported for global hotkeys only.
- `in` **Key** — `Word`
  Virtual key code, see the VK_XXX constants from the Windows SDK.
- `out` **Result** — `Integer`
  Hotkey code

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceActionManager, ...);

### Example

Example is located on the `Demos \ MenuAndActionsDemo`

### Summary

- **Definitions:** apiActions.pas / apiActions.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

## IAIMPAction

### Description

Main feature of Action is an ability to display it in hotkey list, and provide an ability to customize it hotkey.

### Parent

IAIMPAction is inherited from the IAIMPPropertyList.

### Properties

#### AIMP_ACTION_PROPID_CUSTOM

This is a user data parameter, it allow you to bind custom data to the interface.

- **Type:** IUnknown
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IUnknown, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IUnknown>)

#### AIMP_ACTION_PROPID_ID

Unique action identificator, must be unique for all plugins!

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_ACTION_PROPID_NAME

Command name, value is displaying in the hotkey list

Refer to the automatic localization article

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_ACTION_PROPID_GROUPNAME

Group name, used to display the command in the hotkey list.

Refer to the automatic localization article

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_ACTION_PROPID_ENABLED

Action state: 0 - unaccessible, any other value otherwise

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_ACTION_PROPID_DEFAULTLOCALHOTKEY

Default local hotkey, can be 0 (see IAIMPServiceActionManager.MakeHotkey)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_ACTION_PROPID_DEFAULTGLOBALHOTKEY

Default global hotkey, can be 0 (see IAIMPServiceActionManager.MakeHotkey)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_ACTION_PROPID_DEFAULTGLOBALHOTKEY2

Default alternative global hotkey, can be 0 (see IAIMPServiceActionManager.MakeHotkey)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_ACTION_PROPID_EVENT

Execute handler.
The Data parameter of the IAIMPActionEvent handler will be equals to the interface of invoking action as IAIMPAction

- **Type:** IAIMPActionEvent
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPActionEvent, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPActionEvent>)

### Displaying in hotkey list

Only actions with non-empty `AIMP_ACTION_PROPID_ID`, `AIMP_ACTION_PROPID_NAME` and `AIMP_ACTION_PROPID_GROUPNAME` are listed in hotkey list.

### Creating the instance

Instance of interface must be created via <IAIMPCore>.CreateObject(IID_IAIMPAction, ...) method during plugin initialization. After creating, plugin should populate all required properties and register the action via <IAIMPCore>.RegisterExtension(IID_IAIMPServiceActionManager, <IAIMPAction>) method. Action will be automatically unregistered before plugin finalization.

### Summary

- **Definitions:** apiActions.pas / apiActions.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- Automatic localization
- Property list name conversion

## IAIMPActionEvent

### Description

This interface is simple event handler.

### Methods

#### OnExecute

- `in` **Data** — `IUnknown`
  Additional data, it is defined by calling side. Parameter can be `nil / null`.

### Creating the instance

Instance should be created by plugin and set into the IAIMPAction via AIMP_ACTION_PROPID_EVENT property.

### Summary

- **Definitions:** apiActions.pas / apiActions.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455
