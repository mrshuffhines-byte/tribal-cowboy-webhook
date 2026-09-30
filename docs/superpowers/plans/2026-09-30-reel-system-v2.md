# Reel System v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give Stacie four video types from one drop folder, a weekly loop that learns from Metricool and trends, scheduling to three networks at the best hour, and a visual guide that explains the loop.

**Architecture:** Cowork (Claude desktop app) keeps editing; its behavior is steered by a new section in the Editor Prompt docx and one Project instruction line. Everything that touches data lives in `~/TribalCowboy-Social` as slash commands (`.claude/commands/*.md`) that Claude Code executes with the Metricool, Apify, Firecrawl and Higgsfield MCP tools. Two small Python helpers (a docx updater and a voice checker) and one guide generator are the only code.

**Tech Stack:** Claude Code slash commands (markdown), python-docx via `uv run --with python-docx`, Python 3 with Pillow, headless Google Chrome for PDF, pdftoppm for QA, Metricool MCP, Apify MCP, Firecrawl MCP, Higgsfield MCP.

**Spec:** `docs/superpowers/specs/2026-09-30-reel-system-v2-design.md`

## Global Constraints

- Drop folder: `~/Documents/Claude Yap Edits ready to edit/`; finished renders in `Edited/YYYY-MM-DD-slug/`; prompt files in `Yap Edits files/`.
- Metricool brand id `6106320`; timezone `America/Los_Angeles`; networks instagram, facebook, tiktok.
- No schedule call without an explicit yes from Stacie in the same conversation.
- No invented numbers about horses or performance. Empty data means say so and stop.
- Every generated caption, hook, or idea passes the banned phrase list in `memory/brand-memory.md`. One exclamation mark maximum.
- Horse names spelled exactly: Belle, Millie, Abby, Jill, Reba, Dolly, Lainey, Minimus, Monster, Master Chief, Jolene, Rowdy, Nash.
- Prose written for Stacie contains no hyphen characters (her global writing rule). File names and command names may.
- Guide PDF: US Letter, Tribal Cowboy brand layout (dark header bar, cream page, gold step numbers, Cormorant Garamond headings, Montserrat body), footer with `www.tribalcowboy.com` and `info@tribalcowboy.com`.

## Review Focus

1. A voice memo recorded as `.m4a` with an uppercase extension or as a Voice Memos `.caf` file: the type B instructions must still find it. Test in Task 1 step 4 lists every audio extension Cowork should accept.
2. Metricool returns reels but `reelsViewRate` is null for the newest ones (analytics lag): the report must rank by retention for those rows instead of crashing or ranking nulls first. Pinned in Task 4 step 2.
3. A trend brief idea that names a horse not in the herd (a model hallucinating "Duke"): the voice checker must reject unknown horse names. Pinned in Task 3 step 1.
4. `/schedule-reel` when the Edited subfolder has two renders (draft 1 and draft 2): it must pick the newest by modified time and say which one. Pinned in Task 2 step 3.
5. Guide PDF spilling to a seventh page on a font fallback (no network for Google Fonts): the generator must assert the page count equals 7 and fail loudly. Pinned in Task 8 step 5.

---

### Task 1: Editor Prompt v2 with the four video types

**Files:**
- Create: `scripts/update_editor_prompt.py`
- Modify: `~/Documents/Claude Yap Edits ready to edit/Yap Edits files/Yap_Edits_Editor_Prompt.docx` (append section 10)
- Modify: `~/Documents/Claude Yap Edits ready to edit/Yap Edits files/README first.md`
- Create: `docs/cowork-project-instructions.md` (the text Stacie pastes into the Claude Project)

**Interfaces:**
- Consumes: nothing.
- Produces: the section title string `10. VIDEO TYPES` in the docx; the type letters A, B, C, D; the Edited layout `Edited/YYYY-MM-DD-slug/` with `render.mp4`, `transcript.txt`, `overlay-plan.md`, `type.txt` (one letter). Task 2 reads `type.txt`.

- [ ] **Step 1: Write the read back check that fails**

Create `scripts/check_editor_prompt.py`:

```python
import sys
from docx import Document
P = "/Users/staciehuffhines/Documents/Claude Yap Edits ready to edit/Yap Edits files/Yap_Edits_Editor_Prompt.docx"
text = "\n".join(p.text for p in Document(P).paragraphs)
required = [
    "10. VIDEO TYPES",
    "Type A",
    "Type B",
    "Type C",
    "Type D",
    "Which type",
    ".m4a, .mp3, .caf, .wav, .aac",
    "type.txt",
    "bottom third",
    "highlight-01.mp4",
]
missing = [r for r in required if r not in text]
print("missing:", missing)
sys.exit(1 if missing else 0)
```

- [ ] **Step 2: Run it to confirm it fails**

Run: `cd ~/TribalCowboy-Social && uv run --quiet --with python-docx python3 scripts/check_editor_prompt.py`
Expected: `missing: ['10. VIDEO TYPES', ...]` and exit code 1.

- [ ] **Step 3: Write the updater**

Create `scripts/update_editor_prompt.py`:

```python
import copy
from docx import Document
from docx.text.paragraph import Paragraph

P = "/Users/staciehuffhines/Documents/Claude Yap Edits ready to edit/Yap Edits files/Yap_Edits_Editor_Prompt.docx"
d = Document(P)
paras = d.paragraphs
if any(p.text.startswith("10. VIDEO TYPES") for p in paras):
    raise SystemExit("section 10 already present; nothing to do")
heading_src = next(p for p in paras if p.text.startswith("9. TRIBAL COWBOY RULES"))
bullet_src = next(p for p in paras if p.text.startswith("- Background:"))
blank_src = next(p for p in paras if p.text == "")
body = d.element.body
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def add(src, text):
    new = copy.deepcopy(src._p)
    body.append(new)
    par = Paragraph(new, src._parent)
    if par.runs:
        par.runs[0].text = text
        for r in par.runs[1:]:
            r.text = ""
    elif text:
        par.add_run(text)

add(blank_src, "")
add(heading_src, "10. VIDEO TYPES")
lines = [
    "- Before you edit anything, list the files you found with their durations, then ask me three things and wait for my answer: Which type: A talking, B voice over, C highlight, D trend? How long should it run: under 30 s, 30 to 60 s, or 60 to 90 s? Setting: outdoor, truck, or indoor? Do nothing until I reply.",
    "- Type A, talking reel: one clip of me talking to camera. Everything in sections 1 to 9 applies. Pick a Playbook format (A to D) and tell me why.",
    "- Type B, voice over reel: a subfolder holding 3 to 10 clips plus one voice memo (.m4a, .mp3, .caf, .wav, .aac, any capitalization). Transcribe the memo with word timestamps. Order the clips so each sentence lands on the footage it describes: a horse's name lands on that horse, a place name on that place. Cut each clip to the length of its sentence. If a clip is shorter than its sentence, slow push in 1.0 to 1.08x; never freeze a frame. Silence trimming applies to the voice, not the footage. One word captions sit in the bottom third, centered, since there is no chin to anchor to. Headlines and notes sit in the upper third, below the top 15 percent. Series tag on frame one. Follow ending. If no voice memo is in the folder, ask me for it; never narrate with a synthetic voice.",
    "- Type C, highlight cut: one clip longer than 60 seconds. Scan it for the 5 to 15 second stretches with the most motion, faces, or reaction sound. Return 3 to 5 separate vertical clips named highlight-01.mp4, highlight-02.mp4 and so on. Each starts with a text hook on frame one, keeps the natural sound, and ends with the Follow button. Write highlights.txt with one line per clip: file name, start and end time in the source, and a six word description.",
    "- Type D, trend remix: I give you a trend brief entry (the trend, the ranch version, the hook, the length, the beat structure) and the clip I filmed for it. Edit to the length and beats in the brief. Leave a 2 second lead at the start and export with no music; the sound gets added in Instagram or TikTok when I post.",
    "- Output for every type: a folder Edited/YYYY-MM-DD-slug/ holding render.mp4 (or the highlight files), transcript.txt, overlay-plan.md, and type.txt containing the single type letter. Tell me the folder name when you finish.",
]
for t in lines:
    add(bullet_src, t)
sect = body.find(W + "sectPr")
if sect is not None:
    body.remove(sect)
    body.append(sect)
d.save(P)
print("section 10 added")
```

