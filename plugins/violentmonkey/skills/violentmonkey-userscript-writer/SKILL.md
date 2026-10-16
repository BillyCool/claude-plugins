---
name: violentmonkey-userscript-writer
description: >-
  Write correct, minimal Violentmonkey userscripts. Use when the user wants to
  automate/modify page behavior via a userscript, patch a site's own JS
  globals, add a persistent UI element, store settings across sessions, make
  cross-origin requests from a page, or otherwise create/debug a
  `.user.js` file for Violentmonkey. Favors the real GM_/GM.* API and the
  official `@violentmonkey/*` libraries over hand-rolled equivalents.
---

# Violentmonkey userscript writer

Turn a user's intent into a correct, minimal Violentmonkey userscript, grounded
in the real GM API and Violentmonkey's own source behavior — not folklore
copied from other userscript managers or old templates. No maintainer skill
exists for this one; if Violentmonkey's API surface changes, re-derive from
source (`references/sources.md` lists exactly what was checked and how).

## Core rule: no outer IIFE wrapper

**Never wrap the script body in `(function () { 'use strict'; ... })();`.**

This isn't a style preference — it's wrong for two concrete, source-confirmed
reasons (see `references/sandbox-and-injection.md` for the exact code):

1. **Violentmonkey already does it.** Every script is auto-wrapped in its own
   IIFE (and a try/catch on Firefox for console error visibility) at inject
   time, unless the script opts out with `@unwrap`. A hand-added wrapper is a
   redundant *second* layer, not a safety net.
2. **It breaks the common patching pattern.** Top-level `function` and `var`
   declarations in a script are real global bindings — either directly on the
   page's `window` (`@grant none`) or reachable via `unsafeWindow` (any other
   `@grant`). Wrapping them in your own IIFE traps them in a closure instead,
   so inline `onclick="theFunction()"` handlers and site code can no longer
   see or call them. This is the exact mechanism used to patch a site's own
   JS globals (`references/patterns.md` → "Patch a page's own function").

Write scripts as flat top-level code: `function foo() {}`, `var state = ...`,
directly in the file, no wrapper, no `'use strict'` pragma (redundant — see
the same reference for why).

## 1. Classify the intent first

| The user wants to… | Reach for | Reference |
|---|---|---|
| Store/read settings, sync across tabs | `GM_setValue`/`GM_getValue`/`GM_addValueChangeListener` | `references/gm-api.md` § Storage |
| Make a cross-origin request, download a file | `GM_xmlhttpRequest` / `GM_download` | `references/gm-api.md` § Network |
| Copy to clipboard | `GM_setClipboard` (sync, no focus/permission issues — prefer over `navigator.clipboard`) | `references/gm-api.md` § DOM & UI |
| Read/write cookies | `GM_cookie.list/set/delete` (undocumented on the API page, confirmed from source) | `references/gm-api.md` § Cookies |
| Add a menu command / hotkey | `GM_registerMenuCommand` / `@violentmonkey/shortcut` | `references/gm-api.md`, `references/official-libraries.md` |
| Show a toast / floating panel | `@violentmonkey/ui` (`VM.showToast`, `VM.getPanel`) — don't hand-roll a `<div>` overlay | `references/official-libraries.md` |
| Wait for an element to appear (SPA, lazy render) | `@violentmonkey/dom`'s `VM.observe`, or a raw `MutationObserver` for persistent watching | `references/patterns.md` § Waiting for elements |
| Reach a site's own JS functions/variables | Depends on `@grant`: direct `window` access (`@grant none`) or `unsafeWindow` (sandboxed) | `references/sandbox-and-injection.md` |
| Bypass strict CSP that blocks the script | `@inject-into content` (or leave `auto`, the default) | `references/sandbox-and-injection.md` |

## 2. Ground the script in the real page — don't guess

Before writing selectors, function names, or globals to patch: read the
site's actual DOM/JS (`javascript_tool`, `read_page`, `read_network_requests`
if a browser is open). Never invent a global function name or CSS selector —
confirm it exists in the live page or in code the user already pasted.

## 3. Pick the metadata block deliberately

- `@match` over `@include` — stricter, safer (`references/metadata-block.md`).
- `@grant none` when the script only touches the DOM/page JS and needs zero
  GM_ APIs — simplest, unsandboxed, direct `window` access.
- Any specific `@grant` (e.g. `GM_setClipboard`) switches the script into
  Violentmonkey's **sandbox**: `window` is no longer the page's real window.
  Add `@grant unsafeWindow` explicitly whenever the script also needs to touch
  page globals, and use `unsafeWindow.foo`, not `window.foo`, for those.
