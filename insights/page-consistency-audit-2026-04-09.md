# Tribal Cowboy Landing Page Consistency Audit
**Date:** April 9, 2026
**Pages Reviewed:** 5 service landing pages on Squarespace

---

## Summary

Three pages (Horse Photography Props, Corporate Team Building, School & Community Programs) share a consistent template. Pony Parties uses an older, different design. Carriage Rides has no landing page at all — just a plain "Weddings" heading with a paragraph.

---

## Page-by-Page Status

### 1. Horse Photography Props — GOOD (Template Standard)
- **Wrapper:** `tc-hp-wrap` | CSS: 11,631 chars
- **Hero:** Gold h1 heading on dark bg, gold border frame, plain subtitle, CTA button
- **Sections:** Stats bar → How It Works (5 steps) → What You Get (6 cards) → Why Book With Us (features) → Pricing (3 tiers) → Testimonials → FAQ (9 items) → Footer CTA with website + email
- **CTA links:** 4× "Check Availability" (title case)
- **Issues:** "Why Book With Us" heading differs from CB/SP which say "Why Tribal Cowboy"

### 2. Corporate Team Building — GOOD (Template Standard)
- **Wrapper:** `tc-cb-wrap` | CSS: 11,642 chars
- **Hero:** Gold h1 heading on dark bg, gold border frame, plain subtitle, CTA button
- **Sections:** Stats bar → How It Works (5 steps) → What's Included (6 cards) → Why Tribal Cowboy (features) → Pricing (3 tiers) → Testimonials → FAQ (9 items) → Footer CTA with website + email
- **CTA links:** 6× "Check Availability" (title case)
- **Issues:** None — cleanest page

### 3. School & Community Programs — GOOD (Template Standard)
- **Wrapper:** `tc-sp-wrap` | CSS: 11,642 chars (identical to CB)
- **Hero:** Gold h1 heading on dark bg, gold border frame, plain subtitle, CTA button
- **Sections:** Stats bar → How It Works (5 steps) → Program Options (6 cards) → Why Tribal Cowboy (features) → Pricing (3 tiers) → Testimonials → FAQ (9 items) → Footer CTA with website + email
- **CTA links:** 6× "Check Availability" (title case)
- **Issues:** None

### 4. Pony Parties — NEEDS UPDATE (Different Template)
- **Wrapper:** `tc-pp-wrap` | CSS: 8,365 chars
- **Hero:** White heading on dark bg (no gold border), has eyebrow text + italic tagline + paragraph
- **Sections:** Stats bar → How It Works (6 steps) → What's Included (10 cards) → Who Books a Pony Party (chips) → Differentiators → Testimonials (6) → Packages (3 tiers) → FAQ (10 items) → CTA → Footer row
- **CTA links:** 0 named CTA buttons (uses different class), 5 contact links, 8 website refs
- **Issues:** See "Pony Parties Differences" below

### 5. Carriage Rides — NEEDS FULL BUILD
- **No code block exists**
- Shows only a plain "Weddings" heading with a paragraph of text
- No hero, no stats, no process steps, no cards, no pricing, no FAQ, no footer
- Completely out of line with every other page

---

## Pony Parties vs. Standard Template — All Differences

| Element | HP / CB / SP (Standard) | Pony Parties |
|---------|------------------------|--------------|
| **Hero heading** | Gold h1, gold border frame | White h2, no border |
| **Eyebrow text** | None | "PONY PARTIES · NORTH IDAHO & EASTERN WASHINGTON" |
| **Hero subtitle** | Plain paragraph | Italic tagline + longer description paragraph |
| **Hero CTA** | "Check Availability" (title case) | "CHECK AVAILABILITY" (all caps) |
| **Stats bar** | 4 items, dark bg with gold border | 4 items, cream bg with gold text |
| **Section comments** | None | Organized `<!-- ── SECTION ── -->` comments |
| **Process steps** | 5 steps | 6 steps |
| **Cards section** | 6 cards | 10 cards |
| **"Why" section** | h3 "Why Book With Us" / "Why Tribal Cowboy" + feature-items | "We're Not a Rental Service" + differentiator cards |
| **Extra section** | None | "Who Books a Pony Party" with chip tags |
| **Pricing class** | `price-card` | `tc-pp-pkg` |
| **Testimonial class** | `tc-xx-testimonial` | `tc-pp-testi` |
| **FAQ count** | 9 items | 10 items |
| **Footer** | `footer-cta` + `footer-info` with CTA button | `footer-row` with links only |
| **CSS size** | ~11,640 chars | ~8,365 chars |

---

## Recommended Fixes (Priority Order)

### CRITICAL — Build Missing Page
1. **Create Carriage Rides / Clydesdale Wagon Rides landing page** using the HP/CB/SP template structure. Needs: hero, stats bar, how it works, what's included, why section, pricing, testimonials, FAQ, footer CTA.

### HIGH — Align Pony Parties to Standard Template
2. **Rebuild PP hero** to match standard: gold h1 heading, gold border frame, plain subtitle, remove eyebrow and long paragraph
3. **Standardize PP button text** from "CHECK AVAILABILITY" (all caps) to "Check Availability" (title case)
4. **Add PP CTA links** — currently has 0 named CTA buttons vs 4-6 on other pages
5. **Rename PP pricing section** from `tc-pp-pkg` class structure to `price-card` pattern
6. **Standardize PP footer** to match `footer-cta` + `footer-info` layout with CTA button

### MEDIUM — Cross-Page Consistency
7. **Standardize "Why" section heading** — HP says "Why Book With Us" while CB/SP say "Why Tribal Cowboy." Pick one pattern.
8. **Add section comments** to HP/CB/SP code blocks to match PP's organized structure (or remove from PP)
9. **Standardize testimonial class names** across all pages

### LOW — Nice to Have
10. **Consider adding "Who It's For" section** to HP/CB/SP (PP has this, others don't)
11. **Equalize FAQ counts** — PP has 10, others have 9
12. **Add contact links** to HP — currently has 0 vs PP's 5 and CB/SP's contact references

---

## Navigation & Linking Notes

All 5 pages currently sit under "Not Linked" in Squarespace — none are connected to the main navigation dropdown under Services. They need to be either moved under the Services page as dropdown items or linked from the Services page directly.

The nav bar shows: HOME | ABOUT | SERVICES | BOOKING | PHOTOGRAPHY | CONTACT | EVENTS — but clicking Services doesn't dropdown to these landing pages.

---

## What "Match" Means — The Target Standard

The HP/CB/SP template is the standard to match. It follows the Tribal Cowboy brand system:
- Timber Dark (#2C2520) hero background
- Warm Gold (#D4A843) heading text + border accents
- Buckskin Cream (#F3EDE3) content backgrounds
- Gold CTA buttons with #1E1208 text (AAA contrast)
- Consistent section flow: Hero → Stats → Process → Cards → Why → Pricing → Testimonials → FAQ → Footer CTA
- Professional footer with website, email, and CTA
