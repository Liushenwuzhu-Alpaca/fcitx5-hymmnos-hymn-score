#!/usr/bin/env python3
"""Generate the Hymmnos Hymn Score fcitx5 skins (all palettes) into dist/.

Geometry targets fcitx5 classicui with in-app preedit (the panel then shows a
single candidate row):
  - font: Noto Sans Mono CJK SC Bold 13pt at 96 DPI (fontHeight 25),
  - one-row panel: fontHeight + textMargin(T+B) + contentMargin(T+B).

fcitx5 5.1.22 note: Theme::paint() ignores dx/dy for overlay images, so a
highlight overlay is pinned to the panel origin instead of riding the
highlight. The staff note is therefore baked into the highlight image itself,
inside its unscaled 9-slice corner. Only the badge uses an overlay
(background paint has dx=dy=0, so it is unaffected).

Gravity enum values must use the spaced form ("Center Left"), matching
fcitx-config's i18n enum strings.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLYPHS = json.loads((ROOT / "scripts" / "hymmnos_glyphs.json").read_text())
UPM = GLYPHS["unitsPerEm"]
DIST = ROOT / "dist"

THEME_PREFIX = "hymmnos-hymn-score"
DISPLAY_NAME = "Hymmnos Hymn Score"


def glyph_fit(ch: str, cx: float, cy: float, h: float, attrs: str) -> str:
    g = GLYPHS["glyphs"][ch]
    x0, y0, x1, y1 = g["bounds"]
    s = h / (y1 - y0)
    tx, ty = cx - (x0 + x1) / 2 * s, cy + (y0 + y1) / 2 * s
    return (
        f'<path transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f} {-s:.5f})" '
        f'd="{g["d"]}" {attrs}/>'
    )


def svg_doc(w: int, h: int, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}">{body}</svg>\n'
    )


# palette: p0 p1 bg0 bg1 badge line accent hl0 hl1 hlStroke text hlText label hlLabel name
PALETTES = {
    "verdant":  ("#2e3440", "#1c2430", "#1b392e", "#0e211b", "#0f221c", "#c9a55a", "#ecd391", "#9a2c3c", "#6a1824", "#ecd391", "#efe3c2", "#fff6e6", "#b0975c", "#f0cf8a", "Verdant"),
    "nocturne": ("#26283a", "#12141f", "#18204a", "#0b1028", "#0d1330", "#b8c4e4", "#eef3ff", "#4a6ae0", "#2a3ea8", "#dfe8ff", "#e6ebfa", "#ffffff", "#8494c4", "#cfdcff", "Nocturne"),
    "twilight": ("#32243a", "#1b1322", "#2e1a3e", "#170c22", "#1a0e26", "#deae94", "#ffd8c4", "#c8487c", "#8a2454", "#ffd8c4", "#f4e2ea", "#fff4f8", "#b48aa0", "#ffd0e0", "Twilight"),
    "ivory":    ("#e4dcc8", "#cfc4a8", "#fbf6ea", "#efe5cf", "#f6eedb", "#8a6a3c", "#7a1f2b", "#8e2634", "#6a1824", "#c9a55a", "#2a2118", "#fff6ea", "#9a7e52", "#f0cf8a", "Ivory"),
    "frost":    ("#dde4ee", "#c4cfde", "#ffffff", "#eaf0f8", "#f4f8fd", "#6d8fc4", "#2f6fd8", "#4a8ef0", "#2a62c8", "#c8dcff", "#1e2a40", "#ffffff", "#7a90b4", "#dce8ff", "Frost"),
    "obsidian": ("#241e22", "#100d0f", "#1c1618", "#0c0a0b", "#120e10", "#c8a070", "#ff6a7a", "#d0283e", "#8e1424", "#f0c890", "#f0e6e2", "#ffffff", "#a08470", "#ffd2a8", "Obsidian"),
}

# one-row panel geometry: height 70 = 25 + (22+5) + (8+10)
GEO = {
    "text_margin": {"L": 10, "R": 10, "T": 22, "B": 5},
    "content_margin": {"L": 78, "R": 52, "T": 8, "B": 10},
    "panel_w": 420,
    "panel_h": 70,
    "panel_m": {"L": 124, "R": 64, "T": 32, "B": 18},
    "hl_m": {"L": 22, "R": 10, "T": 22, "B": 4},
}


def panel_svg(p: tuple) -> str:
    _, _, bg0, bg1, _, gold, accent, *_ = p
    W, H = GEO["panel_w"], GEO["panel_h"]
    staff = "".join(
        f'<line x1="70" y1="{y}" x2="362" y2="{y}" stroke="{gold}" stroke-opacity=".42" stroke-width=".9"/>'
        for y in (13, 16.5, 20, 23.5, 27)
    )
    frame = (
        f"M18,6 H{W - 18} Q{W - 18},18 {W - 6},18 V{H - 18} Q{W - 18},{H - 18} {W - 18},{H - 6} "
        f"H18 Q18,{H - 18} 6,{H - 18} V18 Q18,18 18,6 Z"
    )
    inner = (
        f"M23,11 H{W - 23} Q{W - 23},23 {W - 11},23 V{H - 23} Q{W - 23},{H - 23} {W - 23},{H - 11} "
        f"H23 Q23,{H - 23} 11,{H - 23} V23 Q23,23 23,11 Z"
    )
    dbar = (
        f'<line x1="358" y1="13" x2="358" y2="27" stroke="{gold}" stroke-opacity=".7" stroke-width="1"/>'
        f'<rect x="360" y="13" width="2.6" height="14" fill="{gold}" fill-opacity=".8"/>'
    )
    return svg_doc(W, H, f"""
    <defs>
      <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/>
      </linearGradient>
    </defs>
    <path d="{frame}" fill="url(#g)" stroke="{gold}" stroke-width="1.8"/>
    <path d="{inner}" fill="none" stroke="{gold}" stroke-width=".7" stroke-opacity=".55"/>
    {staff}{dbar}""")


def badge_svg(p: tuple) -> str:
    _, _, _, _, badge, gold, accent, *_ = p
    W = H = 64
    c = 32
    return svg_doc(W, H, f"""
    <circle cx="{c}" cy="{c}" r="30" fill="{badge}" stroke="{gold}" stroke-width="2"/>
    <circle cx="{c}" cy="{c}" r="25.5" fill="none" stroke="{gold}" stroke-width=".8" stroke-dasharray="1.5 3"/>
    <circle cx="{c}" cy="{c}" r="21" fill="none" stroke="{gold}" stroke-width=".8"/>
    {glyph_fit("A", c, c, 26, f'fill="{gold}"')}""")


def highlight_svg(p: tuple) -> str:
    _, _, _, _, _, _, accent, hl0, hl1, hl_stroke, *_ = p
    m = GEO["hl_m"]
    W, H = 64, m["T"] + 25 + m["B"]          # 64 x 51
    # arch capsule; its left shoulder (x 2..22) sits in the unscaled corner,
    # carrying the staff note glyph above it
    cap = "M2,49 V27 Q2,19 10,19 H54 Q62,19 62,27 V49 Z"
    return svg_doc(W, H, f"""
    <defs><linearGradient id="w" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{hl0}"/><stop offset="1" stop-color="{hl1}"/></linearGradient></defs>
    <path d="{cap}" fill="url(#w)" stroke="{hl_stroke}" stroke-width="1.2"/>
    <line x1="5" y1="47" x2="59" y2="47" stroke="{hl_stroke}" stroke-opacity=".35" stroke-width=".8"/>
    {glyph_fit("E", 11, 11, 13, f'fill="{accent}"')}""")


def menu_panel_svg(p: tuple) -> str:
    p0, p1, line = p[0], p[1], p[5]
    return svg_doc(96, 64, f"""
    <defs><linearGradient id="m" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{p0}"/><stop offset="1" stop-color="{p1}"/></linearGradient></defs>
    <path d="M3,3 H93 V61 H3 Z" fill="url(#m)"/>
    <path d="M3,3 H93 V61 H3 Z" fill="none" stroke="{line}" stroke-opacity=".65" stroke-width="1"/>""")


def menu_highlight_svg(p: tuple) -> str:
    hl0, hl1, hl_stroke = p[7], p[8], p[9]
    return svg_doc(64, 24, f"""
    <defs><linearGradient id="h" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{hl0}"/><stop offset="1" stop-color="{hl1}"/></linearGradient></defs>
    <rect x="2" y="2" width="60" height="20" rx="9" fill="url(#h)" stroke="{hl_stroke}" stroke-width=".8"/>""")


def arrow_svg(p: tuple) -> str:
    return svg_doc(12, 12, f'<path d="M4.5,2.5 L9.5,6 L4.5,9.5" fill="none" stroke="{p[5]}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')


def theme_conf(p: tuple) -> str:
    p0, p1, _bg0, _bg1, _badge, line, accent, hl0, _hl1, hl_stroke, text, hl_text, label, hl_label, name = p
    tm, cm, pm, hm = GEO["text_margin"], GEO["content_margin"], GEO["panel_m"], GEO["hl_m"]
    return f"""# vim: ft=dosini
