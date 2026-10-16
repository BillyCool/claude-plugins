# Menu

## Menu

- IAIMPServiceMenuManager
- IAIMPMenuItem

## IAIMPServiceMenuManager

### Description

The service provides an access to already created menu items.

### Methods

#### GetBuiltIn

Method returns an interface instance for built-in menu items

- `in` **ID** — `Integer`
  Following ID are supported:

  Yellow markers means that new item will added to specified place. Red - into the end of sub menu.

  AIMP_MENUID_PLAYER_EQ_LIB - context menu with equalizer settings.

  AIMP_MENUID_PLAYER_STOP_OPTIONS - context menu of the "stop playback" button. Note: Introduced in v4.00.1691
- `out` **MenuItem** — `IAIMPMenuItem`
  Interface instance for specified menu item. Read only.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetByID

- `in` **ID** — `IAIMPString`
  Unique menu item ID. See AIMP_MENUITEM_PROPID_ID
- `out` **MenuItem** — `IAIMPMenuItem`
  Interface instance for specified menu item
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceMenuManager, ...);

### Example

Example is located in the `Demos \ MenuAndActionsDemo`

### Summary

- **Definitions:** apiMenu.pas / apiMenu.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- Adding custom menu item

## IAIMPMenuItem

### Description

IAIMPMenuItem describes an menu item.

### Parent

IAIMPMenuItem is inherited from IAIMPPropertyList.

### Properties

#### AIMP_MENUITEM_PROPID_CUSTOM

This is a user data parameter, it allow you to bind custom data to the interface.

- **Type:** IUnknown
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IUnknown, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IUnknown>)

#### AIMP_MENUITEM_PROPID_ACTION

This property provides an ability to link menu item with action.
In this case, menu item will inherits the `AIMP_MENUITEM_PROPID_NAME`, `AIMP_MENUITEM_PROPID_ENABLED`, `AIMP_MENUITEM_PROPID_EVENT` properties values from the action.

- **Type:** IAIMPAction
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPAction, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(.., IID_IAIMPAction, ..)

#### AIMP_MENUITEM_PROPID_ID

Unique menu item identification, must be unique for all plugins!

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_MENUITEM_PROPID_CAPTION

Menu item display name

Refer to the automatic localization article

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_MENUITEM_PROPID_HINT

Tooltip text for the menu item _((since v6.0))_

Refer to the automatic localization article.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_MENUITEM_PROPID_CHECKED

State of check mark: 0 - not checked, any other value otherwise
Value is actual only if AIMP_MENUITEM_PROPID_STYLE different from AIMP_MENUITEM_STYLE_NORMAL.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_MENUITEM_PROPID_ENABLED

Action state: 0 - unaccessible, any other value otherwise

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_MENUITEM_PROPID_STYLE

Menu item style, can be one of the following values:
`AIMP_MENUITEM_STYLE_NORMAL`, `AIMP_MENUITEM_STYLE_CHECKBOX` or `AIMP_MENUITEM_STYLE_RADIOBOX`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_MENUITEM_PROPID_EVENT

Click handler

- **Type:** IAIMPActionEvent
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPActionEvent, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPActionEvent>)

#### AIMP_MENUITEM_PROPID_EVENT_ONSHOW

Handler for OnShow event that fired before menu item displays

- **Type:** IAIMPActionEvent
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPActionEvent, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPActionEvent>)

#### AIMP_MENUITEM_PROPID_GLYPH

Menu item glyph (optional)
Note that image must be 32-bit with correct alpha channel.

- **Type:** IAIMPImage
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPImage, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPImage>)

#### AIMP_MENUITEM_PROPID_PARENT

Parent menu item. Refer to the IAIMPServiceMenuManager service.

- **Type:** IAIMPMenuItem
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPMenuItem, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(.., IID_IAIMPMenuItem, ..)

#### AIMP_MENUITEM_PROPID_VISIBLE

Menu item visibility: 0 - hidden, any other value otherwise.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_MENUITEM_PROPID_DEFAULT

Each level of menu can contains only one default item. Default item uses bold font for the text.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_MENUITEM_PROPID_SHORTCUT

Local hotkey for menu item. Cannot be customized by end user.
Refer to the IAIMPServiceActionManager.MakeHotkey
Refer to the IAIMPAction

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_MENUITEM_PROPID_TAG

Field for custom data _((since v6.0))_

- **Type:** Integer (in 32-bit app) / Int64 (in 64-bit app)

### Methods

#### DeleteChildren

Method will call the IAIMPCore.UnregisterExtension method for all sub items.

Refer to the "Removing menu item" remark section for more information about this process.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Creating the instance

Instance must be created via <IAIMPCore>.CreateObject(IID_IAIMPMenuItem, ...) method during plugin initialization. After creating, plugin should populate all required properties and register the action via <IAIMPCore>.RegisterExtension(IID_IAIMPServiceMenuManager, <IAIMPMenuItem>).

### Removing menu item

All menu items will be automatically unregistered before plugin finalization. But if you need to remove menu item during program life time - you should use the IAIMPCore.UnregisterExtension method, that unregistering the menu item and it sub items, and resets the AIMP_MENUITEM_PROPID_PARENT property (to nil / null). To reuse the removed menu item, you must re-initialize it and register in the program.

### Summary

- **Definitions:** apiMenu.pas / apiMenu.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- Automatic localization
- Property list name conversion
