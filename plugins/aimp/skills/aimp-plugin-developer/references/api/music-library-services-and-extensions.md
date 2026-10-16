# Services and Extensions

## Services and Extensions

- IAIMPServiceMusicLibrary
- IAIMPServiceMusicLibraryUI
- IAIMPMLExtensionDataStorage

## IAIMPServiceMusicLibrary

### Description

The IAIMPServiceMusicLibrary service provides an access to data storages of Music Library

### Methods

#### GetActiveStorage

Method returns an instance of interface of ActiveStorage by IID

- `in` **IID** — `TGUID`
  IID of requested interface.
  Use the IID_IAIMPMLDataStorage to access to common properties for all data storages.
  Use the IID_IAIMPMLGroupingPresets to access to presets for grouping tree.
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### SetActiveStorage

- `in` **Storage** — `IUnknown`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetStorage

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  IID of requested interface.
  Use the IID_IAIMPMLDataStorage to access to common properties for all data storages.
  Use the IID_IAIMPMLGroupingPresets to access to presets for grouping tree.
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetStorageByID

- `in` **ID** — `IAIMPString`
  Storage ID.

  Refer to the AIMPML_DATASTORAGE_PROPID_ID for more information.

  Use the AIMPML_LOCALDATASTORAGE_ID constant to get an access to local data storage.
- `in` **IID** — `TGUID`
  IID of requested interface.
  Use the IID_IAIMPMLDataStorage to access to common properties for all data storages.
  Use the IID_IAIMPMLGroupingPresets to access to presets for grouping tree.
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetStorageCount

- `out` **Result** — `Integer`

### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceMusicLibrary, ...);

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Extensions:** IAIMPMLExtensionDataStorage
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPServiceMusicLibraryUI

### Description

The IAIMPServiceMusicLibraryUI service provides an access to data of UI elements for an active data storage that uses by the user.

### Methods

#### GetFiles

Returns file list from table view

- `in` **Flags** — `DWORD`
  One of the following flags:
  AIMPML_GETFILES_FLAGS_ALL
  AIMPML_GETFILES_FLAGS_SELECTED
  AIMPML_GETFILES_FLAGS_FOCUSED
- `out` **List** — `IAIMPMLFileList`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetGroupingFilter

- `out` **Filter** — `IAIMPMLDataFilter`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetGroupingFilterPath

- `out` **Path** — `IAIMPString`
  Returns presentation of grouping filter like a file path. Node separates by the "/" or "\" symbols (depended from source data).
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### SetGroupingFilterPath

Method provides an ability to move focus to other grouping tree node.

- `in` **Path** — `IAIMPString`
  Presentation of grouping filter like a file path.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceMusicLibraryUI, ...);

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPMLExtensionDataStorage

### Description

The extension for the IAIMPServiceMusicLibrary service provides an ability to plugin to implement custom data storage for the Music Library.

Interface implementation must support asynchronous access.

### Parent

IAIMPMLExtensionDataStorage inherits from IAIMPPropertyList

### Properties

#### AIMPML_DATASTORAGE_PROPID_ID

Global unique ID of the data storage

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

#### AIMPML_DATASTORAGE_PROPID_CAPTION

User friendly name of data storage

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

#### AIMPML_DATASTORAGE_PROPID_CAPABILITIES

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

### Methods

#### Initialize

Method calls after succeeded registration of data storage.

- `in` **Manager** — `IAIMPMLDataStorageManager`
  The Manager interface is used to notify the Music Library about the changes in data storage.

#### Finalize

Method calls before the finalization of plugin. Plugin must release all external links.

#### FlushCache

Method calls when user executes the "refresh" command via hotkey or context menu. After this call the Music Library engine will automatically reload the data from data storage.

- `in` **Reserved** — `Integer`
  Reserved, must be set to 0

#### ConfigLoad

Warning: method will be called on first activation of tab of data storage in Music Library interface

- `in` **Config** — `IAIMPConfig`
- `in` **Section** — `IAIMPString`
  Section Name to that contains the settings.
  You can use the children section names if it needed: Section + "." + ChildSectionName
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### ConfigSave

