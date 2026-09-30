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
