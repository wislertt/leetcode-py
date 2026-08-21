"""Generate OG social card: brand surface bg, lockup, tagline, scattered dashes.

Dashes are the "-" dropped from the mark -- it lives on as confetti. Rasterized
with rsvg-convert (cairosvg silently ignores SVG <mask>, which the mark needs).
Requires: brew install librsvg

Run: uv run --with fonttools --with pillow python3 gen_og.py
"""

import math
import random
import re
import subprocess
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from gen_wordmark import load
from PIL import Image

CACHE = Path(".cache")

W, H = 1200, 630
TAGLINE = "Modern Python LeetCode practice environment."
TAG_FONT = ("fonts/Exo2-var.ttf", {"wght": 500})  # heavier than the 280 wordmark
LOCKUP_W = 700
TAG_W = 640
GAP = 56  # lockup bottom -> tagline cap top
SS = 2  # supersample render, LANCZOS back down for crisp edges
DASH_SEED = 8
DASHES = 20
DASH_SPREAD = 90.0  # max dash tilt in degrees; dashes are symmetric, 90 = any direction

# Brand surfaces (see BRAND.md -> Color system): near-neutrals, never pure
# black/white. Dark = GitHub-dark, where the README renders.
MODES = {
    "dark": {
        "bg": "#0D1117",
        "glow": "#161B22",
        "lockup": "leetcode-py-lockup-dark.svg",
        "tag_ink": "#B3B3B3",
        "dashes": ("#387EB8", "#FFE052"),  # python gradient light stops
    },
    "light": {
        "bg": "#F8F9FB",
        "glow": "#FFFFFF",
        "lockup": "leetcode-py-lockup.svg",
        "tag_ink": "#646464",
        "dashes": ("#3776AB", "#FFD43B"),  # python blues/yellows
    },
}


def lockup_inner(name):
    src = (CACHE / name).read_text()
    vb = re.search(r'viewBox="([-\d. ]+)"', src).group(1)
    vw, vh = float(vb.split()[2]), float(vb.split()[3])
    inner = src[src.index(">") + 1 : src.rindex("</svg>")].rstrip()
    return vb, vw, vh, inner


def text_paths(font, text, size):
    """Glyph outlines at `size`, flat baseline y=0. Returns (path d, bounds)."""
    scale = size / font["head"].unitsPerEm
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    gs = font.getGlyphSet()
    ds = []
    x = 0.0
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
    return " ".join(ds), bp.bounds


def blend(fg, bg, t):
    """Pre-composited mix of fg over bg at ratio t, as a hex string."""
    f = [int(fg[i : i + 2], 16) for i in (1, 3, 5)]
    b = [int(bg[i : i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(a * t + c * (1 - t)):02X}" for a, c in zip(f, b, strict=True))


def dashes(rng, safe, spread):
    """Scatter (x, y, len, th, angle) rounded dashes outside the content block."""
    x0, y0, x1, y1 = safe
    out = []
    tries = 0
    while len(out) < DASHES and tries < 500:
        tries += 1
        x, y = rng.uniform(24, W - 24), rng.uniform(24, H - 24)
        ln = rng.uniform(14, 30)
        th = rng.uniform(5, 9)
        ang = rng.uniform(-spread, spread)
        # rotated bounding half-extents of the ln x th bar, 12px margin on top
        a = math.radians(ang)
        hw = (ln * abs(math.cos(a)) + th * abs(math.sin(a))) / 2
        hh = (ln * abs(math.sin(a)) + th * abs(math.cos(a))) / 2
        if x0 - hw - 12 < x < x1 + hw + 12 and y0 - hh - 12 < y < y1 + hh + 12:
            continue
        near = any(
            (x - px) ** 2 + (y - py) ** 2 < ((ln + pln) * 0.9) ** 2 for px, py, pln, _, _ in out
        )
        if near:
            continue
        out.append((x, y, ln, th, ang))
    return out


def build(font, mode, spread=DASH_SPREAD, seed=DASH_SEED):
    m = MODES[mode]
    vb, vw, vh, inner = lockup_inner(m["lockup"])
    lw = LOCKUP_W
    lh = lw * vh / vw

    tag_d, (tx0, ty0, tx1, ty1) = text_paths(font, TAGLINE, 100)
    f = TAG_W / (tx1 - tx0)
    tag_h = f * (ty1 - ty0)  # full ink height: ascender through descender ("y")

    block_h = lh + GAP + tag_h
    top = (H - block_h) / 2
    lx, ly = (W - lw) / 2, top
    tag_base = top + lh + GAP + f * ty1  # baseline y
    tag_tx = (W - TAG_W) / 2 - f * tx0

    # keep dashes off the lockup + tagline block, 12px margin
    safe = (lx - 12, top - 12, lx + lw + 12, top + block_h + 12)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">',
        "  <defs>",
        '    <radialGradient id="glow" cx="0.5" cy="0.45" r="0.75">',
        f'      <stop offset="0%" stop-color="{m["glow"]}"/>',
        # plateau: flat bg from 55% out so card edges land exactly on the
        # page surface color, glow stays a center-only wash
        f'      <stop offset="55%" stop-color="{m["bg"]}"/>',
        f'      <stop offset="100%" stop-color="{m["bg"]}"/>',
        "    </radialGradient>",
        "  </defs>",
        f'  <rect width="{W}" height="{H}" fill="url(#glow)"/>',
    ]

    rng = random.Random(seed)
    pts = dashes(rng, safe, spread)
    cols: list[int] = []
    for i, (x, y, ln, th, ang) in enumerate(pts):
        # color = opposite of the nearest placed dash, so neighbors never match
        if cols:
            near_i = min(range(i), key=lambda k: (pts[k][0] - x) ** 2 + (pts[k][1] - y) ** 2)
            c = 1 - cols[near_i]
        else:
            c = 0
        cols.append(c)
        t = 0.45 - 0.008 * (ln - 14)  # bigger = fainter
        solid = blend(m["dashes"][c], m["bg"], t)
        lines.append(
            f'  <path d="M{x - ln / 2:.1f} {y:.1f}h{ln:.1f}" stroke="{solid}" '
            f'stroke-width="{th:.1f}" stroke-linecap="round" '
            f'transform="rotate({ang:.1f} {x:.1f} {y:.1f})"/>'
        )

    lines += [
        f'  <svg x="{lx:.1f}" y="{ly:.1f}" width="{lw:.1f}" height="{lh:.1f}" viewBox="{vb}">',
        inner,
        "  </svg>",
        f'  <g transform="translate({tag_tx:.1f} {tag_base:.1f}) scale({f:.4f})">',
        f'    <path d="{tag_d}" fill="{m["tag_ink"]}"/>',
        "  </g>",
        "</svg>",
    ]
    return "\n".join(lines)


def render(svg, name):
    src = CACHE / f"{name}.svg"
    out = CACHE / name
    src.write_text(svg)
    subprocess.run(
        ["rsvg-convert", "-w", str(W * SS), "-h", str(H * SS), "-o", str(out), str(src)],
        check=True,
    )
    img = Image.open(out).resize((W, H), Image.Resampling.LANCZOS)
    img.convert("RGB").save(out, optimize=True)
    src.unlink()
    print(f"wrote {out} ({W}x{H}, {out.stat().st_size // 1024}K)")


def main():
    CACHE.mkdir(exist_ok=True)
    tag_font = load(*TAG_FONT)
    for mode in MODES:
        render(build(tag_font, mode), f"og-card-{mode}.png")


if __name__ == "__main__":
    main()
