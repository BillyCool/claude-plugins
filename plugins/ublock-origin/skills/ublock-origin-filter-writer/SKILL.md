---
name: ublock-origin-filter-writer
description: >-
  Write correct, minimal uBlock Origin (uBO) filter rules for Firefox. Use when
  the user wants to block a network request, hide or remove a page element,
  inject a scriptlet, strip a response header, or otherwise create/debug a uBO
  "My filters" rule — often while a page is open in the browser ("block this
  element", "block this request", "hide this ad", "why is this rule not
  working"). Reads the live page/HTML/network to pick a stable, safe rule.
---

# uBlock Origin filter writer (Firefox)

Turn a user's intent into the **best** uBO filter rule, grounded in the actual
page, not guesswork. "Best" = correct, as narrow as possible, resilient to
trivial site changes, and low breakage risk.

**Target: Firefox + uBlock Origin (MV2).** This is the full-feature build — every
option below is available. Ignore Chromium/MV3 limitations entirely; they do not
apply here. Syntax in this skill is confirmed against uBO **1.72.2** source (see
`references/syntax-version.md`).

## 0. First, classify the intent

Pick the filter family before writing anything:

| The user wants to… | Family | Reference |
|---|---|---|
| Stop a request from loading (ad script, tracker, beacon, media, iframe) | **Network filter** | `references/network-filters.md` |
| Hide an element that's already in the page | **Cosmetic filter** (`##`) | `references/cosmetic-filters.md` |
| Hide/select by content, relationship, or randomized markup | **Procedural cosmetic** | `references/procedural-cosmetic.md` |
| Change page JS behavior (anti-adblock, timers, `fetch`, properties) | **Scriptlet** (`##+js()`) | `references/scriptlets.md` |
| Remove elements/scripts from the HTML *before* it parses, or strip a response header | **HTML filtering** (`##^`) — Firefox only | `references/html-filtering-firefox.md` |
| Undo an over-blocking filter | **Exception** (`@@`, `#@#`) | network / cosmetic refs |

Prefer a **network filter** over a cosmetic one whenever the thing is its own
request — blocking the load saves bandwidth and can't be re-shown by the site,
whereas cosmetic only hides what already downloaded.

## 1. Inspect the live page — don't guess

When a page is open in the browser, gather ground truth **before** choosing a
selector or pattern. Use the browser tools:

- **Element hiding:** `read_page` (accessibility tree with refs) and/or
  `javascript_tool` to read the target's real `outerHTML`, id, classList,
  attributes, and its ancestor chain. Never invent a class that isn't in the DOM.
- **Network blocking:** `read_network_requests` (optionally with a `urlPattern`)
  to get the *actual* request URL, its host, resource type, and whether it's
  third-party relative to the page. Base the pattern on the real URL.
- **Scriptlet cases:** `read_console_messages` / `read_network_requests` to see
  what the page's script is doing (adblock walls, redirects, timers).

If no browser is open, ask the user to paste the element's HTML or the request
URL — do not fabricate selectors.

## 2. Choose a STABLE, SAFE target

This is where rule quality is won or lost. Full heuristics live in
`references/selector-strategy.md`; the essentials:

- **Scope to the hostname.** Write `example.com##…`, not a global `##…`, unless
  the pattern is deliberately reusable. Scoping prevents collateral breakage on
  other sites.
- **Prefer stable hooks:** semantic `id`, meaningful class names, `data-*`
  attributes, ARIA roles/labels. 
- **Distrust randomized markup.** Classes like `.css-1a2b3c`, `.jss42`,
  `.a7Bx9`, hashed or build-generated names change on every deploy. Don't anchor
  to them. Instead use attribute substring matches (`[class^=…]`, `[data-testid=…]`),
  text (`:has-text()`), or structure (`:has()`, `:upward()`).
- **Avoid brittle structure:** deep `:nth-child()` chains and `>`-heavy paths
  break when the site reorders nodes. Target the element by what it *is*, not
  where it sits.
- **Minimal footprint:** the narrowest pattern that catches the target and
  nothing else. Overly broad rules are the #1 cause of site breakage.

## 3. Write the rule and verify

- Produce the single best rule (offer one clearly-better alternative only if the
  trade-off is real, e.g. network-block vs cosmetic-hide).
- **Adaptive explanation:** match the user's level. A terse request from someone
  who clearly knows uBO gets the rule + a one-line why. A learner gets the rule
  plus *why this family*, *why this selector*, and the breakage risk.
- When possible, verify: after suggesting a cosmetic rule you can test the
  selector in the page via `javascript_tool`
  (`document.querySelectorAll(<selector>).length`) to confirm it matches the
  intended element(s) and nothing more. For network rules, confirm the pattern
  matches the observed request URL and note what else on the host it would catch.
- Tell the user **where it goes**: uBO dashboard → *My filters* (one rule per
  line), then *Apply changes*. Cosmetic/scriptlet/HTML changes may need a reload.

## Guardrails

- **`trusted-*` scriptlets** (and `$replace`, `$permissions`, `$urlskip`,
  `uritransform`) only run from *trusted* sources — the user's own **My filters**
  or a list they've marked trusted. Flag this when you use one; it won't work
  from an untrusted subscribed list.
- Don't reproduce filter-list content wholesale; write the specific rule asked for.
- If a request is dynamic/first-party and can't be safely blocked by URL, say so
  and fall back to cosmetic or scriptlet rather than a fragile network pattern.
- State breakage risk honestly. A rule that hides an ad *and* the article next to
  it is worse than no rule.

## Reference index

Every reference below is exhaustive for its category — confirmed by
downloading and grepping the actual uBO source, not summarized from the wiki.
If the user's request maps to any of these, load the file rather than relying
on general knowledge.

- `references/network-filters.md` — anchors, every option/modifier + aliases, redirect/CSP, exceptions
- `references/cosmetic-filters.md` — `##`, `#@#`, styling, scope, entity/regex hostnames
- `references/procedural-cosmetic.md` — every procedural operator + action operators
- `references/scriptlets.md` — **all 60+ scriptlets** confirmed from `src/js/resources/*.js`, incl. the `json-edit`/`trusted-json-edit-*` family (JSON request/response value editing via `jsonq`), cookie/storage, timers, network interception, navigation/dialogs, anti-fingerprinting. Trust requirements marked per-scriptlet.
- `references/redirect-resources.md` — **all 49 `$redirect=` tokens** confirmed from `src/web_accessible_resources/`
- `references/html-filtering-firefox.md` — `##^`, `##^responseheader()` (Firefox-only), allowed headers
- `references/preparser-directives.md` — `!#if`/`!#else`/`!#endif` conditions, `!#include`, comments
- `references/selector-strategy.md` — stable-selector heuristics and anti-patterns
- `references/syntax-version.md` — uBO version this knowledge reflects + provenance