[Metadata]
Name={DISPLAY_NAME} {name}
Version=1.1
Author=Liushenwuzhu-Alpaca
Description=Hymmnos Hymn Score fcitx5 skin, {name} palette. Fan-made, not affiliated with GUST/Banpresto/KOEI TECMO.
ScaleWithDPI=True

[InputPanel]
NormalColor={text}
HighlightCandidateColor={hl_text}
HighlightColor={text}
HighlightBackgroundColor=#00000000
CandidateLabelColor={label}
HighlightCandidateLabelColor={hl_label}

[InputPanel/Background]
Image=panel.svg
Color=#0e0e0e
BorderColor=#00000000
BorderWidth=0
Overlay=badge.svg
Gravity=Center Left
OverlayOffsetX=2
OverlayOffsetY=0

[InputPanel/Background/Margin]
Left={pm['L']}
Right={pm['R']}
Top={pm['T']}
Bottom={pm['B']}

[InputPanel/Highlight]
Image=highlight.svg
Color=#00000000
BorderColor=#00000000

[InputPanel/Highlight/Margin]
Left={hm['L']}
Right={hm['R']}
Top={hm['T']}
Bottom={hm['B']}

[InputPanel/TextMargin]
Left={tm['L']}
Right={tm['R']}
Top={tm['T']}
Bottom={tm['B']}

