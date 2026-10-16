# Remote API

## Remote API

- Overview
- Information about the playable file
- Properties
- Events
- Commands

## Overview (RA_CommonTerms)

### Limitations

Remote API is available for Windows OS only!

### Interaction Scheme

Interaction between the player and external application is based on exchanging by messages via native mechanism of Windows OS.

The player creates invisible window with `AIMPRemoteAccessClass` class on startup. It provide an ability to exchange by messages with external applications.

### Definitions

All definitions are located in the apiRemote.pas / apiRemote.h

## Information about the playable file (RAFileInfo)

### Description

AIMP provides an access to information about the playing file for external application via File Mapping.

Mapped file name is `AIMPRemoteAccessClass` and it has a fixed size that is equal to `AIMPRemoteAccessMapFileSize` constant.

File contains `TAIMPRemoteFileInfo` structure, after it few arrays of unicode (UTF16) characters are placed, which contained information about the track: Album, Artist, Year, File Name, Genre and Title.

Length of each array is defined in the `TAIMPRemoteFileInfo` structure, for example: `<TAIMPRemoteFileInfo>.AlbumLength`, `<TAIMPRemoteFileInfo>.GenreLength` and etc.

### Example

Refer to the `Demos \ RemoteAccessDemo` folder

### See also

- AIMP_RA_CMD_GET_ALBUMART
- AIMP_RA_NOTIFY_TRACK_INFO

## Properties

### Properties

- AIMP_RA_PROPERTY_MUTE
- AIMP_RA_PROPERTY_PLAYER_DURATION
- AIMP_RA_PROPERTY_PLAYER_POSITION
- AIMP_RA_PROPERTY_PLAYER_STATE
- AIMP_RA_PROPERTY_RADIOCAP
- AIMP_RA_PROPERTY_TRACK_REPEAT
- AIMP_RA_PROPERTY_TRACK_SHUFFLE
- AIMP_RA_PROPERTY_VERSION
- AIMP_RA_PROPERTY_VISUAL_FULLSCREEN
- AIMP_RA_PROPERTY_VOLUME

### AIMP_RA_PROPERTY_MUTE

##### AIMP_RA_PROPERTY_MUTE

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  Mute switch state (0 - False, otherwise - True)
- `SET` **Param** — `LPARAM`
  New mute switch state (0 - False, otherwise - True)
- `SET` **Result** — `LRESULT`
  Not used

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

**To write property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_SET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

### AIMP_RA_PROPERTY_PLAYER_DURATION

##### AIMP_RA_PROPERTY_PLAYER_DURATION

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  Duration of playing file (in milliseconds)

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

### AIMP_RA_PROPERTY_PLAYER_POSITION

##### AIMP_RA_PROPERTY_PLAYER_POSITION

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  Current playback position (in milliseconds)
- `SET` **Param** — `LPARAM`
  New playback position (in milliseconds)
- `SET` **Result** — `LRESULT`
  Not used

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

**To write property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_SET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

### AIMP_RA_PROPERTY_PLAYER_STATE

##### AIMP_RA_PROPERTY_PLAYER_STATE

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  Player state:

  - 0 - Stopped
  - 1 - Paused
  - 2 - Playing

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

### AIMP_RA_PROPERTY_RADIOCAP

##### AIMP_RA_PROPERTY_RADIOCAP

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  State of radio capture (0 - False, otherwise - True)
- `SET` **Param** — `LPARAM`
  New state of radio capture (0 - False, otherwise - True)
- `SET` **Result** — `LRESULT`
  Not used

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

**To write property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_SET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

### AIMP_RA_PROPERTY_TRACK_REPEAT

##### AIMP_RA_PROPERTY_TRACK_REPEAT

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  Value of track repeat option (0 - False, otherwise - True)
- `SET` **Param** — `LPARAM`
  New value of track repeat option (0 - False, otherwise - True)
- `SET` **Result** — `LRESULT`
  Not used

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

**To write property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_SET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

### AIMP_RA_PROPERTY_TRACK_SHUFFLE

##### AIMP_RA_PROPERTY_TRACK_SHUFFLE

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  Value of the "shuffle playback" option (0 - False, otherwise - True)
- `SET` **Param** — `LPARAM`
  New value of the "shuffle playback" option (0 - False, otherwise - True)
- `SET` **Result** — `LRESULT`
  Not used

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

**To write property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_SET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

