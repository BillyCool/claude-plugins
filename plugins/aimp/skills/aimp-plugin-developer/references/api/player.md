# Player

## Player

- Services
- Extensions
- Primitivies

## Services

### Services

- IAIMPServicePlayer
- IAIMPServicePlayer2
- IAIMPServicePlayerEqualizer
- IAIMPServicePlayerEqualizerPresets
- IAIMPServicePlaybackQueue
- IAIMPServicePlaybackQueue2
- IAIMPServiceWaveform

### IAIMPServicePlayer

#### Description

This service provides an access to playback control interface.

#### Properties

##### AIMP_PLAYER_PROPID_ACTION_ON_END_OF_TRACK

0 - Default
1 - Jump to next track and stop playback
2 - Jump to next track and suspend playback

See also: AIMP_PLAYER_PROPID_AUTOSWITCHING.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_AUTO_JUMP_TO_NEXT_TRACK

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_AUTOSWITCHING

Provides an ability to switch off all effects when switching between tracks automatically.
0 - switched off.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_AUTOSWITCHING_PAUSE_BETWEEN_TRACKS

In milliseconds. 0 - switched off.
See also: AIMP_PLAYER_PROPID_AUTOSWITCHING.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_AUTOSWITCHING_CROSSFADE

Time of cross fade effect when switching between tracks automatically, In milliseconds. 0 - switched off.
See also: AIMP_PLAYER_PROPID_AUTOSWITCHING.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_AUTOSWITCHING_FADEIN

Time of volume fade in effect at beginning of track when switching between tracks automatically, in milliseconds. 0 - switched off.
See also: AIMP_PLAYER_PROPID_AUTOSWITCHING.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_AUTOSWITCHING_FADEOUT

Time of volume fade out effect at ending of track when switching between tracks automatically, in milliseconds. 0 - switched off.
See also: AIMP_PLAYER_PROPID_AUTOSWITCHING.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_MANUALSWITCHING

Provides an ability to switch off all effects when switching between tracks manually.
0 - switched off.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_MANUALSWITCHING_CROSSFADE

Time of cross fade effect when switching between tracks manually, In milliseconds. 0 - switched off.
See also: AIMP_PLAYER_PROPID_MANUALSWITCHING.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_MANUALSWITCHING_FADEIN

Time of volume fade in effect at beginning of track when switching between tracks manually, in milliseconds. 0 - switched off.
See also: AIMP_PLAYER_PROPID_MANUALSWITCHING.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_MANUALSWITCHING_FADEOUT

Time of volume fade out effect at ending of track when switching between tracks manually, in milliseconds. 0 - switched off.
See also: AIMP_PLAYER_PROPID_MANUALSWITCHING.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

##### AIMP_PLAYER_PROPID_OUTPUT

Determines sound output parameters.
To fetch/change current device, use the IAIMPString as argument.
To fetch list of available devices, query the IAIMPObjectList.

- **Type:** IAIMPString / IAIMPObjectList
- **Read:** IAIMPPropertyList.GetValueAsObject
- **Write:** IAIMPPropertyList.SetValueAsObject

#### Methods

##### Play

- `in` **Item** — `IAIMPPlaybackQueueItem`
  Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Play2

- `in` **Item** — `IAIMPPlaylistItem`
  Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Play3

- `in` **Playlist** — `IAIMPPlaylist`
  Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Play4

- `in` **FileURI** — `IAIMPString`
  FileURI (can be file path to playlist)
- `in` **Flags** — `DWORD`
  Combination of following flags:
  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_FROM_PLAYLIST` - player will search file with this file name in all loaded playlists, if succeeded - will start play it.

  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_FROM_PLAYLIST_CAN_ADD` - this flag should be used with previous one, if file is not found in loaded playlists - it will be added to playlist (target playlist is chosen based on current settings)
  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_WITHOUT_ADDING_TO_PLAYLIST` - start file playback without adding it to playlist
  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_SUSPENDED` - pause playback on track beginningNote 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).

  Note 2: the method returns E_FAIL if file does not correspond to conditions that specified via flags.

  Note 3: if FileURI contains path to the playlist file, the `AIMP_SERVICE_PLAYER_FLAGS_PLAY_WITHOUT_ADDING_TO_PLAYLIST` flag ignored, because player cannot start playlist playback without importing it.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GoToNext

