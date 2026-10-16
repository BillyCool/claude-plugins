---
name: aimp-sdk-skill-maintainer
description: >-
  Keep the `aimp-plugin-developer` skill in sync with new AIMP SDK releases.
  Use when the user says a new AIMP SDK dropped, points at an unpacked SDK
  folder, or asks to update/refresh/audit the AIMP skill or check whether its
  documented API is still accurate. Works from an SDK the user supplies — asks
  for the path if none was given, never downloads one. Decompiles that SDK's
  CHM help, re-runs the extraction script, diffs the regenerated references,
  and reconciles the hand-written guides.
---

# AIMP SDK skill maintainer

This skill updates the sibling **`aimp-plugin-developer`** skill so its API
knowledge tracks the shipped SDK. It is **manually invoked** — run it when a
new AIMP SDK lands or when the writer skill's accuracy is in doubt.

Core principle: **everything the writer skill documents comes from the SDK
drop itself** — the CHM help and the `Sources/` tree. Never update a reference
file from memory, from the AIMP forum, or from release notes alone.

## The SDK comes from the user

**The user supplies the SDK. Do not download it.** It ships as a zip from the
vendor behind a download page, and which build the user wants is their call —
this skill never fetches it, and never guesses where a previous copy might be.

If the prompt names a path to an unpacked SDK, use it. **If it does not, stop
and ask for one** before doing anything else; there is nothing useful to do
without it.

An unpacked drop looks like this, and the folder you are given should be the
one containing these:

```
Help/AIMP-en.chm      official API reference (English)
Help/AIMP-ru.chm      the same, Russian
Sources/Cpp/          api*.h, IUnknownImpl.h, testAll.*
Sources/Delphi/       api*.pas, apiConfig.inc, Helpers/, Internal/
Demos/                complete example plugins
*.rtf                 packaging and file-format notes
```

If the folder you were given has no `Sources/` directory, say so and ask for
the right one rather than guessing at a parent or child directory. The script
checks for this too and refuses to run.

## Workflow

### 1. Establish the baseline
Read `../aimp-plugin-developer/references/version.md`: the SDK target it
currently reflects (e.g. `v6.00 build 3000`) and the extraction counts.

### 2. Identify the drop you were given
Take the SDK path from the user's prompt — ask for it if they did not give
one. The authoritative version string is the `Target:` line in the header
comment of every source file:

```bash
head -8 "<sdk>/Sources/Cpp/apiPlugin.h"
```

If it matches the baseline, the SDK has not moved — tell the user and stop,
unless they asked for a full re-audit anyway.

### 3. Regenerate

```bash
python scripts/extract_sdk.py --sdk "<sdk>" --out ../aimp-plugin-developer
```

This decompiles `Help/AIMP-en.chm` with `hh.exe` into a temp directory,
converts every help topic to Markdown, lays the files out along the help file's
own `TOC.hhc`, copies `Sources/` and `Demos/` into
`references/sdk/`, converts the `.rtf` notes, deletes reference files the new
drop no longer produces, and rewrites `references/version.md`.

If `hh.exe` is unavailable, decompile the CHM separately (`7z x AIMP-en.chm`,
or `extract_chmLib`) and pass `--chm-html <dir>`.

The script never touches `references/guides/` — that is the hand-written layer.

### 4. Sanity-check the extraction before trusting the diff
The converters are hand-rolled (`chm2md.py` for the help, `rtf2md.py` for the
notes). A change in how the docs are generated could silently degrade output,
and a smaller diff than expected usually means a parse failure, not a quiet
release. Check:

- the counts the script prints (topics, reference files, vendored sources)
  against the previous run recorded in `version.md` — a large drop is a red
  flag;
- `git diff --stat` on the writer skill: whole files going near-empty, or
  headings collapsing into prose, means the converter broke;
- one changed page read end to end against the same topic opened in the real
  CHM;
- the chapter list in `references/api/` against the help's own "Chapters" node.

If the converter mis-parses something, fix `scripts/chm2md.py` (it is part of
this skill) and re-run. Prefer fixing the converter over hand-patching output —
hand edits are lost on the next regeneration.

### 5. Read the diff for meaning
`git diff` the writer skill and look for:

- **new interfaces** — especially numbered revisions (`IAIMPServiceXxx2`,
  `IAIMPImage4`): these are the version-gated members the writer skill must
  teach people to `QueryInterface` for and fall back from;
- **new or renamed `AIMP_*_PROPID_*` / `AIMP_MSG_*` constants**;
- **new extension points** — a new `IAIMPExtension*` needs a row in
  `references/guides/extension-points.md`, including which service it
  registers with (check the owning service's `Extensions:` line, the demos, and
  the headers — the help does not always say);
- **`Minimal Version` bumps** on existing members;
- **platform notes** — the Windows/Linux table in `concepts.md` grows as the
  Linux port matures;
- **new or changed demos** — `references/guides/extension-points.md` has a
  demo table to keep accurate.

Also skim `references/whats-new.md`, which now carries the SDK's own changelog
for the new version — it names the additions the diff will confirm.

### 6. Reconcile the hand-written guides
`references/guides/` is not regenerated, so it is the part that goes stale.
Re-verify each against the fresh drop:

| Guide | Re-check against |
|---|---|
| `plugin-anatomy.md` | `apiPlugin.h`, `AIMPCustomPlugin.pas`, `apiConfig.inc`, `IUnknownImpl.h`, `concepts.md` (folder layout, Linux table) |
| `idioms.md` | `apiCore.h`, `apiObjects.h`, `apiWrappers.pas` exported helpers, `IAIMPPropertyList*`, `IAIMPServiceThreads` |
| `extension-points.md` | the full `IAIMPExtension*` list in the headers, each owning service's `Extensions:` line, the `Demos/` directory listing |

Useful one-liners for that pass:

```bash
grep -h "^class IAIMPExtension" <sdk>/Sources/Cpp/*.h | sed 's/class //;s/:.*//' | sort
grep -h "^class IAIMPService"   <sdk>/Sources/Cpp/*.h | sed 's/class //;s/:.*//' | sort
```

### 7. Update the writer's front matter
If the SDK version changed, update the version named in
`../aimp-plugin-developer/SKILL.md` (description and body), and add any new
chapter or reference file to its reference map.

### 8. Report
Summarize what moved: SDK version, new/removed interfaces and constants, which
reference files changed, which guides you edited. Flag anything worth teaching
rather than just listing — a new extension family or a changed core convention
matters more than another hundred property rows.

## Scripts

- `scripts/extract_sdk.py` — the whole pipeline; run this.
- `scripts/chm2md.py` — one CHM topic → Markdown. Run standalone on a single
  file to debug conversion (`python chm2md.py <topic.html>`).
- `scripts/rtf2md.py` — the SDK's `.rtf` notes → Markdown. Minimal
  RichEdit-subset reader; the notes are supplementary, so approximate layout in
  its output is acceptable, wrong facts are not.

## Notes

- The CHM ships in English and Russian. The writer skill uses `AIMP-en.chm`
  only; `AIMP-ru.chm` sometimes documents a member the English one misses, so
  it is worth a look when something is conspicuously undocumented — but flag
  anything sourced that way.
- Source headers beat the help text. Where they disagree, follow the headers
  and record the disagreement in `references/version.md`.
- This skill only writes under `../aimp-plugin-developer/` and its own
  `scripts/` and `references/`.
