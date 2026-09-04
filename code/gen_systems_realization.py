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

# note (luojiaxuan): flat icon library, one symbol per 24x24 viewBox
SYM = {}
SYM["ic-image"] = '''
<rect x="2.5" y="4.5" width="19" height="15" rx="3" fill="#CBE2E6" stroke="#29697B" stroke-width="1.4"/>
<circle cx="8" cy="9.5" r="2" fill="#F0CE72"/>
<path d="M4.2 18.6 L10 12 L13.2 15.4 L16.2 12.4 L20.4 18.6 Z" fill="#72ADAB"/>'''
SYM["ic-video"] = '''
<rect x="2.5" y="5" width="19" height="14" rx="3" fill="#D3DEF0" stroke="#29697B" stroke-width="1.4"/>
<path d="M6.5 5 V19" stroke="#29697B" stroke-width="1.1"/>
<path d="M10.5 8.8 L16.3 12 L10.5 15.2 Z" fill="#F8A599" stroke="#29697B" stroke-width="1"/>'''
SYM["ic-audio"] = '''
<g stroke-linecap="round">
<line x1="3.5" y1="10" x2="3.5" y2="14" stroke="#72ADAB" stroke-width="2"/>
<line x1="8" y1="6" x2="8" y2="18" stroke="#29697B" stroke-width="2"/>
<line x1="12.5" y1="9" x2="12.5" y2="15" stroke="#F8A599" stroke-width="2"/>
<line x1="17" y1="4.5" x2="17" y2="19.5" stroke="#29697B" stroke-width="2"/>
<line x1="21" y1="10.5" x2="21" y2="13.5" stroke="#72ADAB" stroke-width="2"/></g>'''
SYM["ic-rgbd"] = '''
<path d="M12 2.6 L21 7.6 L21 16.4 L12 21.4 L3 16.4 L3 7.6 Z" fill="#D6E7CD" stroke="#29697B" stroke-width="1.4"/>
<path d="M12 2.6 V12 M12 12 L21 7.6 M12 12 L3 7.6" fill="none" stroke="#29697B" stroke-width="1.2"/>
<circle cx="12" cy="12" r="1.5" fill="#F8A599"/>'''
SYM["ic-text"] = '''
<rect x="4" y="3.5" width="16" height="17" rx="2.5" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<g stroke="#72ADAB" stroke-width="1.7" stroke-linecap="round">
<line x1="7.3" y1="8.2" x2="16.7" y2="8.2"/><line x1="7.3" y1="12" x2="16.7" y2="12"/>
<line x1="7.3" y1="15.8" x2="13" y2="15.8"/></g>'''
SYM["ic-event"] = '''
<rect x="3" y="5" width="18" height="16" rx="2.5" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<path d="M3 7.5 a2.5 2.5 0 0 1 2.5 -2.5 h13 a2.5 2.5 0 0 1 2.5 2.5 V10 H3 Z" fill="#F8A599"/>
<path d="M3 10 H21" stroke="#29697B" stroke-width="1.2"/>
<g stroke="#29697B" stroke-width="1.7" stroke-linecap="round"><line x1="8" y1="2.8" x2="8" y2="6.5"/><line x1="16" y1="2.8" x2="16" y2="6.5"/></g>
<g fill="#72ADAB"><circle cx="8.5" cy="14" r="1.4"/><circle cx="14" cy="14" r="1.4"/><circle cx="8.5" cy="18" r="1.4"/></g>'''
SYM["ic-table"] = '''
<rect x="3" y="5" width="18" height="14" rx="2.2" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<path d="M3 7.2 a2.2 2.2 0 0 1 2.2 -2.2 h13.6 a2.2 2.2 0 0 1 2.2 2.2 V9.5 H3 Z" fill="#D3DEF0"/>
<g stroke="#29697B" stroke-width="1"><line x1="3" y1="9.5" x2="21" y2="9.5"/><line x1="3" y1="14.3" x2="21" y2="14.3"/>
<line x1="9" y1="9.5" x2="9" y2="19"/><line x1="15" y1="9.5" x2="15" y2="19"/></g>'''
SYM["ic-graph"] = '''
<g stroke="#29697B" stroke-width="1.3"><line x1="6.5" y1="8" x2="17" y2="6.2"/><line x1="6.5" y1="8" x2="12" y2="17.2"/><line x1="17" y1="6.2" x2="12" y2="17.2"/></g>
<circle cx="6.5" cy="8" r="3" fill="#D3DEF0" stroke="#29697B" stroke-width="1.3"/>
<circle cx="17.2" cy="6.2" r="2.6" fill="#F8A599" stroke="#29697B" stroke-width="1.3"/>
<circle cx="12" cy="17.2" r="2.8" fill="#CBE2E6" stroke="#29697B" stroke-width="1.3"/>'''
SYM["ic-tokens"] = '''
<g stroke="#29697B" stroke-width="1.3">
<rect x="2.5" y="8.5" width="6" height="7.5" rx="1.8" fill="#E3DAF2"/>
<rect x="9" y="8.5" width="6" height="7.5" rx="1.8" fill="#F8A599"/>
<rect x="15.5" y="8.5" width="6" height="7.5" rx="1.8" fill="#E3DAF2"/></g>'''
SYM["ic-recur"] = '''
<path d="M19.4 12.6 A7.4 7.4 0 1 1 16.3 6.2" fill="none" stroke="#29697B" stroke-width="1.9" stroke-linecap="round"/>
<path d="M11.6 5.2 L17.6 4.2 L16.6 10.2 Z" fill="#F8A599" stroke="#29697B" stroke-width="1"/>
<circle cx="12" cy="12" r="2.8" fill="#E3DAF2" stroke="#29697B" stroke-width="1.3"/>'''
SYM["ic-kv"] = '''
<g stroke="#29697B" stroke-width="1.1">
<rect x="2.6" y="6.4" width="5.6" height="4.8" rx="1.2" fill="#CBE2E6"/>
<rect x="9.2" y="6.4" width="5.6" height="4.8" rx="1.2" fill="#CBE2E6"/>
<rect x="15.8" y="6.4" width="5.6" height="4.8" rx="1.2" fill="#F8A599"/>
<rect x="2.6" y="12.8" width="5.6" height="4.8" rx="1.2" fill="#E3DAF2"/>
<rect x="9.2" y="12.8" width="5.6" height="4.8" rx="1.2" fill="#E3DAF2"/>
<rect x="15.8" y="12.8" width="5.6" height="4.8" rx="1.2" fill="#E3DAF2"/></g>'''
SYM["ic-adapter"] = '''
<rect x="3.5" y="6" width="12" height="12" rx="2.6" fill="#E3DAF2" stroke="#29697B" stroke-width="1.4"/>
<rect x="7" y="9.5" width="5" height="5" rx="1.2" fill="#72ADAB"/>
<g stroke="#29697B" stroke-width="1.3" stroke-linecap="round"><line x1="15.5" y1="9.2" x2="19" y2="9.2"/><line x1="15.5" y1="14.8" x2="19" y2="14.8"/></g>
<circle cx="20.2" cy="9.2" r="1.7" fill="#F8A599" stroke="#29697B" stroke-width="1.1"/>
<circle cx="20.2" cy="14.8" r="1.7" fill="#F8A599" stroke="#29697B" stroke-width="1.1"/>'''
SYM["ic-chain"] = '''
<g stroke="#29697B" stroke-width="1.8" fill="none" stroke-linecap="round">
<path d="M10 14.6 L7.6 17 a3.6 3.6 0 0 1 -5.1 -5.1 L4.9 9.5"/>
<path d="M14 9.4 L16.4 7 a3.6 3.6 0 0 1 5.1 5.1 L19.1 14.5"/>
<line x1="8.8" y1="15.2" x2="15.2" y2="8.8" stroke="#F8A599" stroke-width="2"/></g>'''
SYM["ic-search"] = '''
<circle cx="10.3" cy="10.3" r="6.2" fill="#FFFFFF" stroke="#29697B" stroke-width="1.8"/>
<circle cx="10.3" cy="10.3" r="3" fill="#CBE2E6"/>
<line x1="14.9" y1="14.9" x2="20.6" y2="20.6" stroke="#29697B" stroke-width="2.3" stroke-linecap="round"/>'''
SYM["ic-radix"] = '''
<g stroke="#29697B" stroke-width="1.2" fill="none">
<path d="M6 12 H9.5 V6.5 H13"/><path d="M9.5 12 V17.5 H13"/>
<path d="M15.5 6.5 H18 V3.5 H20"/><path d="M18 6.5 V9.5 H20"/></g>
<circle cx="4" cy="12" r="2.4" fill="#F8A599" stroke="#29697B" stroke-width="1.2"/>
<circle cx="14.2" cy="6.5" r="2" fill="#CBE2E6" stroke="#29697B" stroke-width="1.2"/>
<circle cx="14.2" cy="17.5" r="2" fill="#CBE2E6" stroke="#29697B" stroke-width="1.2"/>
<circle cx="21" cy="3.5" r="1.6" fill="#FAF4D5" stroke="#29697B" stroke-width="1.1"/>
<circle cx="21" cy="9.5" r="1.6" fill="#FAF4D5" stroke="#29697B" stroke-width="1.1"/>'''
SYM["ic-check"] = '''
<circle cx="12" cy="12" r="8" fill="#D6E7CD" stroke="#29697B" stroke-width="1.5"/>
<path d="M7.8 12.3 L10.8 15.3 L16.2 8.9" fill="none" stroke="#29697B" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/>'''
SYM["ic-queue"] = '''
<g stroke="#29697B" stroke-width="1.3">
<rect x="2.5" y="5" width="12" height="4.2" rx="1.5" fill="#FAF4D5"/>
<rect x="2.5" y="10.4" width="12" height="4.2" rx="1.5" fill="#F8A599"/>
<rect x="2.5" y="15.8" width="12" height="4.2" rx="1.5" fill="#CBE2E6"/></g>
<path d="M16.5 12.5 H21 M19 10.5 L21 12.5 L19 14.5" fill="none" stroke="#29697B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'''
SYM["ic-clock"] = '''
<circle cx="12" cy="12" r="8" fill="#FFFFFF" stroke="#29697B" stroke-width="1.6"/>
<path d="M12 7.2 V12 L15.6 14.2" fill="none" stroke="#29697B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="12" cy="12" r="1.3" fill="#F8A599"/>'''
SYM["ic-gpu"] = '''
<g stroke="#29697B" stroke-width="1.3" stroke-linecap="round">
<line x1="8" y1="2.6" x2="8" y2="5.5"/><line x1="12" y1="2.6" x2="12" y2="5.5"/><line x1="16" y1="2.6" x2="16" y2="5.5"/>
<line x1="8" y1="18.5" x2="8" y2="21.4"/><line x1="12" y1="18.5" x2="12" y2="21.4"/><line x1="16" y1="18.5" x2="16" y2="21.4"/></g>
<rect x="4" y="5.5" width="16" height="13" rx="2.4" fill="#CBE2E6" stroke="#29697B" stroke-width="1.5"/>
<rect x="7.6" y="9" width="8.8" height="6" rx="1.4" fill="#72ADAB"/>'''
SYM["ic-ram"] = '''
<rect x="2.5" y="6.5" width="19" height="9.5" rx="1.8" fill="#D3DEF0" stroke="#29697B" stroke-width="1.4"/>
<g fill="#72ADAB"><rect x="5" y="8.8" width="3.2" height="4.4" rx="0.7"/><rect x="10.4" y="8.8" width="3.2" height="4.4" rx="0.7"/><rect x="15.8" y="8.8" width="3.2" height="4.4" rx="0.7"/></g>
<g stroke="#29697B" stroke-width="1.3" stroke-linecap="round"><line x1="6" y1="16" x2="6" y2="18.8"/><line x1="10" y1="16" x2="10" y2="18.8"/><line x1="14" y1="16" x2="14" y2="18.8"/><line x1="18" y1="16" x2="18" y2="18.8"/></g>'''
SYM["ic-ssd"] = '''
<rect x="3.5" y="5.5" width="17" height="13" rx="2.2" fill="#E3DAF2" stroke="#29697B" stroke-width="1.5"/>
<rect x="6.2" y="8" width="11.6" height="4.6" rx="1.2" fill="#72ADAB"/>
<line x1="6.5" y1="15.4" x2="12" y2="15.4" stroke="#29697B" stroke-width="1.4" stroke-linecap="round"/>
<circle cx="16.6" cy="15.4" r="1.4" fill="#F8A599"/>'''
SYM["ic-cloud"] = '''
<path d="M19.35 9.04 A7.49 7.49 0 0 0 12 3 C9.11 3 6.6 4.64 5.35 7.04 A5.994 5.994 0 0 0 0.6 13 c0 3.31 2.69 6 6 6 h12.4 c2.76 0 4.4 -2.24 4.4 -5 0 -2.64 -1.45 -4.78 -4.05 -4.96 z"
 fill="#CBE2E6" stroke="#29697B" stroke-width="1.4"/>
<g fill="#29697B"><circle cx="8" cy="21.6" r="1.2"/><circle cx="12" cy="21.6" r="1.2"/><circle cx="16" cy="21.6" r="1.2"/></g>'''
SYM["ic-agent"] = '''
<line x1="12" y1="2.2" x2="12" y2="7" stroke="#29697B" stroke-width="1.5"/>
<circle cx="12" cy="2.4" r="1.8" fill="#F8A599" stroke="#29697B" stroke-width="1.2"/>
<rect x="3.5" y="6.8" width="17" height="13.4" rx="4.2" fill="#CBE2E6" stroke="#29697B" stroke-width="1.6"/>
<circle cx="8.6" cy="12.6" r="1.8" fill="#29697B"/><circle cx="15.4" cy="12.6" r="1.8" fill="#29697B"/>
<path d="M9.2 16.8 H14.8" stroke="#29697B" stroke-width="1.5" stroke-linecap="round"/>'''
SYM["ic-ctx"] = '''
<rect x="3" y="5" width="18" height="14" rx="2.5" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<path d="M3 9.2 H21" stroke="#29697B" stroke-width="1.2"/>
<circle cx="6" cy="7.1" r="0.9" fill="#F8A599"/>
<g stroke="#72ADAB" stroke-width="1.6" stroke-linecap="round"><line x1="6" y1="12.6" x2="18" y2="12.6"/><line x1="6" y1="16" x2="14" y2="16"/></g>'''
SYM["ic-feat"] = '''
<g><circle cx="6" cy="6.5" r="1.9" fill="#72ADAB"/><circle cx="12" cy="6.5" r="1.9" fill="#CBE2E6"/><circle cx="18" cy="6.5" r="1.9" fill="#72ADAB"/>
<circle cx="6" cy="12" r="1.9" fill="#CBE2E6"/><circle cx="12" cy="12" r="1.9" fill="#F8A599"/><circle cx="18" cy="12" r="1.9" fill="#CBE2E6"/>
<circle cx="6" cy="17.5" r="1.9" fill="#72ADAB"/><circle cx="12" cy="17.5" r="1.9" fill="#CBE2E6"/><circle cx="18" cy="17.5" r="1.9" fill="#72ADAB"/></g>'''
SYM["ic-identity"] = '''
<circle cx="12" cy="8.6" r="3.8" fill="#F8A599" stroke="#29697B" stroke-width="1.4"/>
<path d="M4.8 20.4 a7.2 7.2 0 0 1 14.4 0" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>'''
SYM["ic-version"] = '''
<path d="M7 8.4 V15.6 M7 12 H12.6 a4.2 4.2 0 0 0 3.6 -2.2" fill="none" stroke="#29697B" stroke-width="1.4"/>
<circle cx="7" cy="6" r="2.5" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<circle cx="7" cy="18" r="2.5" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<circle cx="17.4" cy="8" r="2.5" fill="#F8A599" stroke="#29697B" stroke-width="1.4"/>'''
SYM["ic-prov"] = '''
<rect x="13.5" y="3.5" width="7.5" height="7.5" rx="1.6" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<rect x="3" y="13" width="7.5" height="7.5" rx="1.6" fill="#CBE2E6" stroke="#29697B" stroke-width="1.4"/>
<path d="M13.5 8.5 H10 a2.5 2.5 0 0 0 -2.5 2.5 V12" fill="none" stroke="#29697B" stroke-width="1.4" stroke-dasharray="2.6 2"/>
<path d="M5.6 11.6 L7.5 14.4 L9.4 11.6 Z" fill="#DD6E56"/>'''
SYM["ic-dep"] = '''
<path d="M7 7.4 L15.6 11 M7 16.6 L15.6 13" fill="none" stroke="#29697B" stroke-width="1.4"/>
<circle cx="5" cy="6.4" r="2.4" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<circle cx="5" cy="17.6" r="2.4" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<circle cx="18.2" cy="12" r="2.7" fill="#F8A599" stroke="#29697B" stroke-width="1.4"/>'''
SYM["ic-inval"] = '''
<circle cx="12" cy="12" r="7.6" fill="#FFFFFF" stroke="#29697B" stroke-width="1.7"/>
<line x1="7" y1="17" x2="17" y2="7" stroke="#DD6E56" stroke-width="2" stroke-linecap="round"/>'''
SYM["ic-del"] = '''
<path d="M6 7.6 H18 L16.9 19.4 A1.7 1.7 0 0 1 15.2 21 H8.8 A1.7 1.7 0 0 1 7.1 19.4 Z" fill="#FFFFFF" stroke="#29697B" stroke-width="1.4"/>
<path d="M4.2 7.4 H19.8" stroke="#29697B" stroke-width="1.9" stroke-linecap="round"/>
<path d="M9.6 7.2 V4.8 h4.8 V7.2" fill="none" stroke="#29697B" stroke-width="1.4"/>
<g stroke="#72ADAB" stroke-width="1.4" stroke-linecap="round"><line x1="10.2" y1="11" x2="10.2" y2="17"/><line x1="13.8" y1="11" x2="13.8" y2="17"/></g>'''
SYM["ic-share"] = '''
<circle cx="8.6" cy="12" r="4.8" fill="#CBE2E6" stroke="#29697B" stroke-width="1.4"/>
<circle cx="15.4" cy="12" r="4.8" fill="#FFFFFF" fill-opacity="0.0" stroke="#29697B" stroke-width="1.4"/>
<line x1="12" y1="4.4" x2="12" y2="19.6" stroke="#DD6E56" stroke-width="1.6" stroke-dasharray="2.6 2.2"/>'''


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
