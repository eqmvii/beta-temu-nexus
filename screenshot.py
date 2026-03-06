#!/usr/bin/env python3
"""
Screenshot utility for temu-nexus HTML mocks.

Usage:
  python3 screenshot.py                   # full-page screenshot
  python3 screenshot.py --section NAME    # crop to a named section

Named sections (approximate Y ranges on 1280px-wide viewport):
  header        top of page
  hero          slider area
  top-articles  2 cards + ad row
  community     explore the community banner
  collections   featured collections
  popular       popular in community
  footer        newsletter + footer
"""
import sys
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE    = Path(__file__).parent.resolve()
HTML    = HERE / "index.html"
OUT_DIR = HERE / "examples"

# Named sections: (scroll_to_y, capture_height) at 1280px wide.
# scroll_to_y  — page Y to scroll to before capturing
# height       — how many px tall to capture from top of viewport
SECTIONS = {
    "header":       (0,    150),
    "hero":         (75,   520),
    "top-articles": (540,  440),
    "community":    (1060, 400),   # community banner + leaderboard below it
    "collections":  (1420, 500),   # leaderboard bottom + full collections row
    "popular":      (1780, 560),
    "newsletter":   (2271, 250),
    "footer":       (2500, 436),
}

VIEWPORT_H = 900

def take_screenshot(section=None):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": VIEWPORT_H})
        page.goto(f"file://{HTML}")
        page.wait_for_timeout(800)  # let fonts + JS render

        if section:
            entry = SECTIONS.get(section)
            if not entry:
                print(f"Unknown section '{section}'. Available: {', '.join(SECTIONS)}")
                browser.close()
                return
            scroll_y, capture_h = entry
            # Scroll to position, then clip from top of viewport
            page.evaluate(f"window.scrollTo(0, {scroll_y})")
            page.wait_for_timeout(150)
            clip = {"x": 0, "y": 0, "width": 1280, "height": min(capture_h, VIEWPORT_H)}
            out = OUT_DIR / f"section-{section}.png"
            page.screenshot(path=str(out), clip=clip)
            print(f"Section '{section}' screenshot → {out}")
        else:
            out = OUT_DIR / "current.png"
            page.screenshot(path=str(out), full_page=True)
            print(f"Full-page screenshot → {out}")

        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--section", "-s", help="Named section to crop to")
    args = parser.parse_args()
    take_screenshot(section=args.section)
