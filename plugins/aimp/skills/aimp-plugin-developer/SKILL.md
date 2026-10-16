---
name: aimp-plugin-developer
description: >-
  Expert AIMP plugin development against a full offline copy of the AIMP SDK
  (v6.00 build 3000) — every interface, message, property and constant from the
  official help, plus the SDK's own headers and demo projects. Use for any AIMP
  work: writing or debugging a plugin, adding menu items/actions/options pages,
  audio decoders, visualizations, playlist or Music Library extensions, tag and
  album-art providers, the GUI API, the message dispatcher ("add a menu item to
  AIMP", "how do I hook track change", "what PROPID sets the volume", "why does
  this return E_ACCESSDENIED"), packaging a .aimppack, or the Remote API.
---

# AIMP plugin developer

AIMP's plugin API is COM-shaped but hand-rolled: `IUnknown`-derived interfaces,
`HRESULT` returns, GUID identity, everything reached through `IAIMPCore`. It is
also strict — wrong thread, unchecked service, or a property read with the
wrong accessor all fail quietly or with a bare `E_*`. The SDK ships complete
documentation; this skill carries it offline so answers come from the SDK, not
from recall.

**Never write an AIMP signature, PROPID, GUID or constant from memory.** Look
it up in `references/` first. The API has hundreds of `AIMP_*_PROPID_*` values
whose names are close enough to guess wrong.

## Finding the answer

1. **`references/topics-index.md`** — every documented interface, message and
   property, with the file it lives in. Grep this first; it is the fastest path
   from a name to a page.
2. **`references/guides/extension-points.md`** — the reverse lookup: "I want
   AIMP to do X" → which interface to implement, which service to register it
   with, which reference page to read.
3. **`references/sdk/Sources/`** — the SDK's actual C++ headers (`Cpp/api*.h`)
   and Delphi units (`Delphi/api*.pas`). These are authoritative for exact
   signatures, GUID bytes and constant values. Grep here whenever the prose is
   ambiguous or you need the literal declaration.
4. **`references/sdk/Demos/`** — twelve complete, working Delphi/Lazarus
   plugins. When a task resembles one, read it; the demos show the real
   registration and lifetime patterns, not simplified sketches.

## How to work

**Ground the answer.** Read the reference page for every interface you touch,
and check the header for the exact declaration before writing a signature. If
the user names a constant, confirm it exists — do not adapt a similar one.

**Check the Summary block.** Every documented interface and member ends with:

- `Definition:` which header/unit declares it,
- `Multi-threading:` supported or not — assume **not**,
- `Applications:` Player / Audio Converter / Advanced Tag Editor — a plugin can
  be loaded by any of them, so a service you need may simply be absent,
- `Minimal Version:` the AIMP build that introduced it.

Surface the version and threading facts in your answer when they matter. If a
member needs a build newer than the plugin's likely target, say so and give the
fallback (query the numbered interface; handle failure).

**Match the language.** The demos and helper layer are Delphi/Free Pascal, and
that is the SDK's centre of gravity — default to it unless the user is clearly
in C++. In Delphi lean on the SDK's own helpers
(`references/sdk/Sources/Delphi/Helpers/`): `TAIMPCustomPlugin`,
`TInterfacedObjectEx`, `CoreIntf`, `MakeString`, `CheckResult`,
`PropListGet*`/`PropListSet*`, `uiCreateAction`, `uiWrap`. Re-implementing
those by hand is a smell. In C++ use `IUnknownImpl<T>` from `IUnknownImpl.h`.

**Register in `Initialize`, release in `Finalize`.** Extensions and services
registered through `IAIMPCore` are torn down automatically; anything you cached
is not. If the plugin stores a service reference, it must handle
`AIMP_SYSTEM_NOTIFICATION_SERVICE_REMOVED`.

**Check every HRESULT.** Including `QueryInterface` for services — a missing
service is a normal condition, not an exceptional one.

**Be honest about gaps.** Some behaviour is genuinely undocumented (a few
extensions do not state which service they register with). Say which parts are
confirmed in the SDK and which are inference, rather than presenting both with
the same confidence.

## Reference map

Conceptual, read these before building something new:

- `references/guides/plugin-anatomy.md` — entry point, `IAIMPPlugin` lifecycle,
  folder layout, settings storage, Delphi and C++ scaffolds, Windows/Linux
  differences
- `references/guides/idioms.md` — services vs objects vs extensions,
  refcounting, HRESULTs, `IAIMPString` and UTF-8/UTF-16 indexing, property
  lists, threading, versioning
- `references/guides/extension-points.md` — task → extension → service → page
- `references/concepts.md` — the SDK's own overview: services, custom services,
  plugin folder, settings, strings, GDI+, Linux support

API reference, generated from the official help:

- `references/basic-interfaces.md` — `IAIMPCore`, `IAIMPPlugin`,
  `IAIMPExternalSettingsDialog`
- `references/primitives.md` — `IAIMPString`, `IAIMPStream`, `IAIMPConfig`,
  `IAIMPPropertyList`, `IAIMPObjectList`, `IAIMPImage`, `IAIMPErrorInfo`,
  `HCANVAS`, `VarValue` and the rest of the shared vocabulary
- `references/api/` — one file per chapter: `actions`, `albumarts`, `core`,
  `decoders`, `file-manager`, `gui` (+ `gui-dialogs`,
  `gui-non-visual-objects`, `gui-controls/` one file per control),
  `internet`, `lyrics`, `menu`, `message-dispatcher` (+ `-commands`,
  `-properties`, `-events`), `multi-language-ui`, `music-library` (+
  `-services-and-extensions`, `-primitives`), `options-dialog`, `player`,
  `playlists`, `skins`, `tag-editor`, `threading`, `visuals`
- `references/remote-api.md` — `AIMP_RA_*` for **external applications only**;
  the docs are explicit that plugins must not use it
- `references/whats-new.md` — what each AIMP version added, useful for dating a
  member

Formats and packaging:

- `references/packaging.md` — `.aimppack` layout for plugins, skins, icon sets
- `references/cli-encoders.md` — integrating a command-line encoder via
  `enc_*.xml`
- `references/playlist-file-format.md` — AIMPPL4 sections and keys
- `references/xspf-extensions.md` — AIMP's XSPF extensions

Provenance and version: `references/version.md`.

## Keeping this current

`references/` is generated from a specific SDK drop; nothing in it is written
from memory. When a new SDK ships, the sibling **`aimp-sdk-skill-maintainer`**
skill regenerates it. Don't hand-edit anything under `references/` except
`references/guides/`, which is the hand-written layer the generator leaves
alone.