- `in` **Config** — `IAIMPConfig`
- `in` **Section** — `IAIMPString`
  Section Name to store the settings.
  You can use the children section names if it needed: Section + "." + ChildSectionName
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### GetFields

Method returns settings and layout of the data fields in dependency from specified Schema value.

- `in` **Schema** — `Integer`
  One of the following values:
  - `AIMPML_FIELDS_SCHEMA_ALL` - list of all available fields in data storage. List must contains an IAIMPMLDataField objects
  - `AIMPML_FIELDS_SCHEMA_TABLE_GROUPBY` - list of fields that used for grouping in table. If list is empty - the Group Details and the Album Thumbnails views will not be available for the end user. List of IAIMPString that contains a field names only
  - `AIMPML_FIELDS_SCHEMA_TABLE_GROUPDETAILS` - list of fields that displays in group details area. List of IAIMPString that contains a field names only
  - `AIMPML_FIELDS_SCHEMA_TABLE_VIEW_DEFAULT` - list of fields that displays to end user in table by default in Default view. List of IAIMPString that contains a field names only
  - `AIMPML_FIELDS_SCHEMA_TABLE_VIEW_GROUPDETAILS` - list of fields that displays to end user in table by default in Group Details view. List of IAIMPString that contains a field names only
  - `AIMPML_FIELDS_SCHEMA_TABLE_VIEW_ALBUMTHUMBNAILS` - list of fields that displays to end user in table by default in Album Thumbnails view. List of IAIMPString that contains a field names only
  **Warning!**
  Data storage MUST contains a fields with following names:
  - `AIMPML_RESERVED_FIELD_ID` - unique ID of record in data storage
  - `AIMPML_RESERVED_FIELD_FILENAME` - file name of the record that used by player If this fields are not defined in Data Storage - registration of the extension will be failed.

  Also, the Music Library engine provides an ability to use following special fields:
  - `AIMPML_RESERVED_FIELD_FILESIZE` - file size in bytes (type: Int64), used to calculate information about the content of table
  - `AIMPML_RESERVED_FIELD_DURATION` - duration in seconds (type: Double) ,used to calculate information about the content of table
  - `AIMPML_RESERVED_FIELD_USERMARK` - user rating mark (type: Double), Refer to the IAIMPMLDataStorageCommandUserMark
- `out` **List** — `IAIMPObjectList`
  List of the IAIMPMLDataField or IAIMPString in dependency from specified Schema.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### GetGroupingPresets

Plugin must populate the Presets list by predefined presets for grouping tree based on the Schema value.

- `in` **Schema** — `Integer`
  One of the following values:
  - `AIMPML_GROUPINGPRESETS_SCHEMA_BUILTIN` - built-in presets (cannot be deleted or edited by user)
  - `AIMPML_GROUPINGPRESETS_SCHEMA_DEFAULT` - predefined user presets (can be removed or customized by user)
  **Warning!**
  Plugin must add least one built-in preset.
- `in` **Presets** — `IAIMPMLGroupingPresets`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### Commands (IAIMPMLCommands)

#### Description

Commands is an special extensions for the IAIMPMLExtensionDataStorage that let know to music library engine what commands are supported

Implementation of the commands must be in same level as implementation of the IAIMPMLExtensionDataStorage interface.

#### IAIMPMLDataStorageCommandAddFiles

##### Methods

###### Add

- `in` **Files** — `IAIMPObjectList`
  List of the filenames like a IAIMPString object
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLDataStorageCommandAddFilesDialog

##### Methods

###### Execute

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLDataStorageCommandDeleteFiles

##### Methods

###### CanDelete

- `in` **Physically** — `LongBool`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

###### Delete

- `in` **Files** — `IAIMPMLFileList`
- `in` **Physically** — `LongBool`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLDataStorageCommandDeleteFiles2

##### Description

General case of the IAIMPMLDataStorageCommandDeleteFiles command.
Provides an ability to delete files by user specified filter. Note that data storage must support for filtering on own side - refer to the AIMPML_DATASTORAGE_PROPID_CAPABILITIES property.

##### Parent

IAIMPMLDataStorageCommandDeleteFiles2 inherits from IAIMPMLDataStorageCommandDeleteFiles

