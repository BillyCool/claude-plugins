# Whats new?

## Whats new?

- v6.00.3000
- v5.40.2660
- v5.30.2533
- v5.10.2400
- v5.02.2365
- v5.00.2337
- v4.70.2215
- v4.60.2160
- v4.50.2000
- v4.10.1815
- v4.00.1691
- v4.00.1660

## v6.00.3000 (whats_new_2800)

### Local API

- Linux support
- IAIMPConfigFile
- IAIMPServiceLog
- Improved: automatic localizations

### Local API \ Album Arts

- Deprecated: IAIMPExtensionAlbumArtCatalog.GetIcon

### Local API \ Message Dispatcher

- AIMP_MSG_CMD_BRING_TO_TOP
- AIMP_MSG_PROPERTY_JUMP_TO_BEGINNING_ON_PREV_TRACK

### Local API \ File Manager

- IAIMPServiceFileURI3

### Local API \ Playlists

- IAIMPExtensionPlaylistShuffler

### Local API \ Music Library

- IAIMPMLDataFieldFilter
- new `AIMPML_FIELDFILTER_OPERATION_DOESNOTCONTAIN` flag

### Local API \ Primitives

- IAIMPImage3
- IAIMPNamedContainer
- IAIMPObjectList2

### Local API \ Internet

- IAIMPServiceHTTPClient
- New flag: `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_ACCEPT`
- New flag: `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_PROGRESS`
- New flag: `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_COMPLETE`

### Local API \ Skins

- IAIMPServiceSkinsManager
- new `AIMP_SERVICE_SKINSMAN_PROPID_HUE_BRIGHTNESS` property

### Local API \ GUI

- IAIMPUICardView
- IAIMPUIColorPickerDialog
- IAIMPUIColorButton
- IAIMPUIDateEdit
- IAIMPUIDateTimeEdit
- IAIMPUIFontPickerDialog
- IAIMPUIForm2
- IAIMPUIImageList3
- IAIMPUIPopupMenu2
- IAIMPUIButton
- new `AIMPUI_BUTTON_PROPID_DOWN` property
- IAIMPUIForm
- new `AIMPUI_FORM_PROPID_CLIENTHEIGHT` property
- new `AIMPUI_FORM_PROPID_CLIENTWIDTH` property
- new `AIMPUI_FORM_PROPID_MODALRESULT` property
- new `AIMPUI_FORM_PROPID_STAYONTOP` property
- the Release method has been renamed to Destroy
- IAIMPUILabel
- new `AIMPUI_LABEL_PROPID_TEXTSIZE` property
- IAIMPUIGroupBox
- new `AIMPUI_GROUPBOX_PROPID_PADDING` property
- extended `AIMPUI_GROUPBOX_PROPID_CHECKMODE` property
- IAIMPUITabControl
- new `AIMPUI_TABCONTROL_PROPID_PADDING` property
- new `AIMPUI_TABCONTROL_PROPID_STYLE` property
- new `AIMPUI_TABCONTROL_PROPID_TABPOSITION` property
- IAIMPUIPageControl
- new `AIMPUI_PAGECONTROL_PROPID_TABPOSITION` property
- new `AIMPUI_PAGECONTROL_PROPID_STYLE` property
- IAIMPUIProgressBar
- new `AIMPUI_PROGRESSBAR_PROPID_AUTOSIZE` property
- IAIMPUITreeListDeleteEvents
- IAIMPUISlider
- new `AIMPUI_SLIDER_PROPID_AUTOSIZE` property
- new `AIMPUI_SLIDER_PROPID_LABELPOSITION` property
- new `AIMPUI_SLIDER_PROPID_LABELVALUE` property
- new `AIMPUI_SLIDER_PROPID_LABELVALUE_WIDTH` property
- new `AIMPUI_SLIDER_PROPID_LABELVALUEMIN` property
- new `AIMPUI_SLIDER_PROPID_LABELVALUEMIN_WIDTH` property
- new `AIMPUI_SLIDER_PROPID_LABELVALUEMAX` property
- new `AIMPUI_SLIDER_PROPID_LABELVALUEMAX_WIDTH` property
- IAIMPMenuItem
- new `AIMP_MENUITEM_PROPID_HINT` property
- new `AIMP_MENUITEM_PROPID_TAG` property
- IAIMPUINumericEdit
- IAIMPUIToolButton
- IAIMPUIPathChooser

### Local API \ Visualizations

- IAIMPVisualizationDirectOutput

## v5.40.2660 (whats_new_2600)

### Local API

- General: some types definitions has been moved to the apiTypes unit
- AIMP_CORE_PATH_ENCODERS has been removed
- TaskID of IAIMPServiceAlbumArt, IAIMPServiceHTTPClient and IAIMPServiceLyrics services now defined as TTaskHandle (type compatible with old definition)

