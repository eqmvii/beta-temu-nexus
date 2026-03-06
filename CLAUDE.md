# temu-nexus — Static HTML Mocks

Self-contained static HTML mocks of migraine.com pages, intended for deployment to GitHub Pages. Each page is a single `.html` file with all CSS and JS embedded inline — no build step, no dependencies, opens directly in a browser via `file://`.

## Scope

**Desktop only.** Mobile responsiveness is intentionally out of scope for this version. Design at 1280px viewport width. Do not get confused by code in the nexus3 folder that handles mobile structure, it is different!

## Files

| File | Description |
|---|---|
| `index.html` | Homepage mock — complete |
| `post.html` | *(next)* Single article page — reuse header/footer from index.html |
| `screenshot.py` | Playwright screenshot utility (see below) |
| `examples/` | Reference screenshots and generated output |

## Iteration Workflow

**Always use the screenshot tool to verify before presenting work.** The loop is:
1. Edit HTML/CSS/JS in `index.html`
2. Run `python3 screenshot.py --section <name>` to capture that section
3. Read the resulting PNG with the Read tool to visually inspect it
4. Iterate until it matches prod, then show the user

For sections not covered by named sections, use the full-page clip approach:
```python
page.screenshot(path=..., full_page=True, clip={"x":0, "y": Y, "width":1280, "height": H})
```

**Never present work to the user without first screenshotting and visually verifying it yourself.**

## Screenshot Utility

Requires Python 3 + Playwright (already installed).

```bash
# Full-page screenshot → examples/current.png
python3 screenshot.py

# Crop to a named section → examples/section-{name}.png
python3 screenshot.py --section header
python3 screenshot.py --section hero
python3 screenshot.py --section top-articles
python3 screenshot.py --section community
python3 screenshot.py --section collections
python3 screenshot.py --section popular
python3 screenshot.py --section newsletter
python3 screenshot.py --section footer
```

### Current SECTIONS Y-values (screenshot.py)

```python
SECTIONS = {
    "header":       (0,    150),
    "hero":         (75,   520),
    "top-articles": (540,  440),
    "community":    (1060, 400),
    "collections":  (1420, 500),
    "popular":      (1780, 560),
    "newsletter":   (2271, 250),
    "footer":       (2500, 436),
}
```

If page layout shifts significantly, re-measure Y positions by running JS in Playwright:
```python
page.evaluate("""() => {
    const el = document.querySelector('.my-section');
    return Math.round(el.getBoundingClientRect().top + window.scrollY);
}""")
```

## nexus3 Source Reference

Always check `../nexus3/` before inventing component styles or icons. Key locations:
- `../nexus3/assets/stylesheets/components/` — SCSS for every component
- `../nexus3/assets/icons/` — All SVG icons (ribbon, like, text-bubble, accessibility, etc.)
- `../nexus3/components/` — Vue components for structure/template reference

**Icons used so far** (inline SVG paths, fill-based):
- `ribbon.svg` — bookmark button (used in post teasers + hero carousel)
- `like.svg` — reactions pill in engagement bar
- `text-bubble.svg` — comments pill in engagement bar
- `accessibility.svg` — header accessibility button (the crossed-eye icon)

## Design Tokens

All CSS custom properties are defined in `:root` at the top of each HTML file:

| Token | Value | Usage |
|---|---|---|
| `--cyan` | `#379EC1` | Links, buttons, active dots, engagement icons |
| `--cyan-dark` | `#002E3B` | Headings, footer bg |
| `--cyan-darker` | `#002029` | Header bg, body text |
| `--cyan-lighter` | `#EAF8FC` | Hero slider bg, engagement pill bg |
| `--brand` | `#1E7EBE` | Primary CTA buttons, tags, subscribe pill |
| `--hu-lighter` | `#ECF0F3` | Footer-signup bg, card borders |
| `--hu-lightest` | `#F5F7F9` | Section backgrounds |
| `--max-w` | `1080px` | Max content width |
| `--header-h` | `48px` | Fixed header height |
| `--announce-h` | `32px` | Fixed announce bar height |

