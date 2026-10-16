# GM_* / GM.* API

Confirmed from `src/injected/web/gm-api.js`, `gm-api-wrapper.js`,
`requests.js`, and `src/background/utils/requests-core.js` (forbidden
headers), cross-checked against the docs site's `/api/gm/` page. Every
function needs the matching `@grant` from `metadata-block.md`'s list unless
noted otherwise.

Every `GM_*` function has a promise-based `GM.*` twin (Greasemonkey-4-style).
The rename isn't always a mechanical case change — `GM_xmlhttpRequest` becomes
`GM.xmlHttpRequest` (capital H), `GM_getResourceURL` becomes
`GM.getResourceUrl` (lowercase url). `GM.info` is a synchronous property, not
a function, on both forms.

## Storage

| Function | Signature | Grant |
|---|---|---|
| `GM_getValue` | `(key, defaultValue)` → value | `GM_getValue` |
| `GM_setValue` | `(key, value)` → void (value must be JSON-serializable) | `GM_setValue` |
| `GM_deleteValue` | `(key)` → void | `GM_deleteValue` |
| `GM_listValues` | `()` → `string[]` of all keys | `GM_listValues` |
| `GM_getValues` | `(keysArray \| keysObjectWithDefaults)` → object | `GM_getValues` |
| `GM_setValues` | `(object)` → void, batch set | `GM_setValues` |
| `GM_deleteValues` | `(keysArray)` → void, batch delete | `GM_deleteValues` |
| `GM_addValueChangeListener` | `(key, (key, oldValue, newValue, remote) => void)` → `listenerId` string. `remote === true` means another tab changed it. | `GM_addValueChangeListener` |
| `GM_removeValueChangeListener` | `(listenerId)` → void | `GM_removeValueChangeListener` |

Values are per-script, isolated by the script's storage id — two scripts
never share `GM_setValue` state even on the same site.

## Resources (`@resource name URL` in metadata)

| Function | Signature | Grant |
|---|---|---|
| `GM_getResourceText` | `(name)` → string content of the resource | `GM_getResourceText` |
| `GM_getResourceURL` | `(name, isBlobUrl?)` → `blob:` URL by default, or `data:` URL if `isBlobUrl === false`. `GM.getResourceUrl` is the async form (note the `Url` casing). | `GM_getResourceURL` |

## DOM & UI

| Function | Signature | Grant | Notes |
|---|---|---|---|---|
| `GM_addElement` | `(tagName, attributes)` or `(parentNode, tagName, attributes)` → the created `Element`, synchronously | `GM_addElement` | Bypasses strict CSP that would block a manually-created `<script>`/`<style>`/`<link>`. |
| `GM_addStyle` | `(css)` → the injected `<style>` element | `GM_addStyle` | Simple, unscoped CSS injection. For anything needing a real UI surface, prefer `@violentmonkey/ui`'s shadow-DOM-isolated panel/toast instead of hand-building a styled `<div>`. |
| `GM_setClipboard` | `(data, type = 'text/plain')` → void, synchronous | `GM_setClipboard` | Prefer this over `navigator.clipboard.writeText()` — no document-focus requirement, no permission prompt, works from any handler. |
| `GM_openInTab` | `(url, options \| loadInBackgroundBoolean)` → control object with `.close()`, `.closed`, `onclose` callback | `GM_openInTab` | |
| `GM_notification` | `(options)` or `(text, title, image, onclick)` → control object with `.remove()` | `GM_notification` | Supports `tag` (dedupe) and `zombieTimeout`. |
| `GM_registerMenuCommand` | `(caption, onClick, options?)` → string id | `GM_registerMenuCommand` | Adds an item to the extension's popup menu. `options.id` lets you target a stable id across re-registrations; `options.autoClose` controls whether the popup closes after click. |
| `GM_unregisterMenuCommand` | `(captionOrId)` → void | `GM_unregisterMenuCommand` | |

## Network

| Function | Signature | Grant |
|---|---|---|
| `GM_xmlhttpRequest` | `(details)` → control object with `.abort()` | `GM_xmlhttpRequest` |
| `GM_download` | `(options)` or `(url, name)` → control object | `GM_download` |

### `GM_xmlhttpRequest(details)` — full option set

Confirmed key-by-key from `src/injected/web/requests.js` (`OPTS_TO_PASS`,
`OPTS_TO_KEEP`, destructuring in `onRequestCreate`):

- `url` (required — throws `"Required parameter \"url\" is missing."` if
  absent; accepts a string, a `URL`, or anything stringifiable)