- [ ] **Step 4: Run the updater, then the check**

Run: `cd ~/TribalCowboy-Social && uv run --quiet --with python-docx python3 scripts/update_editor_prompt.py && uv run --quiet --with python-docx python3 scripts/check_editor_prompt.py`
Expected: `section 10 added` then `missing: []` and exit code 0. Run the updater a second time and expect `section 10 already present; nothing to do`.

- [ ] **Step 5: Write the Project instructions file**

Create `docs/cowork-project-instructions.md`:

```markdown
# Paste this into the Claude Project "Yap Edits Reel Editor" → Instructions

For every video I upload or point you to, act as my reel editor. Follow the Yap Edits Editor Prompt and the Yap Edits Playbook in this project's files exactly, using my brand kit, the Tribal Cowboy Rules section, and the Video Types section. Also read My Rules.md and treat those rules as overriding the prompt where they conflict. Use the files in my Assets folder before generating anything. Before editing, list the files you found, then ask me which type of video this is, how long it should run, and the setting, and wait for my answer. Do the full edit yourself and save it to a dated subfolder in Edited with render.mp4, transcript.txt, overlay-plan.md and type.txt. Send me a short list of what you did. When I ask for changes, apply them and give me the change as a one line rule to paste into My Rules.md.

# The message Stacie sends for every new reel

Please request access to my folder called "Claude Yap Edits ready to edit" in Documents. Look at what is new in it, ask me the three questions, then edit using my Yap Edits Editor Prompt, the Playbook, and My Rules.md. Save the draft to the Edited subfolder.
```

- [ ] **Step 6: Update the README in the drop folder**

Replace the contents of `~/Documents/Claude Yap Edits ready to edit/Yap Edits files/README first.md` with:

```markdown
# Yap Edits files — what goes here

Upload these three to the Claude Project "Yap Edits Reel Editor": Yap_Edits_Playbook.pdf, Yap_Edits_Editor_Prompt.docx, My Rules.md.
When the Editor Prompt changes, replace the copy in the Project. My Rules.md is read from this folder, so editing it here is enough.

Four video types. Claude asks you which one each time.
- A talking: one clip of you talking. Drop it in the main folder.
- B voice over: make a subfolder, put 3 to 10 clips in it plus one voice memo.
- C highlight: one long clip (over 60 s) in the main folder. You get 3 to 5 short clips back.
- D trend: the clip you filmed for a trend brief idea. Paste the idea into the chat.

reference.mp4 (add it yourself): one talking reel you admire, screen recorded. Claude matches its pacing.
Finished drafts land in Edited/<date-slug>/. Then run /schedule-reel in Claude Code.
```

- [ ] **Step 7: Live check with Cowork**

Drop one 20 second phone clip in the main folder, send the standard message in the Project with Cowork on. Expected: the first reply lists the file and its duration and asks the three questions, and does not start editing. Answer "A, under 30 s, outdoor". Expected: an `Edited/<date>-<slug>/` folder with `render.mp4`, `transcript.txt`, `overlay-plan.md`, `type.txt` containing `A`. If Cowork skipped the questions, paste the Project instructions again and retry once.

- [ ] **Step 8: Commit**

```bash
cd ~/TribalCowboy-Social
git add scripts/update_editor_prompt.py scripts/check_editor_prompt.py docs/cowork-project-instructions.md
git commit -m "feat: add four video types to the Yap Edits editor prompt"
```

---

### Task 2: `/schedule-reel` upgrade (TikTok, type aware caption, best hour)

**Files:**
- Modify: `.claude/commands/schedule-reel.md`

**Interfaces:**
- Consumes: `Edited/YYYY-MM-DD-slug/type.txt` (A, B, C, or D) and `transcript.txt` from Task 1.
- Produces: one appended line per run in `content/reels-log.md` with the format `YYYY-MM-DD | <folder> | <type> | <networks> | <first caption line> | <metricool id>`. Task 4 reads this log.

- [ ] **Step 1: Replace the file**

Overwrite `.claude/commands/schedule-reel.md` with:

