#!/usr/bin/env python3
"""Draw the 21 Nov 2026 world-news summary image (1024x1024 PNG) with PIL only."""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W = 1024
BG = (18, 24, 38)
PANEL = (32, 42, 62)
WHITE = (245, 247, 250)
MUTED = (180, 190, 205)
YELLOW = (255, 196, 0)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def f(path, size): return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, W), BG)
d = ImageDraw.Draw(img)

# Header
d.rectangle([0, 0, W, 150], fill=(200, 30, 40))
d.text((36, 18), "THE WORLD IN ONE DAY", font=f(BOLD, 52), fill=WHITE)
d.text((36, 82), "SATURDAY  •  21 NOVEMBER 2026", font=f(BOLD, 38), fill=(255, 230, 120))

# Panels: (accent, tag, headline lines, subline)
panels = [
    ((255,90,60), "HORMUZ • GULF", ["Tankers hit near", "Strait of Hormuz"], "2 projectile strikes reported;\noil shipments fall 15%"),
    ((120,170,255), "UKRAINE • EUROPE", ["Russian strike on", "Kryvyi Rih kills 2"], "Paramedic & boy, 7, killed;\n~60 wounded. Missile in Poland"),
    ((90,200,120), "CLIMATE • TÜRKIYE", ["COP31 in Antalya", "goes into overtime"], "Nearly 200 nations deadlocked\nover fossil fuels & finance"),
    ((255,196,0), "MARKETS • USA", ["Nasdaq plunges 5.3%", "in AI sell-off"], "Worst week since 2020;\nS&P 500 slips into correction"),
    ((200,140,255), "APEC • CHINA", ["Xi hosts Trump &", "Putin in Shenzhen"], "Trump touts Putin talk on\nUkraine at APEC summit"),
    ((255,140,170), "GAZA • MIDDLE EAST", ["Israeli fire kills", "4 in Gaza"], "Deaths in north & west Gaza;\nSaudi intercepts Houthi missiles"),
    ((255,160,60), "PERU • AMERICAS", ["Magnitude 6.7 quake", "shakes the Andes"], "Central Peru earthquake;\n~170 homes affected"),
    ((80,210,200), "TRADE • EU-ASIA", ["EU & Indonesia sign", "free-trade deal"], "CEPA trade & investment pact\nsigned after long talks"),
]

cols, rows = 2, 4
mx, my, gap = 28, 168, 16
pw = (W - 2*mx - gap)//cols
ph = (W - my - 74 - (rows-1)*gap)//rows  # leave footer

for i, (accent, tag, head, sub) in enumerate(panels):
    c, r = i % cols, i // cols
    x0 = mx + c*(pw+gap); y0 = my + r*(ph+gap); x1, y1 = x0+pw, y0+ph
    d.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=PANEL)
    d.rectangle([x0, y0, x0+10, y1], fill=accent)
    # simple icon circle
    d.ellipse([x0+24, y0+14, x0+64, y0+54], fill=accent)
    d.text((x0+78, y0+18), tag, font=f(BOLD, 19), fill=accent)
    yy = y0+62
    for line in head:
        d.text((x0+24, yy), line, font=f(BOLD, 27), fill=WHITE); yy += 33
    yy += 2
    for line in sub.split("\n"):
        d.text((x0+24, yy), line, font=f(REG, 19), fill=MUTED); yy += 24

footer_y = my + rows*ph + (rows-1)*gap + 12
d.text((28, footer_y), "Also: Denmark expels Russian attaché over assassination plot  •  Russian cargo ship hit by drones",
       font=f(REG, 19), fill=MUTED)
d.text((28, footer_y+28), "in Gulf of Finland, crew evacuates  •  Mexico captures FBI-wanted cartel leader 'Chapo Isidro'",
       font=f(REG, 19), fill=MUTED)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, optimize=True)
print(out, img.size, os.path.getsize(out))