##### Methods

###### Delete2

- `in` **Filter** — `IAIMPMLDataFilter`
- `in` **Physically** — `LongBool`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLDataStorageCommandDropData

##### Description

Command removes all data from data storage.
The confirmation dialog must be implemented on data storage side.

##### Methods

###### DropData

- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLDataStorageCommandFindInLibrary

##### Description

Command helps player to find file specified by user in music library.
If the file contains in plugin's data storage, plugin must initialize output parameters and return S_OK as result of following method.

##### Methods

###### Find

- `in` **FileInfo** — `IAIMPFileInfo`
  Information about the file to find in music library.
- `out` **GroupingPresetID** — `IAIMPString`
  ID of grouping tree preset that must be selected to apply the `GroupingTreeSelection`.
  Return the `nil/null` if file can be located using current grouping tree preset.
- `out` **GroupingTreeSelection** — `IAIMPMLGroupingTreeSelection`
  Path to grouping tree node that contains the file.
  Return the `nil/null` or empty selection to select root of grouping tree.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2300

#### IAIMPMLDataStorageCommandReloadTags

##### Methods

###### ReloadTags

- `in` **Files** — `IAIMPMLFileList`
  List of filenames like a IAIMPString objects.
  Files can be set to `nil/null` - in this case storage must reload tags for all files.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLDataStorageCommandReportDialog

##### Methods

###### Execute

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLDataStorageCommandUserMark

##### Description

This command is handler for data field with the `AIMPML_RESERVED_FIELD_USERMARK` reserved name.

##### Methods

###### SetMark

- `in` **ID** — `VarValue`
  ID of the changing record.
- `in` **Value** — `Double`
  Rating mark, 0.0 .. 5.0
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLAlbumArtProvider

This extension was deprecated, use the IAIMPMLAlbumArtProvider2 instead.

### IAIMPMLAlbumArtProvider2

#### Description

This interface implements image provider for group details and thumbnails in music library that provided via plugin. Unlike IAIMPServiceAlbumArt this provider works with unique data from the music library.

The interface must be implemented by plugin on same level as the IAIMPMLExtensionDataStorage interface.

Interface implementation must support asynchronous access.

#### Methods

##### Get

- `in` **Fields** — `IAIMPObjectList`
  List of field names presented as IAIMPString that contains a `AIMPML_FIELDFLAG_REQUIRED` flag in the AIMPML_FIELD_PROPID_FLAGS property value.
- `in` **Values** — `PVarValue`
  Pointer to first element of the VarValue array. Size of array is same value of the Fields.GetCount method result.
  Contains values for the Fields based on first file in group.
- `in` **Request** — `IAIMPAlbumArtRequest`
  Search options, refer to the properties of the IAIMPServiceAlbumArt service topic for more information.

  **Attention**! You must check the current options before start the search. Extension must return the E_FAIL code if options does not match to the requirements for search.

  Here is a small example that show how to interact with IAIMPAlbumArtRequest. The example downloads the image that defined as URL in corresponding tag field:

  ```
  function Get(FileInfo: IAIMPFileInfo; Request: IAIMPAlbumArtRequest; out Image: IAIMPImageContainer): HRESULT; stdcall;
  var
  ALink: IAIMPString;
  begin
  Result := E_FAIL;
  // Is file info has a url?
  if PropListGetStr(FileInfo, AIMP_FILEINFO_PROPID_URL, ALink) then
  begin
  // Is image url?
  if IsImageURL(ALink) then
  begin
  // Is image already cached?
  if Succeeded(Request.CacheGet(ALink, Image)) then
  Exit(S_OK);

  // Download the image
  // The Download function will consider values of the
  // AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET and AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET_MAX_FILE_SIZE options
  if Succeeded(Request.Download(ALink, Image)) then
  begin
  // Optimize the image and cache it
  Request.CachePut(ALink, Image);
  Result := S_OK;
  end;
  end;
  end;
  end;
  ```
- `out` **Image** — `IAIMPImageContainer`
  Image for the group
