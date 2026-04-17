# Command Center Agent — Console Setup Guide

**Time to set up:** ~15 minutes
**What you'll have after:** A working Command Center you can open every morning and ask "What do I need to handle today?"

---

## Step 1 — Create the Project

1. Go to [platform.claude.com](https://platform.claude.com)
2. Click **Projects** in the left sidebar
3. Click **New Project**
4. Name it: `Tribal Cowboy Business OS`
5. (Optional) Add a description: `Command center and agent suite for Tribal Cowboy LLC`

---

## Step 2 — Create the Agent

Inside your new project:

1. Click **Create Agent** (or **New Agent** depending on your Console version)
2. Name it: `Command Center`
3. You'll see a **System Prompt** field — this is where the agent's instructions live

---

## Step 3 — Paste the System Prompt

1. Open the file `01-command-center-agent.md` in this folder
2. Copy everything **below** the line that says *"Paste everything below this line..."*
3. Paste it into the System Prompt field in Console
4. Save

---

## Step 4 — Connect the Tools

In the agent settings, enable these integrations. Claude Console connects to them via OAuth — you'll authorize each one with your Google account and your Notion account.

### Gmail
- Click **Add Tool** → select **Gmail**
- Authorize with the Google account that receives Tribal Cowboy emails (the one connected to info@tribalcowboy.com or your personal Gmail that gets Google Voice voicemails)
- Permissions needed: **Read** (the agent never sends — it only reads)

### Google Calendar
- Click **Add Tool** → select **Google Calendar**
- Authorize with the same Google account
- Permissions needed: **Read**

### Notion
- Click **Add Tool** → select **Notion**
- Authorize with your Notion account
- Permissions needed: **Read** access to:
  - Approval Queue database
  - Leads/Bookings database
  - Content Calendar database

> **Note:** If you haven't built the Notion databases yet, the agent will still work — it'll just tell you those sources aren't available. You can use it for Gmail + Calendar only to start, and add Notion when the databases are ready.

---

## Step 5 — Test It

Once the integrations are connected, open a conversation with your Command Center agent and type:

```
What do I need to handle today?
```

It should pull from Gmail and Calendar immediately. If Notion databases aren't set up yet, it will say so.

**Other test prompts:**
- `What's in my inbox?`
- `What events do I have in the next two weeks?`
- `Where does the pipeline stand?`

---

## Step 6 — Bookmark It

Pin or bookmark the Command Center agent so it's the first thing you open in the morning. This is your daily start point — not a chat window, not email. Open this first.

---

## Notion Databases (Set Up When Ready)

When you're ready to connect Notion, you'll need three databases. Create them in Notion and share them with the Claude integration:

### Approval Queue
Fields: `Type` (content / response / lead brief), `Agent` (which agent produced it), `Platform / Recipient`, `Draft Text`, `Status` (pending / approved / changes requested), `Created Date`

### Leads & Bookings
Fields: `Name`, `Contact` (email/phone), `Inquiry Type`, `Event Date` (if known), `Lead Tier` (A / B / C), `Status` (new / responded / follow-up / closed), `Last Contacted`, `Notes`, `Follow-Up Due Date`

### Content Calendar
Fields: `Date`, `Platform` (Instagram / TikTok / Facebook), `Content Pillar`, `Caption Draft`, `Hashtags`, `Status` (idea / draft / approved / scheduled / posted), `Related Event`

---

## What This Agent Does NOT Do Yet

The Command Center is a read-only briefing hub right now. It reads Gmail, Calendar, and Notion — it doesn't take action. The action-taking agents (Social Publisher, Communications Dispatcher) come later in the build.

Here's where each piece lands in the build order:

| # | Agent | Status |
|---|---|---|
| 1 | Command Center | ✅ This one |
| 2 | Email Intake Agent | Next |
| 3 | Content Producer Agent | |
| 4 | Lead & Booking Agent | |
| 5 | Social Inbox Agent | Needs Blotato |
| 6 | Social Publisher Agent | Needs approval interface |
| 7 | Communications Dispatcher | Needs approval interface |
| 8 | Business Intelligence Agent | Standalone, add anytime |
| 9 | Phone & Voicemail Agent | Gmail works now, Vapi is Phase 2 |

---

## Troubleshooting

**"I don't see a tool integration option in Console"**
Tool integrations (Gmail, Calendar, Notion) are available on Claude Pro and Team plans in Console. If you don't see them, check your plan or use the chat window to paste in data manually while integrations roll out.

**"It says it can't access my Notion"**
Make sure the specific databases (Approval Queue, Leads, Content Calendar) are shared with the Claude integration in Notion. Go to each database → Share → Invite → add the Claude connection.

**"It pulled old Gmail data"**
By default it reads recent unread messages. If you want it to go further back, ask explicitly: "Check Gmail for the last 7 days."
