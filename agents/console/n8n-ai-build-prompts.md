# Tribal Cowboy — n8n AI Build Prompts

Paste each prompt into the **n8n AI assistant** (purple ✨ button, bottom right of workflow editor).
Create a new workflow for each one, name it first, then paste the prompt.

---

## Workflow 1: Email Intake Agent

**Workflow name:** `Email Intake Agent`

**Paste this into n8n AI:**

```
Build a workflow called Email Intake Agent with these nodes in order:

1. Gmail Trigger node — credential: Gmail OAuth2 API, poll every 15 minutes, trigger on new email, filter for UNREAD label only, Simplify ON

2. IF node — drop emails that match any of these (OR logic): From contains "noreply", From contains "no-reply", Subject contains "unsubscribe", Subject contains "newsletter", Subject contains "notification". True branch ends here. False branch continues.

3. Anthropic Message a Model node connected to the False branch — credential: Anthropic account, model: claude-sonnet-4-6, Role: user, Simplify ON. Prompt field:

You are the Email Intake Agent for Tribal Cowboy LLC, an Indigenous-owned equine experience business in Athol, Idaho. Read the email below and return ONLY a JSON object with these fields: from, subject, classification (one of: booking_inquiry/corporate_sponsor/creator_deal/media/community/complaint/vendor/spam), urgency (one of: immediate/same_day/this_week/low), key_facts (array), routing_target (one of: lead_booking_agent/intelligence_agent/stacie_direct), draft_response_brief.

EMAIL:
From: {{ $json.From }}
Subject: {{ $json.subject }}
Body: {{ $json.snippet }}

4. Notion Create Database Page node — credential: Notion account, database ID: [PASTE YOUR APPROVAL QUEUE DATABASE ID], Title: {{ $('Gmail Trigger').item.json.subject }}, add a Paragraph block containing: {{ $json.content[0].text }}
```

---

## Workflow 2: Content Producer Agent

**Workflow name:** `Content Producer Agent`

**Paste this into n8n AI:**

```
Build a workflow called Content Producer Agent with these nodes:

1. Webhook trigger node — POST method, path: content-producer, respond immediately

2. Anthropic Message a Model node — credential: Anthropic account, model: claude-sonnet-4-6, Role: user, Simplify ON. Prompt:

You are the Content Producer Agent for Tribal Cowboy LLC, an Indigenous-owned equine experience business in Athol, Idaho owned by Stacie (Nisenan Maidu).

Brand voice rules:
- No exclamation marks except one per post, earned
- No clichés: "making memories", "your special day", "dreams come true" are banned
- No corporate language
- Indigenous identity handled with dignity, never as a marketing hook
- Specificity required: "Millie, our 1,800-lb Clydesdale" not "a beautiful horse"
- Write like a person, not a brand

From the brief below, produce THREE versions of content:

INSTAGRAM: 150-300 word caption + 5-8 hashtags from: #TribalCowboy #NorthIdaho #IdahoHorses #ClydesdaleHorse #PonyParty #HorsePhotography #IndigenousOwned #NiseanMaidu #EquestrianLife #HorsesOfInstagram + suggested post time

TIKTOK: hook line (first 3 words stop the scroll) + 60-90 second script + 4-6 hashtags from: #HorseTok #NorthIdaho #TribalCowboy #ClydesdaleTok #PonyParty #IndigenousCreator + suggested post time

FACEBOOK: community-forward version, slightly longer, event-aware + 2-3 hashtags + suggested post time

BRIEF:
Topic: {{ $json.body.topic }}
Pillar: {{ $json.body.pillar }}
Key details: {{ $json.body.details }}
Platform priority: {{ $json.body.platform }}

3. Notion Create Database Page node — credential: Notion account, database ID: [PASTE YOUR CONTENT CALENDAR DATABASE ID], Title: {{ $json.body.topic }}, Status: draft, add Paragraph block with: {{ $json.content[0].text }}

4. Respond to Webhook node — return: {{ $json.content[0].text }}
```

