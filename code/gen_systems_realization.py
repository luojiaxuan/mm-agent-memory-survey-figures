# -*- coding: utf-8 -*-
"""Generate the 'Systems Realization of Multimodal Agent Memory' survey figure.

Writes latex/figures/systems_realization.svg. Run code/build.sh to also
produce the PDF and PNG.
"""
import pathlib

W, H = 1680, 800

CORAL      = "#F8A599"
CORAL_LN   = "#F09A87"
CORAL_TX   = "#DD6E56"
TEAL       = "#29697B"
MTEAL      = "#72ADAB"
PCYAN      = "#CBE2E6"
PCYAN_LN   = "#8FBDC7"
PYELLOW    = "#FAF4D5"
PYELLOW_LN = "#E0CE8E"
PPEACH     = "#F8D6BE"
PPEACH_LN  = "#E0A47A"
GREEN      = "#D6E7CD"; GREEN_LN = "#A8C79A"
BLUE       = "#D3DEF0"; BLUE_LN  = "#A9BBDD"
LAV        = "#E3DAF2"; LAV_LN   = "#BFAEE0"
RTEAL      = "#D2ECE8"; RTEAL_LN = "#9CD0C7"
CHAR       = "#3A4448"
MUTED      = "#5D6B70"

out = []
def add(s): out.append(s)

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def rect(x, y, w, h, rx=0, fill="none", stroke=None, sw=1.2, dash=None, extra=""):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{sw}"'
        if dash:
            s += f' stroke-dasharray="{dash}"'
    add(s + extra + '/>')

def txt(x, y, s, size=10, fill=CHAR, weight="normal", anchor="start", style="normal", ls=None, op=None):
    a = f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"'
    if style != "normal":
        a += f' font-style="{style}"'
    if ls:
        a += f' letter-spacing="{ls}"'
    if op:
        a += f' opacity="{op}"'
    add(a + f'>{esc(s)}</text>')

def line(x1, y1, x2, y2, stroke=TEAL, sw=1.3, dash=None, marker=None, mstart=None, cap="round"):
    s = f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"'
    if dash:
        s += f' stroke-dasharray="{dash}"'
    if marker:
        s += f' marker-end="url(#{marker})"'
    if mstart:
        s += f' marker-start="url(#{mstart})"'
    add(s + '/>')

def use(sym, x, y, size):
    add(f'<use href="#{sym}" xlink:href="#{sym}" x="{x}" y="{y}" width="{size}" height="{size}"/>')

def pill(x, y, w, h, label, fill=CORAL, tcol="#FFFFFF", size=10.5, weight="bold", stroke=None,
         sw=1.2, dash=None, lines=None, ls=None):
    rect(x, y, w, h, rx=h / 2, fill=fill, stroke=stroke, sw=sw, dash=dash)
    cx = x + w / 2
    if lines:
        n = len(lines)
        y0 = y + h / 2 - (n - 1) * 8 + 4
        for i, ln in enumerate(lines):
            txt(cx, y0 + i * 16, ln, size=size, fill=tcol, weight=weight, anchor="middle", ls=ls)
    else:
        txt(cx, y + h / 2 + size * 0.36, label, size=size, fill=tcol, weight=weight, anchor="middle", ls=ls)

from icons import SYM

# note (luojiaxuan): document head: arrow markers and icon symbols
add(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
    f'viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
    f'font-family="Helvetica Neue, Helvetica, Arial, sans-serif">')
add('<defs>')
for mid, col, size in (("arrT", TEAL, 10), ("arrTs", TEAL, 8), ("arrC", CORAL_TX, 10), ("arrM", MTEAL, 8)):
    add(f'<marker id="{mid}" viewBox="0 0 10 10" refX="9.2" refY="5" markerWidth="{size}" '
        f'markerHeight="{size}" markerUnits="userSpaceOnUse" orient="auto">'
        f'<path d="M0.5 0.8 L9.6 5 L0.5 9.2 L2.4 5 Z" fill="{col}"/></marker>')
for k, v in SYM.items():
    add(f'<symbol id="{k}" viewBox="0 0 24 24" overflow="visible">{v}</symbol>')
add('</defs>')
rect(0, 0, W, H, fill="#FFFFFF")

L, CR = 24, 1512          # note (luojiaxuan): content left / right edge
PX0, PXW = 1532, 124      # note (luojiaxuan): consistency strip geometry

# note (luojiaxuan): title row
pill(L, 14, 128, 26, "SYSTEMS", size=12, ls=1.5)
txt(168, 37, "Systems Realization of Multimodal Agent Memory", size=26, fill=CORAL_TX, weight="bold")
txt(CR, 37, "from logical memory objects to physical state, movement, and reuse",
    size=15, fill=MTEAL, anchor="end", style="italic")

