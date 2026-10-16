# Redirector engine semantics

Confirmed against the source of einaregilsson/Redirector **v3.5.4** (`manifest_version` 2): `js/redirect.js`
(matching), `js/background.js` (request handling), `js/importexport.js` (file format), `redirector.html`
(form values), `help.html` (official docs). Where the help text and the code disagree, **the code is right**
and the disagreement is flagged below.

## The rule object (also the import/export shape)

| Field | UI label | Notes |
|---|---|---|
| `description` | Description | Optional label. Part of the dedupe key. |
| `exampleUrl` | Example URL | **Required by the UI** ("No example URL defined"). Must match include, must not match exclude. |
| `exampleResult` | Example result | Derived. Write what the engine produces; the builder script fills it. |
| `includePattern` | Include pattern | Required. |
| `excludePattern` | Exclude pattern | Optional. Same pattern type as include. |
| `redirectUrl` | Redirect to | Template; `$1`, `$2`... substituted. |
| `patternType` | Pattern type | `"W"` wildcard (default) or `"R"` regex. |
| `patternDesc` | Pattern Description | Optional free text. |
| `processMatches` | Process matches | `noProcessing` (default), `urlEncode`, `urlDecode`, `doubleUrlDecode`, **`base64decode`** (lowercase `d`; help.html's heading says "Base64 Decode" but the stored value and the code check are `base64decode`; a wrong-cased value silently does nothing). |
| `appliesTo` | Apply to | Array of request types; default `["main_frame"]`. |
| `disabled` | (toggle in list) | Default `false`. |
| `grouped` | (organize mode) | Visual grouping only. Default `false`. |
| `error` | | Derived; `null` when valid. |

`appliesTo` values and their UI labels: `main_frame` Main window (address bar), `sub_frame` IFrames,
`stylesheet`, `font`, `script`, `image`, `imageset` Responsive Images in Firefox, `media` Media (audio/video),
`object`, `object_subrequest`, `xmlhttprequest` (Ajax), `history` HistoryState, `other`.

## Matching

1. **Wildcard (`W`)**: the pattern is converted to a regex: starts `^`, ends `$`, `*` becomes `(.*?)`, and
   only these characters are escaped: `( ) [ ] { } ? . ^ $ \ +`. Consequences:
   - The pattern must match the **entire URL** (anchored both ends). `http://example.com` does NOT match
     `http://example.com/` or `http://example.com/x`; add a trailing `*`.
   - Each `*` is a capture group `$1..$n`, lazy (`.*?`) but anchored, so it backtracks to fit.
   - `|` is **not** escaped, so a literal `|` in a wildcard pattern becomes regex alternation. Use a regex rule.
   - There is no way to say "one path segment only" in a wildcard (`*` crosses `/`); use an exclude pattern
     (the help page's "different folder" example) or a regex.
2. **Regex (`R`)**: used as-is, JavaScript syntax, flags `gi` (**always case-insensitive**, no way to turn
   that off). **Not anchored**: without `^` it can match mid-URL. Put `^` at the start, and `$` if the rule
   must match the whole URL. Escape `?` and `.` (`\?`, `\.`); an unescaped `?` in a query string is the
   classic mistake.
3. **Exclude pattern**: tested against the original URL with the same type rules. A match means "never
   redirect". It is only evaluated after the include matched.
4. **Redirect to** is a *template*, not a substitution into the original URL. Everything not captured is
   dropped. To keep the rest of the URL, capture it (`(.*)`) and put `$N` in the template.
5. **`$N` substitution**: runs from the highest group down (so `$10` is safe), case-insensitive, unmatched
   optional groups become empty string. `$0` is NOT supported. A literal `$1` in the target cannot be
   written. Captures containing `$&`, `$'`, `` $` `` get JS replacement-pattern treatment (rare).
6. **Process matches** is applied to **every** capture before substitution (cannot target one group):
   - `urlDecode` / `doubleUrlDecode` use JS `unescape()`, not `decodeURIComponent`: multi-byte UTF-8 such as
     `%C3%A9` comes out as mojibake. ASCII-only payloads are fine.
   - `urlEncode` uses `encodeURIComponent`.
   - `base64decode` runs `atob`; invalid base64 throws (the rule errors for that request). If the capture
     contains `%` it is `unescape`d first.

## Which requests are considered

- **Only `GET`.** POST etc. are never redirected.
- **Only `http://` and `https://` URLs** (`urls: ["https://*/*", "http://*/*"]`). `file:`, `about:`, `ftp:`,
  `moz-extension:` are never seen.
- **Rule order = priority; first match wins.** Rules are checked in list order, per request type.
  Imported rules are appended to the END of the list. Reorder in the UI if a new rule must beat an old one.
- **Request types are separate.** A rule only runs for the types in its `appliesTo`. Default is address-bar
  navigations only. Add `sub_frame`/`xmlhttprequest`/`script`/etc. only when the user truly wants them
  (every matching sub-request is checked: performance cost).
- **No chains, no loops.** The URL a rule redirects *to* is never redirected again (a one-shot ignore), and a
  URL redirected 3+ times within 3 s is ignored. So `a -> b` plus `b -> c` does NOT give `a -> c`. Write
  `a -> c` directly. This also means a redirect whose target matches its own include pattern is harmless
  (e.g. http->https with `http*`... still prefer a pattern that cannot match the target).
- **`history` (HistoryState)**: for single-page apps that change the URL with `pushState` (YouTube,
  Twitter, Facebook) without a real navigation. The extension registers a `webNavigation.onHistoryStateUpdated`
  listener whose filter uses the include pattern as `urlMatches`; the WebExtension spec defines `urlMatches`
  as RE2, so **lookahead/lookbehind do not work in `history` rules**. The tab is then navigated with
  `tabs.update`. Usually paired with `main_frame` in the same rule (README's YouTube Shorts example).

## Import / export file

`importexport.js` accepts JSON with a top-level `"redirects"` array; nothing else is required:

```json
{
    "createdBy": "Redirector v3.5.4",
    "createdAt": "2026-01-01T00:00:00.000Z",
    "redirects": [ { "description": "...", "exampleUrl": "...", "exampleResult": "...", "error": null,
        "includePattern": "...", "excludePattern": "", "patternDesc": "", "redirectUrl": "...",
        "patternType": "R", "processMatches": "noProcessing", "disabled": false, "grouped": false,
        "appliesTo": ["main_frame"] } ]
}
```

- Missing fields fall back to defaults (`patternType` -> `W`, `appliesTo` -> `["main_frame"]`, etc.).
- Duplicates are skipped by comparing description, exampleUrl, both patterns, patternDesc, redirectUrl,
  patternType, processMatches and `appliesTo` (order-sensitive). Re-importing the same file is harmless; a
  one-character change imports as a new rule next to the old one.
- Invalid rules are still imported (they just carry an `error`); validate before shipping.
- Import: extension **Edit Redirects** page -> **Import** (file picker). Export is on the same page.

## Other facts worth knowing

- Storage: Local by default (about 5 MB). Optional Sync storage allows only 8192 bytes for all rules; the
  save fails with a quota message beyond that.
- Settings page has an optional "notification on redirect" and logging toggle, useful when a rule
  "doesn't fire".
- The toolbar badge shows `on`/`off`; a globally disabled extension redirects nothing.
- v3.5.4 is a Manifest V2 extension. Do not promise Chrome behavior beyond what the code shows; the
  maintainer's help text only verifies Firefox for `imageset`.
