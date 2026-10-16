# AlbumArts

## AlbumArts

- Overview
- Services
- Extensions
- Types

## Overview (IAIMPAlbumArtOverview)

### Overview

Album arts can be so different: as small as too large. They can be placed locally or downloaded from the Internet. To prevent app from freezing while track's album art is loading, the AIMP has uses few solutions:

1. Image optimization

Large album arts resizes to optimal size for display. What reason to display image in 10 MPx resolution on Full HD screen?

2. Requests caching

Optimized album art copies are stored in app cache. This lead that second attempt to take an album art will be completed so fast. Cache can be flushed by plugin via special API (refer to IAIMPServiceAlbumArtCache), or by end user via special UI in app settings.

In v5.02, we have re-designed caching mechanism: now each album art provider MUST interact with caching system by itself. This decision was made because only the provider know what file information is used to search the album art and if requests must be cached or not. Refer to IAIMPAlbumArtRequest for more details.

## Services

### Services

- IAIMPServiceAlbumArt
- IAIMPServiceAlbumArtCache

### IAIMPServiceAlbumArt

#### Description

Service provides an ability to get album art for specified file or/and album.
AlbumArt search process will run in separate thread, and plugin will receive a notification about the end of operation via callback function.

#### Properties

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_FILES

0 - disallow an ability to find album art in files

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_FILES_MASKS

List of templates (without extensions) for searching.
Each value must be separated from others by ";" character.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_FILES_EXTS

List of extensions that are supported.
Each value must be separated from others by ";" character.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET

0 - disallow an ability to find album art in Internet.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET_MAX_FILE_SIZE

Maximal size of album art for downloading, in bytes.
0 - size is unlimited.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_TAGS

0 - disallow an ability to find album art in file tags.

_(Since v5.02)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_ALBUMART_REQUEST_PROPID_RESULTS

Specifies number of results that can be received from the providers using the IAIMPAlbumArtRequest.CachePut method during one request.
Only for the providers of the `AIMP_ALBUMART_PROVIDER_CATEGORY_INTERNET_SEARCH` category.

_(Since v5.40)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### Methods

##### Get

- `in` **FileURI** — `IAIMPString`
  FileURI
- `in` **Artist** — `IAIMPString`
  Optional, can be equal to `nil/null`
- `in` **Album** — `IAIMPString`
  Optional, can be equal to `nil/null`
- `in` **Flags** — `DWORD`
  0 or combination of followed flags:
  - `AIMP_SERVICE_ALBUMART_FLAGS_NOCACHE` - flag suppresses album art search in cache
  - `AIMP_SERVICE_ALBUMART_FLAGS_ORIGINAL` - the method return album art in original resolution
  - `AIMP_SERVICE_ALBUMART_FLAGS_WAITFOR` - the method will not return control until operation has been completed.
  - `AIMP_SERVICE_ALBUMART_FLAGS_OFFLINE` - forces to disable search album art in Internet Warning! Each of the flags has a negative impact on program performance, please do not use it without urgent need.
- `in` **CallbackProc** — `TAIMPServiceAlbumArtReceiveProc`
- `in` **UserData** — `Pointer`
  User data for the CallbackProc
- `out` **Task** — `TTaskHandle`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Get2

- `in` **FileInfo** — `IAIMPFileInfo`
- `in` **Flags** — `DWORD`
  0 or combination of followed flags:
  - `AIMP_SERVICE_ALBUMART_FLAGS_NOCACHE` - flag suppresses album art search in cache
  - `AIMP_SERVICE_ALBUMART_FLAGS_ORIGINAL` - the method return album art in original resolution
  - `AIMP_SERVICE_ALBUMART_FLAGS_WAITFOR` - the method will not return control until operation has been completed.
  - `AIMP_SERVICE_ALBUMART_FLAGS_OFFLINE` - forces to disable search album art in Internet Warning! Each of the flags has a negative impact on program performance, please do not use it without urgent need.
- `in` **CallbackProc** — `TAIMPServiceAlbumArtReceiveProc`
- `in` **UserData** — `Pointer`
  User data for the CallbackProc
- `out` **Task** — `TTaskHandle`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Cancel

- `in` **Task** — `TTaskHandle`
- `in` **Flags** — `DWORD`
  0 or combination of following flags:

  - `AIMP_SERVICE_ALBUMART_FLAGS_WAITFOR` - this method will not return control until operation will be completely canceled
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceAlbumArt, ...);

#### Summary