# note (luojiaxuan): top band: indexing, reuse and scheduling
rect(L, 56, CR - L, 90, rx=14, fill=PYELLOW, stroke=PYELLOW_LN, sw=1.3, dash="6 4")
pill(40, 64, 136, 22, "CONTROL PLANE", size=12, ls=0.8)
txt(40, 111, "Indexing, Reuse", size=17, fill=TEAL, weight="bold")
txt(40, 130, "& Scheduling", size=17, fill=TEAL, weight="bold")

CHIPS = [(["ic-search", "ic-graph"], "Semantic · Temporal ·", "spatial / entity paths"),
         (["ic-radix"], "Prefix / Radix Index", "reusable execution state"),
         (["ic-check"], "Reuse Validation", "identity · order · position"),
         (["ic-queue"], "Admission & Retention", "what enters · what persists"),
         (["ic-clock"], "Memory-Aware Scheduling", "cost-aware ordering")]
for i, (icons, t1, t2) in enumerate(CHIPS):
    x = 186 + i * 265
    rect(x, 72, 255, 58, rx=11, fill="#FFFFFF", stroke=PYELLOW_LN, sw=1.1, dash="4 3")
    if len(icons) == 2:
        use(icons[0], x + 10, 88, 24); use(icons[1], x + 36, 88, 24); tx = x + 66
    else:
        use(icons[0], x + 13, 87, 27); tx = x + 50
    txt(tx, 99, t1, size=15, fill=TEAL, weight="bold")
    txt(tx, 116, t2, size=13.5, fill=MUTED)

for cx in (235, 826, 1329):
    line(cx, 148, cx, 165, stroke=MTEAL, sw=1.3, dash="4 3", marker="arrM")
line(462, 148, 462, 590, stroke=MTEAL, sw=1.3, dash="4 4", marker="arrM")

# note (luojiaxuan): left panel: logical memory families
rect(L, 168, 422, 380, rx=14, fill="#FBFDFE", stroke="#B7CFD6", sw=1.3, dash="6 4")
txt(40, 198, "Logical Memory", size=25, fill=TEAL, weight="bold")
txt(40, 216, "representation supplied to downstream computation", size=14, fill=MUTED, style="italic")

CARDS = [("Source & Modality-Specific", "image · video · audio · RGB-D", GREEN, GREEN_LN,
          ["ic-image", "ic-video", "ic-audio", "ic-rgbd"]),
         ("Textual & Structured", "text record · event · table · graph", BLUE, BLUE_LN,
          ["ic-text", "ic-event", "ic-table", "ic-graph"]),
         ("Latent & Parametric", "tokens · recurrent state · adapter", LAV, LAV_LN,
          ["ic-tokens", "ic-recur", "ic-kv", "ic-adapter"]),
         ("Hybrid & Source-Linked", "compact record linked to source", RTEAL, RTEAL_LN,
          ["ic-text", "ic-chain", "ic-image"])]
for i, (t1, t2, fill, ln, icons) in enumerate(CARDS):
    y = 224 + i * 81
    rect(38, y, 394, 71, rx=11, fill=fill, stroke=ln, sw=1.2, dash="5 3")
    txt(52, y + 30, t1, size=17, fill=TEAL, weight="bold")
    txt(52, y + 51, t2, size=14, fill="#46545A")
    n = len(icons)
    sx = 418 - (n * 24 + (n - 1) * 8)
    for j, ic in enumerate(icons):
        use(ic, sx + j * 32, y + 23, 24)

# note (luojiaxuan): centre panel: cross-layer read and write paths
rect(492, 168, 668, 380, rx=16, fill="#FEF8F6", stroke=CORAL_LN, sw=1.6, dash="7 4")
txt(826, 202, "Cross-Layer Memory Runtime", size=25, fill=CORAL_TX, weight="bold", anchor="middle")
txt(826, 221, "materialization on the read path · commit on the write path",
    size=14, fill=MUTED, anchor="middle", style="italic")

txt(512, 246, "READ   ▸   logical memory into execution", size=15, fill=CORAL_TX, weight="bold", ls=0.6)
pill(512, 252, 150, 40, "Index & Select", size=17)
line(664, 272, 684, 272, sw=1.7, marker="arrT")
pill(686, 252, 215, 40, "Materialize", size=17)
line(903, 272, 923, 272, sw=1.7, marker="arrT")
pill(925, 252, 175, 40, None, fill=PCYAN, tcol=TEAL, stroke=PCYAN_LN, sw=1.3, size=16,
     lines=["Active Execution", "State"])
