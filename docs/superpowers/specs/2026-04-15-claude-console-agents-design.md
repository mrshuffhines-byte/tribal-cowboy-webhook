# Tribal Cowboy — Claude Console Agents Design

**Date:** 2026-04-15
**Author:** Stacie Huffhines / Claude Code
**Status:** Approved

---

## Problem

Stacie manually handles every inbound communication (calls, emails, DMs, comments) and every outbound action (content posting, booking responses, follow-ups). There is no automation. Every task requires her to prompt Claude manually. The goal is a fully autonomous business OS where agents handle the full communication and content loop, and Stacie only touches the decisions that require her judgment.

---

## Architecture: 3-Tier Input / Process / Output

All agents live in the Anthropic Console (platform.claude.com) under the Tribal Cowboy workspace. n8n handles all automation wiring between agents. Stacie interacts directly with the Command Center Agent for daily oversight, and with individual agents for on-demand tasks.

```
[Phone/Email/Social] → [Input Agents] → [Processing Agents] → Stacie approval → [Output Agents]
                                                                       ↑
                                                              Command Center Agent
                                                           (daily briefing + routing)
```

---

## Agents

### Tier 1 — Input Agents
*Triggered by n8n automations. Never output to external systems directly.*

---

#### Agent 1: Phone & Voicemail Agent

**Purpose:** Process inbound calls and voicemails from Google Voice.

**How it works:**
- Google Voice auto-transcribes voicemails and delivers them to Gmail
- n8n polls Gmail for Voice voicemail emails on a 15-minute interval
- On match, n8n calls this agent with the transcription text
- Agent classifies intent, extracts key facts, sets urgency level, drafts a response brief for the Lead & Booking Agent

**Output schema:**
```json
{
  "caller": "name or unknown",
  "intent": "booking_inquiry | pricing_question | partnership | media | complaint | spam",
  "urgency": "immediate | same_day | this_week | low",
  "key_facts": ["..."],
  "recommended_action": "...",
  "draft_response_brief": "..."
}
```

**Tools:** Gmail (read)

**Phase 2 upgrade:** Google Voice number forwards live calls to Vapi. Vapi runs a live AI voice conversation, transcribes it, and sends the full transcript + caller intent to this agent in real time. No changes to the agent itself — only the n8n trigger changes.

**Chat use:** "What calls came in this week?" / "Summarize the voicemail from this morning."

---

#### Agent 2: Email Intake Agent

**Purpose:** Process all inbound Gmail messages and route them.

**How it works:**
- n8n polls Gmail inbox every 15 minutes
- Filters out known spam, newsletters, and auto-replies
- Sends new human-sent messages to this agent
- Agent classifies, extracts key facts, and either drafts a response or produces a routing brief

**Classification categories:**
- `booking_inquiry` — someone wants to book an event
- `corporate_sponsor` — brand, company, or chamber inquiry
- `creator_deal` — brand partnership or collab offer
- `media` — press, podcast, publication request
- `community` — school, nonprofit, community program
- `complaint` — dissatisfied customer or negative feedback
- `vendor` — supplier, service provider, misc business
- `spam` — no action needed

**Output schema:**
```json
{
  "from": "...",
  "subject": "...",
  "classification": "...",
  "urgency": "immediate | same_day | this_week | low",
  "key_facts": ["..."],
  "routing_target": "lead_booking_agent | intelligence_agent | stacie_direct",
  "draft_response_brief": "..."
}
```

**Tools:** Gmail (read), web search (to identify unknown senders)

**Chat use:** "What's in my inbox today?" / "Did anything important come in this week?"

---

#### Agent 3: Social Inbox Agent

**Purpose:** Monitor and classify all inbound DMs and comments across Instagram, Facebook, and TikTok.

**How it works:**
- n8n polls social platform APIs (via Blotato) on a 30-minute interval
- Sends new DMs and comments to this agent
- Agent applies Tribal Cowboy's 11-tier reply classification rules
- Outputs a prioritized response queue

**Response tiers (from existing rules):**
1. Hot lead — booking or pricing inquiry → immediate flag to Lead & Booking Agent
2. Partnership signal → immediate flag to Stacie
3. Positive engagement → queue for same-day response
4. Question → queue for same-day response
5. Compliment → batch response at end of day
6. Spam / negative → flag for Stacie review before any action

**Output:** Prioritized queue with classification, platform, message text, recommended response tier, and draft response brief for each item.

**Tools:** Blotato (read DMs/comments)

**Chat use:** "What needs a reply right now?" / "Show me today's comment queue."

---

### Tier 2 — Processing Agents
*Triggered by Tier 1 output briefs or by schedule. All outputs require Stacie approval before Tier 3 acts.*

---

#### Agent 4: Content Producer Agent

**Purpose:** Create platform-ready content from any brief, topic, event, or photo description.

