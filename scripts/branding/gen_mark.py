"""Generate leetcode-py brand mark: LeetCode geometry x Python snakes.

Concept: the official LeetCode header mark recolored as the two Python
snakes -- the L/diagonal stroke is the blue snake, the big open swoosh is
the yellow snake. No gray dash.

Construction: SKELETON STROKES. Each snake is one cubic chain (centerline)
stroked at full body width with round caps, plus a python-logo head cap on
the endpoint. The centerlines were derived once from the official mark's
outline (midpoint between its inner/outer edges, least-squares cubic fit;
the official outline is a uniform 12.77-wide stroke, so the skeleton
reproduces it within ~0.6 units) and are locked below -- change trims by
editing the endpoints, everything else follows.

Eyes and the daylight band between the snakes are transparent holes cut by
mask, so the mark sits on any surface. The daylight gap hugs the blue
snake's actual silhouette (body cap + head profile grown by the gap), not
just a round cap.

Locked config lives in BRAND.md. Run: uv run python3 gen_mark.py
Outputs: .cache/leetcode-py-mark.svg + .cache/leetcode-py-mark-dark.svg
"""

import math
from pathlib import Path

CACHE = Path(".cache")

# Palette (light) -- python.org blues/yellows + Flux wordmark gray
BLUE = "#3776AB"  # Python blue
YELLOW = "#FFD43B"  # Python yellow
# Palette (dark) -- Python logo gradient light stops (brighter on dark bg)
BLUE_DARK = "#387EB8"
YELLOW_DARK = "#FFE052"

# ---- Locked mark config (2026-08-22, eyeball-tuned; see BRAND.md) ----
EXPAND = 28.0  # snake thickness over the original 12.77 stroke (T28)
GAP = 4.5  # transparent daylight between the snakes
HEAD_L_ANGLE = -50.0
HEAD_C_ANGLE = -45.0
HEAD_CORNER = 4.0  # fillet softening the flat side's 90-degree corner
L_ORIG_W = 12.77  # original stroke width of the official mark
HW = (L_ORIG_W + EXPAND) / 2  # half body width = 20.385
HEAD_L_LEN = HW * 1.15  # blue head reach (pokes clear of the swoosh bulge)
HEAD_C_LEN = HW * 1.0  # yellow head reach (= cap radius: face tangent, no kink)
EYE_R = 7.0
EYE_L_PUSH = 5.0  # blue eye pushed back from the tip along the head axis
EYE_C_PUSH = 3.0  # yellow eye pushed back from the tip

# Centerlines, head-end first for the C, top-end first for the L. Trimmed
# at BOTH ends: C head 12 / tail 12 (symmetric C opening), L head 10 /
# tail 32. Each endpoint is its head's terminal center.
SKELETON_C = (
    "M63.65 96.44"
    "C55.22 107.80 37.57 106.47 29.56 95.45"
    "C17.44 85.08 -3.33 67.24 12.82 51.09"
    "C19.79 44.17 25.74 36.10 33.44 30.00"
    "C43.87 23.27 57.09 27.77 64.94 36.28"
)
SKELETON_L = (
    "M47.26 14.21"
    "C43.43 18.31 39.61 22.41 35.78 26.50"
    "C29.17 33.58 22.56 40.66 15.95 47.74"
    "C7.67 54.13 3.69 66.27 9.99 75.42"
)
HEAD_C_BASE = (63.65, 96.44)  # C skeleton endpoint
HEAD_L_BASE = (47.26, 14.21)  # L skeleton endpoint

BODY_W = round(L_ORIG_W + EXPAND, 2)  # total stroke width = dilated body width


def head(
    color: str,
    center: tuple[float, float],
    angle_deg: float,
    flat_sign: float,
    hw: float,
    length: float | None = None,
) -> str:
    """Snake-head cap at a skeleton endpoint: flat inner face, round outer jaw.

    Flat face spans half the width (blunt snout), quarter-circle jaw the
    other half; corner fillet keeps the flat side's corner soft. Head width
    tracks the body half-width.
    """
    ln = hw if length is None else length
    r = HEAD_CORNER
    d = (
        f"M0 {hw:.1f}"
        f"L{ln - r:.1f} {hw:.1f}"
        f"A{r} {r} 0 0 0 {ln:.1f} {hw - r:.1f}"
        f"L{ln:.1f} 0"
        f"A{ln:.1f} {hw:.1f} 0 0 0 0 {-hw:.1f}"
        "Z"
    )
    cx, cy = center
    return (
        f'<g transform="translate({cx:.1f} {cy:.1f}) rotate({angle_deg}) '
        f'scale(1 {flat_sign})">'
        f'<path d="{d}" fill="{color}"/></g>'
    )