### Local API \ Album Arts

- IAIMPAlbumArtRequest
- new `AIMP_ALBUMART_REQUEST_PROPID_RESULTS` property
- IAIMPExtensionAlbumArtProvider3
- new `AIMP_ALBUMART_PROVIDER_CATEGORY_INTERNET_SEARCH` property

### Local API \ Decoders

- IAIMPAudioDecoder - `AIMP_DECODER_SAMPLEFORMAT_64BITFLOAT`

### Local API \ Internet

- IAIMPServiceHTTPClient3

### Local API \ GUI

- IAIMPUIAuthDialog
- IAIMPUIBBCBox
- new `AIMPUI_BBCBOX_PROPID_AUTOSCROLL` property
- new `AIMPUI_BBCBOX_PROPID_TEXTALIGN` property
- new `AIMPUI_BBCBOX_PROPID_TEXTCOLOR` property
- new `AIMPUI_BBCBOX_PROPID_PADDING` property
- IAIMPUIButton
- new `AIMPUI_BUTTON_PROPID_TEXTSTYLE` property
- IAIMPUITrayIcon

### Local API \ Playlists

- IAIMPPlaylist
- new `AIMP_PLAYLIST_PROPID_GROUPNAME` property
- new `AIMP_PLAYLIST_PROPID_DURATION_REMAINING` property
- IAIMPPlaylistListener
- new `AIMP_PLAYLIST_NOTIFY_PLAYBACKBOOKMARK` notify
- new `AIMP_PLAYLIST_NOTIFY_GROUP` notify
- IAIMPPlaylistProperties

## v5.30.2533 (whats_new_2500)

### Local API \ File Manager

- IAIMPServiceFileInfoFormatter
- IAIMPFileInfo - new AIMP_FILEINFO_PROPID_KEY property

### Local API \ Message Dispatcher

- AIMP_MSG_CMD_PLS_DELETE_SELECTED_FROM_HDD_W_FOLDERS
- AIMP_MSG_EVENT_DSP
- AIMP_MSG_EVENT_UI_MODE

### Local API \ Player

- IAIMPServicePlayer - new AIMP_PLAYER_PROPID_OUTPUT property

### Local API \ GUI

- IAIMPUIMode

## v5.10.2400 (whats_new_2400)

### Local API \ Message Dispatcher

- AIMP_MSG_EVENT_PLAYBACK_QUEUE
- AIMP_MSG_CMD_PLS_SORT_RANDOMIZE

### Local API \ Options Dialog

- New `AIMP_SERVICE_OPTIONSDIALOG_NOTIFICATION_RESET` event for IAIMPOptionsDialogFrame.Notification

### Local API \ Playlists

- New sort modes for IAIMPPlaylist.Sort

## v5.02.2365 (whats_new_2360)

### Local API \ Album Arts

- IAIMPAlbumArtRequest
- IAIMPExtensionAlbumArtProvider deprecated
- IAIMPExtensionAlbumArtProvider2 deprecated
- IAIMPExtensionAlbumArtProvider3
- IAIMPServiceAlbumArtCache has been completely redesigned
- The AIMP_SERVICE_ALBUMART_PROPID_* constants has been renamed to AIMP_ALBUMART_REQUEST_PROPID_*

### Local API \ Music Library

- IAIMPMLAlbumArtProvider deprecated
- IAIMPMLAlbumArtProvider2

### Local API \ File Manager

- AIMP_FILEINFO_PROPID_ML_LABELS
- AIMP_SERVICE_FILESTREAMING_FLAG_MAPTOMEMORY replaced by AIMP_SERVICE_FILESTREAMING_FLAG_BUFFERED

## v5.00.2337 (whats_new_2300)

### Local API \ GUI

- IAIMPUIColorSchema

### Local API \ Message Dispatcher

- AIMP_MSG_PROPERTY_EQUALIZER_AUTO
- AIMP_MSG_PROPERTY_PARTREPEAT_RANGE
- AIMP_MSG_PROPERTY_JUMP_TO_NEXT_TRACK

### Local API \ MusicLibrary

- AIMPML_FIELDFILTER_OPERATION_ISLASTXDAYS
- IAIMPMLDataFilter - AIMPML_FILTER_SORTBY and AIMPML_FILTER_SORTDIRECTION has been replaced by AIMPML_FILTER_SORTBYLIST
- IAIMPMLDataStorageCommandFindInLibrary

### Local API \ Player

- IAIMPEqualizerBands
- IAIMPEqualizerPreset
- IAIMPServicePlayerEqualizer
- IAIMPServicePlayerEqualizerPresets
- IAIMPServicePlayer2

### Local API \ Playlists

