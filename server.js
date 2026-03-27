const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();

app.use(cors());
app.use(express.json());

// Serve dashboard HTML from root directory
app.use(express.static(path.join(__dirname)));

// In-memory data store
let igData = {
  followers: 0, reach: 0, impressions: 0,
  profile_views: 0, posts: [], comments: [], last_updated: null
};
let fbData = {
  followers: 0, reach: 0, engagement: 0, posts: [], last_updated: null
};

// Webhook verification
app.get('/webhook', (req, res) => {
  const VERIFY_TOKEN = process.env.VERIFY_TOKEN || 'tribalcowboy2024';
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];
  if (mode === 'subscribe' && token === VERIFY_TOKEN) {
    console.log('Webhook verified!');
    res.status(200).send(challenge);
  } else {
    res.sendStatus(403);
  }
});

// Receive webhook events
app.post('/webhook', (req, res) => {
  const body = req.body;
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
      });
    });
    res.sendStatus(200);
  } else if (body.object === 'page') {
    fbData.last_updated = new Date().toISOString();
    res.sendStatus(200);
  } else {
    res.sendStatus(404);
  }
});

// Get data
app.get('/data', (req, res) => {
  res.json({ instagram: igData, facebook: fbData, server_time: new Date().toISOString() });
});

// Manual update
app.post('/update', (req, res) => {
  const { type, data } = req.body;
  if (type === 'instagram') {
    igData = { ...igData, ...data, last_updated: new Date().toISOString() };
  } else if (type === 'facebook') {
    fbData = { ...fbData, ...data, last_updated: new Date().toISOString() };
  }
  res.json({ success: true });
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'running', uptime: Math.floor(process.uptime()) + 's' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log('Tribal Cowboy server running on port', PORT));