**Fixed layer order (top to bottom):**
1. Header — `position:fixed; top:0; z-index:299`
2. Announce bar — `position:fixed; top:var(--header-h); z-index:298`
3. Body padding-top — `calc(var(--header-h) + var(--announce-h))` = 80px

## Page Structure (index.html) — Current State

1. Header (fixed, `#002029`) — logo far-left, ☰ Menu, 🔍 Search | Accessibility, Log in, Subscribe pill
2. Announce bar (fixed, below header) — "Tell us about your symptom..."
3. Site masthead logo — migraine.com SVG logo, centered
4. Homepage slider (hero carousel) — full-bleed `#EAF8FC`, 3 slides, dot+arrow nav, bookmark icon in byline
5. Top articles — 2 post teasers (no image, with excerpt + engagement bar + bookmark) + square ad
6. "Read recent articles" CTA — centered under the 2 card columns only (margin-right: calc(300px + 20px))
7. Explore the Community banner — full-bleed brand blue
8. Leaderboard ad (Emgality®)
9. Featured Collections — 2 clickable tiles + square ad
10. Popular in the Community — "Explore forums/stories" category links + eng-teaser cards + poll
11. Newsletter / footer-signup — horizontal row: form left, dark social icons right, `#ECF0F3` bg
12. Footer — dark `#002E3B` bg, Health Union logo + communities list

## Post Teaser Anatomy

The `post-card` class (used in top-articles and popular section) follows prod's `post-teaser` structure:
```
.post-card
  .post-card__body
    .post-type          (e.g. "STORY")
    .post-card__title   (Merriweather, 16px bold)
    .post-card__summary (excerpt, 14px)
    .post-card__footer  (flex row: byline left, bookmark-btn right)
    .post-card__engagement
      .eng-action       (cyan-lighter pill: icon + count + label)
```

Icons are module-level JS constants `ICON_LIKE`, `ICON_COMMENT`, `ICON_RIBBON` — defined before `renderSlider()` so all render functions can access them.

## Fake Data Arrays

| Variable | Contents |
|---|---|
| `slides` | Hero carousel (3 items): title, summary, author, readTime, type, imgSrc/imgColor, authorColor |
| `recents` | Top-articles cards (2 items): type, title, excerpt, author, authorColor, readTime, reactions, comments |
| `collections` | Featured collection tiles (2 items): title, imgSrc or imgColor |
| `popularArticles` | Popular section (2 items): category, categoryLabel, title, excerpt, author, authorInitials, authorColor, reactions |
| `ads` | `leaderboard2`, `square` — fake pharma/sponsor ad copy with CSS gradient bg |

## Ad Slots

Rendered by `renderAd(containerId, adData, type)`. Types: `'leaderboard'` (728×90) or `'square'` (300×250). Each slot has an "Advertisement" label above it. **No leaderboard ad at the top** — that space is the masthead logo.

## Interactivity

| Action | Behavior |
|---|---|
| Hamburger / Menu btn | Slides in nav drawer from left; overlay closes it |
| Log in button | Hides itself, shows green avatar button |
| Search icon | Drops down search panel below header |
| Carousel dots / arrows | Cycles through 3 hero slides |
| Poll submit | Visual only |
| Newsletter subscribe | Visual only |

## Building post.html (Next Session)

Copy the `<!-- BEGIN HEADER -->...<!-- END HEADER -->` and `<!-- BEGIN FOOTER -->...<!-- END FOOTER -->` blocks verbatim from `index.html`. The post page will need:
- Same fixed header + announce bar
- Site masthead logo (same as homepage)
- Article hero image (full-width or contained)
- Article title, byline, read time, post type tag
- Article body content (lorem ipsum paragraphs)
- Engagement bar (reactions + comments) below article
- Bookmark button
- Related articles or "More from the community" section
- Same newsletter/footer-signup + footer

## Conventions

- Fonts: `'Lato'` (body), `'Merriweather'` (headings) via Google Fonts CDN
- BEM-ish class naming, matching nexus3 component classes where possible
- No external JS libraries
- Inline SVG for all icons (sourced from `../nexus3/assets/icons/`)
- Images: real migraine.com CDN URLs where available, CSS gradients as fallback
- Favicon: inline SVG data URI of the M circle in `--brand` blue
