# Sources

This skill has no dedicated maintainer companion skill (unlike
`ublock-origin-filter-writer` → `ublock-origin-skill-maintainer`). If Violentmonkey's API
changes, re-derive facts the same way this file was built: **download and
grep the actual source, don't trust doc-page summaries alone.** The docs site
is auto-generated from an Astro build with no plain-markdown source in the
`violentmonkey.github.io` repo, so it must be fetched as rendered pages.

## Last synced

2026-07-18, against `violentmonkey/violentmonkey` `master` branch (commit not
pinned — re-fetch `master` tip when refreshing) and the following library
versions: `@violentmonkey/dom@2.2.1`, `@violentmonkey/ui@0.7.9`,
`@violentmonkey/shortcut@1.4.4`, `@violentmonkey/types@0.3.3`.

## Primary source files pulled (main repo)

| File | What it grounds |
|---|---|
| `src/common/consts.js` | `GM_API_NAMES` (the exhaustive `@grant` list), `RUN_AT_RE`, `UNWRAP`/`TL_AWAIT` constants |
| `src/background/utils/script.js` | `parseMeta`, `metaTypes`/`metaOptionalTypes` (which metadata keys are array/boolean/single) |
| `src/background/utils/preinject-prepare.js` | Auto-IIFE-wrapping behavior (`wrap`/`wrapTryCatch`/`startIIFE`), the source proof for the no-manual-wrapper rule |
| `src/injected/web/gm-api.js` | Every `GM_*` function body, `GM_API_CTX`/`GM_API_CTX_GM4ASYNC`/`GM_API` grouping, `gmCookieInvoker` (undocumented `GM_cookie`) |
| `src/injected/web/gm-api-wrapper.js` | How `GM_cookie.list/set/delete` get assembled from `gmCookieInvoker` |
| `src/injected/web/gm-global-wrapper.js` | Sandbox wrapper construction (confirms `window` ≠ page window when sandboxed) |
| `src/injected/web/requests.js` | `GM_xmlhttpRequest`/`GM_download` full option set (`OPTS_TO_PASS`, `OPTS_TO_KEEP`, event names) |
| `src/background/utils/requests-core.js` | `FORBIDDEN_HEADER_RE` — the exact forbidden-header list for `GM_xmlhttpRequest`'s `headers` option |
| `src/background/utils/requests.js` | `GM_download`'s two save paths (`dlInApi` branch selection), the `Blob`→`leaseBlobUrl` conversion applied before either path runs |
| `src/background/utils/download-via-api.js` | The "Use browser download API" path — real `browser.downloads.download()` call, confirms `filename` is passed through un-sanitized (subfolder support) |
| `src/injected/content/requests.js` | The default/fallback save path — `download(blob, name)`'s `createObjectURL` + `<a download>` + synthetic click, confirmed as the thing that can't do subfolders |
| `src/common/options-defaults.js` | `kGmDownloadViaApi` / `gmDownloadViaApi` — the option key behind "Use browser download API", default `false` |

Fetched via `https://raw.githubusercontent.com/violentmonkey/violentmonkey/master/<path>`. The
`GM_download` two-path/subfolder/Blob-url findings were added 2026-09-20,
prompted by a real user hitting the content-script fallback's silent-failure
mode on Mullvad Browser (Tor-Browser-derived) — downloads reported success
but never appeared on disk until "Use browser download API" was enabled.

**Correction #1, same day, same user:** the source-grounded claim that
`GM_download`'s `url` reliably accepts a raw `Blob` (via `leaseBlobUrl`) was
put into a real script and did not hold up — posts saved that way failed
consistently in practice, for a reason not fully root-caused (no error
logging was wired up yet, so the failure was silent). Switched to a `data:`
URL built via `FileReader.readAsDataURL`, verified end-to-end with a
fetch-and-compare round-trip in a live browser — that test only proved the
`data:` URL's bytes were readable, not that `GM_download` would accept it,
which is a different thing.

