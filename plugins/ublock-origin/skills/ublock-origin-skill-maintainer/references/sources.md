# Canonical uBlock Origin sources

Repo: https://github.com/gorhill/uBlock  ·  Wiki:
https://github.com/gorhill/uBlock/wiki  ·  Default branch: `master`.

**Source code is authoritative. The wiki is secondary and may lag.**

## Release / version

- Latest release (API): https://api.github.com/repos/gorhill/uBlock/releases/latest
  → `tag_name`, `published_at`.
- Releases page: https://github.com/gorhill/uBlock/releases

## Source files (raw)

Raw prefix: `https://raw.githubusercontent.com/gorhill/uBlock/master/`

| Path | Confirms |
|---|---|
| `src/js/static-filtering-parser.js` | Network options (`nodeTypeFromOptionName`); procedural operators (`proceduralOperatorNames`, `maybeProceduralOperatorNames`, `actionOperators`, `proceduralActionNames`, `normalizedOperators`); removable headers (`removableHTTPHeaders`) |
| `src/js/html-filtering.js` | HTML-filtering operators (`operatorToTaskMap`), ignored tags |
| `src/js/httpheader-filtering.js` | Response-header filtering engine |
| `src/js/static-ext-filtering.js` | Extended-filter separators (`##`, `#@#`, `##+js(`, `##^`, …) |
| `src/js/static-net-filtering.js` | Network filter matching/compilation (option semantics) |
| `src/js/resources/` (directory) | Scriptlet + redirect registry |

Enumerate the resources directory:
`https://api.github.com/repos/gorhill/uBlock/contents/src/js/resources`
then fetch each `*.js` and grep for `name:` and `aliases:`.

## Wiki pages (human-readable, verify against source)

- Static filter syntax: https://github.com/gorhill/uBlock/wiki/Static-filter-syntax
- Procedural cosmetic filters: https://github.com/gorhill/uBlock/wiki/Procedural-cosmetic-filters
- Resources Library (scriptlets/redirects): https://github.com/gorhill/uBlock/wiki/Resources-Library
- HTML filtering / capabilities: search the wiki for "cap_html_filtering"

## Method note

The parser/registry tables are large; a web-summarizer will drop entries.
Download raw files and grep them locally for the exact `Map`/`Set`/`name:`
definitions rather than relying on a summarized fetch.
