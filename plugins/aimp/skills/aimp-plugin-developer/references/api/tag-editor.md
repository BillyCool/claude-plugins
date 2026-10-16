# Tag Editor

## Tag Editor

- Services and Extensions
- Primitives

## Services and Extensions

### Services and Extensions

- IAIMPExtensionTagsProvider
- IAIMPServiceFileTagEditor
- IAIMPServiceFindTagsOnline

### IAIMPExtensionTagsProvider

#### Description

Extension for the IAIMPServiceFindTagsOnline service, provides an ability to implement custom tags provider for the "autotagging via online-services" feature that available in advanced tag editor.

Interface implementation must support for multi-threading!

#### Methods

##### GetName

- `out` **Name** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetSupportedFields

Returns list of the tag fields that are supported by provider

- `out` **Fields** — `PInteger`
  Pointer to first element of array, array must be populated via IDs of IAIMPFileInfo properties:
- `out` **Count** — `Integer`
  Number of elements in array.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### FindAlbums

Find albums by user query.

Method will be called from non-main thread!

- `int` **Query** — `IAIMPString`
- `int` **Owner** — `IAIMPTaskOwner`
- `int` **ErrorInfo** — `IAIMPErrorInfo`
  Plugin must populate error info only if unexpected error happened.
- `int` **ReceiveProc** — `TAIMPServiceFindTagsOnlineAlbumInfoReceiveProc`
- `int` **ReceiveProcData** — `Pointer`
  Custom data, must be passed to ReceiveProc during the call.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed.
  E_FAIL - nothing is found
  E_UNEXPECTED - An unexpected failure occurred

##### FindTracks

Provides the list of tracks by AlbumInfo that provided via the FindAlbums method.
You can pass the custom data to AlbumInfo via IAIMPFileInfo.AIMP_FILEINFO_PROPID_CUSTOM.

Method will be called from non-main thread!

- `int` **AlbumInfo** — `IAIMPFileInfo`
- `int` **Owner** — `IAIMPTaskOwner`
- `int` **ErrorInfo** — `IAIMPErrorInfo`
  Plugin must populate error info only if unexpected error happened.
- `out` **TracksInfo** — `IAIMPObjectList`
  List of track, must be populated by IAIMPFileInfo elements
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed.
  E_FAIL - nothing is found
  E_UNEXPECTED - An unexpected failure occurred

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiTagEditor.pas / apiTagEditor.h
- **Multi-threading:** Supported
- **Applications:** Advanced Tag Editor
- **Minimal Version:** 5.00.2300

### IAIMPServiceFileTagEditor

#### Methods

##### EditFile

This method allows you to edit all supported tags in the specified file.
Method will check file format before editing, and will read information about the audio stream.

- `in` **Source** — `IUnknown`
  As a source you can specify the file name (IAIMPString) or file stream (IAIMPStream)
- `in` **IID** — `TGUID`
  IID_IAIMPFileTagEditor
- `out` **Object** — `Untyped`
  IAIMPFileTagEditor
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - file format is not supported by tag editor

##### EditTag

Unlike the EditFile method, this trying to read tag type that specified in the TagID property. Method does not check the file format and does not provides an information about the audio stream.

Attention! Current version of implementation does not have an ability to save changes back.

- `in` **Source** — `IUnknown`
  As a source you can specify the file name (IAIMPString) or file stream (IAIMPStream)
- `in` **TagID** — `Integer`
  AIMP_FILETAG_ID_APEv2
  AIMP_FILETAG_ID_ID3v1
  AIMP_FILETAG_ID_ID3v2
  AIMP_FILETAG_ID_VORBIS
  AIMP_FILETAG_ID_M4A
  AIMP_FILETAG_ID_WMA
- `in` **IID** — `TGUID`
  IID_IAIMPFileInfo
- `out` **Object** — `Untyped`
  IAIMPFileInfo
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - tag was not found in the file.

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileTagEditor, ...);

#### Summary

- **Definitions:** apiTagEditor.pas / apiTagEditor.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1426

### IAIMPServiceFindTagsOnline

#### Description

The IAIMPServiceFindTagsOnline service have no any methods and properties, its required to provide ability to register custom extensions.

Usage example:

```
<IAIMPCore>.RegisterExtension(IID_IAIMPServiceFindTagsOnline, TMyTagsProviderExtension.Create);
```

#### Summary

- **Definitions:** apiTagEditor.pas / apiTagEditor.h
- **Applications:** Advanced Tag Editor
- **Minimal Version:** 4.60.2160

## Primitives

### Primitives

- IAIMPFileTag
- IAIMPFileTagEditor
- Types

### IAIMPFileTag

#### Parent

IAIMPFileTag inherits from the IAIMPFileInfo.

#### Properties

##### AIMP_FILETAG_PROPID_TAG_ID

Tag type, can be one of the following values:
- AIMP_FILETAG_ID_CUSTOM
- AIMP_FILETAG_ID_APEv2
- AIMP_FILETAG_ID_ID3v1
- AIMP_FILETAG_ID_ID3v2
- AIMP_FILETAG_ID_MP4
- AIMP_FILETAG_ID_VORBIS
- AIMP_FILETAG_ID_WMA

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_FILETAG_PROPID_DELETE_ON_SAVING

This property indicates whether to remove the tag from the file when you save changes. If the value is nonzero, the tag will be removed from the file.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### Summary

- **Definitions:** apiTagEditor.pas / apiTagEditor.h
- **Multi-threading:** not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1426

### IAIMPFileTagEditor

#### Methods

##### GetMixedInfo

Method mix information from all tags and provide it as instance of the IAIMPFileInfo interface.

- `out` **Info** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetTag

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  IID_IAIMPFileTag
- `out` **Object** — `Untyped`
  IAIMPFileTag
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetTagCount

- `out` **Result** — `Integer`
  Count of tags in the file.

##### SetToAll

- `in` **Info** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### Save

Method save changes in the file.
To remove tag from file, use the AIMP_FILETAG_PROPID_DELETE_ON_SAVING property of the IAIMPFileTag interface instance.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Summary

- **Definitions:** apiTagEditor.pas / apiTagEditor.h
- **Multi-threading:** not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1426

### Types

#### Types

- TAIMPServiceFindTagsOnlineAlbumInfoReceiveProc

#### TAIMPServiceFindTagsOnlineAlbumInfoReceiveProc

##### Description

- `in` **AlbumInfo** — `IAIMPFileInfo`
  Information about found album
- `in` **Data** — `Pointer`
  Custom data, it passed to plugin with callback function.
  Plugin must pass it to callback function when calling it to return search result.

##### See Also

- IAIMPExtensionTagsProvider
- IAIMPServiceFindTagsOnline

##### Summary

- **Definition:** apiTagEditor.pas / apiTagEditor.h
- **Multi-threading:** not supported
- **Applications:** Advanced Tag Editor
- **Minimal Version:** 4.60.2160
