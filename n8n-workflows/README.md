# Tribal Cowboy n8n Workflows

Nine importable n8n workflows. Drag each JSON file into your n8n.cloud canvas to import.

## One-Time Setup

### 1. Create Anthropic Credential in n8n
1. In n8n.cloud → **Credentials** → **New** → search "Anthropic"
2. Paste your Anthropic API key
3. Name it: `Tribal Cowboy - Anthropic`
4. Save

### 2. Create Twilio Credential (for SMS workflows)
1. **Credentials** → **New** → search "Twilio"
2. Paste: Account SID, Auth Token, and Twilio phone number
3. Name it: `Tribal Cowboy - Twilio`
4. Save

### 3. Create Gmail OAuth2 Credential (for email workflows)
1. **Credentials** → **New** → search "Gmail OAuth2"
2. Follow the Google OAuth flow — connect the **info@tribalcowboy.com** account
3. Name it: `Tribal Cowboy - Gmail`
4. Save

### 4. Set n8n Environment Variables
In n8n.cloud → **Settings** → **Variables**, add:

| Variable | Value | Used By |
|---|---|---|
| `STACIE_PHONE` | Your cell number (e.g. `+12085551234`) | Email alerts SMS |
| `STACIE_EMAIL` | Your **personal** email (NOT info@tribalcowboy.com) | Email alert summary |
| `TWILIO_PHONE_NUMBER` | Your Twilio number (e.g. `+12085559876`) | Email alerts SMS |

> **Important:** `STACIE_EMAIL` must be a different address than `info@tribalcowboy.com` to avoid a loop.

### 5. Import Each Workflow
1. In n8n.cloud → **Workflows** → top-right menu (...) → **Import from File**
2. Upload the `.json` file
3. Open the workflow → click each **Anthropic Chat Model** node → select `Tribal Cowboy - Anthropic`
4. Click **Activate** (top-right toggle) to turn it on

---

## Workflow Directory

| File | Agent | Trigger | Purpose |
|---|---|---|---|
| `01-social.json` | Social | Schedule (8am daily) | Generates daily social content ideas and captions |
| `02-get-paid.json` | Get Paid | Webhook | Responds to free requests with on-brand paid-response scripts |
| `03-council.json` | Council | Webhook | Submit any idea/email/decision for multi-perspective review |
| `04-booking-closer.json` | Booking Closer | Schedule (9am daily) | Checks voice leads and drafts follow-up SMS |
| `05-email-writer.json` | Email Writer | Webhook | Drafts professional emails/proposals from a form |
| `06-brand-design.json` | Brand Design | Webhook | Generates design specs, color schemes, layouts |
| `07-community.json` | Community | Webhook | Processes school/nonprofit partnership requests |
| `08-brand-voice.json` | Brand Voice | Webhook | Reviews content for brand consistency |
| `09-email-alerts-draft-responses.json` | Email Alerts + Drafts | Gmail Trigger (every 1 min) | Alerts Stacie via SMS + sends Council review + draft reply for every inbound email |

---

## Webhook URLs

Once a webhook workflow is **Activated**, n8n gives you a Production URL at the top of the workflow. Use these URLs in your forms, apps, or automations.

**Example webhook URL format:**
```
https://stacieh.app.n8n.cloud/webhook/tribal-cowboy-council
```

**Testing a webhook (POST request):**
```bash
curl -X POST https://stacieh.app.n8n.cloud/webhook/tribal-cowboy-council \
  -H "Content-Type: application/json" \
  -d '{"input":"Should we take a free job at the community center in exchange for exposure?"}'
```

---

## How Each Webhook Works

All webhook workflows expect a JSON POST body with an `input` field:

```json
{
  "input": "your text here"
}
```

Some workflows accept additional fields — see workflow details below.

### Extra Fields Per Agent

**get-paid** — add `requester_name`, `request_details`:
```json
{
  "input": "Someone asking for free work",
  "requester_name": "Sarah",
  "request_details": "Needs photographer for school fundraiser, no budget"
}
```

**email-writer** — add `recipient`, `email_type`, `context`:
```json
{
  "email_type": "proposal",
  "recipient": "Corporate event planner",
  "context": "500-person holiday party, needs full production"
}
```

**community** — add `organization_name`, `organization_type`, `event_details`:
```json
{
  "organization_name": "Lincoln Elementary PTA",
  "organization_type": "school",
  "event_details": "Spring carnival, 300 attendees, May 15"
}
```

**brand-voice** — add `content_type`:
```json
{
  "input": "Draft caption or email to review",
  "content_type": "instagram_caption"
}
```

---

## Connecting to Your Tribal Cowboy App

Your existing webhook server (`server.js`) has endpoints that n8n can call:
- `GET /voice-inquiries` — get all voice leads (booking-closer workflow uses this)
- `POST /send-booking-link` — send SMS booking link
- `POST /voice-inquiry` — create a new inquiry

The `booking-closer` workflow demonstrates this pattern — it fetches voice leads from your server, runs each through Claude to draft follow-ups, then can send SMS via Twilio.

---

## Customization Tips

- **Adjust schedules:** Open a scheduled workflow → click the Schedule Trigger node → change the cron expression
- **Add more actions:** After the Claude node, add Gmail, Slack, Google Sheets, or any n8n node to send the output somewhere
- **Chain workflows:** One workflow can trigger another via the "Execute Workflow" node
- **Save outputs:** Add a "Google Sheets" or "Airtable" node after Claude to log every run

---

---

## How Workflow 09 Works — Email Alerts + Draft Responses

When any email lands in info@tribalcowboy.com, this workflow fires automatically:

1. **Gmail Trigger** polls the inbox every minute for new emails
2. **Extract Email Data** pulls out sender, subject, and body
3. **Two things happen in parallel:**
   - Twilio sends Stacie an **instant SMS alert** with the sender and subject
   - The Council + Email Writer pipeline starts running
4. **Council Agent** reviews the email — categorizes it (Booking / Partnership / Spam / etc.), assigns priority, gives five-perspective analysis, and recommends a response strategy
5. **Email Writer Agent** uses the email content AND the Council's recommendation to draft a complete, ready-to-edit reply in Tribal Cowboy's voice
6. **Build Alert Email** combines everything into one clean document
7. **Gmail sends the summary** to `STACIE_EMAIL` with three sections: original email, Council review, suggested draft

**What Stacie gets:**
- An SMS within seconds: "New email from [Name]. Council + draft on the way."
- An email to her personal inbox with the full Council session and a ready-to-edit draft reply

**What Stacie does:**
- Review the Council's take on priority and strategy
- Copy/edit the draft reply as needed
- Send from her Gmail client

---

## Troubleshooting

- **"No credentials" error** → Click each Anthropic Chat Model node and select `Tribal Cowboy - Anthropic`; click Gmail nodes and select `Tribal Cowboy - Gmail`; click Twilio node and select `Tribal Cowboy - Twilio`
- **Webhook returns 404** → Make sure the workflow is **Activated** (toggle at top-right)
- **Model not found** → Workflow 09 uses `claude-sonnet-4-6`; older workflows use `claude-sonnet-4-5-20250929` — update if needed
- **Email loop** → Make sure `STACIE_EMAIL` is NOT set to `info@tribalcowboy.com`
- **SMS not sending** → Confirm `STACIE_PHONE` and `TWILIO_PHONE_NUMBER` are set in n8n Variables and formatted with country code (e.g. `+12085551234`)
- **Gmail trigger not firing** → Check that the Gmail OAuth credential has permission to read `info@tribalcowboy.com` and that the workflow is activated
