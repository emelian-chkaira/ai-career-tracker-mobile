"""Renders the infographic SVGs to PNG (1.5x) with Playwright's Chromium.
Run:  python3 docs/media/render_png.py   (needs `pip install playwright && playwright install chromium`)."""
import re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

here = Path(__file__).parent
with sync_playwright() as p:
    b = p.chromium.launch()
    for svg in sorted(here.glob("*.svg")):
        w, h = map(int, re.search(r'viewBox="0 0 (\d+) (\d+)"', svg.read_text()).groups())
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1.5)
        pg.goto(svg.as_uri()); pg.screenshot(path=str(svg.with_suffix(".png")))
        print("wrote", svg.with_suffix(".png").name)
    b.close()