- IAIMPExtensionPlaybackQueue2
- IAIMPServicePlaybackQueue2
- AIMP_PLAYLIST_NOTIFY_PLAYBACKQUEUE

### Local API \ Scheduler

Scheduler API no longer supported

## v4.70.2215 (whats_new_2215)

### Local API \ Music Library

- New columns in the LocalDataStorage provider
- IAIMPMLGroupingTreeDataProvider2

### Local API \ Message Dispatcher

- AIMP_MSG_CMD_QFI

## v4.60.2160 (whats_new_2100)

### Local API \ Album Arts

- AIMP_SERVICE_ALBUMART_FLAGS_OFFLINE

### Local API \ Decoders

- IAIMPAudioDecoderListener
- IAIMPAudioDecoderNotifications
- IAIMPExtensionAudioDecoderPriority

### Local API \ GUI

- IAIMPUIForm.AIMPUI_FORM_PROPID_STYLE
- IAIMPUIFormEvents3

### Local API \ Message Dispatcher

- AIMP_MSG_PROPERTY_CROSSMIXING
- AIMP_MSG_PROPERTY_RADIOCAP_SINGLE_TRACK
- AIMP_MSG_PROPERTY_ACTION_ON_END_OF_TRACK

### Local API \ Music Library

- IAIMPMLAlbumArtProvider
- IAIMPMLDataProvider2
- IAIMPMLDataProviderSelection's HasNextPage method replaced with IAIMPMLDataProvider2
- IAIMPMLDataStorage2
- LocalDataStorage Provider

### Local API \ Tag Editor

- IAIMPExtensionTagsProvider
- IAIMPServiceFindTagsOnline

### Local API \ Threading

- IAIMPServiceSynchronizer and IAIMPServiceThreadPool replaced by IAIMPServiceThreads

## v4.50.2000 (whats_new_2000)

### Local API \ DPI Aware

- IAIMPDPIAware
- IAIMPOptionsDialogFrame
- IAIMPUIFormEvents2

### Local API \ File Manager

IAIMPFileInfo:New properties:
- AIMP_FILEINFO_PROPID_CONDUCTOR
- AIMP_FILEINFO_PROPID_MOOD
- AIMP_FILEINFO_PROPID_CATALOG
- AIMP_FILEINFO_PROPID_ISRC
- AIMP_FILEINFO_PROPID_LYRICIST
- AIMP_FILEINFO_PROPID_ENCODEDBY
- AIMP_FILEINFO_PROPID_RATING
Renamed:
- AIMP_FILEINFO_PROPID_MARK — AIMP_FILEINFO_PROPID_ML_DISPLAYING_MARK

## v4.10.1815 (whats_new_1800)

### Local API \ File Manager

- IAIMPServiceFileSystems
- IAIMPFileSystemCommandCopyToClipboard
- IAIMPFileSystemCommandDelete
- IAIMPFileSystemCommandDropSource
- IAIMPFileSystemCommandFileInfo
- IAIMPFileSystemCommandOpenFileFolder
- IAIMPFileSystemCommandStreaming
- IAIMPServiceFileURI2

### Local API \ Options Dialog

- IAIMPOptionsDialogFrameKeyboardHelper2

### Local API \ Music Library

- IAIMPServiceMusicLibrary

### Local API \ Player

- IAIMPExtensionWaveformProvider
- IAIMPServiceWaveform

### Local API \ Playlists

- IAIMPServicePlaylistManager2
- IAIMPExtensionPlaylistPreimageFactory
- IAIMPPlaylistPreimage
- IAIMPPlaylistPreimageDataProvider
- IAIMPPlaylistPreimageListener

## v4.00.1691 (whats_new_1691)

### Local API \ Menu

- AIMP_MENUID_PLAYER_STOP_OPTIONS

### Local API \ Player

- An access to playback settings

## v4.00.1660 (whats_new_1660)

### Local API \ Primitives

- IAIMPImage2

### Local API \ Internet

- IAIMPServiceHTTPClient2
- IAIMPHTTPClientEvents2

### Local API \ File Manager

- IAIMPServiceFileURI

### Local API \ Menu

- AIMP_MENUITEM_PROPID_DEFAULT
- AIMP_MENUITEM_PROPID_SHORTCUT

### Local API \ GUI

- IAIMPServiceUI

### Local API \ Options Dialog

- AIMP_SERVICE_OPTIONSDIALOG_NOTIFICATION_CAN_SAVE

### Local API \ Player

- IAIMPEqualizerPreset
- IAIMPServicePlayerEqualizer
- IAIMPServicePlayerEqualizerPresets

### Local API \ Playlist

- IAIMPPlaylistItem - AIMP_PLAYLISTITEM_PROPID_CUSTOM
- IAIMPPlaylistListener2
- IAIMPPlaylistQueue2
- IAIMPPlaylistQueueListener
