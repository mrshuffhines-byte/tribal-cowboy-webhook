const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const https = require('https');
const app = express();

// ── ACUITY SCHEDULING API ─────────────────────────────────────────────────
// Acuity uses Basic Auth with your User ID and API Key
// Set these in Render environment variables:
//   ACUITY_USER_ID    — your Acuity user ID (found in Acuity > Integrations > API)
//   ACUITY_API_KEY    — your Acuity API key
//   ACUITY_BOOKING_URL — your public Acuity scheduling page URL
const ACUITY_BASE = 'https://acuityscheduling.com/api/v1';

function acuityGet(endpoint) {
  const userId = process.env.ACUITY_USER_ID;
  const apiKey = process.env.ACUITY_API_KEY;
  if (!userId || !apiKey) return Promise.reject(new Error('Acuity credentials not configured'));

  const auth = Buffer.from(`${userId}:${apiKey}`).toString('base64');
  return new Promise((resolve, reject) => {
    const url = `${ACUITY_BASE}${endpoint}`;
    https.get(url, { headers: { 'Authorization': `Basic ${auth}` } }, (res) => {
      let raw = '';
      res.on('data', chunk => raw += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(raw)); }
        catch (e) { reject(e); }
      });
    }).on('error', reject);
  });
}

function acuityPost(endpoint, data) {
  const userId = process.env.ACUITY_USER_ID;
  const apiKey = process.env.ACUITY_API_KEY;
  if (!userId || !apiKey) return Promise.reject(new Error('Acuity credentials not configured'));

  const auth = Buffer.from(`${userId}:${apiKey}`).toString('base64');
  const body = JSON.stringify(data);
  return new Promise((resolve, reject) => {
    const urlObj = new URL(`${ACUITY_BASE}${endpoint}`);
    const options = {
      hostname: urlObj.hostname,
      path: urlObj.pathname,
      method: 'POST',
      headers: {
        'Authorization': `Basic ${auth}`,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body)
      }
    };
    const req = https.request(options, (res) => {
      let raw = '';
      res.on('data', chunk => raw += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(raw)); }
        catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// ── TWILIO SMS ────────────────────────────────────────────────────────────
// Set in Render environment variables:
//   TWILIO_ACCOUNT_SID  — your Twilio account SID
//   TWILIO_AUTH_TOKEN   — your Twilio auth token
//   TWILIO_PHONE_NUMBER — your Twilio phone number (e.g. +12085551234)
function sendSMS(to, message) {
  const sid = process.env.TWILIO_ACCOUNT_SID;
  const token = process.env.TWILIO_AUTH_TOKEN;
  const from = process.env.TWILIO_PHONE_NUMBER;
  if (!sid || !token || !from) {
    console.log('Twilio not configured — skipping SMS');
    return Promise.resolve(null);
  }

  // Normalize phone number
  let phone = to.replace(/[^0-9+]/g, '');
  if (!phone.startsWith('+')) phone = '+1' + phone; // assume US

  const body = new URLSearchParams({ To: phone, From: from, Body: message }).toString();
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.twilio.com',
      path: `/2010-04-01/Accounts/${sid}/Messages.json`,
      method: 'POST',
      headers: {
        'Authorization': 'Basic ' + Buffer.from(`${sid}:${token}`).toString('base64'),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': Buffer.byteLength(body)
      }
    };
    const req = https.request(options, (res) => {
      let raw = '';
      res.on('data', chunk => raw += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(raw);
          if (json.error_code) {
            console.error('Twilio error:', json.message);
            reject(new Error(json.message));
          } else {
            console.log(`SMS sent to ${phone}: ${json.sid}`);
            resolve(json);
          }
        } catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

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
  },
  voice_inquiries: []
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
    fs.writeFileSync(DATA_FILE, JSON.stringify({ instagram: igData, facebook: fbData, voice_inquiries: voiceInquiries }, null, 2));
  } catch (err) {
    console.error('Could not write data.json:', err.message);
  }
}

const saved = loadData();
let igData = saved.instagram;
let fbData = saved.facebook;
let voiceInquiries = saved.voice_inquiries || [];

console.log(`Stats loaded — IG followers: ${igData.followers} | FB followers: ${fbData.followers} | Voice inquiries: ${voiceInquiries.length}`);

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
    // Follower count + media count
    const profile = await graphGet(`/${igId}?fields=followers_count,media_count&access_token=${token}`);
    igData.followers = profile.followers_count || igData.followers;

    // 7-day insights: reach, impressions, profile_views
    // period=day with since/until gives rolling 7 days; use period=week for simplicity
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
        `/${pageId}/posts?fields=message,full_picture,created_time,likes.summary(true),comments.summary(true),shares&limit=5&access_token=${token}`
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
// Also runs at 7 AM Pacific (15:00 UTC) each day so stats are fresh each morning.
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
    voice_inquiries: voiceInquiries,
    server_time: new Date().toISOString()
  });
});

