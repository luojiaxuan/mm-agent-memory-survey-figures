# -*- coding: utf-8 -*-
"""Write every icon as a standalone 24x24 SVG plus a contact sheet.

Output goes to latex/figures/icons/. The files are what a designer opens in
Illustrator, Figma, or Inkscape; the figure itself keeps using icons.py.
"""
import pathlib
from icons import SYM


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# note (luojiaxuan): the illustrator reads these names, so spell out what each
# note (luojiaxuan): icon depicts and where it is used in the figure
CAPTION = {
    "ic-image": "still image", "ic-video": "video clip", "ic-audio": "audio waveform",
    "ic-rgbd": "RGB-D / embodied observation", "ic-text": "text record",
    "ic-event": "event record", "ic-table": "table / schema", "ic-graph": "graph nodes",
    "ic-tokens": "memory tokens", "ic-recur": "recurrent state", "ic-kv": "KV blocks",
    "ic-adapter": "adapter / LoRA", "ic-chain": "source link", "ic-search": "semantic lookup",
    "ic-radix": "prefix / radix index", "ic-check": "reuse validation",
    "ic-queue": "admission & retention", "ic-clock": "memory-aware scheduling",
    "ic-gpu": "accelerator HBM", "ic-ram": "host DRAM", "ic-ssd": "local SSD",
    "ic-cloud": "remote / disaggregated storage", "ic-agent": "model / agent",
    "ic-ctx": "context window", "ic-feat": "multimodal features",
    "ic-identity": "identity", "ic-version": "version", "ic-prov": "provenance",
    "ic-dep": "dependency", "ic-inval": "invalidation", "ic-del": "deletion",
    "ic-share": "sharing & isolation",
}

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "latex" / "figures" / "icons"
OUT.mkdir(parents=True, exist_ok=True)

for name, body in SYM.items():
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
           f'width="24" height="24">\n<title>{name} — {esc(CAPTION[name])}</title>{body}\n</svg>\n')
    (OUT / f"{name}.svg").write_text(svg)

COLS, CW, CH = 6, 190, 120
rows = (len(SYM) + COLS - 1) // COLS
w, h = COLS * CW, rows * CH + 56
sheet = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
         f'font-family="Helvetica Neue, Helvetica, Arial, sans-serif">',
         f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>',
         f'<text x="24" y="36" font-size="21" font-weight="bold" fill="#DD6E56">'
         f'Icon set · Systems Realization figure</text>']
for i, (name, body) in enumerate(SYM.items()):
    cx = (i % COLS) * CW + CW / 2
    cy = (i // COLS) * CH + 78
    sheet.append(f'<g transform="translate({cx - 22} {cy - 22}) scale(1.8333)">{body}</g>')
    sheet.append(f'<text x="{cx}" y="{cy + 40}" font-size="12" font-weight="bold" fill="#29697B" '
                 f'text-anchor="middle">{name}</text>')
    sheet.append(f'<text x="{cx}" y="{cy + 55}" font-size="10.5" fill="#5D6B70" '
                 f'text-anchor="middle">{esc(CAPTION[name])}</text>')
sheet.append('</svg>')
(OUT / "_contact_sheet.svg").write_text("\n".join(sheet))

print(f"wrote {len(SYM)} icons + contact sheet to {OUT}")
