# Metadata block

Confirmed against Violentmonkey source, `src/background/utils/script.js`
(`parseMeta`, `metaTypes`, `metaOptionalTypes`) and `src/common/consts.js`
(`GM_API_NAMES`). This is the actual parser, not a doc summary — it explains
*why* each key behaves the way it does, not just what to write.

## How the parser works (matters for every key below)

Each metadata line is `// @key value`. The parser strips `@`, splits off an
optional `:locale` suffix, camelCases the key (`exclude-match` →
`excludeMatch`, `run-at` → `runAt`), and looks it up in one of three buckets:

- **`arrayType`** — every occurrence is pushed onto an array. Repeatable by
  design.
- **`booleanType`** — presence of the line sets `true`. The value text after
  the key is ignored; you don't need `// @noframes true`, just `// @noframes`.
- **`defaultType`** (the fallback for *any* key not explicitly listed below,
  including `@name`, `@version`, custom/unknown keys) — single value, **first
  occurrence wins**, later repeats of the same key are silently ignored.

This means an unrecognized directive doesn't error — it's parsed and stored as
a plain string, just not read by Violentmonkey itself. Useful for
build-tooling metadata, not for anything Violentmonkey acts on.

`:locale` suffix works on any key: `@name:zh-CN`, `@description:fr`.

## Array-type (repeatable) keys

| Directive | Purpose |
|---|---|
| `@match` | Chrome-extension-style match pattern. Prefer over `@include`. |
| `@exclude-match` | Same syntax as `@match`, negates. |
| `@include` | Legacy wildcard/regex pattern. |
| `@exclude` | Legacy wildcard/regex pattern, negates. |
| `@require` | URL of an external script to load before this one runs. |
| `@grant` | One GM API name per line (or the literal `none`). Full list below. |
| `@antifeature` | Declares a non-privacy-friendly feature (ads, tracking, miner, membership). Informational. |
| `@compatible` | Declares tested browser compatibility. Informational. |
| `@connect` | Declares an intended cross-origin host for `GM_xmlhttpRequest`/`GM_download`. **Not enforced at runtime by Violentmonkey** (no permission-check code found in source) — unlike Tampermonkey, it does not gate the request. Still worth adding for portability/documentation. |
| `@tag` | Organizational tag shown in the UI. |

`@resource` is array-syntax on the line (`@resource name URL`) but merges into
a `{name: url}` object rather than a plain array — see below.

## Boolean-flag keys (presence = true, no value needed)

| Directive | Effect |
|---|---|
| `@noframes` | Script runs only in the top-level document, not in iframes. |
| `@top-level-await` | Enables top-level `await` in the script body — Violentmonkey wraps the auto-generated IIFE as `(async () => { ... })()` instead of a sync IIFE when this is set. See `sandbox-and-injection.md`. |
| `@unwrap` | **Disables Violentmonkey's own automatic IIFE wrapping.** Only set this if you have a specific reason to run fully unwrapped at the top of the injected realm; for ordinary scripts leave it off — VM already wraps for you, so you never need your own manual wrapper either way. |

## Single-value keys (first occurrence wins)

Not an exhaustive enumerated list in source — any key not in the two tables
above falls here automatically. The common ones:

| Directive | Purpose |
|---|---|
| `@name` | Script name (required in practice; combined with `@namespace` for a unique ID). |
| `@namespace` | Disambiguates scripts with the same `@name`. |
| `@version` | Update-check version string (e.g. `1.2.3`, `1.2a.3`). |
| `@description` | Shown in the script list. |
| `@icon` | URL to an icon image. |
| `@run-at` | One of `document-start`, `document-body`, `document-end` (default), `document-idle`. Regex-validated in source (`RUN_AT_RE`); anything else is rejected. |
| `@inject-into` | `page`, `content`, or `auto` (default). See `sandbox-and-injection.md`. |
| `@downloadURL` | Where Violentmonkey checks for/downloads script updates. |
| `@updateURL` | Falls back to `@downloadURL` if unset; used for the update-check request specifically. |
| `@supportURL` | Support/issues link shown in the UI. |
| `@homepageURL` | Homepage link shown in the UI. |

## `@resource` — special merge behavior

Each line is `@resource name URL`. The parser regex-splits on the first
whitespace run (`/^(\w\S*)\s+(.*)/`) and builds `meta.resources = {name: url}`.
Fetch the content in-script with `GM_getResourceText(name)` /
`GM_getResourceURL(name)`.

## `@grant` — the exhaustive list

Confirmed from `src/common/consts.js`, `GM_API_NAMES` (this is the *complete*
array Violentmonkey checks against — nothing else is a valid grant target
besides the literal `none`):

```
GM              GM_addElement            GM_addStyle
GM_addValueChangeListener                 GM_cookie
GM_deleteValue  GM_deleteValues           GM_download
GM_getResourceText                        GM_getResourceURL
GM_getValue     GM_getValues              GM_info
GM_listValues   GM_log                    GM_notification
GM_openInTab    GM_registerMenuCommand    GM_removeValueChangeListener
GM_setClipboard GM_setValue               GM_setValues
GM_unregisterMenuCommand                  GM_xmlhttpRequest
unsafeWindow
```

- `@grant GM` grants the **entire** promise-based `GM.*` namespace at once —
  shorthand instead of listing every `GM.*` alias individually.
- `@grant none` is a special literal, not in the list above — it means "no
  sandbox, no GM APIs at all" (except `GM_info`, which is always available
  regardless of grants).
- `GM_info` needs no `@grant` — it's always present.