**Correction #2, next session, same user:** the `data:` URL did not fix it
either — this time with real error logging in place, the actual failure
surfaced: `browser.downloads.download()` in Firefox throws `Access denied
for URL data:... for downloads.download`, a hardcoded rejection of `data:`
URLs on that specific API, independent of anything about the script. This is
why the round-trip test in Correction #1 gave false confidence — it verified
the URL's *content* was correct, not that the *destination API* would accept
that URL scheme at all. `gm-api.md` now documents both failure modes
precisely (which is broken, and why) and recommends trying the raw `Blob`
again (the one approach source evidence actually supports, now instrumented
with `onerror` logging to catch anything still wrong with it) with a
guaranteed-safe local-save fallback if `GM_download` reports failure, rather
than leaving the user with a silently-failed download either way.

Lesson for future maintenance: a source-code read explaining *why* something
should work is not a substitute for confirming it actually saves a file in
a real browser — prefer testing over inference wherever a live target is
available. And when a test *does* pass, check exactly what it proved: a
round-trip `fetch()` of a `data:` URL confirms the URL is well-formed, not
that every consumer of URLs (like a specific privileged browser API) will
accept that scheme.

## Docs site pages fetched (rendered HTML, via WebFetch)

- `https://violentmonkey.github.io/api/gm/`
- `https://violentmonkey.github.io/api/metadata-block/`
- `https://violentmonkey.github.io/api/matching/`
- `https://violentmonkey.github.io/guide/observing-dom/`
- `https://violentmonkey.github.io/guide/keyboard-shortcuts/` — confirmed this
  is entirely about the `@violentmonkey/shortcut` library (no separate
  built-in extension-level shortcut API for userscripts); surfaced the
  `VM.shortcut.reprShortcut()` + `GM_registerMenuCommand` labeling pattern in
  `patterns.md`
- `https://violentmonkey.github.io/posts/inject-into-context/`

Used for practical framing (which mode to pick, why) — every hard fact
sourced from these was cross-checked against the main-repo source files
above where the two overlapped; source wins on any conflict (there were none
found this pass).

## Library bundles downloaded and grepped directly

- `https://cdn.jsdelivr.net/npm/@violentmonkey/dom@2.2.1/dist/index.js`
- `https://cdn.jsdelivr.net/npm/@violentmonkey/ui@0.7.9/dist/index.js`
- `https://cdn.jsdelivr.net/npm/@violentmonkey/shortcut@1.4.4/dist/index.js`
- READMEs: `raw.githubusercontent.com/violentmonkey/vm-dom`, `vm-shortcut`,
  `vm-ui` (`master` branch)

Grepped for `exports.*` to get the *actual* exported surface rather than
trusting README prose, which for `@violentmonkey/dom` in particular
undersells the package (its README is framed entirely around JSX/`VM.h`, but
the shipped bundle also exports `observe`, `getElementsByXPath`, and
`getTextValues`, none of which the README mentions).

## Known gaps / things not exhaustively verified

- Whether Violentmonkey applies `'use strict'` to injected code beyond
  whatever the surrounding function-declaration syntax implies was not
  conclusively found in source within the time spent; not asserted either way
  in this skill's reference files. Don't add a manual `'use strict'` pragma
  regardless — it's harmless if redundant, pointless if not, and the no-wrapper
  guidance holds independent of this.
- `GM_cookie`'s `details` shape (per-operation required/optional fields) was
  confirmed to follow the browser `cookies` API convention by code shape, not
  by exhaustively diffing every field against `chrome.cookies`/`browser.cookies`
  docs. Treat field-level specifics as needing a live check if a script's
  correctness hinges on them.
- MV3-specific behavior differences (e.g. `xhrs` Map in `src/offscreen/xhr.js`
  gated on `__.MV3`) were noted in passing but not chased down — this skill
  doesn't currently distinguish MV2/MV3 packaging differences, only the
  userscript-author-facing API surface, which is consistent across both.
