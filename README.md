# Tribal Cowboy Webhook Server

Webhook receiver for the Tribal Cowboy LLC command center dashboard.

## Endpoints

- `GET /` — Health check
- `GET /data` — Get latest Instagram and Facebook data
- `POST /update` — Manually update stats
- `GET /webhook` — Meta webhook verification
- `POST /webhook` — Receive Meta webhook events

## Environment Variables

Set these in Render dashboard:

| Variable | Value |
|----------|-------|
| `VERIFY_TOKEN` | `tribalcowboy2024` |
| `PORT` | Set automatically by Render |

## Deploy on Render

1. Push this folder to a GitHub repo
2. Go to render.com → New Web Service
3. Connect your GitHub repo
4. Set build command: `npm install`
5. Set start command: `npm start`
6. Add environment variable: `VERIFY_TOKEN` = `tribalcowboy2024`
7. Deploy!
