# Procedural cosmetic filters

Confirmed against uBO 1.74.0 (`src/js/static-filtering-parser.js`:
`proceduralOperatorNames`, `maybeProceduralOperatorNames`, `actionOperators`,
`proceduralActionNames`, `normalizedOperators`).

Procedural filters run in JS, not the CSS engine. They let you select by
**content**, **relationships**, and **computed style** — essential when markup is
randomized or the target has no stable selector of its own. They **must be
scoped to a hostname** (no generic procedural rules).

## Selector operators

| Operator | Purpose |
|---|---|
| `:content(sel)` | Pierce into a `<template>` element's inert `.content` fragment and continue selecting with `sel` inside it (analogous to `:shadow()` but for template content instead of a shadow root). Also usable in HTML filtering (`##^`). |
| `:has(sel)` | Subject has a descendant matching `sel`. Becomes native CSS `:has()` when possible. |
| `:not(sel)` | Subject does NOT match `sel` (procedural form). Native when possible. |
| `:has-text(needle)` | Subject's text contains `needle`; literal or `/regex/` with `i`/`m` flags. Aliases: `contains`, `-abp-contains`. |
| `:matches-attr(name=value)` | Match by attribute, incl. randomized names — patterns/regex allowed on name and value. |
| `:matches-css(prop: value)` | Match on computed CSS. `/regex/` allowed on value. |
| `:matches-css-before(prop: value)` | Same, for the `::before` pseudo-element. |
| `:matches-css-after(prop: value)` | Same, for the `::after` pseudo-element. |
| `:matches-media((query))` | Apply only when a CSS media query matches. Best used as the last operator. |
| `:matches-path(pattern)` | Match on the document's URL path/query; literal or `/regex/`. Narrow a rule to certain pages. |
| `:matches-prop(chain=value)` | Match by JS DOM property (or property chain) and optional value. |
| `:min-text-length(n)` | Subject text length ≥ `n`. |
| `:others()` | Selects everything *outside* the current set (experimental). |
| `:shadow(sel)` | Pierce into shadow DOM to continue selecting. |
| `:upward(n or sel)` | Move to an ancestor: integer 1–255 levels up, or nearest ancestor matching `sel`. Alias: `nth-ancestor` (n form). |
| `:watch-attr(names)` | Re-run the filter when the named attribute(s) change (for late/dynamic DOM). Alias: `watch-attrs`. |
| `:xpath(expr)` | Select via XPath; can create a new set or filter the current one. |

`:has` and `:not` are "maybe-procedural": uBO uses native CSS if the browser
supports it, else falls back to procedural evaluation.

## Action operators (must be last)

| Operator | Effect |
|---|---|
| `:style(css)` | Apply inline CSS to the matched element instead of hiding. |
| `:remove()` | Remove the matched element from the DOM. |
| `:remove-attr(names)` | Remove attribute(s); pattern/regex allowed. |
| `:remove-class(names)` | Remove class(es); pattern/regex allowed. |

## When to reach for procedural

- **Randomized classes/ids** → anchor on stable structure or text:
  `example.com##.container:has(> [data-testid="ad"])`
- **"Hide the box that contains this text"** →
  `example.com##.post:has-text(/sponsored/i)`
- **Target has no hook but its child does** → select the child, climb up:
  `example.com##a[href*="/ad/"]:upward(3)`
- **Only on certain pages** → add `:matches-path(/^\/watch/)`.
- **Element injected late** → add `:watch-attr(class)` or select a stable parent.

## Cautions

- Procedural filters cost more than plain CSS; prefer a plain `##` selector when
  a stable one exists.
- `:has-text` on generic words can over-match — anchor with a container class and
  specific text.
- Test the full chain against the live DOM before finalizing (see SKILL.md §3).

## Examples

```
! Remove a promo card identified only by its heading text
example.com##article:has(h2:has-text(Advertisement))

! Kill a sticky element whose class is hashed, via its data attribute
example.com##div[class]:matches-attr(data-testid=/^ad-/):remove()

! Hide comment spam over a length threshold containing a keyword
example.com##.comment:has-text(/casino|crypto/i):min-text-length(200)
```
