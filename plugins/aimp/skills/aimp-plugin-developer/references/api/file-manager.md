# File Manager

## File Manager

- Common Terms
- Services
- Extensions
- Primitives

## Common Terms (FileManager)

AIMP works with two file types - real and virtual.

**Virtual file** is file that does not really exists on drive in the form in which it looks for the program. Usually, virtual file is representation of real file in the archive or representation of some part of real file.

Name of virtual file is meta-link to the file-container and track name in the following format:`<Full path to file-container>:<full track name>`**Note 1:** full track name can contains the "/" or "\" symbols, but must not contains the ":" symbol.
**Note 2:** full track name must not be started from the "/", "\" symbols
**Note 3:** name of file-container must not be ended by the "/", "\" symbols.

Examples:
` C:\Music\MyTrack 1.ogg:02
 C:\Music\MyTrack 2.ogg:03_chapter001
 C:\Music\MyTrack 3.cue:15
 C:\Music\MyTrack 4.cue:subtrack 1/chapter 001`
Note, that file container can be an audio file or any other, including really nonexistent.

**Note:** in this API, names of virtual files will be marked as FileURI, names of real files - as FileName.

### See also

- IAIMPServiceFileManager
- IAIMPServiceFileStreaming
- IAIMPExtensionFileExpander
- IAIMPVirtualFile

## Services

### Services

- IAIMPServiceFileFormats
- IAIMPServiceFileInfo
- IAIMPServiceFileInfoFormatter
- IAIMPServiceFileInfoFormatterUtils
- IAIMPServiceFileManager
- IAIMPServiceFileStreaming
- IAIMPServiceFileSystems
- IAIMPServiceFileURI
- IAIMPServiceFileURI2
- IAIMPServiceFileURI3

### IAIMPServiceFileFormats

#### Description

Service provides an access to file formats information that registered in the application.

#### Methods

##### GetFormats

- `in` **Flags** — `DWORD`
  One or combination of following flags:

  - AIMP_SERVICE_FILEFORMATS_CATEGORY_AUDIO;

  - AIMP_SERVICE_FILEFORMATS_CATEGORY_PLAYLISTS;
- `out` **S** — `IAIMPString`
  List of extensions in following format: `*.ext1;*.ext2;...*.ext100;`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### IsSupported

Method checks if file is supported by it extension.

- `in` **FileName** — `IAIMPString`
  Name of real file.
- `in` **Flags** — `DWORD`
  One or combination of following flags:

  - AIMP_SERVICE_FILEFORMATS_CATEGORY_AUDIO;

  - AIMP_SERVICE_FILEFORMATS_CATEGORY_PLAYLISTS;
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileFormats, ...);

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Extensions:** IAIMPExtensionFileFormat
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPServiceFileInfo

#### Methods

##### GetFileInfoFromFileURI

- `in` **FileURI** — `IAIMPString`
  Virtual file
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - AIMP_SERVICE_FILEINFO_FLAG_DONTUSEAUDIODECODERS - prohibit an ability to get information about the track via IAIMPServiceAudioDecoders
- `in` **Info** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetFileInfoFromStream

- `in` **Stream** — `IAIMPStream`
  Note: this method works slowly than the GetFileInfoFromFileURI method.
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - AIMP_SERVICE_FILEINFO_FLAG_DONTUSEAUDIODECODERS - prohibit an ability to get information about the track via IAIMPServiceAudioDecoders
- `in` **Info** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetVirtualFile

- `in` **FileURI** — `IAIMPString`
  Virtual file
- `in` **Flags** — `DWORD`
  Reserved. Must be set to zero.
- `out` **Info** — `IAIMPVirtualFile`
- `out` **Result** — `HRESULT`
  S_OK - method succeeded, if otherwise - file is not virtual.

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileInfo, ...);

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Extensions:** IAIMPExtensionFileInfoProvider, IAIMPExtensionFileInfoProviderEx
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPServiceFileInfoFormatter

