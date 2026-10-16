# Preparser directives

Confirmed against uBO 1.74.0 (`src/js/static-filtering-parser.js`,
`preparserIfTokens`). These are lines processed **before** filter parsing —
valid in the Filters tab, useful for writing conditional or reusable rules.

## Conditional blocks

```
!#if condition
... filters ...
!#else
... filters ...
!#endif
```

`condition` is a boolean expression over the tokens below, combined with `&&`,
`||`, `!` (negation), and parentheses.

### Recognized tokens

| Token | True when… |
|---|---|
| `ext_ublock` | Extension is uBlock Origin |
| `ext_ubol` | Extension is uBO Lite |
| `ext_devbuild` | Running a dev build |
| `env_brave` | Browser is Brave |
| `env_chromium` | Browser is Chromium-based |
| `env_edge` | Browser is Edge |
| `env_firefox` | Browser is Firefox — **the one you'll use most** |
| `env_legacy` | Legacy environment |
| `env_mobile` | Mobile browser |
| `env_mv3` | Running as Manifest V3 |
| `env_safari` | Browser is Safari |
| `cap_html_filtering` | HTML filtering (`##^`) is supported — true on Firefox MV2 |
| `cap_ipaddress` | IP-address matching fully supported |
| `cap_user_stylesheet` | User-stylesheet cosmetic injection supported |
| `false` | Always false (used to comment out a block conditionally) |

An `ext_abp`-prefixed compatibility token also exists for ABP-list interop;
irrelevant for hand-written My-filters rules.

### Example — Firefox-only rule block

```
!#if env_firefox
example.com##^script:has-text(adblock)
example.com##^responseheader(set-cookie)
!#else
! (no equivalent on this platform)
!#endif
```

Since this skill targets Firefox exclusively, `!#if env_firefox` /
`cap_html_filtering` guards are mostly unnecessary in **My filters** (you know
the target), but are worth using if the user shares the list elsewhere or
subscribes it publicly.

## Inclusion

```
!#include relative/path/to/file.txt
```

Imports another filter list file from the **same directory** as the including
list. Mainly relevant to maintained subscription lists, not the My-filters
textarea (which has no filesystem path) — include for completeness, but note
this to the user if they ask for it in My filters.

## Comments

Any line starting with `!` (not followed by `#`) is a comment and ignored by
the filtering engine — freely usable in My filters for notes:

```
! This rule stops the newsletter modal
example.com##.newsletter-modal
```

Lines starting with `[Adblock Plus ...]` or subscription metadata headers
(`! Title:`, `! Expires:`, `! Homepage:`, etc.) are meaningful for **published
subscription lists**, not for My filters — uBO ignores them there as ordinary
comments. No need to add them to a personal rule.
