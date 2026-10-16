# Scriptlets (`##+js(...)`) — exhaustive reference

Confirmed against uBO 1.74.0 by downloading and grepping every file in
`src/js/resources/*.js` (31 files) directly — every `name:`/`aliases:`/
`requiresTrust:` entry below is copied from source, not the wiki. This list
supersedes any earlier partial documentation.

## Mechanism

```
example.com##+js(scriptletName, arg1, arg2, ...)
```

- Always scoped to a hostname (generic `##+js()` is not allowed).
- Exception form: `example.com#@#+js(scriptletName, ...)`.
- Args are comma-separated; escape a literal comma as `\,`.
- The `.js` suffix is implicit; use the short name or any alias.
- Internal `.fn` entries seen in source (e.g. `safe-self.fn`, `proxy-apply.fn`)
  are shared helper code, not directly invocable — they're listed here only
  where relevant to explain a scriptlet's mechanism.

## Trusted vs untrusted — critical distinction

Every scriptlet below is tagged **[trusted]** or plain. **[trusted]** scriptlets
only execute when the filter comes from a **trusted source** — the user's own
*My filters*, or a subscribed list explicitly marked trusted in the dashboard.
From an ordinary subscribed list they are silently no-ops. Always tell the user
when a rule needs *My filters* specifically.

---

## Property / constant control

| Scriptlet | Aliases | Trust | Parameters |
|---|---|---|---|
| `set-constant` | `set` | | `propChain, value[, extraArgs]` — force `window.<propChain>` to a validated constant (`true`,`false`,`null`,`undefined`,`noopFunc`,`trueFunc`,`falseFunc`,`''`,a number, `noopPromiseResolve`, etc.) |
| `trusted-set-constant` | `trusted-set` | **[trusted]** | Same as `set-constant` but accepts **arbitrary** JSON as `value`, not just the safe-value list |
| `set-attr` | | | `selector, attr, value` — sets an attribute on matching elements on load + on DOM mutation. `value` supports `''`, `true`, `false`, an integer 0–32767, or `[other]` to copy another attribute's value |
| `trusted-set-attr` | | **[trusted]** | Same as `set-attr` but `value` is unrestricted |
| `remove-attr` | `ra` | | `attribute[, selector[, behavior]]` — `attribute` may be space-separated names; `behavior` tokens: `asap` (remove ASAP instead of async), `stay` (keep re-removing on mutation) |
| `remove-class` | `rc` | | Same shape as `remove-attr`, for class names |
| `freeze-element-property` | | | `property[, selector[, pattern]]` — conditionally block **assignment** to an element property; `pattern` prefixed with `!` inverts the match |
| `prevent-innerHTML` | | | `[selector[, pattern]]` — specialization of `freeze-element-property` for `innerHTML` |
| `spoof-css` | | | `selector, property, value[, property, value...]` — spoof computed CSS property values read by page JS (anti-fingerprinting/anti-detection) |

## Abort / throw on access

| Scriptlet | Aliases | Trust | Parameters |
|---|---|---|---|
| `abort-on-property-read` | `aopr` | | `propChain` — throws `ReferenceError` when the property is read |
| `abort-on-property-write` | `aopw` | | `propChain` — throws when the property is written |
| `abort-current-script` | `abort-current-inline-script`, `acis`, `acs` | | `propChain[, needle[, srcPattern]]` — aborts the currently-executing (usually inline) script if it touches `propChain` and, optionally, if the script's source text matches `needle` |
| `abort-on-stack-trace` | `aost` | | `propChain[, stackNeedle]` — aborts when `propChain` is accessed from a call stack matching `stackNeedle` |

## Timers / animation frame

| Scriptlet | Aliases | Trust | Parameters |
|---|---|---|---|
| `prevent-setTimeout` | `no-setTimeout-if`, `nostif`, `setTimeout-defuser` | | `[needle[, delay]]` — conditionally block the callback; `needle` can be `!`-negated; `delay` supports `min-max`/`min-`/`-max` ranges, also `!`-negatable |
| `prevent-setInterval` | `no-setInterval-if`, `nosiif`, `setInterval-defuser` | | Same shape as `prevent-setTimeout`, for `setInterval` |
| `prevent-requestAnimationFrame` | `no-requestAnimationFrame-if`, `norafif` | | `[needle]` — conditionally block rAF callbacks |
| `adjust-setInterval` | `nano-setInterval-booster`, `nano-sib` | | Adjust (not block) `setInterval` delay/behavior |
| `adjust-setTimeout` | `nano-setTimeout-booster`, `nano-stb` | | Adjust (not block) `setTimeout` delay/behavior |

## Network interception — fetch / XHR

