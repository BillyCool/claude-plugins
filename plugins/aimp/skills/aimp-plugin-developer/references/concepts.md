# AIMP SDK concepts

## Introduction (index)

AIMP provides two different API types for developers - Local and Remote.

The **Local API** is provided for plugins, which are Dynamic Linking Libraries (DLL) and located in the sub folder of the "AIMP\Plugins" folder. This type of API provide a maximal possibilities to interact with the application.

The **Remote API** is limited version of the Local API, and provided for another applications. This API must not be used in plugins.

## Overview (CommonTerms)

### Overview

All Local API was based on interfaces. if you are not familiar with it, please refer to this article.

Note that some programming languages doesn't interact with reference counter of the interface automatically (Delphi not related to this category of programming languages) - see Microsoft recommendations.

### Structure

All interactions between program and plugin processed via their presenters - IAIMPCore and IAIMPPlugin respectively.
IAIMPCore provides an access to already presented functionality of program (including functionality that implemented via other plugins).
IAIMPPlugin produces a new functionality or extend existing.

Services is interfaces that provides an access to functions grouped by target. Each service presents specific part of program or plugin. Name of interface of service always looks like IAIMPServiceXXX. For example: IAIMPServiceMenuManager, IAIMPServiceActionManager.

Extensions is interfaces that extends an existing services. Name of interface is in the IAIMPExtensionXXX format. For example: IAIMPExtensionAudioDecoder, IAIMPExtensionFileInfoProvider.

### Definitions

In this documentation uses the following definitions:
**1.** Value quoted in "<" ">" means a instance of the interface. For example: <IAIMPCore>

### Multi-threading

Note that only few services are supports multi-threading. Description for each interface contains information about multi-threading support.

### See also

- Plugin work folder structure
- An access to services
- Guidelines for working with services
- Registering extension
- Registering service

### Plugins folder structure (PluginFolder)

#### Plugins folder structure

All plugins has been placed in <PluginsPath> folder. You can get full path via IAIMPCore.GetPath service with `AIMP_CORE_PATH_PLUGINS` parameter.

Each plugin has own work folder that must contains all required files for correct working of plugin, except user settings.

If plugin has own localization files it must place it in the `Langs` sub folder of work folder in `*.lng` format. Localizations will automatically loaded into common stack by the app. An access to common localization stack provided by IAIMPServiceMUI service.

Common structure:

```
<PluginsPath>\<Plugin Name>\Langs\*.lng
<PluginsPath>\<Plugin Name>\<Plugin Name>.dll (Windows 32-bit)
<PluginsPath>\<Plugin Name>\x64\<Plugin Name>.dll (Windows 64-bit)
<PluginsPath>\<Plugin Name>\x64\<Plugin Name>.so (Linux 64-bit)
```

#### See also

- Algorithm of loading custom localizations
- Where plugin must store user settings?
- Linux support

### User settings (PluginSettings)

#### Where plugin must store user settings?

To prevent issues with access rights and to make the backup / synchronizing procedure easier, plugin must store all settings in common configuration file. An access to it is provided by IAIMPServiceConfig service.

**Remark**. If plugin is using data bases or another data which size more than 1 KBytes - plugin must store it as separate file in user's profile folder to prevent performance issues. Path to user's profile folder can be retrieved via IAIMPCore.GetPath method with AIMP_CORE_PATH_PROFILE parameter.

### Working with services (Services)

#### Access to services

An access to services provided via <IAIMPCore>.QueryInterface that inherited from IUnknown interface.

Warning! Do not forget to check function result, requested service can be inaccessible!

#### Access to non built-in services

In cases when you use services that provided by another plugin, you should take into account that required plugin can be loaded after your. According to this, required to you service can be inaccessible during your plugin initialization. In this case you should process AIMP_SYSTEM_NOTIFICATION_SERVICE_ADDED notification in the IAIMPPlugin.SystemNotification method handler.

#### Recommendations

```
if Succeeded(<IAIMPCore>.QueryInterface(IID_IAIMPServiceVersionInfo, AVerInfo)) then
try
// do something
finally
AVerInfo := nil;
end;
```

**2.** In some situations you can urgent need to store reference to the service. In this case, you should process the IAIMPPlugin.SystemNotification notification. Plugin must check all stored references and release those that equals to the removing. Otherwise it can crash.

**3.** Note that plugin can be loaded by Audio Converter or Tag Editor tool. You should check on plugin initialization if all required built-in services are available. If some services are not available plugin may return an error code - AIMP will mark this plugin as unused.

### Creating custom services (CustomServices)

#### Requirements to custom services

1. Each interface (service, object or etc) must have unique GUID
2. GUID must not be equals to GUID of standard interfaces
3. Strictly forbidden to change structure of any interface without changing it GUID, if interface has been published at least once