---

## Workflow 3: Lead & Booking Agent

**Workflow name:** `Lead & Booking Agent`

**Paste this into n8n AI:**

```
Build a workflow called Lead & Booking Agent with these nodes:

1. Webhook trigger node — POST method, path: lead-booking, respond immediately

2. Anthropic Message a Model node — credential: Anthropic account, model: claude-sonnet-4-6, Role: user, Simplify ON. Prompt:

You are the Lead & Booking Agent for Tribal Cowboy LLC, an Indigenous-owned equine experience business in Athol, Idaho.

Services: pony parties (ages 2-10, up to 15 kids), Clydesdale wagon rides, horse photography props with instant QR delivery, school/community programs, corporate events.

Qualify this lead and return ONLY a JSON object with: lead_tier (A=corporate/luxury/200+ guests, B=standard booking, C=early stage browsing), event_type, estimated_group_size, urgency, key_facts (array), draft_response (a warm personalized reply in Stacie's voice — never corporate, never pressure language), follow_up_date (ISO date, 3 days from today if tier B/C), recommended_cta (one of: "Check availability at www.tribalcowboy.com" / "DM us to check dates" / "Email info@tribalcowboy.com").

Rules: Never mention specific pricing. Never send anything — this is a draft only. Flag Tier A immediately.

LEAD:
From: {{ $json.body.from }}
Message: {{ $json.body.message }}
Source: {{ $json.body.source }}

3. IF node — check if lead_tier from Claude response equals "A". True branch: send Slack/email alert to Stacie (flag immediately). False branch: continue to Notion.

4. Notion Create Database Page node — credential: Notion account, database ID: [PASTE YOUR LEADS DATABASE ID], Title: {{ $json.body.from }}, Status: new, add Paragraph block with: {{ $json.content[0].text }}

5. Respond to Webhook node — return: {{ $json.content[0].text }}
```

---

## Workflow 4: Social Inbox Agent

**Workflow name:** `Social Inbox Agent`

**Paste this into n8n AI:**

```
Build a workflow called Social Inbox Agent with these nodes:

1. Schedule Trigger node — runs every 30 minutes

2. HTTP Request node — GET request to Blotato API to fetch new DMs and comments. URL: https://api.blotato.com/v1/inbox. Headers: api-key = [YOUR BLOTATO API KEY from Header Auth credential]

3. Anthropic Message a Model node — credential: Anthropic account, model: claude-sonnet-4-6, Role: user, Simplify ON. Prompt:

You are the Social Inbox Agent for Tribal Cowboy LLC. Classify each inbound social message and return a JSON array. For each message return: platform, message_text, sender, classification (one of: hot_lead/partnership_signal/positive_engagement/question/compliment/spam/negative), urgency (immediate/same_day/end_of_day/low), draft_reply (warm reply in Stacie's voice, specific not generic, no exclamation spam), action_required (true/false).

Tribal Cowboy voice: warm, grounded, real. Like a neighbor who loves horses. No corporate language. No "making memories." Humor is allowed. Horses are funny.

INBOX ITEMS:
{{ $json }}

4. Notion Create Database Page node — credential: Notion account, database ID: [PASTE YOUR APPROVAL QUEUE DATABASE ID], Title: "Social Inbox - " + today's date, add Paragraph block with: {{ $json.content[0].text }}
```

---

## Workflow 5: Social Publisher Agent

**Workflow name:** `Social Publisher Agent`

**Paste this into n8n AI:**