#### Description

Service provides an ability to format file information with specified template.

#### Methods

##### Format

- `in` **Template** — `IAIMPString`
  The list of supported macros for template depends from version of application.
- `in` **FileInfo** — `IAIMPFileInfo`
  Put `nil/null` to generate preview string
- `in` **FormatterID** — `Integer`
  One of following IDs:
  AIMP_FILEINFO_FORMATTER_ID_BASIC (default)
  AIMP_FILEINFO_FORMATTER_ID_PLAYING

  Playing file formatter supports for few additional macros that available for playing file only. Use the IAIMPServicePlayer.GetInfo to retrive information about playing file.
- `in` **AdditionalInfo** — `IUnknown`
  Additional information about the file. Reserved, for future usage. Must be set to `nil / null`.
- `out` **FormattedResult** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileInfoFormatter, ...);

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

#### See also

- How to get list of supported macros?

### IAIMPServiceFileInfoFormatterUtils

#### Description

Service provides an ability to show context menu with the list of supported macros for the IAIMPServiceFileInfoFormatter service.

#### Methods

##### ShowMacrosLegend

- `in` **ScreenTarget** — `TRect`
  The placement of menu invoker in screen coordinates, context menu will not intersects this area.

  If you need to show context menu under mouse cursor, just defined the ScreenTarget as shown below:

  ScreenTarget.Left = ScreenTarget.Right = Cursor.X;
  ScreenTarget.Top = ScreenTarget.Bottom = Cursor.Y;
- `in` **FormatterID** — `Integer`
  One of following IDs:
  AIMP_FILEINFO_FORMATTER_ID_BASIC (default)
  AIMP_FILEINFO_FORMATTER_ID_PLAYING

  Playing file formatter supports for few additional macros that available for playing file only. Use the IAIMPServicePlayer.GetInfo to retrive information about playing file.
- `in` **EventsHandler** — `IUnknown`
  Refer to the IAIMPActionEvent.
  The Data parameter of the IAIMPActionEvent.OnExecute method will contains selected macro as IAIMPString.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileInfoFormatterUtils, ...);

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPServiceFileManager

#### Description

The IAIMPServiceFileManager service provides an ability to register custom extensions.

Usage example:

```
Core.RegisterExtension(IID_IAIMPServiceFileManager, ...);
```

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Extensions:** IAIMPExtensionFileExpander
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPServiceFileStreaming

#### Description

The IAIMPServiceFileStreaming service provides an access to real and virtual files via the IAIMPStream interface.

Interface implementation must support asynchronous access.

#### Methods

##### CreateStreamForFile

Refer to the IAIMPFileSystemCommandStreaming for more information about the parameters.

##### CreateStreamForFileURI

Creates the IAIMPStream for virtual or real file.

- `in` **FileURI** — `IAIMPString`
  Virtual File
- `out` **VirtualFile** — `IAIMPVirtualFile`
  Information about the virtual file, can be equal to nil (null).
- `out` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileStreaming, ...);

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPServiceFileSystems

#### Description

The IAIMPServiceFileSystems service provides an access to commands for specified FileURI.

#### General principle

File system is a set of interfaces that provides an ability to operate with files with special file path:

```
scheme://path or scheme:\\path
```

Each extension of service presents single scheme. Before operate with file, AIMP search the file system for specified FileURI. If no extension of this file system was found - AIMP will use the interface of default file system..

#### Methods

##### Get

Provides an ability to get interface instance of command by IID for specified scheme. Scheme detects by FileURI.

- `in` **FileURI** — `IAIMPString`
  Virtual FileURI
- `in` **IID** — `TGUID`
  IID of command interface
- `out` **Command** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetDefault

Provides an ability to get interface instance of command by IID for default file system (no scheme).

- `in` **IID** — `TGUID`
  IID of command interface
- `out` **Command** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileSystems, ...);

#### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Extensions:** IAIMPExtensionFileSystem
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1815

#### Primitives

##### Primitives

- TAIMPFileAttributes

##### TAIMPFileAttributes

###### Description

####### TAIMPFileAttributes

- `in` **Attributes** — `DWORD`
  Attributes are same to attributes from the WIN32_FIND_DATA structure
- `in` **TimeCreation** — `TDateTime`
  Integer part is days, fractional part is milliseconds.
  Time format is fully compatible with TDateTime type from Delphi language
- `in` **TimeLastAccess** — `TDateTime`
  Integer part is days, fractional part is milliseconds.
  Time format is fully compatible with TDateTime type from Delphi language
- `in` **TimeLastWrite** — `TDateTime`
  Integer part is days, fractional part is milliseconds.
  Time format is fully compatible with TDateTime type from Delphi language
- `in` **Reserved0** — `Int64`
  Reserved, must be set to 0
- `in` **Reserved1** — `Int64`
  Reserved, must be set to 0
- `in` **Reserved2** — `Int64`
  Reserved, must be set to 0

###### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

#### IAIMPFileSystemCustomFileCommand

##### Description

This is basic interface for commands that process the files.

Interface implementation must support asynchronous access.

##### Methods

###### CanProcess

- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

###### Process

- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

#### IAIMPFileSystemCommandCopyToClipboard

##### Description

Command copies content of FileName to clipboard.

##### Methods

###### CopyToClipboard

- `in` **Files** — `IAIMPObjectList`
  List of files like a IAIMPString that content should be copied to clipboard
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

#### IAIMPFileSystemCommandDelete

##### Description

Command removes the FileName physically.

##### Parent

inherits from IAIMPFileSystemCustomFileCommand

##### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

#### IAIMPFileSystemCommandDropSource

##### Description

Command creates the IAIMPStream instance for specified FileName for drag-n-drop operation.

Interface implementation must support asynchronous access.

##### Methods

###### CreateStream

- `in` **FileName** — `IAIMPString`
  File name (without path) used as name for a target file.
  You can edit the FileName content to change the target file name.
- `out` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

#### IAIMPFileSystemCommandFileInfo

##### Description

Returns information about the file

##### Parent

inherits from IAIMPFileSystemCustomFileCommand

##### Methods

###### GetFileAttrs

- `in` **FileName** — `IAIMPString`
- `out` **Attrs** — `TAIMPFileAttributes`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

###### GetFileSize

- `in` **FileName** — `IAIMPString`
- `out` **Size** — `Int64`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

###### IsFileExists

- `in` **FileName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

#### IAIMPFileSystemCommandOpenFileFolder

##### Description

Command opens a folder (source) that contains the FileName, (FileName should be focused).

##### Parent

inherits from IAIMPFileSystemCustomFileCommand

##### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

#### IAIMPFileSystemCommandStreaming

##### Description

Command creates the IAIMPStream for specified FileName.

Interface implementation must support asynchronous access.

##### Methods

###### CreateStream

Creates the IAIMPStream interface for specified real file.

- `in` **FileName** — `IAIMPString`
  Real file name
- `in` **Flags** — `DWORD`
  Combination of following flags:
  - `AIMP_SERVICE_FILESTREAMING_FLAG_CREATENEW` - create or overwrite file
  - `AIMP_SERVICE_FILESTREAMING_FLAG_READ` - open an existing file for reading
  - `AIMP_SERVICE_FILESTREAMING_FLAG_READWRITE` - open an existing file for reading or writing
  - `AIMP_SERVICE_FILESTREAMING_FLAG_BUFFERED` - pre-buffer read/write operation for better performance
- `in` **Offset** — `Int64`
  The Offset and the Size parameters allows to create stream for part of file.
  If you not need that, both parameters should be set to `-1`.

  This feature does not compatible with the `AIMP_SERVICE_FILESTREAMING_FLAG_CREATENEW` and `AIMP_SERVICE_FILESTREAMING_FLAG_READWRITE` flags.
