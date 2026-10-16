# Playlists

## Playlists

- Common Terms
- Services and Extensions
- Primitives

## Common Terms (PlaylistManagerTerms)

### Common terms

AIMP allows to work with one or few playlist, wherein all playlists divided into two types - loaded and unloaded. Loaded playlists are displayed in the application, unloaded are displayed in playlists manager and not loaded to the memory.

### Storing

All playlists, regardless of how they were created - opened from external source or created via AIMP, are stores in the profile folder in the *.aimppl format.

So, player will creates local copy in the profile folder for all opened external playlists and will work with it.

### Autoname

The Autoname is used if name is not specified for playlist. Autoname is calculated based on content of the playlist - name of parent folder for all files is taken.

### View Settings

In additional to global playlists settings, AIMP provides an ability to customize view settings for each playlist individually. Plugin has access to individual settings only.

### Cursors

Each playlist contains additional information about the playback position - index of playing track (`PlayingIndex`), and playback cursor (`PlaybackCursor`).

**`PlaybackCursor`** is cursor of internal playback queue, it does not take custom queue and plugins into account. Value of cursor point to the `PlaybackQueueIndex` property of playing track, and does not equals to item index.

**`PlayingIndex`** is an absolute index of playing item in playlist. Note that each playlist has own PlayingIndex value. If you want to access to playing playlist use the IAIMPServicePlaylistManager.GetPlayingPlaylist method.

### See Also

- Access to playlists folder via the IAIMPCore.GetPath with the AIMP_CORE_PATH_PLAYLISTS parameter

## Services and Extensions

### Services and Extensions

- IAIMPServicePlaylistManager
- IAIMPServicePlaylistManager2
- IAIMPExtensionPlaylistManagerListener
- IAIMPExtensionPlaylistPreimageFactory
- IAIMPExtensionPlaylistShuffler

### IAIMPServicePlaylistManager

#### Methods

##### CreatePlaylist

- `in` **Name** — `IAIMPString`
  Automatic name will be applied if name is equals to `nil/null`
- `in` **Activate** — `LongBool`
- `out` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### CreatePlaylistFromFile

- `in` **FileName** — `IAIMPString`
  Full file name (Refer to the External and Internal Playlists topic)
- `in` **Activate** — `LongBool`
- `out` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetActivePlaylist

- `out` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### SetActivePlaylist

- `in` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetPlayingPlaylist

- `out` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread
  E_FAIL - Playable playlist has been removed or nothing playing at current moment

##### GetLoadedPlaylist

- `in` **Index** — `Integer`
- `out` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetLoadedPlaylistByID

Refer to the AIMP_PLAYLIST_PROPID_ID

- `in` **ID** — `IAIMPString`
- `out` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetLoadedPlaylistByName

Refer to the AIMP_PLAYLIST_PROPID_NAME

- `in` **Name** — `IAIMPString`
- `out` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetLoadedPlaylistCount

- `out` **Result** — `Integer`

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlaylistManager, ...);

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Extensions:** IAIMPExtensionPlaylistManagerListener
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPServicePlaylistManager2

#### Description

Provides an access to custom preimage factories that presented via IAIMPExtensionPlaylistPreimageFactory

#### Parent

IAIMPServicePlaylistManager2 inherits from IAIMPServicePlaylistManager.

#### Methods

##### GetPreimageFactory

- `out` **Factory** — `IAIMPExtensionPlaylistPreimageFactory`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetPreimageFactoryByID

- `in` **ID** — `IAIMPString`
- `out` **Factory** — `IAIMPExtensionPlaylistPreimageFactory`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetPreimageFactoryCount

- `out` **Result** — `Integer`

#### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlaylistManager2, ...);

#### Summary

- **Definition:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPExtensionPlaylistManagerListener

#### Description

This is extension for IAIMPServicePlaylistManager service, provides an ability to receive notifications about the changes in manager

#### Methods

##### PlaylistActivated

- `in` **Playlist** — `IAIMPPlaylist`

##### PlaylistAdded

- `in` **Playlist** — `IAIMPPlaylist`

