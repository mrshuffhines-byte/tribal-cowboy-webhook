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
   - Short: 5 = 5 words or fewer, 3 = 6 to 7 words, 1 = 8 or more (a hook of 8 or more words breaks the step 2 limit and must be rewritten).

   With no report section in `content/reels-log.md`, give every hook 3 for report match and say in the output that the score carries no report signal. Do the same for trend match when there is no trend brief.

4. Write the five hooks one per line to a scratch file and run `python3 scripts/check_voice.py <file>`. Exit 0 means clean. Exit 1 lists problems: rewrite the flagged hooks, recheck the step 2 rules (word limit, mix, horse or number), and run the checker again until it exits 0. Exit 2 means the checker itself failed: say so, show what it printed, and stop without scoring.

5. Show a table: hook, four scores, total. Recommend the top two. Break ties by the higher Specific score, then by fewer words. Say in one line each why. Ask: "Save these two to content/hooks.md? yes / no".

6. On yes, append one line per recommended hook: `- YYYY-MM-DD | <topic> | <hook> | score <n>/20`, with today's date. On no, write nothing.
