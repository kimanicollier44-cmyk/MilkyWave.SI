#!/usr/bin/env python3
"""Generate the MilkyWave.SI cover pic: 2736x912 PNG.

A milky-way wave of stars sweeping over a holographic Earth, with the
Knowledge Constellations (OECD / UNESCO / NIST / ISO / EU AI Act) as
orbiting satellites - the visual from Darion's recording.
Pure PIL, deterministic (seeded)."""
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 2736, 912
OUT = Path(__file__).resolve().parent / "assets" / "cover.png"


def font(size, bold=True):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    rng = random.Random(20261124)
    img = Image.new("RGB", (W, H), (4, 6, 22))
    draw = ImageDraw.Draw(img, "RGBA")

    # deep-space vertical gradient
    for y in range(H):
        t = y / H
        draw.line([(0, y), (W, y)], fill=(int(4 + 10 * t), int(6 + 8 * t), int(22 + 26 * t)))

    # milky way band: a broad sine wave of dense stars across the frame
    for _ in range(5200):
        x = rng.uniform(0, W)
        centre = H * 0.42 + 150 * math.sin(x / W * math.pi * 1.6 - 0.4)
        y = rng.gauss(centre, 95)
        if 0 <= y < H:
            r = rng.choice([1, 1, 1, 2, 2, 3])
            tone = rng.randint(140, 255)
            draw.ellipse([x - r, y - r, x + r, y + r],
                         fill=(tone - 30, tone - 10, tone, 255))
    # sparse field stars elsewhere
    for _ in range(900):
        x, y = rng.uniform(0, W), rng.uniform(0, H)
        draw.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(120, 140, 190, 255))
    # glowing wave crest line
    pts = [(x, H * 0.42 + 150 * math.sin(x / W * math.pi * 1.6 - 0.4))
           for x in range(0, W, 6)]
    draw.line(pts, fill=(90, 200, 255, 255), width=5)
    draw.line([(x, y + 14) for x, y in pts], fill=(60, 120, 255, 110), width=16)

    # holographic Earth, right side
    cx, cy, er = 2180, 470, 265
    draw.ellipse([cx - er, cy - er, cx + er, cy + er], fill=(10, 40, 90, 255),
                 outline=(90, 200, 255), width=6)
    for lat in (-150, -75, 0, 75, 150):
        ry = max(12, int(er * math.cos(math.radians(lat * 0.55))))
        draw.ellipse([cx - er, cy + lat - 8, cx + er, cy + lat + 8],
                     outline=(70, 160, 230, 160), width=2)
        draw.ellipse([cx - ry, cy - er, cx + ry, cy + er],
                     outline=(70, 160, 230, 120), width=2)
    # orbit ring + knowledge constellations
    draw.ellipse([cx - er - 95, cy - 95, cx + er + 95, cy + 95],
                 outline=(120, 220, 255, 150), width=3)
    for label, ang in zip(("OECD", "UNESCO", "NIST", "ISO", "EU AI ACT"),
                          (-50, 15, 265, 150, 215)):
        ox = cx + (er + 110) * math.cos(math.radians(ang))
        oy = cy + (er + 110) * math.sin(math.radians(ang))
        draw.ellipse([ox - 13, oy - 13, ox + 13, oy + 13], fill=(160, 230, 255),
                     outline=(255, 255, 255), width=2)
        draw.text((ox + 20, oy - 16), label, font=font(30), fill=(190, 235, 255))

    # title block, left
    draw.text((110, 250), "MilkyWave.SI", font=font(170), fill=(255, 255, 255))
    draw.text((116, 455), "Planetary Synthetic Intelligence", font=font(64),
              fill=(140, 215, 255))
    draw.text((116, 535), "Governance  •  Simulation  •  Holographic Operating System",
              font=font(42), fill=(200, 220, 245))
    draw.text((116, 640), "HOLOS-CIOS-EARTH  ∞   |   Scout Swarm  •  Digital Twin Earth  •  Ask All",
              font=font(36), fill=(150, 180, 220))
    draw.text((116, 800), "by Darion Kellar", font=font(34), fill=(120, 150, 190))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT} {img.size}")


if __name__ == "__main__":
    main()