##### PlaylistRemoved

- `in` **Playlist** — `IAIMPPlaylist`

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPExtensionPlaylistPreimageFactory

#### Description

Provides an ability to register custom preimage (data provider) factory for smart-playlists

#### Methods

##### CreatePreimage

Creates a new instance of preimage
Refer to the IAIMPPlaylistPreimage for more information.

- `out` **Intf** — `IAIMPPlaylistPreimage`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetID

Unique ID of factory. You must not change the ID during life time of the plugin, because ID will be stored to file of smart-playlist.

- `out` **ID** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetName

- `out` **Name** — `IAIMPString`
  Friendly name of the factory that displays to end user.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetFlags

0 or combinations of flags:
+ AIMP_PREIMAGEFACTORY_FLAG_CONTEXTDEPENDENT - an ability to create the preimage is depended from context. User will have no ability to create preimage via creating new smart-playlist menu.

- `out` **Result** — `DWORD`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlaylistManager2, ...);

#### Summary

- **Definition:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPExtensionPlaylistShuffler

#### Description

This extension provides plugin an ability to register custom shuffler algorithm that used to build shuffled playback queue.

#### Method

##### Shuffle

The method will be invoked each time when need to update playback queue indexes in the playlist.
Usually it happened after:

- Adding new files
- Recreating the queue
- Queue has been modified by user (for example, user has started some track manually)

- `in` **Playlist** — `IAIMPPlaylist`
- `in` **Items** — `IAIMPObjectList2`
  List of IAIMPPlaylistItem to update the `AIMP_PLAYLISTITEM_PROPID_PLAYBACKQUEUEINDEX` property.

  Note: list may contains not all track from the playlist, only the tracks to update. In this case, the `InitialIndex` property will specify a starting playback queue index for the items. Indexes **must** be unique and **must not** be below the `InitialIndex`. This was made to prevent tracks repeations while playing the playlist.
- `in` **InitialIndex** — `Integer`
  Starting playback queue index for the items. Indexes **must** be unique and **must not** be below the `InitialIndex`
- `out` **Result** — `HRESULT`
  Return S_OK if plugin has succeeded update playback queue indexes of the items. Any other result code will be treated as transferring to default algorithm.

#### Summary

- **Definition:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 6.00.3000

## Primitives

### Primitives

- IAIMPPlaylist
- IAIMPPlaylistGroup
- IAIMPPlaylistItem
- IAIMPPlaylistListener
- IAIMPPlaylistListener2
- IAIMPPlaylistPreimage
- IAIMPPlaylistPreimageDataProvider
- IAIMPPlaylistPreimageListener
- IAIMPPlaylistProperties
- IAIMPPlaylistQueue
- IAIMPPlaylistQueue2
- IAIMPPlaylistQueueListener
- Types

### IAIMPPlaylist

#### Properties

##### AIMP_PLAYLIST_PROPID_NAME

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_PLAYLIST_PROPID_GROUPNAME

Name of the group the playlist belongs to _((v5.40))_

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_PLAYLIST_PROPID_READONLY

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_FOCUSED_OBJECT

- **Type:** IAIMPPlaylistItem / IAIMPPlaylistGroup
- **Read:** IAIMPPropertyList.GetValueAsObject
- **Write:** IAIMPPropertyList.SetValueAsObject

##### AIMP_PLAYLIST_PROPID_ID

Unique playlist identificator

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