Same to the AIMP_MSG_CMD_NEXT.

Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GoToPrev

Same to the AIMP_MSG_CMD_PREV.

Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetDuration

Duration of the playing file. Same to the AIMP_MSG_PROPERTY_PLAYER_DURATION.

- `out` **Seconds** — `Double`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

##### GetPosition

Playback position. Same to the AIMP_MSG_PROPERTY_PLAYER_POSITION.

- `out` **Seconds** — `Double`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

##### SetPosition

Set new playback position. Same to the AIMP_MSG_PROPERTY_PLAYER_POSITION.

- `out` **Seconds** — `Double`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

##### GetMute

Same to the AIMP_MSG_PROPERTY_MUTE.

- `out` **Value** — `LongBool`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### SetMute

Same to the AIMP_MSG_PROPERTY_MUTE.

- `in` **Value** — `LongBool`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetVolume

Current volume level (from 0.0 to 1.0). Same to the AIMP_MSG_PROPERTY_VOLUME.

- `out` **Level** — `Single`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### SetVolume

Set current volume level (from 0.0 to 1.0). Same to the AIMP_MSG_PROPERTY_VOLUME.

- `in` **Level** — `Single`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetInfo

Method provides an access to information about the playing file.

Player provides a reference to global instance of interface with information about playing file. You must not change it properties. If you want to edit some properties, you must create a copy of object via IAIMPFileInfo.Clone.

- `in` **FileInfo** — `IAIMPFileInfo`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

##### GetPlaylistItem

- `out` **Item** — `IAIMPPlaylistItem`
  Item of playing file in the playlist
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

##### GetState

Same to the AIMP_MSG_PROPERTY_PLAYER_STATE.

- `out` **Result** — `Integer`
  One of the following values:
  (0) AIMP_PLAYER_STATE_STOPPED
  (1) AIMP_PLAYER_STATE_PAUSED
  (2) AIMP_PLAYER_STATE_PLAYING

##### Pause

Same to the AIMP_MSG_CMD_PAUSE.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

##### Resume

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

##### Stop

Same to the AIMP_MSG_CMD_STOP.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

##### StopAfterTrack

Same to the AIMP_MSG_PROPERTY_ACTION_ON_END_OF_TRACK.

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_FAIL - if nothing is playing

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlayer, ...);

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Extensions:** IAIMPExtensionPlayerHook
- **Applications:** Player
- **Minimal Version:** 3.60.1455

#### See also

- AIMP_MSG_CMD_PLAY
- AIMP_MSG_CMD_PAUSE
- AIMP_MSG_CMD_STOP
- AIMP_MSG_CMD_NEXT
- AIMP_MSG_CMD_PREV
- AIMP_MSG_EVENT_STREAM_END
- AIMP_MSG_EVENT_STREAM_START
- AIMP_MSG_EVENT_STREAM_START_SUBTRACK
- AIMP_MSG_EVENT_PLAYER_STATE
- AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION
- AIMP_MSG_EVENT_PLAYING_FILE_INFO

### IAIMPServicePlayer2

#### Description

Extends API of the IAIMPServicePlayer service.

#### Methods

##### Play

- `in` **Item** — `IAIMPPlaybackQueueItem`
  Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).
- `in` **Offset** — `Single`
  Initial position in seconds.
  Set position to `-1` to allow player to catch automatic bookmark for the track.
- `in` **Flags** — `DWORD`
  0 or combination of following flags:
  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_SUSPENDED` - pause playback on track beginningNote 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Play2

- `in` **Item** — `IAIMPPlaylistItem`
  Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).
- `in` **Offset** — `Single`
  Initial position in seconds.
  Set position to `-1` to allow player to catch automatic bookmark for the track.
- `in` **Flags** — `DWORD`
  0 or combination of following flags:
  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_SUSPENDED` - pause playback on track beginningNote 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### Play4

- `in` **FileURI** — `IAIMPString`
  FileURI (can be file path to playlist)
- `in` **Offset** — `Single`
  Initial position in seconds.
  Set position to `-1` to allow player to catch automatic bookmark for the track.
