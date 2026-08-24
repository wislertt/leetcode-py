# leetcode-py brand

Source of truth for design decisions: concept, color system, tagline, design
constants. Generator tooling lives in [`README.md`](./README.md). Change a
value here first, then regenerate.

## Concept

The official LeetCode header mark recolored as the two Python snakes: the
L-diagonal is the blue snake, the open C-swoosh is the yellow snake. No gray
dash. Each snake is a centerline skeleton stroked at full body width (round
caps), derived once from the official outline (midpoint of its inner/outer
edges, least-squares cubics; reproduces it within ~0.6 units) — a faithful
reconstruction, not the raw official path data. Stroke terminals get
python-logo head profiles (flat face + quarter-circle jaw). Eyes and the
daylight band between the snakes are transparent holes, so the mark sits on
any surface. Transformative recolor of the LeetCode mark for personal OSS
use.

## Color system

Python palette only, never a third hue.

- `blue #3776AB` — Python blue (python.org): blue snake + `py` on light
- `yellow #FFD43B` — Python yellow: yellow snake on light
- `blue-dark #387EB8` / `yellow-dark #FFE052` — Python logo gradient light
  stops: snakes on dark surfaces (brighter, else they sink into the bg)
- `ink #646464` — Flux wordmark gray: `leetcode-` on light
- `ink-dark #B3B3B3` — `leetcode-` on dark

### Rules

- The two snake colors are fixed; dark surfaces only swap to the gradient
  light stops. Nothing else recolors
- Wordmark two-tone mirrors the python.org combined logo: neutral wordmark +
  blue accent. `py` is always Python blue, the hyphen stays ink gray
- Surfaces are near-neutrals, never pure `#000000`/`#FFFFFF`. OG card uses
  GitHub-dark `#0D1117` (where the README renders) and `#F8F9FB` on light

## Tagline

**Card** (OG card, README subtitle, anywhere the logo appears):

```
Modern Python LeetCode practice environment.
```

**Metadata** (`pyproject.toml` description, GitHub About) stays the longer
search-friendly version already in `pyproject.toml`:

```
Modern Python LeetCode practice environment with automated problem
generation, beautiful data structure visualizations, and comprehensive
testing
```

## Design constants

Locked 2026-08-22, eyeball-tuned on the skeleton geometry:

- Construction: skeleton strokes — one cubic centerline per snake, stroked
  40.77 wide (T28 over the original 12.77, half-width 20.385), round caps
- Centerline trims, both ends per snake: C head 12 / tail 12 (symmetric C
  opening), L head 10 / tail 32 (the official L hook reads overlong next to
  the thickened snakes)
- Heads: blue 1.15× half-width (pokes clear of the swoosh bulge), yellow
  1.0× (= cap radius, so the flat face runs tangent into the cap circle);
  one shape family at every length (flat face half + quarter-ellipse jaw),
  corner fillet 4.0
- Eyes: r7, pushed back from the tip along the head axis — blue 5, yellow 3
- Gap: 4.5 transparent daylight between the snakes; the cut hugs the blue
  silhouette (cap + head profile grown by the gap), not just a round cap
- Wordmark: Exo 2 wght 280, `leetcode-` ink + `py` Python blue
- Lockup: ratio 0.85 (mark height = 0.85× wordmark font size), gap 0.3× font size,
  mark bottom 18 px below the wordmark baseline (between the grey baseline
  and the py descenders)
- OG: Exo 2 wght 500 tagline, scattered faint dashes (the "-" dropped from
  the mark — it lives on as confetti); any orientation (±90°, dashes are
  symmetric), seed 8, each dash colored opposite its nearest neighbor so
  blue/yellow never clump
- Raster legibility: eyes and gap vanish ≤32px, snake silhouette still reads
  at 16px

## Asset usage

Assets are committed to `docs/img/brand/` and regenerated with `bake brand`.
README logo URLs point at `cdn.jsdelivr.net` (raw GitHub SVGs are blocked in
`<img>` on PyPI).
