# Primitives (CommonClasses)

## Primitives

- Types
- IAIMPConfig
- IAIMPConfigFile
- IAIMPDPIAware
- IAIMPErrorInfo
- IAIMPFileStream
- IAIMPHashCode
- IAIMPImage
- IAIMPImage2
- IAIMPImage3
- IAIMPImageContainer
- IAIMPMemoryStream
- IAIMPNamedContainer
- IAIMPObjectList
- IAIMPObjectList2
- IAIMPProgressCallback
- IAIMPPropertyList
- IAIMPPropertyList2
- IAIMPString
- IAIMPStream

## Types

### Types

- HCANVAS
- VarValue

### HCANVAS

#### Description

Canvas context handle, native for specified OS.

#### Linux

Defined as pointer to cairo_t

#### Windows

Defined as HDC

#### Summary

- **Definition:** apiTypes.pas / apiTypes.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

### VarValue

#### Description

A special wrapper type that implements a cross-platform analogue of the Variant type used in the AIMP API.
Interaction with the type instance should be done exclusively through special functions defined in the apiTypes module:

#### Methods

##### VarValueInit

Creates a new instance of VarValue-type

- `in` **Value** — `?`
  Source value, can be on of following types: `Int32, Int64, Double, String (PChar)`
- `out` **Result** — `VarValue`

##### VarValueFree

Destroys the VarValue-type instance and releases all it resources

- `var` **Value** — `VarValue`

##### VarValueNull

Returns the VarValue-type without value, that can indicate unknown or missing data. It is not necessary to destroy the returned instance using VarValueFree.

- `out` **Result** — `VarValue`

##### VarValueCopy

Creates a copy of VarValue. The copy must be finalized using VarValueFree

- `in` **Value** — `VarValue`
- `out` **Result** — `VarValue`

##### VarValueIsXXX

Check type of source value inside the VarValue-container

- `in` **Value** — `VarValue`
- `out` **Result** — `Boolean`

##### VarValueToXXX

Returns source value from VarValue-container in specified format. If requested format is not equal to source format, the value will be automatically converter to requested format.

- `in` **Value** — `VarValue`
- `out` **Result** — `?`

#### Summary

- **Definition:** apiTypes.pas / apiTypes.h
- **Applications:** Player
- **Minimal Version:** 6.00.3000

## IAIMPConfig

### Description

This interface provides a basic functionality to work with configuration files.

### Methods

#### Delete

This method allow you to remove key or entire section

- `in` **KeyPath** — `IAIMPString`
  Path to the key or the section.

  Examples:
  - `<Section>`
  - `<Section>`\`<Key>`
- `out` **Result** — `HRESULT`
  S_OK - Method success
  E_ACCESSDENIED - Method has been called from non-main thread
  E_FAIL - Key or section is not found at specified path
  E_INVALIDARG - Path is invalid
  E_UNEXPECTED - Unexpected failure

#### GetValueAsFloat

Method returns key value as floating point value

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `out` **Value** — `Double`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_FAIL - The value was not found at specified path
  E_UNEXPECTED - An unexpected failure occurred

#### GetValueAsInt32

Method returns key value as 32-bit integer value

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `out` **Value** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_FAIL - The value was not found at specified path
  E_UNEXPECTED - An unexpected failure occurred

#### GetValueAsInt64

Method returns key value as 64-bit integer value

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `out` **Value** — `Int64`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_FAIL - The value was not found at specified path
  E_UNEXPECTED - An unexpected failure occurred

#### GetValueAsStream

Method returns key value as binary stream

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `out` **Value** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_FAIL - The value was not found at specified path
  E_UNEXPECTED - An unexpected failure occurred

#### GetValueAsString

Method returns key value as string

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `out` **Value** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_FAIL - The value was not found at specified path
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsFloat

Method writes floating point value to configuration file

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `in` **Value** — `Double`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsInt32

Method writes 32-bit integer value to configuration file

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `in` **Value** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsInt64

Method writes 64-bit integer value to configuration file

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `in` **Value** — `Int64`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsStream

Method writes binary stream to configuration file.

Warning! Avoid to store large stream (more than 1 KByte) into the configuration file, refer to the recommendations.

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `in` **Value** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsString

Method writes string to configuration file.

- `in` **KeyPath** — `IAIMPString`
  The path to the value in followed format: `<Section Name>`\`<Value Name>`