**How it works:**
- Triggered by: Stacie direct request (chat), Social Content Strategist schedule (n8n weekly), or event trigger (n8n detects upcoming event on calendar)
- Receives a brief: topic, event name, photo/video description, pillar target
- Checks content calendar in Notion for recent pillar usage (avoids back-to-back same pillar)
- Produces three platform versions in a single output

**Output per request:**
- Instagram: caption (150–300 words) + 5–10 hashtags from the approved bank + suggested post time
- TikTok: hook line + script (60–90 sec) + 4–6 hashtags + suggested post time
- Facebook: community-forward version (slightly longer, event-aware) + 2–3 hashtags

**Brand voice rules baked into system prompt:**
- No exclamation marks except one per post, earned
- No clichés: "making memories," "your special day," "dreams come true" are blocked
- No corporate language
- Indigenous identity handled with dignity, never as a marketing hook
- Specificity required: "Millie, our 1,800-lb Clydesdale" not "a beautiful horse"

**Tools:** Web search (trend check before writing), Notion (content calendar read)

**Chat use:** "Write content about Millie at Saturday's corporate event." / "I have a video of a kid meeting a pony for the first time — what do we post?"

---

#### Agent 5: Lead & Booking Agent

**Purpose:** Qualify inbound leads and manage the full response + follow-up cycle.

**How it works:**
- Receives classified lead briefs from Phone, Email, or Social Inbox agents
- Qualifies the lead: event type, budget signals, timeline, group size
- Determines appropriate response: templated (low-signal leads) vs. personalized (high-signal)
- Drafts a response at the right CTA level (never urgency-pressure language)
- Creates a follow-up task in Notion with a due date
- Flags corporate sponsors and creator deals to Stacie immediately — never handles those autonomously

**Qualification tiers:**
- **Tier A** — Corporate sponsor, city/chamber, luxury family (200+ guests, premium signals): flag immediately to Stacie with full brief
- **Tier B** — Standard booking inquiry (pony party, wagon ride, school program): draft personalized response, queue for Stacie approval
- **Tier C** — Early-stage inquiry (just browsing, no date/budget info): draft nurture response, add to follow-up sequence

**Response rules:**
- Always include one of the approved CTAs: "Check availability at tribalcowboy.com" / "DM to check dates" / "Email info@tribalcowboy.com"
- Never mention specific pricing without Stacie's approval
- Never send anything autonomously — all responses queue for approval

**Tools:** Gmail (read), Notion (create/update tasks), Google Calendar (check availability windows)

**Chat use:** "What leads need follow-up today?" / "Qualify this inquiry and draft a response."

---

#### Agent 6: Business Intelligence Agent

**Purpose:** Monitor trends, surface opportunities, and deliver weekly competitive intelligence.

**How it works:**
- Runs on weekly schedule (Sunday evening, ready for Monday morning)
- Also available on-demand for deep research requests
- Monitors: trending horse/western/Indigenous content formats, competitor account activity, brand deal candidates in North Idaho and Pacific Northwest, emerging platform features

**Weekly brief output:**
- Top 3 trending content formats in the equine/western space this week
- Any notable competitor moves (new services, viral posts, pricing changes)
- 2–3 brand deal candidates worth pursuing (with contact info where findable)
- Platform algorithm notes (anything that affects reach this week)
- Recommended content angle for the coming week based on trends

**Tools:** Web search (Tavily + Exa), web fetch (competitor pages, brand websites)

**Chat use:** "What's trending in my space right now?" / "Research [brand name] — are they a good fit for a partnership?" / "Find me three companies in North Idaho that sponsor outdoor events."

---

### Tier 3 — Output Agents
*Triggered by n8n after Stacie approves Tier 2 outputs. These are the only agents that take external action.*

---

#### Agent 7: Social Publisher Agent

**Purpose:** Schedule and post approved content to all platforms.

**How it works:**
- n8n receives Stacie's approval signal (button in approval interface, or explicit message)
- Sends approved content package (caption, hashtags, platform, image/video attachment) to this agent
- Agent formats for each platform's requirements, schedules via Blotato at the recommended time
- Updates Notion content calendar with scheduled status
- Confirms post ID and scheduled time back to n8n (logged to Notion)

**Guardrails:**
- Never posts without an explicit approval signal in the n8n payload
- If Blotato returns an error, logs the failure and notifies Stacie — does not retry autonomously
- Respects platform posting frequency limits (max 1 post/day Instagram, 1/day TikTok, 2/week Facebook)

**Tools:** Blotato (schedule + publish), Notion (update content calendar)

---

#### Agent 8: Communications Dispatcher Agent

**Purpose:** Send approved email and DM responses on Stacie's behalf.

