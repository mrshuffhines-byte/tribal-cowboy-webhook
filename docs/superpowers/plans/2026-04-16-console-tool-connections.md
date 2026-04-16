# Tribal Cowboy Console Agents — Tool Connections Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Connect Gmail, Google Calendar, Notion, Blotato, Tavily, and Exa to the 9 Tribal Cowboy Console agents so they can read email, read/write calendar, read/write Notion, post to social media, and search the web.

**Architecture:** Each tool connection has two parts: (1) a Credential Vault entry storing the API key or OAuth token, and (2) an MCP server configuration in the agent's YAML referencing that credential. Agents only get the tools they actually need — no agent gets access to tools it doesn't use.

**Tech Stack:** Anthropic Console Credential Vaults, MCP server configs, Notion API, Blotato API, Google OAuth 2.0, Tavily API, Exa API

---

## Tool-to-Agent Map

| Tool | Agents That Need It |
|---|---|
| Gmail (read) | Email Intake, Phone & Voicemail, Command Center |
| Gmail (send) | Communications Dispatcher |
| Google Calendar (read) | Lead & Booking, Command Center |
| Notion (read/write) | Content Producer, Lead & Booking, Social Publisher, Communications Dispatcher, Command Center |
| Blotato (read DMs/comments) | Social Inbox |
| Blotato (schedule/post) | Social Publisher |
| Blotato (send DM replies) | Communications Dispatcher |
| Web search — Tavily | Business Intelligence, Content Producer |
| Web search — Exa | Business Intelligence |

---

## Task 1: Get Your API Keys

Before touching the Console, collect all the credentials you need. Do this first so you're not switching back and forth.