| Scriptlet | Aliases | Trust | Parameters |
|---|---|---|---|
| `prevent-fetch` | `no-fetch-if` | | `propsToMatch[, responseBody[, responseType[, throttle, n]]]` — block matching `fetch()` calls and return a dummy response; untrusted flavor limits `responseBody` to safe constants |
| `trusted-prevent-fetch` | | **[trusted]** | Same as `prevent-fetch` but `responseBody` is unrestricted |
| `prevent-xhr` | `no-xhr-if` | | `propsToMatch[, responseBody]` — block matching XHR sends and return a dummy response (safe values only) |
| `trusted-prevent-xhr` | | **[trusted]** | Same, `responseBody` unrestricted |
| `trusted-replace-fetch-response` | `trusted-rpfr` | **[trusted]** | `pattern, replacement, propsToMatch` — regex/text replace on a matching `fetch()` response **body** |
| `trusted-replace-xhr-response` | | **[trusted]** | `pattern, replacement, propsToMatch` — same, for XHR responses |
| `trusted-replace-argument` | | **[trusted]** | `propChain, argposRaw, argraw[, condition, pattern]` — replace an argument passed to any method call. `argraw` forms: `json:<value>` (JSON-parsed), `repl:/pat/repl/` (regex replace), `add:<number>` (arithmetic). `argposRaw` accepts a negative index or the literal `this` |
| `trusted-replace-outbound-text` | | **[trusted]** | Replace text in outbound text-returning calls |
| `trusted-suppress-native-method` | | **[trusted]** | Suppress a native method's real behavior conditionally |
| `trusted-override-element-method` | | **[trusted]** | Override an element method's implementation |
| `trusted-prevent-dom-bypass` | | **[trusted]** | Prevent script techniques that bypass DOM-based protections |
| `call-nothrow` | | | `propertyChain` — wraps a function so that if it throws, the exception is swallowed and execution proceeds as if it hadn't |

## JSON editing (prune AND assign) — the `json-edit` family

This is the mechanism for **changing values**, not just removing them, in
objects passed to/from `JSON.parse`, `fetch`, `XMLHttpRequest`, and object
getters/setters/methods. All use a shared query language, **`jsonq`** (uBO-flavored
JSONPath — see below). Plain scriptlets can only **remove** matched paths;
`trusted-*` counterparts can **assign** new values via the query's `=value` suffix.

| Scriptlet | Trust | Parameters | Targets |
|---|---|---|---|
| `json-edit` (`json-edit.js`) | | `jsonq[, matches, pattern]` | Object from `JSON.parse()` — **remove only**. Optional vararg `matches` narrows application to calls whose inbound JSON string matches `pattern` (literal or regex) |
| `trusted-json-edit` | **[trusted]** | `jsonq[, matches, pattern]` | Same, but query can **assign** |
| `edit-inbound-object` | | `propChain, argPos, jsonq` | Object passed **as an argument** to `propChain` — remove only |
| `trusted-edit-inbound-object` | **[trusted]** | `propChain, argPos, jsonq` | Same, assign allowed |
| `edit-outbound-object` | | `propChain, jsonq` | Object **returned by** `propChain` — remove only |
| `trusted-edit-outbound-object` | **[trusted]** | `propChain, jsonq` | Same, assign allowed |
| `edit-this-object` | | `propChain, jsonq[, order]` | `this` object of a method — remove only. `order=after` edits post-call (default: pre-call) |
| `trusted-edit-this-object` | **[trusted]** | `propChain, jsonq[, order]` | Same, assign allowed |
| `edit-object-on-getter` | | `propChain, jsonq` | Object returned on **property read** — remove only |
| `trusted-edit-object-on-getter` | **[trusted]** | `propChain, jsonq` | Same, assign allowed |
| `edit-object-on-setter` | | `propChain, jsonq` | Object passed on **property write** — remove only |
| `trusted-edit-object-on-setter` | **[trusted]** | `propChain, jsonq` | Same, assign allowed |
| `edit-element-object` | | `selector, jsonq[, timeout]` | A DOM-attached JS object located via `selector` — remove only |
| `trusted-edit-element-object`(`trusted-element-this-object.js`) | **[trusted]** | `selector, jsonq[, timeout]` | Same, assign allowed |
| `json-edit-xhr-response` | | `jsonq[, propsToMatch, value...]` | XHR **response** JSON — remove only |
| `trusted-json-edit-xhr-response` | **[trusted]** | Same | Same, assign allowed |
| `json-edit-xhr-request` | | `jsonq[, propsToMatch, value...]` | XHR **request body** JSON — remove only |
| `trusted-json-edit-xhr-request` | **[trusted]** | Same | Same, assign allowed — **this is how you rewrite an outgoing XHR JSON body** |
| `json-edit-fetch-response` | | `jsonq[, propsToMatch, value...]` | `fetch()` **response** JSON — remove only |
| `trusted-json-edit-fetch-response` | **[trusted]** | Same | Same, assign allowed |
| `json-edit-fetch-request` | | `jsonq[, propsToMatch, value...]` | `fetch()` **request body** JSON — remove only |
| `trusted-json-edit-fetch-request` | **[trusted]** | Same | Same, assign allowed — **this is how you rewrite an outgoing fetch JSON body** |
| `jsonl-edit-xhr-response` | | `jsonq[, propsToMatch, value...]` | Each object in a JSONL (newline-delimited JSON) XHR response — remove only |
| `trusted-jsonl-edit-xhr-response` | **[trusted]** | Same | Same, assign allowed |
| `jsonl-edit-fetch-response` | | `jsonq[, propsToMatch, value...]` | Each object in a JSONL fetch response — remove only |
| `trusted-jsonl-edit-fetch-response` | **[trusted]** | Same | Same, assign allowed |

