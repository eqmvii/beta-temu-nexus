# RFP CAS Mock — Swap Specification

Reference template: `rfp-cas.html`

Each swappable element is marked with an HTML comment `<!-- SWAP:ID — description -->`.
This document enumerates every swap point, what fields to change, and where to find them.

---

## Branding (3 items)

### B1 — Page `<title>`
- **Location:** `<head>` > `<title>`
- **Current:** `Parenting and Migraine: Guilt, Genetics, and Coping Tips — Migraine.com`
- **Swap:** Replace CAS topic and community site name
- **Format:** `[CAS Topic] — [Site Name]`

### B2 — Favicon
- **Location:** `<head>` > `<link rel="icon">`
- **Current:** `https://migraine.com/favicon.ico`
- **Swap:** URL to target community's favicon
- **Pattern:** `https://[community-domain]/favicon.ico`

### B3 — Site logo
- **Location:** `<header>` > `a.site-logo`
- **Fields to swap:**
  - `aria-label` — currently `"Migraine.com home"`
  - `img src` — currently `https://migraine.com/images/logo_avatar.svg`
  - `img alt` — currently `"Migraine.com"`
- **Pattern:** `https://[community-domain]/images/logo_avatar.svg`

---

## Page Heading (1 item)

### H1 — CAS heading
- **Location:** `div.cas-heading` > `h1`
- **Current:** `Parenting and Migraine: Guilt, Genetics, and Coping Tips`
- **Swap:** The CAS topic/title for the target campaign

---

## Feature Article (1 item, with image)

### F1 — Feature article
- **Location:** `div.feature-section` (full-width dark-background hero)
- **Fields to swap:**
  - `style="background: #2C3B5C"` — background color for the feature band
  - `img src` — currently `https://migraine.com/wp-content/uploads/2019/11/M-67484-hub-img-left_5.jpg`
  - `img alt` — currently `"Migraine Doesn't Make You a Bad Parent image"`
  - `h2 > a` text — currently `"Migraine Doesn't Make You a Bad Parent"`
  - `p` text — currently `"Insecurity and self-esteem issues often go hand-in-hand..."`
- **Image specs:** 500px wide, flexible height, `object-fit: cover`

---

## Main Column Articles (4 items; first 3 have images, last 1 text-only)

### M1 — Main article 1 (has image)
- **Location:** 1st `article.cas-teaser` in `.cas-columns__main`
- **Fields to swap:**
  - `img src` — currently `https://migraine.com/wp-content/uploads/2017/10/98368_custom-1080x412.jpg`
  - `img alt`
  - `h2 > a` text — currently `"Unique Symptoms of Childhood Migraines"`
  - `p.cas-teaser__summary` text
- **Image specs:** max-width 72% of main column, aspect ~1080x412

### M2 — Main article 2 (has image)
- **Location:** 2nd `article.cas-teaser`
- **Fields to swap:**
  - `img src` — currently `https://migraine.com/.../M-109536-parenting-children-with-migraine-custom-1080x412.jpg`
  - `img alt`
  - `h2 > a` text — currently `"Circle of Life: Parenting a Child who has Migraine"`
  - `p.cas-teaser__summary` text
- **Image specs:** same as M1

### M3 — Main article 3 (has image)
- **Location:** 4th `article.cas-teaser` (after the poll)
- **Fields to swap:**
  - `img src` — currently `https://migraine.com/.../migraine-parenting-107982-custom_edit-1080x412.jpg`
  - `img alt`
  - `h2 > a` text — currently `"Three Ways Migraine Prepared Me to Be a Parent"`
  - `p.cas-teaser__summary` text
- **Image specs:** same as M1

### M4 — Main article 4 (NO image)
- **Location:** 5th `article.cas-teaser`
- **Fields to swap:**
  - `h2 > a` text — currently `"I'm a Stay-At-Home-Mom with Migraines: Here's My Plan"`
  - `p.cas-teaser__summary` text

---

## Sidebar Articles (2 items; both text-only)

### S1 — Sidebar article 1 (NO image)
- **Location:** 1st `article.sidebar-teaser`
- **Fields to swap:**
  - `h3 > a` text — currently `"Parenting While Managing a Chronic Illness"`
  - `p.sidebar-teaser__summary` text

### S2 — Sidebar article 2 (NO image)
- **Location:** 2nd `article.sidebar-teaser`
- **Fields to swap:**
  - `h3 > a` text — currently `"Life with Chronic Migraine Mommy"`
  - `p.sidebar-teaser__summary` text

---

## Ads (3 items, 3 different sizes)

All three ads share the same solid background color (`#6b3fa0`) and display only the brand name centered in white. Fields to swap per ad:
- `style="background:#6b3fa0"` — background color
- `.fake-ad__brand` — brand name or logo text

### A1 — Leaderboard ad
- **Location:** `div.cas-leaderboard` (top of page, below header)
- **Size:** 728 x 90
- **Current brand:** Chillaxa

### A2 — Sidebar square ad
- **Location:** top of `.cas-columns__sidebar`
- **Size:** 300 x 250
- **Current brand:** Chillaxa

### A3 — Sidebar half-page ad
- **Location:** bottom of `.cas-columns__sidebar`
- **Size:** 300 x 600
- **Current brand:** Chillaxa

---

## Poll (1 item)

### P1 — Community poll
- **Location:** `div.poll` (between M2 and M3 in main column)
- **Fields to swap:**
  - `p.poll__question` — currently `"Does migraine affect your parenting?"`
  - 3x `span.poll-radio__label` — currently:
    1. `"Yes, significantly"`
    2. `"Somewhat"`
    3. `"Not very much"`

---

## Summary table

| ID | Type | Has image? | Image size | Location |
|----|------|-----------|------------|----------|
| B1 | Branding | — | — | `<title>` |
| B2 | Branding | — | — | `<link>` favicon |
| B3 | Branding | logo | 48x48 SVG | Header |
| H1 | Heading | — | — | Main `<h1>` |
| F1 | Feature | yes | 500px wide | Full-width hero band |
| M1 | Article | yes | 1080x412 | Main column, 1st |
| M2 | Article | yes | 1080x412 | Main column, 2nd |
| M3 | Article | yes | 1080x412 | Main column, 4th (after poll) |
| M4 | Article | no | — | Main column, 5th |
| S1 | Article | no | — | Sidebar, 1st |
| S2 | Article | no | — | Sidebar, 2nd |
| A1 | Ad | — | 728x90 | Leaderboard (top) |
| A2 | Ad | — | 300x250 | Sidebar (top) |
| A3 | Ad | — | 300x600 | Sidebar (bottom) |
| P1 | Poll | — | — | Main column (between M2 & M3) |

**Total: 14 swap points across 3 branding items, 1 heading, 7 articles, 3 ads, and 1 poll.**
