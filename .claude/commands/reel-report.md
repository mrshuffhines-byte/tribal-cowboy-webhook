---
description: Rank the last 30 days of Tribal Cowboy reels by how well they held attention, find the patterns, and propose rules for My Rules.md
---

# /reel-report

Read only against Metricool. Proposes; never writes a rule without a yes.

**Brand id:** 6106320. **Timezone:** America/Los_Angeles.

## Steps

1. **Pull Instagram reels.** Call `getAnalyticsDataByMetrics` with `brandId` "6106320", `from` = 30 days ago at 00:00:00 with the Pacific offset that applies on that date (-07:00 in daylight time, -08:00 otherwise), `to` = now, `metrics` = ["IGRE02","IGRE03","IGRE06","IGRE23","IGRE11","IGRE27","IGRE24","IGRE28","IGRE12","IGRE21","IGRE07","IGRE26"]. Values arrive as strings; parse numeric strings as numbers. Only null or empty counts as missing. IGRE02 arrives as a 14 digit string like `20260923223140` (YYYYMMDDHHMMSS, UTC). Convert every timestamp to America/Los_Angeles before you show a date or read a posting hour: subtract 7 hours from the second Sunday in March to the first Sunday in November, 8 hours otherwise. If `$ARGUMENTS` contains a number of days, use that window instead. If the result has no rows, say "Metricool has no reels in this window" and stop.

2. **Pull TikTok posts if present.** Call `getAnalyticsAvailableMetrics` with network tiktok, connector posts, and take the field ids for date, content, url, views, reach, average watch time, likes, comments, shares. Call `getAnalyticsDataByMetrics` with them. If it errors, note "TikTok analytics unavailable" and continue.

3. **Rank in tiers. Never compare across tiers.** Tier 1: rows with a `reelsViewRate` (IGRE28) value, sorted by it descending. Tier 2: rows with no `reelsViewRate` but a `retention` (IGRE27) value, sorted by retention descending. Tier 3: rows with neither but with views and reach above 0, sorted by views divided by reach and marked "partial". Tier 4: everything else, marked "no analytics yet". Tiers stack in that order. Never treat a missing value as zero and never let a missing value sort above a present one. If reach is null or 0, or views is missing, the row cannot be in tier 3.

4. **Show top and bottom.** A table of the top three and bottom three: date shown as `Sep 23` (no hyphens), first 60 characters of the caption, duration (IGRE26), views (IGRE23), 3 second hold (IGRE28), retention (IGRE27), saves (IGRE12), shares (IGRE21). Missing values print as `n/a` with no percent sign. With fewer than 6 reels, show each reel once and shorten the bottom list. Link each url.

5. **Find patterns.** Use tier 1 and tier 2 rows only. Skip any row that is missing the field a pattern needs (duration for the length buckets, IGRE02 for hours). Read every remaining caption's first line and each posting hour (IGRE02, converted to Pacific as in step 1). Answer in plain sentences, one per line, only where the data supports it:
   - Which horse names appear in the top half more than the bottom half.
   - Whether reels under 30 s, 30 to 60 s, or over 60 s held better.
   - Which posting hours the top half used.
   - Whether question hooks or statement hooks held better.
   If fewer than four reels exist, say "too few reels to see a pattern" and skip this step.

6. **Propose rules.** Write one or two lines in this exact shape (show them in chat behind the word PROPOSED, which is display only and is never written to the file): `- YYYY-MM-DD: <rule in under 20 words>`. Example: `- 2026-10-07: open with the horse's name in the first line; those reels held 12 points better.` Ask: "Add these to My Rules.md? yes / no / edit". On yes, append them to `~/Documents/Claude Yap Edits ready to edit/Yap Edits files/My Rules.md` under "## Rules from feedback". Before showing them, write the rule lines to a temp file and run `python3 scripts/check_voice.py /tmp/rules.txt`. Exit 1: rewrite the flagged rule and check again. Exit 2: show no rules, tell Stacie the checker failed and what it printed. If Stacie says edit, check the edited rule the same way and ask again.

7. **Best hours.** Call `getBestTimeToPostByNetwork` for instagram and tiktok with brandId "6106320", timezone America/Los_Angeles, `fromDate` = now and `toDate` = now plus 7 days, both ISO 8601 with the Pacific offset. The result comes back by `dayOfWeek` and hour. Convert each dayOfWeek to the real date it falls on inside that window, confirming what 1 means against one known post from `getScheduledPosts` if any exists; if none exists, keep the raw number beside the date. If a call errors or returns nothing, print "best hours unavailable for <network>" and continue. Print the top three slots per network as full dates in Pacific time, like `Sat Oct 3, 6 PM`, with `(dayOfWeek 6, unconfirmed)` appended when the mapping is unconfirmed.

8. **Log.** Append to `content/reels-log.md`:
   ```
   ## Report YYYY-MM-DD
   reels: <n> | top: <first line> (<hold>%) | bottom: <first line> (<hold>%)
   patterns: <one line>
   proposed: <rules or none>
   ```

## Rules
- Numbers come only from Metricool. If a value is missing, write "n/a".
- Every proposed rule passes `scripts/check_voice.py` in step 6 before Stacie sees it.