[InputPanel/ContentMargin]
Left={cm['L']}
Right={cm['R']}
Top={cm['T']}
Bottom={cm['B']}

[InputPanel/BlurMargin]
Left=16
Right=16
Top=16
Bottom=16

[Menu]
NormalColor={text}
HighlightCandidateColor={hl_text}
Spacing=4

[Menu/Background]
Image=menu-panel.svg
Color={p0}
BorderColor={line}
BorderWidth=0

[Menu/Background/Margin]
Left=6
Right=6
Top=6
Bottom=6

[Menu/Highlight]
Image=menu-highlight.svg
Color={hl0}
BorderColor=#00000000

[Menu/Highlight/Margin]
Left=2
Right=2
Top=2
Bottom=2

[Menu/TextMargin]
Left=8
Right=8
Top=4
Bottom=4

[Menu/ContentMargin]
Left=3
Right=3
Top=3
Bottom=3

[Menu/Separator]
Color={line}66

[Menu/SubMenu]
Image=arrow.svg
"""


def build_theme(palette_id: str, p: tuple) -> Path:
    out = DIST / f"{THEME_PREFIX}-{palette_id}"
    if out.exists():
        for stale in out.iterdir():
            stale.unlink()
    out.mkdir(parents=True, exist_ok=True)
    (out / "panel.svg").write_text(panel_svg(p))
    (out / "badge.svg").write_text(badge_svg(p))
    (out / "highlight.svg").write_text(highlight_svg(p))
    (out / "menu-panel.svg").write_text(menu_panel_svg(p))
    (out / "menu-highlight.svg").write_text(menu_highlight_svg(p))
    (out / "arrow.svg").write_text(arrow_svg(p))
    (out / "theme.conf").write_text(theme_conf(p))
    return out


def main() -> None:
    DIST.mkdir(exist_ok=True)
    for pid, p in PALETTES.items():
        print(build_theme(pid, p).name)


if __name__ == "__main__":
    main()
