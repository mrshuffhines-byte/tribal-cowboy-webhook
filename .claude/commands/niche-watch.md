---
description: Weekly scrape of up to 10 equine and ranch accounts, rank their top posts, reverse engineer the formats into briefs Stacie can film
---

# /niche-watch

## Steps

1. Read `content/trends/accounts.md`. Ignore comment lines, which are lines where `#` is followed by a space. If no accounts remain, ask Stacie: "Give me up to 10 handles as platform:handle (instagram:name or tiktok:name)." Write her answer into the file as one `platform:handle` per line, lowercase, with any leading `@` or `#` removed, keeping the existing comment lines. If the file holds more than 10, use the first 10 and say so.

2. Load the Apify MCP tools with ToolSearch "apify". If no Apify tools load, say "Apify is not connected in this session" and stop. For each instagram handle call `apify/instagram-profile-scraper` with `usernames` [handle], `resultsLimit` 30. For each tiktok handle call `clockworks/tiktok-profile-scraper` with `profiles` [handle], `resultsPerPage` 30. Keep posts from the last 30 days. If an actor fails for a handle, note it and continue. If every handle fails, say so and stop.

3. Rank all posts by views. A post with no views count is ranked by likes and its views column reads "likes: <n>". Skip posts with neither. Take the top 10, or all of them if fewer than 10 survive, and say how many. Write a markdown table with these columns: account, date (as `Sep 23`), format (POV, before and after, day in the life, storytime, tutorial, text on silent footage, talking, voice over, highlight), hook on screen, length, sound, views.

4. Best hours: call `getBestTimeToPostByNetwork` for instagram and tiktok, last 30 days, brandId 6106320, timezone America/Los_Angeles. Keep the top two hours per network. Metricool returns `dayOfWeek` as a number. Confirm what 1 means by comparing one known scheduled post from `getScheduledPosts` with its dayOfWeek before naming days. If nothing is scheduled to compare, print the raw number beside the day name in every Post at line and say in the header that the mapping is unconfirmed. If the call fails, write "Post at: your best hour" and say so in the header.

5. Write "## Formats to steal this week": 3 briefs. Each maps a format from the top 10 onto something real at the ranch: a horse from the herd (Belle, Millie, Abby, Jill, Reba, Dolly, Lainey, Minimus, Monster, Master Chief, Jolene, Rowdy, Nash; details in `memory/brand-memory.md`) or a real place (Athol, the paddock, the barn, the truck, a named event). Format each brief exactly like this:

   ```
   ### Idea N: <six word title>
   Trend: <one sentence, cite the account and the post>
   Ranch version: <one sentence>
   Hook (on screen, frame one): <under 8 words>
   Shot: <camera position, which horse or place, what happens, how long to film>
   Audio: <the post's sound if it fits, or "your voice", or "natural sound">
   Type: <A, B, C or D>  Length: <under 30 s / 30 to 60 s / 60 to 90 s>
   Post at: <day and hour from step 4; add (dayOfWeek N) after the day when the mapping is unconfirmed>
   ```

   Type letters: A is one clip of Stacie talking to camera. B is voice over: 3 to 10 clips plus a voice memo. C is a highlight cut: one existing clip over 60 seconds mined for short moments. D is a trend remix: footage filmed on purpose for this idea, edited to the trend's length and beats, audio added at posting. Footage filmed for a brief is D even when it runs on natural sound. Use C only when the idea is to mine a long clip Stacie already has.

6. Write the file `content/trends/niche-YYYY-MM-DD.md`: a header with the accounts scraped and any that failed (and the best hours note from step 4), the table from step 3, and the three briefs from step 5.

7. Run `python3 scripts/check_voice.py content/trends/niche-YYYY-MM-DD.md`. Exit 1 lists problems: fix the flagged lines in the file and run it again until it exits 0. Exit 2 means the checker itself failed: say so, show what it printed, and stop.

8. Print the three briefs in chat and ask: "Which idea do you want to film first? I will run /hooks on it."
