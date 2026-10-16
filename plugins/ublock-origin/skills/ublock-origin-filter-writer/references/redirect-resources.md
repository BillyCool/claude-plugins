# Redirect resources (`$redirect=` / `$redirect-rule=`)

Confirmed against uBO 1.74.0 by listing every file in
`src/web_accessible_resources/` directly (50 real resources; `README.txt`
excluded). These are actual bundled files uBO can substitute for a blocked
request — used with the network-filter options `$redirect=<token>` (implies a
block) or `$redirect-rule=<token>` (redirect without blocking; the request must
already be blocked by another filter).

```
||ads.example.com/banner.js^$script,redirect=noop.js
||ads.example.com/video.mp4^$media,redirect=noop-1s.mp4
```

Priority suffix, when more than one filter could redirect the same request:
`$redirect=noop.js:5` (higher number wins).

## Neutral / empty stand-ins

Use these to replace a blocked resource with an inert equivalent so the page
doesn't break waiting for something that will never load:

| Token | Use for |
|---|---|
| `1x1.gif`, `2x2.png`, `3x2.png`, `32x32.png` | Tracking pixels / ad images |
| `noop.js` | Any blocked script |
| `noop.css` | Blocked stylesheet |
| `noop.html` | Blocked frame/subdocument (alias commonly referred to as "noopframe") |
| `noop.json` | Blocked JSON endpoint |
| `noop.txt` | Blocked plain-text endpoint |
| `noop-0.1s.mp3`, `noop-0.5s.mp3` | Blocked short audio |
| `noop-1s.mp4` | Blocked video (e.g. preroll ads) |
| `noop-vast2.xml`, `noop-vast3.xml`, `noop-vast4.xml` | Blocked VAST ad-tag XML |
| `noop-vmap1.xml` | Blocked VMAP ad-tag XML |
| `empty` | Generic empty response body |
| `click2load.html` | Replace an embed with a click-to-load placeholder |

## Anti-adblock / library defusers

Swap a tracker or anti-adblock library for a harmless stub that satisfies the
page's `typeof` / method-existence checks without doing anything:

`nobab2.js`, `nofab.js`, `popads.js`, `popads-dummy.js`, `fingerprint2.js`,
`fingerprint3.js`, `ampproject_v0.js`, `noeval.js`, `noeval-silent.js`.

## Site/vendor script surrogates

Replace a specific analytics/ads vendor script with a stub implementing just
enough of its API surface that dependent page code doesn't throw:

`google-analytics_ga.js`, `google-analytics_analytics.js`,
`google-analytics_cx_api.js`, `google-analytics_inpage_linkid.js`,
`googletagmanager_gtm.js`, `googletagservices_gpt.js`,
`googlesyndication_adsbygoogle.js`, `google-ima.js`, `google-ima-dai.js`,
`doubleclick_instream_ad_status.js`,
`amazon_ads.js`, `amazon_apstag.js`, `adthrive_abd.js`, `nitropay_ads.js`,
`prebid-ads.js`, `outbrain-widget.js`, `scorecardresearch_beacon.js`,
`chartbeat.js`, `piano-analytics.js`, `sensors-analytics.js`, `hd-main.js`.

## Internal / debugging (not typically hand-written)

`dom-inspector.html`, `epicker-ui.html` — uBO's own element-picker/inspector
UI, exposed as web-accessible resources for the extension itself; not
meaningful as a `$redirect=` target in a hand-written rule.

## Worked examples

```
! Replace a preroll ad video with a 1-second no-op instead of leaving a broken player
||ads.example.com/preroll.mp4^$media,redirect=noop-1s.mp4,domain=example.com

! Neutralize Google Analytics but let the page's own ga() calls keep working
||google-analytics.com/analytics.js$script,redirect=google-analytics_analytics.js

! Replace an embedded iframe ad with a click-to-load placeholder
||ads.example.com/embed^$subdocument,redirect=click2load.html
```