- `out` **Result** — `HRESULT`
  S_OK - if operation successfully completed
  E_FAIL - if error occured or provider has no image for the group
  E_NOTIMPL - provider does not work, player will turn to IAIMPServiceAlbumArt service

#### Summary

- **Definitions:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 5.02.2360

### IAIMPMLDataStorageManager

#### Description

The interface provides an ability to notify music library about the changes in data storage.
Instance of interface creates by music library manager and put to plugin via the IAIMPMLExtensionDataStorage.Initialize method.

#### Methods

##### BackgroundTaskStarted

The BackgroundTaskStarted / BackgroundTaskFinished methods provides an ability to notify the Music Library manager about running a background tasks that related to the data storage.

Note 1: the first of background tasks will be displayed to end user (this ability is depended from the skin).
Note 2: both of functions must be called from main thread.

- `in` **ID** — `Integer`
  Unique ID of background task.
- `in` **Caption** — `IAIMPString`
  Text that will be displayed to end user.

  You can change the content of this variable during execution of the background task. Note that the changes will be displayed on the screen with small delay.
- `in` **CancelEvent** — `IAIMPActionEvent`
  Cancel button handler.
  Put the `nil/null` to disable an ability to cancel this task.

##### BackgroundTaskFinished

- `in` **ID** — `Integer`
  Unique ID of background task

##### Changed

Notifies the manager that data in data storage has been changed. This reloads the data in all views of Music Library and smart-playlists.

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLDataProvider

#### Description

Provides an access to data in data storage. Must be implemented by plugin on same level as the IAIMPMLExtensionDataStorage interface.

You must use the IAIMPMLDataProvider2 instead of this interface if you data storage uses the page-by-page access method.

Interface implementation must support asynchronous access.

#### Methods

##### GetData

- `in` **Fields** — `IAIMPObjectList`
  List of field names that requires the data.
  List populates automatically in dependency what fields are used by user or marked as required.
- `in` **Filter** — `IAIMPMLDataFilter`
  Plugin **must** take it into account, if the `AIMPML_DATASTORAGE_CAP_FILTERING` flag is defined in the AIMPML_DATASTORAGE_PROPID_CAPABILITIES property value.
- `out` **Data** — `IUnknown`
  Must implement one or both interfaces:
  - IAIMPMLDataProviderSelection
  - IAIMPString - text information that displays to user in table of Music Library (formatting via simple BB codes are supported).
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLDataProvider2

##### Description

Provides an access to data in data storage. Must be implemented by plugin on same level as the IAIMPMLExtensionDataStorage interface.

You must use this interface instead of the IAIMPMLDataProvider if you data storage uses the page-by-page access method.

Interface implementation must support asynchronous access.

##### Methods

###### GetData

- `in` **Fields** — `IAIMPObjectList`
  List of field names that requires the data.
  List populates automatically in dependency what fields are used by user or marked as required.
- `in` **Filter** — `IAIMPMLDataFilter`
  Plugin **must** take it into account, if the `AIMPML_DATASTORAGE_CAP_FILTERING` flag is defined in the AIMPML_DATASTORAGE_PROPID_CAPABILITIES property value.
- `in` **Reserved** — `IUnknown`
  Reserved for future usage. Now always set to `nil / null`.
- `var` **PageID** — `IUnknown`
  Argument is used to page-by-page navigation if data storage supports it.

  Input:
  ID of page to read the data, the `nil / null` value points to first page.

  Output:
  ID of next page if it exists or `nil / null` otherwise;
- `out` **Data** — `IUnknown`
  Must implement one or both interfaces:
  - IAIMPMLDataProviderSelection
  - IAIMPString - text information that displays to user in table of Music Library (formatting via simple BB codes are supported).
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.60.2160

#### IAIMPMLDataProviderSelection

##### Description

Provides an access to current data set that has been returned by the IAIMPMLDataProvider.

Interface implementation must support asynchronous access.

##### Methods

###### GetValueAsFloat

- `in` **FieldIndex** — `Integer`
- `out` **Result** — `Double`

###### GetValueAsInt32

- `in` **FieldIndex** — `Integer`
- `out` **Result** — `Double`

###### GetValueAsInt64

- `in` **FieldIndex** — `Integer`
- `out` **Result** — `Double`

