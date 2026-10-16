AIMP Extensions for XSPF
## Introduction
XSPF is the XML format for sharing playlists. Its portable, its free and its extendable. Refer to the https://www.xspf.org/  for more information.
XSPF supports extensions to allow applications to add special data. These extensions can appear in the playlist and track entries. Here you will find description of AIMP extensions for the XSPF file format.

Extensions
All AIMP extensions are defined in the  xmlns:aimp="http://www.aimp.ru/playlist/ns/0/ "  namespace. Each extension marked by different  application  attribute value.
Now, AIMP supports for following extension entries:
Inside playlist entry:
⦁     Summary ( application ="http://www.aimp.ru/playlist/summary/0 ")
⦁     Settings ( application ="http://www.aimp.ru/playlist/settings/0 ")
⦁     Preimage ( application ="http://www.aimp.ru/playlist/preimage/0 ")
Inside track entry:
⦁     Track ( application ="http://www.aimp.ru/playlist/track/0 ")
1    Group ( application ="http://www.aimp.ru/playlist/group/0 ")

Summary Entry
The entry provides summary information about the playlist file and its content. Content provided as key-value pairs using following schema:

<aimp:prop name=" Key "> Value </aimp:prop>

Built-in keys are:
ID  - (TEXT) unuquie ID of playlist
Name  - (TEXT) display name of the playlist
NameIsAutoSet  - (0/1) displays if the playlist name was automatically generated based on playlist content.
ContentDuration  - (Int64) playlist duration, in miliseconds.
ContentFiles  - (Int32) number of files in playlist
ContentSize  - (Int64) total size of all files in playlist
PlaybackCursor  - (Int32) - position of playback cursor in playback queue for the playlist. Note that playback index may differs from track index in playlist.
PlaybackCursorAutoBookmark  - (Int32) - position the playing track
SortingTemplate  - template string that used to sort the track list (list of supported macros depended from AIMP version)
Shuffled  - (0/1) displays if playback queue is shuffled
UserReordered  - (0/1) displays if the track list was reordered by user

The summary entry can contains user-provided keys.
The summary entry  MUST BE  defined before the track list entry.

Settings Entry
** The entry contains grouping / displaying settings that has been  customized by user** .**  Content provided as key-value pairs using follwing schema:**

<aimp:prop name=" Key "> Value </aimp:prop>

Built-in keys are:

⦁     FormatMainLine  is  template for 1st track information line in playlist
1     FormatSecondLine  is   template for 2nd track information line in playlist
2     GroupFormatLine  is template for group names
3     Flags  - determines individual view and behavior settings of the playlist. Value is combination of following flags:
⦁     0x0001 - ContinuousTrackNumeration
1    0x0002 - AllowGroups
2    0x0004 - ShowDurationColumn
3    0x0008 - ShowNumbersColumn
4    0x0010 - ShowSwitchesColumn
5    0x0020 - ShowSecondaryLine
6    0x0040 - UseGlobalFormattingSettings
7    0x0080 - UseGlobalGrouppingSettings
8    0x0100 - UseGlobalLayoutSettings
9    0x0200 - ShowExpandButtons
10    0x0400 - ShowRating
11    0x0800 - MergeGroups
12    0x1000 - CollapseUnusedGroups
13     0x2000 - ShowThumbnails (requires the ShowSecondaryLine flag too)

The summary entry can contains user-provided keys.
The summary entry  MUST BE  defined before the track list entry.

Track Entry
The track entry extension contains additional meta-information for the song. Each sub-entry is defined in  aimp  namespace using following schema:

<aimp: key > value </aimp: key >

Following keys are supported now:
bits  - (Int32) bits per sample (8, 16, 24, 32 and etc)
chans  - (Int32) number of channels (1, 2, 4, 6 and etc)
clipStart / clipFinish  - (Float) clipping bounds in seconds. Always defined in pairs. Defined for tracks splitted by time (track can be splitted using CUE, chapters, etc). In this case, result of " clipFinish-clipStart " expression should be equal to value of  Duration  key.
format  - (Text) user friendly file format desciption (MP3, MP4/AAC and etc).
fileURI  - (Text) native file uri in AIMP terms.  Omit it  if you not sure about valid uri generation. Used by the player for performance purposes only.
samplerate  - (Int32) sampling rate of audio stream in Hz. (44100, 48000 and etc).
size  - (Int64) file size in bytes.
state  - (Int32) if it  set to  10 , track will be skiped during automatic switching between tracks.
queueIndex  - (Int32) position of track in playback queue for the playlist. Playback index may differs from track index in playlist.

Group Entry
The entry is defined for the track that starts new group.  . Each sub-entry is defined in  aimp  namespace using following schema:

<aimp: key > value </aimp: key >

Following keys are supported now:

title  - (Text) group's title, string.
state  - (Int32) group's state, integer.
0 or empty - state is undefined,
1 - group is expanded,
2 - group is collapsed

Preimage Entry
The section contains preimage settings, its used for smart-playlist. Content depended from the type of specified preimage.
