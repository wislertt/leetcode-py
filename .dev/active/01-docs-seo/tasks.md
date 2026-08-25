# Tasks: Docs Site SEO — leetcode-py

Companion to `context.md` (facts, rationale, verification commands). Work phases in order. Decisions locked 2026-08-24:

- All 307 problem pages, 100% generated, no hand-written prose per problem
- Problem pages out of nav, `seo.indexing: "all"` in docs.json
- Problem page URLs: `/problems/<kebab-slug>/`
- Collection head terms ("blind 75") = strengthen only, not chase
- Non-goals in `context.md` stand

## Phase 0 — Measurement setup (do first)

- [x] Submit `https://leetcode-py.wisl.dev/sitemap.xml` in GSC (Sitemaps page, Domain property `wisl.dev`) — done 2026-08-24
- [x] Confirm Bing Webmaster copied sitemap via GSC import — done 2026-08-24
- GSC state 2026-08-24: sitemap Success (21 URLs), 0 indexed, homepage "Crawled - currently not indexed" (canonical correct, crawl clean). Clicked "Request indexing" on homepage (priority crawl queue). Baseline numbers on 2026-09-07 should reflect this
- [ ] Record GSC baseline snapshot on **2026-09-07** (~2 weeks): indexed pages, impressions, queries (where to record: append to this file, section at bottom)

## Phase 1 — Bug fixes (bounded)

- [x] `docs/index.mdx`: keyword title, ≤46 chars, no brand word (suffix adds it). Done 2026-08-24: "LeetCode Practice Environments in Python". Post-deploy: verify rendered `<title>` no longer duplicates
- [x] `docs/docs.json`: `seo.metatags.og:image` → absolute. Done 2026-08-24. `/img/brand/og-card-light.png` verified serving on custom domain (HTTP 200) before switching
- [x] Query-shaped titles + `sidebarTitle` for label pages. Done 2026-08-24 (catalog/index moved to Phase 3, generated file):
    - `getting-started/installation` → "Install the lcpy CLI via pip or uv"
    - `getting-started/quickstart` → "lcpy Quickstart: First Problem in 5 Commands"
    - `getting-started/why-leetcode-py` → "LeetCode Practice Environment vs a Bare Editor"
    - `troubleshooting/index` → "Fixing lcpy Setup and Generation Errors"
    - `cli/lcpy` → "lcpy CLI: Generate and List Problems"
    - `cli/collections` → "Blind 75, Grind 75, NeetCode and Others"
    - `contributing/problem-creation` → "Add a New LeetCode Problem End to End"
    - `contributing/bakefile` → "Contributor Reference: bakefile Tasks"
- [x] `bake docs-check` passed 2026-08-24 (no broken links)
- [ ] Post-deploy `curl` checks: homepage title, og:image host on all pages

## Phase 2 — Tooling niche (repo already ranks #4-10 for these queries)

- [x] Retitle/strengthen `docs/practice/testing.mdx`. Done 2026-08-24: "LeetCode Python Test Cases with pytest" (38 chars, renders 52), sidebarTitle Testing, query-shaped description + intro split pointing to the local page
- [x] New guide page `docs/practice/test-locally.mdx` (in nav, Practice group, after problem-anatomy): "Test LeetCode Solutions Locally with pytest" (43 chars, renders 57), sidebarTitle "Test locally". All output blocks captured from a real `lcpy gen -n 1` run in a temp dir (red 15 failed/3 passed, green 18 passed, `-k` 1 passed/17 deselected, root-run all-problems)
- [x] Interlinks: test-locally <-> testing, -> problem-anatomy, -> cli/lcpy, -> cli/collections, -> catalog; inbound links from quickstart step 3, cli/lcpy, why-leetcode-py "The loop"
- [x] `bake docs-check` passed 2026-08-24. Post-deploy title checks pending (see Phase 5)

## Phase 3 — Collection page strengthening (edit `scripts/gen_catalog.py`, never the mdx)

- [x] Query-shaped frontmatter per collection. Done 2026-08-24. Titles (all ≤46, unique, generator asserts both; `sidebarTitle` carries the old nav label):
    - grind-75 "Grind 75 in Python with Tested Solutions", blind-75 / neetcode-150 / neetcode-250 / neetcode / algo-master-75 same pattern
    - grind: "Grind Collection in Python: Tested Solutions"
    - catalog/index: "LeetCode Problem Catalog: All Collections" / sidebarTitle Catalog
    - catalog/all: "All LeetCode Problems in Python with Tests" / sidebarTitle All Problems
    - Descriptions rewritten query-shaped: "All {n} problems in the {list} list: each generates a tested Python practice environment..."
- [x] Two-sentence keyword intro per collection in `COLLECTION_INTRO` (what the list is + tested environments; `lcpy gen -t <tag>` block stays directly below). neetcode-250 intro notes coverage still growing
- [x] `catalog/neetcode.mdx` stays out of nav (hidden-page pattern untouched; docs.json nav unchanged)
- [x] Regenerated 9 pages, `bake docs-check` passed, `gen_catalog.py --check` no drift, ruff + ty clean. Post-deploy title checks pending (Phase 5)

## Phase 4 — Problem pages (new generator, biggest chunk)

- [x] New `scripts/gen_problems.py` — done 2026-08-25. PoC on two_sum first, then all 310 (catalog grew from 307):
    - Slug: kebab-case (`two_sum` → `/problems/two-sum/`)
    - Title: tiered formula ("X Python Solution with Tests" → "X Python Solution" → bare name → word-boundary truncate), uniqueness + ≤46 asserted
    - Descriptions standalone (no title repeat), ≤120 chars asserted
    - Body: intro + `lcpy gen` CTA (both `-n` and `-s`, snake_case name) / Problem (statement, examples, constraints, follow-up) / Solution verbatim / Complexity table / Tags → catalog links
    - Executed pytest output dropped (user decision: not useful info). Case count lives in intro CTA sentence; CI backs the "passes" claim; generator runs no pytest = fast + fully deterministic
    - `mdx_escape` on all JSON prose (`<` `{` `}` outside fences/inline code); `validate_mdx` post-render assert catches future breakers at gen time
    - Data fix: walls_and_gates example had unbalanced nested fences (5 markers) + stray trailing backtick — fixed in JSON + README
- [x] `docs/docs.json`: `seo.indexing: "all"` added 2026-08-25
- [x] `gen_catalog.py`: Problem column → `/problems/<slug>/`; GitHub solution.py stays as the one secondary link per row
- [x] Bakefile: `bake docs-problems` task added next to `docs-catalog`
- [x] Regenerated everything. Checks passed 2026-08-25: `mintlify broken-links` clean, both `--check` modes no drift, all 310 problems linked from catalog/all. Post-deploy: llms.txt < 100k, sitemap ~331 URLs (Phase 5)
- Note: `bake check-consistency` force-regenerates leetcode/ from templates and clobbered implemented solutions (recovered via git restore). Never run it casually; JSON+README edits must be applied to both manually

## Phase 5 — Post-deploy verification

- [ ] Immediately after deploy: `curl` rendered titles on ~5 sample problem pages, og:image host, sitemap count
- [ ] GSC checkpoint **2026-09-21** (week 4, monitor only, no gate): index coverage rate, impressions by query, "Crawled - not indexed" volume. If problem pages show mass canonical-loss signals (inspect URL tool pointing at github.com) or soft-404, fix template and regenerate
- [ ] Append findings + numbers to this file

## GSC snapshots

(baseline 2026-09-07 and week-4 2026-09-21 numbers go here)
