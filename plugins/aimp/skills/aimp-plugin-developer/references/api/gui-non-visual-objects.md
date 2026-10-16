# Non-visual objects

## Non-visual objects

- IAIMPUIFont
- IAIMPUIMode
- IAIMPUIImageList
- IAIMPUIImageList3
- IAIMPUIPopupMenu
- IAIMPUIPopupMenu2
- IAIMPUITrayIcon

## IAIMPUIFont

### Description

IAIMPUIFont provides access to font parameters.

### Properties

#### AIMPUI_FONT_PROPID_NAME

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMPUI_FONT_PROPID_COLOR

Font color in ARGB format (alpha-channel is ignored)

- **Type:** Int64
- **Read:** IAIMPPropertyList.GetValueAsInt64
- **Write:** IAIMPPropertyList.SetValueAsInt64

#### AIMPUI_FONT_PROPID_SIZE

Size in points for 96 dpi.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_FONT_PROPID_STYLE

Font Styles.
0 or combination of following flags:
`
+ AIMPUI_FLAGS_FONT_BOLD
+ AIMPUI_FLAGS_FONT_ITALIC
+ AIMPUI_FLAGS_FONT_STRIKEOUT
+ AIMPUI_FLAGS_FONT_UNDERLINE`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_FONT_PROPID_SPECS

All font parameters presented in single string line.
May be useful for storing/restoring from/to configuration file.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### Creating the instance

You can take a reference to the interface via <IAIMPServiceUI>.QueryInterface.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPUIMode

### Description

IAIMPUIMode provides an access to UI display settings.

### Properties

#### AIMPUI_MODE_PROPID_ACCENT

Accent Color, in the ARGB format, 0 - accent is not specified.
We recommend to use the IAIMPUIColorSchema for easy and correct theming.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### AIMPUI_MODE_PROPID_DPI

Custom scaling factor of app's UI, in dpi (96 dpi = 100%).
0 - if custom scaling factor is not set, actual scaling factor must be calculated according to OS settings.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### AIMPUI_MODE_PROPID_STYLE

Can determine displaying style (Day or Night).
Can be one of the following values: `AIMPUI_STYLE_LIGHT` / `AIMPUI_STYLE_DARK`.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

### Creating the instance

You can take a reference to the interface via <IAIMPServiceUI>.QueryInterface.

### Notifications

On change the UI display settings, framework will broadcast the AIMP_MSG_EVENT_UI_MODE message.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 5.30.2500

### See Also

- Hook Messages

## IAIMPUIImageList

### Description

IAIMPUIImageList is container for images for controls.

**WARNING: Deprecated since v6.0. Use IAIMPUIImageList3 instead.**

### Methods

#### Add

- `in` **Image** — `IAIMPImage`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Clear

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Delete

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Draw

- `in` **DC** — `HCANVAS`
- `in` **Index** — `Integer`
- `in` **X** — `Integer`
- `in` **Y** — `Integer`
- `in` **Enabled** — `LongBool`
  If the Enabled variable is set to False, the image will be drawn in gray scale.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### LoadFromResource

Deprecated, for Windows OS only. Use IAIMPUIImageList3.LoadFromStream instead

- `in` **Instance** — `HMODULE`
  A handle to the module that contains the resource
- `in` **ResName** — `PChar`
- `in` **ResType** — `PChar`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetCount

- `out` **Result** — `Integer`

#### GetSize

- `out` **Size** — `TSize`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### SetSize

Note that all already added images will be deleted from the list

- `in` **Size** — `TSize`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateObject method.
Control will be destroyed automatically with IAIMPUIForm that contains the control.

### DPI Aware

The IAIMPDPIAware interface are supported. It provides information about source DPI of the images in list.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPUIImageList3

### Description

IAIMPUIImageList3 is container for images for controls.

### Properties

#### AIMPUI_IMAGELIST_PROPID_ALLOWCOLORATION

Specifies whether the color scheme will be applied to images in the list or not.
0 - color scheme will NOT be applied. Default: 1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### Methods

#### Add

- `in` **Image** — `IAIMPImage`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Clear

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Delete

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Draw

- `in` **DC** — `HCANVAS`
- `in` **Index** — `Integer`
- `in` **X** — `Integer`
- `in` **Y** — `Integer`
- `in` **Enabled** — `LongBool`
  If the Enabled variable is set to False, the image will be drawn in gray scale.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### DrawEx

- `in` **DC** — `HCANVAS`
- `in` **Index** — `Integer`
- `in` **R** — `Rect`
- `in` **Enabled** — `LongBool`
  If the Enabled variable is set to False, the image will be drawn in gray scale.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetCount

- `out` **Result** — `Integer`

#### GetImage

Extracts an image from the image list

- `in` **Index** — `Integer`
- `in` **Enabled** — `LongBool`
  If the Enabled variable is set to False, the image will be drawn in gray scale.
- `out` **Image** — `IAIMPImage`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetSize

- `out` **Size** — `TSize`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### SetSize

Note that all already added images will be deleted from the list

- `in` **Size** — `TSize`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### LoadFromStream

- `in` **Stream** — `IAIMPStream`
  Stream must contains an image in JPG, PNG or BMP format.
  Image List will slice the image to frames automatically according to specified width and height.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateObject method.
Control will be destroyed automatically with IAIMPUIForm that contains the control.

### DPI Aware

The IAIMPDPIAware interface are supported. It provides information about source DPI of the images in list.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPUIPopupMenu

### Description

IAIMPUIPopupMenu is non-visual element that provides an ability to create context menus.

### Parent

IAIMPPropertyList — IAIMPUIPopupMenu

### Methods

#### Add

- `in` **ID** — `IAIMPString`
  Unique ID, used for automatic localization.
- `out` **MenuItem** — `IAIMPUIMenuItem`
  Newly created menu item
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Delete

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Get

Method provides an access to children menu item by it index

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  ID of object.
- `out` **MenuItem** — ``
  Object interface
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetCount

- `out` **Result** — `Integer`
  Count of children menu items

#### Popup

- `in` **ScreenPoint** — `TPoint`
  Show menu at specified point.

  Note that point must be defined in screen system of coordinates
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Popup2

- `in` **ScreenRect** — `TRect`
  Show menu under specified rectangle, and does not intersects it under any circumstances.

  Note that rectangle must be defined in screen system of coordinates
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Events

IAIMPUIPopupMenuEvents (or IAIMPUIChangeEvents if first is not specified) fires before show the menu

### Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateObject method.
Component will be destroyed automatically with IAIMPUIForm that contains the control.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

### IAIMPUIMenuItem

#### Description

IAIMPUIMenuItem is a extended version of the IAIMPMenuItem interface. Unlike the ancestor, the IAIMPUIMenuItem interface not requires to create and register via special service of player - each menu item is created via the Add method of the parent.

#### Parent

IAIMPPropertyList — IAIMPMenuItem — IAIMPUIMenuItem

#### Methods

##### Add

- `in` **ID** — `IAIMPString`
  Unique ID, used for automatic localization.
- `out` **MenuItem** — `IAIMPUIMenuItem`
  Newly created menu item
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### Delete

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### Get

Method provides an access to children menu item by it index

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  ID of object.
- `out` **MenuItem** — ``
  Object interface
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetCount

- `out` **Result** — `Integer`
  Count of children menu items

## IAIMPUIPopupMenu2

### Parent

IAIMPPropertyList — IAIMPUIPopupMenu — IAIMPUIPopupMenu2

### Methods

#### PopupFromCursor

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateObject method.
Component will be destroyed automatically with IAIMPUIForm that contains the control.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPUITrayIcon

### Description

IAIMPUITrayIcon provides plugin an ability to create it own icon in notification area.

### Parent

IAIMPPropertyList — IAIMPUITrayIcon

### Properties

#### AIMPUI_TRAYICON_PROPID_ID

ID, used by Windows to customize and store notification settings.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMPUI_TRAYICON_PROPID_HINT

Hint that displayed when mouse pointer inside the icon are.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMPUI_TRAYICON_PROPID_ICON

Pass the `nil/null` as argument to use app icon (default)

- **Type:** IAIMPImage, IAIMPImageContainer, IAIMPStream
- **Read:** Unavailable
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, ..)

#### AIMPUI_TRAYICON_PROPID_VISIBLE

0 - hidden (default).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### Methods

#### Notify

Displays message in notification area.
Click the icon/notification will fire the IAIMPUIChangeEvents events.

- `in` **Title** — `IAIMPString`
  Title
- `in` **Message** — `IAIMPString`
  Text Message
- `in` **Flags** — `DWORD`
  One of following flags:

  - `AIMPUI_TRAYICON_NOTIFY_FLAGS_INFO`
  - `AIMPUI_TRAYICON_NOTIFY_FLAGS_ERROR`
  - `AIMPUI_TRAYICON_NOTIFY_FLAGS_WARNING`
- `in` **Events** — `IUnknown`
  Click by notification will invoke the IAIMPUIChangeEvents if it implemented by the Events
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateObject method.
Component will be destroyed automatically with IAIMPUIForm that contains the control.

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 5.40.2660
