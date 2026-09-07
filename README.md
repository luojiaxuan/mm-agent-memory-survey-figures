# mm-agent-memory-survey-figures

Figures for the multimodal agent memory survey. Each figure is generated from a script; edit the script, not the SVG.

![systems realization](latex/figures/systems_realization.png)

## Layout

- `code/gen_systems_realization.py` — generator for the §7.5 figure
- `code/icons.py` — icon library, 33 symbols, plain SVG primitives
- `code/export_icons.py` — writes one SVG per icon plus a contact sheet
- `code/flatten.py` — writes a copy of the figure with icons inlined
- `code/build.sh` — runs all of the above, then exports PDF and PNG
- `latex/figures/systems_realization.{svg,pdf,png}` — the figure
- `latex/figures/systems_realization_flat.svg` — same figure without `<use>`; open this one in Illustrator or Figma
- `latex/figures/icons/` — individual icons and `_contact_sheet.{svg,png}`

## Build

    bash code/build.sh

Needs python3, Google Chrome, and rsvg-convert (`brew install librsvg`).
The PDF goes through Chrome because rsvg-convert emits Type3 fonts.

## LaTeX

    \includegraphics[width=\textwidth]{figures/systems_realization.pdf}

Page is 1260x600 pt (2.1:1). Text sizes match Figure 1 and Figure 5 of the survey at text width.

## Palette

coral `#F8A599` · dark teal `#29697B` · muted teal `#72ADAB` · pale cyan `#CBE2E6` · pale yellow `#FAF4D5` · pale peach `#F8D6BE` · green `#D6E7CD` · blue `#D3DEF0` · lavender `#E3DAF2` · teal `#D2ECE8`