##### AIMP_PLAYLIST_PROPID_GROUPPING_OVERRIDEN

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_GROUPPING

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_GROUPPING_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_GROUPPING_TEMPLATE

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_GROUPPING_OVERRIDEN` parameter is not equal to 0

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_PLAYLIST_PROPID_GROUPPING_AUTOMERGING

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_GROUPPING_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_FORMATING_OVERRIDEN

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_FORMATING_LINE1_TEMPLATE

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_FORMATING_OVERRIDEN` parameter is not equal to 0

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_PLAYLIST_PROPID_FORMATING_LINE2_TEMPLATE

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_FORMATING_OVERRIDEN` parameter is not equal to 0

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_PLAYLIST_PROPID_VIEW_OVERRIDEN

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_VIEW_DURATION

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_VIEW_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_VIEW_EXPAND_BUTTONS

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_VIEW_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_VIEW_MARKS

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_VIEW_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_VIEW_NUMBERS

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_VIEW_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_VIEW_NUMBERS_ABSOLUTE

Each group will have own tracks numeration if value of this option is set to 0.
Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_VIEW_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_VIEW_SECOND_LINE

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_VIEW_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_VIEW_SWITCHES

Changing the value is available only if value of the `AIMP_PLAYLIST_PROPID_VIEW_OVERRIDEN` parameter is not equal to 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_FOCUSINDEX

Index of focused playlist item.
Index can be equal to `-1`, if no one item is focused.
Use the AIMP_PLAYLIST_PROPID_FOCUSED_OBJECT property to access to focused group.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_PLAYBACKCURSOR

Playback cursor

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_PLAYINGINDEX

can be equal to `-1`, if playing item was removed or playlist never played

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLIST_PROPID_SIZE

Total size, in bytes

- **Type:** Int64
- **Read:** IAIMPPropertyList.GetValueAsInt64

##### AIMP_PLAYLIST_PROPID_DURATION

Total duration, in seconds

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat

##### AIMP_PLAYLIST_PROPID_DURATION_REMAINING

Approximate duration of files remaining to playback _((since v5.40))_

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat

##### AIMP_PLAYLIST_PROPID_PREIMAGE

- **Type:** IAIMPPlaylistPreimage
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPPlaylistPreimage, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPPlaylistPreimage>)

#### Methods

##### Add

- `in` **Object** — `IAIMPString`
  IAIMPString with FileURI or IAIMPFileInfo (if AIMP_PLAYLIST_ADD_FLAGS_FILEINFO flag is presents)
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_PLAYLIST_ADD_FLAGS_NOCHECKFORMAT` - flag suppresses file format checking

  - `AIMP_PLAYLIST_ADD_FLAGS_NOEXPAND` - flag suppresses file expansion to few virtual files
  - `AIMP_PLAYLIST_ADD_FLAGS_NOASYNC` - file adding will be processed in main thread, the method will not return control until operation has been completed (not recommended)
  - `AIMP_PLAYLIST_ADD_FLAGS_FILEINFO` - flag shows that object is IAIMPFileInfo (otherwise object must be a IAIMPString)
- `in` **InsertIn** — `Integer`
  = -2 - adding the records to random position
  = -1 - adding the records to the end of playlist
  >= 0 - adding the records to the specified position
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### AddList

- `in` **ObjList** — `IAIMPObjectList`
  List of FileURI as IAIMPString or list of IAIMPFileInfo (if AIMP_PLAYLIST_ADD_FLAGS_FILEINFO flag is presents)
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_PLAYLIST_ADD_FLAGS_NOCHECKFORMAT` - flag suppresses file format checking

  - `AIMP_PLAYLIST_ADD_FLAGS_NOEXPAND` - flag suppresses file expansion to few virtual files
  - `AIMP_PLAYLIST_ADD_FLAGS_NOASYNC` - file adding will be processed in main thread, the method will not return control until operation has been completed (not recommended)
  - `AIMP_PLAYLIST_ADD_FLAGS_FILEINFO` - flag shows that object is IAIMPFileInfo (otherwise object must be a IAIMPString)
- `in` **InsertIn** — `Integer`
  = -2 - adding the records to random position
  = -1 - adding the records to the end of playlist
  >= 0 - adding the records to the specified position
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Delete

- `in` **Item** — `IAIMPPlaylistItem`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Delete2

- `in` **ItemIndex** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Delete3

- `in` **Physically** — `LongBool`
  0 or combination of following flags:
  + `AIMP_PLAYLIST_DELETE_FLAGS_PHYSICALLY` - flag provides an ability to remove files physically
  + `AIMP_PLAYLIST_DELETE_FLAGS_NOCONFIRMATION` - flag provides an ability to suppress any confirmations
- `in` **Proc** — `TAIMPPlaylistDeleteProc`
  Callback procedure
- `in` **UserData** — `Pointer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### DeleteAll

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Sort

