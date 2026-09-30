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
