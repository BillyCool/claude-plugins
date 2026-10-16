---
name: mudblazor-skill-maintainer
description: >-
  Keep the `mudblazor-ui-writer` skill in sync with new MudBlazor releases. Use
  when the user says a new MudBlazor version shipped, asks to update/refresh/
  audit the MudBlazor skill, or wants to check whether its documented API is
  still accurate. Clones the tagged MudBlazor source, re-runs the API
  extraction script, diffs against the writer's reference files, and applies
  concrete edits.
---

# MudBlazor skill maintainer

This skill updates the sibling **`mudblazor-ui-writer`** skill so its API
knowledge stays true to MudBlazor. It is **manually invoked** — run it when a
new MudBlazor release lands or when the writer skill's accuracy is in doubt.

Core principle: **everything the writer skill documents must be confirmed in
the tagged source code.** Do not update reference files from memory, release
notes, or the website docs alone — those describe changes; the source defines
them.

## Workflow

### 1. Establish baseline
Read `../mudblazor-ui-writer/references/version.md` for the version currently
reflected and the last sync date.

### 2. Find the current release
`https://api.github.com/repos/MudBlazor/MudBlazor/releases/latest` →
`tag_name`, `published_at`. If it equals the baseline, tell the user the skill
is already current and stop (unless they asked for a full re-audit).

### 3. Clone the tagged source
```
git clone --depth 1 --branch <tag> https://github.com/MudBlazor/MudBlazor.git <scratchpad>/mudblazor
```
Always clone the **release tag**, not `dev` — the writer documents released
behavior. Work in the scratchpad directory.

### 4. Regenerate the mechanical references
```
python scripts/extract_api.py <scratchpad>/mudblazor ../mudblazor-ui-writer
```
This rewrites `references/api/*.md`, `components-index.md`, and `enums.md`
in the writer skill directly. Then `git diff` the writer skill to see exactly
what changed in the component API surface (new/removed components, parameters,
defaults, enum values).

Sanity-check the extraction before trusting the diff (the script is
regex-based and a new code style could break it):
- component/enum counts printed by the script vs. the previous run
  (recorded in `version.md`);
- spot-check one changed file against its source `.razor.cs`;
- captured-parameter count roughly matches
  `grep -r "\[Parameter\]" src/MudBlazor/{Components,Base} | wc -l`.
If the script mis-parses something, fix `scripts/extract_api.py` (it is part
of this skill) and re-run.

### 5. Re-verify the hand-written references
`../mudblazor-ui-writer/references/version.md` maps each hand-written file to
its source anchors (theme model defaults, SCSS utility maps, service
interfaces, install snippets). For each anchor, grep the fresh clone and
reconcile — `references/sources.md` in this skill lists the same anchors with
what to look for. Also read the GitHub release notes for the versions between
baseline and current: breaking changes, renames, and deprecations called out
there must each be traced to source and reflected in the writer's prose
(especially the version-honesty guidance in its SKILL.md).

### 6. Propose, then apply
Present a concise summary: what changed in MudBlazor between the two versions,
and which writer files were / will be edited. On approval (or if invoked with
a standing instruction to just update):
- Keep the regenerated `api/`, `enums.md`, `components-index.md` output.
- Edit the affected hand-written files — change facts, not prose style.
- Update `version.md`: version, release date, sync date, new extraction
  counts, and any new caveats.
- Bump the version number in the writer's SKILL.md description and body.

### 7. Report
Summarize what was updated. Flag anything worth teaching in the writer's
guidance sections (a new component family, a renamed core concept, a new
required provider) — parameter tables update themselves; guidance does not.

## Notes

- Source wins over docs site, release notes, and memory. If they disagree,
  note the discrepancy in `version.md`.
- This skill only edits files under `../mudblazor-ui-writer/` and its own
  `scripts/`/`references/`. It does not touch user projects.
- Delete the scratchpad clone when done.
