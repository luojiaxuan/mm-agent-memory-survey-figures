#!/usr/bin/env bash
# note (luojiaxuan): SVG -> icons -> flat SVG -> PDF -> PNG. The PDF must come
# note (luojiaxuan): from Chrome headless: rsvg-convert -f pdf emits Type3 fonts,
# note (luojiaxuan): which arXiv warns on and IEEE PDF eXpress rejects. Chrome
# note (luojiaxuan): emits Type0 subsets only.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FIG="$ROOT/latex/figures"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

python3 "$ROOT/code/gen_systems_realization.py"
python3 "$ROOT/code/export_icons.py"
python3 "$ROOT/code/flatten.py"

WRAP="$(mktemp -t figwrap).html"
cat > "$WRAP" <<'HTML'
<!doctype html><meta charset="utf-8">
<style>@page{size:17.5in 8.3333in;margin:0}html,body{margin:0;padding:0}svg{display:block}</style>
HTML
cat "$FIG/systems_realization.svg" >> "$WRAP"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$FIG/systems_realization.pdf" "file://$WRAP" 2>/dev/null
rm -f "$WRAP"

rsvg-convert -w 2520 "$FIG/systems_realization.svg" -o "$FIG/systems_realization.png"
rsvg-convert -w 1710 "$FIG/icons/_contact_sheet.svg" -o "$FIG/icons/_contact_sheet.png"

echo "built:"
ls -lh "$FIG"
echo "icons: $(ls "$FIG/icons"/ic-*.svg | wc -l | tr -d ' ') files"
