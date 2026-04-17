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
| `10-negotiation-replies.json` | Negotiation Intelligence | Gmail Trigger (every 1 min, label-filtered) | Watches for replies on threads Stacie labeled "TC Negotiations" — fetches full thread history, runs negotiation-specific Council analysis, drafts a strategic reply that protects TC's position |

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

---

## How Workflow 10 Works — Negotiation Reply Intelligence

This workflow only fires on threads you deliberately flag. It gives you the full conversation history and a negotiation-specific analysis — not just "what should I say" but "what are they actually doing, what's their leverage, and what should you never give up."

### One-Time Gmail Setup

1. In Gmail, create a new label: **TC Negotiations**
2. When you send an important business email (event inquiry, partnership pitch, pricing discussion), open that sent thread and apply the **TC Negotiations** label to it
3. When they reply, this workflow triggers automatically

### What the Workflow Does

1. **Gmail Trigger** watches for new replies in any thread labeled TC Negotiations (not from your own address)
2. **Fetch Full Thread** pulls every message in the thread via Gmail API — Claude sees the entire conversation, not just the latest reply
3. **Parse Thread History** decodes and formats all messages, labels each one as "SENT BY STACIE" or "RECEIVED FROM THEM"
4. **SMS Alert** fires immediately with sender, subject, and message count
5. **Negotiation Council** analyzes the full thread and latest reply:
   - What are they actually saying vs. literally writing?
   - Who has more leverage right now?
   - Are they lowballing, stalling, or applying pressure?
   - What should Stacie never concede?
   - Walk-away recommendation
6. **Strategic Reply Writer** reads the Council verdict and drafts a reply that holds TC's position — warm but firm, no apologizing for rates
7. **Alert Email** lands in your personal inbox with: full thread, Council analysis, and strategic draft

### What You Get in Your Inbox

- Full conversation history so you can see the whole arc
- A "Power Read" on who holds leverage
- Specific red flags called out by name
- Hard limits (what NOT to give up)
- A ready-to-edit reply that doesn't undersell TC

### Troubleshooting Workflow 10

- **Not triggering** → Make sure the label is spelled exactly **TC Negotiations** in Gmail and the workflow query matches: `label:tc-negotiations`
- **Thread fetch failing** → The HTTP Request node needs the Gmail OAuth2 credential selected under "Predefined Credential Type" — open the node, click the credential dropdown, select `Tribal Cowboy - Gmail`
- **Empty thread history** → Some Gmail setups return emails in a different format; open the Parse Thread History node and check the output in a test run to confirm field names
