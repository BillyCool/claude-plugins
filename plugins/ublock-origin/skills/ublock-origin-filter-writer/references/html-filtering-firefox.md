# HTML filtering (`##^`) — Firefox only

Confirmed against uBO 1.74.0 (`src/js/static-filtering-parser.js`
`removableHTTPHeaders`; `src/js/html-filtering.js` `operatorToTaskMap`;
`src/js/httpheader-filtering.js`).

HTML filtering edits the response **stream before the browser parses it**, using
Firefox's `webRequest.filterResponseData`. It is **exclusive to Firefox (uBO
MV2)** — it does not exist on Chromium. Because the target element never enters
the DOM, this defeats scripts that check whether their element is still present.

## Element removal

```
example.com##^selector
```

Removes matching elements from the raw HTML. Supported operators are a **subset**
of procedural cosmetics (it works on serialized markup, so no computed-style
operators). Per `operatorToTaskMap`, the supported procedural operators are:

- `:content(...)` — pierce into a `<template>` element's `.content` fragment
- `:has(...)` / `:if(...)`
- `:has-text(...)`
- `:not(...)` / `:if-not(...)`
- `:min-text-length(n)`
- `:upward(n)` / `:nth-ancestor(n)`
- `:xpath(...)`
- plain-CSS selectors (subject path / `spath`)

Common use — strip an inline script by its content:

```
example.com##^script:has-text(adblock)
```

Exception form: `example.com#@#^script:has-text(adblock)`.

Note: uBO ignores a small set of structural tags as removal subjects
(`br`, `head`, `link`, `meta`, `script`, `style` are treated specially in the
walker); target the meaningful element instead.

## Response header removal

```
example.com##^responseheader(header-name)
```

Removes a response header. Only these headers are removable (source:
`removableHTTPHeaders`):

- `location`
- `refresh`
- `report-to`
- `set-cookie`

Anything else is rejected. Exception form:
`example.com#@#^responseheader(set-cookie)`.

```
! Stop a page setting cookies
example.com##^responseheader(set-cookie)

! Neutralize a server-driven redirect
example.com##^responseheader(refresh)
```

## When to use vs alternatives

- Use `##^` when a cosmetic hide isn't enough because a script inspects/needs the
  element absent, or to kill an inline `<script>` there's no network URL for.
- If the offending thing is its own request with a URL, a **network filter** is
  cheaper and simpler — reach for `##^` when it isn't.