- `method` — default `GET`
- `headers` — object of header name → value. See forbidden-header list below.
- `data` — request body. Strings, `FormData`, `URLSearchParams`, and
  Blob/binary all work; non-object values are stringified unless `binary` is set.
- `binary` — `true` forces `data` to be sent as a plain string (TM/GM
  compatibility flag for raw-body requests).
- `timeout` — ms.
- `responseType` — `''` (text, default), `'text'`, `'json'`, `'document'`,
  `'blob'`, or `'arraybuffer'`. Anything else logs a console warning and falls
  back to `''`.
- `overrideMimeType` — string, forwarded to the underlying `XMLHttpRequest`.
- `user`, `password` — HTTP auth.
- `context` — arbitrary value of your choosing, round-tripped back onto the
  response object untouched. Handy for correlating concurrent requests.
- `anonymous` — `true` omits credentials (cookies) for the request. GM4
  compatibility: you may instead pass `withCredentials` (default `true`);
  `anonymous` is just `!withCredentials` under the hood, `anonymous` wins if
  both given.
- `upload` — object of `on*` upload-progress handlers (mirrors the event list
  below), for tracking request body upload progress.
- Event callbacks: `onload`, `onloadstart`, `onloadend`, `onprogress`,
  `onreadystatechange`, `onerror`, `onabort`, `ontimeout`. Exactly this set is
  wired up (`EVENTS_TO_NOTIFY` in source) — nothing else is recognized.

Returns synchronously if `@grant GM_xmlhttpRequest`; `GM.xmlHttpRequest`
(capital H) returns a `Promise` that resolves on `load` and rejects on
`error`, in addition to still firing whichever `on*` callbacks you passed.

**Forbidden headers** — setting these via `headers` is silently blocked by
the browser itself, not by Violentmonkey (confirmed from
`FORBIDDEN_HEADER_RE` in `src/background/utils/requests-core.js`, which
matches the standard [Forbidden header name](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_header_name) list):
any header starting with `Proxy-` or `Sec-`, plus the exact names
`Accept-Charset`, `Accept-Encoding`, `Access-Control-Request-Headers`,
`Access-Control-Request-Method`, `Connection`, `Content-Length`, `Cookie`,
`Cookie2`, `Date`, `DNT`, `Expect`, `Host`, `Keep-Alive`, `Origin`, `Referer`,
`TE`, `Trailer`, `Transfer-Encoding`, `Upgrade`, `Via` (case-insensitive).

### `GM_download(options)` / `GM_download(url, name)`

Thin wrapper over `GM_xmlhttpRequest` — confirmed from source it forces
`responseType: 'blob'`, `data: null`, `method: 'GET'`,
`overrideMimeType: 'application/octet-stream'` onto whatever options you pass,
and requires a `name` (second positional arg, or `options.name`) — errors if
missing or not a string. Accepts the same event-callback options as
`GM_xmlhttpRequest` otherwise.

**Saving locally-built content (e.g. a generated `.md`/`.json`/`.csv`) through
`GM_download` is genuinely unreliable — neither obvious approach is safe to
rely on alone, confirmed two different ways in a real script:**

