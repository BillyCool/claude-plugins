# Sandbox, `unsafeWindow`, and injection modes

Two **independent** axes control where and how a script's code actually runs.
Conflating them is the most common source of "my patch does nothing" bugs.
Confirmed from `src/background/utils/preinject-prepare.js`,
`src/injected/web/gm-global-wrapper.js`, and the `posts/inject-into-context`
doc page.

## Axis 1 — `@grant`: sandboxed or not

- **`@grant none`** — the script runs **unsandboxed**, directly in whatever
  realm it was injected into (see Axis 2). `window` inside the script *is*
  the same object the page's own scripts see. Zero GM APIs are available
  (except `GM_info`, always present). This is the mode to use for scripts
  that are pure DOM/JS manipulation and never need storage, clipboard,
  cross-origin requests, etc.
- **Any other `@grant`** (even just one, e.g. `@grant GM_setClipboard`) puts
  the script in Violentmonkey's **sandbox**. Inside a sandboxed script,
  `window` refers to a separate wrapper object, *not* the page's real
  `window` — confirmed in `gm-global-wrapper.js`, which builds a proxy object
  (`makeGlobalWrapper`) specifically so grant-related globals stay isolated
  from the page. To reach the page's actual global object from a sandboxed
  script, use **`unsafeWindow`** — and add `@grant unsafeWindow` to be
  explicit about needing it (Violentmonkey generally exposes it in sandboxed
  mode by default, but declaring the grant documents the intent and is
  required by some other userscript managers, so always include it when used).

**Practical rule:** if the script both (a) needs a GM API and (b) needs to
read/patch a global the page itself defined (a function, a variable, an
inline `onclick`'s target), every reference to that page global must go
through `unsafeWindow`, not `window`. This includes the assignment that
installs your patch — `unsafeWindow.someSiteFunction = myReplacement` — and
any lookups inside your replacement that need other page globals
(`unsafeWindow.someOtherHelper`, `unsafeWindow.showToast`, etc.), because a
function object closes over the scope it was *defined* in, not the scope it's
*assigned into* — but the page's own inline `onclick="foo()"` handlers always
resolve `foo` by looking it up on the page's real global object, so that's
the one you must have patched.

## Axis 2 — `@inject-into`: which JS realm/world

- **`page`** — the classic mode. Script executes directly in the page's own
  main-world JS context. Full, direct visibility of page globals even with
  `@grant none`. Breaks on Firefox pages with a strict CSP that forbids
  inline script execution (confirmed common on CSP-strict sites; the docs
  cite GitHub as an example).
- **`content`** — script executes in the browser extension's isolated
  content-script world. Survives strict CSP. Even with `@grant none`, `window`
  here is the *content script's* window, not the page's — reaching page
  globals still requires a bridge (below), regardless of the grant setting.
- **`auto`** (default) — tries `page` first; if blocked by CSP, Violentmonkey
  falls back to `content` automatically. **The author is responsible for
  detecting which one actually happened** and handling both — check
  `GM_info.injectInto` at runtime if the script's behavior depends on it.

### Bridging page ↔ content when stuck in `content` mode

If `@inject-into` ends up as `content` (forced by CSP, or chosen explicitly)
and the script genuinely needs to call into or expose something to the page's
own main-world JS (not just read/patch existing globals via `unsafeWindow`,
which still works in content mode for reading/writing plain properties), two
approaches, confirmed from the docs:

1. **Universal**: message across the world boundary with `window.postMessage`
   or a `CustomEvent` dispatched on `window`/`document`, with a listener on
   the other side. Works in every browser.
2. **Firefox-specific**: Firefox's content scripts get `exportFunction` and
   `cloneInto`, plus `wrappedJSObject` on `unsafeWindow`, for direct
   cross-world function/object exposure:

   ```js
   if (typeof exportFunction === 'function') {
     const wnd = typeof unsafeWindow === 'object' ? unsafeWindow : window;
     wnd.wrappedJSObject.foo = 1;
     wnd.wrappedJSObject.bar = exportFunction(function myFancyApi(x) {
       return cloneInto({ test: () => x }, wnd, { cloneFunctions: true });
     });
   }
   ```

For simple property/function reassignment on an already-existing global
(the common "patch this site's function" case), plain `unsafeWindow.foo = ...`
is sufficient in both `page` and `content` mode — the bridge dance above is
only needed for passing live function references/complex objects *into* the
page's world from a content-mode script.

## Why no manual IIFE wrapper

Source-confirmed from `preinject-prepare.js`:

```js
const wrap = !meta[UNWRAP];               // wraps by default, unless @unwrap
const wrapTryCatch = wrap && IS_FIREFOX;   // + try/catch on Firefox for console errors
const startIIFE = topLevelAwait ? 'await(async' : '(';
// ... later, code is spliced together as:
//   (async function(...){ try { <your code> } catch(e){...} })()   [Firefox, wrap=true]
//   (function(...){ <your code> })()                                [Chrome, wrap=true]
```

Violentmonkey wraps every script's body in its own IIFE (async-aware if
`@top-level-await` is set, try/catch-wrapped on Firefox) **before** injecting
it, unless the script sets `@unwrap`. Two consequences:

1. A hand-added `(function(){'use strict'; ...})();` is always a redundant
   *second* wrapper — it does nothing Violentmonkey wasn't already doing.
2. It's actively harmful for the common patching pattern: `function foo(){}`
   and `var x = ...` declared at the top level of *your* code become
   properties of Violentmonkey's auto-generated IIFE's local scope — which is
   exactly what you want, since that's what makes `window.foo = ...` /
   `unsafeWindow.foo = ...` assignments at the top level of your script work
   correctly against the real page/sandbox global. Adding your *own* manual
   IIFE around that same code nests it one level deeper for no benefit, and
   invites copy-paste bugs where someone forgets which scope a helper
   function actually lives in.

Write flat top-level code. If you specifically want to opt out of
Violentmonkey's own wrapping (rare — e.g. you need a bare top-level `return`
or specific interop with `@unwrap`'s different injection path), that's a
metadata decision (`@unwrap`), not something you replicate by hand.