- `in` **Size** — `Int64`
  Refer to the Offset.
- `out` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

### IAIMPServiceFileURI

#### Description

The IAIMPServiceFileURI service provides few methods to work with FileURI of real and virtual files.

#### Methods

##### Build

Method builds a FileURI based on file name of file-container and part name. Refer to the virtual files article.

- `in` **ContainerFileName** — `IAIMPString`
- `in` **PartName** — `IAIMPString`
- `out` **FileURI** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Parse

Methods parses the FileURI and returns file name of container and name of sub-track.
If the FileURI related to real file - PartName will be set to `nil/null`

- `in` **FileURI** — `IAIMPString`
- `out` **ContainerFileName** — `IAIMPString`
- `out` **PartName** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### ChangeFileExt

Method provides an ability to change file ext of file container or sub track

- `var` **FileURI** — `IAIMPString`
- `in` **NewExt** — `IAIMPString`
  New file extension in following format: .mp3
- `in` **Flags** — `DWORD`
  0 or combination of following flags:

  `AIMP_SERVICE_FILEURI_FLAG_DOUBLE_EXTS` - double extensions will be replaced with NewExt. If flag is not set - only last extension will be replaced.

  `AIMP_SERVICE_FILEURI_FLAG_PART_EXT` - if flag is set - function will change the extension of sub track instead of container's file name.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### ExtractFileExt

Method provides an ability to extract file extension

- `in` **FileURI** — `IAIMPString`
- `out` **Ext** — `IAIMPString`
  File extension in following format: .mp3
- `in` **Flags** — `DWORD`
  0 or combination of following flags:

  `AIMP_SERVICE_FILEURI_FLAG_DOUBLE_EXTS` - flag switches on the support of files with double extensions.

  `AIMP_SERVICE_FILEURI_FLAG_PART_EXT` - if flag is set - function will return the extension of sub track instead of container's file name.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### ExtractFileName

Method provides an ability to extract file name without the path.
File name includes name of file-container and sub track name.

- `in` **FileURI** — `IAIMPString`
- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### ExtractFileParentDirName

Method provides an ability to get name of parent folder for real or virtual file.

- `in` **FileURI** — `IAIMPString`
- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### ExtractFileParentName

Method provides an ability to get name of parent:
Function will return name of file-container if FileURI is related to virtual file
Function will return name of parent folder if FileURI is related to real file

- `in` **FileURI** — `IAIMPString`
- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### ExtractFilePath

Method provides an ability get path of file

- `in` **FileURI** — `IAIMPString`
- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### IsURL

Method checks if FileURI is URL.

- `in` **FileURI** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileURI, ...);

#### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

### IAIMPServiceFileURI2

#### Parent

inherits from IAIMPServiceFileURI

#### Methods

##### GetScheme

Method returns the scheme of the FileURI.

- `in` **FileURI** — `IAIMPString`
- `out` **Scheme** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileURI2, ...);

#### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

### IAIMPServiceFileURI3

#### Parent

Inherits from IAIMPServiceFileURI3

#### Methods

##### ProcessEnvironmentVariables

Processes environment variables in specified uri.

Environment variable must be defined using following template: `%env_var_name%`
Example: `%AIMPBIN%\AIMP.exe`

Additionally to system variables, AIMP provides few built-in:

- AIMP_SERVICE_FILEURI_ENVAR_APPDATA - `%AppData%` - path to application data directory
- AIMP_SERVICE_FILEURI_ENVAR_DESKTOP - `%Desktop%` - path to user desktop
- AIMP_SERVICE_FILEURI_ENVAR_HOME - `%Home%` - path to user home directory
- AIMP_SERVICE_FILEURI_ENVAR_MYDOCUMENTS - `%MyDocuments%` - path to "My Documents" directory
- AIMP_SERVICE_FILEURI_ENVAR_MYMUSIC - `%MyMusic%` - path to "My Music" directory
- AIMP_SERVICE_FILEURI_ENVAR_PROFILE - `%Profile%` - path to AIMP profile folder
- AIMP_SERVICE_FILEURI_ENVAR_TEMP - `%Temp%` - path to temporary directory

