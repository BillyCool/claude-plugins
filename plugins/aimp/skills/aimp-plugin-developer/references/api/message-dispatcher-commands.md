# Commands

## Commands

- AIMP_MSG_CMD_STATE_GET
- AIMP_MSG_CMD_ABOUT
- AIMP_MSG_CMD_ADD_FILES
- AIMP_MSG_CMD_ADD_FOLDERS
- AIMP_MSG_CMD_ADD_PLAYLISTS
- AIMP_MSG_CMD_ADD_URL
- AIMP_MSG_CMD_BOOKMARKS
- AIMP_MSG_CMD_BOOKMARKS_ADD
- AIMP_MSG_CMD_BRING_TO_TOP
- AIMP_MSG_CMD_DSPMANAGER
- AIMP_MSG_CMD_NEXT
- AIMP_MSG_CMD_OPEN_FILES
- AIMP_MSG_CMD_OPEN_FOLDERS
- AIMP_MSG_CMD_OPEN_PLAYLISTS
- AIMP_MSG_CMD_OPTIONS
- AIMP_MSG_CMD_PAUSE
- AIMP_MSG_CMD_PLAY
- AIMP_MSG_CMD_PLAYPAUSE
- AIMP_MSG_CMD_PLAY_PREV_PLAYLIST
- AIMP_MSG_CMD_PLS_DELETE_ALL
- AIMP_MSG_CMD_PLS_DELETE_DUPLICATES
- AIMP_MSG_CMD_PLS_DELETE_NON_EXISTS
- AIMP_MSG_CMD_PLS_DELETE_NON_SELECTED
- AIMP_MSG_CMD_PLS_DELETE_PLAYING_FROM_HDD
- AIMP_MSG_CMD_PLS_DELETE_SELECTED
- AIMP_MSG_CMD_PLS_DELETE_SELECTED_FROM_HDD
- AIMP_MSG_CMD_PLS_DELETE_SELECTED_FROM_HDD_W_FOLDERS
- AIMP_MSG_CMD_PLS_DELETE_SWITCHEDOFF
- AIMP_MSG_CMD_PLS_DELETE_SWITCHEDOFF_FROM_HDD
- AIMP_MSG_CMD_PLS_FOCUS_PLAYING
- AIMP_MSG_CMD_PLS_RELOAD_FROM_PREIMAGE
- AIMP_MSG_CMD_PLS_RESCAN
- AIMP_MSG_CMD_PLS_RESCAN_SELECTED
- AIMP_MSG_CMD_PLS_SORT_BY_ARTIST
- AIMP_MSG_CMD_PLS_SORT_BY_DURATION
- AIMP_MSG_CMD_PLS_SORT_BY_PATH
- AIMP_MSG_CMD_PLS_SORT_BY_TITLE
- AIMP_MSG_CMD_PLS_SORT_INVERT
- AIMP_MSG_CMD_PLS_SORT_RANDOMIZE
- AIMP_MSG_CMD_PLS_SWITCH_ON
- AIMP_MSG_CMD_PLS_SWITCH_OFF
- AIMP_MSG_CMD_PLUGINS
- AIMP_MSG_CMD_PREV
- AIMP_MSG_CMD_QFI
- AIMP_MSG_CMD_QFI_PLAYING_TRACK
- AIMP_MSG_CMD_QTE_PLAYING_TRACK
- AIMP_MSG_CMD_QUIT
- AIMP_MSG_CMD_SAVE_PLAYLISTS
- AIMP_MSG_CMD_SCHEDULER
- AIMP_MSG_CMD_SEARCH
- AIMP_MSG_CMD_SHOW_NOTIFICATION
- AIMP_MSG_CMD_STOP
- AIMP_MSG_CMD_TOGGLE_PARTREPEAT
- AIMP_MSG_CMD_VISUAL_NEXT
- AIMP_MSG_CMD_VISUAL_PREV
- AIMP_MSG_CMD_VISUAL_START
- AIMP_MSG_CMD_VISUAL_STOP

## AIMP_MSG_CMD_STATE_GET

#### AIMP_MSG_CMD_STATE_GET

This messages provides an ability to check command accessibility

- `in` **Param1** — `Integer`
  Command ID.
  See the "Commands" chapter
- `in` **Param2** — `Pointer`
  not used
- `out` **Result** — `HRESULT`
  S_OK, if command accessible

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Applications:** Player
- **Minimal Version:** 3.60.1455