`propsToMatch` (where present) narrows which `xhr.open()`/`fetch()` calls this
applies to — by default matched against the URL; `key:pattern` pairs (e.g.
`method:POST`) are also supported.

### `jsonq` — uBO-flavored JSONPath syntax

Confirmed from `src/js/jsonpath.js`. Base syntax follows JSONPath (RFC 9535)
with these differences: no array slice operator; a selector can be a
`/regex/`-delimited pattern (`$./pattern/`); only one filter selector allowed
per filter expression.

**Path examples** (standard JSONPath):
```
.store.book[*].author
..author
.store.*
.store..price
..book[2]
..book[?(.isbn)]
..book[?(.price<10)]
..*
```

**Filter operators** inside `[?(...)]` — operand must be valid JSON:
`==` `!=` `<` `<=` `>` `>=` `^=` (starts with) `$=` (ends with) `*=`
(includes) `=/regex/` (regex test).

**Assignment** — append `=<value>` to the path to **set** instead of remove
(only takes effect via a `trusted-*` scriptlet):
```
.store..price=0
.store.book[*].author="redacted"
```
Advanced assignment forms (per source comment, "to be documented" upstream —
confirm exact shape before relying on them in a critical rule):
- `=repl(...)` — regex replace, shape like `{"regex":"...","flags":"i","replacement":"..."}`
- `=call(...)` — call a function, shape like `["${obj}","setAttribute","${key}"]`

**When no assignment is present, the resolved path is removed** — this is what
the non-`trusted` variants use under the hood.

### Worked examples

```
! Zero out a price field in a checkout API response (assign — needs My filters)
example.com##+js(trusted-json-edit-fetch-response, .cart.total=0, /api\/cart/)

! Change a quantity being sent in a POST body (assign — needs My filters)
example.com##+js(trusted-json-edit-fetch-request, .items[*].qty=1, method:POST)

! Strip a tracking field from a response object (remove — no trust needed)
example.com##+js(json-edit-xhr-response, .telemetry)

! Redact every author field surviving a JSON.parse (assign)
example.com##+js(trusted-json-edit, .store.book[*].author="redacted")
```

## Cookies / storage

| Scriptlet | Aliases | Trust | Parameters |
|---|---|---|---|
| `set-cookie` | | | `name, value[, path]` — value must be from uBO's safe-value list; unsafe values are ignored |
| `trusted-set-cookie` | | **[trusted]** | Same, `value` unrestricted |
| `set-cookie-reload` | | | Like `set-cookie`, reloads the page after setting |
| `trusted-set-cookie-reload` | | **[trusted]** | Trusted + reload variant |
| `remove-cookie` | `cookie-remover` | | `needle[, when, token...]` — removes matching cookies immediately and on unload; `when` vararg: `scroll`, `keydown` — also remove on those events |
| `set-local-storage-item` | | | `key, value` — safe-value list only |
| `set-session-storage-item` | | | Same, `sessionStorage` |
| `trusted-set-local-storage-item` | | **[trusted]** | `value` unrestricted |
| `trusted-set-session-storage-item` | | **[trusted]** | `value` unrestricted |

## Object pruning (legacy/simple form — see also `json-edit` family above)

| Scriptlet | Trust | Parameters |
|---|---|---|
| `json-prune` | | `[rawPrunePaths[, rawNeedlePaths[, stackNeedle]]]` — remove paths from `JSON.parse()` results; no-arg form just logs the object |
| `json-prune-fetch-response` | | `prunePaths[, needlePaths[, propsToMatch]]` — same, scoped to matching `fetch()` responses |
| `json-prune-xhr-response` | | Same, for XHR responses |
| `evaldata-prune` | | Prune properties from data passed through `eval()`/`Function()` |
| `trusted-prune-inbound-object` | **[trusted]** | `propChain, argPos, rawPrunePaths[, ...]` — prune properties of an object argument |
| `trusted-prune-outbound-object` | **[trusted]** | `propChain, rawPrunePaths[, ...]` — prune properties of an object a method returns |