- `in` **Mode** — `Integer`
  Sort mode, one of the following values:
  - AIMP_PLAYLIST_SORTMODE_TITLE
  - AIMP_PLAYLIST_SORTMODE_FILENAME
  - AIMP_PLAYLIST_SORTMODE_DURATION
  - AIMP_PLAYLIST_SORTMODE_ARTIST
  - AIMP_PLAYLIST_SORTMODE_INVERSE
  - AIMP_PLAYLIST_SORTMODE_RANDOMIZE
  - AIMP_PLAYLIST_SORTMODE_RANDOMIZE_GROUPS
  - AIMP_PLAYLIST_SORTMODE_RANDOMIZE_GROUPS_AND_IT_ITEMS
  - AIMP_PLAYLIST_SORTMODE_RANDOMIZE_GROUPITEMS
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Sort2

- `in` **Template** — `IAIMPString`
  Sort template. Refer to the IAIMPServiceFileInfoFormatter
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Sort3

- `in` **Proc** — `TAIMPPlaylistCompareProc`
  Custom comparing callback procedure
- `in` **UserData** — `Pointer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### BeginUpdate

Method blocks all notifications until EndUpdate is called.
This method is recommended to usage if you will change few options of playlist at one time.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### EndUpdate

Method unblocks all notifications. Refer to the BeginUpdate.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Close

- `in` **Flags** — `DWORD`
  0 or one of following values:
  - `AIMP_PLAYLIST_CLOSE_FLAGS_FORCE_REMOVE` - Ignores current settings and remove playlist from disk after closing
  - `AIMP_PLAYLIST_CLOSE_FLAGS_FORCE_UNLOAD` - Ignores current settings and not remove playlist from disk after closing
  Default: `0`.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetFiles

- `in` **Flags** — `DWORD`
  0 or combination of files:
  - `AIMP_PLAYLIST_GETFILES_FLAGS_SELECTED_ONLY`
  - `AIMP_PLAYLIST_GETFILES_FLAGS_VISIBLE_ONLY`
  - `AIMP_PLAYLIST_GETFILES_FLAGS_COLLAPSE_VIRTUAL` - In this case, the file-container will be added to the list if playlist item is virtual file
- `out` **List** — `IAIMPObjectList`
  List of IAIMPString
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### MergeGroup

Merges one or all groups with same names

- `in` **Group** — `IAIMPPlaylistGroup`
  Group to merge.

  All groups will be merged If group is not set (parameter is equals to `nil/null`).
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### ReloadFromPreimage

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - preimage is not set or playlist is read only

##### ReloadInfo

Reloads information about items (running in separate thread)

- `in` **Flags** — `DWORD`
  `AIMP_PLAYLIST_RELOADINFO_FLAGS_DEFAULT` - Information will be updated for files that does not have it
  `AIMP_PLAYLIST_RELOADINFO_FLAGS_FULL` - Information will be updated for all files
  `AIMP_PLAYLIST_RELOADINFO_FLAGS_SELECTED` - Information will be updated for selected files
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetItem

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  Must be set to IID_IAIMPPlaylistItem.
- `out` **Object** — `Untyped`
  Instance of interface
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetItemCount

- `out` **Result** — `Integer`

##### GetGroup

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  Must be set to IID_IAIMPPlaylistGroup.
- `out` **Object** — `Untyped`
  Instance of interface
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetGroupCount

- `out` **Result** — `Integer`

##### ListenerAdd

- `in` **Listener** — `IAIMPPlaylistListener`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### ListenerRemove

- `in` **Listener** — `IAIMPPlaylistListener`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPPlaylistGroup

#### Description

The IAIMPPlaylistGroup interface describes playlist group that can contains one or more playlist items

#### Parent

IAIMPPlaylistGroup inherited from IAIMPPropertyList.

#### Properties

##### AIMP_PLAYLISTGROUP_PROPID_NAME

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

##### AIMP_PLAYLISTGROUP_PROPID_EXPANDED

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLISTGROUP_PROPID_DURATION

Total duration of items in the group, in seconds.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat

##### AIMP_PLAYLISTGROUP_PROPID_INDEX

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

##### AIMP_PLAYLISTGROUP_PROPID_SELECTED

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### Methods

##### GetItem

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  IID of interface, must be set to the IID_IAIMPPlaylistItem.
- `out` **Object** — `Untyped`
  Instance of interface
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetItemCount

- `out` **Result** — `Integer`

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPPlaylistItem

#### Description

The IAIMPPlaylistItem is storage for information about the playlist item

#### Parent

IAIMPPlaylistItem inherits from IAIMPPropertyList.

#### Properties

##### AIMP_PLAYLISTITEM_PROPID_CUSTOM

Custom single line text field, can be defined by plugin. The value of this field stores to playlist.

Value of the field must not contains symbols \r, \n and "|".

Use the `%Custom` macro to use value of this field for grouping or sorting the records.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

##### AIMP_PLAYLISTITEM_PROPID_DISPLAYTEXT

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

##### AIMP_PLAYLISTITEM_PROPID_FILEINFO

- **Type:** IAIMPFileInfo
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPFileInfo, ..)
- **Write:** Via modifying the properties of the <IAIMPFileInfo> instance

##### AIMP_PLAYLISTITEM_PROPID_FILENAME

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

##### AIMP_PLAYLISTITEM_PROPID_GROUP

- **Type:** IAIMPPlaylistGroup
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPPlaylistGroup, ..)

##### AIMP_PLAYLISTITEM_PROPID_INDEX

Absolute item index in the playlist

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLISTITEM_PROPID_MARK

Mark, (0.0 to 5.0)

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

##### AIMP_PLAYLISTITEM_PROPID_PLAYBACKQUEUEINDEX

Index in the internal playback queue.
This index is different from playlist item index!

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

##### AIMP_PLAYLISTITEM_PROPID_PLAYINGSWITCH

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLISTITEM_PROPID_PLAYLIST

- **Type:** IAIMPPlaylist
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPPlaylist, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(.., ..)

##### AIMP_PLAYLISTITEM_PROPID_SELECTED

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### Methods

##### ReloadInfo

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

#### See also

- Creating custom playback queue

### IAIMPPlaylistListener

#### Description

Interface provides an ability to receive notifications about changes in the playlist

#### Methods

##### Activated

Event occurs when playlist is activating

##### Changed

- `in` **Flags** — `DWORD`
  Combination of following flags:
  - `AIMP_PLAYLIST_NOTIFY_NAME`
  - `AIMP_PLAYLIST_NOTIFY_GROUPNAME` _((v5.40))_
  - `AIMP_PLAYLIST_NOTIFY_SELECTION`
  - `AIMP_PLAYLIST_NOTIFY_MODIFIED`
  - `AIMP_PLAYLIST_NOTIFY_DEADSTATE` - one the files in playlist has been marked as "not found"
  - `AIMP_PLAYLIST_NOTIFY_MAKEVISIBLE` - user has send request to make playing item visible
  - `AIMP_PLAYLIST_NOTIFY_PLAYBACKQUEUE` - playback order of files in playlist has been changed
  - `AIMP_PLAYLIST_NOTIFY_PLAYBACKCURSOR` - Refer to the "playback cursor" topic
  - `AIMP_PLAYLIST_NOTIFY_PLAYBACKBOOKMARK` - position of seconds for the "playback cursor" _((v5.40))_
  - `AIMP_PLAYLIST_NOTIFY_FOCUSINDEX`
  - `AIMP_PLAYLIST_NOTIFY_CONTENT`
  - `AIMP_PLAYLIST_NOTIFY_FILEINFO`
  - `AIMP_PLAYLIST_NOTIFY_STATISTICS` - duration or size of playlist have been changed
  - `AIMP_PLAYLIST_NOTIFY_PLAYINGSWITCHS`
  - `AIMP_PLAYLIST_NOTIFY_READONLY`
  - `AIMP_PLAYLIST_NOTIFY_PREIMAGE`

##### Removed

Event occurs before deleting / unloading

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPPlaylistListener2

#### Description

Interface provides an ability to receive notifications about the state of tags scanning background thread.

#### Methods

##### ScanningBegin

##### ScanningProgress

- `in` **Progress** — `Double`
  Scanning progress, 0.0 .. 100.0 %

##### ScanningEnd

- `in` **HasChanges** — `LongBool`
- `in` **Canceled** — `LongBool`

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### IAIMPPlaylistPreimage

#### Description

The IAIMPPlaylistPreimage interface is a general interface for all preimages.

Preimage is data source for smart-playlists with manual or automatic synchronization. The principle of cooperation between preimage and playlist is so simple: when data or settings in preimage are changed - preimage notify playlist about the changes via the IAIMPPlaylistPreimageListener interface that related to binded playlist. Playlist, in own case, will reload data from preimage as soon as data will be required by plugin or user.

#### Parent

IAIMPPlaylistPreimage inherits from IAIMPPropertyList

#### Properties

##### AIMP_PLAYLISTPREIMAGE_PROPID_FACTORYID

ID of factory that creates this preimage

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

##### AIMP_PLAYLISTPREIMAGE_PROPID_AUTOSYNC

The Value different from 0 if automatic synchronization is switched on in the preimage (note that not all preimages support for this property).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLISTPREIMAGE_PROPID_AUTOSYNC_ON_STARTUP

The Value different from 0 if automatic synchronization is switched on in the preimage at Application startup (note that not all preimages support for this property).

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYLISTPREIMAGE_PROPID_HASDIALOG

Return value different from 0 if preimage has implementation of the ExecuteDialog method.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

##### AIMP_PLAYLISTPREIMAGE_PROPID_SORTTEMPLATE

Return sorting template for values in playlist after adding files from preimage

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### Methods

##### Initialize

- `in` **Listener** — `IAIMPPlaylistPreimageListener`

##### Finalize

##### ConfigLoad

- `in` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### ConfigSave

- `in` **Stream** — `IAIMPStream`
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

##### ExecuteDialog

- `in` **OwnerWnd** — `HWND`
  Handle of owner window.
  Set this variable to 0 to use handle of main window of the application.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Summary

- **Definition:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

#### See Also

- IAIMPExtensionPlaylistPreimageFactory
- IAIMPPlaylistPreimageDataProvider
- IAIMPPlaylistPreimageListener

### IAIMPPlaylistPreimageDataProvider

#### Description

Provides data for smart-playlist. Interface must be implemented on the same level as the IAIMPPlaylistPreimage interface.

#### Methods

##### GetFiles

- `in` **Owner** — `IAIMPTaskOwner`
  This interface provides an ability to check if task is canceling.
  Refer to the IAIMPTask for usage recommendations.
- `out` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_PLAYLIST_ADD_FLAGS_NOCHECKFORMAT` - flag suppresses file format checking

  - `AIMP_PLAYLIST_ADD_FLAGS_NOEXPAND` - flag suppresses file expansion to few virtual files
  - `AIMP_PLAYLIST_ADD_FLAGS_NOASYNC` - file adding will be processed in main thread, the method will not return control until operation has been completed (not recommended)
  - `AIMP_PLAYLIST_ADD_FLAGS_FILEINFO` - flag shows that object is IAIMPFileInfo (otherwise object must be a IAIMPString)
