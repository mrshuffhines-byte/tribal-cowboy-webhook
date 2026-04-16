# Meta App Review — Tribal Cowboy Dashboard
## What to Submit and What to Say

**App:** Tribal Cowboy Dashboard
**App ID:** 1630347648109336
**Goal:** Get the `instagram_basic` and `pages_read_engagement` permissions approved so the dashboard pulls live follower counts and post data automatically.

---

## Permissions You Need

| Permission | What it does | Why you need it |
|---|---|---|
| `instagram_basic` | Read follower count, media, profile info | Dashboard Overview tab — live follower number |
| `instagram_manage_insights` | Read reach, impressions, profile views | Dashboard Instagram tab — stats |
| `pages_read_engagement` | Read Facebook page follower count, post reach | Dashboard Facebook tab |
| `pages_show_list` | List pages the account manages | Required to connect the page |

---

## Step-by-Step: Submit for App Review

### 1. Go to Meta for Developers
App Dashboard: https://developers.facebook.com/apps/1630347648109336

### 2. Click "App Review" in the left sidebar

### 3. Click "Permissions and Features"

For each permission, click **Request** and fill out:

---

### For `instagram_basic`

**How are you using this permission?**
> This permission is used to display my own Instagram account's follower count and recent post data in a private business dashboard. The dashboard is used solely by me, Stacie Huffhines, owner of Tribal Cowboy LLC, to monitor my own Instagram performance without logging into the app multiple times per day. No data is shared with third parties or displayed publicly.

**Screencast requirement:** Record a short video showing:
1. Your dashboard loading at https://tribal-cowboy-webhook.onrender.com
2. The Instagram tab showing follower count
3. Explain: "This dashboard is only used by me to track my own business account"

---

### For `instagram_manage_insights`

**How are you using this permission?**
> This permission allows my private dashboard to display reach, impressions, and profile view data for my own Instagram business account (@TribalCowboy). I use this data to plan content for my equine experience business in North Idaho. The data is never shared, sold, or displayed to anyone other than myself as the account owner.

---

### For `pages_read_engagement`

**How are you using this permission?**
> I use this permission to display my own Facebook business page follower count and post engagement data in a private internal dashboard. The Tribal Cowboy LLC Facebook page (ID: 239951139207792) is my own business page. This data feeds a personal command center dashboard used only by me to track social media performance.

---

## App Review Checklist — Before You Submit

- [ ] App is set to **Live** mode (not Development) in the top toggle
- [ ] Privacy Policy URL is filled in — use: `https://www.tribalcowboy.com` (or add a `/privacy` page)
- [ ] App Icon uploaded (use your Tribal Cowboy logo)
- [ ] App Description filled in: "Private social media performance dashboard for Tribal Cowboy LLC, an Indigenous-owned equine experience business in North Idaho."
- [ ] Contact email: `info@tribalcowboy.com`
- [ ] Screencast recorded for each permission (Meta requires a video walkthrough)

---

## Screencast — What to Record

Meta will reject the submission without a working video demo. Record this:

1. Open the dashboard: https://tribal-cowboy-webhook.onrender.com
2. Show each tab (Overview, Instagram, Facebook)
3. Say out loud or show in text: "This is a private dashboard for my own business. I am the only user."
4. Show the Instagram account @TribalCowboy (prove you own it)
5. Show the Facebook page Tribal Cowboy LLC

**Tool to record:** QuickTime (already on your Mac) — File > New Screen Recording

---

## What Meta Is Looking For

Meta App Review rejects most submissions for these reasons — avoid all of them:

| Common rejection reason | Your answer |
|---|---|
| "We can't verify the use case" | Your screencast shows the live dashboard clearly |
| "You're accessing other people's data" | You're only reading your own accounts |
| "No privacy policy" | Add one before submitting — even a simple page works |
| "App purpose is unclear" | Be explicit: personal business dashboard, one user, own account only |

---

## After Approval

Once Meta approves the permissions:

1. Get your **Page Access Token** from the Graph API Explorer: https://developers.facebook.com/tools/explorer/
2. Add this environment variable to Render: `META_ACCESS_TOKEN=your_token_here`
3. The dashboard webhook is already set up to receive live data — it will just start working

**Webhook URL already registered:** https://tribal-cowboy-webhook.onrender.com/webhook
**Verify token already set:** `tribalcowboy2024`

---

## Timeline

Meta App Review typically takes **5–10 business days**. Submit on a Monday for best turnaround. If rejected, they give specific feedback — reply to the rejection with the clarification they ask for and resubmit. Second submissions are usually faster.