def eye_hole(cap: tuple[float, float], angle_deg: float, push: float, r: float) -> str:
    """Transparent eye hole, pushed back from the tip along the head axis."""
    ax, ay = math.cos(math.radians(angle_deg)), math.sin(math.radians(angle_deg))
    return (
        f'<circle cx="{cap[0] + ax * push:.1f}" cy="{cap[1] + ay * push:.1f}" '
        f'r="{r}" fill="black"/>'
    )


def mark(uid: str = "brand") -> str:
    """L=blue snake on top, C=yellow snake below, transparent gap and eyes.

    The daylight gap is the blue snake's silhouette (body + head) grown by
    GAP, cut out of the yellow stroke via mask subtraction; eyes are holes
    cut from each snake's body+head union. viewBox padded so nothing crops.
    """
    pad = EXPAND / 2 + GAP + 4
    view = f"{-pad:.1f} {-pad:.1f} {95 + 2 * pad:.1f} {111 + 2 * pad:.1f}"
    swoosh_cut = (
        f'<path d="{SKELETON_L}" fill="black" stroke="black" '
        f'stroke-width="{BODY_W + 2 * GAP:.2f}" stroke-linecap="round"/>'
        # gap follows the blue HEAD outline too, not just the round cap:
        # same head construction grown by GAP (hw+GAP, ln+GAP)
        + head("black", HEAD_L_BASE, HEAD_L_ANGLE, 1, HW + GAP, HEAD_L_LEN + GAP)
        + eye_hole(HEAD_C_BASE, HEAD_C_ANGLE, EYE_C_PUSH, EYE_R)
    )
    diagonal_cut = eye_hole(HEAD_L_BASE, HEAD_L_ANGLE, EYE_L_PUSH, EYE_R)
    mask = (
        "<defs>"
        f'<mask id="cutSwoosh-{uid}" maskUnits="userSpaceOnUse" '
        f'x="-60" y="-60" width="220" height="240">'
        f'<rect x="-60" y="-60" width="220" height="240" fill="white"/>{swoosh_cut}</mask>'
        f'<mask id="cutDiagonal-{uid}" maskUnits="userSpaceOnUse" '
        f'x="-60" y="-60" width="220" height="240">'
        '<rect x="-60" y="-60" width="220" height="240" fill="white"/>'
        + diagonal_cut
        + "</mask>"
        + "</defs>"
    )
    swoosh_body = (
        f'<path d="{SKELETON_C}" fill="none" stroke="{YELLOW}" '
        f'stroke-width="{BODY_W:.2f}" stroke-linecap="round"/>'
        + head(YELLOW, HEAD_C_BASE, HEAD_C_ANGLE, -1, HW, HEAD_C_LEN)
    )
    diagonal_body = (
        f'<path d="{SKELETON_L}" fill="none" stroke="{BLUE}" '
        f'stroke-width="{BODY_W:.2f}" stroke-linecap="round"/>'
        + head(BLUE, HEAD_L_BASE, HEAD_L_ANGLE, 1, HW, HEAD_L_LEN)
    )
    body = (
        mask
        + f'<g mask="url(#cutSwoosh-{uid})">'
        + swoosh_body
        + "</g>"
        + f'<g mask="url(#cutDiagonal-{uid})">'
        + diagonal_body
        + "</g>"
    )
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" fill="none">{body}</svg>'


def dark(mark_svg: str) -> str:
    """Dark-surface variant: swap to the Python logo gradient light stops."""
    return mark_svg.replace(BLUE, BLUE_DARK).replace(YELLOW, YELLOW_DARK)


def main() -> None:
    CACHE.mkdir(exist_ok=True)
    light = mark()
    for name, svg in (("leetcode-py-mark.svg", light), ("leetcode-py-mark-dark.svg", dark(light))):
        out = CACHE / name
        out.write_text(svg + "\n")
        print(f"wrote {out} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