- `out` **List** — `IAIMPObjectList`
  List of FileURI like the IAIMPString or the IAIMPFileInfo
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPPlaylistPreimageListener

#### Description

The interface provides an ability to notify playlist about the changes in preimage.
Instance of interface creates by playlist and put to plugin via the IAIMPPlaylistPreimage.Initialize method.

#### Methods

##### DataChanged

##### SettingsChanged

#### Summary

- **Definition:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

### IAIMPPlaylistProperties

#### Description

The interface extends the IAIMPPropertyList2 and provides access to custom properties that loads/stores from/to playlist file (for AIMPPL4 and XSPF file formats).

An access to the IAIMPPlaylistProperties interface is provided by <IAIMPPlaylist>.QueryInterface(IID_IAIMPPlaylistProperties, ..);

#### Methods

##### GetCustomValue

- `in` **Name** — `IAIMPString`
  Custom property name
- `out` **Value** — `IAIMPString`
  Custom value, may contains a line breaks
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed.
  E_FAIL - The property was not defined.
  E_ACCESSDENIED - The method was called from non-main thread.

##### SetCustomValue

- `in` **Name** — `IAIMPString`
  Custom property name
- `in` **Value** — `IAIMPString`
  Custom value, may contains a line breaks.
  To remove the property, pass `nil/null` here.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed.
  E_ACCESSDENIED - The method was called from non-main thread.

