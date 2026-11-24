#!/usr/bin/env python3
"""Render the front page of 'The World Today' for Tuesday, 24 November 2026.

A 1024x1024 newspaper front page drawn with Pillow: serif masthead, one
lead story and five more world stories, each with a small pictogram drawn
in code. No photos, no downloaded assets, no network calls.

Stories, each checked against wire reporting dated 24 November 2026:
  1. LEAD  Nvidia reinstates Jensen Huang as CEO; shares jump 31%
  2. Indonesia: candy-factory fire in Cikande, 24 dead, ~30 missing
  3. Ukraine: Russian strikes on the Kyiv region kill at least 12
  4. Climate: COP31 in Antalya ends with no deal on fossil fuels
  5. Sport: Alcaraz beats Zverev to win his first ATP Finals title
  6. Chess: Gukesh v Sindarov, Game 1 of the world title match, Geneva
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

PAGE_W, PAGE_H = 1024, 1024
EDGE = 40
RIGHT_EDGE = PAGE_W - EDGE

CREAM = (247, 242, 231)
INK = (28, 32, 40)
TEAL = (14, 79, 79)
RUST = (139, 30, 30)
GOLD = (176, 141, 46)
MUTED = (96, 92, 82)
FAINT = (196, 186, 158)

DEJAVU = "/usr/share/fonts/truetype/dejavu"


def load_font(filename, size):
    return ImageFont.truetype(os.path.join(DEJAVU, filename), size)


def serif_bold(size):
    return load_font("DejaVuSerif-Bold.ttf", size)


def serif(size):
    return load_font("DejaVuSerif.ttf", size)


def sans_bold(size):
    return load_font("DejaVuSans-Bold.ttf", size)


def sans(size):
    return load_font("DejaVuSans.ttf", size)


def split_lines(draw, text, font, width):
    """Greedy word wrap returning lines that fit inside width."""
    lines, current = [], ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_para(draw, x, y, text, font, width, leading, color=INK):
    """Draw a wrapped paragraph; return the y below its last line."""
    for line in split_lines(draw, text, font, width):
        draw.text((x, y), line, font=font, fill=color)
        y += leading
    return y


def rule(draw, y, width=1, color=INK, x0=EDGE, x1=RIGHT_EDGE):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


# ------------------------------------------------------------------ pictograms

def draw_chip(draw, cx, cy, size, color=TEAL):
    """A microchip: square body, pins, inner square."""
    half = size
    draw.rectangle([cx - half, cy - half, cx + half, cy + half],
                   outline=color, width=5)
    draw.rectangle([cx - half // 2, cy - half // 2,
                    cx + half // 2, cy + half // 2], fill=color)
    for k in range(-1, 2):
        off = k * half * 2 // 3
        draw.line([(cx + off, cy - half - 12), (cx + off, cy - half)],
                  fill=color, width=4)
        draw.line([(cx + off, cy + half), (cx + off, cy + half + 12)],
                  fill=color, width=4)
        draw.line([(cx - half - 12, cy + off), (cx - half, cy + off)],
                  fill=color, width=4)
        draw.line([(cx + half, cy + off), (cx + half + 12, cy + off)],
                  fill=color, width=4)


def draw_factory(draw, cx, cy, size, color=TEAL):
    """Factory with chimney, smoke rings and a flame in the window."""
    # chimney
    draw.rectangle([cx + size - 30, cy - size + 16, cx + size - 10, cy + 22],
                   fill=color)
    for ox, oy, rr in ((2, -size + 12, 6), (10, -size + 2, 7),
                       (20, -size - 8, 8)):
        draw.ellipse([cx + size - 30 + ox - rr, cy + oy - rr,
                      cx + size - 30 + ox + rr, cy + oy + rr],
                     outline=MUTED, width=2)
    # sawtooth-roof hall
    draw.polygon([(cx - size, cy + 22), (cx - size, cy - 4),
                  (cx - size + 26, cy - 24), (cx - size + 26, cy - 4),
                  (cx - size + 52, cy - 24), (cx - size + 52, cy - 4),
                  (cx + size - 34, cy - 4), (cx + size - 34, cy + 22)],
                 fill=color)
    # flame in the windows
    draw.polygon([(cx - 24, cy + 20), (cx - 15, cy - 4), (cx - 6, cy + 20)],
                 fill=GOLD)
    draw.polygon([(cx + 0, cy + 20), (cx + 9, cy - 2), (cx + 18, cy + 20)],
                 fill=RUST)


def draw_blast(draw, cx, cy, size, color=TEAL):
    """Apartment block hit by a blast: cracked wall and burst lines."""
    draw.rectangle([cx - size, cy - size + 8, cx + size, cy + size - 6],
                   outline=color, width=4)
    for row in range(3):
        yy = cy - size + 26 + row * 18
        for col in range(3):
            xx = cx - size + 12 + col * 24
            draw.rectangle([xx, yy, xx + 12, yy + 10], fill=color)
    # crack down the middle
    draw.line([(cx + 6, cy - size + 8), (cx - 4, cy - 8),
               (cx + 8, cy + 8), (cx - 2, cy + size - 6)],
              fill=RUST, width=3)
    # burst rays (kept short so they stay clear of the kicker above)
    for ang in range(0, 360, 45):
        rad = math.radians(ang)
        x0 = cx + int(math.cos(rad) * (size + 6))
        y0 = cy + int(math.sin(rad) * (size + 6))
        x1 = cx + int(math.cos(rad) * (size + 16))
        y1 = cy + int(math.sin(rad) * (size + 16))
        draw.line([(x0, y0), (x1, y1)], fill=GOLD, width=3)


def draw_globe(draw, cx, cy, radius, color=TEAL):
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                 outline=color, width=4)
    draw.ellipse([cx - int(radius * 0.45), cy - radius,
                  cx + int(radius * 0.45), cy + radius],
                 outline=color, width=3)
    draw.line([(cx, cy - radius), (cx, cy + radius)], fill=color, width=2)
    for frac in (-0.55, 0.55):
        yy = cy + int(radius * frac)
        half = int(math.sqrt(max(radius * radius - (radius * frac) ** 2, 0)))
        draw.line([(cx - half, yy), (cx + half, yy)], fill=color, width=2)
    # a crack across the globe: the talks broke down
    draw.line([(cx - radius + 8, cy + radius - 14),
               (cx - 6, cy + 6), (cx + 10, cy - 4),
               (cx + radius - 6, cy - radius + 12)],
              fill=RUST, width=3)


def draw_trophy(draw, cx, cy, size, color=TEAL):
    """A cup with two handles on a plinth."""
    draw.polygon([(cx - size, cy - size), (cx + size, cy - size),
                  (cx + size - 12, cy + 2), (cx - size + 12, cy + 2)],
                 fill=color)
    draw.arc([cx - size - 22, cy - size + 2, cx - size + 10, cy + 12],
             90, 270, fill=color, width=4)
    draw.arc([cx + size - 10, cy - size + 2, cx + size + 22, cy + 12],
             270, 90, fill=color, width=4)
    draw.rectangle([cx - 6, cy + 2, cx + 6, cy + size - 12], fill=color)
    draw.rectangle([cx - size + 4, cy + size - 12, cx + size - 4, cy + size],
                   fill=GOLD)
    # ball on top
    draw.ellipse([cx - 9, cy - size - 12, cx + 9, cy - size + 6],
                 fill=GOLD)


def draw_knight(draw, cx, cy, size, color=TEAL):
    """Chess knight glyph in a ring."""
    draw.ellipse([cx - size, cy - size, cx + size, cy + size],
                 outline=color, width=4)
    glyph = "\u265e"
    fnt = sans(size * 2 - 6)
    w = draw.textlength(glyph, font=fnt)
    bbox = draw.textbbox((0, 0), glyph, font=fnt)
    draw.text((cx - w / 2, cy - (bbox[3] - bbox[1]) / 2 - bbox[1]),
              glyph, font=fnt, fill=color)


# ------------------------------------------------------------------ page

def build_page():
    img = Image.new("RGB", (PAGE_W, PAGE_H), CREAM)
    d = ImageDraw.Draw(img)

    # ---- header ----
    rule(d, 30, 2)
    d.text((EDGE, 40), "TUESDAY, 24 NOVEMBER 2026", font=sans_bold(18),
           fill=INK)
    tag = "WORLD EDITION  \u2022  No. 328"
    d.text((RIGHT_EDGE - d.textlength(tag, font=sans_bold(16)), 42),
           tag, font=sans_bold(16), fill=MUTED)

    name = "The World Today"
    name_w = d.textlength(name, font=serif_bold(88))
    d.text(((PAGE_W - name_w) / 2, 66), name, font=serif_bold(88), fill=INK)

    motto = "S I X   S T O R I E S   F R O M   A R O U N D   T H E   G L O B E"
    motto_w = d.textlength(motto, font=sans_bold(15))
    d.text(((PAGE_W - motto_w) / 2, 164), motto, font=sans_bold(15),
           fill=TEAL)

    rule(d, 192, 3)
    rule(d, 198, 1)

    # ---- lead story: Nvidia ----
    y = 214
    d.text((EDGE, y), "LEAD STORY  \u2014  MARKETS", font=sans_bold(17),
           fill=RUST)
    y += 30
    for line in ("Huang is back: Nvidia chief",
                 "reinstated as shares soar 31%"):
        d.text((EDGE, y), line, font=serif_bold(37), fill=INK)
        y += 45
    y += 4
    y = draw_para(
        d, EDGE, y,
        "Eleven days after he resigned, Jensen Huang was reinstated as "
        "Nvidia's chief executive on Monday, the board unanimous after "
        "talks with US officials. Shares jumped 31%, their best day since "
        "2003, and the Nasdaq rallied 6.5%.",
        sans(19), 610, 25)
    draw_chip(d, 852, 316, 76)

    rule(d, 446, 2, FAINT)

    # ---- grid: four stories, two columns by two rows ----
    grid = [
        ("DISASTER", "Factory fire kills 24 in Java",
         "Rescuers recovered 24 body bags from the burnt candy factory "
         "in Cikande, Banten, by Monday. About 30 people are still "
         "missing; an air-conditioner short circuit is suspected.",
         draw_factory, (42, 52, 40)),
        ("UKRAINE", "Strikes kill at least 12 near Kyiv",
         "Russian drones hit a five-storey block in Dymer, a supermarket "
         "in Vyshneve and a home in Bila Tserkva. Rescuers are still "
         "searching the rubble for survivors.",
         draw_blast, (42, 48, 34)),
        ("CLIMATE", "COP31 ends with no deal at all",
         "After 44 hours of overtime in Antalya, the climate talks closed "
         "with no agreement. The EU rejected a draft that made no mention "
         "of fossil fuels. It was the longest COP ever.",
         draw_globe, (46, 46, 44)),
        ("SPORT", "Alcaraz wins first ATP Finals",
         "Carlos Alcaraz beat world No. 1 Alexander Zverev 6-2, 7-6(7) in "
         "Turin on Sunday. At 23, he is only the fourth man to hold all "
         "four Slams and the Finals title.",
         draw_trophy, (40, 48, 32)),
    ]
    col_w = 457
    col_x = [EDGE, EDGE + col_w + 30]
    row_y = [462, 652]
    for i, (kicker, head, body, pict, (px, py, ps)) in enumerate(grid):
        x = col_x[i % 2]
        yy = row_y[i // 2]
        d.text((x, yy), kicker, font=sans_bold(15), fill=RUST)
        yy += 24
        pict(d, x + px, yy + py, ps)
        tx = x + 104
        for line in split_lines(d, head, serif_bold(23), col_w - 104):
            d.text((tx, yy), line, font=serif_bold(23), fill=INK)
            yy += 28
        yy += 6
        draw_para(d, tx, yy, body, sans(16), col_w - 104, 21)
        if i % 2 == 0:
            d.line([(x + col_w + 15, row_y[i // 2] - 4),
                    (x + col_w + 15, row_y[i // 2] + 176)],
                   fill=FAINT, width=1)
    rule(d, 640, 1, FAINT)

    # ---- bottom strip: chess ----
    y = 856
    rule(d, 844, 2, FAINT)
    draw_knight(d, EDGE + 46, y + 52, 48)
    tx = EDGE + 112
    d.text((tx, y), "CHESS", font=sans_bold(15), fill=RUST)
    d.text((tx, y + 24), "Gukesh defends his crown in Geneva",
           font=serif_bold(27), fill=INK)
    draw_para(
        d, tx, y + 62,
        "Game 1 of the World Championship begins today at the Fondation "
        "Martin Bodmer: champion D Gukesh, 20, against challenger "
        "Javokhir Sindarov, 20. The youngest title match ever, over 14 "
        "games, is worth $2.5 million.",
        sans(16), RIGHT_EDGE - tx, 21)

    # ---- footer ----
    rule(d, 986, 1)
    d.text((EDGE, 996),
           "Sources: Reuters  \u2022  CNN  \u2022  NPR  \u2022  ATP Tour  "
           "\u2022  ChessBase India",
           font=sans(13), fill=MUTED)
    foot_r = "Compiled early Tuesday, 24 November 2026 (UTC)"
    d.text((RIGHT_EDGE - d.textlength(foot_r, font=sans(13)), 996),
           foot_r, font=sans(13), fill=MUTED)

    return img


def main():
    img = build_page()
    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
