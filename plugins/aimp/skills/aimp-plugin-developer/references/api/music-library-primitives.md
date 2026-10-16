# Primitives

## Primitives

- IAIMPMLDataField
- IAIMPMLDataFieldDisplayValue
- IAIMPMLDataFilter
- IAIMPMLGroupingPresets
- IAIMPMLDataStorage
- IAIMPMLDataStorage2
- IAIMPMLFileList
- IAIMPMLPlaylistPreimage
- IAIMPMLSortDirection

## IAIMPMLDataField

### Description

Provides information about the data field for Music Library.

### Parent

IAIMPMLDataField inherits from IAIMPPropertyList

### Properties

#### AIMPML_FIELD_PROPID_CUSTOM

This is a user data parameter, it allow you to bind custom data to the interface.

- **Type:** IUnknown
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IUnknown, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IUnknown>)

#### AIMPML_FIELD_PROPID_NAME

Internal field name, this values used as unique ID of field in space of current data storage.

Display name for the field gets from the custom localization from the `AIMPML\<FieldName>` key path.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMPML_FIELD_PROPID_TYPE

Field type, one of the following values:
- `AIMPML_FIELDTYPE_INT32`
- `AIMPML_FIELDTYPE_INT64`
- `AIMPML_FIELDTYPE_FLOAT`
- `AIMPML_FIELDTYPE_STRING`
- `AIMPML_FIELDTYPE_STRINGSET` - set of string values divided by ";" character
- `AIMPML_FIELDTYPE_DATETIME` - type equals to AIMPML_FIELDTYPE_FLOAT, display value is formatted data time value (format string is depended from the context)
- `AIMPML_FIELDTYPE_DURATION` - type equals to AIMPML_FIELDTYPE_FLOAT, display value is formatted time value (format string is depended from the context)
- `AIMPML_FIELDTYPE_FILESIZE` - type equals to AIMPML_FIELDTYPE_INT64, display value is formatted file size value (format string is depended from the context)
- `AIMPML_FIELDTYPE_FILENAME` - type equals to AIMPML_FIELDTYPE_STRING, grouping tree split the value by levels by the "\" and "/" characters. Grouping by this field with other fields is not available.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPML_FIELD_PROPID_FLAGS

0 or combination of flags:
- `AIMPML_FIELDFLAG_GROUPING` - is field available for grouping presets
- `AIMPML_FIELDFLAG_FILTERING` - is field available for filtering
- `AIMPML_FIELDFLAG_INTERNAL` - mark field as internal - this field will not display for end user
- `AIMPML_FIELDFLAG_REQUIRED` - mark field as required - this field will be automatically included to data query

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPML_FIELD_PROPID_IMAGE

Image index for grouping tree:
- AIMPML_FIELDIMAGE_FOLDER
- AIMPML_FIELDIMAGE_ARTIST
- AIMPML_FIELDIMAGE_DISK
- AIMPML_FIELDIMAGE_NOTE
- AIMPML_FIELDIMAGE_STAR
- AIMPML_FIELDIMAGE_CALENDAR
- AIMPML_FIELDIMAGE_LABEL

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPML_FIELD_PROPID_DISPLAYVALUE

Provides an ability to specify custom display values provider.

- **Type:** IAIMPMLDataFieldDisplayValue
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPMLDataFieldDisplayValue, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPMLDataFieldDisplayValue>)

### Creating the instance

<IAIMPCore>.CreateObject(IID_IAIMPMLDataField, ...)

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPMLDataFieldDisplayValue

### Description

Providers an ability to customize display value for specified field

### Methods

#### GetDisplayValue

- `in` **Value** — `VarValue`
  Original value.
- `out` **Length** — `Integer`
  Count of elements in Result array
- `out` **Result** — `PChar`
  Customized display value

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPMLDataFilter

### Parent

IAIMPMLDataFilter inherits from IAIMPMLDataFilterGroup

### Properties

#### AIMPML_FILTER_OFFSET

Record count to skip.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPML_FILTER_LIMIT

Max count of records to return. 0 - maximum is not set.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPML_FILTER_SORTBYLIST

Field list.
Each entry of the list must implements least two interfaces: IAIMPString (field name) and IAIMPMLSortDirection (sorting direction).

