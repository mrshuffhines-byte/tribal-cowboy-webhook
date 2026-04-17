# Tribal Cowboy n8n Workflows

Eleven importable n8n workflows. Import each JSON file into your n8n.cloud canvas.

---

## One-Time Setup (Required Before Any Workflow Works)

### 1. Anthropic Credential
1. n8n.cloud → **Credentials** → **New** → search "Anthropic"
2. Paste your Anthropic API key
3. Name it: `Tribal Cowboy - Anthropic` → Save

### 2. Gmail OAuth2 Credential
1. **Credentials** → **New** → search "Gmail OAuth2"
2. Follow the Google OAuth flow — sign in as `info@tribalcowboy.com`
3. Name it: `Tribal Cowboy - Gmail` → Save

### 3. Twilio Credential
1. **Credentials** → **New** → search "Twilio"
2. Paste: Account SID + Auth Token
3. Name it: `Tribal Cowboy - Twilio` → Save

### 4. Google Sheets OAuth2 Credential (Social workflow only)
1. **Credentials** → **New** → search "Google Sheets OAuth2"
2. Follow Google OAuth flow
3. Name it: `Tribal Cowboy - Google Sheets` → Save

### 5. Set n8n Environment Variables
n8n.cloud → **Settings** → **Variables**, add:

| Variable | Value | Used By |
|---|---|---|
| `STACIE_PHONE` | Your cell number (e.g. `+12085551234`) | Email alerts SMS |
| `STACIE_EMAIL` | Your **personal** email (NOT info@tribalcowboy.com) | Email alert summary |
| `TWILIO_PHONE_NUMBER` | Your Twilio number (e.g. `+12085559876`) | Email alerts SMS |

> **Important:** `STACIE_EMAIL` must be different from `info@tribalcowboy.com` to avoid a loop.

### 6. Import Each Workflow
1. n8n.cloud → **Workflows** → top-right `...` menu → **Import from File**
2. Upload the `.json` file
3. Open the workflow and connect credentials on each node that requires them
4. Click the **Activate** toggle (top-right) to turn it on

---

## Workflow Directory

| File | Trigger | Purpose |
|---|---|---|
| `01-social.json` | Schedule (8am daily) | Generates daily content ideas for IG/FB/TikTok, emails + logs to Google Sheets |
| `02-get-paid.json` | Form | Submit a free request — get an on-brand paid-response script emailed back |
| `03-council.json` | Form | Submit any idea/email/decision — get 5-perspective advisory review emailed back |
| `04-booking-closer.json` | Schedule (9am daily) | Fetches new voice leads, sends Twilio SMS follow-ups, updates status to Contacted |
| `05-email-writer.json` | Form | Submit email type + context — get a polished draft emailed to you |
| `06-brand-design.json` | Form | Submit a design need — get full spec (colors, fonts, layout) emailed back |
| `07-community.json` | Form | Submit school/nonprofit request — get tiered partnership proposal emailed back |
| `08-brand-voice.json` | Form | Submit any content — get brand voice review + corrected version emailed back |
| `09-daily-brief.json` | Schedule (7am daily) | Emails morning summary of IG/FB stats + voice leads pipeline |
| `09-email-alerts-draft-responses.json` | Gmail Trigger (every 1 min) | Monitors info@tribalcowboy.com — SMS alert + Council review + draft reply for every inbound email |
| `10-negotiation-replies.json` | Gmail Trigger (every 1 min) | Auto-detects replies to emails Stacie sent — full thread analysis, negotiation Council, strategic draft |

---

## Form URLs (Bookmark These)

After activating each Form workflow, these URLs go live:

```
Get Paid:     https://stacieh.app.n8n.cloud/form/tribal-cowboy-get-paid
Council:      https://stacieh.app.n8n.cloud/form/tribal-cowboy-council
Email Writer: https://stacieh.app.n8n.cloud/form/tribal-cowboy-email
Brand Design: https://stacieh.app.n8n.cloud/form/tribal-cowboy-design
Community:    https://stacieh.app.n8n.cloud/form/tribal-cowboy-community
Brand Voice:  https://stacieh.app.n8n.cloud/form/tribal-cowboy-brand-voice
```

Save these to your phone's home screen for instant access.

---

## What Each Workflow Sends to Your Email

All workflows email output to `info@tribalcowboy.com` (except 09 and 10, which go to `STACIE_EMAIL`).

