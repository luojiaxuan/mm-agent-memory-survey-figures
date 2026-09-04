# -*- coding: utf-8 -*-
"""Write a copy of the figure with every <use> expanded inline.

Illustrator and Figma handle <symbol>/<use> inconsistently. The flat copy
carries no symbol indirection, so any editor opens it with the icons intact.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIG = ROOT / "latex" / "figures"
svg = (FIG / "systems_realization.svg").read_text()

bodies = dict(re.findall(r'<symbol id="([^"]+)"[^>]*>(.*?)</symbol>', svg, re.S))

def expand(m):
    name, x, y, size = m.group(1), float(m.group(2)), float(m.group(3)), float(m.group(4))
    return (f'<g transform="translate({x} {y}) scale({round(size / 24, 6)})">'
            f'{bodies[name]}</g>')

flat = re.sub(r'<use href="#([^"]+)" xlink:href="[^"]+" x="([\d.]+)" y="([\d.]+)" '
              r'width="([\d.]+)" height="[\d.]+"/>', expand, svg)
flat = re.sub(r'<symbol id="[^"]+"[^>]*>.*?</symbol>\n?', "", flat, flags=re.S)

assert "<use " not in flat, "unexpanded <use> remains"
out = FIG / "systems_realization_flat.svg"
out.write_text(flat)
print(f"wrote {out}")
