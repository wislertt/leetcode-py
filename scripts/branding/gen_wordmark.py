"""Generate leetcode-py wordmark: Exo 2 outlines -> SVG, two-color runs.

`leetcode-` in Flux-wordmark gray, `py` in Python blue -- mirrors the
python.org combined logo (neutral wordmark + blue accent, hyphen stays gray).

Run: uv run --with fonttools python3 gen_wordmark.py
"""

import math
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

TEXT_RUNS = ("leetcode-", "py")
SIZE = 160
INK = "#646464"  # `leetcode-` = Flux wordmark gray (official combined-logo fill)
INK_DARK = "#B3B3B3"  # `leetcode-` on dark surfaces
PY_BLUE = "#3776AB"  # `py` on light (python.org --color-blue)
PY_BLUE_DARK = "#387EB8"  # `py` on dark (Python logo gradient light stop)
PAD = 4
CACHE = Path(".cache")

FONT = ("fonts/Exo2-var.ttf", {"wght": 280})  # wordmark weight, python.org-close


def load(path, overrides):
    font = TTFont(path)
    if "fvar" in font:
        axes = {a.axisTag: a.defaultValue for a in font["fvar"].axes}
        axes.update(overrides)
        font = instantiateVariableFont(font, axes, inplace=True)
    return font


def run_paths(font, text, size, x0=0.0):
    """Glyph outlines for `text` at `size`, flat baseline y=0, pen x advances.

    Returns (path d, x_end, bounds) in svg space (y flipped, baseline at 0).
    """
    scale = size / font["head"].unitsPerEm
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    gs = font.getGlyphSet()
    ds = []
    x = x0
    bp = BoundsPen(None)
    for ch in text:
        gname = cmap[ord(ch)]
        rp = DecomposingRecordingPen(gs)
        gs[gname].draw(rp)
        t = (scale, 0, 0, -scale, x, 0)
        sp = SVGPathPen(None)
        for op in rp.value:
            getattr(TransformPen(sp, t), op[0])(*op[1])
        ds.append(sp.getCommands())
        for op in rp.value:
            getattr(TransformPen(bp, t), op[0])(*op[1])
        x += hmtx[gname][0] * scale
    return " ".join(ds), x, bp.bounds


def wordmark_parts(font):
    """Color-split wordmark: [(d, fill)], union ink box, x-height (svg space)."""
    parts = []
    boxes = []
    x = 0.0
    for text, color in zip(TEXT_RUNS, (INK, PY_BLUE), strict=True):
        d, x, (bx0, by0, bx1, by1) = run_paths(font, text, SIZE, x)
        parts.append((d, color))
        boxes.append((bx0, by0, bx1, by1))
    xh = font["OS/2"].sxHeight * (SIZE / font["head"].unitsPerEm)
    return parts, boxes, xh


def build(font, ink, accent):
    parts, boxes, _xh = wordmark_parts(font)
    swap = {INK: ink, PY_BLUE: accent}
    parts = [(d, swap.get(c, c)) for d, c in parts]
    xs0, ys0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
    xs1, ys1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
    vx0, vy0 = math.floor(xs0 - PAD), math.floor(ys0 - PAD)
    vx1, vy1 = math.ceil(xs1 + PAD), math.ceil(ys1 + PAD)
    w, h = vx1 - vx0, vy1 - vy0
    body = "\n".join(f'  <path d="{d}" fill="{c}"/>' for d, c in parts)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx0} {vy0} {w} {h}" '
        f'width="{w}" height="{h}" role="img" aria-label="leetcode-py wordmark">\n'
        f"{body}\n"
        "</svg>"
    )


def main():
    font = load(*FONT)
    CACHE.mkdir(exist_ok=True)
    for suffix, ink, accent in (("", INK, PY_BLUE), ("-dark", INK_DARK, PY_BLUE_DARK)):
        svg = build(font, ink, accent)
        out = CACHE / f"leetcode-py-wordmark{suffix}.svg"
        out.write_text(svg + "\n")
        print(f"wrote {out} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
