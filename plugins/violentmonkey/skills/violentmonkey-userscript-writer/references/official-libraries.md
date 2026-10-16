# Official `@violentmonkey/*` libraries

Four packages published by the Violentmonkey team under the `@violentmonkey`
npm scope. Every function/export below was confirmed by downloading the
actual jsDelivr-served bundle and grepping its `exports.*` — not copied from
README prose, which is often thinner than the real API. Reach for these
before hand-rolling the equivalent; they're small, dependency-free, and exist
specifically to remove this kind of boilerplate from userscripts.

Load with `@require`, versions pinned via jsDelivr's npm proxy:

```js
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/dom@2
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/ui@0.7
```

Or combine multiple requires into one request with jsDelivr's combine
endpoint (confirmed from the `@violentmonkey/ui` README):

```js
// @require https://cdn.jsdelivr.net/combine/npm/@violentmonkey/dom@2,npm/@violentmonkey/ui@0.7
```

Everything is exposed under the shared global namespace `VM` (e.g. `VM.observe`,
`VM.showToast`) — safe to `@require` several of these together, they merge
onto the same object rather than clobbering each other.

## `@violentmonkey/dom` (latest confirmed: 2.2.1)

```js
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/dom@2
```

| Export | Signature | Notes |
|---|---|---|
| `VM.observe` | `(node, callback, options?)` → `disconnect` function | Thin `MutationObserver` wrapper (`childList: true, subtree: true` by default, overridable via `options`). Calls `callback(mutations, observer)` on every mutation batch; **if the callback returns a truthy value, the observer auto-disconnects**. For a one-shot "wait until this element exists" case this is exactly the pattern — return `true` once you've found and handled it. For persistent watching (element gets re-added repeatedly, e.g. list re-renders), just never return truthy from the callback. |
| `VM.h` | `(tag, attrs, ...children)` → vdom node | JSX-pragma-compatible element builder (`React.createElement`-alike). |
| `VM.m` | `(vdomNode)` → real `Element` | "Mount" a `VM.h` result into an actual DOM node. |
| `VM.hm` | `(tag, attrs, ...children)` → real `Element` directly | `VM.h` + `VM.m` combined, skips the intermediate vdom step, no SVG support. |
| `VM.Fragment` | JSX fragment marker | For `<>...</>`-style grouping when using JSX + a bundler. |
| `VM.getElementsByXPath` | `(xpath, contextNode?)` | XPath querying helper. |
| `VM.getTextValues` | `(node)` → `string[]` | Walks a node's text content, skipping `<script>`/`<style>`, recursively. |

