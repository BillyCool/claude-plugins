# Lyrics

## Lyrics

- Services
- Extensions
- Primitives
- Types

## Services

### Services

- IAIMPServiceLyrics

### IAIMPServiceLyrics

#### Description

Service provides an ability to get the lyrics for specified file
The lyrics searching is running in separate thread (optionally), plugin will receive a notification about the result of operation via callback function.

#### Methods

##### Get

- `in` **FileInfo** — `IAIMPFileInfo`
- `in` **Flags** — `DWORD`
  0 or combination of following flags:
  - `AIMP_SERVICE_LYRICS_FLAGS_NOCACHE` - ignore cached values
  - `AIMP_SERVICE_LYRICS_FLAGS_WAITFOR` - the method will not return control until operation has been completed if this flag is used
- `in` **CallbackProc** — `TAIMPServiceLyricsReceiveProc`
- `in` **UserData** — `Pointer`
  User data that will be passed to the CallbackProc
- `out` **Task** — `TTaskHandle`
  Task ID, if method succeeded
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Cancel

Method provides an ability to cancel active task.

- `in` **Task** — `TTaskHandle`
- `in` **Flags** — `DWORD`
  0 or combination of following flags:
  - `AIMP_SERVICE_LYRICS_FLAGS_WAITFOR` - the method will not return control until operation has been completed if this flag is used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceLyrics, ...);

#### Summary

- **Definition:** apiLyrics.pas / apiLyrics.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.50.2000

## Extensions

### Extensions

- IAIMPExtensionLyricsProvider

### IAIMPExtensionLyricsProvider

#### Description

The IAIMPExtensionLyricsProvider is extension for the IAIMPServiceLyrics service that allows to plugin implement custom lyrics provider.

Interface implementation must support asynchronous access.

#### Methods

##### Get

- `in` **Owner** — `IAIMPTaskOwner`
  This interface provides an ability to check if task is canceling.
  Refer to the IAIMPTask for usage recommendations.
- `in` **FileInfo** — `IAIMPFileInfo`
- `in` **Flags** — `DWORD`
  Flags are same to flags for the IAIMPServiceLyrics.Get method
- `in` **Lyrics** — `IAIMPLyrics`
  Container for found information. Must be populated by plugin only if result of request is succeeded.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### GetCategory

Provides information about category of the provider

- `out` **Result** — `DWORD`
  One of following values:

  - AIMP_LYRICS_PROVIDER_CATEGORY_FILE
  - AIMP_LYRICS_PROVIDER_CATEGORY_INTERNET

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definition:** apiLyrics.pas / apiLyrics.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.50.2000

## Primitives

### Primitives

- IAIMPLyrics

### IAIMPLyrics

#### Description

The IAIMPLyrics is a advanced container for lyrics, that support plain and synchronized texts.

Interface implementation must support asynchronous access.

#### Parent

IAIMPLyrics is inherited from the IAIMPPropertyList.

#### Properties

##### AIMP_LYRICS_PROPID_TEXT

Plain text (without any control tags)

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_LYRICS_PROPID_LYRICIST

Lyricist (optionally)

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_LYRICS_PROPID_ALBUM

Album (optionally)

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_LYRICS_PROPID_TITLE

Title (optionally)

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_LYRICS_PROPID_CREATOR

Creator of the lyrics file (optionally)

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_LYRICS_PROPID_APP

App name that has been used for creating the lyrics file (optionally)

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_LYRICS_PROPID_APPVER

App version that has been used for creating the lyrics file (optionally)

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_LYRICS_PROPID_TYPE

One of following values:
- AIMP_LYRICS_TYPE_UNKNOWN
- AIMP_LYRICS_TYPE_UNSYNCED
- AIMP_LYRICS_TYPE_SYNCED

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

##### AIMP_LYRICS_PROPID_OFFSET

Offset time, in milliseconds.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### Methods

##### Assign

Copies all data from source.

- `in` **Source** — `IAIMPLyrics`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Clone

- `out` **Target** — `IAIMPLyrics`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Add

Adds new time range. Ranges will be automatically sorted.

- `in` **TimeStart** — `Integer`
  In milliseconds
- `in` **TimeFinish** — `Integer`
  In milliseconds
- `in` **Text** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Delete

- `in` **Index** — `Integer`
  Index of the range, begins from 0.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Find

- `in` **Time** — `Integer`
  In milliseconds
- `out` **Index** — `Integer`
  Index of the range, begins from 0.
- `out` **Text** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Get

- `in` **Index** — `Integer`
  Index of the range, begins from 0.
- `out` **TimeStart** — `Integer`
  In milliseconds
- `out` **TimeFinish** — `Integer`
  In milliseconds
- `out` **Text** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetCount

- `out` **Count** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### LoadFromFile

- `in` **FileURI** — `IAIMPString`
  File URI
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### LoadFromStream

- `in` **Stream** — `IAIMPStream`
- `in` **Format** — `Integer`
  Stream format, can be one of following values:
  - AIMP_LYRICS_FORMAT_TXT
  - AIMP_LYRICS_FORMAT_LRC
  - AIMP_LYRICS_FORMAT_SRT
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### LoadFromString

- `in` **Stream** — `IAIMPString`
- `in` **Format** — `Integer`
  Stream format, can be one of following values:
  - AIMP_LYRICS_FORMAT_TXT
  - AIMP_LYRICS_FORMAT_LRC
  - AIMP_LYRICS_FORMAT_SRT
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### SaveToFile

- `in` **FileURI** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### SaveToStream

- `in` **Stream** — `IAIMPStream`
- `in` **Format** — `Integer`
  Stream format, can be one of following values:
  - AIMP_LYRICS_FORMAT_TXT
  - AIMP_LYRICS_FORMAT_LRC
  - AIMP_LYRICS_FORMAT_SRT
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### SaveToString

- `out` **String** — `IAIMPString`
- `in` **Format** — `Integer`
  Stream format, can be one of following values:
  - AIMP_LYRICS_FORMAT_TXT
  - AIMP_LYRICS_FORMAT_LRC
  - AIMP_LYRICS_FORMAT_SRT
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Creating the instance

<IAIMPCore>.CreateObject(IID_IAIMPLyrics, ...)

#### Summary

- **Definition:** apiLyrics.pas / apiLyrics.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.50.2000

## Types

### Types

- TAIMPServiceLyricsReceiveProc

### TAIMPServiceLyricsReceiveProc

#### Description

The TAIMPServiceLyricsReceiveProc is callback function that receives IAIMPLyrics from asynchronized request. This function will be called from main thread of the application.

#### Methods

- `in` **Lyrics** — `IAIMPLyrics`
  The Lyrics instance, can be equal to `nil / null`, if lyrics was not found.
- `in` **UserData** — `Pointer`

#### Summary

- **Definition:** apiLyrics.pas / apiLyrics.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.50.2000
