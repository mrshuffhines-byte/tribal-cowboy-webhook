# Reel System v2: voice over, attention clips, algorithm feedback

Date: 2026-09-30
Owner: Stacie (Tribal Cowboy)
Status: draft for review

## Goal

Extend the Yap Edits setup so Stacie can make four kinds of short video from one drop folder, learn from Metricool what holds attention, pull weekly trend ideas mapped onto the ranch, and schedule to Instagram, Facebook and TikTok at the best hour. Every step asks her what she wants instead of expecting her to remember a convention. A visual PDF guide explains the whole loop.

## Non goals

- No rebuild of the video editor in Claude Code. Cowork in the Claude desktop app keeps doing the cutting and rendering.
- No AI generated footage. Real ranch clips only.
- No AI voice in this version. Own voice memos are the default. AI voice is a later piece with its own approval.
- No auto posting. Every schedule call waits for an explicit yes.
- No Blotato publishing. Metricool is the scheduler and the analytics source.

## Division of labor

| Job | Where | Why |
|---|---|---|
| Cut, caption, headline, render | Cowork (desktop app) | Already set up, already has the Playbook and brand kit |
| Ask which kind of video, collect the inputs | Cowork first message, or `/reel` in Claude Code | Stacie should be asked, never expected to remember |
| Analytics, trends, hooks, competitor research, captions, scheduling | Claude Code in `~/TribalCowboy-Social` | Only Claude Code can reach Metricool, Apify, Higgsfield, Firecrawl |

## Piece 1: Editor Prompt v2 with two new formats

The Editor Prompt docx in `Yap Edits files/` gains a section 10, Video Types. Cowork's Project instructions gain one line: "Before editing, ask me which type of video this is and how long it should run, then confirm the inputs you found."

**Type A: Talking reel.** Unchanged. One clip of Stacie talking. Playbook formats A to D apply.

