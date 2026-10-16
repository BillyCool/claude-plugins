# Properties

## Properties

- AIMP_MSG_PROPERTY_ACTION_ON_END_OF_PLAYLIST
- AIMP_MSG_PROPERTY_ACTION_ON_END_OF_TRACK
- AIMP_MSG_PROPERTY_BALANCE
- AIMP_MSG_PROPERTY_CHORUS
- AIMP_MSG_PROPERTY_CROSSMIXING
- AIMP_MSG_PROPERTY_ECHO
- AIMP_MSG_PROPERTY_ENHANCER
- AIMP_MSG_PROPERTY_EQUALIZER
- AIMP_MSG_PROPERTY_EQUALIZER_AUTO
- AIMP_MSG_PROPERTY_EQUALIZER_BAND
- AIMP_MSG_PROPERTY_FLANGER
- AIMP_MSG_PROPERTY_HWND
- AIMP_MSG_PROPERTY_JUMP_TO_BEGINNING_ON_PREV_TRACK
- AIMP_MSG_PROPERTY_JUMP_TO_NEXT_TRACK
- AIMP_MSG_PROPERTY_LOADED
- AIMP_MSG_PROPERTY_MINIMIZED_TO_TRAY
- AIMP_MSG_PROPERTY_MUTE
- AIMP_MSG_PROPERTY_PARTREPEAT
- AIMP_MSG_PROPERTY_PARTREPEAT_RANGE
- AIMP_MSG_PROPERTY_PITCH
- AIMP_MSG_PROPERTY_PLAYER_BUFFERING
- AIMP_MSG_PROPERTY_PLAYER_DURATION
- AIMP_MSG_PROPERTY_PLAYER_POSITION
- AIMP_MSG_PROPERTY_PLAYER_STATE
- AIMP_MSG_PROPERTY_PREAMP
- AIMP_MSG_PROPERTY_RADIOCAP
- AIMP_MSG_PROPERTY_RADIOCAP_SINGLE_TRACK
- AIMP_MSG_PROPERTY_REPEAT
- AIMP_MSG_PROPERTY_REPEAT_SINGLE_FILE_PLAYLISTS
- AIMP_MSG_PROPERTY_REVERB
- AIMP_MSG_PROPERTY_REVERSETIME
- AIMP_MSG_PROPERTY_SHUFFLE
- AIMP_MSG_PROPERTY_SPEED
- AIMP_MSG_PROPERTY_STAYONTOP
- AIMP_MSG_PROPERTY_TEMPO
- AIMP_MSG_PROPERTY_TRUEBASS
- AIMP_MSG_PROPERTY_VISUAL_FULLSCREEN
- AIMP_MSG_PROPERTY_VOLUME

## AIMP_MSG_PROPERTY_ACTION_ON_END_OF_PLAYLIST

#### AIMP_MSG_PROPERTY_ACTION_ON_END_OF_PLAYLIST

Action on end of playlist

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit integer variable (Integer).
  0 - Jump to the next playlist
  1 - Repeat current playlist
  2 - Stand by
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_ACTION_ON_END_OF_TRACK

#### AIMP_MSG_PROPERTY_ACTION_ON_END_OF_TRACK

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit integer variable (Integer).

  0 - Default Action
  1 - Jump to next track and stop playback
  2 - Jump to next track and pause playback

  Default: 0
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.60.2160

### See also

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_BALANCE

#### AIMP_MSG_PROPERTY_BALANCE

Balance

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: -1.0 .. +1.0
  Default: 0.0
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_CHORUS

#### AIMP_MSG_PROPERTY_CHORUS

Chorus effect

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: 0.0 .. 1.0
  Default: 0.0 (switched off)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_CROSSMIXING

#### AIMP_MSG_PROPERTY_CROSSMIXING

Toggles state of cross-mixing the tracks sound effect

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: True
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.60.2160

### See also

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_ECHO

#### AIMP_MSG_PROPERTY_ECHO

Echo effect

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: 0.0 .. 1.0
  Default: 0.0 (switched off)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_ENHANCER

#### AIMP_MSG_PROPERTY_ENHANCER

Enhancer effect

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: 1.0 .. 5.0
  Default: 1.0 (switched off)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_EQUALIZER

#### AIMP_MSG_PROPERTY_EQUALIZER

Equalizer state (switched on / off)

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_EQUALIZER_AUTO