| Workflow | Subject Line |
|---|---|
| Social | `📱 Tribal Cowboy Social Content — [Day]` |
| Get Paid | `💰 Get Paid Script — [Request Type]` |
| Council | `🏛️ Council Report — [Topic]` |
| Booking Closer | `📞 Booking Follow-Up Sent — [Name]` |
| Email Writer | `✉️ Draft Email — [Email Type]` |
| Brand Design | `🎨 Design Spec — [Design Type]` |
| Community | `🏫 Community Partnership Proposal — [Org Name]` |
| Brand Voice | `🎙️ Brand Voice Review — [Content Type]` |
| Daily Brief | `🤠 Tribal Cowboy Daily Brief — [Day]` |
| Email Alerts | `[TC Email Alert] [Subject] — Council + Draft Ready` |
| Negotiation | `[TC Negotiation] [Subject] — Analysis + Draft Ready` |

---

## Google Sheet (Social Workflow)

The Social workflow logs content ideas to:
**Tribal Cowboy - Social**
Sheet ID: `1xy75VdK4NDtVZtjNAzE1ED0vrVLsh7iy9sjnl4URN80`

Columns: Date | Platform | Content Idea | Caption | Hashtags

---

## Connecting to Your Tribal Cowboy Server

The Booking Closer workflow calls your live server at `https://tribal-cowboy-webhook.onrender.com`:
- `GET /voice-inquiries` — fetch all voice leads
- `PATCH /voice-inquiry/:id` — update lead status to "Contacted" after SMS

The Daily Brief also fetches from:
- `GET /data` — IG/FB stats
- `GET /voice-inquiries` — pipeline counts

---

## How Workflow 09 (Email Alerts) Works

When any email lands in info@tribalcowboy.com, this fires automatically:

1. **Gmail Trigger** polls the inbox every minute
2. **Extract Email Data** pulls sender, subject, and body
3. **SMS Alert** fires immediately to `STACIE_PHONE`
4. **Council Agent** categorizes the email, sets priority, gives five-perspective analysis, recommends response strategy
5. **Email Writer Agent** drafts a complete reply in Tribal Cowboy's voice, informed by the Council's verdict
6. **Summary email** goes to `STACIE_EMAIL` with: original email, Council review, draft reply

---

## How Workflow 10 (Negotiation Replies) Works

**Nothing to configure** — just send emails from info@tribalcowboy.com as normal. When someone replies, the workflow auto-detects whether you started that thread. If you did, the full negotiation analysis runs. If not, it skips silently.

1. **Gmail Trigger** watches all new inbound emails
2. **Fetch Full Thread** pulls every message via Gmail API
3. **Detect Direction** — if the first message in the thread is from info@tribalcowboy.com → continue; otherwise → stop
4. **SMS Alert** fires immediately
5. **Negotiation Council** reads the full thread labeled "SENT BY STACIE" / "RECEIVED FROM THEM" and analyzes: subtext, power dynamics, pricing pressure, red flags, what not to concede, walk-away read
6. **Strategic Reply Writer** drafts a reply using the Council's verdict — holds TC's position, warm but firm
7. **Summary email** to `STACIE_EMAIL` with full thread, Council verdict, and strategic draft

---

## Troubleshooting

| Error | Fix |
|---|---|
| "No credentials" on Anthropic node | Open workflow → Anthropic Chat Model node → select `Tribal Cowboy - Anthropic` |
| "No credentials" on Gmail node | Select `Tribal Cowboy - Gmail` OAuth2 credential |
| "No credentials" on Twilio node | Select `Tribal Cowboy - Twilio` credential |
| Form URL returns 404 | Make sure the workflow is **Activated** (toggle at top right) |
| Booking Closer sends no SMS | Check Twilio credential is connected and numbers are E.164 format (+12085551234) |
| Daily Brief shows N/A for stats | Your Render server may be sleeping — hit `/refresh` endpoint to wake it |
| Email loop on workflow 09/10 | Make sure `STACIE_EMAIL` is NOT set to `info@tribalcowboy.com` |
| SMS not sending on workflow 09/10 | Confirm `STACIE_PHONE` and `TWILIO_PHONE_NUMBER` are set in n8n Variables |
| Workflow 10 not triggering | Confirm the original email was sent FROM info@tribalcowboy.com |
| Thread fetch failing (workflow 10) | Open "Fetch Full Thread" node → select `Tribal Cowboy - Gmail` under Predefined Credential Type |
| Model not found | Workflows use `claude-sonnet-4-6` — update in the Anthropic Chat Model node if needed |
