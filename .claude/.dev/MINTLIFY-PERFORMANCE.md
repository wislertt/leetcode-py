# Mintlify Performance Playbook

Lessons from optimizing https://leetcode-py.wisl.dev (Lighthouse mobile 67, desktop 86). Applies to any Mintlify-hosted docs site: leetcode-py, zerv, bakefile, portfolio docs.

## TL;DR

Most of the page weight on a Mintlify-hosted site comes from the platform, not your content. You control a small slice: hero image hints, preconnect, badge images, and content-page images. Expect to gain a few points, not a green score. The ceiling is Mintlify's fixed client bundle.

## How to measure

Run Lighthouse locally against the live site. Same engine as PageSpeed Insights, no quota limits.

```bash
bunx lighthouse https://YOUR-DOCS-DOMAIN/ --output=json --output-path=/tmp/lh-mob.json \
  --only-categories=performance --chrome-flags="--headless=new" \
  --form-factor=mobile --screenEmulation.mobile
```

Then read the report:

```bash
python3 - << 'EOF'
import json
d = json.load(open('/tmp/lh-mob.json'))
a = d['audits']
m = a['metrics']['details']['items'][0]
print('score', round(d['categories']['performance']['score'] * 100))
print('FCP', a['first-contentful-paint']['displayValue'])
print('LCP', a['largest-contentful-paint']['displayValue'])
print('observed LCP', m['observedLargestContentfulPaint'], 'vs simulated', m['largestContentfulPaint'])
print('lcpLoadDelay', round(m.get('lcpLoadDelay', 0)), 'lcpLoadDuration', round(m.get('lcpLoadDuration', 0)))
print('TBT', a['total-blocking-time']['displayValue'], 'CLS', a['cumulative-layout-shift']['displayValue'])
nets = a['network-requests']['details']['items']
nets.sort(key=lambda r: -(r.get('transferSize') or 0))
print('total KB', sum(r.get('transferSize', 0) for r in nets) // 1024, 'requests', len(nets))
for r in nets[:15]:
    print(f"{r.get('transferSize', 0) / 1024:.0f}KB {r.get('resourceType')} {r.get('url', '')[:100]}")
EOF
```

Key readings:

- **observed LCP vs simulated LCP.** Lighthouse mobile uses simulated throttling (1.6Mbps, 4x CPU). On leetcode-py, observed LCP was 2.3s but simulated 8.4s. The gap is bandwidth contention and CPU, not server slowness.
- **lcpLoadDelay.** Time before the LCP resource even starts loading. High value means missing preconnect, missing fetchpriority, or late discovery in the HTML.
- **Heaviest requests.** On every Mintlify site expect the same platform items first: a ~700KB core JS chunk, preloaded woff2 fonts, one large render-blocking CSS file. Your own images come after those.

## What the platform costs you (fixed, not fixable from docs.json)

Measured on leetcode-py, free plan, theme `mint`:

| Item          | Cost                                | Detail                                                                                                                                   |
| ------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Core JS chunk | 175KB transfer / 683KB uncompressed | Contains loaders for posthog, plausible, fathom, kapa, Assistant, MCP. Ships even when none are configured.                              |
| Total JS      | ~700KB transfer                     | Lighthouse flags ~180KB unused.                                                                                                          |
| Fonts         | 3 woff2 files, 150KB, preloaded     | Preloaded in `<head>` on every page, highest priority, competes with LCP.                                                                |
| CSS           | 67KB, render-blocking               | ~750ms wasted per Lighthouse.                                                                                                            |
| LCP hints     | none                                | No preconnect to `mintcdn.com`, no fetchpriority on content images. Mintlify preloads both nav logo variants instead, one always hidden. |

Dial these down from the dashboard: you cannot. Checked every settings page (Search, Assistant, Add-ons, General). No bundle, font, or head-tag controls exist. `docs.json` has no `head` field, `search` config has no off switch. Tracked upstream: https://github.com/mintlify/docs/issues/7195

## What you control

### 1. LCP hints on the hero image (biggest own-side win)

In the page that has a large hero image (usually `index.mdx`), add a preconnect at the top of the file and priority attributes on the image:

```mdx
<link rel="preconnect" href="https://mintcdn.com" />

<img src="/img/brand/hero.png" loading="eager" fetchpriority="high" decoding="sync" />
```

Notes:

- Mintlify rewrites `/img/...` srcs to `mintcdn.com` with `auto=format` and a `srcset`, so the wire format is already WebP at the right width. Do not hand-convert to WebP; the CDN does it.
- The `<link>` inside MDX works because React 19 hoists resource-hint links to `<head>`. Verify after deploy; if a future Mintlify change strips it, the preconnect is lost silently.
- Verify the deployed HTML actually carries the hints:

```bash
curl -s https://YOUR-DOCS-DOMAIN/ | grep -o 'fetchpriority="high"' | head -1
curl -s https://YOUR-DOCS-DOMAIN/ | grep -c preconnect
```

### 2. Theme-variant images

If you show light/dark image variants hidden by CSS, both variants download. On leetcode-py that was 19KB total for the hero, small enough to keep the toggle-following behavior. If your variants are heavy (100KB+ each), consider accepting the mismatch and using `<picture>` with `media="(prefers-color-scheme: dark)"` so only one downloads, at the cost of breaking sync with the in-site theme toggle.

### 3. Third-party badge images

shields.io and codecov badges each open a separate origin connection (~560ms latency under mobile throttling). Keep them, they are tiny, but do not add more external images above the fold.

### 4. Content-page images

Large PNGs on subpages (up to 200KB+ in leetcode-py `docs/images/`) are fine for the homepage score but slow their own pages. The CDN converts format and resizes, so usually leave them. If a page feels slow, check that page with the same Lighthouse command.

### 5. Components and config that do NOT help

- Removing `CardGroup`/`Card`: they render server-side, no JS saved.
- Disabling features in dashboard: no such controls.
- Custom fonts via docs.json: platform fonts load regardless.
- Reverse-proxy caching tweaks: irrelevant unless you self-proxy `mintlify-assets`.

## Expected outcome

On leetcode-py, an A/B test with a local HTML proxy (patch in preconnect and fetchpriority, Lighthouse both versions) moved the score within noise: roughly 1 to 3 points at best. Run-to-run Lighthouse variance was plus or minus 6 points, larger than the fix. So:

- Make the changes, they are correct and free.
- Do not expect green (90+) while the site stays on Mintlify Cloud. The 683KB chunk, 150KB fonts, and 67KB CSS set the ceiling.
- If green is a hard requirement, that means moving off Mintlify or waiting on the upstream issue.

## Reference runbook for a new site

1. Run the Lighthouse command above. Record score, FCP, LCP, observed-vs-simulated LCP, total transfer.
2. Confirm the top transfers are the platform chunk, fonts, CSS. If something of your own tops the list, fix that first (usually an oversized hero PNG used directly in `og:image` position).
3. Add preconnect plus `fetchpriority="high"` to the hero image page. Deploy. Verify hints survive in the served HTML.
4. Re-run Lighthouse twice, before-and-after if you captured a baseline. Judge only the trend across multiple runs, single runs lie.
5. Optional: file or reference https://github.com/mintlify/docs/issues/7195 for the platform-side items.