```
Build a workflow called Social Publisher Agent with these nodes:

1. Webhook trigger node — POST method, path: publish-content, respond immediately. This webhook is called ONLY after Stacie approves content in Notion.

2. IF node — check that {{ $json.body.approved }} equals true. False branch: stop, log rejection to Notion. True branch: continue.

3. HTTP Request node connected to True branch — POST to Blotato API to schedule post. URL: https://api.blotato.com/v1/posts. Headers: api-key = [YOUR BLOTATO API KEY]. Body: platform={{ $json.body.platform }}, content={{ $json.body.caption }}, scheduled_time={{ $json.body.scheduled_time }}, media_url={{ $json.body.media_url }}

4. Notion Update Page node — credential: Notion account, update the content calendar page to Status: scheduled. Page ID: {{ $json.body.notion_page_id }}

5. Respond to Webhook node — return success confirmation with post ID
```

---

## Workflow 6: Communications Dispatcher Agent

**Workflow name:** `Communications Dispatcher Agent`

**Paste this into n8n AI:**

```
Build a workflow called Communications Dispatcher with these nodes:

1. Webhook trigger node — POST method, path: send-response, respond immediately. Called ONLY after Stacie approves a response.

2. IF node — check that {{ $json.body.approved }} equals true. False branch: stop. True branch: continue.

3. Switch node connected to True branch — route based on {{ $json.body.channel }}: if "email" go to Gmail node, if "dm" go to HTTP Blotato node.

4a. Gmail Send Message node (email branch) — credential: Gmail OAuth2 API, To: {{ $json.body.recipient }}, Subject: {{ $json.body.subject }}, Message: {{ $json.body.message_text }}

4b. HTTP Request node (dm branch) — POST to Blotato API. URL: https://api.blotato.com/v1/messages. Headers: api-key = [YOUR BLOTATO API KEY]. Body: recipient={{ $json.body.recipient }}, message={{ $json.body.message_text }}, platform={{ $json.body.platform }}

5. Notion Create Database Page node — both branches log to Notion. Database ID: [PASTE YOUR LEADS DATABASE ID]. Title: "Sent: " + {{ $json.body.recipient }}, add Paragraph block with the message text and timestamp.

6. Respond to Webhook node — return confirmation
```

---

## Workflow 7: Business Intelligence Agent

**Workflow name:** `Business Intelligence Agent`

**Paste this into n8n AI:**

```
Build a workflow called Business Intelligence Agent with these nodes:

1. Schedule Trigger node — runs every Sunday at 6pm

2. HTTP Request node — GET request to Tavily search API. URL: https://api.tavily.com/search. Body: query="horse pony equine western Indigenous content trends this week", api_key=[YOUR TAVILY KEY]

3. HTTP Request node — second search. URL: https://api.tavily.com/search. Body: query="pony party horse photography corporate events North Idaho Pacific Northwest competitors", api_key=[YOUR TAVILY KEY]

4. Anthropic Message a Model node — credential: Anthropic account, model: claude-sonnet-4-6, Role: user, Simplify ON. Prompt:

You are the Business Intelligence Agent for Tribal Cowboy LLC, an Indigenous-owned equine experience business in Athol, Idaho. Based on the research data below, produce a weekly intelligence brief with these sections:

1. TOP 3 TRENDING CONTENT FORMATS this week in the equine/western/outdoor space
2. COMPETITOR MOVES — any notable activity from similar businesses
3. BRAND DEAL CANDIDATES — 2-3 companies in North Idaho or Pacific Northwest worth approaching for sponsorship or partnership (with contact info if available)
4. PLATFORM ALGORITHM NOTES — anything affecting reach this week on Instagram, TikTok, or Facebook
5. RECOMMENDED CONTENT ANGLE for Tribal Cowboy this coming week based on trends

RESEARCH DATA:
{{ $json }}

5. Notion Create Database Page node — credential: Notion account, database ID: [PASTE YOUR CONTENT CALENDAR OR INSIGHTS DATABASE ID], Title: "Weekly Intelligence Brief - " + this week's date, add Paragraph block with: {{ $json.content[0].text }}
```

---

## Workflow 8: Phone & Voicemail Agent

**Workflow name:** `Phone & Voicemail Agent`

**Paste this into n8n AI:**

