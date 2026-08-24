"""Generate lockup: snake mark left + wordmark right, one SVG (light + dark).

Mark embeds as nested <svg> scaled by viewBox; text reuses wordmark parts.
Ratio 0.85 (locked): mark height = MARK_FONT_RATIO x wordmark font size,
mark bottom sits MARK_BOTTOM_DROP below the wordmark baseline.

Run: uv run --with fonttools python3 gen_lockup.py
"""

import math
import re
from pathlib import Path

from gen_mark import dark as mark_dark
from gen_wordmark import (
    FONT,
    INK,
    INK_DARK,
    PY_BLUE,
    PY_BLUE_DARK,
    SIZE,
    load,
    wordmark_parts,
)

MARK = ".cache/leetcode-py-mark.svg"
MARK_FONT_RATIO = 0.85  # mark height vs wordmark font size
GAP_FONT_RATIO = 0.3  # mark-to-text gap vs font size
MARK_BOTTOM_DROP = (
    18  # mark bottom below baseline; between grey baseline (0) and py descenders (~33)
)
PAD = 2
CACHE = Path(".cache")


def mark_inner(src):
    vb = re.search(r'viewBox="([-\d. ]+)"', src).group(1)
    vw, vh = float(vb.split()[2]), float(vb.split()[3])
    inner = src[src.index(">") + 1 : src.rindex("</svg>")].rstrip()
    return vb, vw, vh, inner


def build(font, mark_src, ink, accent):
    parts, boxes, _ = wordmark_parts(font)
    swap = {INK: ink, PY_BLUE: accent}
    parts = [(d, swap.get(c, c)) for d, c in parts]
    tx0 = min(b[0] for b in boxes)
    tx1 = max(b[2] for b in boxes)
    ty0 = min(b[1] for b in boxes)
    ty1 = max(b[3] for b in boxes)

    mark_h = MARK_FONT_RATIO * SIZE
    gap = GAP_FONT_RATIO * SIZE
    vb, mvw, mvh, inner = mark_inner(mark_src)
    mark_w = mvw * mark_h / mvh

    mark_top = MARK_BOTTOM_DROP - mark_h
    text_dx = mark_w + gap - tx0

    x0 = min(0.0, text_dx + tx0)
    x1 = max(mark_w, text_dx + tx1)
    y0 = min(mark_top, ty0)
    y1 = max(mark_top + mark_h, ty1)
    vx0, vy0 = math.floor(x0 - PAD), math.floor(y0 - PAD)
    vx1, vy1 = math.ceil(x1 + PAD), math.ceil(y1 + PAD)
    w, h = vx1 - vx0, vy1 - vy0
    body = "\n".join(f'    <path d="{d}" fill="{c}"/>' for d, c in parts)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx0} {vy0} {w} {h}" '
        f'width="{w}" height="{h}" role="img" aria-label="leetcode-py logo">\n'
        f'  <svg x="0" y="{mark_top:.1f}" width="{mark_w:.1f}" '
        f'height="{mark_h:.1f}" viewBox="{vb}">\n'
        f"{inner}\n"
        "  </svg>\n"
        f'  <g transform="translate({text_dx:.1f} 0)">\n'
        f"{body}\n"
        "  </g>\n"
        "</svg>"
    )


def main():
    font = load(*FONT)
    mark_src = Path(MARK).read_text()
    CACHE.mkdir(exist_ok=True)
    for suffix, src, ink, accent in (
        ("", mark_src, INK, PY_BLUE),
        ("-dark", mark_dark(mark_src), INK_DARK, PY_BLUE_DARK),
    ):
        svg = build(font, src, ink, accent)
        out = CACHE / f"leetcode-py-lockup{suffix}.svg"
        out.write_text(svg + "\n")
        print(f"wrote {out} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
