# Context: Docs Site SEO — leetcode-py

Companion to a future `tasks.md` (checklist). This file holds everything an agent needs to plan SEO work: verified live findings, known bug classes, transferable decisions from the bakefile repo's completed SEO pass, and the opportunities specific to this repo. Dates are absolute. Verify anything marked "verify" against the live site before acting — this reflects 2026-08-24 state.

## Project facts

- Repo: `github.com/wislertt/leetcode-py`, main branch `main`.
- Product: Python package that generates LeetCode practice environments (problem README, typed solution stub, parametrized pytest suite with 10+ cases, helpers, playground notebook) from JSON templates.
- PyPI package name: `leetcode-py-sdk` (NOT `leetcode-py`). CLI: `lcpy`.
- Scale: 307 problems under `leetcode/`, six collections (Grind 75, Grind, Blind 75, NeetCode 150, NeetCode 250, AlgoMaster 75).
- Author: Wisaroot Lertthaweedech (`wisl.dev`). Same author as bakefile (`bakefile.wisl.dev`).
- Docs: Mintlify site at `https://leetcode-py.wisl.dev` (custom domain; default deployment host `leetcode-py.mintlify.app`).

## Docs stack and conventions

- Mintlify, `docs/docs.json` at root of `docs/`. Theme `mint`. Site name `leetcode-py` (rendered title suffix is ` - leetcode-py`, 14 chars, so frontmatter titles must stay ≤~46 chars).
- `docs/skill.md` is hand-written, served raw at `/skill.md`, overrides Mintlify's auto-generated one. Do not delete, no MDX-only components in it.
- `markdown.instructions` in docs.json is injected into `llms.txt`, `llms-full.txt`, and Markdown page exports.
- **Catalog pages are GENERATED** by `scripts/gen_catalog.py` (`docs/catalog/*.mdx` carry "GENERATED — do not edit" headers). Any change to catalog content = edit the generator, not the mdx.
- Docs verification command: `bake docs-check` (runs `mintlify broken-links`). `bake docs` runs the dev server. Both defined in `bakefile.py`.
- Examples policy: docs examples are backed by tests, copy verbatim from tested sources.

## Verified live state (2026-08-24)

Checked directly against production:

- `robots.txt`: Mintlify default, clean. AI bots allowed, `Content-Signal: ai-train=yes, search=yes, ai-input=yes`. Do not replace.
- `sitemap.xml`: auto-generated, 21 pages, fresh `lastmod`.
- `llms.txt`: HTTP 200.
- Canonical: set globally (`https://leetcode-py.wisl.dev`).
- Organization schema with `sameAs` (GitHub, PyPI, wisl.dev).
- PyPI `[project.urls]` links to docs site (dofollow backlink).
- README links deeply into docs pages (collections, why-page, CLI guide).

## Known bugs (same class as bakefile, verified live 2026-08-24)

1. **Duplicated title tag.** Homepage renders `<title>leetcode-py - leetcode-py</title>` (page title + site name identical). Fix: give `docs/index.mdx` a keyword title, e.g. "LeetCode practice environments in Python" or similar; the suffix carries the brand.
2. **og:image resolves to wrong host.** Meta emits `https://leetcode-py.mintlify.app/img/brand/og-card-light.png` (default deployment host) because `seo.metatags.og:image` in docs.json is a relative path. Fix: absolute URL `https://leetcode-py.wisl.dev/img/brand/og-card-light.png`. Verify the custom domain serves `/img/brand/*` (bakefile's did).
3. **Product-label titles.** "Installation", "Quickstart", "Catalog", "Troubleshooting", "lcpy", "bakefile" (contributing) are labels, not search queries. Same fix pattern as bakefile: query-shaped titles + `sidebarTitle` for anything long.

## Measurement status (head start — mostly done)

- GSC **Domain property `wisl.dev` verified 2026-08-24** via DNS TXT at Spaceship registrar. A Domain property covers ALL subdomains, so `leetcode-py.wisl.dev` is already verified. No new verification needed.
- Bing Webmaster imported from GSC same day (covers Bing + DuckDuckGo + Yahoo).
- **Pending:** submit `https://leetcode-py.wisl.dev/sitemap.xml` in GSC (Sitemaps page) and confirm Bing copied it via import.
- **Pending:** GSC baseline (~2 weeks after sitemap submit): record indexed pages, impressions, queries.

## The big opportunity: 307 problem long-tail pages

This repo has an asset bakefile does not: 307 problems whose names are high-volume search queries ("two sum python", "longest substring without repeating characters python solution"). Current state:

- Catalog pages (`docs/catalog/blind-75.mdx` etc.) list problems but link them **offsite to GitHub** (`github.com/.../leetcode/two_sum/README.md`). All that content lives on github.com, not the docs domain. SEO value leaks offsite.
- `leetcode/<problem>/README.md` per problem exists in-repo with rich content.

Decision space (for the planning agent, not settled):

- Generate per-problem docs pages from the same JSON/templates (mirror `gen_catalog.py` approach). 307 pages of real content, each targeting "[problem name] python". Mintlify scales fine; nav would need a hidden or collapsed section (`seo.indexing: "all"` exists for pages outside navigation).
- Collection names are themselves high-volume keywords ("blind 75", "neetcode 150", "grind 75"). Those pages already exist — they mostly need title/description/intro strengthening, not creation.
- Risks to weigh: thin-content pages if problem pages are just stubs, maintenance coupling to problem JSON.

## Transferable decisions from the bakefile SEO pass (2026-08-24, same author, same Mintlify setup)

Applied and verified on bakefile.wisl.dev — reuse the patterns:

- Homepage/landing `title` frontmatter = keywords ("Python task runner, Makefile alternative"), site-name suffix carries brand. Never put the brand word in the title when the suffix already appends it.
- `sidebarTitle` frontmatter decouples long SEO titles from sidebar labels. Mintlify supports it natively.
- `og:image` must be absolute; relative resolves against the mintlify.app host.
- Query-shaped H2s on comparison pages ("Make vs bakefile") match "X vs Y" queries. FAQ sections only with genuinely matching Q&A content.
- Troubleshooting: split into per-error pages with the exact error string as title, hub page links all with error strings as anchor text. Behavioral notes stay on the hub.
- Internal linking: no orphan pages (footer/sidebar links don't count — content links only), first-mention descriptive anchors, both directions between related pages.
- Titles: unique, 50–60 chars rendered (including the ` - leetcode-py` suffix).
- Verification: `bake docs-check` after every docs edit; `curl -s <url> | grep '<title>'` for rendered-title checks after deploy.

## Off-repo SEO context (separate track, informational)

- No blog on the docs site (author decision). Articles will live on wisl.dev (planned Astro blog) linking into both docs sites. Cross-posting to Medium/dev.to only with canonical → wisl.dev.
- Backlinks create authority: awesome-list PRs, launch posts, GitHub topics, SO answers.
- Both docs sites are subdomains of wisl.dev; the GSC Domain property covers them all.

## Verification commands

```bash
bake docs-check                                              # broken links
curl -s https://leetcode-py.wisl.dev/ | grep '<title>'      # rendered title
curl -s https://leetcode-py.wisl.dev/ | grep 'og:image'     # og image host
curl -s https://leetcode-py.wisl.dev/sitemap.xml | grep -c '<loc>'  # page count
```

## Non-goals (decided, do not relitigate)

- No blog section on the docs site.
- No custom `robots.txt` / `sitemap.xml` (Mintlify defaults correct).
- No structured-data changes beyond Mintlify's automatic JSON-LD + existing organization block.
- Not moving docs off the subdomain.