- `var` **FileURI** — `IAIMPString`
- `in` **Flags** — `DWORD`
  One of flags:

  - `AIMP_SERVICE_FILEURI_ENVAR_FLAG_EXPAND` - replaces the variables by their actual values
  - `AIMP_SERVICE_FILEURI_ENVAR_FLAG_COLLAPSE` - replaces the values by variable names (for built-in variables only)
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceFileURI3, ...);

#### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## Extensions

### Extensions

- IAIMPExtensionFileExpander
- IAIMPExtensionFileFormat
- IAIMPExtensionFileInfoProvider
- IAIMPExtensionFileInfoProviderEx
- IAIMPExtensionFileSystem

### IAIMPExtensionFileExpander

#### Description

The IAIMPExtensionFileExpander interface is an extension for the IAIMPServiceFileManager service that allows split real file container into one or view virtual files.

Interface implementation must support asynchronous access.

#### Methods

##### Expand

- `in` **FileName** — `IAIMPString`
  Name of real file
- `out` **List** — `IAIMPObjectList`
  List of virtual files (refer to the IAIMPVirtualFile)
  The List must be created and filled only if result of the method is S_OK.
- `in` **ProgressCallback** — `IAIMPProgressCallback`
  Optional, can be equal to nil (null).
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPExtensionFileFormat

#### Description

The IAIMPExtensionFileFormat interface is an extension for the IAIMPServiceFileFormats service that provides an information about the new file format.

#### Methods

##### GetDescription

- `out` **S** — `IAIMPString`
  Short description of file type.
  For example: `Ogg Vorbis`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### GetExtList

- `out` **S** — `IAIMPString`
  List of supported extensions.
  For example: `*.ogg;*.oga;`

  Note that the ";" symbol must be specified after each element, even after last element of list.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### GetFlags

- `out` **S** — `IAIMPString`
  One of the following flags:

  - AIMP_SERVICE_FILEFORMATS_CATEGORY_AUDIO;

  - AIMP_SERVICE_FILEFORMATS_CATEGORY_PLAYLISTS;
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPExtensionFileInfoProvider

#### Description

The IAIMPExtensionFileInfoProvider interface is an extension for the IAIMPServiceFileInfo service that provides an extended information about the file.

Interface implementation must support asynchronous access.

#### Methods

##### GetFileInfo

Method returns extended information about specified file

- `in` **FileURI** — `IAIMPString`
  Name of virtual file
- `in` **Info** — `IAIMPFileInfo`
  You must not set the AIMP_FILEINFO_PROPID_FILENAME field, because it set by the invoker.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPExtensionFileInfoProviderEx

#### Description

The IAIMPExtensionFileInfoProviderEx interface is an extension for theIAIMPServiceFileInfo service that provides an extended information about the file..

This interface is more general type of the IAIMPExtensionFileInfoProvider interface. Unlike original, this interface allows to get information about the file that specified via IAIMPStream. Note, that this type of extension works slowly than IAIMPExtensionFileInfoProvider.

Interface implementation must support asynchronous access.

#### Methods

##### GetFileInfo

- `in` **Stream** — `IAIMPStream`
- `in` **Info** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### IAIMPExtensionFileSystem

#### Description

Extension for the IAIMPServiceFileSystems service.
Must implement one or few file system commands (Refer to the children articles of the IAIMPServiceFileSystems chapter).

Interface implementation must support asynchronous access.

#### Parent

IAIMPExtensionFileSystem inherits from IAIMPPropertyList.

#### Properties

##### AIMP_FILESYSTEM_PROPID_SCHEME

