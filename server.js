const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const app = express();

app.use(cors());
app.use(express.json());

// Serve the dashboard HTML at the root URL
app.use(express.static(path.join(__dirname, 'public')));

// ── PERSISTENT STORAGE ────────────────────────────────────────────────────
// Stats are saved to data.json so they survive Render free tier spin-downs.
// Note: a full redeploy will reset the filesystem — for that, add a Render
// Persistent Disk or migrate to a hosted DB like Supabase (free tier).
const DATA_FILE = path.join(__dirname, 'data.json');

const DEFAULT_DATA = {
  instagram: {
    followers: 0, reach: 0, impressions: 0, profile_views: 0,
    posts: [], comments: [], last_updated: null
  },
  facebook: {
    followers: 0, reach: 0, engagement: 0,
    posts: [], last_updated: null
  }
};

function loadData() {
  try {
    if (fs.existsSync(DATA_FILE)) {
      const raw = fs.readFileSync(DATA_FILE, 'utf8');
      const parsed = JSON.parse(raw);
      console.log('Loaded data.json from disk');
      return parsed;
    }
  } catch (err) {
    console.error('Could not read data.json, using defaults:', err.message);
  }
  return JSON.parse(JSON.stringify(DEFAULT_DATA));
}

function saveData() {
  try {
    fs.writeFileSync(DATA_FILE, JSON.stringify({ instagram: igData, facebook: fbData }, null, 2));
  } catch (err) {
    console.error('Could not write data.json:', err.message);
  }
}

const saved = loadData();
let igData = saved.instagram;
let fbData = saved.facebook;

console.log(`Stats loaded — IG followers: ${igData.followers} | FB followers: ${fbData.followers}`);

// ── WEBHOOK VERIFICATION ──────────────────────────────────────────────────
// Meta calls this URL when you register the webhook to confirm it is real
app.get('/webhook', (req, res) => {
  const VERIFY_TOKEN = process.env.VERIFY_TOKEN || 'tribalcowboy2024';
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  if (mode === 'subscribe' && token === VERIFY_TOKEN) {
    console.log('Webhook verified by Meta!');
    res.status(200).send(challenge);
  } else {
    console.log('Webhook verification failed');
    res.sendStatus(403);
  }
});

// ── RECEIVE WEBHOOK EVENTS ────────────────────────────────────────────────
// Meta sends data here whenever something happens on Instagram or Facebook
app.post('/webhook', (req, res) => {
  const body = req.body;
  console.log('Webhook received:', JSON.stringify(body, null, 2));

  if (body.object === 'instagram') {
    body.entry.forEach(entry => {
      (entry.changes || []).forEach(change => {
        if (change.field === 'comments') {
          igData.comments.unshift({
            text: change.value.text || '',
            from: change.value.from?.username || 'someone',
            timestamp: new Date().toISOString(),
            source: 'Instagram'
          });
          if (igData.comments.length > 10) igData.comments.pop();
          igData.last_updated = new Date().toISOString();
        }
        if (change.field === 'mentions') {
          igData.last_updated = new Date().toISOString();
        }
      });
    });
    saveData();
    res.sendStatus(200);

  } else if (body.object === 'page') {
    body.entry.forEach(entry => {
      (entry.changes || []).forEach(change => {
        if (change.field === 'feed') {
          fbData.last_updated = new Date().toISOString();
        }
      });
    });
    saveData();
    res.sendStatus(200);

  } else {
    res.sendStatus(404);
  }
});

// ── READ DATA ─────────────────────────────────────────────────────────────
// Dashboard fetches this URL to get the latest data
app.get('/data', (req, res) => {
  res.json({
    instagram: igData,
    facebook: fbData,
    server_time: new Date().toISOString()
  });
});

// ── MANUAL UPDATE ─────────────────────────────────────────────────────────
// Dashboard can push your manually entered stats here
app.post('/update', (req, res) => {
  const { type, data } = req.body;
  if (type === 'instagram') {
    igData = { ...igData, ...data, last_updated: new Date().toISOString() };
    console.log('Instagram data updated manually:', data);
  } else if (type === 'facebook') {
    fbData = { ...fbData, ...data, last_updated: new Date().toISOString() };
    console.log('Facebook data updated manually:', data);
  }
  saveData();
  res.json({ success: true });
});

// ── HEALTH CHECK ──────────────────────────────────────────────────────────
app.get('/health', (req, res) => {
  res.json({
    status: 'Tribal Cowboy Webhook Server is running',
    instagram_last_updated: igData.last_updated || 'No data yet',
    facebook_last_updated: fbData.last_updated || 'No data yet',
    uptime: Math.floor(process.uptime()) + ' seconds',
    data_file: fs.existsSync(DATA_FILE) ? 'data.json persisted' : 'data.json not yet written'
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Tribal Cowboy webhook server running on port ${PORT}`);
});