// ── MANUAL REFRESH TRIGGER ─────────────────────────────────────────────────
// Hit this endpoint from the dashboard to force an immediate Meta pull
app.post('/refresh', async (req, res) => {
  console.log('Manual refresh triggered');
  await runDailyRefresh();
  res.json({ success: true, instagram: igData, facebook: fbData });
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

// ── VOICE INQUIRY (from ElevenLabs agent) ─────────────────────────────
// The ElevenLabs conversational AI agent posts here when it collects
// booking details from a caller on tribalcowboy.com.
// Now with auto-SMS follow-up via Twilio and Acuity booking link.
app.post('/voice-inquiry', async (req, res) => {
  const { caller_name, service_requested, event_date, guest_count, event_location, phone_number, notes, source } = req.body;
  const inquiry = {
    id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
    caller_name: caller_name || 'Unknown',
    service_requested: service_requested || 'Not specified',
    event_date: event_date || '',
    guest_count: guest_count || '',
    event_location: event_location || '',
    phone_number: phone_number || '',
    notes: notes || '',
    source: source || 'Voice Assistant',
    status: 'New',
    sms_sent: false,
    received_at: new Date().toISOString()
  };
  voiceInquiries.unshift(inquiry);
  // Keep last 50 inquiries
  if (voiceInquiries.length > 50) voiceInquiries = voiceInquiries.slice(0, 50);
  saveData();
  console.log(`Voice inquiry received: ${inquiry.caller_name} — ${inquiry.service_requested}`);

  // Auto-send SMS follow-up if we have a phone number
  if (phone_number) {
    try {
      const bookingUrl = process.env.ACUITY_BOOKING_URL || 'https://www.tribalcowboy.com';
      const smsMessage = `Hey ${caller_name || 'there'}! Thanks for reaching out to Tribal Cowboy. ` +
        `Here's our booking link so you can check availability and lock in your date: ${bookingUrl} ` +
        `\n\nQuestions? Just reply to this text or email info@tribalcowboy.com. Talk soon!`;
      await sendSMS(phone_number, smsMessage);
      inquiry.sms_sent = true;
      inquiry.sms_sent_at = new Date().toISOString();
      saveData();
      console.log(`Auto-SMS sent to ${phone_number} for inquiry ${inquiry.id}`);
    } catch (smsErr) {
      console.error('Auto-SMS failed:', smsErr.message);
    }
  }

  res.json({ success: true, inquiry });
});

// Read all voice inquiries
app.get('/voice-inquiries', (req, res) => {
  res.json({ inquiries: voiceInquiries });
});

// Update a voice inquiry status (e.g. mark as contacted, booked, etc.)
app.patch('/voice-inquiry/:id', (req, res) => {
  const { id } = req.params;
  const { status, notes } = req.body;
  const inquiry = voiceInquiries.find(i => i.id === id);
  if (!inquiry) return res.status(404).json({ error: 'Inquiry not found' });
  if (status) inquiry.status = status;
  if (notes) inquiry.notes = notes;
  inquiry.updated_at = new Date().toISOString();
  saveData();
  res.json({ success: true, inquiry });
});

// ── ACUITY: CHECK AVAILABILITY ────────────────────────────────────────────
// ElevenLabs agent (or dashboard) can call this to check open dates
// GET /acuity/availability?date=2026-06-15&appointmentTypeID=12345
app.get('/acuity/availability', async (req, res) => {
  const { date, appointmentTypeID } = req.query;
  if (!date) return res.status(400).json({ error: 'date parameter required (YYYY-MM-DD)' });

  try {
    // If no appointment type specified, get all types first
    let typeParam = appointmentTypeID ? `&appointmentTypeID=${appointmentTypeID}` : '';
    const slots = await acuityGet(`/availability/dates?month=${date.slice(0, 7)}${typeParam}`);
    res.json({ available_dates: slots, month: date.slice(0, 7) });
  } catch (err) {
    console.error('Acuity availability check failed:', err.message);
    res.status(500).json({ error: err.message });
  }
});

// ── ACUITY: LIST APPOINTMENT TYPES ────────────────────────────────────────
// Returns all your Acuity appointment types so the agent knows what to offer
app.get('/acuity/appointment-types', async (req, res) => {
  try {
    const types = await acuityGet('/appointment-types');
    res.json({ appointment_types: types });
  } catch (err) {
    console.error('Acuity appointment types failed:', err.message);
    res.status(500).json({ error: err.message });
  }
});

// ── ACUITY: GET TIME SLOTS ────────────────────────────────────────────────
// Returns available time slots for a specific date and appointment type
// GET /acuity/times?date=2026-06-15&appointmentTypeID=12345
app.get('/acuity/times', async (req, res) => {
  const { date, appointmentTypeID } = req.query;
  if (!date || !appointmentTypeID) {
    return res.status(400).json({ error: 'date and appointmentTypeID required' });
  }
  try {
    const times = await acuityGet(`/availability/times?date=${date}&appointmentTypeID=${appointmentTypeID}`);
    res.json({ available_times: times, date });
  } catch (err) {
    console.error('Acuity times check failed:', err.message);
    res.status(500).json({ error: err.message });
  }
});

// ── ACUITY: BOOK APPOINTMENT ──────────────────────────────────────────────
// ElevenLabs agent calls this to actually create a booking
// POST /acuity/book { appointmentTypeID, datetime, firstName, lastName, email, phone, notes }
app.post('/acuity/book', async (req, res) => {
  const { appointmentTypeID, datetime, firstName, lastName, email, phone, notes } = req.body;
  if (!appointmentTypeID || !datetime || !firstName) {
    return res.status(400).json({ error: 'appointmentTypeID, datetime, and firstName are required' });
  }
  try {
    const appointment = await acuityPost('/appointments', {
      appointmentTypeID,
      datetime,
      firstName,
      lastName: lastName || '',
      email: email || '',
      phone: phone || '',
      notes: notes || ''
    });
    console.log(`Acuity booking created: ${appointment.id} for ${firstName} on ${datetime}`);

    // Also log it as a voice inquiry marked as Booked
    const inquiry = {
      id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
      caller_name: `${firstName} ${lastName || ''}`.trim(),
      service_requested: appointment.type || 'Acuity Booking',
      event_date: datetime,
      guest_count: '',
      event_location: '',
      phone_number: phone || '',
      notes: notes || '',
      source: 'Voice Assistant — Direct Book',
      status: 'Booked',
      acuity_id: appointment.id,
      received_at: new Date().toISOString()
    };
    voiceInquiries.unshift(inquiry);
    if (voiceInquiries.length > 50) voiceInquiries = voiceInquiries.slice(0, 50);
    saveData();

    // Send confirmation SMS
    if (phone) {
      try {
        const confirmMsg = `You're booked with Tribal Cowboy! ${firstName}, we've got you down for ${new Date(datetime).toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' })}. ` +
          `We'll follow up with details closer to your date. Questions? Reply here or email info@tribalcowboy.com.`;
        await sendSMS(phone, confirmMsg);
      } catch (smsErr) {
        console.error('Booking confirmation SMS failed:', smsErr.message);
      }
    }

    res.json({ success: true, appointment, inquiry });
  } catch (err) {
    console.error('Acuity booking failed:', err.message);
    res.status(500).json({ error: err.message });
  }
});

// ── TWILIO: SEND BOOKING LINK ─────────────────────────────────────────────
// Manual trigger to text someone the booking link
// POST /send-booking-link { phone, name }
app.post('/send-booking-link', async (req, res) => {
  const { phone, name } = req.body;
  if (!phone) return res.status(400).json({ error: 'phone number required' });

  const bookingUrl = process.env.ACUITY_BOOKING_URL || 'https://www.tribalcowboy.com';
  const message = `Hey ${name || 'there'}! Here's the link to book with Tribal Cowboy: ${bookingUrl}\n\nPick the service you're interested in, choose your date, and you're set. Reply to this text if you have any questions!`;

  try {
    await sendSMS(phone, message);
    res.json({ success: true, message: `Booking link sent to ${phone}` });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ── HEALTH CHECK ──────────────────────────────────────────────────────────
app.get('/health', (req, res) => {
  res.json({
    status: 'Tribal Cowboy Webhook Server is running',
    instagram_last_updated: igData.last_updated || 'No data yet',
    facebook_last_updated: fbData.last_updated || 'No data yet',
    uptime: Math.floor(process.uptime()) + ' seconds',
    data_file: fs.existsSync(DATA_FILE) ? 'data.json persisted' : 'data.json not yet written',
    voice_inquiries: voiceInquiries.length,
    meta_configured: !!(process.env.META_ACCESS_TOKEN && process.env.IG_USER_ID && process.env.FB_PAGE_ID),
    acuity_configured: !!(process.env.ACUITY_USER_ID && process.env.ACUITY_API_KEY),
    twilio_configured: !!(process.env.TWILIO_ACCOUNT_SID && process.env.TWILIO_AUTH_TOKEN && process.env.TWILIO_PHONE_NUMBER)
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Tribal Cowboy webhook server running on port ${PORT}`);
});