## AIMP_MSG_CMD_ABOUT

#### AIMP_MSG_CMD_ABOUT

Show the "About" dialog

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

## AIMP_MSG_CMD_ADD_FILES

#### AIMP_MSG_CMD_ADD_FILES

Show the "File Adding" dialog

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

## AIMP_MSG_CMD_ADD_FOLDERS

#### AIMP_MSG_CMD_ADD_FOLDERS

Show the "Folder adding" dialog

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

## AIMP_MSG_CMD_ADD_PLAYLISTS

#### AIMP_MSG_CMD_ADD_PLAYLISTS

Show the "Playlists adding" dialog

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

## AIMP_MSG_CMD_ADD_URL

#### AIMP_MSG_CMD_ADD_URL

Show the "Add URL" dialog

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

## AIMP_MSG_CMD_BOOKMARKS

#### AIMP_MSG_CMD_BOOKMARKS

Show the "Bookmarks Manager" dialog

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

## AIMP_MSG_CMD_BOOKMARKS_ADD

#### AIMP_MSG_CMD_BOOKMARKS_ADD

Add file(s) to bookmarks

- `in` **Param1** — `Integer`
  0 - add playing file
  1 - add selected files from active playlist
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

## AIMP_MSG_CMD_BRING_TO_TOP

#### AIMP_MSG_CMD_BRING_TO_TOP

Brings main window of the app to top.
Restores the window If it was minimized to tray/taskbar.

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
- **Minimal Version:** 6.00.3000

## AIMP_MSG_CMD_DSPMANAGER

#### AIMP_MSG_CMD_DSPMANAGER

Show the "DSP Manager" dialog

- `in` **Param1** — `Integer`
  Index of tab sheet to active, 0..3.
  0 - Common settings (default)
  1 - Equalizer
  2 - Volume normalization
  3 - Cross mixing settings
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

## AIMP_MSG_CMD_NEXT

#### AIMP_MSG_CMD_NEXT

Jump to next track.

Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).

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

## AIMP_MSG_CMD_OPEN_FILES

#### AIMP_MSG_CMD_OPEN_FILES

Show the "Open files" dialog

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

## AIMP_MSG_CMD_OPEN_FOLDERS

#### AIMP_MSG_CMD_OPEN_FOLDERS

Show the "Open folders" dialog

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

## AIMP_MSG_CMD_OPEN_PLAYLISTS

#### AIMP_MSG_CMD_OPEN_PLAYLISTS

Show the "Open Playlists" dialog

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

## AIMP_MSG_CMD_OPTIONS

#### AIMP_MSG_CMD_OPTIONS

Show options dialog

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

## AIMP_MSG_CMD_PAUSE

#### AIMP_MSG_CMD_PAUSE

Pause / Resume

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

## AIMP_MSG_CMD_PLAY

#### AIMP_MSG_CMD_PLAY

If player is stopped - starts playback.
If player is paused - resumes playback.
If player is playing - start playing from beginning.

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

## AIMP_MSG_CMD_PLAYPAUSE

#### AIMP_MSG_CMD_PLAYPAUSE

If player is stopped - starts playback.
If player is paused - resumes playback.
If player is playing - pauses playback.

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

## AIMP_MSG_CMD_PLAY_PREV_PLAYLIST

#### AIMP_MSG_CMD_PLAY_PREV_PLAYLIST

Start playback of previous playing playlist

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

## AIMP_MSG_CMD_PLS_DELETE_ALL

#### AIMP_MSG_CMD_PLS_DELETE_ALL

Delete all tracks from active playlist

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

## AIMP_MSG_CMD_PLS_DELETE_DUPLICATES

#### AIMP_MSG_CMD_PLS_DELETE_DUPLICATES

Delete duplicate tracks from active playlist.
Tracks will be compared by full file name.

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

## AIMP_MSG_CMD_PLS_DELETE_NON_EXISTS

#### AIMP_MSG_CMD_PLS_DELETE_NON_EXISTS

Remove non exists tracks from active playlist

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

## AIMP_MSG_CMD_PLS_DELETE_NON_SELECTED

#### AIMP_MSG_CMD_PLS_DELETE_NON_SELECTED

Remove all tracks from active playlist except selected

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

## AIMP_MSG_CMD_PLS_DELETE_PLAYING_FROM_HDD

