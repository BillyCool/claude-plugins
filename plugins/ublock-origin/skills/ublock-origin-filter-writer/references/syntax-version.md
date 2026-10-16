# Syntax provenance

This skill's syntax is confirmed against live uBlock Origin source, not memory.

- **uBO version reflected:** 1.74.0 (released 2026-08-25)
- **Last synced:** 2026-08-26 (delta pass against 1.73.0 — see "What changed in 1.74.0" below)
- **Target platform:** Firefox + uBlock Origin (MV2). Full-feature build.
- **Synced by:** `ublock-origin-skill-maintainer` skill.
- **Coverage:** every category valid in the My Filters tab is documented:
  network filters, cosmetic filters, procedural cosmetic, HTML filtering,
  60+ scriptlets, all 50 redirect resources, preparser directives.

## Sources confirmed against (branch: `master`)

| Fact | Source file |
|---|---|
| Network option tokens + aliases | `src/js/static-filtering-parser.js` (`nodeTypeFromOptionName`) |
| Procedural operators, actions, aliases | `src/js/static-filtering-parser.js` (`proceduralOperatorNames`, `maybeProceduralOperatorNames`, `actionOperators`, `proceduralActionNames`, `normalizedOperators`) |
| Removable response headers | `src/js/static-filtering-parser.js` (`removableHTTPHeaders`) |
| Preparser `!#if` tokens | `src/js/static-filtering-parser.js` (`preparserIfTokens`) |
| HTML-filtering operators / ignored tags | `src/js/html-filtering.js` (`operatorToTaskMap`, `ignoreTags`) |
| Response-header filtering engine | `src/js/httpheader-filtering.js` |
| Extended-filter separators | `src/js/static-ext-filtering.js` |
| **Every** scriptlet name/alias/trust flag | all 31 files in `src/js/resources/*.js` (downloaded + grepped for `registerScriptlet`/`builtinScriptlets.push` blocks — directory listing confirmed complete via GitHub contents API) |
| `jsonq` (uBO-flavored JSONPath) syntax | `src/js/jsonpath.js` |
| Every redirect resource token | `src/web_accessible_resources/` (directory listing via GitHub contents API — 50 files) |

## What changed in 1.74.0 (vs 1.73.0)

Confirmed via `git compare 1.73.0...1.74.0` (75 commits) plus direct source
diffs of every touched file under `src/js/`. Network option tokens/aliases and
removable response headers are unchanged — no changes to `network-filters.md`
were needed.

Reflected in the writer skill:
- **New procedural operator `:content(sel)`** (`src/js/contentscript-extra.js`,
  `src/js/html-filtering.js`, and recognized in
  `static-filtering-parser.js`'s `proceduralOperatorTokens`) — pierces into a
  `<template>` element's inert `.content` fragment to continue selecting with
  `sel`, analogous to `:shadow()` but for template content. Unusually, it's
  usable in **both** cosmetic (`##`) and HTML filtering (`##^`) — added to
  `procedural-cosmetic.md` and `html-filtering-firefox.md`.
- **New preparser token `env_brave`** (`preparserIfTokens`) — added to
  `preparser-directives.md`.
- **New redirect resource** `google-ima-dai.js` (alias `google-ima3-dai`,
  `src/js/redirect-resources.js`) — added to `redirect-resources.md`; resource
  count bumped 49 → 50.
- **`json-edit` / `trusted-json-edit`** gained an optional `matches, pattern`
  vararg to conditionally apply based on the inbound JSON string, matching the
  shape already used by the other `json-edit` family members. Confirmed in
  `src/js/resources/json-edit.js`.
- **Fixed a pre-existing inaccuracy**: `prevent-clipboard-write`'s doc row
  described a `cssSelector|message` domAlert format that never matched source
  (its true syntax, a vararg `domAlert, message` pair, was already true in
  1.73.0 — this was an error carried from an earlier, less rigorous sync).
  1.74.0 also added an `${text}` interpolation placeholder, `\n` escape
  support, and a `selectable` vararg to the alert; all now documented in
  `scriptlets.md`.
- Internal-only, no doc change: most `src/js/resources/*.js` scriptlets moved
  from a hand-rolled `getExtraArgs()` vararg parser to a shared
  `safe.parseVarargs()` — same `key:value` argument syntax for filter authors,
  purely an implementation refactor. `:remove()`'s internal
  "usable in HTML filtering" bit flipped in `proceduralOperatorTokens`, but it
  still does not appear in `html-filtering.js`'s `operatorToTaskMap`, so it
  remains cosmetic-only in practice — no doc change.

## What changed in 1.73.0 (vs 1.72.2)

Confirmed via `git compare 1.72.2...1.73.0` (93 commits) plus direct source
diffs of every touched file under `src/js/`. Network options, procedural
operators/actions, removable headers, preparser tokens, HTML-filtering
operators, and extended-filter separators are **byte-identical** between the
two tags — no changes to `network-filters.md`, `procedural-cosmetic.md`,
`html-filtering-firefox.md`, `cosmetic-filters.md`, or `preparser-directives.md`
were needed.

Scriptlet-affecting changes, all reflected in `scriptlets.md`:
- **New scriptlet** `proxy-apply-config.js` (`src/js/resources/proxy-apply.js`) —
  takes a JSON `config` object merged into the `proxy-apply.fn` helper's
  internal config; registered with execution priority 100 so it runs before
  other scriptlets.
- **`trusted-click-element`** gained a documented `steps` syntax: the list can
  be separated by `;` or `\|` instead of `,` (prefix the whole arg), for
  selectors that themselves contain a comma. Confirmed in
  `src/js/resources/scriptlets.js`.
- Internal reorg only (no doc changes needed): `abort-current-script.js`,
  `prevent-clipboard-write.js`, and `prevent-bab.js` were split out of the
  monolithic `scriptlets.js` into their own files under `src/js/resources/`;
  names/aliases unchanged. `prevent-bab.js`'s underlying file moved from
  `src/web_accessible_resources/nobab.js` — it was never a documented
  `$redirect=` target (correctly so: it's absent from `redirect-resources.js`'s
  registry in both versions), so `redirect-resources.md` needed no change.
- **New redirect resource** `piano-analytics.js` (`src/js/redirect-resources.js`)
  — already listed in `redirect-resources.md` from a prior sync (turns out the
  physical file didn't exist in 1.72.2 at all — a pre-1.73.0 documentation
  inaccuracy that is now correct as of this release). Net web-accessible-resource
  count stayed at 49 (nobab.js left the directory, piano-analytics.js entered).
- Internal engine change (not exposed as filter syntax): scriptlets now support
  an internal `priority` field controlling injection order
  (`src/js/scriptlet-filtering-core.js`); there is no `+js()` argument to set
  this yourself, so nothing to document for filter authors.

## Known deltas from the wiki at sync time

- Source exposes a `:shadow()` procedural operator not prominent on the wiki
  Procedural-cosmetic page.
- `requestheader` exists in the option table alongside `responseheader`
  (aliased as `header`).

## What to re-check on each uBO release

1. New/renamed/removed network options in `nodeTypeFromOptionName`.
2. Changes to `proceduralOperatorNames` / action operators.
3. Changes to `removableHTTPHeaders`.
4. Added/removed/renamed scriptlets and aliases across `src/js/resources/*.js`.
5. New redirect resources.
6. Any Firefox-relevant capability changes.