```markdown
---
description: Take the newest finished reel from the Edited folder, write the caption in Stacie's voice, and schedule it to Instagram, Facebook and TikTok through Metricool at the best hour
---

# /schedule-reel

Closes the loop from a finished Cowork render to a scheduled post.

**Edited folder:** `~/Documents/Claude Yap Edits ready to edit/Edited/`
**Metricool blog ID:** `6106320`. Facebook Page `239951139207792`. TikTok `tribal_cowboy`. Instagram `tribalcowboy`.
**Timezone:** America/Los_Angeles.

## Steps

1. **Find the reel.** List subfolders of Edited, newest modified first, skipping `Scheduled/`. Use the newest unless `$ARGUMENTS` names one. Inside it, take the newest `*.mp4` or `*.mov` by modified time and say which file you picked and why ("draft-2.mp4, newer than draft-1.mp4"). Read `type.txt` for the type letter; if missing, ask Stacie which type it is. Read `transcript.txt`; if missing, transcribe with `whisper "<file>" --model small.en --output_format txt --output_dir /tmp/reel-caption`. Run `ffprobe` and confirm height > width and duration under 90 s; if not, stop and say so. For type C, list every `highlight-*.mp4` and ask which one to schedule.

2. **Write the caption.** Load `anthropic-skills:stacie-voice`, read `memory/brand-memory.md`. Then by type:
   - A talking: hook line that adds to the video, two to four sentences with one specific detail, CTA "Follow along for more from the ranch." or a question.
   - B voice over: first line names the horse or place on screen in the first three seconds, then two sentences, then a question that invites comments.
   - C highlight: one line under 80 characters plus a question. No CTA.
   - D trend: the hook from the brief as line one, one sentence tying it to the ranch, and for Instagram the audio name in the last line ("Sound: <name>").
   All types: 8 to 12 hashtags from the bank in `CLAUDE.md` on their own line. Run `python3 scripts/check_voice.py` on the caption text (see Task 3); fix anything it flags before showing it.

3. **Get a public URL.** Copy the file to `~/Library/CloudStorage/Dropbox-Mrs.huffhines/Tribal Cowboy Reels/` (create the folder if missing). Ask Stacie to right click it in Finder → Copy Dropbox Link and paste it. Replace `?dl=0` with `?dl=1`.

4. **Pick the time.** If `$ARGUMENTS` has a date or time, use it. Otherwise call `getBestTimeToPostByNetwork` for instagram for the last 30 days and pick the highest value hour within the next 3 days that is at least 2 hours from now. Show the hour and the value.

5. **Show the plan and stop.** Print: file, type, caption, hashtags, networks, time, cover frame (`videoCoverMilliseconds` 1500). Ask: "Schedule this? yes / change something / draft only". Do nothing until the answer.

6. **Schedule.** Call `createScheduledPost` with `blogId` "6106320", `date` in ISO 8601 with the Pacific offset, and `info`:
   - `text`: caption plus hashtags
   - `media`: [dropbox url]
   - `providers`: `[{"network":"instagram"},{"network":"facebook"},{"network":"tiktok"}]`
   - `instagramData`: `{"type":"REEL","showReelOnFeed":true}`
   - `facebookData`: `{"type":"REEL"}`
   - `tiktokData`: `{"title": <first caption line, max 90 chars>, "privacyOption":"PUBLIC_TO_EVERYONE", "disableComment":false, "disableDuet":false, "disableStitch":false, "isAigc":false}`
   - `publicationDate`: `{"dateTime":"YYYY-MM-DDTHH:mm:ss","timezone":"America/Los_Angeles"}`
   - `videoCoverMilliseconds`: 1500
   - `autoPublish`: true, `draft`: false (or `draft`: true if Stacie said draft only)
   If Stacie says to drop a network, remove it from providers and its networkData.

7. **Log and move.** Append to `content/reels-log.md`: `YYYY-MM-DD | <folder> | <type> | <networks> | <first caption line> | <metricool post id>`. Move the Edited subfolder into `Edited/Scheduled/`.

## Rules
- Never schedule without the explicit yes in step 5.
- Never invent numbers about the horses.
- Horse names spelled exactly as in `memory/brand-memory.md`.
- If the transcript is empty, ask Stacie for two sentences about the clip instead of guessing.
```

- [ ] **Step 2: Create the log file header**

Create `content/reels-log.md`:

```markdown
# Reels log

date | folder | type | networks | first line | metricool id
```

- [ ] **Step 3: Test the newest file rule**

Make a throwaway folder `Edited/2026-01-01-test/` with `type.txt` containing `A`, `transcript.txt` containing `Belle had opinions about breakfast this morning.`, and two empty files `draft-1.mp4` then (one second later) `draft-2.mp4`. Run `/schedule-reel 2026-01-01-test`. Expected: it names `draft-2.mp4` as the pick and explains why, then stops at ffprobe with "not a valid video" because the file is empty. Delete the folder.

- [ ] **Step 4: Live draft test**

With a real render from Task 1, run `/schedule-reel` and answer "draft only". Expected: `createScheduledPost` succeeds with `draft: true`; `getScheduledPosts` for that day shows the post with instagram, facebook and tiktok providers; the log line is appended; the folder moved into `Scheduled/`. Then delete the draft in Metricool's planner.

- [ ] **Step 5: Commit**

```bash
git add .claude/commands/schedule-reel.md content/reels-log.md
git commit -m "feat: schedule reels to TikTok too, type aware captions, best hour default"
```

---

### Task 3: Voice checker helper

**Files:**
- Create: `scripts/check_voice.py`
- Create: `scripts/test_check_voice.py`

**Interfaces:**
- Consumes: `memory/brand-memory.md` (the "Banned Phrases" numbered list and "The Herd" names).
- Produces: `check_voice.py` reads text from stdin or a file path argument; prints one line per problem (`banned: <phrase>`, `unknown horse: <name>`, `exclamations: <n>`); exit 1 if any problem, 0 if clean. Tasks 2, 4, 5, 6 call it.

- [ ] **Step 1: Write the failing tests**

Create `scripts/test_check_voice.py`:

```python
import subprocess, sys
from pathlib import Path
HERE = Path(__file__).parent

def run(text):
    r = subprocess.run([sys.executable, str(HERE / "check_voice.py")], input=text, capture_output=True, text=True)
    return r.returncode, r.stdout

def test_clean_text_passes():
    code, out = run("Belle had opinions about breakfast. She is 22 and has earned the right.")
    assert code == 0, out

def test_banned_phrase_flagged():
    code, out = run("Memories to last a lifetime with our herd.")
    assert code == 1 and "banned: memories to last a lifetime" in out.lower()

def test_unknown_horse_flagged():
    code, out = run("Duke pulled the wagon today.")
    assert code == 1 and "unknown horse: duke" in out.lower()

def test_two_exclamations_flagged():
    code, out = run("Big day! Belle was ready! ")
    assert code == 1 and "exclamations: 2" in out

def test_real_horse_not_flagged():
    code, out = run("Master Chief acts like he runs the mini herd.")
    assert code == 0, out
```

- [ ] **Step 2: Run tests to confirm they fail**

Run: `cd ~/TribalCowboy-Social && uv run --quiet --with pytest pytest scripts/test_check_voice.py -q`
Expected: 5 failed (check_voice.py not found).

- [ ] **Step 3: Write the checker**

Create `scripts/check_voice.py`:

```python
import re, sys
from pathlib import Path

BRAND = Path(__file__).resolve().parent.parent / "memory" / "brand-memory.md"
HERD = ["Belle", "Millie", "Abby", "Jill", "Reba", "Dolly", "Lainey", "Minimus",
        "Monster", "Master Chief", "Jolene", "Rowdy", "Nash", "Monster Unicorn"]
# names that a model tends to invent for horses
SUSPECT = ["Duke", "Thunder", "Storm", "Blaze", "Shadow", "Spirit", "Maverick", "Bandit"]

def banned_phrases():
    text = BRAND.read_text()
    block = text.split("## Banned Phrases")[1].split("## Premium Vocabulary")[0]
    phrases = []
    for line in block.splitlines():
        m = re.match(r"\d+\.\s+(.*)", line.strip())
        if not m:
            continue
        for q in re.findall(r'"([^"]+)"', m.group(1)):
            phrases.append(q.lower())
    return phrases

def main():
    text = Path(sys.argv[1]).read_text() if len(sys.argv) > 1 else sys.stdin.read()
    low = text.lower()
    problems = []
    for p in banned_phrases():
        core = p.replace("...", "").strip()
        if core and core in low:
            problems.append(f"banned: {p}")
    for name in SUSPECT:
        if re.search(rf"\b{name}\b", text) and name not in HERD:
            problems.append(f"unknown horse: {name}")
    n = text.count("!")
    if n > 1:
        problems.append(f"exclamations: {n}")
    for line in problems:
        print(line)
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd ~/TribalCowboy-Social && uv run --quiet --with pytest pytest scripts/test_check_voice.py -q`
Expected: 5 passed. If `test_banned_phrase_flagged` fails, open `memory/brand-memory.md` and confirm the banned list items are wrapped in straight double quotes; adjust the regex to also accept curly quotes `“([^”]+)”`.