#### Summary

- **Definition:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 5.40.2660

### IAIMPPlaylistQueue

#### Description

This interface provides an access to playback queue.

#### Properties

##### AIMP_PLAYLISTQUEUE_PROPID_SUSPENDED

Queue is suspended if value is not equals to zero

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### Methods

##### Add

- `in` **Item** — `IAIMPPlaylistItem`
- `in` **InsertAtBeginning** — `LongBool`
  Default: False.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### AddList

- `in` **ItemList** — `IAIMPObjectList`
  List of the IAIMPPlaylistItem values
- `in` **InsertAtBeginning** — `LongBool`
  Default: False.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Delete

- `in` **Item** — `IAIMPPlaylistItem`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Delete2

- `in` **Playlist** — `IAIMPPlaylist`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Move

- `in` **Item** — `IAIMPPlaylistItem`
- `in` **TargetIndex** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - Item is not exists in queue

##### Move2

- `in` **ItemIndex** — `Integer`
- `in` **TargetIndex** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetItem

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  IID of interface, must be equals to the IID_IAIMPPlaylistItem.
- `out` **Object** — `Untyped`
  Instance of interface
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetItemCount

- `out` **Result** — `Integer`

#### Access to service

<IAIMPServicePlaylistManager>.QueryInterface(IID_IAIMPPlaylistQueue, ...);

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPPlaylistQueue2

