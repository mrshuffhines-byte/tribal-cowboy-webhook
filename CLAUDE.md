# Tribal Cowboy Webhook — Project Guide

## What This Project Is

A Node.js/Express webhook server and single-page dashboard for **Tribal Cowboy LLC** — an event planning and entertainment company. The server aggregates real-time social media analytics (Instagram, Facebook, TikTok), manages voice inquiries from an AI assistant (ElevenLabs), integrates with appointment scheduling (Acuity), and sends SMS follow-ups (Twilio).

The dashboard (`index.html`) is a single-page app with tabs for: Overview, Tasks, Instagram, Facebook, TikTok, Email Tracker, Voice Leads, Bookings, and CRM.

## Tech Stack

- **Backend:** Node.js + Express
- **Frontend:** Vanilla JS single-page app (no framework)
- **Storage:** File-based JSON (`data.json`) — survives Render free-tier spin-downs
- **Deployment:** Render (PaaS)
- **External APIs:** Meta Graph API v19, Acuity Scheduling, Twilio, ElevenLabs

## Running the Project

```bash
npm start          # production
npm run dev        # development with auto-restart (requires nodemon)
```

Server runs on port 3000 by default (or `PORT` env var on Render).

## Environment Variables

```
META_ACCESS_TOKEN      # Facebook/Instagram Graph API token
IG_USER_ID             # Instagram business account ID
FB_PAGE_ID             # Facebook page ID
ACUITY_USER_ID         # Acuity Scheduling user ID
ACUITY_API_KEY         # Acuity API key
ACUITY_BOOKING_URL     # Public booking page URL (e.g. https://www.tribalcowboy.com)
TWILIO_ACCOUNT_SID     # Twilio account SID
TWILIO_AUTH_TOKEN      # Twilio auth token
TWILIO_PHONE_NUMBER    # Twilio phone number (e.g. +12085551234)
VERIFY_TOKEN           # Meta webhook verification token (default: tribalcowboy2024)
PORT                   # Server port (set automatically by Render)
```

## Key API Endpoints

| Method | Route | Purpose |
|--------|-------|---------|
| GET | `/` | Serve dashboard |
| GET | `/health` | Health check with config status |
| GET | `/data` | Return latest IG/FB stats + voice inquiries |
| POST | `/refresh` | Trigger immediate Meta data pull |
| GET/POST | `/webhook` | Meta webhook verification + event receiver |
| POST | `/voice-inquiry` | Receive voice inquiry from ElevenLabs |
| GET | `/voice-inquiries` | List all voice inquiries |
| PATCH | `/voice-inquiry/:id` | Update inquiry status (New → Contacted → Booked) |
| GET | `/acuity/availability` | Check available dates |
| GET | `/acuity/appointment-types` | List appointment types |
| GET | `/acuity/times` | Get time slots for a date |
| POST | `/acuity/book` | Create booking |
| POST | `/send-booking-link` | Send booking link via SMS |

## Data Model (data.json)

```js
{
  instagram: { followers, reach, impressions, profile_views, posts[], comments[], last_updated },
  facebook: { followers, reach, engagement, views, posts[], last_updated },
  voice_inquiries: [{
    id, caller_name, service_requested, event_date,
    guest_count, event_location, phone_number, notes, source,
    status,          // New | Contacted | Booked
    sms_sent,        // boolean
    received_at, updated_at, acuity_id
  }]
}
```

## Claude Code Agents (.claude/agents/)

Eight specialized agents for Tribal Cowboy business operations:

| Agent File | Purpose | Invoke When |
|---|---|---|
| `social.md` | Instagram/Facebook/TikTok content, captions, hashtags, growth | Creating social content or planning posts |
| `get-paid.md` | Converts free requests into paid work, pricing scripts | Someone asks for free work or you need pricing help |
| `council.md` | 5-voice advisory board for decisions and strategy | Important decisions, email reviews, idea vetting — also use `/council` |
| `booking-closer.md` | Lead follow-up sequences via SMS/Acuity | Reviewing voice leads, drafting follow-up messages |
| `email-writer.md` | Proposals, pitches, client communications | Writing any business email |
| `brand-design.md` | Full visual identity system — colors, fonts, themes | Design work, new materials, UI consistency |
| `community.md` | School/nonprofit partnerships, tiered pricing | Schools or nonprofits requesting services |
| `brand-voice.md` | Reviews all content before it goes out | Before publishing any public-facing content |