- [ ] **Step 5: Commit**

```bash
git add scripts/check_voice.py scripts/test_check_voice.py
git commit -m "feat: voice checker for banned phrases, unknown horses, exclamation count"
```

---

### Task 4: `/reel-report`

**Files:**
- Create: `.claude/commands/reel-report.md`

**Interfaces:**
- Consumes: Metricool `getAnalyticsDataByMetrics` with field ids `IGRE03, IGRE06, IGRE23, IGRE11, IGRE27, IGRE24, IGRE28, IGRE12, IGRE21, IGRE07, IGRE26, IGRE02`; `content/reels-log.md` from Task 2.
- Produces: an appended dated section in `content/reels-log.md` under a `## Report YYYY-MM-DD` heading; proposed rules in the My Rules.md one line format.

- [ ] **Step 1: Write the command**

Create `.claude/commands/reel-report.md`:

```markdown
---
description: Rank the last 30 days of Tribal Cowboy reels by how well they held attention, find the patterns, and propose rules for My Rules.md
---

# /reel-report

Read only against Metricool. Proposes; never writes a rule without a yes.

**Brand id:** 6106320. **Timezone:** America/Los_Angeles.

## Steps

1. **Pull Instagram reels.** Call `getAnalyticsDataByMetrics` with `brandId` "6106320", `from` = 30 days ago at 00:00:00-07:00, `to` = now, `metrics` = ["IGRE02","IGRE03","IGRE06","IGRE23","IGRE11","IGRE27","IGRE24","IGRE28","IGRE12","IGRE21","IGRE07","IGRE26"]. If `$ARGUMENTS` contains a number of days, use that window instead. If the result has no rows, say "Metricool has no reels in this window" and stop.

2. **Pull TikTok posts if present.** Call `getAnalyticsAvailableMetrics` with network tiktok, connector posts, and take the field ids for date, content, url, views, reach, average watch time, likes, comments, shares. Call `getAnalyticsDataByMetrics` with them. If it errors, note "TikTok analytics unavailable" and continue.

3. **Rank.** For each reel compute the sort key: `reelsViewRate` (IGRE28) when it is a number, else `retention` (IGRE27) when it is a number, else views per reach. Rows with none of the three go to the bottom and are marked "no analytics yet". Sort descending. Never treat null as zero and never put nulls first.

4. **Show top and bottom.** A table of the top three and bottom three: date, first 60 characters of the caption, duration, views, 3 second hold percent, retention percent, saves, shares. Link each url.

5. **Find patterns.** Read every caption's first line and each posting hour (IGRE02). Answer in plain sentences, one per line, only where the data supports it:
   - Which horse names appear in the top half more than the bottom half.
   - Whether reels under 30 s, 30 to 60 s, or over 60 s held better.
   - Which posting hours the top half used.
   - Whether question hooks or statement hooks held better.
   If fewer than four reels exist, say "too few reels to see a pattern" and skip this step.

6. **Propose rules.** Write one or two lines in this exact shape, prefixed PROPOSED: `- YYYY-MM-DD: <rule in under 20 words>`. Example: `- 2026-10-07: open with the horse's name in the first line; those reels held 12 points better.` Ask: "Add these to My Rules.md? yes / no / edit". On yes, append them to `~/Documents/Claude Yap Edits ready to edit/Yap Edits files/My Rules.md` under "## Rules from feedback".

7. **Best hours.** Call `getBestTimeToPostByNetwork` for instagram and tiktok for the last 30 days. Print the top three hours per network for the next seven days.

8. **Log.** Append to `content/reels-log.md`:
   ```
   ## Report YYYY-MM-DD
   reels: <n> | top: <first line> (<hold>%) | bottom: <first line> (<hold>%)
   patterns: <one line>
   proposed: <rules or none>
   ```

## Rules
- Numbers come only from Metricool. If a value is missing, write "n/a".
- Run `python3 scripts/check_voice.py` on every proposed rule before showing it.
```

- [ ] **Step 2: Test the null handling by hand**

Run `/reel-report 7`. Expected: at least one row from the last week shows "no analytics yet" or a real hold percent; no row with `n/a` appears above a row with a number; the command does not crash on a null `reelsViewRate`. If Metricool has no reels in 7 days, run `/reel-report 60`.

- [ ] **Step 3: Cross check one number**

Open metricool.com → Instagram → Reels, sort by the 3 second view rate. Expected: the top reel there is the top reel in the command's table, with the same views count.

- [ ] **Step 4: Commit**

```bash
git add .claude/commands/reel-report.md
git commit -m "feat: /reel-report ranks reels by attention held and proposes rules"
```

---

### Task 5: `/trend-brief`

**Files:**
- Create: `.claude/commands/trend-brief.md`
- Create: `content/trends/hashtags.md`
- Create: `content/trends/README.md`

**Interfaces:**
- Consumes: Firecrawl `firecrawl_search`; Apify MCP (Instagram hashtag scraper `apify/instagram-hashtag-scraper`, TikTok scraper `clockworks/tiktok-scraper`); Higgsfield `tiktok_accounts` and `tiktok_music_trending`; Metricool `getBestTimeToPostByNetwork`; `scripts/check_voice.py`.
- Produces: `content/trends/YYYY-MM-DD.md` with 3 to 5 ideas in the fixed block format below. Task 6 (`/hooks`) reads the latest of these files.

- [ ] **Step 1: Create the hashtag list**

Create `content/trends/hashtags.md`:

```markdown
# Hashtags the trend brief scrapes each week
# one per line, no # sign; add your own below the line
clydesdale
minihorse
miniaturehorse
ranchlife
horsesoftiktok
horsesofinstagram
drafthorse
ponyparty
northidaho
idaho
---
```

- [ ] **Step 2: Write the command**

Create `.claude/commands/trend-brief.md`:

```markdown
---
description: Weekly brief of 3 to 5 trend ideas mapped onto the ranch, with the hook, the shot, the audio and the video type for each
---

# /trend-brief

Sources fail independently. Skip a source that errors, say so in one line, keep going.

## Steps

1. **Web trends.** Call `firecrawl_search` three times, `tbs` "qdr:w" (past week), limit 8 each:
   - `TikTok trending sounds this week` with `includeDomains` ["ads.tiktok.com","tiktok.com"]
   - `Instagram Reels trends this week creators`
   - `horse ranch TikTok trend viral this week`
   Keep results dated within 7 days. From each, note the format (POV, before and after, day in the life, storytime, tutorial, duet, text on screen with silent footage) and the sound if named.

2. **Niche scrape.** Read `content/trends/hashtags.md`. Load the Apify MCP tools (ToolSearch "apify"). For Instagram call the actor `apify/instagram-hashtag-scraper` with `hashtags` = the list, `resultsLimit` 20, `resultsType` "posts". For TikTok call `clockworks/tiktok-scraper` with `hashtags` = the list, `resultsPerPage` 20. Sort everything by views (or likes when views are missing) and keep the top 15 overall from the last 7 days. For each note: format, hook text on screen, length, sound.

