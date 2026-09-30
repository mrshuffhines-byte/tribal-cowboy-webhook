---
description: Weekly scrape of up to 10 equine and ranch accounts, rank their top posts, reverse engineer the formats into briefs Stacie can film
---

# /niche-watch

## Steps

1. Read `content/trends/accounts.md`. Ignore lines starting with `#`. If no accounts remain, ask Stacie: "Give me up to 10 handles as platform:handle (instagram:name or tiktok:name)." Write her answer into the file and continue.

2. Load the Apify MCP tools. For each instagram handle call `apify/instagram-profile-scraper` with `usernames` [handle], `resultsLimit` 30. For each tiktok handle call `clockworks/tiktok-profile-scraper` with `profiles` [handle], `resultsPerPage` 30. Keep posts from the last 30 days. If an actor fails for a handle, note it and continue.

3. Rank all posts by views, falling back to likes. Take the top 10. For each write one line: account, date, format (POV, before and after, day in the life, storytime, tutorial, text on silent footage, talking, voice over, highlight), hook on screen, length, sound, views.

4. Write "## Formats to steal this week": 3 briefs in the exact idea block from /trend-brief (Idea N, Trend, Ranch version, Hook, Shot, Audio, Type, Length, Post at). "Trend:" cites the account and post. Every brief names a horse from the herd or a real place.

5. Run `python3 scripts/check_voice.py <file>`. Exit 1 lists problems: fix the flagged lines and run it again until it exits 0. Exit 2 means the checker itself failed: say so, show what it printed, and stop.

6. Save `content/trends/niche-YYYY-MM-DD.md`: a header with the accounts scraped and any that failed, the top 10 table, the three briefs. Print the briefs in chat.
