---
name: ublock-origin-skill-maintainer
description: >-
  Keep the `ublock-origin-filter-writer` skill in sync with new uBlock Origin releases.
  Use when the user says a new uBO version shipped, asks to update/refresh/audit
  the uBO filter skill, or wants to check whether its documented syntax is still
  accurate. Fetches live uBO source + wiki, diffs against the skill's reference
  files, and proposes concrete edits.
---

# uBlock Origin skill maintainer

This skill updates the sibling **`ublock-origin-filter-writer`** skill so its syntax
stays true to uBlock Origin. It is **manually invoked** — run it when a new uBO
release lands or when the writer skill's accuracy is in doubt.

Core principle (from the user): **everything the writer skill documents must be
confirmed in live source code. The wiki may be outdated — source wins.** Do not
update reference files from memory or from the wiki alone.

## Workflow

### 1. Establish baseline
Read `../ublock-origin-filter-writer/references/syntax-version.md` to see which uBO
version the writer skill currently reflects and when it was last synced.

### 2. Find the current release
Get the latest uBO release tag and date from the GitHub API
(`https://api.github.com/repos/gorhill/uBlock/releases/latest`). If it equals the
baseline version, tell the user the skill is already current and stop (unless
they asked for a full re-audit anyway).

### 3. Pull authoritative source
Fetch the live source files listed in `references/sources.md`. Prefer downloading
raw files and grepping them locally over trusting a summarizer — the option and
operator tables must be read exactly. The canonical anchors:

- `src/js/static-filtering-parser.js` → `nodeTypeFromOptionName` (network
  options + aliases), `proceduralOperatorNames` / `maybeProceduralOperatorNames`
  / `actionOperators` / `proceduralActionNames` / `normalizedOperators`
  (procedural), `removableHTTPHeaders` (removable headers).
- `src/js/html-filtering.js` → `operatorToTaskMap`, ignored tags.
- `src/js/httpheader-filtering.js` → response-header filtering behavior.
- `src/js/static-ext-filtering.js` → extended-filter separators.
- `src/js/resources/*.js` → scriptlet registry (`name:` + `aliases:`) and
  redirect resources. Enumerate the directory via the GitHub contents API, then
  grep each file for `name:`/`aliases:`.

### 4. Diff against the skill
Compare what the source defines to what each reference file documents:

| Source anchor | Writer-skill file to reconcile |
|---|---|
| `nodeTypeFromOptionName` | `references/network-filters.md` |
| procedural sets | `references/procedural-cosmetic.md` |
| `removableHTTPHeaders`, `operatorToTaskMap` | `references/html-filtering-firefox.md` |
| extended separators | `references/cosmetic-filters.md` |
| `src/js/resources/*.js` | `references/scriptlets.md` |

Look for: added options/operators/scriptlets, renamed or newly-aliased ones,
removed/deprecated ones, and changed allowed-value lists. **Filter for Firefox
relevance** — the writer skill targets Firefox MV2; note (don't necessarily add)
Chromium/MV3-only changes.

### 5. Propose, then apply
Present a concise diff summary to the user: what changed in uBO, and the exact
edits you'd make to each reference file. On approval:
- Edit the affected reference files.
- Update `references/syntax-version.md`: bump the version, the "Last synced"
  date, refresh "Known deltas from the wiki", and note anything newly Firefox-only.
- Keep the writer skill's tone and structure; change facts, not prose style.

### 6. Report
Summarize what was updated and, if useful, flag any new feature worth teaching in
the writer skill's decision tree (e.g. a new option family).

## Notes

- Read the wiki (`references/sources.md` lists the pages) for human-readable
  descriptions and examples, but **treat every syntactic fact as unconfirmed
  until you see it in source.**
- If source and wiki disagree, source wins and the disagreement goes in
  `syntax-version.md` under "Known deltas from the wiki".
- This skill only edits files under `../ublock-origin-filter-writer/`. It does not
  change filter behavior anywhere else.