3. **Trending music.** Call Higgsfield `tiktok_accounts`. If none, print once: "Link TikTok in Higgsfield to get the trending chart: use tiktok_connect" and skip. If an active account exists, call `tiktok_music_trending` with its `connector_id`, `country_code` US, `date_range` 7DAY, `genre` COUNTRY, limit 10, then again with genre ALL. Keep the titles and listen links.

4. **Best hours.** Call `getBestTimeToPostByNetwork` for instagram and tiktok, last 30 days, brandId 6106320, timezone America/Los_Angeles. Keep the top two hours per network.

5. **Write 3 to 5 ideas.** Each idea must map a format or sound from steps 1 to 3 onto something real at the ranch: a named horse, a real chore, a real event, a real place. Use `memory/brand-memory.md` for names and content angles. Format each idea exactly like this:

   ```
   ### Idea N: <six word title>
   Trend: <one sentence, cite the source>
   Ranch version: <one sentence>
   Hook (on screen, frame one): <under 8 words>
   Shot: <camera position, which horse or place, what happens, how long to film>
   Audio: <track name and link, or "your voice", or "natural sound">
   Type: <A, B, C or D>  Length: <under 30 s / 30 to 60 s / 60 to 90 s>
   Post at: <day and hour from step 4>
   ```

6. **Check.** Write all ideas to a temp file and run `python3 scripts/check_voice.py <file>`. Fix anything flagged. Every idea must name at least one horse from the herd or one real place (Athol, the paddock, the barn, the truck, a named event).

7. **Save and show.** Write `content/trends/YYYY-MM-DD.md` with a header line listing which sources worked and which were skipped, then the ideas. Print the same in chat. Ask: "Which idea do you want to film first? I will run /hooks on it."
```

- [ ] **Step 3: Create the folder README**

Create `content/trends/README.md`:

```markdown
# Trends folder
- YYYY-MM-DD.md: weekly trend briefs from /trend-brief
- niche-YYYY-MM-DD.md: weekly competitor briefs from /niche-watch
- hashtags.md: the hashtags the trend brief scrapes
- accounts.md: the 10 accounts niche watch follows
```

- [ ] **Step 4: Run it once**

Run `/trend-brief`. Expected: a file `content/trends/<today>.md` with a sources header and 3 to 5 ideas in the exact block format; every idea names a horse or place; `python3 scripts/check_voice.py content/trends/<today>.md` exits 0; if Apify failed, the header says so and the ideas still exist.

- [ ] **Step 5: Commit**

```bash
git add .claude/commands/trend-brief.md content/trends/hashtags.md content/trends/README.md
git commit -m "feat: /trend-brief maps weekly trends onto the ranch"
```

---

### Task 6: `/hooks <topic>`

**Files:**
- Create: `.claude/commands/hooks.md`
- Create: `content/hooks.md`

**Interfaces:**
- Consumes: latest `content/trends/*.md` (Task 5), the latest `## Report` section in `content/reels-log.md` (Task 4), `scripts/check_voice.py`.
- Produces: appended entries in `content/hooks.md` in the format `- YYYY-MM-DD | <topic> | <hook> | score <n>/20`.

- [ ] **Step 1: Write the command**

Create `.claude/commands/hooks.md`:

```markdown
---
description: Write five hooks for a topic in Stacie's voice, score them against the reel report and the trend brief, recommend two
---

# /hooks $ARGUMENTS

If `$ARGUMENTS` is empty, ask "What is the reel about?" and stop.

## Steps

1. Load `anthropic-skills:stacie-voice`. Read `memory/brand-memory.md` (tone rules, herd, content angles). Read the newest file in `content/trends/` that does not start with `niche-`, and the newest `## Report` section in `content/reels-log.md`. If either is missing, say so and score without it.

2. Write five hooks for the topic. Each under 8 words, on screen text style, no hashtags, no emoji. At least two must name a horse or a number. Mix: one question, one bold claim, one "POV" or scene setter, one number, one contrast.

3. Score each hook 1 to 5 on four things and sum to 20:
   - Report match: uses a pattern the report said held (horse name first, question vs statement, length).
   - Trend match: fits a format in the latest trend brief.
   - Specific: names a horse, number, place, or moment.
   - Short: 5 = under 6 words, 3 = 6 to 8, 1 = over 8.

4. Run `python3 scripts/check_voice.py` on all five. Rewrite any flagged hook before scoring it.

5. Show a table: hook, four scores, total. Recommend the top two and say in one line each why. Ask: "Save these two to content/hooks.md? yes / no".

6. On yes, append: `- YYYY-MM-DD | <topic> | <hook> | score <n>/20` for each of the two.
```

- [ ] **Step 2: Create the hooks file**

Create `content/hooks.md`:

```markdown
# Hooks bank
# date | topic | hook | score
```

- [ ] **Step 3: Run it**

Run `/hooks Belle turning 22 and still working`. Expected: five hooks, all under 8 words, at least two with "Belle" or "22", a scored table, two recommendations, and on yes two lines in `content/hooks.md`.

- [ ] **Step 4: Commit**

```bash
git add .claude/commands/hooks.md content/hooks.md
git commit -m "feat: /hooks writes and scores five hooks per topic"
```

---

### Task 7: `/niche-watch`

**Files:**
- Create: `.claude/commands/niche-watch.md`
- Create: `content/trends/accounts.md`

**Interfaces:**
- Consumes: Apify `apify/instagram-profile-scraper` and `clockworks/tiktok-profile-scraper`; `scripts/check_voice.py`.
- Produces: `content/trends/niche-YYYY-MM-DD.md` with a "## Formats to steal this week" section in the same idea block format as Task 5 so `/hooks` can read it the same way.

- [ ] **Step 1: Create the accounts template**

Create `content/trends/accounts.md`:

```markdown
# Accounts niche watch follows
# one per line as platform:handle, no @ sign; fill in up to 10
# examples of the shape:
# instagram:budweiserclydesdales
# tiktok:someranchaccount
```

- [ ] **Step 2: Write the command**

Create `.claude/commands/niche-watch.md`:

```markdown
---
description: Weekly scrape of up to 10 equine and ranch accounts, rank their top posts, reverse engineer the formats into briefs Stacie can film
---

# /niche-watch

## Steps

1. Read `content/trends/accounts.md`. Ignore lines starting with `#`. If no accounts remain, ask Stacie: "Give me up to 10 handles as platform:handle (instagram:name or tiktok:name)." Write her answer into the file and continue.

2. Load the Apify MCP tools. For each instagram handle call `apify/instagram-profile-scraper` with `usernames` [handle], `resultsLimit` 30. For each tiktok handle call `clockworks/tiktok-profile-scraper` with `profiles` [handle], `resultsPerPage` 30. Keep posts from the last 30 days. If an actor fails for a handle, note it and continue.

3. Rank all posts by views, falling back to likes. Take the top 10. For each write one line: account, date, format (POV, before and after, day in the life, storytime, tutorial, text on silent footage, talking, voice over, highlight), hook on screen, length, sound, views.

4. Write "## Formats to steal this week": 3 briefs in the exact idea block from /trend-brief (Idea N, Trend, Ranch version, Hook, Shot, Audio, Type, Length, Post at). "Trend:" cites the account and post. Every brief names a horse from the herd or a real place.

5. Run `python3 scripts/check_voice.py` on the file. Fix anything flagged.

6. Save `content/trends/niche-YYYY-MM-DD.md`: a header with the accounts scraped and any that failed, the top 10 table, the three briefs. Print the briefs in chat.
```

- [ ] **Step 3: Run it**

Fill `accounts.md` with three real handles (ask Stacie). Run `/niche-watch`. Expected: `content/trends/niche-<today>.md` with a top 10 table and three briefs; `check_voice.py` exits 0 on it.

- [ ] **Step 4: Commit**

```bash
git add .claude/commands/niche-watch.md content/trends/accounts.md
git commit -m "feat: /niche-watch turns competitor top posts into filmable briefs"
```

---

### Task 8: The visual guide PDF

**Files:**
- Create: `scripts/build_reel_guide.py`
- Create: `scripts/reel_guide_pages.py` (page copy and checklists only, no layout)
- Output: `~/Documents/Claude Yap Edits ready to edit/Yap Edits files/How to make a reel.pdf`

**Interfaces:**
- Consumes: the logo from the tribal cowboy brand skill (already extracted at build time by the script), the folder and command names from Tasks 1, 2, 4, 5.
- Produces: a 7 page PDF (map page + six stage pages).

- [ ] **Step 1: Write the page content module**

Create `scripts/reel_guide_pages.py`:

```python
# Copy for each page. Short sentences. No paragraphs over two sentences.
PAGES = [
    dict(
        num="1", title="Film", one="Point the phone at the ranch and talk.",
        checklist=["Lens wiped, phone at eye level", "A hand of space above your head", "Say the hook first, keep rolling through mistakes"],
        say="Nothing yet. Just film.",
        picture="film",
    ),
    dict(
        num="2", title="Drop", one="Move the clip into the Yap Edits folder.",
        checklist=["AirDrop the clip to this Mac", "Talking reel: main folder", "Voice over: a new subfolder with clips and your voice memo"],
        say="Nothing yet. Just drop.",
        picture="folder",
    ),
    dict(
        num="3", title="Ask and edit", one="Open the Claude app, send the message, answer three questions.",
        checklist=["Project: Yap Edits Reel Editor", "Cowork switched on", "Answer: type, length, setting"],
        say='Please request access to my folder called "Claude Yap Edits ready to edit" in Documents. Look at what is new in it, ask me the three questions, then edit using my Yap Edits Editor Prompt, the Playbook, and My Rules.md. Save the draft to the Edited subfolder.',
        picture="claude",
    ),
    dict(
        num="4", title="Review", one="Watch the draft twice. Once with sound, once muted.",
        checklist=["Captions clear of your mouth", "Nothing cut off at the edges", "Ends on the Follow click"],
        say="Move the captions a little left and use fewer zooms. Give me that as a rule for My Rules.md.",
        picture="review",
    ),
    dict(
        num="5", title="Schedule", one="Open Claude Code in TribalCowboy Social and run one command.",
        checklist=["Type /schedule-reel", "Paste the Dropbox link when asked", "Say yes to the plan"],
        say="/schedule-reel",
        picture="schedule",
    ),
    dict(
        num="6", title="Weekly", one="Two commands on Monday. Ten minutes.",
        checklist=["/reel-report shows what held attention", "/trend-brief gives you 3 to 5 things to film", "/hooks before a talking reel"],
        say="/reel-report   then   /trend-brief",
        picture="weekly",
    ),
]
LOOP = ["Film", "Drop", "Ask and edit", "Review", "Schedule", "Report", "Next idea"]
```

- [ ] **Step 2: Write the generator with SVG illustrations**

Create `scripts/build_reel_guide.py`:

```python
import base64, re, subprocess, sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from reel_guide_pages import PAGES, LOOP

OUT_DIR = Path.home() / "Documents/Claude Yap Edits ready to edit/Yap Edits files"
OUT = OUT_DIR / "How to make a reel.pdf"
TMP = Path("/tmp/reel-guide"); TMP.mkdir(exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def logo_b64():
    skill = next(Path.home().glob(".claude/skills/synced/*/tribal-cowboy-brand/SKILL.md"))
    m = re.search(r'TRIBAL_COWBOY_LOGO_B64 = "([^"]+)"', skill.read_text())
    return m.group(1)