```
Build a workflow called Phone & Voicemail Agent with these nodes:

1. Gmail Trigger node — credential: Gmail OAuth2 API, poll every 15 minutes, filter for emails FROM "voice-noreply@google.com" (Google Voice voicemail notifications only), Simplify ON

2. Anthropic Message a Model node — credential: Anthropic account, model: claude-sonnet-4-6, Role: user, Simplify ON. Prompt:

You are the Phone & Voicemail Agent for Tribal Cowboy LLC. This is a voicemail transcription from a potential customer or partner. Extract and classify it, then return ONLY a JSON object with: caller (name or unknown), phone_number, intent (one of: booking_inquiry/pricing_question/partnership/media/complaint/spam), urgency (immediate/same_day/this_week/low), key_facts (array of important details), recommended_action, draft_response_brief (what Stacie should say when she calls back).

VOICEMAIL TRANSCRIPTION:
From: {{ $json.From }}
Subject: {{ $json.subject }}
Transcription: {{ $json.snippet }}

3. Notion Create Database Page node — credential: Notion account, database ID: [PASTE YOUR APPROVAL QUEUE DATABASE ID], Title: "Voicemail: " + {{ $('Gmail Trigger').item.json.From }}, Status: pending, add Paragraph block with: {{ $json.content[0].text }}
```

---

## Workflow 9: Command Center Daily Briefing

**Workflow name:** `Command Center — Daily Briefing`

**Paste this into n8n AI:**

```
Build a workflow called Command Center Daily Briefing with these nodes:

1. Schedule Trigger node — runs every day at 7am

2. Notion Get Database Items node — credential: Notion account, database ID: [APPROVAL QUEUE DATABASE ID], filter Status = pending

3. Gmail Get Many Messages node — credential: Gmail OAuth2 API, return unread messages from last 24 hours, max 20 results, Simplify ON

4. Google Calendar Get Many Events node — credential: Google Calendar account, calendar: primary, return events from today through 14 days from now

5. Anthropic Message a Model node — credential: Anthropic account, model: claude-sonnet-4-6, Role: user, Simplify ON. Prompt:

You are the Command Center for Tribal Cowboy LLC. Based on the data below, produce a daily briefing for Stacie using EXACTLY this structure:

🔴 IMMEDIATE (needs attention today)
[hot leads, flagged items, anything urgent — or "Nothing urgent right now."]

🟡 APPROVALS WAITING  
[items in Approval Queue with pending status — or "Queue is clear."]

📋 FOLLOW-UPS DUE TODAY
[leads or tasks with follow-up due today — or "No follow-ups due today."]

📅 UPCOMING EVENTS (Next 14 Days)
[list each event with date, type, and whether content is scheduled]

📲 CONTENT QUEUE STATUS
[how many posts scheduled per platform this week, flag any gaps]

Be direct. No filler. No corporate language. Stacie is busy.

APPROVAL QUEUE:
{{ $('Notion').all() }}

GMAIL (last 24 hours):
{{ $('Gmail').all() }}

CALENDAR (next 14 days):
{{ $('Google Calendar').all() }}

6. Notion Create Database Page node — save today's briefing to Notion for reference. Title: "Daily Briefing - " + today's date. Add Paragraph block with briefing text.
```

---

## Important: Replace These Placeholders

Before using any prompt, replace:
- `[PASTE YOUR APPROVAL QUEUE DATABASE ID]` → your Notion Approval Queue database ID
- `[PASTE YOUR LEADS DATABASE ID]` → your Notion Leads database ID  
- `[PASTE YOUR CONTENT CALENDAR DATABASE ID]` → your Notion Content Calendar database ID
- `[YOUR BLOTATO API KEY]` → your Blotato API key
- `[YOUR TAVILY KEY]` → your Tavily API key (for Business Intelligence Agent)

## After Each Workflow Is Built

1. Click **Execute workflow** to test it
2. Fix any node errors n8n flags
3. Click **Publish** to activate it
4. Move to the next workflow
