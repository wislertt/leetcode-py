# Branding generators

Tooling that generates the brand assets (snake mark, wordmark, lockup,
favicons, OG card). Design decisions — colors, tagline, constants — live in
[`BRAND.md`](./BRAND.md). Outputs are committed to `docs/img/brand/`.
Regenerate with `bake brand` (or the manual steps below) only when a design
constant changes, then review `preview.html`.

## Files

| File              | Produces                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------- |
| `gen_mark.py`     | `leetcode-py-mark.svg`, `leetcode-py-mark-dark.svg`                                                           |
| `gen_wordmark.py` | `leetcode-py-wordmark.svg`, `leetcode-py-wordmark-dark.svg`                                                   |
| `gen_lockup.py`   | `leetcode-py-lockup.svg`, `leetcode-py-lockup-dark.svg` (reads the generated mark)                            |
| `gen_pngs.py`     | `favicon.ico` + `favicon-{16,32,48}.png`, `apple-touch-icon.png` (white bg), `leetcode-py-mark-{256,512}.png` |
| `gen_og.py`       | `og-card-dark.png`, `og-card-light.png` (1200×630, brand surfaces + lockup + tagline + dash confetti)         |

## Regenerate

Run from this directory. Needs [fonttools](https://fonttools.readthedocs.io)
and [librsvg](https://gitlab.gnome.org/GNOME/librsvg) (pulled/built outside
Python by `uv`/brew):

```bash
cd scripts/branding
uv run python3 gen_mark.py
uv run --with fonttools python3 gen_wordmark.py
uv run --with fonttools python3 gen_lockup.py
uv run --with pillow python3 gen_pngs.py
uv run --with fonttools --with pillow python3 gen_og.py
mkdir -p ../../docs/img/brand
cp .cache/leetcode-py-*.svg .cache/leetcode-py-mark-*.png .cache/favicon* \
  .cache/apple-touch-icon.png .cache/og-card-*.png ../../docs/img/brand/
```

Generated files land in `.cache/` (gitignored). Dependency chain: lockup
imports wordmark parts and reads the generated mark, `gen_og.py` reads the
generated lockups. Run in the order above.

`gen_pngs.py` and `gen_og.py` rasterize with `rsvg-convert` — cairosvg
silently ignores SVG `<mask>`, which the mark's eye holes and snake gap need.
Requires system librsvg (`brew install librsvg`).

`preview.html` renders the `.cache/` outputs for side-by-side review. Serve:
`python3 -m http.server 8742` from this directory.

## Font license

`fonts/Exo2-var.ttf` is [Exo 2](https://fonts.google.com/specimen/Exo+2) by
Natanael Gama, licensed under the [SIL Open Font License
1.1](./OFL-Exo2.txt). Bundling the font with its license file satisfies the
license terms. The committed assets contain outlined paths only.