# ---------- SVG pictures: simplified drawings of the real screens ----------
GOLD, CREAM, TIMBER, TEAL, LEATHER, MUTED = "#D4A843", "#F3EDE3", "#2C2520", "#1A7A6B", "#C8A96E", "#8A7560"

def svg(inner, w=520, h=300):
    return f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Montserrat, sans-serif">{inner}</svg>'

def window(x, y, w, h, title):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#FFFCF7" stroke="#E0D6C8"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="8" fill="#EDE5D8"/>'
            f'<circle cx="{x+14}" cy="{y+13}" r="4" fill="#E06B5B"/><circle cx="{x+28}" cy="{y+13}" r="4" fill="#E9B94E"/><circle cx="{x+42}" cy="{y+13}" r="4" fill="#6CC070"/>'
            f'<text x="{x+w/2}" y="{y+17}" font-size="10" fill="{MUTED}" text-anchor="middle">{title}</text>')

def pic_film():
    return svg(
        f'<rect x="200" y="30" width="120" height="240" rx="18" fill="{TIMBER}"/>'
        f'<rect x="210" y="45" width="100" height="210" rx="8" fill="#5A4A3A"/>'
        f'<circle cx="260" cy="120" r="26" fill="{LEATHER}"/><path d="M225 200 Q260 150 295 200 Z" fill="{LEATHER}"/>'
        f'<line x1="260" y1="60" x2="260" y2="88" stroke="{GOLD}" stroke-width="3" stroke-dasharray="4 3"/>'
        f'<text x="335" y="76" font-size="12" fill="{TIMBER}">a hand of space above your head</text>'
        f'<text x="40" y="150" font-size="12" fill="{TIMBER}">window or open sky</text><text x="40" y="168" font-size="12" fill="{TIMBER}">on this side of you</text>'
        f'<path d="M150 155 L195 140" stroke="{GOLD}" stroke-width="3" fill="none"/><path d="M185 133 L197 139 L188 147" stroke="{GOLD}" stroke-width="3" fill="none"/>'
        f'<text x="335" y="230" font-size="12" fill="{TIMBER}">say the hook first</text><text x="335" y="248" font-size="12" fill="{TIMBER}">keep rolling if you mess up</text>')