#### AIMP_MSG_CMD_PLS_DELETE_PLAYING_FROM_HDD

Remove playing file from disk drive

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

## AIMP_MSG_CMD_PLS_DELETE_SELECTED

#### AIMP_MSG_CMD_PLS_DELETE_SELECTED

Delete selected tracks from active playlist

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

## AIMP_MSG_CMD_PLS_DELETE_SELECTED_FROM_HDD

#### AIMP_MSG_CMD_PLS_DELETE_SELECTED_FROM_HDD

Delete selected tracks from disk drive

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

## AIMP_MSG_CMD_PLS_DELETE_SELECTED_FROM_HDD_W_FOLDERS

#### AIMP_MSG_CMD_PLS_DELETE_SELECTED_FROM_HDD_W_FOLDERS

Removes selected tracks from disk drive with it folders.

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
- **Minimal Version:** 5.30.2500

## AIMP_MSG_CMD_PLS_DELETE_SWITCHEDOFF

#### AIMP_MSG_CMD_PLS_DELETE_SWITCHEDOFF

Delete switched off tracks from active playlist

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

## AIMP_MSG_CMD_PLS_DELETE_SWITCHEDOFF_FROM_HDD

#### AIMP_MSG_CMD_PLS_DELETE_SWITCHEDOFF_FROM_HDD

Delete switched off tracks from disk drive

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

## AIMP_MSG_CMD_PLS_FOCUS_PLAYING (AIMP_MSG_CMD_PLS_FOCUS_NOWPLAYING)

#### AIMP_MSG_CMD_PLS_FOCUS_PLAYING

Activate playing playlist and focus playing file

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

## AIMP_MSG_CMD_PLS_RELOAD_FROM_PREIMAGE

#### AIMP_MSG_CMD_PLS_RELOAD_FROM_PREIMAGE

Synchronize active playlist with preimage if it presents.

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

## AIMP_MSG_CMD_PLS_RESCAN

#### AIMP_MSG_CMD_PLS_RESCAN

Reload file tags for all tracks in active playlist

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

## AIMP_MSG_CMD_PLS_RESCAN_SELECTED

#### AIMP_MSG_CMD_PLS_RESCAN

Reload file tags for selected tracks in active playlist

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

## AIMP_MSG_CMD_PLS_SORT_BY_ARTIST

#### AIMP_MSG_CMD_PLS_SORT_BY_ARTIST

Sort tracks in active playlist by artist field

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

## AIMP_MSG_CMD_PLS_SORT_BY_DURATION

#### AIMP_MSG_CMD_PLS_SORT_BY_DURATION

Sort tracks in active playlist by duration field

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

## AIMP_MSG_CMD_PLS_SORT_BY_PATH (AIMP_MSG_CMD_PLS_SORT_BY_FOLDER)

#### AIMP_MSG_CMD_PLS_SORT_BY_PATH

Sort tracks in active playlist by path

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

## AIMP_MSG_CMD_PLS_SORT_BY_TITLE

#### AIMP_MSG_CMD_PLS_SORT_BY_TITLE

Sort tracks in active playlist by title

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

## AIMP_MSG_CMD_PLS_SORT_INVERT

#### AIMP_MSG_CMD_PLS_SORT_INVERT

Invert tracks in active playlists

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

## AIMP_MSG_CMD_PLS_SORT_RANDOMIZE

#### AIMP_MSG_CMD_PLS_SORT_SHUFFLE

Shuffle tracks in active playlists

- `in` **Param1** — `Integer`
  0 - all
  1 - groups only
  2 - items inside groups
  3 - groups and it items
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

## AIMP_MSG_CMD_PLS_SWITCH_ON

#### AIMP_MSG_CMD_PLS_SWITCH_ON

Switch on auto playing marker for selected tracks in active playlist

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

## AIMP_MSG_CMD_PLS_SWITCH_OFF

#### AIMP_MSG_CMD_PLS_SWITCH_OFF

Switch off auto playing marker for selected tracks in active playlist

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

## AIMP_MSG_CMD_PLUGINS

#### AIMP_MSG_CMD_PLUGINS

Show options dialog and activate the "Plugins" sheet

- `in` **Param1** — `Integer`
  Page Index (starts from 1), 0 is for previous user choice (default)
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

## AIMP_MSG_CMD_PREV

#### AIMP_MSG_CMD_PREV