### /council Slash Command

Use `/council [your topic]` to instantly convene the advisory board on any idea, email, or decision. It brings 5 perspectives: Strategist, Money Mind, Brand Guardian, Devil's Advocate, Community Voice.

## n8n Workflows (n8n-workflows/)

Nine importable workflows for n8n.cloud (`stacieh.app.n8n.cloud`):

| File | Trigger | What It Does |
|---|---|---|
| `01-social.json` | Daily 7am | Generates IG/FB/TikTok content, emails it + saves to Google Sheets |
| `02-get-paid.json` | Form | Responds to free requests, emails script |
| `03-council.json` | Form | Multi-perspective advisory review, emails report |
| `04-booking-closer.json` | Daily 9am | Fetches leads, sends SMS via Twilio, updates status, emails confirmation |
| `05-email-writer.json` | Form | Drafts professional emails, sends to inbox |
| `06-brand-design.json` | Form | Generates design specs, emails guidance |
| `07-community.json` | Form | Creates school/nonprofit proposals, emails them |
| `08-brand-voice.json` | Form | Reviews content for brand consistency, emails corrected version |
| `09-daily-brief.json` | Daily 7am | Emails morning summary of IG/FB stats + lead pipeline |

### n8n Setup Checklist (one-time)

- [ ] Add **Anthropic** credential: Credentials → New → "Anthropic" → paste API key
- [ ] Add **Gmail OAuth2** credential: Credentials → New → "Gmail OAuth2"
- [ ] Add **Twilio** credential: Credentials → New → "Twilio" → Account SID + Auth Token
- [ ] Add **Google Sheets OAuth2** credential (for Social workflow)
- [ ] In each workflow, replace `YOUR_EMAIL@gmail.com` with your actual Gmail address
- [ ] In `01-social.json`, replace `YOUR_GOOGLE_SHEET_ID` with your content calendar sheet ID
- [ ] Import each JSON file: Workflows → ⋯ → Import from File
- [ ] Select credentials on each workflow's relevant nodes
- [ ] Activate all workflows

### n8n Form URLs (after activation)

```
Get Paid:     https://stacieh.app.n8n.cloud/form/tribal-cowboy-get-paid
Council:      https://stacieh.app.n8n.cloud/form/tribal-cowboy-council
Email Writer: https://stacieh.app.n8n.cloud/form/tribal-cowboy-email
Brand Design: https://stacieh.app.n8n.cloud/form/tribal-cowboy-design
Community:    https://stacieh.app.n8n.cloud/form/tribal-cowboy-community
Brand Voice:  https://stacieh.app.n8n.cloud/form/tribal-cowboy-brand-voice
```

Bookmark these on your phone for instant access.

## Brand Identity (Quick Reference)

**Colors:**
- Gold `#C9A84C` — primary accent, headings, CTAs
- Cream `#F5F0E8` — primary background
- Deep Teal `#2D6A6A` — section contrast
- Warm Amber `#D4850A` — accent pops
- Forest Green `#3A7D44` — success states
- Warm Red `#C0392B` — urgency (use sparingly)

**Typography:**
- Playfair Display (serif) — all headers and display text
- Lato (sans-serif) — body, UI, captions

**Voice:** Warm, confident, celebratory, authentic, community-rooted, professional.
Never: apologetic, corporate, hedging, cheap/budget language.

## Common Tasks

### Add a new voice inquiry status
Edit `server.js` — find the `PATCH /voice-inquiry/:id` route and update the allowed status values.

### Change social media refresh schedule
In `server.js`, find the `setInterval` call for `refreshInstagram()` / `refreshFacebook()` (currently every 24 hours).

### Update the booking URL
Change `ACUITY_BOOKING_URL` environment variable on Render.

### Add a new dashboard tab
In `index.html`, add a tab button in the nav section and a corresponding `<div id="p-tabname">` section following the existing pattern.
