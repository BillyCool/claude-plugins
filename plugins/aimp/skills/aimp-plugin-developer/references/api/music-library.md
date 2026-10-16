# Music Library

## LocalDataStorage (AIMPMLLocalDataStorage)

### Description

Using the `AIMPML_LOCALDATASTORAGE_ID` as ID argument of the IAIMPServiceMusicLibrary.GetStorageByID method, you will get an low level access to the "Local Files" data storage.

### Usage example

Excerpt from MusicLibraryBrowserDemo:

```
<IAIMPServiceMusicLibrary>.GetStorageByID(<AIMPML_LOCALDATASTORAGE_ID>, IID_IAIMPMLDataStorage2, DataStorage);

if Supports(DataStorage, IAIMPMLDataProvider, DataProvider) then
begin
CoreCreateObject(IID_IAIMPObjectList, FieldList);
FieldList.Add(<AIMPML_LOCALDATASTORAGE_FIELD_FILENAME>);

DataStorage.CreateObject(IID_IAIMPMLDataFilter, FieldFilter);
FieldFilter.Add(<AIMPML_LOCALDATASTORAGE_FIELD_ARTIST>, "ArtistName", Null, AIMPML_FIELDFILTER_OPERATION_EQUALS);
FieldFilter.SetValueAsInt32(AIMPML_FILTERGROUP_OPERATION, AIMPML_FILTERGROUP_OPERATION_AND);

if Succeeded(DataProvider.GetData(FieldList, Filter, Data)) then
begin
if Supports(Data, IAIMPMLDataProviderSelection, ASelection) then
repeat
SetString(FileName, ASelection.GetValueAsString(0, Length), Length);
//.. do something with FileName
until not ASelection.NextRow;
end;
end;
```

We recommends to execute all code that works with the DataProvider from non-main threads to prevent UI from freezing. Do not forget about the IAIMPTaskOwner when using threading.

### Available Fields

#### AIMPML_LOCALDATASTORAGE_FIELD_ID

ID of file in database

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_ADDDED

Date and time of adding file to database

- **Type:** Float

  Integer part is days, fractional part is milliseconds.
  Time format is fully compatible with TDateTime type from Delphi language

#### AIMPML_LOCALDATASTORAGE_FIELD_ALBUM

Album

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_ALBUMARTIST

Album Artist

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_ARTIST

Artist

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_BITDEPTH

Information about bit depth of audio stream.
= 0 - bit depth is unknown
< 0 - corresponds to floating point sample type.

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_BITRATE

Bitrate in kbps

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_BPM

Beats per minute

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_CHANNELS

Number of channels

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_CATALOG

Catalog Key

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_COMMENT

Comment

- **Type:** String
- **Value:** Multiline

#### AIMPML_LOCALDATASTORAGE_FIELD_COMPOSER

Composer

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_CONDUCTOR

Conductor

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_COPYRIGHTS

Copyrights

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_DISKNUMBER

Disk number

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_DURATION

Song duration in seconds

- **Type:** Float

#### AIMPML_LOCALDATASTORAGE_FIELD_FILEFORMAT

File format in style of file extension without dot

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_FILENAME

File name or URL

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_FILESIZE

File size in bytes

- **Type:** Int64

#### AIMPML_LOCALDATASTORAGE_FIELD_GENRE

Genre

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_LABELS

Custom labels

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_LASTMODIFICATION

Date and time of last file modification

- **Type:** Float

  Integer part is days, fractional part is milliseconds.
  Time format is fully compatible with TDateTime type from Delphi language

#### AIMPML_LOCALDATASTORAGE_FIELD_LASTPLAYBACK

Date and time of last file playback

- **Type:** Float

  Integer part is days, fractional part is milliseconds.
  Time format is fully compatible with TDateTime type from Delphi language

#### AIMPML_LOCALDATASTORAGE_FIELD_LYRICIST

Lyricist

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_MOOD

Mood

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_PLAYBACKCOUNT

Number of file playback

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_PUBLISHER

Publisher

- **Type:** String
- **Value:** Multiple values split by ";" character

#### AIMPML_LOCALDATASTORAGE_FIELD_RATING

Rating of track that calculates automatically based on playback statistic. Value range: 0 - 100.

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_SAMPLERATE

Sampling rate in HZ.

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_TITLE

Track title

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_TRACKNUMBER

Track number in album or disk

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_URL

- **Type:** String
- **Value:** Single

#### AIMPML_LOCALDATASTORAGE_FIELD_USERMARK

User rating. Value range: 0 - 5.

- **Type:** Int32

#### AIMPML_LOCALDATASTORAGE_FIELD_YEAR

Year

- **Type:** String
- **Value:** Single

### Summary

- **Definition:** apiMusicLibrary.pas / apiMusicLibrary.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 4.60.2160

## More in this chapter

- **Services and Extensions** — `api/music-library-services-and-extensions.md`
- **Primitives** — `api/music-library-primitives.md`