### AIMP_RA_PROPERTY_VERSION

##### AIMP_RA_PROPERTY_VERSION

Player version. Read only

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  HiWord(Result) - Version ID
  LoWord(Result) - Build Number

  ID of version in the XYY format.
  X - Major version number, does not limited
  YY - Minor version number, from 0 to 99

  Examples:
  355 — 3.55
  1005 — 10.05
  001 — 0.01

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

### AIMP_RA_PROPERTY_VISUAL_FULLSCREEN

##### AIMP_RA_PROPERTY_VISUAL_FULLSCREEN

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  Value of the "Full screen mode" option (0 - False, otherwise - True)
- `SET` **Param** — `LPARAM`
  New value of the "Full screen mode" option (0 - False, otherwise - True)
- `SET` **Result** — `LRESULT`
  Not used

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

**To write property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_SET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

### AIMP_RA_PROPERTY_VOLUME

##### AIMP_RA_PROPERTY_VOLUME

- `GET` **Param** — `LPARAM`
  Not used
- `GET` **Result** — `LRESULT`
  Volume, in percents (from 0 to 100)
- `SET` **Param** — `LPARAM`
  New volume, in percents (from 0 to 100)
- `SET` **Result** — `LRESULT`
  Not used

**To get property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_GET, Param);
```

**To write property value:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_PROPERTY, ID or AIMP_RA_PROPVALUE_SET, Param);
```

#### See also

- The AIMP_RA_NOTIFY_PROPERTY event

## Events

### Events

- Subscribe to events
- AIMP_RA_NOTIFY_TRACK_INFO
- AIMP_RA_NOTIFY_TRACK_START
- AIMP_RA_NOTIFY_PROPERTY

### Subscribe to events (RA_Events)

#### Warning

Subscribing mechanism is working for 32-bit applications only

#### Subscribing to events

Subscribing / unsubscribing from events implemented via special commands: AIMP_RA_CMD_REGISTER_NOTIFY and AIMP_RA_CMD_UNREGISTER_NOTIFY.

External program should put own window handle as LParam, player will sent WM_AIMP_NOTIFY message to it. WParam of this message will contains Event ID (see "Events" section).

Example:

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
// Subscribing
SendMessage(Window, WM_AIMP_COMMAND, AIMP_RA_CMD_REGISTER_NOTIFY, Form1.Handle);

// Unsubscribing
SendMessage(Window, WM_AIMP_COMMAND, AIMP_RA_CMD_UNREGISTER_NOTIFY, Form1.Handle);

// Handling events:
TForm1 = class(TForm)
protected
procedure WMAIMPNotify(var Message: TMessage); message WM_AIMP_NOTIFY;
end;

