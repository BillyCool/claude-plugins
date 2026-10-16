# Plugin anatomy: entry point, lifetime, layout

Everything here is confirmed against `references/sdk/Sources/` and the demo
projects in `references/sdk/Demos/`. Read those files when you need the exact
current text — this page is the map, not the territory.

## What a plugin is

A DLL (Windows) or `.so` (Linux) in its own folder under AIMP's `Plugins`
directory, exporting exactly one function:

```
AIMPPluginGetHeader(IAIMPPlugin **Header) -> HRESULT
```

`apiPlugin.h` declares it as
`typedef HRESULT (WINAPI *TAIMPPluginGetHeaderProc)(IAIMPPlugin **Header);`.
AIMP calls it once, gets your `IAIMPPlugin`, and drives the plugin through
that interface for the rest of the session.

`IAIMPPlugin` (apiPlugin.h) is five methods:

| Method | Purpose |
|---|---|
| `InfoGet(Index)` | name / author / short / full description — `AIMP_PLUGIN_INFO_*` |
| `InfoGetCategories()` | bitmask of `AIMP_PLUGIN_CATEGORY_*` (ADDONS, DECODERS, VISUALS, DSP, ENCODER) |
| `Initialize(IAIMPCore*)` | the only place you get the core; register everything here |
| `Finalize()` | release everything you kept |
| `SystemNotification(NotifyID, Data)` | `SERVICE_ADDED` / `SERVICE_REMOVED` / `EXTENSION_REMOVED` |

Optionally implement `IAIMPExternalSettingsDialog` (one method, `Show(HWND)`)
so AIMP's plugin list can open your settings directly.

## Initialize is the contract

`Initialize` decides whether the plugin is usable at all:

- Query every service you *require* first, and **return a failure HRESULT if
  one is missing**. AIMP then marks the plugin unused instead of running it
  half-broken. `MenuAndActionsDemoUnit.pas` does exactly this — it queries
  `IID_IAIMPServiceMenuManager` before calling `inherited Initialize`.
- A plugin can be loaded by the Audio Converter or the Advanced Tag Editor,
  not only by the player. Each documented interface's **Summary** block lists
  which applications provide it (`Applications: Player, Audio Converter, …`).
  Never assume the player's services exist.
- Register extensions and services here. Both are unregistered automatically
  before finalization, so `Finalize` only has to drop what you stored.
- Services provided by *other plugins* may not exist yet — yours can load
  first. Handle `AIMP_SYSTEM_NOTIFICATION_SERVICE_ADDED` in
  `SystemNotification` instead of giving up in `Initialize`.

If you store a service reference for later, you must also handle
`AIMP_SYSTEM_NOTIFICATION_SERVICE_REMOVED` and release the matching reference —
the docs are explicit that failing to do so can crash the host.

## Folder layout (what you ship)

From `references/concepts.md` ("Plugins folder structure"):

```
<PluginsPath>\<Plugin Name>\<Plugin Name>.dll      Windows 32-bit
<PluginsPath>\<Plugin Name>\x64\<Plugin Name>.dll  Windows 64-bit
<PluginsPath>\<Plugin Name>\x64\<Plugin Name>.so   Linux 64-bit
<PluginsPath>\<Plugin Name>\Langs\*.lng            localizations, auto-loaded
```

Get `<PluginsPath>` from `IAIMPCore.GetPath(AIMP_CORE_PATH_PLUGINS, …)`; never
hard-code it. For distribution as a `.aimppack`, see `references/packaging.md`.

## Where settings go

- Small settings → the shared config, via `IAIMPServiceConfig` (an
  `IAIMPConfig`). Keys are path-like strings.
- Anything over ~1 KB (databases, caches) → your own file under
  `IAIMPCore.GetPath(AIMP_CORE_PATH_PROFILE, …)`. Putting bulk data in the
  shared config hurts app-wide performance.

## Delphi scaffold

The SDK's own helper base class is
`references/sdk/Sources/Delphi/Helpers/AIMPCustomPlugin.pas`:

```pascal
library MyPlugin;

uses apiPlugin, MyPluginUnit in 'MyPluginUnit.pas';

{$R *.res}

function AIMPPluginGetHeader(out Header: IAIMPPlugin): HRESULT; stdcall;
begin
  try
    Header := TMyPlugin.Create;
    Result := S_OK;
  except
    Result := E_UNEXPECTED;
  end;
end;

exports AIMPPluginGetHeader;
begin
end.
```

The unit derives from `TAIMPCustomPlugin` (which itself wires
`TAIMPAPIWrappers.Initialize/Finalize`, giving you `CoreIntf`, `MakeString`,
`CheckResult` and friends) and overrides `InfoGet`, `InfoGetCategories`,
`Initialize`. Always `{$I apiConfig.inc}` — it sets `{$MINENUMSIZE 4}`, rejects
non-Unicode Delphi, and switches Free Pascal into Delphi mode.

Both Delphi (`.dproj`) and Lazarus/FPC (`.lpi`) project files ship for every
demo; FPC is how the Linux build is produced.

## C++ scaffold

`references/sdk/Sources/Cpp/` is header-only. `IUnknownImpl.h` gives you a
reference-counting base:

```cpp
class MyPlugin : public IUnknownImpl<IAIMPPlugin> { … };

extern "C" HRESULT WINAPI AIMPPluginGetHeader(IAIMPPlugin **Header)
{
    *Header = new MyPlugin();
    (*Header)->AddRef();
    return S_OK;
}
```

`ISubInterfaceImpl<Owner, T>` is for a secondary interface whose lifetime is
the owner's. `testAll.cpp` / `testAll.sh` show the include set and the Linux
compile line (`-I/usr/include/cairo`, because `HCANVAS` is a `cairo_t*` there).

## Cross-platform notes

`references/concepts.md` has the full Windows/Linux table. The parts that bite:

- `PChar` is `PWideChar` on Windows, `PAnsiChar` (UTF-8 bytes) on Linux — so
  `IAIMPString` element indices are not character indices on either platform.
- `HDC` → `HCANVAS`, a `cairo_t*` on Linux.
- `HWND` on Linux is emulated by the GUI API and is not interoperable with
  other toolkits; a plugin with its own UI must move to the GUI API.
- `OleVariant` → `VarValue`, with `VarValueInit`/`VarValueFree` helpers in
  `apiTypes`.
- `LoadFromResource` / `LoadFromBitmap` variants are Windows-only; use the
  stream-based alternatives (`IAIMPUIImageList3.LoadFromStream`).
- Third-party native libraries must be loaded dynamically in `Initialize` and
  unloaded in `Finalize`; Linux will not find them next to your module.