- **Definitions:** apiAlbumArt.pas / apiAlbumArt.h
- **Multi-threading:** Supported
- **Extensions:** IAIMPExtensionAlbumArtCatalog, IAIMPExtensionAlbumArtCatalog2, IAIMPExtensionAlbumArtProvider, IAIMPExtensionAlbumArtProvider2, IAIMPExtensionAlbumArtProvider3
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPServiceAlbumArtCache

#### Description

This service provides an access to cache manager for album arts.

#### Methods

##### Flush

Flushes all cache

**Warning!** Frequent cache flush can lead to poor performance of the application.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Get

Returns the IAIMPImageContainer for specified key.
Note that `Image` may set to `nil / null` event if function succeeded.

- `in` **Key** — `IAIMPString`
  The key must be built to uniquely identify the album art for the specified IAIMPFileInfo.
- `var` **Image** — `IAIMPImageContainer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Put

Optimizes the IAIMPImageContainer and put it to cache.
You can put the `nil / null` to `Image` parameter to cache an empty value for the `key`.

- `in` **Key** — `IAIMPString`
  The key must be built to uniquely identify the album art for the specified IAIMPFileInfo.
- `var` **Image** — `IAIMPImageContainer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Remove

Flushes cache for specified key.

- `in` **Key** — `IAIMPString`
  The key must be built to uniquely identify the album art for the specified IAIMPFileInfo.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Stat

Returns information about number of images in the cache and it size.

- `out` **Size** — `Int64`
- `out` **NumberOfEntries** — `DWORD`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceAlbumArtCache, ...);

#### See Also

Cache: best practices

#### Summary

- **Definitions:** apiAlbumArt.pas / apiAlbumArt.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 5.02.2360

## Extensions

### Extensions

- IAIMPExtensionAlbumArtCatalog
- IAIMPExtensionAlbumArtCatalog2
- IAIMPExtensionAlbumArtProvider
- IAIMPExtensionAlbumArtProvider2
- IAIMPExtensionAlbumArtProvider3

### IAIMPExtensionAlbumArtCatalog

#### Description

The IAIMPExtensionAlbumArtCatalog interface is a extension for the IAIMPServiceAlbumArt service, and allows to plugin add a menu item to the context menu for external album art catalogs.

#### Methods

##### GetIcon

Deprecated: now player query for IAIMPImageContainer using <IAIMPExtensionAlbumArtCatalog>.QueryInterface method.

- `out` **Image** — `HICON`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### GetName

Catalog display name

- `out` **Name** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Show

This method will be called on menu item click

- `in` **FileURI** — `IAIMPString`
  FileURI
- `in` **Artist** — `IAIMPString`
  Optional, can be equal to `nil / null`
- `in` **Album** — `IAIMPString`
  Optional, can be equal to `nil / null`
- `out` **Image** — `IAIMPImageContainer`
  Image instance, can be equal to `nil / null` if catalog does not provides an ability to select album art immediately. For example, if the extension just open external link via Internet browser.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiAlbumArt.pas / apiAlbumArt.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPExtensionAlbumArtCatalog2

#### Description

The IAIMPExtensionAlbumArtCatalog2 is a second edition of the IAIMPExtensionAlbumArtCatalog interface.

#### Methods

##### Show2

This method will be called on menu item click

- `in` **FileInfo** — `IAIMPFileInfo`
- `out` **Image** — `IAIMPImageContainer`
  Image instance, can be equal to `nil / null` if catalog does not provides an ability to select album art immediately. For example, if the extension just open external link via Internet browser.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiAlbumArt.pas / apiAlbumArt.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1473

### IAIMPExtensionAlbumArtProvider

This extension was deprecated, use the IAIMPExtensionAlbumArtProvider3 instead.

### IAIMPExtensionAlbumArtProvider2

This extension was deprecated, use the IAIMPExtensionAlbumArtProvider3 instead.

### IAIMPExtensionAlbumArtProvider3

#### Description

The IAIMPExtensionAlbumArtProvider3 interface is a extension for the IAIMPServiceAlbumArt service, and allows to plugin implement custom album art provider.

Interface implementation must support asynchronous access.

#### Methods

##### Get

- `in` **FileInfo** — `IAIMPFileInfo`
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
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### GetCategory

Returns provider category.

- `out` **Result** — `DWORD`
  One of the following values:

  - `AIMP_ALBUMART_PROVIDER_CATEGORY_TAGS` - artwork extracts from the file tags

  - `AIMP_ALBUMART_PROVIDER_CATEGORY_FILE` - artwork loads from physical file (Example: cover.jpg that placed in near the audio file)

  - `AIMP_ALBUMART_PROVIDER_CATEGORY_INTERNET` - artwork downloads from network

  - `AIMP_ALBUMART_PROVIDER_CATEGORY_INTERNET_SEARCH` - artwork downloads from network, indicates that the AIMP_ALBUMART_REQUEST_PROPID_RESULTS is supported by the provider _((since v5.40))_

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiAlbumArt.pas / apiAlbumArt.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 5.02.2360

