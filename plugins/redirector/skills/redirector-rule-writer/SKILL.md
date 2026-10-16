---
name: redirector-rule-writer
description: >-
  Write correct Redirector browser-extension rules (the einaregilsson/Redirector
  add-on for Firefox/Chrome: "Create Redirect" with Include pattern, Exclude
  pattern, Redirect to, Wildcard/Regular Expression, Process matches, Apply to).
  Use when the user wants to redirect one URL or a family of URLs to another
  (de-AMP, old.reddit, http->https, strip tracking wrappers, search-engine
  bangs, swap a domain), or asks for a Redirector rule, pattern, regex or
  import file. Interviews the user for URL, target and constraints, tests the
  rule against a port of the extension's engine, and outputs either a
  copy-paste field sheet or an importable JSON file.
---

# Redirector rule writer

Turn "when I open X, send me to Y" into the **simplest rule that is correct**, proven against the real
matching semantics, and deliver it in the form the user wants. Knowledge is sourced from Redirector v3.5.4
code and docs (`references/engine-semantics.md`), not from memory. Read it before writing any non-trivial
rule; the engine has sharp edges (anchored wildcards, always-case-insensitive regex, `base64decode` casing,
no chaining, first match wins).

## Step 1: Intake (ask only for what is missing)

Infer from the request first. If the user gave a URL and a goal, do **not** re-ask. Gather these, in this order,
as one compact question set (use AskUserQuestion when the harness offers it, otherwise a short list):

1. **From**: one real example URL that should be redirected (required: the extension itself demands an
   Example URL). Ask for 1 to 3 if the family varies (subdomains, with/without query).
2. **To**: the destination, or the transformation ("same URL but old.reddit.com", "the url= parameter").
3. **Constraints** (offer these as optional prompts, don't interrogate):
   - *Only apply to* a host, path, or scheme?
   - *Never apply to* some path/host/parameter (becomes the **Exclude pattern**)?
   - Should it also affect embeds/iframes/Ajax/images (**Apply to**; default is address bar only)?
   - Is the site a single-page app that changes URL without reloading (needs `history`)?
4. **Output** (ask once, at the end of intake, unless already stated):
   - **Field sheet**: every field exactly as in the "Create Redirect" form, to copy-paste, or
   - **Import file**: a `.json` attached to the chat to load via Edit Redirects -> Import, or
   - **Both** (recommended when there are 2+ rules or the user will keep them).

If the user cannot give a negative example, propose one yourself ("should
`https://example.com/foo?next=...` also redirect?") and test it.

## Step 2: Design

- Prefer a **wildcard** rule wherever possible: it is simpler to read, write and edit in the UI. Reserve
  **regex** for the more complex tasks that wildcard cannot express, and try a wildcard first even when
  regex looks tempting (e.g. a fixed-shape URL where a trailing `?*` drops the query string). See
  `references/rule-recipes.md` for the decision list and ready recipes.
- Make the rule narrow: anchor regexes with `^`, exclude paths the user named, keep `appliesTo` as
  `["main_frame"]` unless asked otherwise.
- Redirect to is a **template**: capture whatever must survive (`$1`...).
- One rule per intent. If the request needs chaining (`a -> b -> c`) collapse it into direct rules, because
  redirect results are never redirected again.
- If several rules are needed, order matters (first match wins; imports append to the end). Put narrower
  rules above broader ones and say so.

## Step 3: Test before presenting (mandatory)

Write a draft JSON (scratchpad, not the repo) with each rule and a `tests` array of real positive **and
negative** URLs, then run the builder, which is a faithful port of `js/redirect.js`:

```bash
node "<skill-dir>/scripts/build-rules.mjs" draft.json --out redirector-rules.json
```

Draft shape (all fields optional except `exampleUrl`, `includePattern`, `redirectUrl`; defaults match the
extension):

```json
[{
  "description": "Old Reddit",
  "exampleUrl": "https://www.reddit.com/r/linux/comments/abc/title/",
  "includePattern": "https://www.reddit.com/*",
  "excludePattern": "https://www.reddit.com/gallery/*",
  "redirectUrl": "https://old.reddit.com/$1",
  "patternType": "W",
  "processMatches": "noProcessing",
  "appliesTo": ["main_frame"],
  "tests": [
    { "url": "https://www.reddit.com/r/foo/", "expect": "https://old.reddit.com/r/foo/" },
    { "url": "https://www.reddit.com/gallery/x", "expect": null }
  ]
}]
```

`<skill-dir>` is the directory containing this SKILL.md. The script exits non-zero on any failure, writes the
import file only if everything passes, and prints lint warnings (unanchored regex, `$N` beyond the groups,
`|` in wildcards, URL-decode mojibake, RE2 limits for `history`, shadowing by an earlier rule). Fix or consciously
accept every warning. If Node is unavailable, hand-check the example URL and say the rule is untested.

## Step 4: Deliver

**Field sheet.** Use this block per rule (same order and labels as the form), so they
copy cleanly. Leave out "Exclude pattern" and "Process matches" when empty/default, but always state
**Apply to** (it is a checkbox list):

```
Description:       …
Example URL:       …
Include pattern:   …
Redirect to:       …
Pattern type:      Wildcard | Regular Expression
Pattern Description: … (optional)
Example result:    … (must match what the form shows; this is the tested result)
Advanced options -> Show advanced options…
  Exclude pattern: …
  Process matches: No Processing | URL Encode | URL Decode | Double URL Decode | Base64 Decode
  Apply to:        [x] Main window (address bar)   [ ] IFrames … (tick only what is needed)
```

**Import file.** Never leave it in the working directory (it is usually a git repo and the file would be
easy to commit by accident). Write draft and `--out` file in the scratchpad directory, then attach it to
the chat with SendUserFile (`display: "attach"`). Only write it elsewhere if the user names a path. Then tell them: *Redirector toolbar icon -> Edit Redirects -> Import -> choose the file.*
New rules land at the **end** of the list (lowest priority); duplicates of existing rules are ignored. Offer
to produce both outputs from the same tested draft; never hand-write the JSON separately from the tested one.

Always finish with a **3-line summary**: what it matches, what it deliberately does not (excludes), and any
caveat (ordering, SPA/`history`, GET-only, case-insensitivity).

## Guardrails

- Never present a rule that was not run through the builder (or hand-verified and labeled untested).
- Don't invent engine features: no `$0`, no case-sensitive matching, no per-group processing, no chaining,
  no POST redirects, no non-http(s) schemes.
- `processMatches` value for Base64 is `base64decode` (lowercase d) in files; the UI label is "Base64 Decode".
- Redirecting main-window navigation can lock the user out of a page; for broad patterns (whole domains)
  recommend adding an exclude for login/auth paths if the example suggests there are any, and mention the
  extension's toolbar toggle as the escape hatch.
- Don't reproduce the help docs; give the rule and the minimum reasoning. Match the user's level: terse
  for someone who writes regex, one extra line of "why wildcard / why exclude" for a newcomer.

## References

- `references/engine-semantics.md`: rule fields, exact wildcard-to-regex conversion, `$N` substitution,
  process-matches behavior, request types, GET-only, ordering, no-chaining, `history`, import/export format.
- `references/rule-recipes.md`: wildcard-vs-regex guidance, the official examples, common request patterns,
  anti-patterns.
- `scripts/build-rules.mjs`: validator, tester and exporter (port of the extension's matching engine).
