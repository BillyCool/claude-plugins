# Selector strategy — picking stable, safe targets

This is the judgment layer. A syntactically valid rule that anchors to volatile
markup is a bad rule. Goal: match the intended target, survive routine site
changes, and break nothing else.

## Ranking of hooks (best → worst)

1. **Semantic id** — `#comments`, `#cookie-banner`. Stable and unique. Verify it
   isn't randomized.
2. **`data-*` attributes with meaning** — `[data-ad-slot]`,
   `[data-testid="promo"]`. Often survive redesigns; test frameworks keep them.
3. **ARIA / role / semantic attributes** — `[role="dialog"]`, `[aria-label="Advertisement"]`.
4. **Meaningful class names** — `.newsletter-signup`, `.sponsored`. Good if
   human-authored.
5. **Structure via `:has()` / `:upward()`** — target a stable child, climb to the
   container. Use when the container itself has no hook.
6. **Text via `:has-text()`** — when content is the only reliable signal.
7. **Positional (`:nth-child`, deep `>` chains)** — last resort; brittle.
8. **Randomized/hashed class or id** — never anchor here directly.

## Detecting randomized markup

Treat a token as randomized (do NOT anchor to it) when it looks like:
- Hash-ish: `.css-1a2b3c`, `.jss127`, `.sc-bdVaJa`, `._1x9Yz`, `.a7Bx9Q`.
- High-entropy / mixed-case short strings, trailing numeric counters that clearly
  increment per build.
- Different on reload or between similar elements.

When you see randomized tokens, pivot to a stable signal:
- Substring/prefix match on a *partially* stable attribute:
  `[class^="Banner__"]`, `[id*="ad-container"]`.
- `:matches-attr()` with a regex for randomized attribute names/values.
- Structure: `.stable-parent:has(> .css-1a2b3c)` — but anchor the `:has()` on
  something stable, not two randomized tokens.
- Text or role.

Confirm on the live page: read the element's real attributes, and if possible
reload once to see which tokens change.

## Scope discipline

- Default to **hostname scope** (`example.com##…`). It's the single biggest
  breakage-prevention lever.
- Use **entity** scope (`example.*##…`) only when the layout is genuinely shared
  across TLDs of the same brand.
- Reserve **generic** (unscoped) rules for unambiguous, universally-bad patterns.
  When in doubt, scope it.

## Network vs cosmetic decision

- Separate request (script/img/iframe/media/xhr with its own URL) → **network
  filter**. Blocks the load, saves bandwidth, can't be re-injected by the site.
- First-party, inlined, or bundled into a needed request → **cosmetic** or
  **scriptlet**; you can't cleanly block it by URL without collateral.
- Element needs to be *absent* (site checks for it) → `:remove()` or, on Firefox,
  `##^` HTML filtering.

## Verify before finalizing

For a cosmetic/procedural selector, count matches on the live page:

```js
document.querySelectorAll('YOUR_PLAIN_CSS_PART').length
```

(For procedural chains, verify the plain-CSS portion, then reason about the
procedural narrowing.) You want it to hit the target(s) and nothing important.
For network rules, confirm the pattern matches the observed request URL and
enumerate what else on that host it would catch.

## Anti-patterns to avoid

- Anchoring to a randomized class "because it works right now".
- Over-broad generic rules (`##.container`, `##div[style]`).
- Deep `:nth-child()` ladders that assume a fixed DOM order.
- Blocking a first-party bundle URL that also carries needed functionality.
- Using `$important` or `:remove()` when a plain hide would do.
- Hiding an ad's shared ancestor that also contains real content.
