"""Rasterize the snake mark: favicon set (.ico + .png), apple-touch-icon, avatar PNGs.

Mark viewBox is 140x156 (not square); icons must be, so render a transparent
square master and center the mark on it, then downscale.

Uses rsvg-convert (librsvg) -- cairosvg silently ignores SVG <mask>, which the
mark's eye holes and snake gap need. Requires: brew install librsvg

Run: uv run --with pillow python3 gen_pngs.py
"""

import subprocess
from pathlib import Path

from PIL import Image

CACHE = Path(".cache")
SRC = CACHE / "leetcode-py-mark.svg"

MASTER = 1024
FAVICON_PNG_SIZES = (16, 32, 48)
ICO_SIZES = (16, 32, 48)
APPLE_TOUCH = 180
AVATAR_SIZES = (256, 512)
APPLE_BG = "#FFFFFF"  # iOS composites black behind alpha, keep opaque


def rasterize(src: Path, out: Path, height: int) -> None:
    subprocess.run(["rsvg-convert", "-h", str(height), "-o", str(out), str(src)], check=True)


def master_png() -> Image.Image:
    tmp = CACHE / "leetcode-py-mark-master.png"
    # fit by HEIGHT: the mark is taller than wide (140x156), fitting by width
    # would crop the heads/tail in the square master
    rasterize(SRC, tmp, MASTER)
    img = Image.open(tmp).convert("RGBA")
    canvas = Image.new("RGBA", (MASTER, MASTER), (0, 0, 0, 0))
    canvas.paste(img, ((MASTER - img.width) // 2, (MASTER - img.height) // 2), img)
    tmp.unlink()
    return canvas


def save(master, size, name, bg=None):
    img = master.resize((size, size), Image.Resampling.LANCZOS)
    if bg:
        flat = Image.new("RGBA", img.size, bg)
        flat.alpha_composite(img)
        img = flat
    out = CACHE / name
    img.save(out)
    print(f"wrote {out} ({size}x{size})")


def main():
    CACHE.mkdir(exist_ok=True)
    master = master_png()

    for s in FAVICON_PNG_SIZES:
        save(master, s, f"favicon-{s}.png")
    save(master, APPLE_TOUCH, "apple-touch-icon.png", bg=APPLE_BG)
    for s in AVATAR_SIZES:
        save(master, s, f"leetcode-py-mark-{s}.png")

    ico = CACHE / "favicon.ico"
    master.save(ico, format="ICO", sizes=[(s, s) for s in ICO_SIZES])
    print(f"wrote {ico} ({'/'.join(map(str, ICO_SIZES))})")


if __name__ == "__main__":
    main()
