"""Shared drawing helpers for the README infographics (app-architecture.svg, app-how-it-works.svg)."""
from pathlib import Path
from xml.sax.saxutils import escape

out: list[str] = []
COLORS = {"violet": "#8b5cf6", "blue": "#2563eb", "green": "#16a34a", "orange": "#ea580c", "red": "#dc2626", "teal": "#0891b2", "brown": "#a16207", "pink": "#db2777", "gray": "#64748b"}


def t(x, y, s, size=14, weight=600, fill="#0f172a", anchor="middle", italic=False):
    out.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{" font-style=\"italic\"" if italic else ""}>{escape(s)}</text>')


def pill(cx, cy, s, bg, fg="#fff", size=14, pad=12):
    w = len(s) * size * 0.58 + pad * 2
    out.append(f'<rect x="{cx - w / 2}" y="{cy - size}" width="{w}" height="{size * 1.9}" rx="7" fill="{bg}" stroke="#0f172a" stroke-opacity=".15"/>')
    t(cx, cy + size * 0.33, s, size, 800, fg)


def card(x, y, w, h, stroke, fill, title=None, title_bg=None, dash=False):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="2.2"{" stroke-dasharray=\"7 6\"" if dash else ""}/>')
    if title: pill(x + w / 2, y, title, title_bg or stroke, size=15)


def icon(cx, cy, emoji, size=40, ring=None):
    if ring: out.append(f'<circle cx="{cx}" cy="{cy - size * 0.32}" r="{size * 0.78}" fill="{ring}" opacity=".18"/>')
    t(cx, cy, emoji, size, 400)


def chip(cx, cy, s, bg, fg="#0f172a", size=12.5):
    w = len(s) * size * 0.56 + 18
    out.append(f'<rect x="{cx - w / 2}" y="{cy - 15}" width="{w}" height="26" rx="13" fill="{bg}" stroke="#0f172a" stroke-opacity=".12"/>')
    t(cx, cy + 3, s, size, 700, fg)


def cyl_h(x, y, w, h, color, label, sub=None):
    """Horizontal cylinder (a queue), like the reference picture."""
    r = h / 2
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>')
    out.append(f'<ellipse cx="{x}" cy="{y + r}" rx="{r * .45}" ry="{r}" fill="{color}"/>')
    out.append(f'<ellipse cx="{x + w}" cy="{y + r}" rx="{r * .45}" ry="{r}" fill="#fff" stroke="{color}" stroke-width="3"/>')
    out.append(f'<rect x="{x}" y="{y + 6}" width="{w}" height="{h * .18}" fill="#fff" opacity=".25"/>')
    t(x + w / 2, y + h + 22, label, 14, 800)
    if sub: t(x + w / 2, y + h + 40, sub, 12, 500, "#475569")


def cyl_v(cx, y, w, h, color, label, sub=None):
    """Vertical cylinder (a database)."""
    rx, ry = w / 2, w * .16
    out.append(f'<path d="M{cx - rx},{y} v{h} a{rx},{ry} 0 0 0 {w},0 v{-h}" fill="{color}"/>')
    out.append(f'<ellipse cx="{cx}" cy="{y}" rx="{rx}" ry="{ry}" fill="#fff" stroke="{color}" stroke-width="3"/>')
    for k in (h * .38, h * .72): out.append(f'<path d="M{cx - rx},{y + k} a{rx},{ry} 0 0 0 {w},0" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="2"/>')
    t(cx, y + h + ry + 22, label, 13.5, 800)
    if sub: t(cx, y + h + ry + 39, sub, 11.5, 500, "#475569")


def arrow(pts, color, label=None, at=0.5, both=False, dash=True, lx=0, ly=0, label_bg="#fff7ed"):
    c = COLORS[color]
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="3"{" stroke-dasharray=\"9 7\"" if dash else ""} marker-end="url(#m-{color})"{f" marker-start=\"url(#s-{color})\"" if both else ""}/>')
    if label:
        i = max(0, min(len(pts) - 2, int((len(pts) - 1) * at)))
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        mx, my = (x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly
        w = len(label) * 6.9 + 16
        out.append(f'<rect x="{mx - w / 2}" y="{my - 13}" width="{w}" height="24" rx="6" fill="{label_bg}" stroke="{c}" stroke-width="1.5" transform="rotate(-4 {mx} {my})"/>')
        out.append(f'<text x="{mx}" y="{my + 4}" font-size="12.5" font-weight="700" fill="{c}" text-anchor="middle" transform="rotate(-4 {mx} {my})">{escape(label)}</text>')




def diamond(cx, cy, lines, color, w=110, h=84):
    out.append(f'<path d="M{cx},{cy - h / 2} L{cx + w / 2},{cy} L{cx},{cy + h / 2} L{cx - w / 2},{cy} z" fill="#fef9c3" stroke="{color}" stroke-width="2.2"/>')
    for i, s in enumerate(lines): t(cx, cy + 4 + (i - (len(lines) - 1) / 2) * 14, s, 11.5, 800, "#713f12")


def node(cx, cy, emoji, name, color, subs=(), ring=None):
    """An icon, a coloured name pill and up to two grey lines under it."""
    icon(cx, cy, emoji, 36, ring or color); pill(cx, cy + 34, name, color, size=13)
    for i, s in enumerate(subs): t(cx, cy + 62 + i * 16, s, 11.5, 600, "#475569")


def save(name, W, H):
    defs = "".join(f'<marker id="m-{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
                   f'<marker id="s-{n}" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for n, c in COLORS.items())
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Inter, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif">'
           f"<defs>{defs}</defs>" + "".join(out) + "</svg>")
    Path(__file__).with_name(name).write_text(svg)
    out.clear()
    print("wrote", name)