- **A `data:` URL as `url`** — plausible-looking (a plain string, no
  Blob-realm/messaging concerns, and both `fetch()`/XHR and
  `browser.downloads.download()` can read a `data:` URL's bytes in
  principle) but **confirmed hard-broken specifically on the "Use browser
  download API" path in Firefox**: `browser.downloads.download({ url:
  'data:...' })` throws `Error processing url: Error: Access denied for URL
  data:...  for downloads.download` — a hardcoded security restriction in
  Firefox itself (data: URLs are disallowed for that API, not something
  fixable by reshaping the URL). This is a definitive block, seen directly
  in a `GM_download` `onerror` payload, not a guess.
- **A raw `Blob` as `url`** — what source reading suggests is the "correct"
  answer: `src/background/utils/requests.js` does
  `if (IS_FIREFOX && opts.url instanceof Blob) { opts.url = leaseBlobUrl(opts.url) }`
  before either download path runs, converting a passed Blob into a real
  `blob:` URL created in the *background/extension* context specifically so
  a page-context `blob:` URL's realm problem doesn't apply — `blob:` URLs
  (unlike `data:`) are NOT subject to the same Firefox `downloads.download`
  restriction. This *should* work per source, but an earlier attempt in a
  real script failed with no visible error (no `onerror` logging was wired
  up at the time, so the exact cause was never pinned down) — treat as
  "plausible, not confirmed" until proven live with proper error logging.

**Practical recommendation:** always wire up `onerror`/`ontimeout` and log
what they receive — silent failure here has burned real time twice. And
don't let a `GM_download` failure for locally-built content be a hard
failure for the user: fall back to the plain, guaranteed-to-work technique
(`URL.createObjectURL` + `<a download>` + synthetic click, in page context)
if `GM_download` reports failure —

```js
function saveBlobLocally(blob, filename) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename; // basename only -- see the no-subfolder note below
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 5000);
}
```

This fallback can't place the file in a subfolder (see the `download`-attribute
restriction below), but it always saves *something* rather than leaving the
user with a failed download and no recourse.

**Two entirely different save mechanisms exist, and which one runs changes
what `name` can do.** Confirmed from
`src/background/utils/requests.js`, `download-via-api.js`, and
`src/injected/content/requests.js`:

- **Default (off): content-script fallback.** When Violentmonkey's own
  **Settings → "Use browser download API"** toggle (`kGmDownloadViaApi` /
  `gmDownloadViaApi` in `src/common/options-defaults.js`, default `false`) is
  off — or the extension lacks the optional `downloads` permission — the
  fetched blob is handed back to a content script, which does exactly what
  you'd hand-roll yourself: `createObjectURL` + `<a href=blobUrl download=name>`
  + a synthetic click (`src/injected/content/requests.js`'s `download()`).
  Because this is a real anchor click from page/content-script context,
  **any directory component in `name` is silently dropped** — this is a
  browser security restriction on the `download` attribute, not something
  Violentmonkey controls — the file always lands flat in the Downloads root.
  It's also indistinguishable, from the browser's own anti-abuse heuristics,
  from a page spamming manual downloads: firing several `GM_download` calls
  in a row (a bulk-download loop, a multi-file post) can trigger the
  browser's own "this site is trying to download multiple files" block/allow
  prompt, and on some hardened/privacy-focused browsers (e.g. Mullvad
  Browser, which is Tor-Browser-derived) files can still fail to reliably
  land on disk afterward even once the user clicks "Allow" there — that
  symptom (progress reaches 100%, `onload` fires, nothing appears in
  `about:downloads`) is a strong signal to check this setting, not a script
  bug.
- **Opt-in (on): real browser API.** With the setting on *and* the
  `downloads` permission granted, `HttpRequest`'s handler in
  `src/background/utils/requests.js` computes
  `dlInApi = fileName && !dlInTab && permissionDownloads && getOption(kGmDownloadViaApi)`
  and routes to `download-via-api.js`, which calls the real
  `browser.downloads.download({ filename: fileName, url, headers, method,
  saveAs, ... })` — the privileged WebExtension API, not a page-level trick.
  Per that API's own contract, **`filename` supports `"subfolder/name.ext"`
  relative to the Downloads directory** (forward slashes, no leading slash,
  no `..`) — this is the *only* path that actually creates subfolders; ask
  for one via `name`/`filename` and it silently degrades to a flat filename
  under the fallback mechanism above instead of erroring.

Practical implication for a script that wants organized downloads: build
`name` as `"<subfolder>/<file>.ext"` unconditionally — it's free, correct
behavior either way (nested when the API setting is on, same flat name as
before when it's off), so there's no need to detect which mode is active.

## Cookies — `GM_cookie`

**Not documented on the `/api/gm/` page as of this writing; confirmed
directly from `gm-api.js`/`gm-api-wrapper.js` source.** Tampermonkey-compatible
shape: an object with three methods, each `(details, callback)`:

```js
GM_cookie.list(details, (cookies, error) => { ... });
GM_cookie.set(details, (error) => { ... });
GM_cookie.delete(details, (error) => { ... });
```

`@grant GM_cookie` covers all three. `details` follows the browser's own
`cookies` API shape (`name`, `url`, `domain`, etc. depending on operation).
When used as `GM.cookie.list/set/delete`, they're promise-based like the rest
of the `GM.*` namespace.

## Misc

| Function | Grant | Notes |
|---|---|---|
| `GM_info` | **none needed** — the only genuinely grant-free API (confirmed absent from `GM_API_NAMES` in source) | Object: `script` (parsed metadata), `scriptHandler` (`"Violentmonkey"`), `scriptMetaStr`, `version`, `uuid`, `injectInto` (`"auto"`\|`"page"`\|`"content"` — tells you which mode actually got used), `isIncognito`, `platform`, `userAgentData`. |
| `GM_log` | `GM_log` | Despite reading like a debugging primitive, it's in `GM_API_NAMES` and needs its own `@grant` line. Implemented via native `console.log` internally (for clickable source links), which is just an implementation detail — the grant requirement still applies. |
| `unsafeWindow` | `@grant unsafeWindow` | Not a function — a property. See `sandbox-and-injection.md`. |
