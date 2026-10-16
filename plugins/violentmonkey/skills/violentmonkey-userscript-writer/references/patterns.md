# Common patterns

Recipes for the situations that come up repeatedly. Each cites which
reference file has the underlying facts.

## Waiting for a dynamic/lazily-rendered element

One-shot (element will appear once, possibly after a delay — SPA hydration,
lazy-loaded widget):

```js
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/dom@2
VM.observe(document.body, () => {
  const el = document.querySelector('.target');
  if (el) {
    doSomethingWith(el);
    return true; // stop observing
  }
});
```

Persistent (element gets removed and re-added repeatedly — list re-renders on
sort/filter, virtualized lists, tab switches):

```js
VM.observe(document.body, () => {
  document.querySelectorAll('.target:not([data-patched])').forEach(el => {
    el.dataset.patched = '1';
    doSomethingWith(el);
  });
  // never return true - keep watching indefinitely
});
```

Mark handled elements (`dataset.patched` above, or any idempotent check) so
repeated mutation batches don't redo work — cheaper than a `WeakSet` for this
case and survives node removal/re-add naturally.

Don't hand-roll a raw `MutationObserver` unless you specifically need
non-default observe options (`attributes`, `characterData`) that `VM.observe`
doesn't expose as conveniently — its `options` third argument still accepts
the full native `MutationObserverInit` shape, so even that's rarely a reason
to skip it.

See `official-libraries.md` § `@violentmonkey/dom` for the exact `VM.observe`
signature and auto-disconnect behavior.

## Patching a page's own function/global

The core question is always: **which realm does the site's own code resolve
this identifier in?** Inline `onclick="foo()"` attributes and other `<script>`
tags on the page always resolve against the page's real global object.

With `@grant none` (unsandboxed — `window` here *is* the page's window):

```js
// @grant none
function tryPatch() {
  if (window.__patched) return true;
  if (typeof window.siteFunction !== 'function') return false;
  const original = window.siteFunction;
  window.siteFunction = function (...args) {
    // ...your behavior...
    return original.apply(this, args);
  };
  window.__patched = true;
  return true;
}
if (!tryPatch()) {
  const iv = setInterval(() => tryPatch() && clearInterval(iv), 250);
  setTimeout(() => clearInterval(iv), 20000);
}
```

With any other `@grant` (sandboxed — `window` is *not* the page's window, use
`unsafeWindow`):

```js
// @grant GM_setClipboard
// @grant unsafeWindow
function tryPatch() {
  if (unsafeWindow.__patched) return true;
  if (typeof unsafeWindow.siteFunction !== 'function') return false;
  unsafeWindow.siteFunction = function (...args) { /* ... */ };
  unsafeWindow.__patched = true;
  return true;
}
```

The retry loop exists because the target function may be defined by a
`<script>` tag that hasn't run yet at `document-idle` in edge cases, or the
page may redefine it later (SPA re-init). If the site is known to define it
synchronously before your script's `@run-at`, the loop is unnecessary — a
single check suffices; don't add polling machinery you don't need.

No manual IIFE around this — see `sandbox-and-injection.md` for why wrapping
would trap `tryPatch`/`iv` and defeat the whole pattern.

## Cross-tab-synced persistent settings

```js
// @grant GM_getValue
// @grant GM_setValue
// @grant GM_addValueChangeListener
let enabled = GM_getValue('enabled', true);
GM_addValueChangeListener('enabled', (key, oldValue, newValue, remote) => {
  enabled = newValue;
  if (remote) console.log('setting changed from another tab');
});

function toggle() {
  enabled = !enabled;
  GM_setValue('enabled', enabled); // fires the listener in *other* tabs, not this one
}
```

`GM_setValue` doesn't trigger your own tab's `GM_addValueChangeListener` for
the change you just made (only other tabs see `remote: true`); update local
state directly at the call site, as above.

## Cross-origin fetch (bypassing page CORS/CSP)

```js
// @grant GM_xmlhttpRequest
GM_xmlhttpRequest({
  method: 'GET',
  url: 'https://api.example.com/data',
  responseType: 'json',
  headers: { 'Accept': 'application/json' }, // no Cookie/Origin/Referer/etc - see gm-api.md
  onload(res) {
    console.log(res.response); // already parsed per responseType
  },
  onerror(err) { console.error(err); },
});
```

Or the promise-based form:

```js
// @grant GM.xmlHttpRequest
const res = await GM.xmlHttpRequest({ url: '...', responseType: 'json' });
console.log(res.response);
```

See `gm-api.md` § Network for the complete option list and the forbidden-
header list — don't promise a script can override `Cookie`/`Origin`/etc.,
the browser blocks it regardless of grant.

## Copy something to the clipboard from a click handler

```js
// @grant GM_setClipboard
function onClick() {
  GM_setClipboard(theValue, 'text');
}
```

Prefer this over `navigator.clipboard.writeText()` inside userscripts —
`navigator.clipboard` requires the document to be focused, which fails
unpredictably from handlers fired via synthetic/injected clicks or from
callbacks that resolve after focus has moved (confirmed to fail with
`"Document is not focused"` in real testing). `GM_setClipboard` has neither
restriction.

## Menu command + hotkey for the same action

```js
// @grant GM_registerMenuCommand
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/shortcut@1
function doTheThing() { /* ... */ }

GM_registerMenuCommand('Do the thing', doTheThing);
VM.shortcut.register('c-shift-k', doTheThing);
```

Label the menu item with its own bound key using `VM.shortcut.reprShortcut`
(confirmed pattern from the official guide) instead of hardcoding the
human-readable text — it stays correct if the shortcut string changes later:

```js
const shortcut = 'c-g c-g';
const label = `Good Game (${VM.shortcut.reprShortcut(shortcut)})`; // "Good Game (Ctrl-G Ctrl-G)"
GM_registerMenuCommand(label, () => alert('Good Game!'));
VM.shortcut.register(shortcut, () => alert('Good Game!'));
```

## SPA sites that don't re-run scripts on soft navigation

Match the whole site, then detect navigation yourself — Violentmonkey's own
matching only fires on real page loads, not `pushState`/`history` navigation
(confirmed guidance from the matching docs):

```js
// @match *://example.com/*
let lastPath = location.pathname;
new MutationObserver(() => {
  if (location.pathname !== lastPath) {
    lastPath = location.pathname;
    onNavigate();
  }
}).observe(document.body, { childList: true, subtree: true });

function onNavigate() { /* re-run whatever needs to happen per-page */ }
onNavigate(); // handle the initial load too
```

Or, if the target browser supports it, the native `navigation` API's
`navigate` event is a cleaner signal than a `MutationObserver` for this
specific purpose — use it when available and fall back to the observer
otherwise.
