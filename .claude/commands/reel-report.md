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