Scheme of file system:

```
scheme://path or scheme:\\path
```

Refer to the IAIMPServiceFileSystems for more information.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

##### AIMP_FILESYSTEM_PROPID_READONLY

Return the nonzero value if file system does not support for data modification

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definition:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1800

## Primitives

### Primitives

- IAIMPFileInfo
- IAIMPVirtualFile

### IAIMPFileInfo

#### Description

The IAIMPFileInfo is storage for extended information about the file.

Interface implementation must support asynchronous access.

#### Parent

The IAIMPFileInfo inherits from IAIMPPropertyList.

#### Properties

##### AIMP_FILEINFO_PROPID_CUSTOM

This is a user data parameter, it allow you to bind custom data to the interface.

- **Type:** IUnknown
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IUnknown, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IUnknown>)

##### AIMP_FILEINFO_PROPID_ALBUM

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_ALBUMART

The IAIMPImage and the IAIMPImageContainer are supported by this property.

- **Type:** IAIMPImage / IAIMPImageContainer
- **Read:** IAIMPPropertyList.GetValueAsObject
- **Write:** IAIMPPropertyList.SetValueAsObject

##### AIMP_FILEINFO_PROPID_ALBUMARTIST

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_ALBUMGAIN

Average volume level for album, in dB.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_FILEINFO_PROPID_ALBUMPEAK

Maximal volume level for album, in dBFS.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_FILEINFO_PROPID_ARTIST

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_BITRATE

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_FILEINFO_PROPID_BPM

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_FILEINFO_PROPID_BITDEPTH

Information about bit depth of audio stream.
= 0 - bit depth is unknown
< 0 - corresponds to floating point sample type.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_FILEINFO_PROPID_CHANNELS

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_FILEINFO_PROPID_CODEC

Information about codec that displayed in the "File Information" dialog.
Optional, can be missed.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_COMMENT

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_COMPOSER

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_COPYRIGHT

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_CUESHEET

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_DATE

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_DISKNUMBER

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_DISKTOTAL

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_DURATION

Track duration, in seconds.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_FILEINFO_PROPID_FILENAME

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_FILESIZE

- **Type:** Int64
- **Read:** IAIMPPropertyList.GetValueAsInt64
- **Write:** IAIMPPropertyList.SetValueAsInt64

##### AIMP_FILEINFO_PROPID_GENRE

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_LYRICS

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_PUBLISHER

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_SAMPLERATE

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_FILEINFO_PROPID_TITLE

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_TRACKGAIN

Average volume level for track, in dB.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_FILEINFO_PROPID_TRACKNUMBER

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_TRACKPEAK

Maximal volume level for track, in dBFS.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_FILEINFO_PROPID_TRACKTOTAL

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_URL

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_CONDUCTOR

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_MOOD

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_CATALOG

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_ISRC

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_LYRICIST

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_ENCODEDBY

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_RATING

Rating of the track that stored in tags of file
Can be in range from 0 to 5.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_FILEINFO_PROPID_KEY

Also known as initial key

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_FILEINFO_PROPID_ML_ADDINGDATE

Adding date to DB of Audio Library

Integer part is days, fractional part is milliseconds.
Time format is fully compatible with TDateTime type from Delphi language

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat

##### AIMP_FILEINFO_PROPID_ML_LASTPLAYDATE

Date of last playback

Integer part is days, fractional part is milliseconds.
Time format is fully compatible with TDateTime type from Delphi language

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat

##### AIMP_FILEINFO_PROPID_ML_MARK

User defined rating (mark) that stored in music library database (0..5)

Use the write function to modify property value.
Note that the write function may return E_FAIL error if the audio file cannot be imported to music library database.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_FILEINFO_PROPID_ML_PLAYCOUNT

Playback count

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

##### AIMP_FILEINFO_PROPID_ML_RATING