#### Custom Extensions

1. Service must implement IAIMPServiceAttrExtendable***** interface if it want to support extensions
2. Service must not implement own version of extensions registration mechanism.
3. All extensions must be registered via IAIMPCore.RegisterExtension. This will allow to application to track relationships between plugins and unregister extensions automatically before plugin unload

#### Registering Primitives

Service must implement IAIMPServiceAttrObjects***** interface if it want to share own primitives for itself and other plugins. According to this other plugins will be able to access to primitives via IAIMPCore.CreateObject method.

#### Registering Services

To registering custom service call the IAIMPCore.RegisterService method during plugin initialization. Custom service will be unregistered automatically before plugin finalization.

#### Example

Refer to the `Demos \ CustomServiceDemo`

***** All required interfaces are defined in the apiCore.

### Linux support (LinuxDialect)

#### Changes in the API for cross-platform plugins

| API | Windows | Linux |
|---|---|---|
| PWideChar has been replaced with PChar | Defined as PWideChar | Defined as PAnsiChar. See for details on working with strings in Linux |
| HDC replaced with HCANVAS | Defined as HDC | Defined as a pointer to cairo_t |
| HWND | Works as before | Emulated within GUI API, incompatible with windows of third-party applications or libraries. The plugin UI needs to be migrated to the GUI API | is required
| OleVariant has been replaced with VarValue | Defined as OleVariant. It is recommended to migrate to the VarValue API | Our own type. Migration to VarValue API |
| IAIMPImage2.LoadFromBitmap | Works as before | Not supported. Migration to one of the alternative methods is required |
| IAIMPImage2.LoadFromResource | Works as before | Not supported. Migration to one of the alternative methods is required |
| IAIMPUIImageList.LoadFromResource | Works as before | Not supported. Migration to IAIMPUIImageList3.LoadFromStream |
| IAIMPExtensionAlbumArtCatalog.GetIcon | Not supported. Now the player requests the icon as IAIMPImageContainer via <IAIMPExtensionAlbumArtCatalog>.QueryInterface |
| The AIMPUI_FORM_PROPID_ICON property of the IAIMPUIForm object supports: | HICON, IAIMPStream, IAIMPImage, IAIMPImageContainer | IAIMPStream, IAIMPImage, IAIMPImageContainer |
| The AIMPUI_TRAYICON_PROPID_ICON property of the object IAIMPUITrayIcon supports: | HICON, IAIMPStream, IAIMPImage, IAIMPImageContainer | IAIMPStream, IAIMPImage, IAIMPImageContainer |

#### Using third-party libraries in Linux

If the plugin uses a third-party library that is not included in the OS's default distribution, you must use dynamic loading:

- Linux does not search for statically linked modules in the folder with the library that calls them
- AIMP does not provide options for installing/removing libraries from shared folders
- Dynamic loading/unloading must occur in IAIMPPlugin.Initialize/IAIMPPlugin.Finalize
- If the dynamic loading failed - the plugin can notify the player about unavailability by returning E_FAIL to IAIMPPlugin.Initialize

#### See also

- Working with strings in Linux

### Using GDI+ (GDIPlus)

#### Using GDI+

If plugin using GDI+ API it must initialize and finalize GDI+ library (calling the GdiplusStartup and GdiplusShutdown functions) in <IAIMPPlugin>.Initialize and <IAIMPPlugin>.Finalize according to the Microsoft requirements (see the "Remark" section).

### Working with strings (PChar)

#### Linux

In Linux, all strings are represented as an array of bytes in UTF8 encoding, rather than UTF16 as in Windows.

#### Nuances

Working with strings in multibyte encodings requires special attention to a number of nuances that need to be taken into account:

- In UTF8, a single character can occupy from 1 to 8 bytes (1-8 elements of IAIMPString).
The letters of the English alphabet take up 1 byte, all others take up more than 1 byte.
Accordingly, indexing by elements is not equal to indexing by characters in most cases.
The affected API is IAIMPString.Get / IAIMPString.Set
- In UTF16, a single character can take up 2 or 4 bytes (1 or 2 IAIMPString elements).
In most cases, a character fits into 1 IAIMPString.
Accordingly, indexing by elements may not coincide with indexing by symbols.
Affected API: IAIMPString.Get / IAIMPString.Set
- Trimming a byte array by an arbitrary offset can split a multibyte character into parts, resulting in incorrect data.
Affected API: IAIMPString.Delete
- The length of a string is the number of bytes, not the number of characters
Affected API: IAIMPString.GetLength
- When concatenating strings, it is important to ensure that each fragment is a valid utf8/utf16 sequence and that there are no "trimmed" characters at the boundaries.
Affected API: IAIMPString.Insert
If you need to work with a string character by character, it is recommended to use specialized libraries for utf8/utf16.
