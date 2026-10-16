# Network filters

Confirmed against uBO 1.72.2 (`src/js/static-filtering-parser.js`,
`nodeTypeFromOptionName`). Firefox MV2 = full support for everything here.

## Pattern anchoring

| Token | Meaning |
|---|---|
| `\|\|example.com^` | Hostname anchor — matches `example.com` and all subdomains, any scheme |
| `^` | Separator — matches any char that isn't a letter/digit/`_`/`-`/`.`/`%`, or end of URL (commonly the boundary after a host or path segment) |
| `\|` at start | Anchors to the start of the URL (e.g. `\|https://`) |
| `\|` at end | Anchors to the end of the URL |
| `*` | Wildcard, matches zero+ chars |
| bare `example.com` | Substring match anywhere in the URL (usually you want `\|\|…^` instead) |
| `/regex/` | Whole pattern as a regex when wrapped in slashes |

Canonical shape for "block a host": `||host^`. For a specific path/file:
`||host/path/file.js`.

## Type options (what kind of request)

`script`, `image`, `stylesheet` (alias `css`), `font`, `media`, `object`
(alias `object-subrequest`), `frame` (alias `subdocument`), `xhr` (alias
`xmlhttprequest`), `websocket`, `ping` (alias `beacon`), `other`,
`popup`, `popunder`, `document` (alias `doc`), `inline-script`, `inline-font`,
`webrtc`.

- `$all` = all network types + `popup` + `document` + `inline-script` +
  `inline-font` (the broadest block).
- Combine multiple types with commas: `$script,xhr`.
- Negate a type with `~`: `$~image` (everything except images).

## Party options

- `3p` (alias `third-party`) / `1p` (alias `first-party`).
- `strict3p` / `strict1p` — partyness judged against the top document's domain,
  not the immediate request context.

## Scoping options

- `domain=` (alias `from=`) — restrict to page domains, pipe-separated, `~` to
  exclude, `.*` entity and `/regex/` supported: `$domain=a.com|~sub.a.com`.
- `to=` — restrict by the request's *destination* domain (same value syntax).
- `top=` — restrict by the top-level document domain.
- `denyallow=` — with `$domain=`, block everything from the matched context
  *except* the listed destination hosts. Requires `$domain=`.
- `method=` — HTTP method(s): `$method=get`, negate `$method=~post`.
- `ipaddress=` — match by resolved IP, supports wildcards, `/regex/`, and the
  keywords `lan` / `loopback`.

## Action / rewrite options

- `important` — overrides any exception (`@@`) filter. Use sparingly.
- `badfilter` — appended to an existing filter's exact text to disable it.
- `redirect=` / `redirect-rule=` — redirect the request to a bundled neutered
  resource (see `scriptlets.md` for resource names). `redirect` implies a block;
  `redirect-rule` only redirects requests already blocked by another filter.
  Optional priority: `$redirect=noopjs:5`.
- `removeparam=` (alias `queryprune`) — strip query parameters; `/regex/`
  supported; bare `$removeparam` strips all. Negate with `~`.
- `csp=` — inject a Content-Security-Policy directive (e.g.
  `$csp=script-src 'self'`). Applies to `document`/`subdocument`.
- `permissions=` — inject a Permissions-Policy directive. *Trusted source only.*
- `header=` (alias of `responseheader`) — match on a response header value;
  `/regex/` and `~` supported. `requestheader` is the request-side counterpart.
- `replace=` — regex replace in the response body: `$replace=/find/replace/i`.
  **Firefox MV2 only, trusted source only.**
- `urlskip=` / `uritransform` — rewrite/extract the destination URL. *Trusted
  source only*; `uritransform` is a deprecation candidate.
- `inline-script` / `inline-font` — block inline scripts/fonts via CSP.

## Cosmetic-control options (on network filters)

- `elemhide` (alias `ehide`) — disable ALL cosmetic filtering on the scope.
- `generichide` (alias `ghide`) — disable generic cosmetic filters only.
- `specifichide` (alias `shide`) — disable host-specific cosmetic filters only.
- `genericblock` — recognized token; disables generic *network* filters on the
  scope. Use only in exceptions and with care.

Typically used as exceptions: `@@||example.com^$elemhide` (stop uBO hiding
things on a site that breaks).

## Deprecated / redirect-preferred

- `empty` → prefer `$redirect=empty`.
- `mp4` → prefer `$redirect=noopmp4-1s`.
- `webrtc` as a blocking type is legacy; prefer the `nowebrtc` scriptlet.
- `cname` — Firefox-only exception modifier controlling CNAME uncloaking.
- `reason` — annotation token, not a matching condition.

## Exceptions

- `@@` prefix makes an allow rule: `@@||example.com^$script,domain=site.com`.
- Options narrow the exception. `@@||host^$important` cannot be beaten by a
  non-important block, but `important` on the block side wins over a plain `@@`.

## Worked examples

```
! Block a third-party tracker script everywhere
||tracker.example^$script,3p

! Block a beacon only on one site
||metrics.example.com^$ping,domain=news.example

! Neutralize an ad video instead of leaving a broken player
||ads.example.com/preroll.mp4^$redirect=noopmp4-1s,media

! Strip a tracking query param site-wide
||example.com^$removeparam=utm_source

! Allow-list a script uBO's lists block, because it breaks the site
@@||cdn.example.com/app.js^$script,domain=example.com
```