- `in` **Flags** — `DWORD`
  Combination of following flags:
  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_FROM_PLAYLIST` - player will search file with this file name in all loaded playlists, if succeeded - will start play it.

  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_FROM_PLAYLIST_CAN_ADD` - this flag should be used with previous one, if file is not found in loaded playlists - it will be added to playlist (target playlist is chosen based on current settings)
  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_WITHOUT_ADDING_TO_PLAYLIST` - start file playback without adding it to playlist
  - `AIMP_SERVICE_PLAYER_FLAGS_PLAY_SUSPENDED` - pause playback on track beginningNote 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).

  Note 2: the method returns E_FAIL if file does not correspond to conditions that specified via flags.

  Note 3: if FileURI contains path to the playlist file, the `AIMP_SERVICE_PLAYER_FLAGS_PLAY_WITHOUT_ADDING_TO_PLAYLIST` flag ignored, because player cannot start playlist playback without importing it.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlayer2, ...);

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Extensions:** IAIMPExtensionPlayerHook
- **Applications:** Player
- **Minimal Version:** 5.00.2300

#### See also

- IAIMPServicePlayer

### IAIMPServicePlayerEqualizer

#### Description

Service provides an access to equalizer.
Inherits from IAIMPEqualizerBands.

#### Methods

##### GetActive

Same to AIMP_MSG_PROPERTY_EQUALIZER

- `out` **Result** — `BOOL`

##### SetActive

Same to AIMP_MSG_PROPERTY_EQUALIZER

- `in` **Value** — `BOOL`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetPreamp

Same to AIMP_MSG_PROPERTY_PREAMP

- `out` **Value** — `double`
  Preamp value in range of -15.0 to +15.0 dB.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### SetPreamp

Same to AIMP_MSG_PROPERTY_PREAMP

- `in` **Value** — `double`
  Preamp value in range of -15.0 to +15.0 dB.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetPreset

- `in` **IID** — `TGUID`
  Put the IID_IAIMPEqualizerPreset to take the IAIMPEqualizerPreset object.
- `out` **Preset** — `Untyped`
  Object instance
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread
  E_FAIL - preset is not selected

##### SetPreset

Activates the preset

- `in` **Preset** — `IAIMPEqualizerPreset`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlayerEqualizer, ...);

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2322

#### See also

- AIMP_MSG_PROPERTY_EQUALIZER
- AIMP_MSG_PROPERTY_EQUALIZER_BAND
- AIMP_MSG_EVENT_EQUALIZER_PRESET_NAME

### IAIMPServicePlayerEqualizerPresets

#### Description

Service provides an access to equalizer presets library.

#### Method

##### Add

- `in` **Name** — `IAIMPString`
- `in` **IID** — `TGUID`
  Put the IID_IAIMPEqualizerPreset to take the IAIMPEqualizerPreset object.
- `out` **Preset** — `Untyped`
  Object instance
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### FindByName

- `in` **Name** — `IAIMPString`
- `in` **IID** — `TGUID`
  Put the IID_IAIMPEqualizerPreset to take the IAIMPEqualizerPreset object.
- `out` **Preset** — `Untyped`
  Object instance
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### Delete

- `in` **Preset** — `IAIMPEqualizerPreset`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### Delete2

- `in` **Index** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetPreset

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
  Put the IID_IAIMPEqualizerPreset to take the IAIMPEqualizerPreset object.
- `out` **Preset** — `Untyped`
  Object instance
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetPresetCount

- `out` **Result** — `Integer`

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlayerEqualizerPresets, ...);

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2322

### IAIMPServicePlaybackQueue

#### Description

Service provides an access to internal playback queue (do not confuse with IAIMPPlaylistQueue).
Internal playback queue based (by default) on content of playlist and state of the "Shuffle" mode, but can be overridden by plugin via an extension for the IAIMPServicePlaybackQueue service.

#### Methods

##### GetNextTrack

Function returns next track. Calculation must be based on current playing file.

- `out` **Item** — `IAIMPPlaybackQueueItem`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

##### GetPrevTrack

Function returns previous track. Calculation must be based on current playing file.

- `out` **Item** — `IAIMPPlaybackQueueItem`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlaybackQueue, ...);

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Extensions:** IAIMPExtensionPlaybackQueue
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPServicePlaybackQueue2

#### Description

Extends abilities of the IAIMPServicePlaybackQueue service.

#### Methods

##### NotifyChanged

Notifiers the player about changes in playback queue that implemented by a plugin via the IAIMPExtensionPlaybackQueue extension.

- `in` **Sender** — `IAIMPExtensionPlaybackQueue`
  Reference to playback queue interface.

#### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServicePlaybackQueue2, ...);

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2300

### IAIMPServiceWaveform

#### Description

Service provides an ability to register custom data provider for the waveform-navigator.

#### Access to Service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceWaveform, ...);

#### Summary

- **Definition:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** not supported
- **Extensions:** IAIMPExtensionWaveformProvider
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## Extensions

### Extensions

- IAIMPExtensionPlayerHook
- IAIMPExtensionPlaybackQueue
- IAIMPExtensionPlaybackQueue2
- IAIMPExtensionWaveformProvider

### IAIMPExtensionPlayerHook

#### Description

This is extension for the IAIMPServicePlayer service, it provides an ability to check an external URL and replace it (if needed). This can be useful if external server requires to set additional parameters for playback stream that can not be stored in playlist (an authorization data, for example).

Interface implementation must support asynchronous access.

#### Methods

##### OnCheckURL

Event occurs when trying to open a remote URL in the player.

- `in` **URL** — `IAIMPString`
- `var` **Handled** — `LongBool`
  Plugin should set the Handled parameter to True if it processes this call.

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPExtensionPlaybackQueue

#### Description

This extension provides an ability to override internal playback queue.

**Warning**! Next / previous track must be calculated based on value of the Current parameter. In general, it may not match the currently playing track. Also, player can request information about next / previous track several times.

Plugin must not take into account the value of the `AIMP_PLAYLISTITEM_PROPID_PLAYINGSWITCH` property of theIAIMPPlaylistItem during search of next / previous track, this parameter will be checked automatically on player side.

#### Methods

##### GetNext

Event occurs when player is looking for next track for playback

- `in` **Current** — `IUnknown`
  Current position in queue from which the next one is calculated (see `flags`)
  In general, it may not match the currently playing track.
- `in` **Flags** — `DWORD`
  The flags shows, how value of the Current parameter must be interpreted.
  For Now, the Flags parameter can contains one of following values:
  - `AIMP_PLAYBACKQUEUE_FLAGS_START_FROM_BEGINNING` - queue should return first item in the playlist. The Current is IAIMPPlaylist
  - `AIMP_PLAYBACKQUEUE_FLAGS_START_FROM_CURSOR` - queue should return item next after the playback cursor. The Current is IAIMPPlaylist
  - `AIMP_PLAYBACKQUEUE_FLAGS_START_FROM_ITEM` - queue should return item next after the Current. The Current is IAIMPPlaylistItem
- `in` **QueueItem** — `IAIMPPlaybackQueueItem`
  Interface instance that contains information about the track. Must be populated on plugin side.
- `out` **Result** — `LongBool`
  False - queue is switched off.

  Note that even if the queue could not find the record suitable to search parameters, this method must populate the QueueItem parameter and return the True value as result.

##### GetPrev

Event occurs when player is looking for previous track for playback

- `in` **Current** — `IUnknown`
  Current position in queue from which the previous one is calculated (see `flags`)
  In general, it may not match the currently playing track.
- `in` **Flags** — `DWORD`
  The flags shows, how value of the Current parameter must be interpreted.
  For Now, the Flags parameter can contains one of following values:
  - `AIMP_PLAYBACKQUEUE_FLAGS_START_FROM_BEGINNING` - queue should return last item in the playlist. The Current is IAIMPPlaylist
  - `AIMP_PLAYBACKQUEUE_FLAGS_START_FROM_CURSOR` - queue should return item previous before the playback cursor. The Current is IAIMPPlaylist
  - `AIMP_PLAYBACKQUEUE_FLAGS_START_FROM_ITEM` - queue should return item previous before the Current. The Current is IAIMPPlaylistItem
- `in` **QueueItem** — `IAIMPPlaybackQueueItem`
  Interface instance that contains information about the track. Must be populated on plugin side.
- `out` **Result** — `LongBool`
  False - queue is switched off.

  Note that even if the queue could not find the record suitable to search parameters, this method must populate the QueueItem parameter and return the True value as result.

##### OnSelect

Event occurs when playback of the Item is started. Plugin must not change properties of the Item.

- `in` **Item** — `IAIMPPlaylistItem`
- `in` **QueueItem** — `IAIMPPlaybackQueueItem`

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### IAIMPExtensionPlaybackQueue2

#### Description

Extends an abilities of the IAIMPExtensionPlaybackQueue.

#### Methods

##### GetInfo

Returns information about the queue size and position of the Current item in it.

- `in` **Current** — `IUnknown`
  Current item, IAIMPPlaylistItem.
- `out` **Position** — `Integer`
  Position of the current item in playback queue (1-based). Must return 0 if position is unknown.
- `out` **Size** — `Integer`
  Size of the queue. Must return 0 if size is unknown.
- `out` **Result** — `LongBool`

#### Notifications

Plugin must call the IAIMPServicePlaybackQueue2.NotifyChanged method if order of items in it own playback queue has been changed.

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2300

### IAIMPExtensionWaveformProvider

#### Description

This is an extension for the IAIMPServiceWaveform service that allows to plugin register custom data provider for the waveform-navigator

Interface implementation must support asynchronous access.

#### Methods

##### Calculate

- `in` **FileURI** — `IAIMPString`
  FileURI
- `in` **TaskOwner** — `IAIMPTaskOwner`
  This interface provides an ability to check if task is canceling.
  Refer to the IAIMPTask for usage recommendations.
- `in` **Peaks** — `PAIMPWaveformPeakInfoArray`
  Pointer to first element of the TAIMPWaveformPeakInfo array.

  Plugin must calculate the "wave" for the FileURI in resolution of `PeakCount` points and populate this array.
- `in` **PeakCount** — `Integer`
  Size (elements count) of the Peaks array
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise

#### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

#### Summary

- **Definition:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815

## Primitivies

### Primitivies

- IAIMPEqualizerBands
- IAIMPEqualizerPreset
- IAIMPPlaybackQueueItem
- TAIMPWaveformPeakInfo

### IAIMPEqualizerBands

#### Descriptions

IAIMPEqualizerBands is general interface to access to equalizer bands.

#### Methods

##### GetBandCount

- `out` **Result** — `Integer`
  Band count

##### GetBandFrequency

- `int` **BandIndex** — `Integer`
  Band index, started from 0.
- `out` **Value** — `double`
  Band frequency, in Hz.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### GetBandGain

- `int` **BandIndex** — `Integer`
  Band index, started from 0.
- `out` **Value** — `double`
  Current gain level, in range of -15.0 to +15.0 dB.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### SetBandGain

- `int` **BandIndex** — `Integer`
  Band index, started from 0.
- `in` **Value** — `double`
  Current gain level, in range of -15.0 to +15.0 dB.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2322

### IAIMPEqualizerPreset

#### Description

Interface provides an access to the equalizer preset.
Inherits from IAIMPEqualizerBands.

#### Methods

##### GetName

- `out` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

##### SetName

- `in` **S** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2322

### IAIMPPlaybackQueueItem

#### Description

Interface provides an access to extended information about the track in the playback queue.

#### Parent

IAIMPPlaybackQueueItem is inherited from IAIMPPropertyList.

#### Properties

##### AIMP_PLAYBACKQUEUEITEM_PROPID_CUSTOM

This is a user data parameter, it allow you to bind custom data to the interface.

- **Type:** IUnknown
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IUnknown, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IUnknown>)

##### AIMP_PLAYBACKQUEUEITEM_PROPID_PLAYLISTITEM

Playlist item. can be equal to `nil / null`, in this case, playback will be stopped.

- **Type:** IAIMPPlaylistItem
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPPlaylistItem, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPPlaylistItem>)

##### AIMP_PLAYBACKQUEUEITEM_PROPID_OFFSET

Initial playback offset, in seconds. The -1 value means that offset is not specified.
Provides an ability to start playback from specified position.

Note, the property is available since v5.01.

- **Type:** Double
- **Read:** IAIMPPropertyList.GetValueAsFloat
- **Write:** IAIMPPropertyList.SetValueAsFloat

#### Summary

- **Definitions:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### TAIMPWaveformPeakInfo

#### Description

##### TAIMPWaveformPeakInfo

- `in` **MaxNegative** — `Word`
  Maximal absolute value from negative values from data block that presented by this point.
- `in` **MaxPositive** — `Word`
  Maximal absolute value from positive values from data block that presented by this point.

#### Summary

- **Definition:** apiPlayer.pas / apiPlayer.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.10.1815