def pic_folder():
    rows = [("Assets", True), ("Edited", True), ("Yap Edits files", True), ("IMG_8795.mov  ← talking reel", False), ("belle-birthday  ← voice over subfolder", True)]
    items = "".join(
        f'<rect x="70" y="{70+i*36}" width="26" height="20" rx="3" fill="{"#7FB3D5" if f else "#BFB3A3"}"/>'
        f'<text x="108" y="{85+i*36}" font-size="13" fill="{TIMBER}">{t}</text>' for i, (t, f) in enumerate(rows))
    return svg(window(40, 20, 440, 260, "Claude Yap Edits ready to edit") + items +
               f'<text x="300" y="258" font-size="11" fill="{TEAL}">inside belle-birthday: 5 clips + voice.m4a</text>')

def pic_claude():
    return svg(window(30, 15, 460, 270, "Claude · Yap Edits Reel Editor") +
        f'<rect x="60" y="60" width="400" height="70" rx="10" fill="#F6F1EA" stroke="#E0D6C8"/>'
        f'<text x="75" y="85" font-size="11" fill="{TIMBER}">Please request access to my folder called</text>'
        f'<text x="75" y="102" font-size="11" fill="{TIMBER}">"Claude Yap Edits ready to edit" in Documents...</text>'
        f'<rect x="60" y="145" width="400" height="80" rx="10" fill="#EEF7F5" stroke="{TEAL}"/>'
        f'<text x="75" y="168" font-size="11" fill="{TEAL}">I found IMG_8795.mov (48 s). Three questions:</text>'
        f'<text x="75" y="186" font-size="11" fill="{TIMBER}">Which type: A talking, B voice over, C highlight, D trend?</text>'
        f'<text x="75" y="202" font-size="11" fill="{TIMBER}">How long: under 30 s, 30 to 60 s, 60 to 90 s?  Setting?</text>'
        f'<rect x="60" y="238" width="60" height="22" rx="11" fill="#E8E1D6"/><text x="90" y="253" font-size="10" text-anchor="middle" fill="{MUTED}">Chat</text>'
        f'<rect x="124" y="238" width="70" height="22" rx="11" fill="{TEAL}"/><text x="159" y="253" font-size="10" text-anchor="middle" fill="#fff">Cowork ✓</text>'
        f'<text x="210" y="253" font-size="11" fill="{TIMBER}">you type:  A, under 30 s, outdoor</text>')

def pic_review():
    return svg(
        f'<rect x="60" y="20" width="130" height="260" rx="14" fill="{TIMBER}"/>'
        f'<rect x="72" y="60" width="106" height="20" rx="4" fill="{CREAM}"/><text x="125" y="74" font-size="9" text-anchor="middle" fill="{TIMBER}">Belle at 22</text>'
        f'<circle cx="125" cy="130" r="22" fill="{LEATHER}"/><path d="M95 200 Q125 160 155 200 Z" fill="{LEATHER}"/>'
        f'<rect x="80" y="175" width="34" height="12" rx="2" fill="#fff"/><text x="97" y="184" font-size="8" text-anchor="middle" fill="{TIMBER}">still</text>'
        f'<rect x="90" y="240" width="70" height="20" rx="10" fill="{GOLD}"/><text x="125" y="254" font-size="9" text-anchor="middle" fill="#1E1208">Follow along</text>'
        f'<text x="220" y="70" font-size="13" fill="{TIMBER}">Watch it twice</text>'
        f'<text x="220" y="92" font-size="12" fill="{MUTED}">1. with sound   2. muted</text>'
        f'<text x="220" y="130" font-size="13" fill="{TIMBER}">Tell Claude what to change, like a friend</text>'
        f'<text x="220" y="152" font-size="12" fill="{MUTED}">"captions a little left"  "fewer zooms"</text>'
        f'<text x="220" y="190" font-size="13" fill="{TIMBER}">Keep the good changes</text>'
        f'<text x="220" y="212" font-size="12" fill="{MUTED}">paste the rule into My Rules.md</text>')

def pic_schedule():
    return svg(window(30, 15, 460, 270, "Terminal · Claude Code · TribalCowboy Social") +
        f'<text x="55" y="60" font-size="12" fill="{TEAL}" font-family="Menlo, monospace">&gt; /schedule-reel</text>'
        f'<text x="55" y="88" font-size="11" fill="{TIMBER}">Picked Edited/2026-10-03-belle-at-22/render.mp4 (type A)</text>'
        f'<text x="55" y="108" font-size="11" fill="{TIMBER}">Caption: Belle had opinions about breakfast this morning...</text>'
        f'<text x="55" y="128" font-size="11" fill="{TIMBER}">Copied to Dropbox. Paste the Dropbox link:</text>'
        f'<text x="55" y="156" font-size="11" fill="{TIMBER}">Best hour: Saturday 6 pm (Instagram)   Networks: IG, FB, TikTok</text>'
        f'<rect x="55" y="180" width="410" height="60" rx="8" fill="#FAF4EA" stroke="{GOLD}"/>'
        f'<text x="70" y="203" font-size="12" fill="{TIMBER}">Schedule this?  yes / change something / draft only</text>'
        f'<text x="70" y="226" font-size="12" fill="{TEAL}" font-family="Menlo, monospace">&gt; yes</text>')

def pic_weekly():
    cx, cy, r = 260, 150, 105
    n = len(LOOP)
    dots = ""
    for i, label in enumerate(LOOP):
        a = -math.pi/2 + 2*math.pi*i/n
        x, y = cx + r*math.cos(a), cy + r*math.sin(a)
        dots += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="17" fill="{GOLD}"/><text x="{x:.0f}" y="{y+4:.0f}" font-size="10" text-anchor="middle" fill="#1E1208" font-weight="700">{i+1}</text>'
        lx, ly = cx + (r+40)*math.cos(a), cy + (r+40)*math.sin(a)
        anchor = "middle" if abs(math.cos(a)) < 0.3 else ("start" if math.cos(a) > 0 else "end")
        dots += f'<text x="{lx:.0f}" y="{ly+4:.0f}" font-size="12" text-anchor="{anchor}" fill="{TIMBER}">{label}</text>'
    return svg(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LEATHER}" stroke-width="3" stroke-dasharray="6 6"/>' + dots)

PICS = dict(film=pic_film, folder=pic_folder, claude=pic_claude, review=pic_review, schedule=pic_schedule, weekly=pic_weekly)