`VM.observe` example (exact source, `vm-dom`'s own doc comment):

```js
VM.observe(document.body, () => {
  const node = document.querySelector('.profile');
  if (node) {
    console.log("It's there!");
    return true; // disconnect
  }
});
```

## `@violentmonkey/ui` (latest confirmed: 0.7.9)

```js
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/dom@2
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/ui@0.7
```

**Hard dependency on `@violentmonkey/dom@2`** — the bundle itself throws at
load time if `VM.versions.dom` isn't a `2.x` string, with an explicit error
message telling you to add the `@require`. Order matters: `dom` before `ui`.

| Export | Signature | Notes |
|---|---|---|
| `VM.showToast` | `(content, options?)` → `{ close(), ...hostElem }` | `content` can be a plain string or a `VM.h`/DOM node. `options`: `theme` (`'light'`\|`'dark'`), `duration` (ms, `0` = manual close only, default `2000`), `shadow` (boolean, default `true` — renders in a shadow root for style isolation from the host page), `className`, `style`, `beforeEnter`/`beforeClose` (async hooks). Prefer this over hand-building a styled `<div>` toast — it's shadow-DOM isolated by default, so the host page's CSS can't leak in or clash. |
| `VM.getPanel` | `(options?)` → panel object: `{ wrapper, body, show(), hide(), clear(), append(...nodes), setContent(...nodes), setMovable(bool, opts?), dispose() }` | Persistent floating panel, same shadow-DOM isolation as the toast. `setMovable(true)` makes it mouse-draggable (backed by the exported `Movable` class). Position it via `panel.wrapper.style.top = '...'` etc. after creation. |
| `VM.Movable` | class `(el, options)` | What `getPanel`'s `setMovable` uses internally; `options.origin` controls which edge the drag snaps to (`{x: 'auto'|'start', y: 'auto'|'start'}`). Rarely used directly — go through `getPanel`. |
| `VM.getHostElement` | `(shadow = true)` → `{ id, host, root, addStyle(css), dispose(), show(), hide() }` | Low-level primitive both `showToast` and `getPanel` are built on. Use directly only if you need a custom shadow-DOM-isolated container that isn't a toast or panel. |
| `VM.appendToBody` | `(tag, ...children)` | Internal helper; warns and no-ops if `document.body` doesn't exist yet (i.e. called too early relative to `@run-at`). |
| `VM.classNames` | `(namesArray)` → space-joined string, falsy entries filtered | Small utility, same idea as the popular `classnames` npm package. |

## `@violentmonkey/shortcut` (latest confirmed: 1.4.4)

```js
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/shortcut@1
```

| Export | Signature | Notes |
|---|---|---|
| `VM.shortcut.register` | `(keySequence, callback, options?)` → registers on the default shared `KeyboardService` | Shortcuts are enabled by default once registered. |
| `VM.shortcut.enable` / `.disable` | `()` | Toggle all shortcuts on the default service at once. |
| `VM.shortcut.handleKey` | `(keyboardEvent)` | Feed key events manually (e.g. from inside a rich-text editor's own `keydown` handler) instead of relying on the service's own document-level listener. |
| `VM.shortcut.KeyboardService` | class, `new KeyboardService(options?)` | Independent instance for scoped shortcut sets. `options.sequenceTimeout` (ms) controls the multi-key-sequence timeout. Has its own `.register()`, `.enable()`, `.disable()`, `.setContext(name, value)` for conditional shortcuts. |
| `VM.shortcut.parseKey` / `.buildKey` / `.reprKey` / `.reprShortcut` / `.normalizeSequence` / `.parseCondition` | lower-level parsing utilities | Rarely needed directly. |

**Key syntax**: modifiers joined by `-` before exactly one base key, e.g.
`ctrl-alt-c` or the abbreviated `c-a-c`. Modifier aliases: `c`/`ctrl`/`control`,
`s`/`shift`, `a`/`alt`, `m`/`meta`/`cmd`, and the cross-platform special case
`cm`/`ctrlcmd` (resolves to `ctrl` on Windows/Linux, `cmd` on macOS — use this
for a shortcut that should feel native on both). Sequences are space-separated
combined keys: `register('c-a c-b', fn)` fires on Ctrl-A then Ctrl-B in
sequence.

**Conditional registration**: `register(key, fn, { condition: '!disableThisKey' })`
— condition strings support `&&` and `!`, evaluated against values set via
`service.setContext(name, value)`.

## `@violentmonkey/types` (latest confirmed: 0.3.3)

TypeScript ambient type declarations for the whole `GM_*`/`GM.*` surface.
Dev-time only (no runtime `@require` — it's a `devDependency` for a
TS-based userscript project, not something you load in the browser). Only
relevant if the user is authoring in TypeScript with a real build step; skip
for plain hand-written `.user.js` files.

## When *not* to reach for these

- Don't `@require` `@violentmonkey/ui` for a one-off `alert()`-equivalent if
  the target site already has its own toast/notification function you can
  call — reuse the site's own UI system for visual consistency (as done in
  earlier StreamRecorder scripts this skill's author has written, which
  called the site's own `showToast`).
- Don't pull in `@violentmonkey/dom` just for `VM.h`/`VM.m` if the script
  only creates one or two elements — plain `document.createElement` is
  simpler for something that small. Reach for it when you're building real
  structure repeatedly (list rendering, a whole panel's contents) or when you
  specifically want `VM.observe`.