#### Description

IAIMPPlaylistQueue2 is extended version of the IAIMPPlaylistQueue

#### Methods

##### ListenerAdd

- `in` **Listener** — `IAIMPPlaylistQueueListener`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### ListenerRemove

- `in` **Listener** — `IAIMPPlaylistQueueListener`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_ACCESSDENIED - The method was called from non-main thread
  E_HANDLE - The object that is bound to the interface has been freed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to service

<IAIMPServicePlaylistManager>.QueryInterface(IID_IAIMPPlaylistQueue2, ...);

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### IAIMPPlaylistQueueListener

#### Description

Interface provides an ability to receive notifications about changes in the queue

#### Methods

##### ContentChanged

Event occurs when content of queue was changed

##### StateChanged

Event occurs when the `AIMP_PLAYLISTQUEUE_PROPID_SUSPENDED` property of IAIMPPlaylistQueue has been changed.

#### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### Types

#### Types

- TAIMPPlaylistCompareProc
- TAIMPPlaylistDeleteProc

#### TAIMPPlaylistCompareProc

##### Description

- `in` **Item1** — `IAIMPPlaylistItem`
- `in` **Item2** — `IAIMPPlaylistItem`
- `in` **UserData** — `Pointer`
- `out` **Result** — `Integer`
  = 0, if Item1 = Item2
  = -1, if Item1 < Item2
  = +1, if Item1 > Item2

##### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

#### TAIMPPlaylistDeleteProc

##### Description

- `in` **Item1** — `IAIMPPlaylistItem`
- `in` **UserData** — `Pointer`
- `out` **Result** — `LongBool`
  True - if item must be deleted from playlist

##### Summary

- **Definitions:** apiPlaylists.pas / apiPlaylists.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455
