#!/usr/bin/env python3
"""Draw entry.png: one picture summing up the world news of Wednesday 25 November 2026.

All artwork is drawn from scratch with PIL primitives and text: no photos,
no copyrighted assets, no outlet logos. Run: python3 make_image.py

Stories (reported 25 Nov 2026 by Reuters/AP and other wires):
tankers hit mines in the Strait of Hormuz and Houthis struck Saudi oil
sites; the US proposed new tariffs and Wall Street slid; a US jury
convicted Huawei; Shenzhou-24 carried Pakistan's first astronaut to
Tiangong; Australia and the Solomon Islands signed a security treaty;
Russian strikes hit Odesa and Kyiv.
"""
import math

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
BACKDROP = (16, 20, 30)
CARD = (27, 34, 48)
CARD_EDGE = (70, 84, 108)
RED = (232, 76, 79)
AMBER = (245, 166, 35)
BLUE = (84, 150, 255)
TEAL = (64, 210, 190)
WHITE = (245, 247, 251)
MIST = (178, 192, 210)
LEAF = (124, 222, 158)
VIOLET = (178, 132, 255)

SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def face(size, bold=True):
    return ImageFont.truetype(SANS_BOLD if bold else SANS, size)


def wrapped(draw, text, fnt, max_width):
    lines, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def tanker(draw, cx, cy):
    draw.polygon([(cx - 72, cy), (cx + 72, cy), (cx + 56, cy + 26),
                  (cx - 56, cy + 26)], fill=AMBER)
    draw.rectangle([cx - 32, cy - 20, cx + 8, cy], fill=AMBER)
    draw.rectangle([cx + 26, cy - 13, cx + 48, cy], fill=AMBER)
    draw.ellipse([cx - 11, cy - 42, cx + 11, cy - 24], fill=RED)
    draw.polygon([(cx - 8, cy - 26), (cx + 8, cy - 26), (cx, cy - 44)], fill=RED)
    # naval mine
    mx, my = cx + 58, cy + 38
    draw.ellipse([mx - 9, my - 9, mx + 9, my + 9], fill=MIST)
    for ang in range(0, 360, 60):
        x2 = mx + 16 * math.cos(math.radians(ang))
        y2 = my + 16 * math.sin(math.radians(ang))
        draw.line([mx, my, x2, y2], fill=MIST, width=3)


def falling_chart(draw, cx, cy):
    pts = [(cx - 70, cy - 36), (cx - 32, cy - 12), (cx + 4, cy - 24),
           (cx + 38, cy + 8), (cx + 70, cy + 36)]
    draw.line(pts, fill=RED, width=7)
    for px, py in pts:
        draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=WHITE)
    draw.polygon([(cx + 70, cy + 44), (cx + 52, cy + 32), (cx + 57, cy + 56)], fill=RED)
    draw.text((cx - 66, cy - 52), "%", font=face(26), fill=AMBER)


def gavel(draw, cx, cy):
    draw.line([cx - 26, cy + 22, cx + 24, cy - 26], fill=AMBER, width=10)
    draw.line([cx - 22, cy - 22, cx + 30, cy + 30], fill=WHITE, width=7)
    draw.rectangle([cx - 40, cy + 32, cx + 24, cy + 40], fill=MIST)
    draw.rectangle([cx - 34, cy - 34, cx - 8, cy - 20], fill=BLUE)


def rocket(draw, cx, cy):
    draw.polygon([(cx, cy - 48), (cx - 14, cy - 10), (cx - 14, cy + 22),
                  (cx + 14, cy + 22), (cx + 14, cy - 10)], fill=WHITE)
    draw.ellipse([cx - 7, cy - 22, cx + 7, cy - 8], fill=BLUE)
    draw.polygon([(cx - 14, cy + 8), (cx - 30, cy + 30), (cx - 14, cy + 30)], fill=RED)
    draw.polygon([(cx + 14, cy + 8), (cx + 30, cy + 30), (cx + 14, cy + 30)], fill=RED)
    draw.polygon([(cx - 8, cy + 22), (cx + 8, cy + 22), (cx, cy + 48)], fill=AMBER)
    for sx, sy in ((cx - 52, cy - 30), (cx + 48, cy - 40), (cx + 56, cy + 6)):
        draw.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=TEAL)