- **Type:** IAIMPObjectList
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPObjectList, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPObjectList>)

#### AIMPML_FILTER_SORTDIRECTION

One of the following values: `AIMPML_SORTDIRECTION_ASCENDING / AIMPML_SORTDIRECTION_DESCENDING`;

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPML_FILTER_SEARCHSTRING

Search string. Can be `nil / null`.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMPML_FILTER_ALPHABETICINDEX

Code of character in the alphabetic index. 0 - character is not set.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### Methods

#### Assign

Copies the data from Source filter.

Note: source filter must be assigned to same data storage.

- `in` **Source** — `IAIMPMLDataFieldFilter`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Clone

- `out` **Source** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLDataFilterGroup

#### Description

Provides an ability to group few filters

#### Parent

IAIMPMLDataFilterGroup inherits from IAIMPPropertyList2

#### Properties

##### AIMPML_FILTERGROUP_OPERATION

One of the following values::
- `AIMPML_FILTERGROUP_OPERATION_OR` - result = True, if one of the children filters returns True
- `AIMPML_FILTERGROUP_OPERATION_AND` - result = True, if all children filters returns True
- `AIMPML_FILTERGROUP_OPERATION_NOTOR` - result = True, if all children filters returns False
- `AIMPML_FILTERGROUP_OPERATION_NOTAND` - result = True, if one of the children filters returns False

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### Methods

##### Add

Adding the IAIMPMLDataFieldFilter

- `in` **Field** — `IUnknown`
  Field Name, IAIMPString
- `in` **Value1** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `in` **Value2** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `in` **Operation** — `Integer`
  Refer to the IAIMPMLDataFieldFilter
- `out` **Filter** — `IAIMPMLDataFieldFilter`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Add2

Adding the IAIMPMLDataFieldFilterByArray

- `in` **Field** — `IUnknown`
  Field Name, IAIMPString
- `in` **Values** — `PVarValue`
  Pointer to first element of array of the VarValue values.
  The VarValue instance must be released by calling side using theVarValueFree method.
- `in` **Count** — `Integer`
- `out` **Filter** — `IAIMPMLDataFieldFilterByArray`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### AddGroup

Adding the children group

- `out` **Group** — `IAIMPMLDataFilterGroup`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Clear

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Delete

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetChild

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
- `out` **Object** — `Untyped`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetChildCount

- `out` **Result** — `Integer`

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLDataFieldFilter

#### Parent

IAIMPMLDataFieldFilter inherits from IAIMPPropertyList2

#### Properties

##### AIMPML_FIELDFILTER_FIELD

Field name

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMPML_FIELDFILTER_OPERATION

One of the following values::
- `AIMPML_FIELDFILTER_OPERATION_EQUALS`
- `AIMPML_FIELDFILTER_OPERATION_NOTEQUALS`
- `AIMPML_FIELDFILTER_OPERATION_BETWEEN` (for numbers only)
- `AIMPML_FIELDFILTER_OPERATION_LESSTHAN` (for numbers only)
- `AIMPML_FIELDFILTER_OPERATION_LESSTHANOREQUALS` (for numbers only)
- `AIMPML_FIELDFILTER_OPERATION_GREATERTHAN` (for numbers only)
- `AIMPML_FIELDFILTER_OPERATION_GREATERTHANOREQUALS` (for numbers only)
- `AIMPML_FIELDFILTER_OPERATION_CONTAINS` (for text only)
- `AIMPML_FIELDFILTER_OPERATION_BEGINSWITH` (for text only)
- `AIMPML_FIELDFILTER_OPERATION_ENDSWITH` (for text only)
- `AIMPML_FIELDFILTER_OPERATION_ISLASTXDAYS` (for date-time only)
- `AIMPML_FIELDFILTER_OPERATION_DOESNOTCONTAIN` (for text only, _(since v6.00)_ )
Text based operations must be non case sensitive!

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMPML_FIELDFILTER_VALUE1

- **Type:** VarValue
- **Read:** IAIMPPropertyList.GetValueAsVariant(ID, ..)
- **Write:** IAIMPPropertyList.SetValueAsVariant(ID, ..)

##### AIMPML_FIELDFILTER_VALUE2

