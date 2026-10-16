AIMP4 Playlist File Format Specification

General
AIMPPL4 file is simple text file that devided to few data sections via special macro words. Macro format is
#----- SectionName -----#
Nota that playlist can contains user-provided sections with custom formatting.

The "SUMMARY" section
The summary section must be placed as first section of the file. The section provides summary information about the playlist file and its content.
Content of section provided as key-value pairs, where each key placed on new line.

Key = Value

Note that summary section can contains user-provided keys.
Built-in key values are:
ID  - (TEXT) unuquie ID of playlist
Name  - (TEXT) display name of the playlist
NameIsAutoSet  - (0/1) displays if the playlist name was automatically generated based on playlist content.
ContentDuration  - (msec)
ContentFiles
ContentSize  - (bytes)
PlaybackCursor  - (integer) - position of playback cursor in playback queue for the playlist. Note that playback index may be differs from track index in playlist.

The "CONTENT" section
The section provides information about groups and tracks that playlist file contains. Line per element.
Line that started from "+" or "-" character is line of playlist group. "+" - group is collapsed, "-" - group is expanded. Format line for group is:

State GroupName

In other case, line is track. Format is:
FileName | Title | Artist | Album | AlbumArtist | Genre | Date | TrackNumber | DiskNumber | Composer | Publisher |Bitrate|Channels|SampleRate|Duration|FileSize|BPM|PlaybackSwitch|PlaybackQueueIndex| Custom|Lyricist|Mood| BitDepth| URL|FileFormat|Comment
Where the  value  is text value, and the  value  is int64 value.
Note that each value MUST NOT contain the "|", "\n" or "\r" characters. If value contains it - characters must be replaced by any other symbol before saving the track information.
Note:  PlaybackSwitch  - (0/1) state of the automatic playback switch. If it set to 0 - track will be skiped during automatic switching between tracks.
Note:  PlaybackQueueIndex  - position of track in playback queue for the playlist. Playback index may be differs from track index in playlist.

## The "SETTINGS" section
** Player specific. The section contains grouping / displaying settings that has been  customized by user** .

The "PREIMAGE" section
Player specific. This section contains preimage settings that used for smart-playlist. Content is HexCode encoded and depended from the type of specified preimage.
