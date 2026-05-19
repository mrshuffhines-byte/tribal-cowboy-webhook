require('dotenv').config();
const express = require('express');
const fs = require('fs');
const path = require('path');
const https = require('https');

const app = express();
const PORT = process.env.PORT || 3001;
const DATA_FILE = path.join(__dirname, 'data.json');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

function loadData() {
  if (!fs.existsSync(DATA_FILE)) return { waitlist: [] };
  return JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
}

function saveData(data) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

function notifyBySms(entry) {
  const { NOTIFY_SMS, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER } = process.env;
  if (!NOTIFY_SMS || !TWILIO_ACCOUNT_SID || !TWILIO_AUTH_TOKEN || !TWILIO_PHONE_NUMBER) return;

  const body = `ArenaShot waitlist: ${entry.name} (${entry.business || 'no biz'}) — ${entry.event_type}. ${entry.email}`;
  const payload = new URLSearchParams({ To: NOTIFY_SMS, From: TWILIO_PHONE_NUMBER, Body: body }).toString();
  const auth = Buffer.from(`${TWILIO_ACCOUNT_SID}:${TWILIO_AUTH_TOKEN}`).toString('base64');

  const req = https.request({
    method: 'POST',
    hostname: 'api.twilio.com',
    path: `/2010-04-01/Accounts/${TWILIO_ACCOUNT_SID}/Messages.json`,
    headers: {
      'Authorization': `Basic ${auth}`,
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Length': Buffer.byteLength(payload)
    }
  }, (res) => res.on('data', () => {}));
  req.on('error', (err) => console.error('SMS notify failed:', err.message));
  req.write(payload);
  req.end();
}

app.post('/waitlist', (req, res) => {
  const { name, email, business, event_type, volume, notes } = req.body || {};
  if (!name || !email) return res.status(400).json({ error: 'name and email required' });

  const data = loadData();
  const entry = {
    id: `ws_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`,
    name: String(name).trim(),
    email: String(email).trim().toLowerCase(),
    business: business ? String(business).trim() : '',
    event_type: event_type ? String(event_type).trim() : '',
    volume: volume ? String(volume).trim() : '',
    notes: notes ? String(notes).trim() : '',
    user_agent: req.headers['user-agent'] || '',
    received_at: new Date().toISOString()
  };

  if (data.waitlist.some((e) => e.email === entry.email)) {
    return res.json({ ok: true, duplicate: true });
  }

  data.waitlist.push(entry);
  saveData(data);
  notifyBySms(entry);
  res.json({ ok: true, position: data.waitlist.length });
});

app.get('/waitlist/count', (_req, res) => {
  res.json({ count: loadData().waitlist.length });
});

app.get('/health', (_req, res) => {
  res.json({ ok: true, sms_configured: !!(process.env.NOTIFY_SMS && process.env.TWILIO_ACCOUNT_SID) });
});

app.listen(PORT, () => {
  console.log(`ArenaShot landing on http://localhost:${PORT}`);
});