**How it works:**
- n8n receives Stacie's approval signal with the approved response text and destination
- Agent sends via Gmail (for email) or Blotato (for DM replies)
- Logs every outbound message to Notion (date, recipient, channel, message text)
- Updates lead status in Notion (e.g., "inquiry → responded")

**Guardrails:**
- Never sends without an explicit approval signal
- Never modifies approved text — sends exactly what was approved
- Any send failure → logged + Stacie notified immediately
- No follow-up messages sent autonomously — each one requires a new approval

**Tools:** Gmail (send), Blotato (DM reply), Notion (log + update)

---

#### Note: Proactive Corporate Outreach

The existing `corporate-luxury-leads-agent.md` covers proactive outreach to corporate targets (chambers, HR departments, local businesses). In this Console architecture, that capability lives inside the **Lead & Booking Agent** — it handles both inbound qualification and outbound corporate pitch drafting. When Stacie says "draft outreach to Silver Lake Mall," that request goes to Lead & Booking Agent, not a separate agent. This collapses two markdown agents into one Console agent without losing capability.

---

### Command Layer

---

#### Agent 9: Command Center Agent

**Purpose:** Daily business briefing and routing hub. This is the agent Stacie opens every morning.

**How it works:**
- On demand: Stacie opens it and asks "What do I need to handle today?"
- Pulls from Notion (pending approvals, open leads, content queue, follow-up tasks due), Gmail (flagged high-priority items), and Google Calendar (upcoming events in next 14 days)
- Produces a prioritized daily briefing organized by urgency
- Routes new ad-hoc requests to the appropriate agent via n8n webhook

**Daily briefing structure:**
1. Immediate attention required (hot leads, flagged partnerships, anything marked urgent)
2. Approvals waiting (content drafts, response drafts ready for your sign-off)
3. Follow-ups due today (leads that haven't heard back, tasks overdue)
4. Upcoming events in 14 days (content push windows, logistics to confirm)
5. Content queue status (what's scheduled, what's missing for this week)

**Tools:** Notion (read), Gmail (read), Google Calendar (read)

**Chat use:** "What do I need to handle today?" / "Where does the pipeline stand?" / "Set up the workflow for this week's content." / "Something feels off — give me a full status check."

---

## n8n Automation Triggers

| Trigger | Frequency | Calls Agent |
|---|---|---|
| Gmail poll — Voice voicemail | Every 15 min | Phone & Voicemail Agent |
| Gmail poll — inbox | Every 15 min | Email Intake Agent |
| Social inbox poll | Every 30 min | Social Inbox Agent |
| Content calendar gap check | Daily 7am | Content Producer Agent |
| Intelligence brief | Sunday 6pm | Business Intelligence Agent |
| Stacie approves content | On approval | Social Publisher Agent |
| Stacie approves response | On approval | Communications Dispatcher Agent |

---

## Credential Vaults Required

| Credential | Used By |
|---|---|
| Gmail OAuth | Phone & Voicemail, Email Intake, Lead & Booking, Communications Dispatcher, Command Center |
| Blotato API key | Social Inbox, Social Publisher, Communications Dispatcher |
| Notion API key | Content Producer, Lead & Booking, Social Publisher, Communications Dispatcher, Command Center |
| Google Calendar OAuth | Lead & Booking, Command Center |
| Tavily API key | Business Intelligence, Content Producer |
| Exa API key | Business Intelligence |

---

## Approval Interface

All Tier 2 outputs land in a Notion database called **Approval Queue**. Each row has:
- Output type (content draft / response draft / lead brief)
- Agent that produced it
- Platform / recipient
- Full draft text
- Approve / Request changes buttons (via n8n webhook)

Stacie reviews the queue once or twice a day. Approved items trigger the relevant Tier 3 agent automatically.

---

## Build Order

1. **Command Center Agent** — gives Stacie immediate value from day one. No integrations needed to start; add Notion/Gmail/Calendar progressively.
2. **Email Intake Agent** — highest volume input, clearest ROI. Gmail integration already available.
3. **Content Producer Agent** — biggest time savings on daily work.
4. **Lead & Booking Agent** — directly tied to revenue.
5. **Social Inbox Agent** — requires Blotato integration to be wired.
6. **Social Publisher Agent** — requires Blotato + Notion + approval interface.
7. **Communications Dispatcher Agent** — requires approval interface to be live.
8. **Business Intelligence Agent** — standalone, add any time.
9. **Phone & Voicemail Agent** — Gmail integration works immediately for voicemails. Live answering (Vapi) is Phase 2.

---

## Out of Scope (Phase 2)

- Live AI voice answering via Vapi (requires Google Voice → Vapi call forwarding setup)
- Automatic booking confirmation and calendar blocking (requires Acuity API integration)
- Photo delivery automation (requires facial recognition pipeline)
- Revenue reporting and QuickBooks sync
- YouTube / podcast content pipeline