add(f'<path d="M448 308 H466 Q478 308 478 296 V284 Q478 272 490 272 H508" fill="none" '
    f'stroke="{TEAL}" stroke-width="1.8" stroke-linecap="round" marker-end="url(#arrT)"/>')
line(1104, 272, 1178, 272, sw=1.8, marker="arrT")

READ_EX = [("text", "→ into context"), ("image", "→ into VLM input"),
           ("feature", "→ model interface"), ("stored / rebuilt", "→ into KV state")]
for i, (a, b) in enumerate(READ_EX):
    x = 512 + i * 150
    rect(x, 304, 138, 46, rx=9, fill="#FFFFFF", stroke=CORAL_LN, sw=1, dash="3.5 3")
    txt(x + 69, 324, a, size=14, fill=TEAL, weight="bold", anchor="middle")
    txt(x + 69, 341, b, size=13.5, fill=MUTED, anchor="middle")

line(512, 368, 1100, 368, stroke=CORAL_LN, sw=1, dash="3 4")

txt(512, 396, "WRITE   ◂   execution into logical memory", size=15, fill=CORAL_TX, weight="bold", ls=0.6)
pill(512, 402, 175, 40, None, size=16, lines=["Commit &", "Write-back"])
line(709, 422, 689, 422, sw=1.7, marker="arrT")
pill(711, 402, 215, 40, None, size=16, lines=["Summarize · Compress ·", "Encode"])
line(948, 422, 928, 422, sw=1.7, marker="arrT")
pill(950, 402, 150, 40, None, fill=PCYAN, tcol=TEAL, stroke=PCYAN_LN, sw=1.3, size=16,
     lines=["Execution", "History"])
add(f'<path d="M508 422 H490 Q478 422 478 410 V398 Q478 386 466 386 H450" fill="none" '
    f'stroke="{TEAL}" stroke-width="1.8" stroke-linecap="round" marker-end="url(#arrT)"/>')
line(1178, 422, 1104, 422, sw=1.8, marker="arrT")

WRITE_EX = [("expired", "context"), ("completed", "trajectory"),
            ("reasoning-derived", "state"), ("persistent record", "or latent memory")]
for i, (a, b) in enumerate(WRITE_EX):
    x = 512 + i * 150
    rect(x, 454, 138, 46, rx=9, fill="#FFFFFF", stroke=CORAL_LN, sw=1, dash="3.5 3")
    txt(x + 69, 474, a, size=14, fill=TEAL, weight="bold", anchor="middle")
    txt(x + 69, 491, b, size=13.5, fill=MUTED, anchor="middle")

txt(826, 528, "a residency change moves bytes without changing the logical memory state",
    size=14, fill=MUTED, anchor="middle", style="italic")

# note (luojiaxuan): right panel: active model execution
rect(1182, 168, 294, 380, rx=14, fill="#EAF5F7", stroke=PCYAN_LN, sw=1.3, dash="6 4")
txt(1329, 200, "Active Model Execution", size=24, fill=TEAL, weight="bold", anchor="middle")
INP = [("ic-ctx", "Context"), ("ic-feat", "Multimodal Features"),
       ("ic-tokens", "Latent Tokens"), ("ic-kv", "KV / Recurrent State")]
for i, (ic, a) in enumerate(INP):
    y = 214 + i * 38
    rect(1196, y, 266, 32, rx=9, fill="#FFFFFF", stroke=PCYAN_LN, sw=1, dash="4 3")
    use(ic, 1206, y + 6, 20)
    txt(1234, y + 22, a, size=16, fill=TEAL, weight="bold")
line(1329, 360, 1329, 374, sw=1.7, marker="arrT")
rect(1298, 376, 62, 62, rx=15, fill="#FFFFFF", stroke=TEAL, sw=1.7)
use("ic-agent", 1308, 386, 42)
for i, lab in enumerate(("Reason", "Plan", "Act")):
    x = 1196 + i * 95
    pill(x, 446, 76, 30, lab, size=16)
    if i < 2:
        line(x + 78, 461, x + 93, 461, sw=1.6, marker="arrT")
rect(1196, 484, 266, 58, rx=10, fill="#FFFFFF", stroke=CORAL_LN, sw=1.1, dash="4 3")
for i, sline in enumerate(["Request-local state is an execution",
                           "artifact; only state retained and",
                           "reused later becomes agent memory."]):
    txt(1329, 502 + i * 16, sline, size=13.5, fill=MUTED, anchor="middle")

rect(1484, 168, 28, 380, rx=9, fill=PCYAN, stroke=PCYAN_LN, sw=1.2)
add(f'<text x="1498" y="358" font-size="17" fill="{TEAL}" font-weight="bold" text-anchor="middle" '
    f'transform="rotate(-90 1498 358)">Downstream Computation</text>')