- `in` **Value** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_INVALIDARG - The key path is not valid
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPConfigFile

### Description

IAIMPConfigFile is extension for IAIMPConfig that provides an ability to load/save configuration from file/stream.

### Methods

#### LoadFromFile

- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### LoadFromStream

- `in` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SaveToFile

- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SaveToStream

- `in` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
[/methods]

### Creating the object

<IAIMPCore>.CreateObject(IID_IAIMPConfigFile, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3066

## IAIMPDPIAware

### Descriptions

The interface provides information about current DPI of the object.
This information uses by app engine to calculate target sizes, bounds of the object and determine how to stretch it during drawing.

### Methods

#### GetDPI

- `out` **Result** — `Integer`
  In range of 40-250 dpi.

#### SetDPI

Attention! Some objects may not implement this method.

- `in` **DPI** — `Integer`
  New resolution, in range of 40-250 dpi.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.50.2000

## IAIMPErrorInfo

### Description

Interface provides an ability to return extended information about the error to calling side.

### Methods

#### GetInfo

- `out` **ErrorCode** — `Integer`
  Error code
- `out` **Message** — `IAIMPString`
  Short error description.
- `out` **Details** — `IAIMPString`
  Extended error description. Can be `nil` / `NULL`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetInfoFormatted

Method returns formatted information about the error to display to user.

- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetInfo

- `in` **ErrorCode** — `Integer`
  Error code
- `in` **Message** — `IAIMPString`
  Short error description.
- `in` **Details** — `IAIMPString`
  Extended error description. Can be `nil` / `NULL`

### Creating the instance

<IAIMPCore>.CreateObject(IID_IAIMPErrorInfo, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPFileStream

### Description

IAIMPFileStream is extended variant of IAIMPStream specially for file-based streams.

### Parent

IAIMPFileStream is inherited from IAIMPStream

### Methods

#### GetClipping

If file is clipped the method will return clipping bounds.
See the IAIMPServiceFileStreaming.CreateStreamForFile

- `out` **Offset** — `Int64`
- `out` **Size** — `Int64`
- `out` **Result** — `HRESULT`
  S_OK - Method success
  E_FAIL - File is not clipped
  E_UNEXPECTED - Unexpected failure

#### GetFileName

- `out` **S** — `IAIMPString`
  Full name of real file on disk drive
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Creating the object

See the IAIMPServiceFileStreaming

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPHashCode

### Methods

#### GetHashCode

- `out` **Result** — `Integer`
  Hash code of data of source object

#### Recalculate

This function provides an ability to force recalculate hash code

## IAIMPImage

### Methods

#### LoadFromFile

- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### LoadFromStream

- `in` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SaveToFile

- `in` **FileName** — `IAIMPString`
- `in` **FormatID** — `Integer`
  Image format identification, can be one of the followed values:

  - AIMP_IMAGE_FORMAT_BMP
  - AIMP_IMAGE_FORMAT_GIF
  - AIMP_IMAGE_FORMAT_JPG
  - AIMP_IMAGE_FORMAT_PNG
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SaveToStream

- `in` **Stream** — `IAIMPStream`
- `in` **FormatID** — `Integer`
  Image format identification, can be one of the followed values:

  - AIMP_IMAGE_FORMAT_BMP
  - AIMP_IMAGE_FORMAT_GIF
  - AIMP_IMAGE_FORMAT_JPG
  - AIMP_IMAGE_FORMAT_PNG
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetFormatID

- `out` **Result** — `Integer`
  Image format identification, can be one of the followed values:

  - AIMP_IMAGE_FORMAT_BMP
  - AIMP_IMAGE_FORMAT_GIF
  - AIMP_IMAGE_FORMAT_JPG
  - AIMP_IMAGE_FORMAT_PNG
  - AIMP_IMAGE_FORMAT_UNKNOWN

#### GetSize

- `out` **Size** — `TSize`
  Size of image, in pixels
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Clone

Method creates copy of image

- `out` **Image** — `IAIMPImage`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Draw

Method draw image on specified canvas

- `in` **DC** — `HCANVAS`
  Canvas handle
- `in` **R** — `TRect`
  Target rect
- `in` **Flags** — `DWORD`
  Combination of flags from different groups:

  Group AIMP_IMAGE_DRAW_STRETCHMODE provides an ability to specify on of the following stretch mode:

  Group AIMP_IMAGE_DRAW_QUALITY provides an ability to specify stretch quality. Note that drawing speed is inversely proportional to the quality.

  - AIMP_IMAGE_DRAW_QUALITY_DEFAULT
  - AIMP_IMAGE_DRAW_QUALITY_LOW
  - AIMP_IMAGE_DRAW_QUALITY_HIGH
- `in` **Attrs** — `IUnknown`
  Reserved. Must be `nil / null`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Resize

- `in` **Width** — `Integer`
  New width
- `in` **Height** — `Integer`
  New height
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### DPI Aware

The IAIMPDPIAware interface are supported. It provides information about source DPI of the image.

### Creating the object

<IAIMPCore>.CreateObject(IID_IAIMPImage, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPImage2

### Description

IAIMPImage2 is extended version of the IAIMPImage interface

### Methods

#### LoadFromResource

- `in` **Instance** — `HMODULE`
  Module handle that contains the image
  Deprecated, for Windows OS only
- `in` **ResName** — `PChar`
- `in` **ResType** — `PChar`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### LoadFromBitmap

- `in` **Bitmap** — `HBITMAP`
  Bitmap handle.
  Deprecated, for Windows OS only
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### LoadFromBits

- `in` **Bits** — `PRGBQuad`
  Pointer to first element of array of RGBQuads.
- `in` **Width** — `Integer`
- `in` **Height** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### CopyToClipboard

Copy image to clipboard in BMP and PNG formats

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### CanPasteFromClipboard

Check the clipboard for BMP and PNG images.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### PasteFromClipboard

Paste the image from a clipboard, the BMP and PNG formats are supported.
In case, if clipboard contains BMP format only, image will be automatically converter to PNG format to save memory.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Creating the instance

<IAIMPCore>.CreateObject(IID_IAIMPImage2, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Asynchronous access:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal version:** 4.00.1660

## IAIMPImage3

### Description

IAIMPImage3 is extended version of the IAIMPImage2 interface

### Methods

#### SaveToBits

Stores pixels to array of RGB-quads (A, R, G, B).

- `in` **Bits** — `PRGBQuad`
  Pointer to first element of array of RGB-quads.
  Memory must be allocated by the calling side (plugin) using the formula: `width * height * 4`;
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Creating the instance

<IAIMPCore>.CreateObject(IID_IAIMPImage3, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Asynchronous access:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal version:** 6.00.3000

## IAIMPImageContainer

### Description

The IAIMPImageContainer interface unlike IAIMPImage is used for storing and sharing images. The image data is compressed and all requested parameters are calculated on-fly.

The IAIMPHashCode interface is supported by this object.

### Methods

#### CreateImage

Method creates IAIMPImage that based on copy of source data.

- `out` **Image** — `IAIMPImage`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetInfo

Information about the image.
Information is calculated on-fly using format headers - image data is not uncompressed to do it. Note that this information can be wrong if format headers in the file are corrupted.

- `out` **Size** — `TSize`
  Size of image
- `out` **FormatID** — `Integer`
  Format identificator, can be one of the following values:

  - AIMP_IMAGE_FORMAT_UNKNOWN
  - AIMP_IMAGE_FORMAT_BMP
  - AIMP_IMAGE_FORMAT_GIF
  - AIMP_IMAGE_FORMAT_JPG
  - AIMP_IMAGE_FORMAT_PNG
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetData

- `out` **Result** — `PByte`
  Pointer to first element of byte-array.

#### GetDataSize

- `out` **Result** — `DWORD`
  Length of data array

#### SetDataSize

- `in` **Value** — `DWORD`
  Method provides an ability to set new size of data array.

  Warning! Changing the size leads to flush image data.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Creating the object

<IAIMPCore>.CreateObject(IID_IAIMPImageContainer, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPMemoryStream

### Description

IAIMPMemoryStream is extended variant of IAIMPStream that stores all data in memory.

### Parent

IAIMPMemoryStream is inherited from IAIMPStream

### Methods

#### GetData

- `out` **Result** — `PByte`
  Pointer to first element of byte-array

### Creating the object

<IAIMPCore>.CreateObject(IID_IAIMPMemoryStream, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPNamedContainer

### Description

IAIMPNamedContainer is special version of IAIMPString that provides an ability to bind custom data with the string.
It may be useful in GUI API to bind the user data to the displayed text.

### Creating the object

<IAIMPCore>.CreateObject(IID_IAIMPNamedContainer, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPObjectList

### Description

IAIMPObjectList is a list of general purpose, it can contains any interfaces.

### Methods

#### Add

- `in` **Obj** — `IUnknown`
  Object
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
  Index of object in the list
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Insert

- `in` **Index** — `Integer`
  New object will be inserted before Index
- `in` **Obj** — `IUnknown`
  Object
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetCount

- `out` **Result** — `Integer`
  Count of objects in the list

#### GetObject

- `in` **Index** — `Integer`
  Index
- `in` **IID** — `TGUID`
  IID of subobject
- `out` **Obj** — `Untyped`
  subobject
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_NOINTERFACE - if subobject with specified IID is not supported by object.

#### SetObject

- `in` **Index** — `Integer`
  Index of object in the list
- `in` **Obj** — `IUnknown`
  New object
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Creating the object

<IAIMPCore>.CreateObject(IID_IAIMPObjectList, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPObjectList2

### Description

IAIMPObjectList2 is extended version of the IAIMPObjectList interface

### Methods

#### IndexOf

- `in` **Object** — `IUnknown`
- `out` **Result** — `Integer`

### Creating the object

<IAIMPCore>.CreateObject(IID_IAIMPObjectList2, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPProgressCallback

### Description

This interface provides an ability to show operation progress and an ability to cancel it if needed.

Interface instance is transmitted to plugin when calling a command. Plugin should: call the Progress method of the interface during operation progress, and check state of Canceled flag after each call.

### Methods

#### Process

- `in` **Progress** — `Single`
  Operation progress in percents
- `var` **Canceled** — `LongBool`
  If user cancels the operation Canceled value will be set to True.

### Creating the instance

Instance will be created by calling side.

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPPropertyList

### Description

The IAIMPPropertyList is low-level interface that provides an access to additional properties of binded object.

### Methods

#### BeginUpdate

Method blocks all notifications about changes until the EndUpdate call.
Recommended for usage in cases when you changing more than one parameter at once.

#### EndUpdate

Refer to the BeginUpdate method

#### Reset

Reset all settings to their defaults.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetValueAsFloat

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `out` **Value** — `Double`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetValueAsInt32

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `out` **Value** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetValueAsInt64

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `out` **Value** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetValueAsObject

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `in` **IID** — `TGUID`
  IID of object. For example: IID_IAIMPString.
- `out` **Value** — `Untyped`
  Value as IUnknown or it descendants. For example: IAIMPString
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsFloat

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `in` **Value** — `Double`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsInt32

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `in` **Value** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsInt64

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `in` **Value** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsObject

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `in` **Value** — `IUnknown`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Example

```
<IAIMPPropertyList>.BeginUpdate;
try
<IAIMPPropertyList>.SetValueAsObject(...);
<IAIMPPropertyList>.SetValueAsObject(...);
<IAIMPPropertyList>.SetValueAsInt64(...);
finally
<IAIMPPropertyList>.EndUpdate;
end;
```

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### See also

Property name conversion

### Name conversion (IAIMPPropertyList_PropIDNameConv)

#### Name template

Name of property ID is based on specific rule and contains additional information: type of object and description

Name template looks like:`AIMP_OOOOO_PROPID_DDDDD`Where:`OOOOO` - type of parent object (without "IAIMP" prefix)
`DDDDD` - description
Example 1:`AIMP_FILEINFO_PROPID_ALBUMGAIN`

Description: AlbumGain
Object type: FILEINFO - IAIMPFileInfo
Example 2:`AIMP_FILEINFO_PROPID_ALBUMARTIST`

Description: AlbumArtist
Object type: FILEINFO - IAIMPFileInfo

#### Custom properties

Value of custom properties identifications must be started from value defined in the AIMP_PROPERTYLIST_CUSTOM_PROPID_BASE constant to prevent conflicts in future versions of SDK.

## IAIMPPropertyList2

### Description

IAIMPPropertyList2 is extended version of the IAIMPPropertyList interface

### Methods

#### GetValueAsVariant

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `out` **Value** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetValueAsVariant

- `in` **PropertyID** — `Integer`
  Property identificator, determined by the object that is bound to the interface
- `in` **Value** — `VarValue`
  The VarValue instance must be released by calling side using theVarValueFree method.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1841

## IAIMPString

### Description

IAIMPString is a high-level wrapper over the byte array of the original string.
Strings has differences in implementation between Windows and Linux.

The IAIMPHashCode interface is supported by this object.

### Methods

#### Get

- `in` **Index** — `Integer`
  The ordinal number of the requested item (from 0 to GetLength - 1)
- `out` **Item** — `Char`
  A character or part of a multibyte character
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### GetData

Method will return pointer to first element in null-terminate array. Length of this array is GetLength + 1 (including null character in the end).
Null-terminating allows you to put result of this method to the Win32 API functions without length definition.

Warning! This array is "read only"!

- `out` **Result** — `PChar`
  Pointer to first element in array

#### GetLength

- `out` **Result** — `Integer`
  Count of elements in the array

#### GetHashCode

- `out` **Result** — `Integer`
  Returns hash code.

#### Set

- `in` **Index** — `Integer`
  The index of the element to be replaced (from 0 to GetLength - 1)
- `out` **Item** — `Char`
  Character or part of a multibyte character
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SetData

Method allows you to replace all data at once

- `in` **Items** — `PChar`
  Pointer to first element in array
- `in` **ItemCount** — `Integer`
  Length of array. Can be set to `-1`, in this case, array length will be automatically calculated until null-terminator.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Add

- `in` **S** — `IAIMPString`
  Adding the string
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Add2

- `in` **Items** — `PChar`
  Pointer to first element in array
- `in` **ItemCount** — `Integer`
  Length of array
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### ChangeCase

Method allows you to change registry of string depends from one of following modes

- `in` **Mode** — `Integer`
  - AIMP_CASE_LOWER
  - AIMP_CASE_UPPER
  - AIMP_CASE_ALL_WORDS_WITH_CAPICAL_LETTER
  - AIMP_CASE_FIRST_WORD_WITH_CAPICAL_LETTER
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Clone

Method creates clone of string

- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Compare

- `in` **S** — `IAIMPString`
- `out` **CompareResult** — `Integer`
  -1, 0, +1
- `in` **IgnoreCase** — `LongBool`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Compare2

- `in` **Items** — `PChar`
  Pointer to first element in array
- `in` **ItemCount** — `Integer`
  Length of array
- `out` **CompareResult** — `Integer`
  -1, 0, +1
- `in` **IgnoreCase** — `LongBool`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Delete

- `in` **Index** — `Integer`
  Index of the element from which the deletion will begin (from 0 to GetLength - 1).
- `in` **Count** — `Integer`
  The number of elements to be deleted. If you want to delete all characters until the end of the string, you can specify an infinite large number, such as MAXINT.

  **It is important** that the part to be deleted does not fall into the middle of multibyte characters, otherwise the data will be incorrect. See working with strings
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Find

- `in` **S** — `IAIMPString`
  Search string
- `out` **Index** — `Integer`
  The index of the element where the match was found (from 0 to GetLength - 1).
- `in` **Flags** — `Integer`
  Search options.
  The parameter can be a zero or combination of followed flags:
  - AIMP_STRING_FIND_IGNORECASE - ignore case during search
  - AIMP_STRING_FIND_WHOLEWORD - find whole word only
- `in` **StartFromIndex** — `Integer`
  The index of the element from which to start the search. The default value is 0.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Find2

- `in` **Items** — `PChar`
  Search string, pointer to the first array element
- `in` **ItemCount** — `Integer`
  Number of elements in the array
- `out` **Index** — `Integer`
  The index of the element where the match was found (from 0 to GetLength - 1).
- `in` **Flags** — `Integer`
  Search options.
  The parameter can be a zero or combination of followed flags:
  - AIMP_STRING_FIND_IGNORECASE - ignore case during search
  - AIMP_STRING_FIND_WHOLEWORD - find whole word only
- `in` **StartFromIndex** — `Integer`
  The index of the element from which to start the search. The default value is 0.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Insert

- `in` **Index** — `Integer`
  The index of the element before which the string specified in S will be inserted (from 0 to GetLength).

  **It is important** that the index does not fall in the middle of a multibyte character, otherwise it will result in incorrect data. See working with strings
- `in` **S** — `IAIMPString`
  The string to be inserted
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Insert2

- `in` **Index** — `Integer`
  The ordinal number of the element before which the string specified in S will be inserted (from 0 to GetLength).

  **Important** that the index does not fall in the middle of a multibyte character, otherwise it will result in incorrect data. See working with strings
- `in` **Items** — `PChar`
  Pointer to the first element of the array
- `in` **ItemCount** — `Integer`
  Number of elements in the array
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Replace

- `in` **OldPattern** — `IAIMPString`
  Search text
- `in` **NewPattern** — `IAIMPString`
  Text for replacement
- `in` **Flags** — `Integer`
  Search options.
  The parameter can be a zero or combination of followed flags:
  - AIMP_STRING_FIND_IGNORECASE - ignore case during search
  - AIMP_STRING_FIND_WHOLEWORD - find whole word only
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Replace2

- `in` **OldPatternItems** — `PChar`
  Search string, pointer to the first array element
- `in` **OldPatternItemCount** — `Integer`
  Number of elements in the array
- `in` **NewPatternItems** — `PChar`
  Replacement string, pointer to the first array element
- `in` **NewPatternItemCount** — `Integer`
  Number of elements in the array
- `in` **Flags** — `Integer`
  Search options.
  The parameter can be a zero or combination of followed flags:
  - AIMP_STRING_FIND_IGNORECASE - ignore case during search
  - AIMP_STRING_FIND_WHOLEWORD - find whole word only
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### SubString

Method copies a part of the string into a separate instance of IAIMPString

- `in` **Index** — `Integer`
  The ordinal number of the element from which copying will begin (from 0 to GetLength - 1).

  **It is important** that the index does not fall into the middle of a multibyte character, as this will result in incorrect data. See working with strings
- `in` **Count** — `Integer`
  The number of elements to be copied. If you need to copy all characters to the end of the string, you can specify an infinite large number, for example, `MAXINT`
- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Creating the object

<IAIMPCore>.CreateObject(IID_IAIMPString, ...)

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPStream

### Description

IAIMPStream provides interface for working with binary stream.

### Methods

#### GetSize

- `out` **Result** — `Int64`
  Size of stream, in bytes

#### SetSize

Method provides an ability to set stream size, in bytes.

Note: size of stream will be automatically extended when it needed. This method is for optimization purposes only.

Warning! If current stream size more than new defined - part of data will be truncated.

- `in` **Value** — `Int64`
  New size, in bytes
- `out` **Result** — `HRESULT`
  S_OK - Method success
  E_NOTIMPL - Stream is read only
  E_UNEXPECTED - Unexpected failure

#### GetPosition

- `out` **Result** — `Int64`
  Position of reading / writing cursor in bytes

#### Seek

Method allows you to change position of reading / writing cursor.

- `in` **Offset** — `Int64`
  Offset in bytes
- `in` **Mode** — `Integer`
  The parameter defines as the Offset parameter should be used.
  Can be one of the following values:
  - AIMP_STREAM_SEEKMODE_FROM_BEGINNING - Offset value is offset from stream beginning
  - AIMP_STREAM_SEEKMODE_FROM_CURRENT - Offset value is offset from current cursor position
  - AIMP_STREAM_SEEKMODE_FROM_END - Offset value is offset from the end of stream
- `out` **Result** — `HRESULT`
  S_OK - Method success
  E_FAIL - Can not change the position at specified Offset.
  E_INVALIDARG - One of parameters is invalid
  E_UNEXPECTED - Unexpected failure

#### Read

- `var` **Buffer** — `PByte`
- `in` **Count** — `DWORD`
- `out` **Result** — `Integer`
  `-1` on unexpected failure or count of read bytes otherwise.

#### Write

- `in` **Buffer** — `PByte`
- `in` **Count** — `DWORD`
- `out` **Written** — `PInteger`
  Pointer to 32-bit integer value.
  Parameter displays what bytes has been really written to the stream.
  This parameter is optional - can be `nil` / `NULL`.
- `out` **Result** — `HRESULT`
  S_OK - Method success
  E_NOTIMPL - Stream is read only
  E_UNEXPECTED - An unexpected failure occurs

### Creating the object

- <IAIMPCore>.CreateObject(IID_IAIMPMemoryStream, ...) - Creating the memory based stream
- See IAIMPServiceFileStreaming

### Summary

- **Definition:** apiObjects.pas / apiObjects.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455