###### GetValueAsString

- `in` **FieldIndex** — `Integer`
- `out` **Length** — `Integer`
- `out` **Result** — `PChar`

###### NextRow

Jumps to next row. Returns False if current row is last.

- `out` **Result** — `LongBool`

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLGroupingTreeDataProvider

#### Description

Interface provides an ability to specify custom data provider for a grouping tree.

Interface implementation must support asynchronous access.

#### Methods

##### AppendFilter

Plugin must build the data filter for table based on current Selection.

- `in` **Filter** — `IAIMPMLDataFilterGroup`
- `in` **Selection** — `IAIMPMLGroupingTreeSelection`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### GetCapabilities

- `out` **Result** — `DWORD`
  0 or combination of following flags:

  - AIMPML_GROUPINGTREEDATAPROVIDER_CAP_HIDEALLDATA - hide the "(show all)" node in grouping tree
  - AIMPML_GROUPINGTREEDATAPROVIDER_CAP_DONTSORT - disable auto sorting in grouping tree

##### GetData

Returns the data for next level of selected node in grouping tree

- `in` **Selection** — `IAIMPMLGroupingTreeSelection`
- `out` **Data** — `IAIMPMLGroupingTreeDataProviderSelection`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### GetFieldForAlphabeticIndex

- `in` **FieldName** — `IAIMPString`
  Returns the name of top level field for alphabetic index.
  Note: Return the E_FAIL code if your top level nodes uses different fields, because alphabetic index cannot be used in this case.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

  If result is differs from S_OK - alphabetic index will not available for end user.

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### See Also

- IAIMPMLExtensionDataStorage.GetGroupingPresets
- IAIMPMLGroupingPreset

#### IAIMPMLGroupingTreeDataProviderSelection

##### Description

Interface provides an access to data from the IAIMPMLGroupingTreeDataProvider.GetData.

Interface implementation must support asynchronous access.

##### Methods

###### GetDisplayValue

Returns text to display to end user (optionally)

- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

  If result is differs from S_OK - display text will be calculated automatically based on type of field.

###### GetFlags

- `out` **Result** — `DWORD`
  0 or combination of following flags:

  - `AIMPML_GROUPINGTREENODE_FLAG_HASCHILDREN`
  - `AIMPML_GROUPINGTREENODE_FLAG_STANDALONE` - refer to the IAIMPMLGroupingTreeSelection

###### GetImageIndex

- `out` **ImageIndex** — `Integer`
  Image index for grouping tree:
  - AIMPML_FIELDIMAGE_FOLDER
  - AIMPML_FIELDIMAGE_ARTIST
  - AIMPML_FIELDIMAGE_DISK
  - AIMPML_FIELDIMAGE_NOTE
  - AIMPML_FIELDIMAGE_STAR
  - AIMPML_FIELDIMAGE_CALENDAR
  - AIMPML_FIELDIMAGE_LABEL
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

###### GetValue

- `out` **FieldName** — `IAIMPString`
- `out` **Value** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

###### NextRecord

Jumps to the next record. Returns False if current node is last.

- `out` **Result** — `LongBool`

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### IAIMPMLGroupingTreeSelection

##### Description

Interface provides an access to selected nodes in grouping tree.

First element in the Selection is focused node. If current node does not have the `AIMPML_GROUPINGTREENODE_FLAG_STANDALONE` flag - the parent node will be added to Selection. Algorithm running until root or node with the `AIMPML_GROUPINGTREENODE_FLAG_STANDALONE` flag.

##### Methods

###### GetCount

- `out` **Result** — `Integer`

###### GetValue

- `in` **Index** — `Integer`
- `out` **FieldName** — `IAIMPString`
- `out` **Value** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLGroupingTreeDataProvider2

#### Description

IAIMPMLGroupingTreeDataProvider2 is an optional extension of IAIMPMLGroupingTreeDataProvider interface.

#### Methods

##### GetPathSeparator

- `out` **Result** — `Char`
  Specifies delimiter character used for build grouping tree path.

  Native path delimiter will be used if plugin does not implement the interface.

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.70.2215

#### See Also

- IAIMPMLGroupingTreeDataProvider
