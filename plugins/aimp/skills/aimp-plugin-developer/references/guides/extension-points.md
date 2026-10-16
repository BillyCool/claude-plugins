# Extension points: what to implement for what you want to build

Start here when the task is "make AIMP do X". Find the row, then read the
reference file named in the last column before writing anything.

Registration is `IAIMPCore.RegisterExtension(<Target service IID>, <your object>)`
during `IAIMPPlugin.Initialize`, unless the row says otherwise.

## Add to the UI

| Goal | Implement / create | Target service | Reference |
|---|---|---|---|
| Menu item anywhere in the player | `IAIMPMenuItem` (via `CreateObject`) | `IID_IAIMPServiceMenuManager` | `api/menu.md` |
| Bindable, hotkey-able command | `IAIMPAction` (via `CreateObject`) + `IAIMPActionEvent` | `IID_IAIMPServiceActionManager` | `api/actions.md` |
| Page in Preferences | `IAIMPOptionsDialogFrame` | `IID_IAIMPServiceOptionsDialog` | `api/options-dialog.md` |
| Your own window / dialog / controls | `IAIMPServiceUI.CreateForm` / `CreateControl` | — (service, not extension) | `api/gui.md`, `api/gui-controls/` |
| Settings button in the plugin list | `IAIMPExternalSettingsDialog` on your plugin object | — | `basic-interfaces.md` |
| Tray icon, popup menu, image list, font | `IAIMPServiceUI` non-visual objects | — | `api/gui-non-visual-objects.md` |
| Standard dialogs (file, folder, colour, auth, progress…) | `IAIMPServiceUI` dialogs | — | `api/gui-dialogs.md` |

## Handle audio

| Goal | Implement | Target service | Reference |
|---|---|---|---|
| Decode a new audio format | `IAIMPExtensionAudioDecoder` (+ `IAIMPAudioDecoder`) | `IID_IAIMPServiceAudioDecoders` | `api/decoders.md` |
| Declare a file format / extension list | `IAIMPExtensionFileFormat` | `IID_IAIMPServiceFileFormats` | `api/file-manager.md` |
| Read tags / duration for a file | `IAIMPExtensionFileInfoProvider(Ex)` | `IID_IAIMPServiceFileInfo` | `api/file-manager.md` |
| Expand a container into tracks (cue, archive) | `IAIMPExtensionFileExpander` | `IID_IAIMPServiceFileManager` | `api/file-manager.md` |
| Virtual file system / custom URI scheme | `IAIMPExtensionFileSystem` | `IID_IAIMPServiceFileSystems` | `api/file-manager.md` |
| Observe or veto playback transitions | `IAIMPExtensionPlayerHook` | `IID_IAIMPServicePlayer` | `api/player.md` |
| Custom "what plays next" logic | `IAIMPExtensionPlaybackQueue(2)` | `IID_IAIMPServicePlaybackQueue` | `api/player.md` |
| Provide waveform data | `IAIMPExtensionWaveformProvider` | `IID_IAIMPServiceWaveform` | `api/player.md` |
| Visualization (embedded or windowed) | `IAIMPExtensionEmbeddedVisualization` / `IAIMPExtensionCustomVisualization` | `IID_IAIMPServiceVisualizations` | `api/visuals.md` |

## Metadata, art and lyrics

| Goal | Implement | Target service | Reference |
|---|---|---|---|
| Album art from a local source | `IAIMPExtensionAlbumArtCatalog(2)` | `IID_IAIMPServiceAlbumArt` | `api/albumarts.md` |
| Album art from the internet | `IAIMPExtensionAlbumArtProvider(2,3)` | `IID_IAIMPServiceAlbumArt` | `api/albumarts.md` |
| Lyrics provider | `IAIMPExtensionLyricsProvider` | `IID_IAIMPServiceLyrics` | `api/lyrics.md` |
| Online tag lookup ("autotagging") | `IAIMPExtensionTagsProvider` | `IID_IAIMPServiceFindTagsOnline` | `api/tag-editor.md` |
| Read/write tags yourself | `IAIMPServiceFileTagEditor`, `IAIMPFileTag` | — | `api/tag-editor.md` |

## Playlists and library

| Goal | Implement | Target service | Reference |
|---|---|---|---|
| React to playlists being added/removed/changed | `IAIMPExtensionPlaylistManagerListener` | `IID_IAIMPServicePlaylistManager` | `api/playlists.md` |
| Auto-populated ("smart") playlist source | `IAIMPExtensionPlaylistPreimageFactory` + `IAIMPPlaylistPreimage` | `IID_IAIMPServicePlaylistManager` | `api/playlists.md`, `Demos/CustomPreimageDemo` |
| Custom shuffle algorithm | `IAIMPExtensionPlaylistShuffler` (v6.00) | `IID_IAIMPServicePlaylistManager` — *the help does not state the target for this one; the playlist-manager service is the chapter's owner and matches the preimage factory* | `api/playlists.md` |
| A whole new Music Library data source | `IAIMPMLExtensionDataStorage` (+ providers, fields, filters) | `IID_IAIMPServiceMusicLibrary` | `api/music-library*.md`, `Demos/MusicLibraryDemo` |
| Query the existing library | `IAIMPServiceMusicLibrary`, `AIMPML_LOCALDATASTORAGE_ID` | — | `api/music-library.md`, `Demos/MusicLibraryBrowserDemo` |

## Cross-cutting

| Goal | Mechanism | Reference |
|---|---|---|
| Receive player events | `IAIMPMessageHook` + `IAIMPServiceMessageDispatcher.Hook` (**not** RegisterExtension) | `api/message-dispatcher*.md` |
| Drive the player / read global state | `Send(AIMP_MSG_CMD_*)`, `AIMP_MSG_PROPERTY_*` | `api/message-dispatcher-commands.md`, `-properties.md` |
| Background work | `IAIMPServiceThreads`, `IAIMPTask` | `api/threading.md` |
| HTTP requests | `IAIMPServiceHTTPClient(2,3)`, `IAIMPHTTPClientEvents` | `api/internet.md` |
| Localized UI text | `IAIMPServiceMUI` + `Langs/*.lng` | `api/multi-language-ui.md` |
| Publish a service for other plugins | `IAIMPCore.RegisterService`, `IAIMPServiceAttrExtendable`, `IAIMPServiceAttrObjects` | `concepts.md`, `Demos/CustomServiceDemo` |
| Skin / colour awareness | `IAIMPServiceSkinsManager`, `IAIMPUIColorSchema` | `api/skins.md`, `api/gui.md` |
| Control AIMP from a *separate application* | Remote API (`AIMP_RA_*`) — never from a plugin | `remote-api.md` |

## Demo projects

All demos are Delphi/Lazarus and live in `references/sdk/Demos/`:

| Demo | Shows |
|---|---|
| `MenuAndActionsDemo` | menu items, sub-items, actions, event handlers, glyphs |
| `OptionFrameDemo` | a Preferences page |
| `GUI Demo` | building a form with the GUI API |
| `SimpleInformationBar` | `IAIMPMessageHook` + a UI overlay |
| `CustomServiceDemo` | publishing your own service and extension point |
| `DemoCustomFileSystem` | `IAIMPExtensionFileSystem` + a menu entry |
| `CustomPreimageDemo` | playlist preimage factory and listener |
| `MusicLibraryDemo` | a full custom data storage with grouping trees |
| `MusicLibraryBrowserDemo` | querying the built-in library from background tasks |
| `VisualPeakDemo`, `VisualSpectrumDemo`, `VisualWaveDemo` | embedded visualizations |
| `RemoteAccessDemo` | the Remote API from an external app |