- [ ] **Step 1: Notion API key**

  1. Go to [notion.so/profile/integrations](https://notion.so/profile/integrations)
  2. Click **+ New integration**
  3. Name it: `Tribal Cowboy Console`
  4. Set type: Internal
  5. Select your Tribal Cowboy workspace
  6. Copy the **Internal Integration Token** (starts with `secret_`)
  7. Save it somewhere safe — you'll paste it into Console in Task 2

  Also: for each Notion database the agents need to read/write (content calendar, lead pipeline, approval queue), open the database → click `...` → **Add connections** → select `Tribal Cowboy Console`.

- [ ] **Step 2: Blotato API key**

  1. Log into your Blotato account
  2. Go to Settings → API or Developer settings
  3. Generate or copy your API key
  4. Save it

- [ ] **Step 3: Tavily API key**

  1. Go to [app.tavily.com](https://app.tavily.com) 
  2. Sign in (or create a free account)
  3. Copy your API key from the dashboard
  4. Save it

- [ ] **Step 4: Exa API key**

  1. Go to [exa.ai](https://exa.ai)
  2. Sign in → API Keys
  3. Create a new key, name it `Tribal Cowboy`
  4. Save it

- [ ] **Step 5: Gmail + Google Calendar OAuth**

  This is the most involved step. Gmail and Google Calendar use OAuth 2.0, not simple API keys. You need a Google Cloud project.

  1. Go to [console.cloud.google.com](https://console.cloud.google.com)
  2. Create a new project: name it `Tribal Cowboy Console`
  3. Go to **APIs & Services → Enable APIs**
  4. Enable: **Gmail API** and **Google Calendar API**
  5. Go to **APIs & Services → Credentials**
  6. Click **+ Create Credentials → OAuth client ID**
  7. Application type: **Web application**
  8. Name: `Tribal Cowboy Console Agents`
  9. Under **Authorized redirect URIs**, add the Console's callback URL. Check the Anthropic Console docs or the Credential Vault setup screen for the exact URL — it will look like `https://platform.claude.com/oauth/callback` or similar.
  10. Save the **Client ID** and **Client Secret**

  Note: Google will require you to verify your app if you want to use it beyond test users. For now, add your own Gmail address as a test user under **OAuth consent screen → Test users**.

---

## Task 2: Set Up Credential Vaults in the Console

- [ ] **Step 1: Open Credential Vaults**

  Go to: `platform.claude.com` → Tribal Cowboy workspace → Managed Agents → **Credential vaults**

- [ ] **Step 2: Create vault — Notion**

  Click **+ New credential vault**
  - Name: `notion-api`
  - Type: API Key (or Secret)
  - Value: paste your Notion Internal Integration Token (`secret_...`)
  - Save

- [ ] **Step 3: Create vault — Blotato**

  - Name: `blotato-api`
  - Type: API Key
  - Value: your Blotato API key
  - Save

- [ ] **Step 4: Create vault — Tavily**

  - Name: `tavily-api`
  - Type: API Key
  - Value: your Tavily API key
  - Save

- [ ] **Step 5: Create vault — Exa**

  - Name: `exa-api`
  - Type: API Key
  - Value: your Exa API key
  - Save

- [ ] **Step 6: Create vault — Gmail / Google Calendar OAuth**

  - Name: `google-oauth`
  - Type: OAuth 2.0
  - Client ID: from Google Cloud Console
  - Client Secret: from Google Cloud Console
  - Scopes: `https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/calendar.readonly`
  - Complete the OAuth flow to authorize your Gmail account
  - Save

  Note: If the Console doesn't have a built-in OAuth 2.0 vault type, use the Gmail MCP server's own OAuth flow — see Task 3 Step 1 for the alternative approach.

---

## Task 3: Update Agent YAMLs with MCP Server Configs

For each agent below, open it in the Console (Managed Agents → Agents → click the agent → Edit config) and replace the `mcp_servers: []` line with the config shown. Leave everything else in the YAML unchanged.

- [ ] **Step 1: Command Center — add Gmail + Google Calendar + Notion**

  Replace `mcp_servers: []` with:

  ```yaml
  mcp_servers:
    - name: gmail
      type: url
      url: https://mcp.composio.dev/gmail
      credentials: google-oauth
    - name: google-calendar
      type: url
      url: https://mcp.composio.dev/googlecalendar
      credentials: google-oauth
    - name: notion
      type: url
      url: https://mcp.composio.dev/notion
      credentials: notion-api
  ```

  > **Note on MCP server URLs:** The exact URLs depend on which MCP provider you use. Two options:
  > - **Composio** ([composio.dev](https://composio.dev)) — hosted MCP servers for Gmail, Calendar, Notion, and others. Sign up, connect your accounts, and get the MCP URLs.
  > - **Anthropic's own integrations** — check the Console's Environments or MCP server setup screen for any built-in integrations.
  > If the URLs above don't work, use Composio and copy the URLs from their dashboard.

- [ ] **Step 2: Email Intake — add Gmail (read)**

  Replace `mcp_servers: []` with:

  ```yaml
  mcp_servers:
    - name: gmail
      type: url
      url: https://mcp.composio.dev/gmail
      credentials: google-oauth
  ```

- [ ] **Step 3: Phone & Voicemail — add Gmail (read)**

  Same as Email Intake:

  ```yaml
  mcp_servers:
    - name: gmail
      type: url
      url: https://mcp.composio.dev/gmail
      credentials: google-oauth
  ```

- [ ] **Step 4: Social Inbox — add Blotato (read)**

  ```yaml
  mcp_servers:
    - name: blotato
      type: url
      url: https://mcp.blotato.com
      credentials: blotato-api
  ```

  > **Note:** Verify the Blotato MCP server URL in your Blotato account settings or their developer docs. If Blotato doesn't have an MCP server, you'll connect it via n8n instead — n8n polls Blotato and calls the Social Inbox agent via API. That's covered in Plan 3 (n8n automation).

- [ ] **Step 5: Content Producer — add Notion + Tavily**

  ```yaml
  mcp_servers:
    - name: notion
      type: url
      url: https://mcp.composio.dev/notion
      credentials: notion-api
    - name: tavily
      type: url
      url: https://mcp.tavily.com
      credentials: tavily-api
  ```

- [ ] **Step 6: Lead & Booking — add Gmail + Google Calendar + Notion**

  ```yaml
  mcp_servers:
    - name: gmail
      type: url
      url: https://mcp.composio.dev/gmail
      credentials: google-oauth
    - name: google-calendar
      type: url
      url: https://mcp.composio.dev/googlecalendar
      credentials: google-oauth
    - name: notion
      type: url
      url: https://mcp.composio.dev/notion
      credentials: notion-api
  ```

- [ ] **Step 7: Business Intelligence — add Tavily + Exa**

  ```yaml
  mcp_servers:
    - name: tavily
      type: url
      url: https://mcp.tavily.com
      credentials: tavily-api
    - name: exa
      type: url
      url: https://mcp.exa.ai
      credentials: exa-api
  ```

- [ ] **Step 8: Social Publisher — add Blotato + Notion**

  ```yaml
  mcp_servers:
    - name: blotato
      type: url
      url: https://mcp.blotato.com
      credentials: blotato-api
    - name: notion
      type: url
      url: https://mcp.composio.dev/notion
      credentials: notion-api
  ```

- [ ] **Step 9: Communications Dispatcher — add Gmail + Blotato + Notion**

  ```yaml
  mcp_servers:
    - name: gmail
      type: url
      url: https://mcp.composio.dev/gmail
      credentials: google-oauth
    - name: blotato
      type: url
      url: https://mcp.blotato.com
      credentials: blotato-api
    - name: notion
      type: url
      url: https://mcp.composio.dev/notion
      credentials: notion-api
  ```

---

## Task 4: Smoke Test Each Tool Connection

For each agent, send a test message that requires a live tool call. If the tool isn't connected correctly, the agent will say it can't access the tool — fix the credential or MCP URL and retry.

- [ ] **Command Center — test Gmail read**

  Send: `"Check my Gmail inbox and tell me if there are any unread messages from the last 24 hours."`

  Expected: Agent reads your inbox and lists recent messages. If it says it can't access Gmail, the Google OAuth credential or MCP URL needs fixing.

- [ ] **Email Intake — test Gmail read**

  Send: `"Read the most recent email in my Gmail inbox and classify it."`

  Expected: Valid JSON output with classification of a real email.

- [ ] **Content Producer — test Notion + web search**

  Send: `"Check the Notion content calendar and tell me what's scheduled this week. Then search for what's trending in horse content on TikTok right now."`

  Expected: Agent reads from Notion (may say the database isn't connected yet if you haven't shared it with the integration) and returns web search results about horse TikTok trends.

- [ ] **Business Intelligence — test Tavily search**

  Send: `"Search for equine event businesses in the Pacific Northwest and summarize what you find."`

  Expected: Agent returns real web search results, not hallucinated ones.

- [ ] **Lead & Booking — test Notion write**

  Send: `"Create a test lead in Notion: Name: Test Lead, Source: Manual, Status: New Inquiry, Notes: Testing tool connection."`

  Expected: Agent confirms it created the entry. Check your Notion database to verify it appeared.

---

## Task 5: Create Notion Databases (if they don't exist yet)

The agents need specific Notion databases to read from and write to. Create these if they don't exist.

- [ ] **Content Calendar database**

  Columns: Platform (select), Post Type (select), Caption (text), Hashtags (text), Scheduled Time (date), Status (select: Draft / Approved / Scheduled / Posted), Post ID (text), Pillar (select)

- [ ] **Lead Pipeline database**

  Columns: Name (title), Source (select: Email / Phone / Instagram / Facebook / TikTok), Lead Tier (select: A / B / C), Status (select: New / Responded / Qualified / Booked / Closed), Event Type (text), Event Date (date), Budget Signal (text), Notes (text), Next Follow-Up (date)

- [ ] **Approval Queue database**

  Columns: Output Type (select: Content Draft / Response Draft / Lead Brief), Agent (text), Platform or Recipient (text), Draft Text (text), Status (select: Pending / Approved / Changes Requested), Created (date)

- [ ] **Communications Log database**

  Columns: Date (date), Recipient (text), Contact (text), Channel (select: Email / Instagram DM / Facebook DM / TikTok DM), Message Excerpt (text), Lead ID (relation to Lead Pipeline), Status (select: Sent / Failed)

- [ ] **Share all 4 databases with the Tribal Cowboy Console integration**

  For each database: open it → click `...` → **Add connections** → select `Tribal Cowboy Console`

---

## After Tool Connections Are Complete

Every agent now has live tool access. The system can:
- Read and classify your Gmail inbox
- Read and write your Notion databases
- Schedule posts via Blotato (once Blotato MCP is confirmed)
- Search the web for trends and research

**Next step: Plan 3 — n8n Automation**

Plan 3 wires the automation layer: n8n polls Gmail every 15 minutes, sends new messages to Email Intake automatically, and handles the approval-to-publish workflow so Stacie only touches the approval decision.

See `docs/superpowers/plans/2026-04-16-n8n-automation.md`
