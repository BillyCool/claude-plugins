# Working idioms: objects, strings, properties, threads, errors

The AIMP API is COM-shaped but not COM: plain `IUnknown`-derived interfaces,
`HRESULT` returns, GUID identity, no registry, no apartments. These are the
conventions that decide whether a plugin is correct or subtly broken.

## Getting hold of things

Three distinct verbs, and mixing them up is the most common beginner error:

| You want | Call | Notes |
|---|---|---|
| A **service** the host provides | `IAIMPCore.QueryInterface(IID_IAIMPServiceXxx, …)` | Always check the result — a service can be absent |
| A **new object** (menu item, string, list, file info…) | `IAIMPCore.CreateObject(IID_IAIMPXxx, …)` | The host constructs it; you own the reference |
| To **plug your code in** | `IAIMPCore.RegisterExtension(IID_IAIMPServiceXxx, YourObject)` | The service IID is the *target*, your object is the extension |

`RegisterService` is only for publishing a service of your own. Extensions and
services registered through the core are unregistered automatically before the
plugin is unloaded — see `Demos/CustomServiceDemo`.

The recommended shape (from the SDK docs) is acquire → use → release:

```pascal
if Succeeded(CoreIntf.QueryInterface(IID_IAIMPServiceVersionInfo, AVerInfo)) then
try
  // do something
finally
  AVerInfo := nil;
end;
```

Prefer *not* to cache service references. If you must, release them on
`AIMP_SYSTEM_NOTIFICATION_SERVICE_REMOVED`.

## Reference counting

Delphi and C++Builder manage `IUnknown` refcounts for you; raw C++ does not.
For C++ use `IUnknownImpl<T>` from `references/sdk/Sources/Cpp/IUnknownImpl.h`
for your own objects, and match every `QueryInterface`/`CreateObject` with a
`Release()`. Objects you hand to `RegisterExtension` are retained by the host.

In Delphi, the SDK's `TInterfacedObjectEx` (in `apiWrappers.pas`) is the base
to use for objects you pass to AIMP — it implements `IUnknown` with the
platform-correct calling convention (`stdcall` on Windows, `cdecl` elsewhere).

## HRESULT, always

Every method that can fail returns `HRESULT`. The recurring set:

- `S_OK` — success
- `E_INVALIDARG` — bad argument
- `E_NOTIMPL` — not implemented (very common: newer interface on older build)
- `E_UNEXPECTED` — general failure
- `E_ACCESSDENIED` — usually "called from a non-main thread"
- `E_FAIL` — operation-specific refusal

Never ignore a return value; the docs mark which codes each method can produce.
In Delphi, `CheckResult(HRESULT)` from `apiWrappers.pas` raises on failure.
When an API hands you an `IAIMPErrorInfo`, fill it — `CoreProcessException`
shows the pattern for turning a Pascal exception into an HRESULT plus error
info.

## Strings

Strings cross the boundary as `IAIMPString`, not raw pointers. Create one with
`IAIMPCore.CreateObject(IID_IAIMPString, …)`, or in Delphi with `MakeString(s)`
and back with `IAIMPStringToString(s)`.

The trap is indexing: `IAIMPString.Get`/`Set` index *elements*, not characters.
On Linux elements are UTF-8 bytes (1–8 per character); on Windows they are
UTF-16 code units (1–2 per character). Slicing at an arbitrary offset can split
a character. See "Working with strings" in `references/concepts.md`.

## Property lists

Many objects expose their state through `IAIMPPropertyList` rather than named
methods: menu items, playlists, forms, controls, the player itself. The shape
is always the same — an `AIMP_XXX_PROPID_*` constant plus a typed accessor:

```
GetValueAsInt32 / SetValueAsInt32
GetValueAsInt64 / SetValueAsInt64
GetValueAsFloat / SetValueAsFloat
GetValueAsObject / SetValueAsObject
GetValueAsVariant / SetValueAsVariant   (IAIMPPropertyList2, VarValue)
BeginUpdate / EndUpdate                 (batch changes)
Reset
```

Each reference page lists, per PROPID, its **Type** and which accessor pair
reads and writes it — use exactly those. A service that has properties says so:
"An access to the IAIMPPropertyList interface is provided by
`<IAIMPServiceXxx>.QueryInterface(IID_IAIMPPropertyList, ..)`".

Delphi shortcut helpers: `PropListGetInt32/GetStr/GetObj/SetStr/…` and the
`TAIMPPropertyList` base class for implementing one yourself.

## Threading

Assume **not thread-safe** unless the page says otherwise. Every documented
interface carries a `Multi-threading:` line in its Summary block; check it
before touching an object from a worker.

- All GUI API calls are main-thread only — the wrong thread returns
  `E_ACCESSDENIED`.
- Background work belongs in `IAIMPServiceThreads` (`IAIMPTask`,
  `IAIMPTaskOwner`, `IAIMPTaskPriority`) — see `references/api/threading.md`
  and `Demos/MusicLibraryBrowserDemo`, which marshals results back to the UI
  through a task callback synchronizer.

## Messages and events

`IAIMPServiceMessageDispatcher` is the single channel for commands, global
properties, and events:

- `Send(AIMP_MSG_CMD_*)` to do something,
- `Send(AIMP_MSG_PROPERTY_* , AIMP_MSG_PROPVALUE_GET/SET, &value)` to read or
  write a global property,
- implement `IAIMPMessageHook` and `Hook()` it to receive `AIMP_MSG_EVENT_*`.

Note this is a *hook*, registered with `IAIMPServiceMessageDispatcher.Hook`,
not `RegisterExtension`. `Demos/SimpleInformationBar` is the worked example.

## Versioning honestly

Every documented member has a **Minimal Version** in its Summary block. When
you use one that is newer than the AIMP release the user might run, either:

- check with `IAIMPServiceVersionInfo` (`GetVersionID`, `GetBuildNumber`, or
  Delphi's `CoreCheckVersion`), or
- rely on the numbered-interface convention: `IAIMPServicePlayer2`,
  `IAIMPImage3`, `IAIMPPlaylistQueue2` are later revisions, and
  `QueryInterface` for them simply fails on older builds. Query the newest you
  can use, fall back to the base interface.

`E_NOTIMPL` from a method you expected to work usually means exactly this.