Rating for track, that calculates automatically based on all the statistics from the database (0.0 to 1.0).

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat

##### AIMP_FILEINFO_PROPID_ML_DISPLAYING_MARK

Mark that displayed for user (0..5). Mark can be equal to rating value (depended from settings of Music Library). (See also the AIMP_FILEINFO_PROPID_ML_MARK)

Use the write function to modify property value.
Note that the write function may return E_FAIL error if the audio file cannot be imported to music library database.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_FILEINFO_PROPID_ML_LABELS

Set of custom labels divided by ";" character that specified for a audio file in music library database.

Use the write function to modify property value.
Note that the write function may return E_FAIL error if the audio file cannot be imported to music library database.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### Methods

##### Assign

Copies all data from source.

- `in` **Source** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Clone

- `out` **Info** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating the instance

<IAIMPCore>.CreateObject(IID_IAIMPFileInfo, ...)

#### Summary

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

#### See also

- Properties name conversion
- Format information about the file

### IAIMPVirtualFile

#### Description

The IAIMPVirtualFile interface provides an information about the virtual file.

Interface implementation must support asynchronous access.

#### Parent

The IAIMPVirtualFile inherits from IAIMPPropertyList.

#### Properties

##### AIMP_VIRTUALFILE_PROPID_INDEXINSET

Index of virtual track in the set (if presented).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_VIRTUALFILE_PROPID_CLIPSTART / AIMP_VIRTUALFILE_PROPID_CLIPFINISH

Bounds of the playback range, in seconds.
If virtual file have not limitation by time (all file is played), the IAIMPPropertyList.GetValueAsFloat method must return the E_NOTIMPL value for this properties.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_VIRTUALFILE_PROPID_AUDIOSOURCEFILE

Real file name of audio file.
Property can be not set if real file name is not exists or file name is same to file name of file-container. In this case the IAIMPPropertyList.GetValueAsObject method must return the E_NOTIMPL value.

Example 1: CUE sheet is presented as separate file - C:\Music\Track.cue. So, name of virtual file will looks like C:\Music\Track.cue:1. In this case, the AIMP_VIRTUALFILE_PROPID_AUDIOSOURCEFILE property will return name of audio file, C:\Music\Track.mp3 for example.
Example 2: CUE sheet is embedded and stored in file tags. So, name of virtual file will looks like C:\Music\Track.mp3:1. In this case, the AIMP_VIRTUALFILE_PROPID_AUDIOSOURCEFILE property is not required and the GetValueAsObject method returns E_NOTIMPL.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_VIRTUALFILE_PROPID_FILEFORMAT

Short file format. For example: MP3, OGG, CDA.

This property is optional. If property is not set, the application will detect file format by extension of file-container.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

##### AIMP_VIRTUALFILE_PROPID_FILEURI

Name of virtual file

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### Methods

##### CreateStream

Methods creates an instance of the IAIMPStream interface.

if method returns E_NOTIMPL the application will create stream instance by yourself.

- `out` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetFileInfo

- `in` **Info** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### IsExists

Method checks an existence of source

- `out` **Result** — `LongBool`

##### IsInSameStream

Method shows is streams that created via CreateStream method for the current and the VirtualFile are refer to same part of source.

If you cannot calculate this info by any reasons, just return the E_FAIL value.

This method is for optimization purposes only.

- `in` **VirtualFile** — `IAIMPVirtualFile`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### Synchronize

Plugin must validate state of all internal data that refer with source. If internal data is not valid, plugin must return any error code except S_OK. In this case, the application will automatically reload virtual files for current file-container via one of the IAIMPExtensionFileExpander extensions.

The method called by the application before call the CreateStream method.

- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating the instance

The instance creates by plugin and adding to the List parameter in the IAIMPExtensionFileExpander.Expand method handler

#### Remark

- **Definitions:** apiFileManager.pas / apiFileManager.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal version:** 3.60.1455

#### See also

- Properties name conversion