**Type B: Voice over reel.** Inputs: a subfolder in the drop folder holding 3 to 10 clips plus one voice memo (`.m4a` or `.mp3`). Cowork transcribes the memo, orders the clips to match the words (a horse's name lands on that horse), cuts each clip to the sentence it covers, adds one word captions at the bottom third since there is no chin to anchor to, headlines in the upper third, series tag, Follow ending. Silence trimming applies to the voice track, not the footage. Clips shorter than the sentence get a slow push in; never a freeze frame.

**Type C: Highlight cut.** Input: one clip longer than 60 seconds. Cowork scans for the 5 to 15 second stretches with the most motion, faces, or reaction sound, returns each as its own vertical clip with a text hook on frame one and the Follow ending. Target 3 to 5 clips per source. Each clip is named `highlight-01.mp4` and so on with a one line description in `highlights.txt`.

**Type D: Trend remix.** Input: the trend brief entry (see piece 3) and Stacie's clip filmed for it. Cowork edits to the length and beat structure the brief specifies. Audio is added at posting time in Instagram or TikTok, so Cowork leaves a 2 second lead and exports without music.

**The type question.** When Stacie drops files and sends the standard message, Cowork's first reply lists what it found (files, durations) and asks: "Which type: A talking, B voice over, C highlight, D trend? How long should it run: under 30 s, 30 to 60 s, or 60 to 90 s? Setting: outdoor, truck, or indoor?" It waits for her answer before doing anything.

**Edited folder layout.** `Edited/YYYY-MM-DD-slug/` holds the render, the transcript, and the overlay plan. `/schedule-reel` reads from here.

## Piece 2: `/reel-report`

Claude Code command. Pulls Instagram reels for the last 30 days from Metricool (`getAnalyticsDataByMetrics`, fields: content, url, views, reach, retention, averageWatchTime, reelsViewRate, saved, shares, comments, durationSeconds) and TikTok posts where available. Ranks by reelsViewRate then retention. Output in chat:

1. Top three and bottom three reels with the numbers and the first line of their captions.
2. Patterns: which horses, which hook styles, which lengths, which posting hours held people.
3. One or two proposed rules in the My Rules.md format, marked as proposals. Stacie says yes before anything is written.
4. Best posting hours for the next week per network from `getBestTimeToPostByNetwork`.

Appends a dated summary to `content/reels-log.md`. If Metricool returns no reels, it says so and stops.

## Piece 3: `/trend-brief`

Weekly. Sources in order, each optional if it fails:

1. Firecrawl search: TikTok Creative Center trend pages, Instagram trend roundups from the last 7 days, queries scoped to equine, ranch, western, animals, small business.
2. Apify: Instagram hashtag scraper and TikTok hashtag scraper on a fixed list (`#clydesdale`, `#minihorse`, `#ranchlife`, `#horsesoftiktok`, `#idaho`, plus any Stacie adds in `content/trends/hashtags.md`). Top 20 posts each by views in the last 7 days.
3. Higgsfield `tiktok_music_trending` once Stacie links TikTok in Higgsfield. Until then, skipped with a one line note.
4. Metricool best hours.

Output: `content/trends/YYYY-MM-DD.md` with 3 to 5 ideas. Each idea has: the trend in one sentence, the ranch version in one sentence, the hook line, the exact shot to film (camera position, which horse, how long), the audio to use at posting, and the video type letter. Chat shows the same list. No idea uses a banned phrase.

## Piece 4: `/hooks <topic>`

Writes five hooks for the topic in Stacie's voice (stacie voice skill plus brand memory). Scores each 1 to 5 on: matches a pattern from the latest reel report, matches a format from the latest trend brief, specific detail present, under 8 words. Shows the table, recommends the top two, offers to save them to `content/hooks.md`.

## Piece 5: `/niche-watch`

Reads `content/trends/accounts.md` (Stacie fills in 10 Instagram or TikTok handles; the command asks her for them if the file is empty). Apify profile scraper pulls the last 30 days per account. Ranks all posts by views. For the top ten: format, hook style, length, on screen text, sound. Writes `content/trends/niche-YYYY-MM-DD.md` with a section "Formats to steal this week" written as filmable briefs. Runs weekly alongside the trend brief.

## Piece 6: AI voice (deferred)

Not built in this version. Placeholder: a `/narrate` command that takes a script and an ElevenLabs cloned voice and writes `voice.m4a` into a reel subfolder. Requires 2 to 3 minutes of clean recordings from Stacie to clone. Posts made with it set the AI generated flag on Instagram and TikTok. Gets its own approval when Stacie says the clone sounds right.

## Piece 7: `/schedule-reel` upgrade

- Adds TikTok as a third provider (`tiktokData` with title, privacy PUBLIC_TO_EVERYONE, comments on, duet and stitch on).
- Reads the type from the Edited subfolder and adapts the caption: voice over reels get a first line that names the horse on screen; highlight cuts get a one line caption and a question; trend remixes get the audio name in the caption for Instagram.
- Defaults the time to the best hour on Instagram from Metricool in the next 3 days, then asks.
- Everything else unchanged: Dropbox link, explicit yes, log line.

## Piece 8: The visual guide (PDF)

`Yap Edits files/How to make a reel.pdf`. Tribal Cowboy brand layout. Built for an ADHD reader:

- One page per stage: Film, Drop, Ask and edit, Review, Schedule, Weekly (trends and report). Six pages plus a one page map at the front.
- Each page: a big step number, one sentence of what to do, a picture, a three item checklist, and "what you say to Claude" in a copy box. Nothing else.
- Pictures are drawn illustrations of the actual screens and folders (the Finder folder with the subfolders, the Claude app message box with the Cowork switch, the type question reply, the Dropbox right click, the Metricool queue), not stock art. Rendered as SVG inside the page so they stay sharp.
- The front page map shows the loop as a circle: film → drop → answer the type question → review → schedule → report → next idea.
- Sentences under 12 words where possible. No paragraphs over two sentences. Cream pages, dark header, gold step numbers.
- Delivered after pieces 1, 2, 3 and 7 exist so the pictures match reality.

## Data flow

```
phone clips + voice memo
   → Documents/Claude Yap Edits ready to edit/<subfolder>/
   → Cowork asks type, length, setting → edits → Edited/<date-slug>/
   → /schedule-reel (Claude Code) → Dropbox link → Metricool → IG, FB, TikTok
   → /reel-report (weekly) reads Metricool → proposes rules → My Rules.md
   → /trend-brief + /niche-watch (weekly) → content/trends/ → next thing to film
   → /hooks before filming a talking reel
```

## Error handling

- Metricool empty or errors: say so, stop, never invent numbers.
- Apify actor fails or token missing: skip that source, note it, continue with the rest.
- Higgsfield TikTok not linked: skip music, print the link once.
- Dropbox link missing `dl=1`: fix it silently.
- Any banned phrase in generated text: rewrite before showing.
- Cowork cannot find a voice memo in a type B folder: ask for it, do not narrate with a synthetic voice.

## Testing

- Piece 1: one real clip of each type through Cowork; check the type question fires and the Edited subfolder layout matches.
- Piece 2: run against the live Metricool account; verify the ranking matches the Metricool web UI for the top reel.
- Piece 3 and 5: run once; every idea must name a horse or a place and pass the banned phrase check.
- Piece 7: schedule one reel as a draft (`draft: true`) to all three networks, confirm it appears in Metricool, then delete it.
- Piece 8: print the PDF, hand it to Stacie, watch her do one full loop without asking a question.

## Order of work

1, 7, 2, 3, 4, 5, 8. Piece 6 waits.