procedure TForm1.WMAIMPNotify(var Message: TMessage);
begin
case Message.WParam of
AIMP_RA_NOTIFY_TRACK_START:
// do something
AIMP_RA_NOTIFY_TRACK_INFO:
// do something
AIMP_RA_NOTIFY_PROPERTY:
case Message.LParam of
AIMP_RA_PROPERTY_PLAYER_POSITION:
// do something
end;
end;
end;
```

### AIMP_RA_NOTIFY_TRACK_INFO

##### AIMP_RA_NOTIFY_TRACK_INFO

Event occurs when information about the playing file has been changed

- `in` **Param2** — `LPARAM`
  0 - information about the playing file has been changed
  1 - album art of playing file has been changed
- `out` **Result** — `LRESULT`
  not used

#### See also

- How to subscribe to event?
- How to access to information about the playing file?

### AIMP_RA_NOTIFY_TRACK_START

##### AIMP_RA_NOTIFY_TRACK_START

Event occurs when new track was started

- `in` **Param2** — `LPARAM`
  0 - when file is started, 1 - when new track is started while playing the internet radio
- `out` **Result** — `LRESULT`
  not used

#### See also

- How to subscribe to event?

### AIMP_RA_NOTIFY_PROPERTY

##### AIMP_RA_NOTIFY_PROPERTY

Event occurs when property value has been changed

- `in` **Param2** — `LPARAM`
  Property ID (see the "Properties" section)
- `out` **Result** — `LRESULT`
  not used

#### See also

- How to subscribe to event?

## Commands

### Commands

- AIMP_RA_CMD_ADD_FILES
- AIMP_RA_CMD_ADD_FOLDERS
- AIMP_RA_CMD_ADD_PLAYLISTS
- AIMP_RA_CMD_ADD_URL
- AIMP_RA_CMD_GET_ALBUMART
- AIMP_RA_CMD_NEXT
- AIMP_RA_CMD_OPEN_FILES
- AIMP_RA_CMD_OPEN_FOLDERS
- AIMP_RA_CMD_OPEN_PLAYLISTS
- AIMP_RA_CMD_PAUSE
- AIMP_RA_CMD_PLAY
- AIMP_RA_CMD_PLAYPAUSE
- AIMP_RA_CMD_PREV
- AIMP_RA_CMD_QUIT
- AIMP_RA_CMD_STOP
- AIMP_RA_CMD_VISUAL_NEXT
- AIMP_RA_CMD_VISUAL_PREV
- AIMP_RA_CMD_VISUAL_START
- AIMP_RA_CMD_VISUAL_STOP

### AIMP_RA_CMD_ADD_FILES

##### AIMP_RA_CMD_ADD_FILES

Execute the "Files Adding" dialog

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_ADD_FOLDERS

##### AIMP_RA_CMD_ADD_FOLDERS

Execute the "Folders Adding" dialog

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_ADD_PLAYLISTS

##### AIMP_RA_CMD_ADD_PLAYLISTS

Execute the "Playlists Adding" dialog

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_ADD_URL

##### AIMP_RA_CMD_ADD_URL

Execute "URL Adding" dialog

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_GET_ALBUMART

##### AIMP_RA_CMD_GET_ALBUMART

This command is provided for an ability to get album art for playing file.

There are two stages:
1st - external application sends request to the player
2nd - player receive it and sends the answer back as WM_COPYDATA message

LParam of the WM_COPYDATA message contained pointer to the CopyDataStruct structure which will contains followed data:
- dwData - Signature, must be = WM_AIMP_COPYDATA_ALBUMART_ID
- lpData - Pointer to first element of byte array that contained data of Album Art image in PNG format
- cbData - Length of data array

- `in` **Param** — `LPARAM`
  Handle of window that will receive the answer.
- `out` **Result** — `LRESULT`
  Return 0 if player is stopped or album art is not presented for playing file

#### Example

Refer to the `Demos\RemoteAccessDemo` folder

#### Warning

This command is working only for 32-bit applications

### AIMP_RA_CMD_NEXT

##### AIMP_RA_CMD_NEXT

Next track

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_OPEN_FILES

##### AIMP_RA_CMD_OPEN_FILES

Execute "Files Opening" dialog

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_OPEN_FOLDERS

##### AIMP_RA_CMD_OPEN_FOLDERS

Execute "Folders Opening" dialog

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_OPEN_PLAYLISTS

##### AIMP_RA_CMD_OPEN_PLAYLISTS

Execute "Playlists Opening" dialog

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_PAUSE

##### AIMP_RA_CMD_PAUSE

If player is playing this command pauses playback.
If player is paused this command resumes playback.

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_PLAY

##### AIMP_RA_CMD_PLAY

If player is stopped this command starts playback
If player is paused this command resumes playback
If player is playing this command starts playback from beginning

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_PLAYPAUSE

##### AIMP_RA_CMD_PLAYPAUSE

If player is stopped this command starts playback
If player is paused this command resumes playback
If player is playing this command pauses playback

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_PREV

##### AIMP_RA_CMD_PREV

Previous track

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_QUIT

##### AIMP_RA_CMD_QUIT

Exit from the application

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_STOP

##### AIMP_RA_CMD_STOP

Stop playback

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_VISUAL_NEXT

##### AIMP_RA_CMD_VISUAL_NEXT

Next visualization

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_VISUAL_PREV

##### AIMP_RA_CMD_VISUAL_PREV

Previous visualization

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_VISUAL_START

##### AIMP_RA_CMD_VISUAL_START

Starts previous selected by user visualization. If visualization is not found - first will be started.

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```

### AIMP_RA_CMD_VISUAL_STOP

##### AIMP_RA_CMD_VISUAL_STOP

Stop visualization

- `in` **Param** — `LPARAM`
  not used
- `out` **Result** — `LRESULT`
  not used

**Usage principle:**

```
Window = FindWindow(AIMPRemoteAccessClass, null);
...
Result = SendMessage(Window, WM_AIMP_COMMAND, CommandID, Param);
```
