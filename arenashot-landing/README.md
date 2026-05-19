# ArenaShot — Landing + Waitlist

Validation-phase landing page for ArenaShot, a face-match photo delivery tool built for rodeo, horse show, and fair photographers.

**Status:** Pre-launch. Collecting first 50 photographers to validate before building the SaaS.

---

## Run locally

```bash
npm install
cp .env.example .env   # optional: configure Twilio for SMS notifications
npm start
```

Open http://localhost:3001

## Endpoints

| Method | Route | Purpose |
|--------|-------|---------|
| GET | `/` | Landing page |
| POST | `/waitlist` | Add a signup (name, email, business, event_type, volume, notes) |
| GET | `/waitlist/count` | Current waitlist size |
| GET | `/health` | Health check |

## Storage

Signups live in `data.json` (gitignored). Survives Render free-tier spin-downs because Render mounts a persistent disk.

## Optional: SMS notification on each signup

Set these env vars to get an SMS when someone joins:

```
NOTIFY_SMS=+12085551234
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_PHONE_NUMBER=+12085550000
```

## Deploy to Render

1. Push this to a Git repo (see extraction below if you're spinning out from tribal-cowboy-webhook).
2. Render → New Web Service → connect the repo.
3. Build command: `npm install`
4. Start command: `npm start`
5. Add env vars (optional).
6. Point your domain CNAME at the Render URL.

## Spinning out into its own repo

This folder lives inside `tribal-cowboy-webhook` during validation. When you're ready to make it a real product, extract:

```bash
./extract-to-new-repo.sh ../arenashot
cd ../arenashot
gh repo create arenashot --private --source=. --remote=origin --push
```

That gives you a clean Git history and a deployable repo in under a minute.

## What's next (after 50 signups)

1. **Lock the domain.** arenashot.com — check Namecheap.
2. **Pick the first 10 beta photographers** from the waitlist. Free month in exchange for product feedback + an on-the-record testimonial.
3. **Build the actual SaaS.** Face-match upload pipeline (port `tag-my-photos.py` from `tribal-cowboy-webhook`), photographer dashboard, Stripe billing, branded guest galleries.
4. **Marketing channels.** Facebook groups for rodeo photographers, NRHA, NCHA, USEF photographer lists, Indigenous photographer networks.