- Reach for `@require` + an official `@violentmonkey/*` library before
  hand-rolling something the library already does simply (DOM waiting, toasts,
  panels, shortcuts) — see `references/official-libraries.md` for exact
  `@require` URLs and version-pinning.
- `@run-at` only when timing actually matters (default `document-end` is fine
  for most DOM-patching scripts; `document-start` for early hooks).

## 4. Write, then sanity-check

- Every `GM_*` call needs its matching `@grant` line, or it's `undefined` at
  runtime — cross-check against `references/gm-api.md`'s exact grant name per
  function (not all follow the obvious pattern, e.g. `GM.xmlHttpRequest` vs
  `GM_xmlhttpRequest`).
- If the script patches a function the site calls via an inline
  `onclick="..."` attribute or another of its own `<script>` tags, confirm
  *where* that identifier resolves (real page global vs. this script's own
  scope) before deciding whether to assign to `window.foo` or
  `unsafeWindow.foo`. Getting this backwards is the single most common
  Violentmonkey bug — the patch silently does nothing because the site never
  sees it.
- If the target element can appear more than once (re-renders, pagination,
  SPA navigation), don't patch it once — use `VM.observe` or a persistent
  `MutationObserver`, matching the site's actual re-render behavior instead of
  a one-shot `querySelector`.
- Adaptive explanation: a terse request from someone who clearly knows
  Violentmonkey gets the script + a one-line why. A learner gets the script
  plus *why this `@grant`*, *why this injection approach*, and what would
  silently break if patched the other way.

## Guardrails

- `@connect` is accepted as metadata but — per source inspection — Violentmonkey
  does not gate `GM_xmlhttpRequest`/`GM_download` by a per-request `@connect`
  allowlist the way Tampermonkey does. Don't tell users it restricts anything at
  runtime in Violentmonkey; it's compatibility/documentation metadata only.
- `GM_xmlhttpRequest`'s `headers` option cannot set browser-forbidden headers
  (`Cookie`, `Origin`, `Referer`, `Host`, `Connection`, `Content-Length`, any
  `Proxy-*`/`Sec-*` header, etc. — full list in `references/gm-api.md`). Don't
  promise a script can override these.
- Don't fabricate a `@violentmonkey/*` library API from memory — every
  function documented in `references/official-libraries.md` was pulled from
  the actual published bundle on jsDelivr, not the README prose. If asked for
  something not listed there, say so and fall back to plain DOM/GM APIs.
- Sandboxed scripts (`@grant` other than `none`) that need to expose a
  function for the page to call back into (e.g. a callback passed through
  `postMessage`) must assign it on `unsafeWindow`, not `window` — `window`
  inside a sandboxed script is a distinct object from what the page sees.
- State plainly when a request is genuinely better served by a browser
  extension the user already has, or when the site's own CSP will block
  `@inject-into page` — don't force page-mode injection where content-mode
  (the default `auto` already handles this) is clearly required.

## Reference index

Every reference file below is grounded in Violentmonkey's actual source
(`violentmonkey/violentmonkey` on GitHub) and the official `@violentmonkey/*`
library bundles, not just the docs site's prose — see `references/sources.md`
for exactly what was pulled and from where.

- `references/metadata-block.md` — every metadata directive, its type
  (single/array/boolean), locale suffix, `@resource`'s special `name URL`
  merge behavior, unknown-key fallback.
- `references/gm-api.md` — every `GM_*`/`GM.*` function, its exact `@grant`
  name, full parameter list (incl. the complete `GM_xmlhttpRequest`/
  `GM_download` option keys and the forbidden-header list), sync vs. async
  form.
- `references/sandbox-and-injection.md` — `@grant none` vs. sandboxed,
  `unsafeWindow`, `@inject-into` page/content/auto, the Firefox
  `exportFunction`/`cloneInto`/`wrappedJSObject` bridge, and the source proof
  for the no-wrapper rule.
- `references/official-libraries.md` — `@violentmonkey/dom` (`VM.observe`,
  `VM.h`/`m`/`hm`, `getElementsByXPath`, `getTextValues`), `@violentmonkey/ui`
  (`VM.showToast`, `VM.getPanel`, `Movable`), `@violentmonkey/shortcut`
  (`register`, `KeyboardService`, key syntax), `@violentmonkey/types`; exact
  `@require` CDN URLs, version pinning, the jsDelivr combine trick.
- `references/patterns.md` — recipes: waiting for dynamic elements, patching
  a page's own function/global, persistent settings with cross-tab sync, SPA
  re-injection, cross-origin fetch, menu commands/hotkeys.
- `references/sources.md` — exact URLs/commits/files this skill's facts were
  pulled from.