## Types

### Types

- IAIMPAlbumArtRequest
- TAIMPServiceAlbumArtReceiveProc

### IAIMPAlbumArtRequest

#### Description

IAIMPAlbumArtRequest is extension of the IAIMPPropertyList interface that implements helper methods that make easier to interact with search options, cache and download images from the Internet.
The app passes the interface to plugin via methods of the IAIMPMLAlbumArtProvider2 and IAIMPExtensionAlbumArtProvider3 interfaces.

#### Properties

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_FILES

0 - disallow an ability to find album art in files

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_FILES_MASKS

List of templates (without extensions) for searching.
Each value must be separated from others by ";" character.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_FILES_EXTS

List of extensions that are supported.
Each value must be separated from others by ";" character.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET

0 - disallow an ability to find album art in Internet.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET_MAX_FILE_SIZE

Maximal size of album art for downloading, in bytes.
0 - size is unlimited.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_TAGS

0 - disallow an ability to find album art in file tags.

_(Since v5.02)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_ALBUMART_REQUEST_PROPID_RESULTS

Specifies number of results that can be received from the providers using the IAIMPAlbumArtRequest.CachePut method during one request.
Only for the providers of the `AIMP_ALBUMART_PROVIDER_CATEGORY_INTERNET_SEARCH` category.

_(Since v5.40)_

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### Methods

##### CacheGet

Returns the IAIMPImageContainer for specified key.
Note that `Image` may set to `nil / null` event if function succeeded.

- `in` **Key** — `IAIMPString`
  The key must be built to uniquely identify the album art for the specified IAIMPFileInfo.
- `var` **Image** — `IAIMPImageContainer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_FAIL - cache has no entry for the Key
  E_ACCESSDENIED - cache is disabled due app settings or search options
  E_UNEXPECTED - An unexpected failure occurred

##### CachePut

Optimizes the IAIMPImageContainer and put it to cache.
You can put the `nil / null` to `Image` parameter to cache an empty value for the `key`.

- `in` **Key** — `IAIMPString`
  The key must be built to uniquely identify the album art for the specified IAIMPFileInfo.
- `var` **Image** — `IAIMPImageContainer`
  Method will return optimized version of the Image if the AIMP_SERVICE_ALBUMART_FLAGS_ORIGINAL flag is not specified in search options.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_UNEXPECTED - An unexpected failure occurred

##### Download

This is helper function that make download images easier.
The method take the `AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET` and `AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET_MAX_FILE_SIZE` options into account by itself.

- `in` **URL** — `IAIMPString`
  Following protocols are supported: file:// and http(s)://
- `out` **Image** — `IAIMPImageContainer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_FAIL - The method was failed
  E_ABORT - The operation was canceled by a user
  E_ACCESSDENIED - an ability to download album arts from the Internet has been disabled by app settings or search options
  E_OUTOFMEMORY - image size exceed limit that defined by the `AIMP_ALBUMART_REQUEST_PROPID_FIND_IN_INTERNET_MAX_FILE_SIZE` option
  E_UNEXPECTED - An unexpected failure occurred

##### IsCanceled

This is tool interface that provides an ability to plugin to be notified about canceling the operation

- `out` **Result** — `LongBool`
  Plugin must break the operation if the method returns True.

#### Usage example

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

#### Summary

- **Definitions:** apiAlbumArt.pas / apiAlbumArt.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 5.02.2360

### TAIMPServiceAlbumArtReceiveProc

#### Description

The TAIMPServiceAlbumArtReceiveProc is callback function that provides an ability to receive a image container (or image). This function will be called from main thread of the application.

#### Methods

- `in` **Image** — `IAIMPImage`
  The image instance. can be equal to `nil / null`, in this case you should work with the ImageContainer value.
- `in` **ImageContainer** — `IAIMPImageContainer`
  The image container instance, can be equal to `nil / null`, if album art was not found.
- `in` **UserData** — `Pointer`
  The user instance data given when the IAIMPServiceAlbumArt.Get or the IAIMPServiceAlbumArt.Get2 methods were called.

#### Summary

- **Definitions:** apiAlbumArt.pas / apiAlbumArt.h
- **Multi-threading:** Supported
- **Extensions:** -
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1418
