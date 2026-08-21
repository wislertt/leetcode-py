"""Generate leetcode-py brand mark: LeetCode geometry x Python snakes.

Concept: the CURRENT official LeetCode mark (extracted from leetcode.com
header, 95x111 viewBox), recolored to the Python brand -- the L/diagonal
stroke is the blue snake, the big open swoosh is the yellow snake. No gray
dash.

Thickness comes from stroking the original outlines with their own fill color
(uniform dilation -- the shape is never redrawn). Stroke terminals become
snake heads: square inner corner + half-width flat face (blunt snout) on the
inner side, quarter-circle jaw on the outer side; body geometry untouched.
Eyes are transparent holes cut by mask, as is the daylight gap between the
two snakes (a halo of the diagonal cut out of the swoosh).

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

# Official LeetCode mark paths (leetcode.com header, 95x111 viewBox)
# Both tails end on a straight band segment (unit direction u below) closed
# by a two-cubic round cap; trimming = translating the cap assembly back
# along the band, so the tail stays round at every trim length.
SWOOSH_TAIL_U = (0.7775, 0.6288)
DIAGONAL_TAIL_U = (0.7143, 0.6999)

# The C part (swoosh) is the official path with its tail-cap points translated
# -- see swoosh_path() below. The L part keeps its exact official geometry
# (see diagonal_path()).

# Head/eye terminals (on the real geometry)
EYE_L_TOP = (54.8, 6.2)  # top cap of the diagonal (blue snake)
EYE_C_BOTTOM = (72.5, 87.5)  # bottom-right terminal of the swoosh (yellow)

# Snake-head caps (python-logo head profile): asymmetric. Inner side = square
# 90-degree corner + flat face spanning HALF the width (the blunt snout); outer
# side = quarter-circle arc (r = half width). Head width tracks stroke width
# (original outline + dilation). Eye sits at the head base (the terminal).
HEAD_CORNER = 4.0  # fillet softening the flat side's 90-degree corner
L_ORIG_W = 12.77  # original stroke width of L/diagonal and swoosh

# ---- Locked mark config (2026-08-21, eyeball-tuned; see BRAND.md) ----
EXPAND = 28.0  # snake thickness (uniform dilation; T28)
GAP = 4.5  # transparent daylight between the snakes
TAIL_TRIM = 8.0  # yellow tail pulled back along its band (head-tail breathing room)
TAIL_TRIM_L = 16.0  # blue tail pulled back along its band (0 = official length)
EYE_R = 8.0
EYE_L_PUSH = 5.0  # blue eye pushed back from the tip along the head axis
EYE_C_PUSH = 3.0  # yellow eye pushed back from the tip
HEAD_L_ANGLE = -50.0
HEAD_C_ANGLE = -45.0

HW = (L_ORIG_W + EXPAND) / 2  # dilated half-width = 20.385
HEAD_L_LEN = HW * 1.15  # blue head reach (pokes clear of the swoosh bulge)
HEAD_C_LEN = HW * 0.9  # yellow head reach


def diagonal_path(trim: float = 0.0) -> str:
    """The L part (fill white on leetcode.com), exact official geometry.

    `trim` pulls the bottom tail cap back along the band (DIAGONAL_TAIL_U):
    the cap's two cubics plus the straight edge endpoint translate together,
    exactly like the swoosh tail trim.
    """
    dx, dy = -DIAGONAL_TAIL_U[0] * trim, -DIAGONAL_TAIL_U[1] * trim

    def p(x: float, y: float) -> str:
        # %g-style: trim=0 must reproduce the official path's mixed precision
        # (some points carry 2-3 decimals, not 4).
        sx = f"{x + dx:.4f}".rstrip("0").rstrip(".")
        sy = f"{y + dy:.4f}".rstrip("0").rstrip(".")
        return f"{sx} {sy}"

    return (
        "M49.9118 2.02335C52.3173 -0.55232 56.3517 -0.686894 58.9228 1.72277"
        "C61.494 4.13244 61.6284 8.17385 59.2229 10.7495L16.4276 56.5729"
        "C11.7768 61.552 12.2861 69.5738 17.6453 74.8292"
        f"L{p(37.4088, 94.2091)}"
        f"C{p(39.9249, 96.6764)} {p(39.968, 100.72)} {p(37.505, 103.24)}"
        f"C{p(35.042, 105.761)} {p(31.0056, 105.804)} {p(28.4895, 103.337)}"
        "L8.72593 83.9567"
        "C-1.42529 74.0021 -2.43665 58.0741 7.1169 47.8463L49.9118 2.02335Z"
    )


def swoosh_path(trim: float = 0.0) -> str:
    dx, dy = -SWOOSH_TAIL_U[0] * trim, -SWOOSH_TAIL_U[1] * trim

    def p(x: float, y: float) -> str:
        return f"{x + dx:.4f} {y + dy:.4f}"

    return (
        "M68.0063 83.0664C70.5 80.5764 74.5366 80.5829 77.0223 83.0809"
        "C79.508 85.579 79.5015 89.6226 77.0078 92.1127L65.9346 103.17"
        "C55.7187 113.371 39.06 113.519 28.6718 103.513"
        "C28.6117 103.456 23.9861 98.9201 8.72653 83.957"
        "C-1.42528 74.0029 -2.43665 58.0749 7.11648 47.8464L24.9282 28.7745"
        "C34.4095 18.6219 51.887 17.5122 62.7275 26.2789"
        f"L{p(78.9048, 39.362)}"
        f"C{p(81.6444, 41.5776)} {p(82.0723, 45.5985)} {p(79.8606, 48.3429)}"
        f"C{p(77.6488, 51.0873)} {p(73.635, 51.5159)} {p(70.8954, 49.3003)}"
        "L54.7182 36.2173"
        "C49.0488 31.6325 39.1314 32.2622 34.2394 37.5006L16.4274 56.5727"
        "C11.7767 61.5522 12.2861 69.574 17.6456 74.8292"
        "C28.8516 85.8169 37.4869 94.2846 37.4969 94.2942"
        "C42.8977 99.496 51.6304 99.4184 56.9331 94.1234L68.0063 83.0664Z"
    )


def head(
    color: str,
    center: tuple[float, float],
    angle_deg: float,
    flat_sign: float,
    hw: float,
    length: float | None = None,
) -> str:
    """Snake-head cap at a stroke terminal: flat inner face, round outer jaw.

    `length` adjusts head length WITHOUT changing shape character: every
    length uses the same construction -- flat face on the top half,
    quarter-ellipse jaw on the bottom half -- so short and long heads stay
    one shape family. Back edge stays flush at the terminal; the dilated
    stroke always joins the neck.
    """
    ln = hw if length is None else length
    # Corner soften shrinks with a short head so the curve never eats the flat
    # side (keeps the corner proportion at every length).
    r = HEAD_CORNER if ln >= hw else HEAD_CORNER * ln / hw
    d = (
        f"M0 {hw:.1f}"
        f"L{ln - r:.1f} {hw:.1f}"
        f"A{r} {r} 0 0 0 {ln:.1f} {hw - r:.1f}"  # softened 90-degree corner
        f"L{ln:.1f} 0"  # flat face: top half of the width
        f"A{ln:.1f} {hw:.1f} 0 0 0 0 {-hw:.1f}"  # jaw: quarter ellipse
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


def dilate(d: str, color: str, expand: float) -> str:
    """Uniform dilation: stroke the outline with its own fill color."""
    if expand <= 0:
        return f'<path d="{d}" fill="{color}"/>'
    return (
        f'<path d="{d}" fill="{color}" stroke="{color}" stroke-width="{expand}" '
        'stroke-linejoin="round"/>'
    )


def mark(
    uid: str,
    expand: float = EXPAND,
    gap: float = GAP,
    head_l_len: float | None = HEAD_L_LEN,
    head_c_len: float | None = HEAD_C_LEN,
    tail_trim: float = TAIL_TRIM,
    tail_trim_l: float = TAIL_TRIM_L,
    eye_r: float = EYE_R,
    head_l_eye: float = EYE_L_PUSH,
    head_c_eye: float = EYE_C_PUSH,
) -> str:
    """Real LeetCode geometry; L=blue snake on top, C=yellow snake below.

    TRANSPARENT gap between the blue diagonal and yellow swoosh (Python-logo
    style): a halo of the diagonal, wider by 2*gap, is cut OUT of the yellow
    swoosh via mask subtraction -- the background shows through the gap band.
    Eyes are transparent holes too, cut from their snake. viewBox padded by
    the dilation so nothing crops.
    """
    pad = expand / 2 + gap + 4
    view = f"{-pad:.1f} {-pad:.1f} {95 + 2 * pad:.1f} {111 + 2 * pad:.1f}"
    hw = (L_ORIG_W + expand) / 2
    swoosh_cut = (
        f'<path d="{diagonal_path(tail_trim_l)}" fill="black" stroke="black" '
        f'stroke-width="{expand + 2 * gap}" stroke-linejoin="round"/>'
        + eye_hole(EYE_C_BOTTOM, HEAD_C_ANGLE, head_c_eye, eye_r)
    )
    diagonal_cut = eye_hole(EYE_L_TOP, HEAD_L_ANGLE, head_l_eye, eye_r)
    mask = (
        f"<defs>"
        f'<mask id="cutSwoosh-{uid}" maskUnits="userSpaceOnUse" '
        f'x="-60" y="-60" width="220" height="240">'
        f'<rect x="-60" y="-60" width="220" height="240" fill="white"/>' + swoosh_cut + "</mask>"
        f'<mask id="cutDiagonal-{uid}" maskUnits="userSpaceOnUse" '
        f'x="-60" y="-60" width="220" height="240">'
        '<rect x="-60" y="-60" width="220" height="240" fill="white"/>'
        + diagonal_cut
        + "</mask>"
        + "</defs>"
    )
    swoosh_body = dilate(swoosh_path(tail_trim), YELLOW, expand) + head(
        YELLOW, EYE_C_BOTTOM, HEAD_C_ANGLE, -1, hw, head_c_len
    )
    diagonal_body = dilate(diagonal_path(tail_trim_l), BLUE, expand) + head(
        BLUE, EYE_L_TOP, HEAD_L_ANGLE, 1, hw, head_l_len
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
    light = mark("brand")
    for name, svg in (("leetcode-py-mark.svg", light), ("leetcode-py-mark-dark.svg", dark(light))):
        out = CACHE / name
        out.write_text(svg + "\n")
        print(f"wrote {out} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