# ---------- HTML ----------
CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Montserrat:wght@400;500;600;700&display=swap');
@page {{ size: 8.5in 11in; margin: 0; }}
* {{ box-sizing: border-box; }} html, body {{ margin:0; background:{CREAM}; }}
body {{ font-family:'Montserrat',sans-serif; color:#574838; font-size:11.5pt; line-height:1.75; }}
.page {{ width:8.5in; height:11in; position:relative; overflow:hidden; page-break-after:always; }}
.page:last-child {{ page-break-after:auto; }}
.header {{ background:{TIMBER}; height:0.7in; display:flex; align-items:center; justify-content:space-between; padding:0 0.6in; }}
.header img {{ height:0.55in; width:0.55in; object-fit:contain; background:#fff; border-radius:4px; }}
.header .label {{ color:{GOLD}; font-weight:700; font-size:9pt; letter-spacing:0.18em; text-transform:uppercase; }}
.body {{ padding:0.45in 0.7in 0; }}
.num {{ width:0.9in; height:0.9in; border-radius:50%; background:{GOLD}; color:#1E1208; font-weight:700; font-size:34pt; display:flex; align-items:center; justify-content:center; float:left; margin:0 0.3in 0.2in 0; }}
h1 {{ font-family:'Cormorant Garamond',serif; font-weight:500; font-size:34pt; color:{TIMBER}; margin:0.05in 0 0 0; line-height:1.05; }}
.one {{ font-family:'Cormorant Garamond',serif; font-size:17pt; color:{MUTED}; margin:0 0 0.25in 0; clear:none; }}
.pic {{ clear:both; background:#FFFCF7; border:0.5px solid #E8DFD0; border-radius:4px; box-shadow:0 4px 14px rgba(0,0,0,0.10); padding:0.15in; margin:0.1in 0 0.3in 0; }}
.checks {{ list-style:none; margin:0 0 0.25in 0; padding:0; }}
.checks li {{ position:relative; padding:0.06in 0 0.06in 0.45in; font-size:13pt; color:{TIMBER}; font-weight:500; }}
.checks li:before {{ content:''; position:absolute; left:0; top:0.13in; width:0.22in; height:0.22in; border:2px solid {GOLD}; border-radius:4px; }}
.say {{ border-left:4px solid {TEAL}; background:#EEF7F5; padding:0.15in 0.22in; font-size:11pt; color:{TIMBER}; }}
.say .lab {{ display:block; color:{TEAL}; font-weight:700; font-size:8pt; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:4px; }}
.map h1 {{ text-align:center; margin-top:0.2in; }}
.map .one {{ text-align:center; }}
.map .pic {{ margin-top:0.2in; }}
.map .legend {{ display:grid; grid-template-columns:1fr 1fr; gap:0.08in 0.4in; margin-top:0.25in; font-size:12pt; color:{TIMBER}; }}
.map .legend b {{ color:{GOLD}; font-weight:700; margin-right:6px; }}
.footer {{ position:absolute; bottom:0.3in; left:0.7in; right:0.7in; border-top:1px solid #E0D6C8; padding-top:8px; display:flex; justify-content:space-between; font-size:8.5pt; color:{MUTED}; font-weight:500; }}
"""

def page_html(logo, p):
    return f"""<div class="page"><div class="header"><img src="data:image/jpeg;base64,{logo}"><div class="label">How to make a reel · step {p['num']} of 6</div></div>
<div class="body"><div class="num">{p['num']}</div><h1>{p['title']}</h1><div class="one">{p['one']}</div>
<div class="pic">{PICS[p['picture']]()}</div>
<ul class="checks">{''.join(f'<li>{c}</li>' for c in p['checklist'])}</ul>
<div class="say"><span class="lab">What you say to Claude</span>{p['say']}</div></div>
<div class="footer"><span>www.tribalcowboy.com</span><span>From the Ranch · Yap Edits × Tribal Cowboy</span><span>info@tribalcowboy.com</span></div></div>"""

def map_html(logo):
    legend = "".join(f'<div><b>{i+1}</b>{l}</div>' for i, l in enumerate(LOOP))
    return f"""<div class="page map"><div class="header"><img src="data:image/jpeg;base64,{logo}"><div class="label">How to make a reel · the loop</div></div>
<div class="body"><h1>One loop. Seven stops.</h1><div class="one">Film it, drop it, answer three questions, watch it, say yes. Monday tells you what to film next.</div>
<div class="pic">{pic_weekly()}</div><div class="legend">{legend}</div></div>
<div class="footer"><span>www.tribalcowboy.com</span><span>From the Ranch · Yap Edits × Tribal Cowboy</span><span>info@tribalcowboy.com</span></div></div>"""

def build():
    logo = logo_b64()
    html = f"<!doctype html><html><head><meta charset='utf-8'><title>How to make a reel</title><style>{CSS}</style></head><body>" + map_html(logo) + "".join(page_html(logo, p) for p in PAGES) + "</body></html>"
    (TMP / "guide.html").write_text(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={TMP/'guide.pdf'}", f"file://{TMP/'guide.html'}"], check=True, capture_output=True)
    info = subprocess.run(["pdfinfo", str(TMP / "guide.pdf")], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    if pages != 7:
        raise SystemExit(f"expected 7 pages, got {pages}; a page overflowed")
    OUT.write_bytes((TMP / "guide.pdf").read_bytes())
    subprocess.run(["pdftoppm", "-jpeg", "-r", "70", str(OUT), str(TMP / "preview")], check=True)
    print("built", OUT, "previews in", TMP)

if __name__ == "__main__":
    build()
```

- [ ] **Step 3: Run the generator**

Run: `cd ~/TribalCowboy-Social && python3 scripts/build_reel_guide.py`
Expected: `built .../How to make a reel.pdf previews in /tmp/reel-guide` and seven `preview-N.jpg` files.

- [ ] **Step 4: Visual QA**

Open each `/tmp/reel-guide/preview-*.jpg`. Check: step number circle and title on one line; picture fits inside its card; three checkboxes; the "what you say" box fully above the footer; nothing overlapping; the map page's seven labels do not collide with the circle. Fix copy or CSS and rebuild until all seven pass.

- [ ] **Step 5: Overflow guard test**

Temporarily add a fourth checklist line of 200 characters to page 3 in `reel_guide_pages.py`, rebuild. Expected: the script exits with `expected 7 pages, got 8`. Remove the line and rebuild to 7 pages.

- [ ] **Step 6: Hand it over**

Open the PDF. Ask Stacie to do one loop with the guide beside her and note every place she had to ask a question. Fold each into the page copy and rebuild.

- [ ] **Step 7: Commit**

```bash
git add scripts/build_reel_guide.py scripts/reel_guide_pages.py
git commit -m "feat: visual how to make a reel guide, seven pages"
```

---

### Task 9: Memory and README updates

**Files:**
- Modify: `~/.claude/agent-memory/adspirer-ads-agent-performance-marketing-agent/project_yap_edits_setup.md`
- Modify: `README.md` in the project (add a "Reels" section)

- [ ] **Step 1: Update the memory note**

Append to `project_yap_edits_setup.md` body:

```
Reel System v2 (2026-10): four video types (A talking, B voice over, C highlight, D trend) in Editor Prompt section 10; Cowork asks type, length, setting first. Commands in TribalCowboy Social: /schedule-reel (IG, FB, TikTok, best hour), /reel-report (Metricool ranking, proposes rules), /trend-brief (weekly ideas), /hooks <topic>, /niche-watch (accounts in content/trends/accounts.md). Voice checker: scripts/check_voice.py. Guide: "How to make a reel.pdf" in Yap Edits files. AI voice deferred until Stacie approves a clone.
```

- [ ] **Step 2: Add the README section**

Append to `README.md`:

```markdown
## Reels
Editing happens in the Claude desktop app (Cowork) from `~/Documents/Claude Yap Edits ready to edit/`.
Commands here: `/schedule-reel`, `/reel-report`, `/trend-brief`, `/hooks <topic>`, `/niche-watch`.
Guide: `Yap Edits files/How to make a reel.pdf`. Spec: `docs/superpowers/specs/2026-09-30-reel-system-v2-design.md`.
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: reels section in README"
```
