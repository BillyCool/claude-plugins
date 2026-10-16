# Events

## Events

- AIMP_MSG_EVENT_CMD_STATE
- AIMP_MSG_EVENT_EQUALIZER_PRESET_NAME
- AIMP_MSG_EVENT_FILEMARK
- AIMP_MSG_EVENT_DSP
- AIMP_MSG_EVENT_LANGUAGE
- AIMP_MSG_EVENT_LOADED
- AIMP_MSG_EVENT_OPTIONS
- AIMP_MSG_EVENT_OPTIONS_FRAME_LIST
- AIMP_MSG_EVENT_OPTIONS_FRAME_MODIFIED
- AIMP_MSG_EVENT_PLAYBACK_QUEUE
- AIMP_MSG_EVENT_PLAYER_STATE
- AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION
- AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION_HR
- AIMP_MSG_EVENT_PLAYING_FILE_INFO
- AIMP_MSG_EVENT_PROPERTY_VALUE
- AIMP_MSG_EVENT_SKIN
- AIMP_MSG_EVENT_STATISTICS_CHANGED
- AIMP_MSG_EVENT_STREAM_END
- AIMP_MSG_EVENT_STREAM_START
- AIMP_MSG_EVENT_STREAM_START_SUBTRACK
- AIMP_MSG_EVENT_TERMINATING
- AIMP_MSG_EVENT_VISUAL_PLUGIN
- AIMP_MSG_EVENT_UI_MODE

## AIMP_MSG_EVENT_CMD_STATE

#### AIMP_MSG_EVENT_CMD_STATE

Event occurs when state of command has been changed

- `in` **Param1** — `Integer`
  Command ID, see the "Commands" chapter
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK, if command is accessible

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- How to hook message?

## AIMP_MSG_EVENT_EQUALIZER_PRESET_NAME

#### AIMP_MSG_EVENT_EQUALIZER_PRESET_NAME

Event occurs when name of currently used preset has been changed.

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `PChar`
  Can be equal to `nil/null`.
  Read only.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_FILEMARK

#### AIMP_MSG_EVENT_FILEMARK

Event occurs when file mark has been changed

- `in` **Param1** — `Integer`
  New mark (from 0 to 5)
- `in` **Param2** — `PChar`
  File name. If file name is `nil/null` or empty its mean that marks for all files have been changed.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### WARNING!

You must not generate this event by yourself!

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_DSP

#### AIMP_MSG_EVENT_DSP

Event occurs on change the list of DSP/VST plugins or it states

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 5.30.2500

### See also

- How to hook message?

## AIMP_MSG_EVENT_LANGUAGE

#### AIMP_MSG_EVENT_LANGUAGE

Event occurs when localization has been changed

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- How to hook message?

## AIMP_MSG_EVENT_LOADED

#### AIMP_MSG_EVENT_LOADED

Event occurs when application completely initialized.

Note that plugin can be loaded after program initialization. You should check current state via the AIMP_MSG_PROPERTY_LOADED property if it needed.

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- AIMP_MSG_PROPERTY_LOADED
- How to hook message?

## AIMP_MSG_EVENT_OPTIONS

#### AIMP_MSG_EVENT_OPTIONS

Event occurs when some settings have been changed

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- How to hook message?

## AIMP_MSG_EVENT_OPTIONS_FRAME_LIST

#### AIMP_MSG_EVENT_OPTIONS_FRAME_LIST

Event occurs when list of sheet for Options Dialog has been changed

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- How to hook message?

## AIMP_MSG_EVENT_OPTIONS_FRAME_MODIFIED

#### AIMP_MSG_EVENT_OPTIONS_FRAME_MODIFIED

Event occurs when one of settings in the Option Dialog sheet has been changed by user

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- How to hook message?

## AIMP_MSG_EVENT_PLAYBACK_QUEUE

#### AIMP_MSG_EVENT_PLAYER_STATE

Event occurs when playback queue has been changed

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 5.10.2400

### See also

- How to hook message?

## AIMP_MSG_EVENT_PLAYER_STATE

#### AIMP_MSG_EVENT_PLAYER_STATE

Event occurs when player state has been changed

- `in` **Param1** — `Integer`
  One of the following values:
  (0) AIMP_PLAYER_STATE_STOPPED
  (1) AIMP_PLAYER_STATE_PAUSED
  (2) AIMP_PLAYER_STATE_PLAYING
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION

#### AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION

Unlike the AIMP_MSG_EVENT_PROPERTY_VALUE event for the AIMP_MSG_PROPERTY_PLAYER_POSITION property, this event occurs even second.
This event can be useful for update information about the playing track.

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION_HR

#### AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION_HR

Unlike the AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION event this event has higher resolution (about 10-15 calls per second)

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_PLAYING_FILE_INFO

#### AIMP_MSG_EVENT_PLAYING_FILE_INFO

Event occurs when information about the playing file has been changed.

Event not occurs:
1. On start playback (See AIMP_MSG_EVENT_STREAM_START, AIMP_MSG_EVENT_STREAM_START_SUBTRACK)
2. On stop playback (See AIMP_MSG_EVENT_STREAM_END)

- `in` **Param2** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_PROPERTY_VALUE

#### AIMP_MSG_EVENT_PROPERTY_VALUE

Event occurs when property value has been changed.
See the "Properties" chapter.

- `in` **Param1** — `Integer`
  Property ID
- `in` **Param2** — `Pointer`
  This parameter is same to Param2 for specified property
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### See also

- How to hook message?

## AIMP_MSG_EVENT_SKIN

#### AIMP_MSG_EVENT_SKIN

Event occurs when skin has been applied

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_STATISTICS_CHANGED

#### AIMP_MSG_EVENT_STATISTICS_CHANGED

Event occurs when statistics has been changed

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `PChar`
  File name. If file name is `nil/null` or empty its mean that statistic for all files have been changed.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Warning!

You must not generate this event by yourself!

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_STREAM_END

#### AIMP_MSG_EVENT_STREAM_END

Event occurs when track has been finished

- `in` **Param1** — `Integer`
  Contains zero or combination of following flags: AIMP_MES_END_OF_QUEUE, AIMP_MES_END_OF_PLAYLIST, AIMP_MES_END_OF_QUEUE
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### See also

- How to hook message?

## AIMP_MSG_EVENT_STREAM_START

#### AIMP_MSG_EVENT_STREAM_START

Event occurs when playback of track has been started

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_STREAM_START_SUBTRACK

#### AIMP_MSG_EVENT_STREAM_START_SUBTRACK

This event like to AIMP_MSG_EVENT_STREAM_START, but it occurs when playing radio stream and track has been changed

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_TERMINATING

#### AIMP_MSG_EVENT_TERMINATING

Event occurs when closing the application.

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- How to hook message?

## AIMP_MSG_EVENT_VISUAL_PLUGIN

#### AIMP_MSG_EVENT_VISUAL_PLUGIN

Event occurs when switching between visualizations

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- How to hook message?

## AIMP_MSG_EVENT_UI_MODE

#### AIMP_MSG_EVENT_UI_MODE

Event occurs on changing UI mode - accent color, day / night mode and etc.

- `in` **Param1** — `Integer`
  unused
- `in` **Param2** — `Pointer`
  unused
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 5.30.2500

### See also

- How to hook message?
