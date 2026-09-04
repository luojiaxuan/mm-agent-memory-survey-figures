# -*- coding: utf-8 -*-
"""Icon library shared by the figure generator and the icon exporter.

Each entry is the body of a 24x24 SVG symbol, built from plain vector
primitives only: no external references, no embedded bitmaps, no fonts.
Colours come from the survey palette so an icon can be dropped into any
figure in this repo unchanged.
"""

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