#### AIMP_MSG_PROPERTY_EQUALIZER_AUTO

State of the "auto load equalizer presets" option (switched on / off).

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2300

### See also

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_EQUALIZER_BAND

#### AIMP_MSG_PROPERTY_EQUALIZER_BAND

- `in` **Param1** — `Integer`
  LoWord: AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET
  HiWord: Band Index (from 0 to 18)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: -15.0 .. 15.0 dB
  Default: 0.0 dB
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Note

Param2 in the AIMP_MSG_EVENT_PROPERTY_VALUE event will be set to nil / null

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_FLANGER

#### AIMP_MSG_PROPERTY_FLANGER

Flanger effect

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: 0.0 .. 1.0
  Default: 0.0 (switched off)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_HWND

#### AIMP_MSG_PROPERTY_HWND

Handle of one of application windows. Read only.

- `var` **Param1** — `Integer`
  One of following values:
  - AIMP_MPH_MAINFORM
  - AIMP_MPH_APPLICATION
  - AIMP_MPH_TRAYCONTROL
  - AIMP_MPH_PLAYLISTFORM
  - AIMP_MPH_EQUALIZERFORM
- `var` **Param2** — `Pointer`
  Pointer to the HWND.
  In Linux, window handles are emulated by GUI API, they are not compatible with handles from 3rd-party apps or libraries.
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

## AIMP_MSG_PROPERTY_JUMP_TO_BEGINNING_ON_PREV_TRACK

#### AIMP_MSG_PROPERTY_JUMP_TO_BEGINNING_ON_PREV_TRACK

Toggles state of "the "previous track" action jumps to track beginning" option.

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 6.00.3052

### See also

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_JUMP_TO_NEXT_TRACK

#### AIMP_MSG_PROPERTY_JUMP_TO_NEXT_TRACK

Toggles state of the "automatically jump to next track" option

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: True
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2337

### See also

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_LOADED

#### AIMP_MSG_PROPERTY_LOADED

Property shows whether an application is initialized

- `in` **Param1** — `Integer`
  AIMP_MSG_PROPVALUE_GET
  Read Only
- `var` **Param2** — `Pointer`
  Pointer to LongBool
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

- AIMP_MSG_EVENT_LOADED

## AIMP_MSG_PROPERTY_MINIMIZED_TO_TRAY

#### AIMP_MSG_PROPERTY_MINIMIZED_TO_TRAY

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_MUTE

#### AIMP_MSG_PROPERTY_MUTE

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_PARTREPEAT

#### AIMP_MSG_PROPERTY_PARTREPEAT

Part repeat state. Read only

- `in` **Param1** — `Integer`
  AIMP_MSG_PROPVALUE_GET
  Read Only
- `in` **Param2** — `Pointer`
  Pointer to the 32-bit integer variable (Integer).
  0 - Repeat is switched off
  1 - Point "A" is defined
  2 - Point "B" is defined, repeat is switched on
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

- AIMP_MSG_CMD_TOGGLE_PARTREPEAT
- AIMP_MSG_EVENT_PROPERTY_VALUE

## AIMP_MSG_PROPERTY_PARTREPEAT_RANGE

#### AIMP_MSG_PROPERTY_PARTREPEAT_RANGE

Provides an ability to take or change part-repeat range.

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `in` **Param2** — `Pointer`
  Pointer to first element of array of two Single (32-bit floating point value) values.

  1st element is a position of the A point (in seconds) of part-repeat range or -1 if point is not specified
  2nd element is a position of the B point (in seconds) of part-repeat range or -1 if point is not specified
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 5.00.2300

### See also

- AIMP_MSG_CMD_TOGGLE_PARTREPEAT
- AIMP_MSG_EVENT_PROPERTY_VALUE

## AIMP_MSG_PROPERTY_PITCH

#### AIMP_MSG_PROPERTY_PITCH

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: -10.0 .. 10.0
  Default: 0.0 (switched off)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_PLAYER_BUFFERING

#### AIMP_MSG_PROPERTY_PLAYER_BUFFERING

Displays buffering progress of playing track

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Value in percents (from 0.0 to 100.0 %)
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Note

The AIMP_MSG_EVENT_PROPERTY_VALUE is not used here. Use the AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION instead.

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- AIMP_MSG_EVENT_PROPERTY_VALUE
- AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION

## AIMP_MSG_PROPERTY_PLAYER_DURATION

#### AIMP_MSG_PROPERTY_PLAYER_DURATION

- `in` **Param1** — `Integer`
  AIMP_MSG_PROPVALUE_GET
  Read Only
- `in` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Value is defined in seconds.
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_PLAYER_POSITION

#### AIMP_MSG_PROPERTY_PLAYER_POSITION

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Value is defined in seconds.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Note

The AIMP_MSG_EVENT_PROPERTY_VALUE event occurs on seeking operation only.

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.00.1660

### See also

- AIMP_MSG_EVENT_PROPERTY_VALUE
- AIMP_MSG_EVENT_PLAYER_UPDATE_POSITION

## AIMP_MSG_PROPERTY_PLAYER_STATE

#### AIMP_MSG_PROPERTY_PLAYER_STATE

- `in` **Param1** — `Integer`
  AIMP_MSG_PROPVALUE_GET
  Read Only
- `in` **Param2** — `Pointer`
  Pointer to the 32-bit integer variable (Integer).
  One of the following values:
  (0) AIMP_PLAYER_STATE_STOPPED
  (1) AIMP_PLAYER_STATE_PAUSED
  (2) AIMP_PLAYER_STATE_PLAYING
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

- AIMP_MSG_EVENT_PLAYER_STATE

## AIMP_MSG_PROPERTY_PREAMP

#### AIMP_MSG_PROPERTY_PREAMP

Preamp. Equalizer must be switched on, see AIMP_MSG_PROPERTY_EQUALIZER

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: -15.0 .. 15.0 dB
  Default: 0.0 dB
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

- AIMP_MSG_PROPERTY_EQUALIZER
- AIMP_MSG_EVENT_PROPERTY_VALUE

## AIMP_MSG_PROPERTY_RADIOCAP

#### AIMP_MSG_PROPERTY_RADIOCAP

State of internet radio capture.

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_RADIOCAP_SINGLE_TRACK

#### AIMP_MSG_PROPERTY_RADIOCAP_SINGLE_TRACK

State of capture of single track from internet radio.

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.60.2160

### See also

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_REPEAT

#### AIMP_MSG_PROPERTY_REPEAT

Track repeat state

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Value: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_REPEAT_SINGLE_FILE_PLAYLISTS

#### AIMP_MSG_PROPERTY_REPEAT_SINGLE_FILE_PLAYLISTS

State of "repeat single file playlists" option. It is actual for "repeat playlist" mode only (see AIMP_MSG_PROPERTY_ACTION_ON_END_OF_PLAYLIST)

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_REVERB

#### AIMP_MSG_PROPERTY_REVERB

Reverb effect

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: 0.0 .. 1.0
  Default: 0.0 (switched off)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_REVERSETIME

#### AIMP_MSG_PROPERTY_REVERSETIME

Switching on/off countdown mode of playback time

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Value: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_SHUFFLE

#### AIMP_MSG_PROPERTY_SHUFFLE

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_SPEED

#### AIMP_MSG_PROPERTY_SPEED

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: 0.5 .. 1.5 (50% .. 150%)
  Default: 1.0 (100%)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_STAYONTOP

#### AIMP_MSG_PROPERTY_STAYONTOP

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Values: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_TEMPO

#### AIMP_MSG_PROPERTY_TEMPO

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Values: 0.8 .. 1.5 (80% .. 150%)
  Default: 1.0 (100%)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_TRUEBASS

#### AIMP_MSG_PROPERTY_TRUEBASS

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: 0.0 .. 2.0
  Default: 0.0 (switched off)
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_VISUAL_FULLSCREEN

#### AIMP_MSG_PROPERTY_VISUAL_FULLSCREEN

Full screen visualization mode

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit logical variable (LongBool).
  Value: False / True
  Default: False
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event

## AIMP_MSG_PROPERTY_VOLUME

#### AIMP_MSG_PROPERTY_VOLUME

- `in` **Param1** — `Integer`
  Access direction: Read / Write (AIMP_MSG_PROPVALUE_GET / AIMP_MSG_PROPVALUE_SET)
- `var` **Param2** — `Pointer`
  Pointer to the 32-bit floating point variable (Single).
  Range: 0.0 .. 1.0
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

- The AIMP_MSG_EVENT_PROPERTY_VALUE event