This value is used if the `AIMPML_FIELDFILTER_OPERATION` property is set to the `AIMPML_FIELDFILTER_OPERATION_BETWEEN` value.

- **Type:** VarValue
- **Read:** IAIMPPropertyList.GetValueAsVariant(ID, ..)
- **Write:** IAIMPPropertyList.SetValueAsVariant(ID, ..)

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLDataFieldFilterByArray

#### Description

The filter is optimized analog of the following expression:

```
(FieldValue = Value1) OR (FieldValue = Value2) OR ... OR (FieldValue = ValueN)
```

#### Parent

IAIMPMLDataFieldFilterByArray inherits from IAIMPPropertyList2

#### Properties

##### AIMPML_FIELDFILTERBYARRAY_FIELD

Field Name

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### Methods

##### GetData

- `in` **Values** — `PVarValue`
  Pointer to first element of the array of VarValue.
  To calculate buffer size for an array put the `nil/null` to this parameter.
  The VarValue instance must be released by calling side using theVarValueFree method.
- `var` **Count** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### SetData

- `in` **Values** — `PVarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `in` **Count** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPMLGroupingPresets

### Description

Provides an access to presets for grouping tree for the specified data storage

### Methods

#### Add

Creates the preset with a custom data provider.
Note that this preset will be determined by the App as Built-in preset - user will not able to edit or delete it.

- `in` **ID** — `IAIMPString`
  Unique preset identificator, must be unique for all plugins!
- `in` **Name** — `IAIMPString`
  Preset name.
  Set the nil/null if the automatic localization is used by ID of preset
- `in` **Reserved** — `DWORD`
  Reserved for future usage, must be set to 0.
- `in` **Provider** — `IAIMPMLGroupingTreeDataProvider`
  Custom data provider for a grouping tree
- `out` **Preset** — `IAIMPMLGroupingPreset`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Add2

Creates the standard preset based on list of fields

- `in` **ID** — `IAIMPString`
  Unique preset identificator, must be unique for all plugins!
- `in` **Name** — `IAIMPString`
  Preset name.
  Set the nil/null if the automatic localization is used by ID of preset
- `in` **Reserved** — `DWORD`
  Reserved for future usage, must be set to 0.
- `in` **FieldNames** — `IAIMPObjectList`
  Field list.
  Each entry of the list must implements least two interfaces: IAIMPString (field name) and IAIMPMLSortDirection (sorting direction).
- `out` **Preset** — `IAIMPMLGroupingPresetStandard`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Add3

Simplified version of the Add2 method - creates the standard preset based on single field

- `in` **ID** — `IAIMPString`
  Unique preset identificator, must be unique for all plugins!
- `in` **Name** — `IAIMPString`
  Preset name.
  Set the nil/null if the automatic localization is used by ID of preset
- `in` **Reserved** — `DWORD`
  Reserved for future usage, must be set to 0.
- `in` **FieldName** — `IAIMPString`
  Field Name like a IAIMPString
- `out` **Preset** — `IAIMPMLGroupingPresetStandard`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### BeginUpdate

Method blocks all notifications about changes until the EndUpdate call.
Recommended for usage in cases when you changing more than one parameter at once.

#### EndUpdate

See the BeginUpdate method notes

#### Delete

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Get

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetByID

- `in` **ID** — `IAIMPString`
  Refer to the AIMPML_GROUPINGPRESET_PROPID_ID
- `in` **IID** — `TGUID`
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetCount

- `out` **Result** — `Integer`

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLGroupingPreset

#### Parent

IAIMPMLGroupingPreset inherited from the IAIMPPropertyList

#### Properties

##### AIMPML_GROUPINGPRESET_PROPID_CUSTOM

This is a user data parameter, it allow you to bind custom data to the interface.

- **Type:** IUnknown
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IUnknown, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IUnknown>)

##### AIMPML_GROUPINGPRESET_PROPID_ID

Unique preset identification, must be unique for all plugins!

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMPML_GROUPINGPRESET_PROPID_NAME

Preset name, value is displaying to end user

Refer to the automatic localization article

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPMLGroupingPresetStandard

#### Description

Interface describes a preset that uses standard data provider for a grouping tree

#### Parent

IAIMPMLGroupingPresetStandard inherits from IAIMPMLGroupingPreset

#### Properties

##### AIMPML_GROUPINGPRESETSTD_PROPID_FIELDS

Field list.
Each entry of the list must implements least two interfaces: IAIMPString (field name) and IAIMPMLSortDirection (sorting direction).

- **Type:** IAIMPObjectList
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPObjectList, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPObjectList>)

#### Methods

##### GetFilter

- `out` **Filter** — `IAIMPMLDataFilterGroup`
  All changes in the Filter will be automatically applied to the preset.
  Use the BeginUpdate / EndUpdate methods to change few settings at one time.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPMLDataStorage

### Description

Interface provides an access to common to all data storages settings. The IAIMPMLGroupingPresets is implemented on same level.

### Parent

IAIMPMLDataStorage inherited from IAIMPPropertyList

### Properties

#### AIMPML_DATASTORAGE_PROPID_ID

Global unique ID of the data storage

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

#### AIMPML_DATASTORAGE_PROPID_CAPTION

User friendly name of data storage

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

#### AIMPML_DATASTORAGE_PROPID_GROUPINGPRESET

Active grouping tree preset

- **Type:** IAIMPMLGroupingPreset
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPMLGroupingPreset, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(.., <IAIMPMLGroupingPreset>)

### Creating the instance

<IAIMPServiceMusicLibrary>.GetStorageByID(.., IID_IAIMPMLDataStorage, ..)

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPMLDataStorage2

### Description

Extended version of the IAIMPMLDataStorage interface that provides an ability to create data storage based objects.

Additionally, the IAIMPMLDataProvider and IAIMPMLDataProvider2 interfaces are implemented on same level. You can get their instances via the IAIMPMLDataStorage.QueryInterface(...) method.

### Parent

IAIMPMLDataStorage2 inherited from IAIMPMLDataStorage

### Methods

#### CreateObject

- `in` **ID** — `TGUID`
  ID of object.

  Following IDs are now supported:

  - IID_IAIMPMLDataFilter - ID of the IAIMPMLDataFilter
- `out` **Obj** — `Untyped`
  Object instance
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_NOINTERFACE - object with specified GUID is not registered.

### Creating the instance

<IAIMPServiceMusicLibrary>.GetStorageByID(.., IID_IAIMPMLDataStorage2, ..)

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.60.2160

## IAIMPMLFileList

### Description

List of the <FileName, ID> pairs for specified data storage.

Note: type and format of ID field are depended from specified data storage.

### Methods

#### Add

- `in` **ID** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Clear

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Delete

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Insert

- `in` **Index** — `Integer`
- `in` **ID** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetCount

- `out` **Result** — `Integer`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetFileName

- `in` **Index** — `Integer`
- `out` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetFileName

- `in` **Index** — `Integer`
- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetID

- `in` **Index** — `Integer`
- `out` **ID** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetID

- `in` **Index** — `Integer`
- `in` **ID** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Clone

- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Creating the instance

<IAIMPCore>.CreateObject(IID_IAIMPMLFileList, ...)

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPMLPlaylistPreimage

### Description

Provides an access to preimage settings that based on one of data storages of Music Library.

Note that some data storage has no support of preimages.

### Parent

IAIMPMLPlaylistPreimage inherits from IAIMPPlaylistPreimage

### Methods

#### GetFilter

- `out` **Filter** — `IAIMPMLDataFieldFilter`
  All changes in the Filter will be automatically applied to the preimage.
  Use the BeginUpdate / EndUpdate methods to change few settings at one time.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetStorage

Source of the data

- `out` **Storage** — `IUnknown`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## IAIMPMLSortDirection

### Description

Interface provides an access to sorting direction.

### Methods

#### GetValue

- `out` **Value** — `Integer`
  Can be one of following values:

  - `AIMPML_SORTDIRECTION_ASCENDING`
  - `AIMPML_SORTDIRECTION_DESCENDING`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetValue

- `in` **Value** — `Integer`
  Can be one of following values:

  - `AIMPML_SORTDIRECTION_ASCENDING`
  - `AIMPML_SORTDIRECTION_DESCENDING`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.60.2160