*(These predate the `json-edit` family's `jsonq` syntax and use a simpler
dot/pipe path list. Prefer `json-edit`/`trusted-json-edit-*` for new rules —
they're strictly more capable since they also support assignment.)*

## XML / playlist pruning

| Scriptlet | Parameters |
|---|---|
| `xml-prune` | `[selectorOrXpath[, urlPattern]]` — remove matching elements from an XML response |
| `m3u-prune` | `[pattern[, urlPattern]]` — remove matching segments from an M3U8 playlist response |

## Navigation / windows / dialogs

| Scriptlet | Aliases | Trust | Parameters |
|---|---|---|---|
| `prevent-window-open` | `nowoif`, `no-window-open-if`, `window.open-defuser` | | `[pattern[, delay, decoy]]` — `decoy`: `blank`, `object`, `frame` |
| `close-window` | `window-close-if` | | Conditionally close the current window |
| `window.name-defuser` | | | Clears `window.name` (common exploit/tracking vector) |
| `prevent-navigation` | | | `[pattern]` — abort matching navigation events; `!` inverts |
| `prevent-dialog` | | | `[selector]` — auto-close native `<dialog>` elements matching `dialog{selector}` |
| `prevent-clipboard-write` | | **[trusted]** | `matches[, excludeMatches, pattern][, domAlert, message[, selectable, bool]]` — block clipboard overwrites matching `matches` (pattern/regex); vararg key:value pairs follow: `excludeMatches` exempts text matching its pattern from prevention; `domAlert` shows an on-page message (`${text}` interpolates the matched clipboard text, `\n` for a literal newline); `selectable` (default `true`) controls whether the alert text can be selected |
| `href-sanitizer` | | | `selector, source` — rewrite an `<a>`'s `href` from text content, another attribute, or via `urlskip`-style transform steps |
| `disable-newtab-links` | | | No-arg: stop links from force-opening new tabs |
| `overlay-buster` | | | No-arg: attempt to remove common paywall/overlay blockers |
| `alert-buster` | | | No-arg: neutralize `alert()`/`confirm()`/`prompt()` dialogs |
| `trusted-click-element` | | **[trusted]** | `steps[, extraMatch[, delay]]` — `steps` is a comma-separated list of CSS selectors (or `xpath:`-prefixed expressions) to click in order and/or integers giving a delay in ms before the next step (a trailing integer is instead the overall bail-out timeout, default 11s); prefix the whole list with `;` or `\|` to use that character as the separator instead of comma (for a selector that itself contains a comma); `>>>` pierces into a shadow root, `when-visible:` prefix defers the click until the element is visible |
| `trusted-create-html` | | **[trusted]** | `parent, html[, duration]` — parse and inject an HTML string as children of `parent`; optional auto-removal after `duration` ms |
| `remove-node-text` | `rmnt` | | Remove matching text nodes |
| `trusted-replace-node-text` | `trusted-rpnt`, `replace-node-text`, `rpnt` | **[trusted]** | Regex-replace text nodes |

## Anti-fingerprinting / misc defusers

| Scriptlet | Parameters |
|---|---|
| `nowebrtc` | No-arg: disable `RTCPeerConnection` |
| `webrtc-if` | Conditionally disable WebRTC |
| `prevent-canvas` | `[contextType]` — block canvas API access; `contextType` regex/string, `!`-negatable |
| `multiup` | Site-specific defuser (multiup.io) |
| `break-on-call` | `propertyChain` — trigger a debugger breakpoint when the property chain is called (debugging aid) |
| `proxy-apply-config.js` | `config` — a JSON object merged into the internal `proxy-apply.fn` helper's config (e.g. `{"skipToString":true}` to stop it from proxying `Function.prototype.toString`, which some anti-debugging scripts probe). Runs before other scriptlets on the page (registered with an internal execution priority) so the config takes effect first. Advanced/rarely needed — only relevant when another scriptlet built on `proxy-apply.fn` needs tuning |

## Anti-adblock-detector defusers

`prevent-addEventListener` (aliases `addEventListener-defuser`, `aeld`),
`prevent-bab` (aliases `bab-defuser`, `nobab`) — plus the redirect-resource
surrogates `nobab2.js`, `nofab.js`, `popads.js`, `popads-dummy.js`,
`fingerprint2.js`, `fingerprint3.js`, `ampproject_v0.js` (see
`redirect-resources.md` — these are swapped in via `$redirect=`, not `##+js()`).

---

See `references/redirect-resources.md` for the `$redirect=`/`$redirect-rule=`
resource tokens (neutered stand-ins, not scriptlets).
