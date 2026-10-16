# Canonical AIMP SDK sources

The SDK is distributed as a zip by the vendor, not as a repository. There is no
release feed to poll and nothing here fetches it: **the user supplies an
unpacked drop, and its version lives in the source headers.** If no path was
given, ask for one.

## Drop layout

```
<sdk>/
  Help/AIMP-en.chm            official API reference (English)
  Help/AIMP-ru.chm            same, Russian — occasionally more complete
  Sources/Cpp/api*.h          C++ headers: interfaces, GUIDs, constants
  Sources/Cpp/IUnknownImpl.h  refcounting base for C++ plugins
  Sources/Cpp/testAll.{cpp,sh} include set + the Linux compile line
  Sources/Delphi/api*.pas     the same API for Delphi / Free Pascal
  Sources/Delphi/apiConfig.inc compiler switches every unit must include
  Sources/Delphi/Helpers/     TAIMPCustomPlugin, apiWrappers*, GUI/menu adapters
  Sources/Delphi/Internal/    apiDeprecated, apiCDDA, apiScrobbler, apiUpdater
  Demos/                      twelve complete Delphi/Lazarus plugins
  *.rtf                       add-on packaging, CLI encoders, playlist format,
                              XSPF extensions
```

## Authority order

1. **`Sources/`** — exact signatures, GUID bytes, constant values, calling
   conventions. Wins over everything.
2. **`Help/AIMP-en.chm`** — semantics, threading, minimal version,
   which applications provide a service, property types and accessors.
3. **`Demos/`** — how the pieces are actually wired together.
4. **`.rtf` notes** — packaging and file formats, nothing else.

Anything not in one of these four is not a source.

## Anchors

| Anchor | Confirms | Writer file |
|---|---|---|
| `Sources/Cpp/apiPlugin.h` header comment (`Target:`) | the SDK version string | `references/version.md` |
| `Help/AIMP-en.chm` → `TOC.hhc` | the chapter layout the reference tree mirrors | `references/api/*`, `concepts.md`, `primitives.md`, `basic-interfaces.md`, `remote-api.md` |
| `grep "^class IAIMPExtension" Sources/Cpp/*.h` | the complete extension-point list | `references/guides/extension-points.md` |
| `grep "^class IAIMPService" Sources/Cpp/*.h` | the complete service list | `references/guides/extension-points.md` |
| each service topic's `Extensions:` Summary line | which extensions a service accepts | `references/guides/extension-points.md` |
| `Sources/Cpp/apiPlugin.h` (`AIMP_PLUGIN_*`) | plugin categories, info indices, system notifications | `references/guides/plugin-anatomy.md` |
| `Sources/Cpp/apiCore.h` (`AIMP_CORE_PATH_*`) | the path IDs `GetPath` accepts | `references/guides/plugin-anatomy.md` |
| `Sources/Delphi/Helpers/apiWrappers.pas` interface section | the Delphi helper surface (`CoreIntf`, `MakeString`, `CheckResult`, `PropList*`, `Lang*`) | `references/guides/idioms.md` |
| `Sources/Delphi/Helpers/AIMPCustomPlugin.pas`, `apiConfig.inc` | the Delphi plugin scaffold | `references/guides/plugin-anatomy.md` |
| `Sources/Cpp/IUnknownImpl.h` | the C++ scaffold | `references/guides/plugin-anatomy.md` |
| `Demos/` directory listing + each demo's `RegisterExtension` calls | the demo table and real registration targets | `references/guides/extension-points.md` |
| the help's "Linux support" topic | the Windows/Linux API differences table | `references/guides/plugin-anatomy.md` |

## Method notes

- The CHM's topic pages are machine-generated with a stable class vocabulary
  (`group_header`, `cm_table`, `code_param_var`, `code_param_notes`, `hotkey`).
  `chm2md.py` keys off exactly those; if AIMP changes its doc generator, that
  is the file to fix.
- `TOC.hhc` is the layout spine. Files are one per chapter, auto-split into
  sub-group files (and then per-topic files) past a size threshold — so a
  chapter that grows reorganises itself instead of becoming unreadable.
- The property surface is in the hundreds of `AIMP_*_PROPID_*` constants;
  never diff it by reading. Regenerate and use `git diff`.
- `Sources/Delphi/Internal/` (apiDeprecated, apiCDDA, apiScrobbler, apiUpdater)
  is vendored but deliberately not surfaced in the writer skill's guidance —
  it is internal/deprecated surface, not something to build on.
