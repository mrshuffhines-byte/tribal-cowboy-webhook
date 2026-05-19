# Tribal Cowboy Social Media Operating System

**Business:** Tribal Cowboy LLC — Indigenous-owned equine experience, Athol, Idaho
**Owner:** Stacie (Nisenan Maidu)
**Website:** www.tribalcowboy.com | **Instagram:** @TribalCowboy | **Email:** info@tribalcowboy.com

---

## System Overview

This is a multi-agent social media and monetization operating system for Tribal Cowboy LLC. It is not a post scheduler. It is not a content calendar app. It is a full content strategy, brand voice, funnel, and creator income infrastructure — managed through Claude Code with structured documents and draft files.

The system serves four revenue streams in priority order:

1. **Creator income** — brand deals, sponsored content, UGC licensing
2. **Brand deals and partnerships** — lifestyle, western, outdoor, tourism sponsors
3. **Corporate event bookings** — team events, company parties, branded experiences
4. **Premium service bookings** — pony parties, wagon rides, photography sessions

Social media is the top of the funnel for all four. Every post, every reel, every caption either builds trust, attracts a partner, or moves someone closer to booking. Nothing posts just to post.

---

## Quick Start — How to Use This Daily

**Draft a post:**
Say "Draft an Instagram post about [topic]" — Claude writes caption + hashtags + suggested posting time. Drafts save to `content/drafts/` as `.md` files named `YYYY-MM-DD-platform-topic.md`.

**Plan content:**
Say "Plan this week's content" or "Give me 5 post ideas for [month/event]." Claude will rotate through content pillars and flag which posts serve which funnel stage.

**Research competitors:**
Say "Research [account] on Instagram" or "Find top horse content on TikTok." Claude uses Apify tools to scrape and analyze.

**Repurpose content:**
Say "Turn this caption into a TikTok script" or "Make a Facebook version of this." Claude reformats for the platform without just copy-pasting.

**Draft a pitch:**
Say "Draft a brand partnership pitch for [company type]." Claude writes an outreach email using the brand voice guide and positioning docs.

**Update the calendar:**
Say "Add this event to the content calendar." Claude updates the relevant file in `content/calendar/`.

**Approval rule:** Nothing posts without Stacie's review. Claude drafts. Stacie approves and posts.

---

## File Structure

```
TribalCowboy-Social/
│
├── README.md                          ← This file. System operating manual.
├── CLAUDE.md                          ← Instructions for Claude Code agents
│
├── docs/
│   ├── brand-profile.md               ← Who Tribal Cowboy is, positioning, revenue model
│   ├── voice-guide.md                 ← Brand voice, tone by platform, do/don't, banned phrases
│   ├── audience-personas.md           ← 6 detailed audience personas
│   ├── content-pillars.md             ← 8 content pillars with post formats and examples
│   ├── funnel-strategy.md             ← Full funnel: Discover → Trust → Book → Advocate
│   └── website-funnel-map.md          ← Website page structure, missing pages, SEO, CTAs
│
├── content/
│   ├── drafts/                        ← Drafted posts awaiting review
│   │   └── YYYY-MM-DD-platform-topic.md
│   ├── templates/                     ← Reusable caption templates by post type
│   │   ├── pony-party-recap.md
│   │   ├── corporate-inquiry-cta.md
│   │   ├── animal-personality.md
│   │   └── booking-open.md
│   └── calendar/                      ← Monthly content plans
│       └── 2026-03-calendar.md
│
└── insights/                          ← Notes on what's working, trends, competitor findings
    └── YYYY-MM-insights.md
```

---

## Agent Directory

| Agent / Document | Purpose |
|---|---|
| `brand-profile.md` | Source of truth for who TC is and what it stands for — referenced before any positioning decision |
| `voice-guide.md` | Governs every word written for Tribal Cowboy — captions, pitches, emails, bios |
| `audience-personas.md` | Defines who we're talking to so content is never generic |
| `content-pillars.md` | Framework for what to post — 8 pillars with examples, platform fit, and cadence |
| `funnel-strategy.md` | Maps how followers become buyers and how content accelerates each stage |
| `website-funnel-map.md` | Connects social traffic to website pages; includes SEO targets and missing page recommendations |
| Claude Code (active) | Drafts content, researches competitors, builds pitches, updates calendars — all on command |

---

## Weekly Workflow (5-Step Summary)

1. **Monday:** Review the week's content calendar. Ask Claude to draft any posts not yet written. Confirm which pillar each post serves.
2. **Tuesday–Thursday:** Review drafts, approve or request revisions. Schedule approved posts in your platform of choice (Later, Meta Business Suite, TikTok native).
3. **Wednesday:** Engage with comments and DMs. If an inquiry comes in, refer to the funnel strategy doc for lead nurture steps.
4. **Friday:** Review what performed. Drop observations into `insights/` — no analytics tools required. Note: saves, shares, DMs are more valuable than likes.
5. **Weekend (light):** Post one organic, low-effort piece — behind the scenes, animal moment, land/season shot. These often outperform planned content.

---

## How Social Connects to the Website

Social media drives cold traffic to the website. The website closes the sale. They must work together.

- Instagram bio link points to the appropriate landing page (rotate by season/priority: pony parties in spring, corporate in fall, wagon rides in winter)
- Stories with links should go directly to the relevant service page, not the homepage
- Every post with a booking CTA needs a live URL to land on — if the page doesn't exist yet, see `website-funnel-map.md` for what to build
- The website should feel like the natural next step after someone finds TC on social — same voice, same premium positioning, no tonal whiplash

---

## How Creator Income Fits In

Tribal Cowboy is not just a service business. It is a creator-led media brand featuring an Indigenous woman running horses in North Idaho. That is rare. That is marketable.

Creator income paths:
- **Sponsored posts/reels:** Lifestyle, western, outdoor, equine brands pay for placement
- **UGC licensing:** Brands pay to license TC content for their own ads and channels
- **Brand ambassador relationships:** Ongoing paid partnerships with aligned brands (horse care, western apparel, outdoor gear, family lifestyle)
- **Tourism partnerships:** Idaho tourism boards, regional CVBs, travel brands co-marketing the experience

To attract sponsors: content must consistently demonstrate reach, engagement, and a specific aesthetic. Brand Authority posts (Pillar 8) are built specifically for this purpose. Keep a press/media kit current in `insights/`.

---

## Key Rules

1. **Approval first, always.** Claude drafts. Stacie posts. Nothing goes live without human review.
2. **No auto-posting.** This system does not connect to any posting API. It is a drafting and strategy system.
3. **Premium positioning always.** Tribal Cowboy is not a cheap pony party vendor. Every word, every photo choice, every CTA reinforces that this is a premium, owner-operated, Indigenous-led brand.
4. **Indigenous identity is not a marketing tactic.** It is part of who Stacie is. It is never used as a hook or an angle. It is present with dignity when relevant.
5. **No urgency language.** Never "book before it's too late" or "limited spots remaining." If spots are actually limited, say that plainly: "We have two open weekends in May."
6. **No AI-sounding language.** Review every draft before posting. Remove: "delve," "testament to," "seamlessly," "in conclusion," "it's worth noting," "unique experience," "making memories."
7. **Pillar rotation matters.** Never post the same pillar back to back. Max one booking/promotional post per five posts.
8. **Platform voice is different on each channel.** Do not copy-paste from Instagram to TikTok. See `voice-guide.md`.

---

## Contact

**Website:** www.tribalcowboy.com
**Email:** info@tribalcowboy.com
**Instagram:** @TribalCowboy
**Location:** Athol, Idaho — serving North Idaho and Eastern Washington