Previous track

Note 1: Note that function doesn't check if file playback really started. It just put the file into queue of loading thread (Refer to the AIMP_MSG_EVENT_STREAM_START).

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

## AIMP_MSG_CMD_QFI

#### AIMP_MSG_CMD_QFI

Show the "Quick File Information" card for specified file

- `in` **Param1** — `Integer`
  not used
- `in` **Param2** — `Pointer`
  Pointer to the TAIMPQuickFileInfoParams structure
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### TAIMPQuickFileInfoParams

- `in` **cbSize** — `Integer`
  size of the structure
- `in` **CmdShow** — `Integer`
  Command to show / hide the window.
  May be one of following values:
  `AIMP_QFI_SW_HIDE`
  `AIMP_QFI_SW_SHOW`
- `in` **AnimationType** — `Integer`
  May be one of following values:
  `AIMP_QFI_ANIMATION_NONE`
  `AIMP_QFI_ANIMATION_FADE`
- `in` **AnimationTime** — `Integer`
  animation time in milliseconds
- `in` **DisplayTime** — `Integer`
  display time in milliseconds.
  set to 0 to use default display time.
- `in` **Opacity** — `Byte`
  Opacity in percents: 0..100%
- `in` **FileInfo** — `IAIMPFileInfo`
  References to file information to display

### Summary

- **Definition:** apiMessages.pas / apiMessages.h
- **Multi-threading:** not supported
- **Applications:** Player
- **Minimal Version:** 4.70.2215

## AIMP_MSG_CMD_QFI_PLAYING_TRACK (AIMP_MSG_CMD_SHOW_CURRENT_QFI)

#### AIMP_MSG_CMD_QFI_PLAYING_TRACK

Show the "Quick File Information" card for playing file

- `in` **Param1** — `Integer`
  LoWord: display time in milliseconds (Set 0 to use default time).
  HiWord: card position (0 - near notification area, 1 - near mouse cursor).
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

## AIMP_MSG_CMD_QTE_PLAYING_TRACK (AIMP_MSG_CMD_QTE_NOWPLAYING_FILE)

#### AIMP_MSG_CMD_QTE_PLAYING_TRACK

Show the "File Information" dialog for playing track

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

## AIMP_MSG_CMD_QUIT

#### AIMP_MSG_CMD_QUIT

Close the application

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

## AIMP_MSG_CMD_SAVE_PLAYLISTS

#### AIMP_MSG_CMD_SAVE_PLAYLISTS

Show the "Save Playlist" dialog

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

## AIMP_MSG_CMD_SCHEDULER

#### AIMP_MSG_CMD_SCHEDULER

Show settings dialog of the "Simple Scheduler" plugin

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

## AIMP_MSG_CMD_SEARCH

#### AIMP_MSG_CMD_SEARCH

Show the "Advanced Search" dialog

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

## AIMP_MSG_CMD_SHOW_NOTIFICATION (AIMP_MSG_CMD_RUNSTR_SHOW_TEXT)

#### AIMP_MSG_CMD_SHOW_NOTIFICATION

Show custom text in the running line or text box

- `in` **Param1** — `Integer`
  0 - text will be automatically hidden (delay before hiding is 2 seconds)
  1 - text will be hidden manually (you must send message with Param2 set to nil / null).
- `in` **Param2** — `Pointer`
  Showing text: null-terminated PChar
  Hiding text: nil / null (for Param set to 1 only)
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

## AIMP_MSG_CMD_STOP

#### AIMP_MSG_CMD_STOP

Stop playback

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

## AIMP_MSG_CMD_TOGGLE_PARTREPEAT

#### AIMP_MSG_CMD_TOGGLE_PARTREPEAT

Toggles state of the "Repeat part A-B" function

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

## AIMP_MSG_CMD_VISUAL_NEXT

#### AIMP_MSG_CMD_VISUAL_NEXT

Next visualization

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

## AIMP_MSG_CMD_VISUAL_PREV

#### AIMP_MSG_CMD_VISUAL_PREV

Previous visualization

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

## AIMP_MSG_CMD_VISUAL_START

#### AIMP_MSG_CMD_VISUAL_START

Starts previous selected by user visualization. If visualization is not found - first will be started.

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

## AIMP_MSG_CMD_VISUAL_STOP

#### AIMP_MSG_CMD_VISUAL_STOP

Stop visualization

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
