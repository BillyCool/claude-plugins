# Rule recipes

Starting points for common intents. Official examples are from Redirector's `README.md` / `help.html`
(v3.5.4). Adapt, then **always run `scripts/build-rules.mjs`** with `tests`; do not trust a recipe untested.

## Choosing wildcard vs regex

Default to **wildcard** when: swapping a host/scheme/path prefix, or capturing "everything after X".
Use **regex** when you need any of: optional parts (`(www\.)?`), alternation (`com|org`), character classes
or "single path segment" (`[^/]+`), non-capturing groups, matching a query parameter regardless of position,
or a partial pattern. Wildcard is preferred wherever it can do the job, because it is simpler and easier to
read and edit in the UI; regex is for the more complex tasks. Don't reach for regex needlessly: several
host variants can often be covered by a `*` in the host (e.g. `https://picclick.*/track/url/*/itm/*?*`
instead of a `[a-z.]+` regex).

## Official examples (verbatim intent)

| Intent | Type | Include | Redirect to |
|---|---|---|---|
| Static redirect | W | `http://example.com/foo` | `http://example.com/bar` |
| Query param (wildcard) | W | `http://example.com/index.php?id=*&a=b` | `http://example.com/printerfriendly.php?id=$1&a=b` |
| Query param (regex) | R | `http://example.com/index.php\?id=(\d+)&a=b` | `http://example.com/printerfriendly.php?id=$1&a=b` |
| Different folder (with exclude) | W | `http://example.com/category/*/index.php`, exclude `http://example.com/category/*/*/index.php` | `http://example.com/category/cat/index.php` |
| http -> https | W | `http://mail.google.com*` | `https://mail.google.com$1` |
| De-mobilize | R | `^(https?://)([a-z0-9-]*\.)m(?:obile)?\.(.*)` | `$1$2$3` |
| Strip AMP wrapper | R | `^(?:https?://)www.(?:google\|bing).com/amp/(?:s/)?(.*)` | `https://$1` |
| Unwrap DoubleClick | R | `^(?:https?://)ad.doubleclick.net/.*\?(http?s://.*)` | `$1` |
| YouTube Shorts -> watch | R, `appliesTo: main_frame + history` | `^(?:https?://)(?:www.)?youtube.com/shorts/([a-zA-Z0-9_-]+)(.*)` | `https://www.youtube.com/watch?v=$1$2` |
| Tracking-redirect unwrap | R, `urlDecode` | `^https?://foo\.com/redirect\.php\?url=(.*)` | `$1` |
| Proxy a site | R, `urlEncode` | `^(http://example\.com/.*)` | `http://proxysite.com?url=$1` |
| Base64 parameter | R, `base64decode` | `^https?://x\.com/go\?u=([^&]+)` | `$1` |

(In the README the AMP pattern is shown with `|`; in a Markdown table it is escaped as `\|`. In the rule
itself write a plain `|`.) The DoubleClick pattern in the README has the typo `http?s`; prefer `https?`.

## Patterns for typical requests

- **Domain swap, keep everything** (W): include `https://old.example.com/*`, redirect `https://new.example.com/$1`.
- **Swap host, keep path and query, any scheme** (R): `^https?://(?:www\.)?old\.com(/.*)?$` -> `https://new.com$1`.
- **All subdomains** (W): `https://*.reddit.com/*` -> `https://old.reddit.com/$2` would also catch
  `old.reddit.com` itself: add an exclude (`https://old.reddit.com/*`) or use the target host in the exclude.
  Pairs of include/exclude is the main reason excludes exist.
- **Query parameter anywhere** (R): `^https?://site\.com/search\?(?:.*&)?q=([^&]+)` -> `https://other.com/?q=$1`.
- **Strip tracking params** (R): `^(https?://[^?#]+)\?(?:utm_[^&#]*&?)+$` -> `$1` (only when the query is
  *all* trackers; per-parameter stripping of mixed queries needs several chained edits which Redirector's
  no-chaining rule forbids, so say so and offer the closest single-rule approximation).
- **Only a specific path** (W): `https://site.com/foo/*`; **everything except a path**: use an exclude.
- **Case**: regex flags are `gi`; never write `(?i)` and never try to make a rule case-sensitive.

## Anti-patterns to flag to the user

- Expecting `a -> b -> c` chaining (it won't).
- Redirecting `POST` form submits or login flows (only GET is touched).
- Wildcard without trailing `*` when the user wants "the whole site" (anchored `$`).
- Unanchored regex that also matches inside a query string (`...?next=https://example.com/foo`).
- Using `urlDecode` on non-ASCII text.
- `appliesTo` of many types with a broad pattern.
- Redirecting `main_frame` for a site that is an SPA: add `history`.
