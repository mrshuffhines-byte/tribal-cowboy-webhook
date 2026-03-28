const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const https = require('https');
const app = express();

app.use(cors());
app.use(express.json());

// Serve the dashboard HTML at the root URL
app.use(express.static(__dirname));

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

// ── META GRAPH API HELPERS ─────────────────────────────────────────────────
function graphGet(path) {
  return new Promise((resolve, reject) => {
    const url = `https://graph.facebook.com/v19.0${path}`;
    https.get(url, (res) => {
      let raw = '';
      res.on('data', chunk => raw += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(raw);
          if (json.error) reject(new Error(json.error.message));
          else resolve(json);
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', reject);
  });
}

// ── PULL INSTAGRAM STATS ───────────────────────────────────────────────────
async function refreshInstagram() {
  const token = process.env.META_ACCESS_TOKEN;
  const igId  = process.env.IG_USER_ID;
  if (!token || !igId) {
    console.log('Instagram refresh skipped — META_ACCESS_TOKEN or IG_USER_ID not set');
    return;
  }

  try {
    // Follower count
    const profile = await graphGet(`/${igId}?fields=followers_count,media_count&access_token=${token}`);
    igData.followers = profile.followers_count || igData.followers;

    // 7-day insights: reach, impressions, profile_views
    try {
      const insights = await graphGet(
        `/${igId}/insights?metric=reach,impressions,profile_views&period=week&access_token=${token}`
      );
      (insights.data || []).forEach(metric => {
        const latest = metric.values?.[metric.values.length - 1]?.value || 0;
        if (metric.name === 'reach')         igData.reach         = latest;
        if (metric.name === 'impressions')   igData.impressions   = latest;
        if (metric.name === 'profile_views') igData.profile_views = latest;
      });
    } catch (insightErr) {
      // insights require instagram_manage_insights — log but don't crash
      console.warn('IG insights error (token may need instagram_manage_insights):', insightErr.message);
    }

    // Recent 5 posts
    try {
      const media = await graphGet(
        `/${igId}/media?fields=caption,like_count,comments_count,timestamp,media_type,permalink&limit=5&access_token=${token}`
      );
      igData.posts = (media.data || []).map(p => ({
        caption:   (p.caption || '').slice(0, 120),
        likes:     p.like_count     || 0,
        comments:  p.comments_count || 0,
        timestamp: p.timestamp,
        url:       p.permalink
      }));
    } catch (mediaErr) {
      console.warn('IG media fetch error:', mediaErr.message);
    }

    igData.last_updated = new Date().toISOString();
    saveData();
    console.log(`Instagram refreshed — followers: ${igData.followers}, reach: ${igData.reach}`);
  } catch (err) {
    console.error('Instagram refresh failed:', err.message);
  }
}

// ── PULL FACEBOOK STATS ────────────────────────────────────────────────────
async function refreshFacebook() {
  const token  = process.env.META_ACCESS_TOKEN;
  const pageId = process.env.FB_PAGE_ID;
  if (!token || !pageId) {
    console.log('Facebook refresh skipped — META_ACCESS_TOKEN or FB_PAGE_ID not set');
    return;
  }

  try {
    // Page followers
    const page = await graphGet(`/${pageId}?fields=fan_count,followers_count&access_token=${token}`);
    fbData.followers = page.followers_count || page.fan_count || fbData.followers;

    // Page insights: reach + engagement
    try {
      const insights = await graphGet(
        `/${pageId}/insights?metric=page_impressions_unique,page_post_engagements,page_views_total&period=week&access_token=${token}`
      );
      (insights.data || []).forEach(metric => {
        const latest = metric.values?.[metric.values.length - 1]?.value || 0;
        if (metric.name === 'page_impressions_unique') fbData.reach      = latest;
        if (metric.name === 'page_post_engagements')  fbData.engagement  = latest;
        if (metric.name === 'page_views_total')        fbData.views       = latest;
      });
    } catch (insightErr) {
      console.warn('FB insights error (token may need pages_read_engagement):', insightErr.message);
    }

    // Recent 5 posts
    try {
      const posts = await graphGet(
        `/${pageId}/posts?fields=message,created_time,likes.summary(true),comments.summary(true),shares&limit=5&access_token=${token}`
      );
      fbData.posts = (posts.data || []).map(p => ({
        message:   (p.message || '').slice(0, 120),
        likes:     p.likes?.summary?.total_count     || 0,
        comments:  p.comments?.summary?.total_count  || 0,
        shares:    p.shares?.count                   || 0,
        timestamp: p.created_time
      }));
    } catch (postErr) {
      console.warn('FB posts fetch error:', postErr.message);
    }

    fbData.last_updated = new Date().toISOString();
    saveData();
    console.log(`Facebook refreshed — followers: ${fbData.followers}, reach: ${fbData.reach}`);
  } catch (err) {
    console.error('Facebook refresh failed:', err.message);
  }
}

// ── DAILY PULL SCHEDULER ───────────────────────────────────────────────────
// Runs once on startup, then every 24 hours.
async function runDailyRefresh() {
  console.log('Running scheduled Meta data refresh...');
  await refreshInstagram();
  await refreshFacebook();
}

// Run once at startup so the dashboard has data immediately
runDailyRefresh();

// Then every 24 hours
setInterval(runDailyRefresh, 24 * 60 * 60 * 1000);

// ── WEBHOOK VERIFICATION ──────────────────────────────────────────────────
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
app.get('/data', (req, res) => {
  res.json({
    instagram: igData,
    facebook: fbData,
    server_time: new Date().toISOString()
  });
});

// ── MANUAL REFRESH TRIGGER ─────────────────────────────────────────────────
// Hit this to force an immediate Meta API pull
app.post('/refresh', async (req, res) => {
  console.log('Manual refresh triggered');
  await runDailyRefresh();
  res.json({ success: true, instagram: igData, facebook: fbData });
});

// ── MANUAL UPDATE ─────────────────────────────────────────────────────────
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
    data_file: fs.existsSync(DATA_FILE) ? 'data.json persisted' : 'data.json not yet written',
    meta_configured: !!(process.env.META_ACCESS_TOKEN && process.env.IG_USER_ID && process.env.FB_PAGE_ID)
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Tribal Cowboy webhook server running on port ${PORT}`);
});
