# leetcode-py brand

Source of truth for design decisions: concept, color system, tagline, design
constants. Generator tooling lives in [`README.md`](./README.md). Change a
value here first, then regenerate.

## Concept

The official LeetCode header mark (real geometry, 95×111 viewBox) recolored as
the two Python snakes: the L-diagonal is the blue snake, the open C-swoosh is
the yellow snake. No gray dash. Uniform dilation thickens both strokes into
snake bodies; stroke terminals get python-logo head profiles (flat face +
quarter-circle jaw). Eyes and the daylight band between the snakes are
transparent holes, so the mark sits on any surface. Transformative recolor of
the LeetCode mark for personal OSS use.

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

Locked 2026-08-21, eyeball-tuned on the real geometry:

- Thickness: T28 — uniform dilation of 28 over the original 12.77 stroke
  (half-width 20.385)
- Heads: blue 1.15× half-width (pokes clear of the swoosh bulge), yellow
  0.9×; one shape family at every length (flat face top half +
  quarter-ellipse jaw), corner fillet 4.0 scaled down for short heads
- Yellow tail trimmed 8 units along its band — head/tail breathing room
- Blue tail trimmed 16 units along its band — the official L hook reads
  overlong next to the thickened snakes
- Eyes: r8, pushed back from the tip along the head axis — blue 5, yellow 3
- Gap: 4.5 transparent daylight between the snakes
- Wordmark: Exo 2 wght 280, `leetcode-` ink + `py` Python blue
- Lockup: ratio 1.0 (mark height = wordmark font size), gap 0.3× font size,
  mark optically centered on the x-height midline
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
