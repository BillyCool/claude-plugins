# Cosmetic filters

Confirmed against uBO 1.72.2 (`src/js/static-ext-filtering.js`,
`src/js/static-filtering-parser.js`). Cosmetic filters **hide** elements with
CSS; they do not stop downloads. Prefer a network filter when the target is its
own request.

## Separators

| Separator | Meaning |
|---|---|
| `##` | Hide elements matching the selector |
| `#@#` | Exception — un-hide (cancel a `##` rule) for this scope |
| `##+js(` | Scriptlet injection (see `scriptlets.md`) |
| `#@#+js(` | Scriptlet injection exception |
| `##^` | HTML filtering (Firefox only, see `html-filtering-firefox.md`) |
| `#@#^` | HTML filtering exception |

## Scope (left of `##`)

- `example.com##.ad` — applies only on `example.com` (and subdomains).
- `example.com,other.net##.ad` — multiple hosts.
- `~sub.example.com,example.com##.ad` — exclude a subdomain with `~`.
- `example.*##.ad` — **entity** syntax: all public-suffix variants
  (`example.com`, `example.co.uk`, …).
- `/regex/##.ad` — hostname matched as a regex, e.g.
  `/^img[a-z]{3}\.example\./##.banner`.
- `##.ad` (no scope) — **generic**, applies everywhere. Use rarely and only for
  patterns that are unambiguous garbage; generic rules are the main breakage risk.

## Selector body (right of `##`)

Any standard CSS selector: `.class`, `#id`, `[attr]`, `[attr="v"]`,
`[attr^="v"]`, `[attr*="v"]`, `tag`, combinators (`>`, `+`, `~`, descendant),
`:nth-child()`, etc. Everything the browser's CSS engine supports.

For anything beyond plain CSS (content, ancestors, randomized markup), use a
procedural cosmetic filter — see `procedural-cosmetic.md`.

## Styling / removal action

- `example.com##.overlay:style(display: block !important; position: static !important;)`
  — apply CSS instead of hiding. Good for un-freezing scroll, killing sticky
  overlays, restoring visibility.
- `example.com##.ad:remove()` — remove the node from the DOM entirely (stronger
  than hiding; use when the site checks whether the element is still present).

`:style()` and `:remove()` are the two action operators; they must be the **last**
component of the selector. (`:remove-attr()` / `:remove-class()` also exist — see
`procedural-cosmetic.md`.)

## Examples

```
! Hide a specific ad container
example.com##.sponsored-post

! Hide by stable attribute rather than a randomized class
example.com##div[data-ad-slot]

! Un-hide something an over-broad list rule hid
example.com#@#.promo

! Restore scrolling disabled by an anti-adblock overlay
example.com##body:style(overflow: auto !important;)
```
