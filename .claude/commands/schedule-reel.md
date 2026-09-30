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