def islands(draw, cx, cy):
    draw.polygon([(cx - 66, cy + 26), (cx - 34, cy - 6), (cx - 2, cy + 26)], fill=LEAF)
    draw.polygon([(cx + 6, cy + 26), (cx + 36, cy - 14), (cx + 68, cy + 26)], fill=TEAL)
    draw.line([cx - 70, cy + 34, cx + 70, cy + 34], fill=BLUE, width=5)
    # shield between the islands
    draw.polygon([(cx, cy - 44), (cx + 18, cy - 36), (cx + 18, cy - 14),
                  (cx, cy - 2), (cx - 18, cy - 14), (cx - 18, cy - 36)], fill=AMBER)
    draw.line([cx - 8, cy - 24, cx - 2, cy - 16, cx + 10, cy - 30], fill=BACKDROP, width=4)


def burning_block(draw, cx, cy):
    draw.rectangle([cx - 34, cy - 40, cx + 34, cy + 36], fill=MIST)
    for r in range(3):
        for c in range(3):
            x = cx - 24 + c * 20
            y = cy - 30 + r * 20
            draw.rectangle([x, y, x + 10, y + 12], fill=BACKDROP)
    draw.ellipse([cx - 12, cy - 58, cx + 12, cy - 38], fill=RED)
    draw.polygon([(cx - 8, cy - 40), (cx + 8, cy - 40), (cx, cy - 60)], fill=AMBER)


PANELS = [
    ("STRAIT OF HORMUZ", "Tankers hit mines, ships burn", "Iran says vessels struck mines in the strait; Houthis hit a Saudi refinery. Oil climbs.", tanker, RED),
    ("UNITED STATES", "New tariffs shake markets", "Washington proposes 20-40% duties; the Nasdaq slides 2% as the AI rout deepens.", falling_chart, AMBER),
    ("U.S. COURT", "Huawei convicted", "A jury finds the Chinese tech giant guilty of stealing trade secrets in its Iran-business trial.", gavel, BLUE),
    ("SPACE", "Pakistan's first astronaut", "Shenzhou-24 carries Muhammad Zeeshan Ali to China's Tiangong station, its first foreign crew member.", rocket, TEAL),
    ("PACIFIC", "Australia-Solomons treaty", "Canberra and Honiara sign a pact barring any foreign military base in the Solomon Islands.", islands, LEAF),
    ("UKRAINE", "Kyiv and Odesa struck", "Russian strikes kill two in Odesa and set a Kyiv apartment block ablaze, officials say.", burning_block, VIOLET),
]


def main():
    img = Image.new("RGB", (SIZE, SIZE), BACKDROP)
    draw = ImageDraw.Draw(img)

    # header
    draw.text((48, 36), "WEDNESDAY 25 NOVEMBER 2026", font=face(44), fill=WHITE)
    draw.text((48, 92), "The world in one picture", font=face(30, bold=False), fill=MIST)
    draw.line([48, 138, 976, 138], fill=AMBER, width=4)

    # 2 x 3 card grid
    x0, y0 = 48, 162
    cw, ch = 452, 240
    gap = 24
    for i, (kicker, headline, body, icon, accent) in enumerate(PANELS):
        col, row = i % 2, i // 2
        x = x0 + col * (cw + gap)
        y = y0 + row * (ch + gap)
        draw.rounded_rectangle([x, y, x + cw, y + ch], radius=18, fill=CARD, outline=CARD_EDGE, width=2)
        draw.rectangle([x, y, x + 8, y + ch], fill=accent)
        icon(draw, x + 92, y + 96)
        tx = x + 178
        draw.text((tx, y + 22), kicker, font=face(19), fill=accent)
        hy = y + 50
        for line in wrapped(draw, headline, face(27), cw - 196):
            draw.text((tx, hy), line, font=face(27), fill=WHITE)
            hy += 33
        by = hy + 8
        for line in wrapped(draw, body, face(19, bold=False), cw - 200):
            draw.text((tx, by), line, font=face(19, bold=False), fill=MIST)
            by += 25

    # footer strip
    fy = y0 + 3 * ch + 2 * gap + 18
    draw.rounded_rectangle([48, fy, 976, fy + 62], radius=14, fill=CARD, outline=CARD_EDGE, width=2)
    footer = "Also today: Sudan drone strikes kill 19  ·  Pope Leo XIV warns after COP31 fails  ·  Bangladesh raises garment pay 36%"
    for j, line in enumerate(wrapped(draw, footer, face(19, bold=False), 880)):
        draw.text((72, fy + 10 + j * 24), line, font=face(19, bold=False), fill=MIST)

    img.save("entry.png", optimize=True)


if __name__ == "__main__":
    main()