# note (luojiaxuan): connectors from the three panels down to the tiers
for x, lab in ((200, "records & replicas"), (826, "byte movement"), (1329, "resident state")):
    line(x, 552, x, 592, stroke=MTEAL, sw=1.4, dash="5 3", marker="arrM", mstart="arrM")
    txt(x + 10, 578, lab, size=14, fill=MTEAL, style="italic")

# note (luojiaxuan): bottom band: physical memory hierarchy
rect(L, 596, CR - L, 172, rx=14, fill="#F7FBFC", stroke=PCYAN_LN, sw=1.3, dash="6 4")
txt(40, 628, "Physical Memory Hierarchy", size=24, fill=TEAL, weight="bold")
txt(392, 628, "physical placement is orthogonal to logical representation — the same logical memory "
              "may be replicated across tiers", size=14, fill=MUTED, style="italic")

TIERS = [("ic-gpu", "Accelerator", "HBM", "active KV · working set"),
         ("ic-ram", "Host", "DRAM", "staged context · pools"),
         ("ic-ssd", "Local", "SSD", "session state · media cache"),
         ("ic-cloud", "Remote / Disaggregated", "Storage", "shared pool · cold archive")]
for i, (ic, t1, t2, s1) in enumerate(TIERS):
    x = 40 + i * 397
    rect(x, 634, 265, 92, rx=12, fill=PCYAN, stroke=TEAL, sw=1.4)
    use(ic, x + 12, 660, 34)
    txt(x + 54, 668, t1, size=17, fill=TEAL, weight="bold")
    txt(x + 54, 686, t2, size=17, fill=TEAL, weight="bold")
    txt(x + 54, 707, s1, size=14, fill="#3E5057")
for gx in (371, 768, 1165):
    line(gx + 54, 664, gx - 54, 664, sw=1.6, marker="arrT")
    txt(gx, 654, "Prefetch · Promote", size=14, fill=TEAL, weight="bold", anchor="middle")
    line(gx - 54, 700, gx + 54, 700, sw=1.6, marker="arrT")
    txt(gx, 719, "Offload · Demote", size=14, fill=TEAL, weight="bold", anchor="middle")

txt(40, 755, "Movement cost knobs:", size=15, fill=TEAL, weight="bold")
kx = 214
for lab, w in (("Compress", 92), ("Transfer", 90), ("Reconstruct", 114), ("Recompute", 100)):
    rect(kx, 737, w, 26, rx=13, fill="#FFFFFF", stroke=MTEAL, sw=1, dash="3.5 3")
    txt(kx + w / 2, 755, lab, size=15, fill=TEAL, anchor="middle")
    kx += w + 12
txt(1496, 755, "cost = bytes moved × effective bandwidth, overlapped with computation or traded "
               "against recompute", size=14, fill=MUTED, anchor="end", style="italic")

# note (luojiaxuan): right strip: consistency and coordination
rect(PX0, 56, PXW, 712, rx=14, fill=PPEACH, stroke=PPEACH_LN, sw=1.3, dash="6 4")
cxp = PX0 + PXW / 2
txt(cxp, 86, "Consistency &", size=15, fill=TEAL, weight="bold", anchor="middle")
txt(cxp, 104, "Coordination", size=15, fill=TEAL, weight="bold", anchor="middle")
ITEMS = [("ic-identity", "Identity", "stable unit id"), ("ic-version", "Version", "what changed"),
         ("ic-prov", "Provenance", "back to source"), ("ic-dep", "Dependency", "what derives"),
         ("ic-inval", "Invalidation", "what is stale"), ("ic-del", "Deletion", "what retires"),
         ("ic-share", "Sharing &", "Isolation")]
for i, (ic, a, b) in enumerate(ITEMS):
    top = 122 + i * 90
    use(ic, cxp - 15, top + 4, 30)
    txt(cxp, top + 52, a, size=15, fill=TEAL, weight="bold", anchor="middle")
    if a.endswith("&"):
        txt(cxp, top + 69, b, size=15, fill=TEAL, weight="bold", anchor="middle")
    else:
        txt(cxp, top + 68, b, size=13.5, fill="#7A5B43", anchor="middle")
for y in (100, 260, 430, 690):
    line(PX0 - 3, y, PX0 - 18, y, stroke=PPEACH_LN, sw=1.4, dash="4 3", marker="arrM")

txt(24, 789, "Logical memory type is defined by the operative representation supplied to computation, not by "
             "where its bytes reside; indices and stores realize access without defining a new memory type.",
    size=14, fill=MUTED, style="italic")

add('</svg>')
OUT = pathlib.Path(__file__).resolve().parents[1] / "latex" / "figures" / "systems_realization.svg"
OUT.write_text("\n".join(out))
print(f"wrote {OUT}")
