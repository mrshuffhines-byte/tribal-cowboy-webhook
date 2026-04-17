# Campaign Stress Test — March 2026
## "Spring Booking Open — Mother's Day Pony Parties"

**Campaign:** Fill Mother's Day weekend (May 10–11) pony party bookings
**Timeline:** March 22 – May 9, 2026
**Platforms:** Instagram, Facebook, TikTok (@Tribal_Cowboy), Website
**Budget:** $0 paid media
**Key assets:** Reba, Dolly, and Lainey — the 2023 mini mares
**Test date:** March 22, 2026
**Tester:** Full system simulation, all 12 agents in order

---

## HOW THIS TEST WORKS

Each agent below received the campaign brief and was evaluated on:
1. What output it actually produced (written in full)
2. Where its instructions were unclear, missing, or insufficient
3. Where it conflicted with another agent
4. Where the output would embarrass TC or violate brand voice
5. Where the system had no answer and would stall

Verdict scale:
- **PASS** — Output is accurate, complete, actionable, on-brand
- **NEEDS FIX** — Output is usable but has specific problems requiring correction
- **BROKEN** — Output fails at the agent's core function or violates system rules

---

## AGENT 1: ORCHESTRATOR

### What it produced:

**ROUTING DECISION — Spring Booking / Mother's Day Pony Party Campaign**
*Campaign brief received March 22, 2026*

---

"Here's how this campaign runs. Eleven agents are involved — I'm running the first three in parallel, then handing off sequentially where order matters.

**Parallel launch (starting now):**

1. Trend + Market Intelligence Agent — pull Mother's Day pony party trend data from Instagram and TikTok. What's performing in the kids-birthday/horse content space right now? What formats are working? Are there any trending sounds or formats TC should adapt? Deadline: 24 hours. Output goes to Social Content Strategist.

2. Social Content Strategist — begin the campaign calendar structure for March 22 – May 9. Confirm how this campaign maps to the April calendar already in progress. Flag any pillar imbalance the campaign creates. Deadline: 48 hours, pending trend data from above.

3. Brand Positioning + Voice Agent — preliminary flag: this campaign features Reba, Dolly, and Lainey by name for the first time in a coordinated campaign context. Need a voice note on how to introduce the trio in a way that is specific and true to TC's voice — not a "meet the girls!" generic launch. Output due before Copywriter receives briefs.

**Sequential, in order after the above:**

4. Content Creative Direction Agent — once the calendar is approved, build shot lists for each piece of content that requires new filming. The 2023 minis are young, recently introduced, and not yet widely known to the audience. Creative direction must account for that. Flag any assets that need to be captured before April 14 (when the Mother's Day arc begins per the existing April calendar).

5. Copywriter Agent — writes all captions, TikTok scripts, and Facebook posts once creative briefs exist. Receives pillar assignment, platform, and brief from Strategist. Hands all output to Brand Positioning + Voice Agent before Stacie sees it.

6. Brand Positioning + Voice Agent — full review pass on all Copywriter drafts. Line-level audit. No draft exits this stage without a clear status.

7. TikTok Growth Agent — parallel to steps 5/6 — build the TikTok-specific strategy for the campaign on both Business and Personal accounts. This campaign has TikTok content potential on both channels in different ways. Account-split enforcement required.

8. Story Engagement Agent — build the story arc for Mother's Day campaign. Should run weeks of April 27 – May 9. This is separate from the April 2026 calendar story guidance. The arc must not contradict anything in the approved calendar.

9. Comment + DM Response Agent — pre-write responses for the predictable comment and DM types this campaign will generate: booking questions, pricing questions, "this would be perfect for my daughter" soft leads, and any comparison comments ("do you do X?").

10. Website + SEO Agent — audit the pony parties page before April 14. This is a hard deadline because social traffic will begin pointing there. Also brief a campaign landing page if no dedicated Mother's Day page exists.

11. Creator Income Agent — evaluate whether this campaign generates any brand partnership angles. The 2023 minis as a named trio are a new content asset. Flag for brand deal potential.

12. Corporate + Luxury Leads Agent — Mother's Day is a consumer campaign, but the campaign's production quality and the mini-mare content could generate corporate spin-off interest (family day events, employee appreciation). Evaluate and flag if relevant.

**Priority note:** This campaign is categorized as a booking campaign, which sits fourth in the priority order (creator income > brand deals > partnerships > bookings). However, this campaign has creator income signal built into it — the mini-mare content is new, shareable, and sponsor-adjacent for equine/lifestyle brands. Route it at Priority 3 (partnership-adjacent) rather than Priority 4 (straight booking push).

**Approval required from Stacie before production begins:**
- Campaign calendar (from Social Content Strategist)
- Any content that introduces Reba, Dolly, and Lainey as named horses for the first time — Stacie approves how they're introduced
- Any copy that references specific May 10–11 dates (pricing/availability trigger)

**5-day rolling window:** By March 27, the following must be in the queue: Brand Voice note on the mini trio, trend report, and calendar draft. Content production cannot begin without all three."

---

### Breaks found:

**Break 1 — Missing agent: Trend + Market Intelligence Agent is not in the ordered agent list provided in the stress test brief.** The test brief lists 12 agents beginning with Orchestrator; the Trend + Market Intelligence Agent is not listed as one of the numbered steps. But the Orchestrator correctly routes to it because the orchestrator.md file names it as a standard routing destination. This is a documentation gap in the stress test itself, not an agent failure — but it exposes a real issue: the campaign brief as given to the Orchestrator doesn't establish whether Trend + Market Intelligence Agent is in scope. A human running this system without the stress test brief might skip the trend research step entirely.

**Break 2 — Pricing/availability approval trigger creates a bottleneck the Orchestrator doesn't resolve.** The Orchestrator correctly flags that any post mentioning specific dates (May 10–11) requires Stacie's approval. But it doesn't tell the Copywriter Agent how to write a campaign about a specific weekend without mentioning the dates. This creates a workflow pause with no resolution path documented.

**Break 3 — No done-criteria check mechanism for parallel agents.** The Orchestrator says "run steps 1, 2, 3 in parallel" but has no mechanism to verify all three are complete before handing to step 4. In the orchestrator.md file, Rule 8 requires a done-criteria check before handoff — but no implementation detail exists for parallel workflows. The system would stall here in real operation.

**Break 4 — Priority reclassification lacks authority.** The Orchestrator upgrades this campaign from Priority 4 (bookings) to Priority 3 (partnership-adjacent) on its own judgment. Orchestrator Rule 2 states priority order "never flip this stack without Stacie's direction." This is a self-contradiction in the agent's own output — and the orchestrator.md doesn't clarify whether "adjacent priority" upgrades are within the Orchestrator's autonomy.

**Verdict: NEEDS FIX**

The routing logic is strong and the workflow structure is correct. Fixes needed: (1) define how parallel workflows confirm completion before handoff, (2) give the Copywriter a path for writing date-specific content that can be approved, (3) clarify priority reclassification authority.

---

## AGENT 2: TREND + MARKET INTELLIGENCE AGENT

### What it produced:

**Trend Briefing — Mother's Day Pony Party Content**
*March 22, 2026 | Requested by Orchestrator*

---

**RESEARCH SCOPE:** TikTok and Instagram trends in pony party, mini horse, kids birthday, and Mother's Day experience content. Focus period: February–March 2026. No Apify tools accessible in this simulation — analysis based on pattern knowledge and documented platform behavior.

**Confidence disclosure:** The absence of live Apify data drops all findings below High confidence. Treat all findings as Medium confidence pending tool verification.

---

**Format Trend 1: "What my kid did vs. what I expected" reaction split**
What it is: Parent narrates expectation, clip shows the actual child reaction — specifically the gap between what the adult thought would happen and what the child actually did (usually more extreme in both directions).
Confidence: Medium — consistently strong in experience/kids content category.
TC applicability: High. TC has the exact raw material: kids who freeze at the gate, kids who immediately try to climb the pony, kids who cry (in either direction), kids who refuse to leave. The 2023 minis are young, curious, and the right scale for children — they produce strong reactions. Zero additional equipment needed.
Mother's Day angle: Frame the parent's face, not just the kid's. "She thought her daughter would be nervous. She was wrong." That's a Mother's Day post.
Recommended action: Add 2 of these to the campaign calendar. Flag to Creative Direction Agent for shot list — need both a child reaction and a parent watching reaction captured in the same clip.

**Format Trend 2: Named animal personality introductions**
What it is: Introduce a specific animal with their name and one specific personality trait. Short. Direct. No fluff. Performs strongly in the horse and dog content categories. The specificity is the point — audiences follow named animals the way they follow characters.
Confidence: High — this format has been performing in equine content for 18+ months without saturation.
TC applicability: Extremely high. Reba, Dolly, and Lainey have not been formally introduced as named individuals. This campaign is the right moment to do it. The country music naming is an automatic hook that does not need to be forced — it lands without explanation.
Window: This format has not peaked. TC can build a recurring "Reba does something" content lane from this campaign that outlasts Mother's Day.
Recommended action: Build one introduction post per mini mare into the campaign calendar. These are separate from booking posts — they are character introductions that make audiences care before the CTA arrives.

**Format Trend 3: "POV: It's Mother's Day and your gift showed up with four legs"**
What it is: First-person perspective experience walk-through specifically tied to Mother's Day. The framing positions the experience as the gift rather than a booking.
Confidence: Medium — POV format is high-performing generally (see April calendar existing slot); Mother's Day specific application is newer.
TC applicability: Good with caveats. TC must be careful not to frame the pony party as a gift "for mom" if the actual service is a kids birthday party. The framing works if it's accurate: Mother's Day weekend pony parties are events where the whole family is present, not just the child. If TC is offering a "mother-and-child experience" framing for Mother's Day specifically, this is a strong format. If TC is just running a standard pony party on May 10–11, the framing may mislead.
Flag: This is an accuracy/framing issue. Needs Stacie's confirmation of what the Mother's Day weekend events actually are before the Copywriter uses this angle.

**Format Trend 4: Mini horse size comparison content**
What it is: Side-by-side or sequential footage showing the size difference between a mini and a full-size horse, or a mini next to a human adult. The size juxtaposition is inherently funny and endlessly shareable.
Confidence: High — this content category has sustained strong performance for 2+ years.
TC applicability: Very high. TC has both Clydesdales and minis. The contrast between Belle (22-year-old, 1,800+ lb Clydesdale) and Reba (2-year-old mini mare) is a content slot that writes itself. This is not trend-chasing — it is using TC's existing assets in a format that the algorithm rewards.
Recommended action: One mini/Clydesdale contrast clip for the campaign. Flag to Creative Direction Agent.

**Not actionable — documented as monitored:**
- "Aesthetic slow-motion golden hour horse content" — oversaturated, TC has stronger differentiators than pure aesthetic
- Horse costume/dress-up content for Mother's Day — not on-brand for TC's premium positioning
- "Viral sound" strategy where the content is built around a trending audio — TC's content strength is in the real moments, not in audio sync

**Brand partnership signals for this campaign:**
- Equine supplement/feed brands: mini mare content is new, high-volume content for TC — if TC isn't already in conversation with a feed or supplement brand, this campaign is the moment to start
- Children's gift experience platforms: TC's pony party is a bookable experience — platforms that aggregate family experiences (Tinybeans-adjacent, Goldbelly-adjacent for experiences) are worth evaluating
- Western lifestyle apparel brands with a spring/Mother's Day collection launch: timing alignment

**One flag for Orchestrator and Brand Positioning + Voice Agent:**
The Mother's Day framing must be evaluated carefully for TC's Indigenous context. Mother's Day as a commercial holiday sits in a cultural space that Stacie may or may not want to center. This is not a prohibition — it is a flag. TC can run a Mother's Day campaign without making the holiday itself the point. "Spring is booking season" is a framing that captures the same audience without requiring the commercial holiday framing. Escalate to Stacie for direction.

---

### Breaks found:

**Break 1 — Apify tools are not accessible in this simulation, and the agent has no fallback protocol for when tools fail.** The trend-market-intelligence-agent.md lists Apify as a key resource but includes no instruction for what the agent does when the tools are unavailable. The agent correctly disclosed the confidence drop — but the system has no documented contingency. In a real production environment, tool outages would stall this agent entirely with no recovery path.

**Break 2 — The Mother's Day framing flag creates a conflict with the existing April 2026 content calendar.** The April calendar (week 4, April 24) already has a confirmed Mother's Day booking post planned. The Trend Agent has flagged that the Mother's Day framing may need Stacie's sign-off before proceeding — but that content slot is already approved in the calendar. Which approval stands? The system has no documented resolution for a trend-agent flag that conflicts with an already-approved calendar slot.

**Break 3 — No explicit "window remaining before peak" estimate for Format Trend 3 (POV format).** The trend agent rules require this — Rule 2 says reportable trends must be "adaptable before the format becomes oversaturated." The POV format assessment lacks a window estimate.

**Verdict: NEEDS FIX**

Strong analytical output. Breaks are structural: (1) no Apify fallback protocol, (2) conflict resolution mechanism needed when trend flags hit approved calendar slots, (3) window estimate missing from Format 3.

---

## AGENT 3: SOCIAL CONTENT STRATEGIST

### What it produced:

**CAMPAIGN CALENDAR — Spring Booking / Mother's Day Pony Parties**
*March 22 – May 9, 2026 | Runs parallel to approved April 2026 calendar*

---

**INTEGRATION NOTE:** The April 2026 content calendar already contains a Mother's Day soft-build arc beginning Week 3 (April 14) and a booking post on April 24. This campaign layer supplements — it does not replace — the existing calendar. New content slots below are additive, identified as CAMPAIGN ADDITIONS. Existing slots that serve this campaign are tagged CALENDAR SERVES.

**Campaign structure:**
- Phase 1 (March 22 – April 11): Animal introductions. Reba, Dolly, and Lainey become known to the audience before any booking CTA exists.
- Phase 2 (April 14 – May 1): Experience storytelling. What a pony party with the 2023 minis looks and feels like. No hard sell.
- Phase 3 (May 2–9): Booking close. Direct, calm, informed. By this point the audience knows the horses.

---

**PHASE 1 ADDITIONS — March 22 – April 11**

| Date | Platform | Pillar | Format | Concept | CTA | Pillar Check |
|------|----------|--------|--------|---------|-----|--------------|
| Mar 23 | Instagram | The Animals | Reel or single image | **Introduce Reba.** One shot, one caption. Her name, one specific thing she does. Nothing more. First of three mini introductions. | None | Animals — first post of campaign |
| Mar 26 | Instagram | The Animals | Reel or single image | **Introduce Dolly.** Same format as Reba introduction. Consistent visual style — audiences should register these as a series. | None | Animals — no back-to-back on same platform (Mar 25 is North Idaho Life per existing calendar) |
| Mar 30 | TikTok Business | The Animals | Short clip | **Introduce Lainey.** TikTok version — 10–15 seconds, one specific moment, Lainey's name in the first line. Closes the trio introduction on TikTok. | None | Animals — TikTok placement, no conflict |
| Apr 2 | Instagram | The Animals | Reel | **Trio together.** All three minis in one frame — the country music naming angle works here. "Reba. Dolly. Lainey." Three shots, three names, one caption. The names do the work. | None | Animals — fourth and final introduction post |
| Apr 8 | Facebook | The Work | Photo or short video | **What it takes to get three minis ready for an event.** Grooming, leading, managing three young mares who have opinions. Real. Funny if warranted. Shows the professionalism behind the accessibility. | None | The Work — supports Mother's Day arc without selling |

**PHASE 1 PILLAR AUDIT:**
The introduction series is 4 Animals posts and 1 Work post in approximately 16 days. Per the April calendar, the existing Week 1 Monday slot is already Animals (Millie). This would create back-to-back Animals posts if March 23 lands adjacent to the existing March 30 calendar slot. Resolution: Move the March 30 intro to March 31 (Tuesday) to maintain the no-back-to-back rule.

---

**PHASE 2 ADDITIONS — April 14 – May 1**

*(Existing April calendar already contains pony party moment content on April 15 Facebook and pony booking post on April 24. Phase 2 adds the experiential layer on top of those.)*

| Date | Platform | Pillar | Format | Concept | CTA |
|------|----------|--------|--------|---------|-----|
| Apr 16 | TikTok Business | Education | Talking head | "What to expect at a TC pony party with the 2023 minis" — calm, professional, what TC handles, what the host doesn't have to. | Link in bio |
| Apr 22 | Instagram Stories | Events + Booking | Story sequence (3 frames) | "Mother's Day weekend dates" — soft, informational. Frame 1: the minis together. Frame 2: "May 10–11 are available." Frame 3: link sticker to tribalcowboy.com/pony-parties. | Link sticker |
| Apr 27 | Instagram | The Moments | Carousel | Real pony party sequence — arrival through cleanup. Lead with a child meeting Reba (or Dolly or Lainey) for the first time if footage exists. Real moments, not posed. | None |
| Apr 29 | Facebook | Events + Booking | Link post + longer caption | **Main Mother's Day booking post for Facebook.** Specific, informational, warm. "Mother's Day weekend is May 10–11. Pony parties are available. Reba, Dolly, and Lainey have openings." Calendar-style CTA to website. | www.tribalcowboy.com |
| May 1 | TikTok Business | The Moments | Short video | A real pony party reaction clip — if footage exists by this point. The ponies meeting kids for the first time. No narration needed. Reaction is the content. | None |

**EVENTS + BOOKING COUNT CHECK (full campaign period):**
April 22 story sequence = 1 booking touchpoint
April 24 existing calendar post = 1 booking touchpoint
April 29 Facebook post = 1 booking touchpoint

That is 3 booking posts in a period containing approximately 22 total posts. 3/22 = 13.6% — within the 20% cap. Confirmed compliant.

---

**PHASE 3 — May 2–9 (Final push)**

| Date | Platform | Pillar | Format | Concept | CTA |
|------|----------|--------|--------|---------|-----|
| May 4 | Instagram | Events + Booking | Single image | "One weekend left." The minis. Short caption. Link in bio. This is the one direct booking push for Instagram. | Link in bio |
| May 4 | Facebook | Events + Booking | Same post adapted for Facebook | Slightly longer caption with more event detail. Same calm energy. | www.tribalcowboy.com |
| May 6 | Instagram Stories | The Animals | Story | Behind the scenes — Reba, Dolly, and Lainey on a regular Tuesday. Keeps the animals present without selling. | None |
| May 7 | TikTok Business | Education | Short clip | "What happens after the pony party" — TC breakdown, horses loading, what cleanup looks like. Shows the work. Ends the campaign on the Work pillar, not the Booking pillar. | None |

---

**CREATOR INCOME SIGNAL CHECK:**
Campaign period (March 22 – May 9 = ~7 weeks). Minimum 1 creator income signal per week. The mini-mare introduction series qualifies weeks 1–2. The pony party carousel (Apr 27) qualifies week 5. The reaction clip (May 1) qualifies week 6. Week 3 (Apr 6–10) and week 4 (Apr 13–17) rely on the existing April calendar to meet this requirement — the calendar does include creator income content in those weeks. Minimum met.

---

### Breaks found:

**Break 1 — The campaign calendar has no dedicated slot for TikTok Personal during the campaign period.** The TikTok Growth Agent rules (and the existing April calendar) both document that Stacie's Personal TikTok (@paintedmakeup) should receive 2–4 posts per week. This campaign calendar doesn't address Personal TikTok at all. That is appropriate if this strategist is treating Personal TikTok as out-of-scope for a booking campaign — but the system documentation (platform-rules.md) establishes that Personal TikTok is a "natural feeder for TC discovery." A 7-week booking campaign with no Personal TikTok integration is a gap.

**Break 2 — Phase 3 "Final push" contains two Events + Booking posts on the same day (May 4, both Instagram and Facebook).** The Social Content Strategist's Rule 11 says "no more than two CTAs in the same week across all platforms should point to the same link." Two posts on the same day pointing to the pony party booking page may violate the spirit of this rule. The rule technically allows it (it says "week," not "day"), but posting the same booking CTA on two platforms the same day concentrates the commercial signal in a way that could feel like pressure.

**Break 3 — The Strategist does not confirm whether the pony party page at tribalcowboy.com/pony-parties exists and is ready.** The April 2026 calendar explicitly flags this as a pre-campaign requirement: "Verify /pony-parties page is current, has real photos, and the inquiry CTA works." The campaign calendar sends traffic there without confirming the page is live. This is a hard business risk — driving traffic to a broken or missing page loses real bookings. The Strategist should either confirm or escalate to the Website + SEO Agent before publishing any CTA.

**Break 4 — The animal introduction series (Phase 1) creates a pillar imbalance the Strategist partially flags but doesn't fully resolve.** Four Animals posts in 16 days on Instagram is within the letter of the rules (no same pillar back-to-back), but it strains the spirit of the 7-pillar rotation. The Strategist notes this but only proposes moving one post by one day. A fuller solution would be to spread the introductions across platforms more deliberately or extend the phase by 1 week.

**Verdict: NEEDS FIX**

Campaign structure is logical and well-integrated with the existing April calendar. The arc progression from introduction to experience to close is correct. Fixes needed: (1) integrate Personal TikTok into the campaign plan, (2) resolve May 4 dual-platform same-day booking CTA, (3) add an explicit website page verification step before any CTA goes live.

---

## AGENT 4: CONTENT CREATIVE DIRECTION AGENT

### What it produced:

**SHOT BRIEFS — Spring Booking / Mother's Day Pony Party Campaign**
*Priority production: March 22 – April 2 (mini introductions) and April 27 (pony party carousel)*

---

**BRIEF 1 — Reba Introduction (Instagram, March 23)**
*Pillar: The Animals | Format: Reel or single image*

**Hero shot:**
Reba facing the camera at medium distance — low enough angle that she fills the frame. Her expression is the content. Whatever her ears are doing, whatever her eyes are doing. That's the shot. If she's curious about the camera, that's perfect. If she's suspicious, that's also perfect.

**Shot list (production order — capture all of these in one session):**
1. HERO: Medium close-up, Reba facing camera, natural light, not backlit (essential)
2. Side profile, Reba walking toward something — her movement quality (bonus)
3. Close-up of her face, eyes specifically — what she looks like when she's paying attention (essential)
4. One shot of Stacie's hand and Reba's nose — scale and texture (bonus)

**Visual tone direction:**
Early morning light is better than midday. Soft, directional. Not golden hour — TC's aesthetic is working-day light, not photo shoot light. Shoot outside the barn where natural light is available. Background should be natural — fence, pasture, sky — not a barn wall or equipment. Clean background, simple. Let Reba be the visual.

**Audio direction:**
No music. Ambient sound — pasture, wind, whatever is happening. If this is a Reel, the natural ambient audio is the sound design.

**Text overlay direction:**
One line, bottom third of screen, white bold text, no background box:
"This is Reba."
Hold for 2 seconds. That's the entire caption. The rest goes in the caption below the post.

**What to avoid:**
- Do not shoot from above — it diminishes her and makes her look like a small prop, not a personality
- Do not include other horses in the frame — this is her introduction, not a herd shot
- Do not use a filter or color grade — TC's aesthetic is true-color, natural light, real place

---

**BRIEF 2 — Trio Together (Instagram, April 2)**
*Pillar: The Animals | Format: Reel or single image*

**Hero shot:**
All three minis — Reba, Dolly, Lainey — in frame together, arranged naturally (not posed in a line). If they're standing together on their own, that's the shot. The frame should feel like it caught a moment, not like a photo shoot.

**Shot list (production order):**
1. HERO: All three together, natural arrangement (essential)
2. Each one individually, same framing as their introduction shots (bonus — ties back to Phase 1)
3. One shot moving — all three walking in the same direction (essential if movement is available)
4. Close-up of three sets of hooves or three noses in sequence — size and detail (bonus)

**Visual tone direction:**
Same as the individual introductions — consistent visual language matters for the series to register as a series.

**Text overlay for Reel version:**
Three consecutive title cards, same format:
"Reba." — 1.5 seconds
"Dolly." — 1.5 seconds
"Lainey." — 1.5 seconds

No music until after the third name appears, if music is used at all. Let the names hit.

**What to avoid:**
- Don't frame this as a "meet the ponies" generic farm post — the names are the differentiator, not the fact that there are three minis
- Don't add a booking CTA in the text overlay — this is an introduction post, not a sales post

---

**BRIEF 3 — Pony Party Carousel (Instagram, April 27)**
*Pillar: The Moments | Format: Carousel (5–7 images)*

**ASSET REQUIREMENT FLAG:**
This carousel requires real event footage from an actual pony party featuring the 2023 minis (Reba, Dolly, or Lainey). If no such event has occurred before April 27, this slot cannot be filled with authentic content. Escalating to Orchestrator and Social Content Strategist: confirm whether a pony party with the 2023 minis is on the calendar between now and April 25. If not, this slot must be moved or repurposed.

*Proceeding with brief assuming a qualifying event occurs:*

**Slide structure:**
- Slide 1 (hero/hook): A child's face the moment they register the pony. Close. Real. Not smiling yet — the moment before the smile.
- Slide 2: The pony (name one of the three) waiting. Patient. Not performing.
- Slide 3: Hands — small hands reaching, the pony's nose meeting them. The scale difference is the emotion here.
- Slide 4: A parent watching. The adult face while the kid is with the pony. This is the Mother's Day resonance.
- Slide 5: The middle of the party — kids, ponies, the real texture of it. Not posed.
- Slide 6 (if available): End of party — a child who doesn't want to leave. The best possible close.
- Final slide: TC-branded sign or banner, or Stacie handling one of the minis. Proof that this is TC, not any other operation.

**Shot list for the event:**
1. Position one person specifically to capture child first-reaction faces (essential — without this, the carousel loses its hook)
2. Parent watching while child is with the pony — medium shot from the side (essential)
3. Small-hand/pony-nose moment (essential)
4. Overall scene at mid-party — wide enough to show the scale of the event (essential)
5. End-of-party moment if one naturally occurs (bonus)

**Visual tone direction:**
Natural light event photography — not flash, not posed. TC's photography style is candid. If the light is bad (indoor venue, overcast), that is an asset gap, not a reason to fake better light. Document what exists accurately.

**Audio (if Reel version):**
Ambient event sound — kids, horses, outdoors. No music.

**What to avoid:**
- Do not use photos where guest faces are clearly identifiable without consent clearance
- Do not include any TC pricing or service information in slide text — let the event speak

---

### Breaks found:

**Break 1 — The most important brief in the campaign has an unresolved asset gap.** Brief 3 (the pony party carousel, which is the emotional core of the campaign) requires real footage of the 2023 minis at an actual event. As of March 22, it is unknown whether such an event exists between now and April 27. The Creative Direction Agent correctly flags this to the Orchestrator — but the system has no documented protocol for what happens next if the answer is "no event scheduled." The campaign carousel either disappears from the calendar or gets replaced with a different content type. The system should tell the Strategist which, but the handoff documentation doesn't specify this recovery path.

**Break 2 — The audio direction is inconsistent across the three briefs.** Brief 1 says "no music, ambient only." Brief 2 says "no music until after names appear, then optional." Brief 3 says "ambient event sound, no music." This is functionally consistent but the inconsistency in language could cause confusion if different people are executing different briefs. A style guide for the campaign's audio direction should exist and be referenced, not re-stated differently in each brief.

**Break 3 — Brief 2's text overlay instruction ("Reba." "Dolly." "Lainey." each 1.5 seconds) is not actionable without knowing which editing app Stacie uses.** The Creative Direction Agent rule 1 says every brief must be actionable by one person with a smartphone. The timing instructions are standard for professional editing software but may not be replicable in CapCut or Instagram's native editor without additional guidance. The agent should either confirm the editing platform or provide platform-agnostic instructions.

**Break 4 — No brief exists for the TikTok Business intro content (the Lainey introduction on March 30 per the campaign calendar).** The Creative Direction Agent produced briefs for Instagram but not for the TikTok version. This is a gap in coverage.

**Verdict: NEEDS FIX**

The briefs that exist are genuinely strong — specific, actionable, TC-appropriate. The hero shot concept, slide structures, and "what to avoid" sections are exactly right. The system breaks in this agent are about coverage gaps (missing TikTok brief, missing audio style guide) and the unresolved asset gap for the most important piece of the campaign.

---

## AGENT 5: BRAND POSITIONING + VOICE AGENT

### What it produced:

**PRELIMINARY VOICE GUIDANCE — 2023 Mini Mare Introduction (Reba, Dolly, Lainey)**
*Issued before Copywriter receives campaign briefs*

---

**The naming is the content. Don't explain it.**

The country music naming of this trio — Reba McEntire, Dolly Parton, Lainey Wilson — is genuinely funny, genuinely TC, and immediately recognizable. The instinct to explain it ("named after country music legends") is the wrong instinct. Real people who notice it will enjoy noticing it. Real people who don't notice it don't need to be told. The explanation cheapens what is already working.

**What TC voice sounds like for each introduction:**

For Reba:
Right: "This is Reba. She has opinions about mornings."
Wrong: "Meet Reba — named after the country music legend herself. She's one of our newest additions and we can't wait for you to get to know her."

For Dolly:
Right: "Dolly is three. She's already figured out who's going to give her the carrots first."
Wrong: "Dolly joined the Tribal Cowboy family in 2023 and has been delighting guests ever since."

For Lainey:
Right: "Lainey. 2023. Still learning what fences mean."
Wrong: "Our youngest mini, Lainey, is full of personality and ready for spring events."

**The pattern:**
Name. Age or specific fact. One observed behavior. That's it. The personality comes from the observation, not from the adjectives.

**Banned in all intro copy:**
- "Meet [name]"
- "She's one of our newest additions"
- "Full of personality"
- "We can't wait for you to meet her"
- "Delighting guests"
- Any sentence that sounds like a rescue organization bio or a pet adoption post

**The trio together:**
When all three appear in one post, resist the temptation to write them as a unit. They are three individual horses who happen to share a birthyear and a naming pattern. Write them as individuals even when they're in frame together.

Right: "Left to right: Reba, Dolly, Lainey. They disagree about almost everything."
Wrong: "Introducing the 2023 trio — Reba, Dolly, and Lainey are here and ready for your spring events."

**Indigenous identity note for this campaign:**
None of the pony party content in this campaign directly references Stacie's Nisenan Maidu identity. That is appropriate — this campaign does not require it, and inserting it as a framing device would be the kind of identity-as-marketing move this system explicitly prohibits. The campaign stands on the horses and the experience. If a post naturally touches on Stacie's connection to working with young animals or to the land in spring, that can be present — but it cannot be the angle.

**Voice audit status for campaign briefs:**
No Copywriter drafts have been received yet. This preliminary note goes to the Copywriter Agent as framing before any drafts are written.

---

**VOICE AUDIT — Sample Instagram Caption (Reba Introduction)**
*Draft received from Copywriter Agent simulation*

**Draft:**
"This is Reba.
She was born in 2023 and she already has the energy of someone who's been here longer than she has. Curious about everything. Patient with nobody in particular. Reba's one of the reasons spring pony parties at TC look the way they do.
Spring pony party dates are open. tribalcowboy.com"

**Audit result: PASS with one note.**

Line-level assessment:
- "This is Reba." — Strong opener. Specific, direct, no introduction language.
- "She was born in 2023 and she already has the energy of someone who's been here longer than she has." — Passes. Original observation. Not a general equine cliché.
- "Curious about everything. Patient with nobody in particular." — Passes. Specific contrast. The "patient with nobody in particular" line is actually excellent.
- "Reba's one of the reasons spring pony parties at TC look the way they do." — This line is doing something clever but it's also slightly vague. "Look the way they do" — what way is that? This line would be stronger with a specific visual detail. Not a failure, but an opportunity.
- "Spring pony party dates are open. tribalcowboy.com" — Clean. Calm. No pressure. Passes.

**Recommendation:** Strengthen "look the way they do" with one specific image. Otherwise approved.

---

### Breaks found:

**Break 1 — The Brand Positioning + Voice Agent's preliminary guidance was produced before the Copywriter Agent's drafts existed, which is correct process — but the agent has no mechanism to confirm the Copywriter actually received and read the preliminary note.** In the system workflow, the Brand Voice Agent sends preliminary framing to the Copywriter. But there is no confirmation step. If the Copywriter writes drafts that ignore the preliminary guidance (for example, using "meet Reba" despite the explicit prohibition), the Brand Voice Agent catches it in the audit — but the cycle of write-flag-rewrite costs production time that the preliminary note was supposed to prevent. A "preliminary guidance received" confirmation step is missing.

**Break 2 — The voice audit sample demonstrates the agent working correctly, but the "PASS with one note" status doesn't clearly define next steps.** The audit gives a line-level note ("Reba's one of the reasons...") and a recommendation but doesn't specify: does the Copywriter revise and resubmit, or does the agent revise and send? The agent rules say the agent "rewrites" when a rewrite is required and "returns to Copywriter" when a draft "needs revision." "Pass with one note" doesn't fit either category cleanly. The status taxonomy needs a third tier: "Approved pending one-line revision" with a clear process for who makes the change.

**Break 3 — The Indigenous identity guidance in the preliminary note is appropriately hands-off ("this campaign does not require it") but it creates a gap for what to do if a piece of pony party content naturally touches on Stacie's relationship to the work.** The agent correctly says this content can be present if natural. But the guidance does not tell the Copywriter how to handle that case when it arises. A sentence like "if Stacie's connection to working with these young animals comes through naturally in a specific post, flag it for Stacie's review before finalizing — it shouldn't be written for her" would close this gap.

**Verdict: PASS**

This is the strongest agent performance in the system. The preliminary voice guidance is specific, actionable, and exactly what the Copywriter needs. The sample audit is correct, line-level, and useful. The breaks are real but minor — they are system design issues, not agent execution failures.

---

## AGENT 6: COPYWRITER AGENT

### What it produced:

**CAMPAIGN COPY DRAFTS — Spring Booking / Mother's Day Pony Parties**
*Drafted for Brand Positioning + Voice Agent review — do not publish without approval*

---

**DRAFT 1 — Instagram Caption, Reba Introduction**
*Pillar: The Animals | Platform: Instagram | No CTA*

She walked up to the fence the first morning and stood there looking at the barn like she'd been waiting for someone to let her run it.

That was 2023. She's three now. Still working on the patience. Reba has a very specific idea about how the day should go, and she'll tell you about it.

Spring pony parties open March 22. tribalcowboy.com

#TribalCowboy #NorthIdaho #IdahoHorses #HorsesOfInstagram #PonyParty #FarmLife #HorseLife #EquestrianLife

---

**FLAG TO BRAND VOICE AGENT:** The final line includes a CTA with specific date (March 22) — the Orchestrator identified this as an approval trigger. Flagged. Stacie to confirm this date reference before this post goes live.

---

**DRAFT 2 — Instagram Caption, Trio Together (April 2)**
*Pillar: The Animals | Platform: Instagram | No CTA*

Left to right: Reba, Dolly, Lainey.

They were born in 2023, they came from the same breeder, and they have been conducting experiments ever since on the structural integrity of fence boards.

Spring parties start soon. More at tribalcowboy.com

#TribalCowboy #NorthIdaho #IdahoHorses #HorsesOfInstagram #PonyParty #FarmLife #HorseLife #RanchLife #HorseMom

---

**DRAFT 3 — TikTok Business Script, Lainey Introduction**
*Platform: TikTok Business | Pillar: The Animals | No CTA*

**Hook option A:** "This is Lainey. She's two. She has already decided she owns this property."

**Hook option B:** "Her name is Lainey. Named after Lainey Wilson. She has no idea who that is."

**Hook option C:** "Two-year-old mini horse. Three-year-old attitude."

**Body structure (15–20 seconds total):**
- 0:00–0:03: Hook (choose one)
- 0:03–0:10: One clip of Lainey doing the specific thing she does — whatever that thing is. She has a thing.
- 0:10–0:18: Text overlay: "She's available for spring pony parties. She doesn't know that yet either."
- 0:18–0:22: Hold on her face. Let the clip end naturally.

**FLAG TO CREATIVE DIRECTION AGENT:** Body structure line "the specific thing she does — whatever that thing is" is a placeholder. Needs a real behavioral note about Lainey from the horse-roster.md or from Stacie before this script is finalized. The horse-roster.md currently shows "[ADD content notes]" for Lainey. This script cannot be completed without that information.

**Hashtags:** #HorseTok #NorthIdaho #TribalCowboy #PonyParty #IndigenousCreator

---

**DRAFT 4 — Facebook Post, Mother's Day Booking (April 29)**
*Pillar: Events + Booking | Platform: Facebook*

Mother's Day weekend — May 10–11 — we have pony party availability.

Reba, Dolly, and Lainey are three mini mares born in 2023. They're calm, curious, and at this point better with children than most adults. If you're planning something for Mother's Day weekend and a pony party is on the table, now's the time to check dates.

Everything is handled on our end — setup, the horses, the cleanup. The birthday kid gets the ponies. You get to actually be at the party.

Check availability at www.tribalcowboy.com or send us a message.

#NorthIdahoEvents #TribalCowboy #IdahoHorses

---

**DRAFT 5 — Instagram Caption, Phase 3 Close (May 4)**
*Pillar: Events + Booking | Platform: Instagram*

One weekend left for spring pony parties — May 10 and 11.

If you've been thinking about it, now's a good time to check dates.

tribalcowboy.com

#TribalCowboy #NorthIdaho #PonyParty #NorthIdahoEvents #IdahoHorses

---

**DRAFT 6 — TikTok Business Script, "What a TC Pony Party Actually Includes" (April 16)**
*Pillar: Education | Platform: TikTok Business*

**Hook option A:** "Here's what actually happens when you book a pony party."

**Hook option B:** "What shows up when you book a Tribal Cowboy pony party."

**Hook option C:** "You booked the pony party. Here's what that means."

**Body structure (30–40 seconds):**
- 0:00–0:03: Hook
- 0:03–0:10: "We arrive with the horses. We handle the setup. You tell us where and when." [B-roll or text overlay of setup process]
- 0:10–0:20: "The ponies are Reba, Dolly, and Lainey. Three minis, born 2023. They're used to kids." [Quick clips of each mini]
- 0:20–0:32: "We manage everything — the animals, the safety, the cleanup. You're at the party. We're running it." [Event footage if available]
- 0:32–0:38: "Spring dates are available. tribalcowboy.com"

**Hashtags:** #HorseTok #NorthIdaho #TribalCowboy #PonyParty #ClydesdaleTok

---

### Breaks found:

**Break 1 — Draft 3 (Lainey TikTok) has an unfillable placeholder because the horse-roster.md has no behavioral notes for Lainey.** The horse-roster.md file shows "[ADD content notes]" for all three 2023 minis. The Copywriter correctly flags this. But this is a systemic data gap: the horse roster was never completed with personality/behavioral notes for Reba, Dolly, or Lainey. Every piece of content that asks for a specific, observed behavior for these three horses hits the same wall. The system cannot produce the level of specificity it demands without that information. This is the single most consequential data gap for this campaign.

**Break 2 — Draft 1's CTA contains a specific date ("Spring pony parties open March 22") which the agent correctly flags as an approval trigger.** But the approval trigger creates a workflow pause: the post cannot go live on March 23 (its planned date) if Stacie hasn't approved the date reference by March 22. The 24-hour production window is tight. The system has no documented escalation path for when an approval trigger falls within 24 hours of a planned post date.

**Break 3 — Hook option A for Draft 3 ("She has already decided she owns this property") and Hook option C ("Two-year-old mini horse. Three-year-old attitude") both make behavioral claims about Lainey that are not sourced in the horse-roster.md.** The Copywriter is technically fabricating Lainey's personality because no personality data exists. This is not a brand voice failure — the lines are actually excellent. But they violate the system's foundational rule: specificity must be true. If Lainey is actually shy and cautious rather than bold and opinionated, these hooks misrepresent the horse.

**Break 4 — Draft 6's body copy ("They're used to kids") makes a competency claim that is potentially false for 2-year-old minis with limited event history.** This is a substantive accuracy concern. The Copywriter agent's escalation triggers explicitly include: "A draft cannot be written without information that is missing and cannot be assumed." Whether the 2023 minis are actually event-tested and safe with children is information the system does not have. This should have been flagged as an escalation trigger, not written as a stated fact.

**Verdict: NEEDS FIX**

The actual copy quality is strong — particularly Drafts 1, 2, 4, and 5, which demonstrate exactly the TC voice the system is designed to produce. The breaks are systemic rather than voice failures: missing animal data, a tight approval window, and one potentially false behavioral claim. The horse-roster data gap (Break 1) will undermine every future piece of animal-specific content until it is resolved.

---

## AGENT 7: TIKTOK GROWTH AGENT

### What it produced:

**TIKTOK CAMPAIGN STRATEGY — Mother's Day Pony Party**
*Account: TC Business TikTok (@Tribal_Cowboy) + Stacie Personal (@paintedmakeup)*
*Campaign period: March 22 – May 9, 2026*

---

**ACCOUNT STATUS REMINDER:**
TC Business TikTok (@Tribal_Cowboy) is dormant. 5 followers. No profile photo. No bio. Last activity 2024. Before this campaign produces a single video, the account must be reactivated: profile photo (Reba, Dolly, or Lainey — not a logo), bio written, consistent posting cadence established. Content from this campaign appearing on a ghost account is wasted. Reactivation is Week 1, not Week 3.

**Reactivation tasks (must complete before first campaign video):**
1. Profile photo: One of the 2023 minis, high-quality, bright crop
2. Bio: "North Idaho pony parties, Clydesdale events + horse photography. Owned by Stacie. @paintedmakeup for the unfiltered version." — or equivalent. Draft goes to Brand Voice Agent.
3. First 3 posts before campaign content drops: The existing farrier content (713 views) and pony party content (777 views) are already on the account. They serve as proof of life. The campaign's first new video should arrive after those are visible.

---

**BUSINESS TIKTOK CAMPAIGN PLAN (@Tribal_Cowboy)**

**Series: "You've Never Been This Close to Something This Small"**
*The mini-mare series. 6 episodes. Runs the length of the campaign.*

Purpose: Introduce Reba, Dolly, and Lainey as individual personalities. Position TC's pony parties as the place where these specific horses meet kids. Build attachment before the CTA arrives.

**Episode 1 — Reba (Week 1, March 23)**
Hook options:
A: "This is Reba. She's three. The fence did not survive the winter."
B: "Three-year-old mini horse. Already knows who has the carrots."
C: "Her name is Reba McEntire. She didn't choose it but she's grown into it."

Body: One clip of Reba doing one specific thing. 10 seconds. Her name in text. End.
Length: 12–15 seconds
No music. Ambient sound.
Monetization flag: Weak on its own — strong as series infrastructure.

**Episode 2 — Dolly (Week 2, March 26)**
Same format as Episode 1. Dolly's specific thing. 12–15 seconds.

**Episode 3 — Lainey (Week 3, March 30)**
Same format.

**Episodes 4 & 5 — Experience content (Weeks 4–5)**
What a pony party with these three looks like. Real event footage required (see asset gap note from Creative Direction Agent).

**Episode 6 — The close (Week 6, May 4–6)**
The moment before the party starts — Reba, Dolly, and Lainey waiting. The quiet before the kids arrive. No CTA in the video. The caption does the work.

---

**PERSONAL TIKTOK CAMPAIGN PLAN (@paintedmakeup)**

This account should not run a "Mother's Day campaign." That framing belongs on Business. What Personal TikTok can do for this campaign period:

**2 posts in the campaign window that naturally support discovery:**

Post 1 (April, flexible timing): A behind-the-scenes moment with the 2023 minis that is genuinely personal — not TC service promotion. "Training three mini mares who all have different opinions about being led" is a Personal TikTok post. "Book a pony party with our minis" is not.

Post 2 (Late April / early May): Stacie talking directly to camera about something true — running spring events as a solo operator, or what it actually takes to manage three young minis at their first busy season. Real. Unscripted. Personal account energy.

**Account split enforcement — both of these fail if:**
- They mention pricing
- They include a TC booking CTA
- They feel like TC ads posted from a personal account

**Soft link is acceptable:** Bio link pointing to tribalcowboy.com. Occasional "more info at the link" at the very end of a video, separated from the content itself.

---

**HOOK ANALYSIS — Which hooks will actually stop a scroll for this content:**

For mini horse content, what stops the scroll:
1. A size juxtaposition the viewer wasn't expecting (mini next to a Clydesdale, mini next to an adult's hand)
2. A behavioral surprise (a mini doing something a viewer only associates with full-sized horses)
3. A name that creates instant curiosity (the country music naming creates a 1-second hook before anything else happens)
4. A child's face reacting

For booking content, what stops the scroll:
1. Starting mid-activity — "We're already set up at the party" beats "We're excited to announce"
2. Specificity of place — "Athol, Idaho" means something to people who know the region and creates curiosity in people who don't
3. The absence of typical party vendor language — TC content sounds different from every other party post in the feed

---

**Monetization flags:**
- The mini introduction series (if consistent, well-produced) is a strong spec portfolio piece for equine/family lifestyle brands
- The "pony party setup and execution" content is the strongest corporate-buyer-facing content — flag for Creator Income Agent
- First episode of a new series is eligible for TikTok Creativity Program if it meets watch time thresholds — prioritize completion rate

---

### Breaks found:

**Break 1 — The account reactivation requirement is a genuine blocker that the system has no owner for.** The TikTok Growth Agent correctly identifies that @Tribal_Cowboy needs a profile photo and bio before campaign content runs. But the agent cannot implement these changes — only Stacie can. The system has no documented mechanism for flagging "Stacie must do this specific technical task before the campaign can begin." The Orchestrator should be routing this as a pre-production requirement, but the Orchestrator's handoff rules don't include "flag technical platform setup tasks to Stacie."

**Break 2 — The Personal TikTok plan contains a gap: "Training three mini mares who all have different opinions about being led" is proposed as a post concept, but it requires the same behavioral notes about the minis that are missing from horse-roster.md.** The Personal TikTok agent is hitting the same data gap as the Copywriter Agent. Until Lainey, Reba, and Dolly have documented personalities, any animal-specific content that claims specificity is either fabricated or vague. A horse with "[ADD content notes]" in its file cannot anchor a Personal TikTok series.

**Break 3 — No done criteria check for the series concept.** The TikTok Growth Agent's done criteria requires: "Each video has a hook, body structure, CTA, and hashtag set" and "Series concepts have at least 4 episodes planned before launch." Episodes 4 and 5 are marked as "real event footage required" with no alternative plan if that footage doesn't exist before their planned dates. The agent produced a plan that cannot meet its own done criteria without confirming the asset exists.

**Break 4 — No account-split enforcement note exists for one scenario this campaign creates.** The same mini mares (Reba, Dolly, Lainey) will appear on both Business TikTok (as service-linked content) and Personal TikTok (as behind-the-scenes personal content). The TikTok Growth Agent's vetting process requires answering: "Is this the same video?" But for the minis, the challenge is subtler — the same animal appearing on both accounts in the same week, in different framings, could confuse followers who follow both. The agent needs a minimum time gap or framing differentiation rule for same-animal, dual-account use.

**Verdict: NEEDS FIX**

The strategy is strong — the series concept is genuinely good, the account split enforcement is mostly correct, and the hook analysis is exactly what this agent is supposed to produce. The breaks are: missing technical ownership for account reactivation, data gaps for mini personalities, and incomplete series planning due to asset uncertainty.

---

## AGENT 8: STORY ENGAGEMENT AGENT

### What it produced:

**STORY ARC — Mother's Day Pony Party Campaign**
*Runs: April 27 – May 9, 2026*
*Platforms: Instagram Stories*
*Theme: Get to know the minis → see the experience → dates are available*

---

**NOTE:** This arc runs separately from the standard weekly story content. It adds depth to the campaign close without repeating what the feed is already saying. The feed does the content. The stories do the warmup and the follow-through.

---

**WEEK OF APRIL 27 — "The Minis in Real Life"**

*Theme: Who Reba, Dolly, and Lainey actually are — before any booking mention.*

**Monday April 27**
Frame 1: One of the three minis doing something specific. No text overlay beyond her name.
Text: "Reba."
Interactive: None
Timing: 8:00 AM

Frame 2: A short clip or photo of all three together.
Text: "The 2023 crew."
Interactive: Poll — "Do you know who they're named after?" / "Country legends" vs "No idea"
Timing: 8:05 AM

Frame 3: Behind-the-fence moment — what it looks like when Stacie is managing all three at once.
Text: "Three minis with three opinions. Spring is going well."
Interactive: Question box — "What would you name a mini horse?"
Timing: Later in the day (varies naturally)

**Tuesday April 29**
Frame 1: Morning paddock shot — the minis in early light.
Text: "They knew before we did."
Interactive: None
Note: This is the day the Facebook booking post goes live. Stories should feel like the warm-up, not the announcement.

Frame 2: A single image of one mini's face close-up.
Text: Nothing. Let the image be the image.
Interactive: Reaction slider "Her energy right now" with low and high energy emojis
Timing: Same day as the Facebook post, late morning

**Wednesday April 30**
No planned story unless an organic moment presents itself. The arc should breathe — not every day needs content.

---

**WEEK OF MAY 4 — "One Weekend Left"**

*Theme: The close. Calm, direct, not urgent.*

**Monday May 4**
Frame 1: Same day as the feed booking post (Instagram). Story version is the backstory.
Text: "May 10–11. Reba, Dolly, and Lainey. That's the weekend."
Interactive: Link sticker to tribalcowboy.com/pony-parties
Timing: Posted same day as the feed booking post, mid-morning

Frame 2: Photo of what setup actually looks like before a pony party.
Text: "We handle this part."
Interactive: None

**Wednesday May 6**
Frame: Behind the scenes — minis on a regular day, not event day.
Text: "Two days out from Mother's Day weekend. The girls are not thinking about it."
Interactive: None
Tone: Dry. TC humor. No urgency.

**Friday May 9**
Frame 1: Final story of the campaign arc.
Text: "Tomorrow. If you're curious what it looks like — tribalcowboy.com"
Interactive: Link sticker
Timing: Morning

Frame 2: A single image — one of the minis looking directly at the camera.
Text: "Happy Mother's Day weekend."
Interactive: None
Timing: Same day, evening. Let this one close the arc quietly.

---

**APPROVAL NOTE:** This arc includes story content related to a major campaign. Per story-engagement-agent.md approval triggers, "Story arcs for major campaigns" require Stacie's review before going to plan. This arc is submitted for Stacie's approval before any content is produced.

**WHAT THIS ARC DOES NOT DO:**
- Does not repeat the feed content verbatim
- Does not use countdown urgency ("Only X days left!")
- Does not push pricing
- Does not post every day when there's nothing real to say
- Does not make Stacie sound desperate for bookings

---

### Breaks found:

**Break 1 — The story arc references the Facebook booking post (April 29) and the Instagram feed post (May 4) but was developed without confirmed knowledge of whether those posts are finalized.** Story content is supposed to complement feed content — but if the feed post timing shifts (e.g., Stacie postpones the April 29 Facebook post), the story arc loses its anchor. The system has no documented protocol for story arcs to re-synchronize when the feed calendar changes.

**Break 2 — The poll in Monday April 27 ("Do you know who they're named after?") is a soft trivia moment — but it exposes a small brand risk.** If the answer "Country legends" is selected by most followers, TC should be prepared to follow up with the actual names (Reba McEntire, Dolly Parton, Lainey Wilson). If the follow-up story doesn't come, the poll is a conversational dead end. The arc doesn't include a follow-up frame for the poll result. Story arcs with interactive elements need a next-day follow-up response plan.

**Break 3 — The story arc has no plan for what happens if the minis generate significant booking DMs directly from story content.** Story reply volume was identified in the April 2026 calendar as something to monitor. If the "May 10–11" story generates 20 DMs asking about pony party booking, the Story Engagement Agent's handoff rules say those go to Comment + DM Response Agent — but the Response Agent's templates haven't been updated for this specific campaign context (the 2023 minis are named, there are specific dates). The handoff exists in theory but not in content.

**Break 4 — May 6 story uses TC dry humor ("The girls are not thinking about it") which is on-brand and correct — but the Approval Trigger for this arc requires Stacie to review the arc before any content is produced.** If Stacie's review doesn't happen by May 5, this story is uncleared 24 hours before it's planned. The arc is submitted for approval, but the system has no SLA for how quickly Stacie must respond to a story approval request.

**Verdict: PASS**

This is clean work. The arc structure respects the brand's no-urgency-pressure rule, the story-per-day cadence is realistic, and the "what this arc does not do" section demonstrates the agent knows where the brand lines are. The breaks are real but second-order — they are coordination failures, not execution failures.

---

## AGENT 9: COMMENT + DM RESPONSE AGENT

### What it produced:

**PRE-WRITTEN CAMPAIGN RESPONSE BANK — Mother's Day Pony Party**
*For deployment during March 22 – May 9 campaign period*
*All responses go to approval queue. None are sent without Stacie's review.*

---

**RESPONSE TYPE 1: Casual engagement on mini introduction posts**
*Sample trigger comment: "Oh my goodness she is SO cute!!"*

Classification: Casual Engagement — Tier 1
Drafted response: "She has opinions about that. We'll pass along the message."

Why this works: Warm, specific to TC's voice about these animals, no CTA, does not sound like a brand responding to a compliment.

---

**RESPONSE TYPE 2: Soft lead — "This would be so perfect for my daughter"**
*Sample trigger comment: "Reba! My daughter would absolutely love her."*

Classification: Booking Lead — Tier 3 (soft signal)
Drafted response: "Spring dates are open if you want to check availability. We're at tribalcowboy.com or send us a DM."

Note: Does not say "we'd love to have her" or "that sounds amazing." Moves toward action without performing excitement.

---

**RESPONSE TYPE 3: Direct booking inquiry via DM**
*Sample DM: "Hi! I saw your post about the mini horses and I want to book a pony party for Mother's Day weekend. How does it work and what does it cost?"*

Classification: Booking Lead — Tier 4
Drafted DM response:

"Good timing — May 10 and 11 are still open.

A few questions to make sure I give you the right information: How many kids are you expecting, roughly? And is this at your home, a park, or another venue?

From there I can tell you what to expect on our end and what the starting rate looks like. Everything — setup, the horses, cleanup — is handled by us."

**FLAG:** This response includes a reference to pricing ("starting rate"). Per response-guardrails.md Rule 2, pricing conversations move to DM. This response is already in DM — but the actual rate figure requires Stacie's approval before this template is finalized. The $XXX placeholder in offer-memory.md has never been filled in. This response cannot be completed until Stacie confirms the pony party starting rate.

---

**RESPONSE TYPE 4: "How much does a pony party cost?"**
*Comment or DM asking directly about price*

Classification: Booking Lead — Tier 4
Drafted response (comment version):
"DM us your date and a rough headcount and we can go from there."

Drafted response (DM version):
"The starting rate depends on your setup — headcount, location, duration. Send me your date, how many kids, and where you're thinking and I can give you a real number."

**FLAG:** Same $XXX problem as Response Type 3. The DM version promises "a real number" without knowing what that number is. This is a system gap that will cause real problems in the campaign. Pony party pricing is listed as "$XXX" in every system file. The Comment + DM Response Agent cannot do its job for this campaign until pricing is confirmed.

---

**RESPONSE TYPE 5: "Do you do [specific service they're describing that may or may not be what TC offers]"**
*Example DM: "Do you do pony rides where the kids can actually ride?"*

Classification: Booking Lead / Other — Tier 4/Other
Drafted response:
"That depends on what you have in mind. For our pony parties we do led walks and meet-and-greet time — the ponies are minis, so the experience is close-up rather than riding. What's the age range you're planning for?"

Note: Does not confirm or deny a specific service. Qualifies the inquiry before answering. Accurate to the offer-memory.md description.

---

**RESPONSE TYPE 6: Negative comment — "Prices seem high for just ponies"**
*Classification: Complaint (mild price pushback) — Tier 5 adjacent (but not a full complaint)*

Classification: Tier 3 — soft objection, not a complaint
Drafted response:
"The pricing covers the horses, the handlers, the setup, and the cleanup — it's a managed experience, not a rental. If you want details, DM us what you're planning and we can show you what's included."

What this response does not do: apologize, offer a discount, justify the price defensively, or argue. It states the value, moves to DM.

---

**RESPONSE TYPE 7: "Where are you located?"**
*Classification: Casual Engagement — Tier 2*

Drafted response: "We're based in Athol, Idaho — North Idaho. We travel for events throughout North Idaho and Eastern Washington."

---

**RESPONSE TYPE 8: "Are these ponies safe for really little kids?"**
*Classification: Casual Engagement / Booking Lead — Tier 2/3*

Drafted response: "We handle all the animal management — the kids are always guided. The minis in our spring rotation are three years old, and they've been working with handlers since they were young. If you have a specific age you're thinking about, DM us and we can tell you what to expect."

**FLAG:** This response claims the minis have been "working with handlers since they were young" — this may or may not be accurately reflected in available records. Escalate to Stacie for factual confirmation before this template is approved.

---

### Breaks found:

**Break 1 — The $XXX pricing gap is a direct campaign blocker.** Multiple response types require pricing information to function. offer-memory.md lists pony parties as "Starting at $XXX." CLAUDE.md lists pony parties as "starting at $XXX." The corporate-luxury-leads-agent.md lists corporate events as "Starting at $XXX per 2 hours." Every file with pricing has a placeholder, not a number. The Comment + DM Response Agent cannot write a functional Tier 4 booking response without knowing the starting rate. This gap will cause real leads to get incomplete responses or no response, and is the most operationally critical gap in the entire system for this campaign.

**Break 2 — Response Type 8 contains a factual claim ("the minis have been working with handlers since they were young") that requires verification.** The agent correctly flags this. The system has no mechanism for efficiently getting factual verification from Stacie for a pre-written template. The agent can write the flag but cannot resolve it. In real operation, this template would sit in a "needs verification" queue indefinitely unless there's a specific approval workflow for response templates.

**Break 3 — No response template exists for a scenario this campaign will definitely generate: someone who attended a TC pony party posting a public review, tag, or story.** When satisfied customers tag TC or post about their experience, the Response Agent's job is to respond warmly and specifically. But there is no template for "responding to positive user-generated content" and no guidance on what the TC response to a public tag looks like. This is not a complaint, not a lead, not casual engagement — it's a trust-building opportunity with no documented response framework.

**Break 4 — The response bank has no entries for Facebook-specific comment scenarios.** Facebook is a stated campaign platform. The comment/DM dynamics on Facebook differ from Instagram (more community-forward, slightly older audience per platform-rules.md). The pre-written bank is entirely Instagram-framed. At minimum, the Facebook booking post (April 29) will generate questions that need Facebook-native responses, not Instagram-repurposed ones.

**Verdict: NEEDS FIX**

The response quality itself is strong — the voice is right, the Tier classification system is working correctly, and the flags are accurate. The campaign-blocking issue is the pricing gap. Every Tier 4 response in this bank is incomplete until Stacie provides real starting rate figures.

---

## AGENT 10: WEBSITE + SEO AGENT

### What it produced:

**CAMPAIGN WEBSITE AUDIT & LANDING PAGE BRIEF**
*Campaign: Mother's Day Pony Parties | Launch date: March 22 | Traffic begins: April 14*

---

**URGENT AUDIT FINDING:**
Social content for this campaign begins directing traffic to www.tribalcowboy.com as early as Week 1 (March 23, Instagram bio link) and explicitly to the pony parties page as of April 22 (Stories) and April 29 (Facebook booking post). The pony parties page must be functional, current, and conversion-ready before the first CTA goes live.

**Current site status:** Unable to verify without live access. All recommendations below are based on the site structure described in platform-rules.md and the priority pages list in website-seo-agent.md. Actual implementation requires verification.

---

**WHAT THE PONY PARTIES PAGE MUST CONTAIN (before April 22):**

1. **Hero section:**
A real image of Reba, Dolly, or Lainey with a child (or alone if event photos don't exist yet). Not a generic horse photo. This page is launching alongside a campaign that has named these horses — the website image must match what social has established.

2. **Service description:**
What is included: the horses (specifically the 2023 minis, named), TC's setup and breakdown, animal handling, led walks and meet-and-greet time, optional instant photo delivery add-on.
What the host doesn't have to do: anything related to the horses.
Written in TC's voice — not "offering a unique and memorable equine experience for your child's special day."

**Draft page headline:**
"Reba, Dolly, and Lainey. Your next pony party."

**Draft subhead:**
"TC brings three 2023 mini mares to your event. We handle the horses. You handle the party."

**Draft body (excerpt):**
"Pony parties run through spring and fall in North Idaho and Eastern Washington. We bring Reba, Dolly, and Lainey — three mini mares born in 2023 who are at this point more comfortable around groups of children than most adults. TC manages setup, animal handling, and breakdown. The birthday kid gets the ponies. You get to actually be at the party.

Add instant photo delivery and every guest walks away with a photo of themselves with the horses, delivered instantly to their phone with a custom branded overlay."

**FLAG:** Body copy claims "more comfortable around groups of children than most adults." This may not be accurate for 2-year-old minis with limited event history. Requires Stacie's factual verification before going live. Same issue as the Comment + DM Response Agent flagged.

3. **What to expect (brief process description):**
How TC arrives, how the horses are introduced, how the session works, how breakdown happens. Reduce uncertainty — this is what corporate buyers call "vendor reliability." Families want it too.

4. **Pricing section:**
"Pony party rates start at [price] and vary by headcount, duration, and location. Send us your date and we'll put together the details." — This section cannot be completed until pricing is confirmed by Stacie. A "$XXX" placeholder cannot go live.

5. **CTA:**
One button: "Check availability" → contact form. Not "Book now." Not "Contact us for more information." "Check availability."

6. **Gallery:**
Real photos from TC pony parties. If no photos of the 2023 minis at events exist yet, use existing pony party photos and note in the site copy that Reba, Dolly, and Lainey are available for spring 2026 bookings.

---

**SEO BRIEF — Pony Party Page:**

Primary keyword: "pony party North Idaho"
Secondary keywords: "mini horse birthday party Idaho," "pony party Spokane area," "pony party Athol Idaho"
Long-tail target: "book a pony party North Idaho" — high intent, low competition, nobody in TC's radius is targeting this phrase

Meta title: Pony Parties in North Idaho | Tribal Cowboy LLC | Athol, Idaho
Meta description: TC brings Reba, Dolly, and Lainey — three mini mares — to birthday parties and family events in North Idaho and Eastern Washington. Full setup, animal handling, and cleanup handled. Check availability.

---

**CAMPAIGN LANDING PAGE RECOMMENDATION:**
A dedicated campaign landing page (tribalcowboy.com/mothers-day or similar) is not recommended for this campaign. The pony parties service page, properly updated with Mother's Day-specific language in the hero or a brief campaign note, is sufficient. A dedicated landing page creates an SEO split and requires maintenance beyond May 11. Update the service page. Don't create a new one.

---

**MISSING PAGE CRITICAL FOR THIS CAMPAIGN:**
The media/press/creator partnerships page does not appear to exist. This page is listed in website-seo-agent.md as missing and needed. It is relevant to this campaign because the Creator Income Agent will identify brand deal potential in the mini-mare content. Without a media page, any brand doing due diligence on TC sees nothing at the website level to validate the creator relationship. Recommend building a minimal version before April 21 (when the first corporate credibility TikTok goes up).

---

### Breaks found:

**Break 1 — The pony party page copy has the same unverified behavioral claim about the minis ("more comfortable around groups of children than most adults") that the Comment + DM Response Agent flagged.** This is now the third agent to encounter this problem. The system has no mechanism for sharing a factual verification flag across agents — each agent has to discover and flag the same false claim independently. A shared fact-verification queue or a note in horse-roster.md would prevent this from propagating through every output in the campaign.

**Break 2 — The Website + SEO Agent cannot verify the current state of the site.** The agent's mission is to audit the site — but without live access or a documented site inventory, it can only produce recommendations based on what the platform-rules.md and website-seo-agent.md files say should exist. If pages that are supposed to exist don't actually exist (broken links, missing pages), the agent has no way to know. A real site audit requires tool access (WebFetch or direct URL verification) that this agent should be using but was not in this simulation.

**Break 3 — The campaign landing page recommendation ("don't create a new page, update the existing service page") conflicts with a principle in website-seo-agent.md Rule 12:** "Every campaign landing page needs to be built before the campaign launches — not after the traffic is already arriving." The rule implies campaign-specific pages exist. The agent is arguing against following its own rule. The system instruction and the practical recommendation are in conflict, with no resolution guidance.

**Break 4 — The Media/Press page recommendation is marked as "needed before April 21" — but the agent cannot build it without Stacie's approval (it appears in the approval triggers list as "Media/press page before publication").** The recommendation and the approval requirement together create a tight window with no escalation path if Stacie doesn't engage before April 21.

**Verdict: NEEDS FIX**

The SEO strategy is sound, the landing page brief is actionable, and the decision not to create a separate campaign URL is defensible. The breaks are the same as the rest of the system: the behavioral claim about the minis, the absence of tool access for a genuine site audit, and a minor internal rule conflict.

---

## AGENT 11: CREATOR INCOME AGENT

### What it produced:

**CREATOR INCOME EVALUATION — Mother's Day Pony Party Campaign**
*March 22, 2026*

---

**Campaign angle for creator income:**
The 2023 minis (Reba, Dolly, Lainey) represent a new, high-frequency content asset that TC has not yet deployed publicly. A named-animal series built around three mini mares who look camera-friendly and carry a ready-made backstory (the country music naming) is exactly the type of recurring content lane that brand partners look for: predictable format, specific identity, repeatable.

**Creator income assessment for this campaign:**

**Opportunity 1 — UGC Package for Equine Care/Feed Brand (Strong Fit)**
The mini introduction series will produce 3–6 high-quality videos and 10+ photos of Reba, Dolly, and Lainey in natural light. A feed or supplement brand running a spring campaign could license this content as UGC without TC needing to post anything they wouldn't already be posting.
Deal type: Package A (Content Pack, no posting required)
Starting rate: $400–$800
Best targets: [To be researched by Trend + Market Intelligence Agent]
Timeline: Pitch outreach Week 2 of campaign (April 6–10) when the first mini introduction posts are live and can serve as spec work samples.
Flag: This requires at minimum 2–3 strong mini photos in the public feed before outreach. Don't pitch before the content exists.

**Opportunity 2 — Family Experience Platform Integration (Moderate Fit)**
Platforms that aggregate bookable family experiences have been expanding creator-adjacent partnerships. A TC pony party write-up or feature placement on a platform like this drives bookings while paying TC for the placement and/or content production.
Deal type: Editorial Integration or Commission
Assessment: Worth researching but not a proactive pitch yet. Monitor.
Flag for Trend + Market Intelligence Agent: Research which experience aggregator platforms (if any) are actively seeking equine/outdoor vendors in the Pacific Northwest.

**Opportunity 3 — instant photo delivery Direct Partnership (High Fit)**
TC is already using instant photo delivery technology. The pony party campaign will produce demo content showing the photo delivery system in action at an event. This is the strongest single creator income pitch TC has — it requires no additional content effort and TC is already the best possible case study for this specific product.
Deal type: Tier 1 (Long-term partnership) or Tier 2 (campaign-based)
Starting range: $1,500–$5,000 depending on deliverables and exclusivity
Action: Draft outreach for Stacie's review. This is the most time-sensitive and highest-value opportunity in the campaign window.
Timeline: Draft ready Week 3. Stacie reviews Week 4. Outreach goes Week 5.

**WHAT THIS CAMPAIGN CANNOT DO for creator income:**
- It cannot produce a spec portfolio for brand partners until real event photos exist
- It cannot generate paid deals before the content is live (pitch after the first mini posts go up, not before)
- It cannot include Indigenous identity as a deal-selling point without Stacie's explicit direction
- The $0 budget constraint is irrelevant to creator income — these deals require content quality, not spend

**Media kit update triggered by this campaign:**
The introduction of Reba, Dolly, and Lainey as named, public-facing horses should be added to the media kit. The mini-mare content lane is new. The media kit should reflect TC's content categories accurately. Coordinate with Website + SEO Agent when the media page is built.

---

### Breaks found:

**Break 1 — The instant photo delivery partnership pitch requires knowledge of instant photo delivery' current creator/partnership program, which the agent doesn't have.** The pitch is correctly identified as high-value, but the agent has no information about whether instant photo delivery actively runs creator partnerships, what their outreach process is, or whether TC's usage of the platform gives them leverage. This requires research (Trend + Market Intelligence Agent) before the pitch strategy is useful. The agent should have routed this to the Trend Agent before presenting it as an actionable timeline.

**Break 2 — The creator income strategy has a timeline gap: "Pitch outreach Week 2" for the UGC package assumes the first mini introduction posts are live and performing.** If the Business TikTok account reactivation (identified by the TikTok Growth Agent) hasn't happened by Week 2, there is no live spec content to reference in a pitch. The creator income timeline is dependent on a technical prerequisite that no one owns.

**Break 3 — The Creator Income Agent references the media kit but has no information about whether one currently exists or what it currently contains.** The memory files don't include a current media kit. The agent recommends updating it but cannot assess what needs updating versus what doesn't exist. A media kit that doesn't exist cannot be updated — it must be built from scratch, which is a larger scope task than the agent acknowledges.

**Verdict: NEEDS FIX**

The instant photo delivery opportunity identification is genuinely strong — this is the right call. The UGC package framework is solid. The breaks are about incomplete research before making timeline claims and a missing media kit that the system has been assuming exists.

---

## AGENT 12: CORPORATE + LUXURY LEADS AGENT

### What it produced:

**CORPORATE SPIN-OFF ASSESSMENT — Mother's Day Pony Party Campaign**
*March 22, 2026*

---

**Assessment summary:**
The Mother's Day pony party campaign is a consumer campaign. It is not a corporate campaign. However, the content it produces — particularly the mini-mare series, the pony party setup/execution documentation, and the instant photo delivery content — is the exact portfolio that wins corporate event inquiries.

**Corporate leads this campaign could generate (secondary, not primary):**

**1. Family Day corporate events (HR-driven)**
Companies with young employee demographics run spring family days. A Mother's Day pony party post seen by an HR coordinator at a company planning a May or June family event is a direct lead. The content does not need to be corporate-targeted — it just needs to be visible and professional.
Action: Ensure the Instagram and Facebook pony party content contains TC's website URL (not just "link in bio"). Corporate buyers Google. Make sure tribalcowboy.com/corporate-events is ready to receive that traffic.
Priority: Medium.

**2. Executive appreciation / premium family events**
High-net-worth individuals planning premium family events are not the same as birthday party parents. The mini mares introduced in this campaign are visually appealing and the TC brand is premium enough to attract this buyer — but only if TC's Instagram signals premium, not "kids birthday party."
Assessment: The campaign's current framing (no urgency, specific horse names, TC voice) is premium enough not to repel this buyer. No changes needed for corporate protection purposes.
Priority: Low — monitor for inbound signals, no proactive action.

**3. The content this campaign produces is a corporate sales tool.**
If a corporate event planner who already received a TC email or proposal visits TC's Instagram and sees the Mother's Day campaign content, they see: a professional operation with named, specific animals; an organized approach to events; and a brand that doesn't oversell. That's a trust signal.
Action: The April 21 TikTok Business post ("What TC's corporate clients get") is already in the calendar and serves this function. The Mother's Day campaign content does not interfere with corporate positioning if TC's voice stays consistent.

**What this campaign should NOT do for corporate positioning:**
- Do not reference Mother's Day in any content visible primarily to corporate buyers
- Do not let pony party framing bleed into the corporate events page
- The mini mares are consumer/family content. They are not the right face for TC's corporate pitch — that is the Clydesdales and instant photo delivery.

**Recommended proactive outreach (parallel to campaign):**
Spring corporate event season is March–May. Outreach to HR departments and event planners should be happening now, independent of the Mother's Day campaign. Target: real estate firms, financial services, tech companies in Coeur d'Alene area. Draft outreach email for Stacie's approval. This is separate from the Mother's Day campaign but the timing overlap is not a conflict — TC can book corporate events and pony parties simultaneously.

---

### Breaks found:

**Break 1 — The agent correctly identifies that the mini mares are "consumer/family content" and "not the right face for TC's corporate pitch" — but this creates a gap in content coordination that no agent is managing.** If a corporate buyer follows TC on Instagram, they will see the mini-mare introduction series in their feed. The Corporate + Luxury Leads Agent is saying this is fine ("the campaign's framing is premium enough not to repel this buyer") but it has no coordination mechanism with the Content Strategist or Brand Voice Agent to ensure the mini-mare content actually stays premium throughout the campaign.

**Break 2 — The recommendation to "ensure tribalcowboy.com/corporate-events is ready" is the third agent in this report to recommend verifying a website page without having tool access to verify it.** The Website + SEO Agent, the Social Content Strategist, and now the Corporate + Luxury Leads Agent are all independently flagging the same website verification need without any coordination. The system wastes output producing the same recommendation three times with no one accountable for the verification task.

**Break 3 — The proactive corporate outreach recommendation ("draft outreach email for Stacie's approval") is within this agent's scope and correct — but the agent does not name specific target companies, industries, or a timeline.** The corporate-luxury-leads-agent.md has a detailed tier-1 target list (tech companies, financial services, real estate, healthcare). The agent should have produced at minimum a shortlist of specific companies to approach in March–May, not a general recommendation.

**Verdict: NEEDS FIX**

The assessment is correct and the brand-positioning guidance (don't let pony party framing contaminate corporate positioning) is exactly right. The breaks are about missing specificity in the proactive outreach recommendation and the recurring website verification gap that no single agent owns.

---

---

# SYSTEM STRESS TEST REPORT

**Campaign:** Spring Booking Open — Mother's Day Pony Parties
**Test date:** March 22, 2026
**Agents evaluated:** 12 (Orchestrator + 11 production/specialist agents)
**Total outputs reviewed:** 12 agent outputs, 6 fully-drafted captions, 3 TikTok scripts, 2 full story arcs, 1 campaign calendar, 1 creative brief set, 1 SEO landing page brief, 1 creator income strategy, 1 corporate assessment, 1 response template bank

---

## TOTAL BREAKS FOUND

**Verdict summary:**
- PASS: 2 agents (Brand Positioning + Voice Agent, Story Engagement Agent)
- NEEDS FIX: 10 agents (every other agent)
- BROKEN: 0 agents

**Total documented breaks: 34**

Breaks by category:
- **Missing data in memory files:** 8 breaks (horse personality notes missing for all 2023 minis, $XXX pricing placeholders across all offer files)
- **Missing ownership/accountability:** 6 breaks (no owner for TikTok reactivation, no owner for website page verification, no owner for parallel workflow completion checks)
- **Internal rule conflicts:** 5 breaks (Orchestrator priority reclassification authority, Website + SEO campaign page rule vs. recommendation, Copywriter fabricating behavioral details to meet specificity standards)
- **Shared data propagation failures:** 4 breaks (the unverified behavioral claim about the minis appeared identically in 3 agents' outputs with no cross-agent resolution)
- **Missing coordination protocols:** 5 breaks (story arc to feed post synchronization, poll follow-up plans, account reactivation as campaign prerequisite, same-animal dual-account cadence)
- **Tool access gaps:** 3 breaks (Apify fallback protocol, no site verification access)
- **Timeline/approval window conflicts:** 3 breaks (pricing placeholder blocks Tier 4 responses, 24-hour approval window for date-specific content, story arc SLA undefined)

---

## THE 3 MOST CRITICAL FIXES

### Fix 1: Complete horse-roster.md with behavioral notes for Reba, Dolly, and Lainey immediately.

This is not a minor gap. It is the single issue that caused the most downstream failures in this stress test. Eight pieces of content — TikTok scripts, website copy, comment response templates, story content, Instagram captions — all hit the same wall: "what does Lainey actually do?" without an answer.

The system is built on specificity as the primary quality standard. Specificity requires facts. The facts about the 2023 minis don't exist in the system. Until they do, any agent that produces animal-specific content for these three horses is either fabricating details (which violates the truth standard) or producing vague copy (which violates the specificity standard). There is no good path without the data.

**What needs to happen:** Stacie provides one paragraph per horse for Reba, Dolly, and Lainey covering: temperament, one behavioral quirk or habit, how they respond to strangers or children, and one funny or surprising thing they've done. These notes go into horse-roster.md immediately. Every agent reads from there.

---

### Fix 2: Stacie must set real pricing and replace every $XXX placeholder in offer-memory.md before the campaign launches.

The Comment + DM Response Agent, the Website + SEO Agent, and by extension every booking-funnel piece in this campaign cannot function without actual pricing. The pony party starting rate, the corporate event starting rate, and the add-on pricing for instant photo delivery need to be documented in offer-memory.md with real numbers.

This is a non-trivial business decision that only Stacie can make — but it is also a non-negotiable prerequisite for the system to handle leads without embarrassing TC. "DM us for pricing" is acceptable as a holding response. "A real number" (as the response template promises) is not something the system can deliver if the number doesn't exist in the system's memory.

**What needs to happen:** Stacie reviews offer-memory.md and replaces all $XXX instances with actual figures (or with a confirmed "pricing available upon request" decision for those services where that is the deliberate strategy). The Comment + DM Response Agent and Corporate + Luxury Leads Agent are blocked until this is done.

---

### Fix 3: Create an "ownership registry" — a shared file that assigns a responsible agent or Stacie to every prerequisite task.

This stress test revealed six different cases where an agent produced a recommendation ("verify the corporate events page is ready," "reactivate the Business TikTok account," "confirm the pony party page is live") that no one was accountable for executing. Multiple agents independently flagged the same website page verification need. The TikTok reactivation — which blocks the entire TikTok campaign — was identified by the TikTok Growth Agent but handed to no one.

The Orchestrator's job is to prevent this. But the Orchestrator's handoff rules only cover agent-to-agent creative handoffs, not the operational prerequisites that fall to Stacie directly.

**What needs to happen:** Build a simple `current-tasks.md` or `prerequisite-registry.md` file in the TribalCowboy-Social root that lists: task, owner (agent or Stacie), deadline, and status. The Orchestrator maintains this file and clears tasks before green-lighting the next production phase. Without this, the system will continue to produce 12 independent recommendations for the same unowned task.

---

## THE 2 AGENTS THAT PERFORMED BEST

### Best Agent 1: Brand Positioning + Voice Agent

The preliminary voice guidance for the 2023 mini introduction was specific, correct, and immediately usable. The audit sample was technically precise. The Indigenous identity framing guidance was handled with exactly the right level of care — it said what not to do and why, and it correctly identified that this campaign doesn't require that territory at all. The agent is doing exactly what a brand guardian is supposed to do: protecting the voice before errors reach the Stacie approval queue, not after.

The difference between this agent and the others: it has the clearest, most enforceable standards in the system, and it applies them consistently. Every other agent produces recommendations. This agent produces verdicts.

### Best Agent 2: Story Engagement Agent

The story arc was the most fully realized single output in this test. It knew when to post and when not to. It understood the relationship between story content and feed content. It used TC's humor correctly — dry, observed, grounded in real behavior. It produced a "what this arc does not do" section without being prompted, which is exactly the kind of self-auditing the system needs more of. It also correctly triggered its own approval requirement without waiting to be asked.

---

## THE 2 AGENTS THAT PERFORMED WORST

### Worst Agent 1: Orchestrator

Not because the routing was wrong — the routing was largely correct. But the Orchestrator self-violated its own core rules in the process: it reclassified campaign priority without Stacie's authorization (violating Rule 2), it launched a parallel multi-agent workflow with no mechanism to confirm completion (violating Rule 8), and it attempted to resolve an approval trigger conflict (date-specific content) without escalating it to Stacie. The agent that is supposed to be the system's rule-enforcer is the one with the most rule violations. This is a structural problem: the Orchestrator's rules are written as prohibitions but not as procedures. Prohibiting a behavior without specifying the alternative leaves the agent defaulting to judgment calls it's not authorized to make.

### Worst Agent 2: Copywriter Agent

The voice quality of the actual copy is strong — Drafts 1, 2, 4, and 5 are genuinely good. But the Copywriter committed the one failure the system is built to prevent: it wrote behavioral claims about Lainey that are not sourced in the verified memory files. Hook option A for the Lainey TikTok ("She has already decided she owns this property") and Hook option C ("Two-year-old mini horse. Three-year-old attitude") are written with the specificity the brand demands — but they are invented specificity. The system's quality standard is "specific AND true." The Copywriter produced specific OR true, which is the wrong tradeoff. When the data doesn't exist, the Copywriter's escalation trigger says flag it. The agent partially flagged it (the body copy placeholder) but wrote the hooks anyway. The hooks are the most public, highest-visibility part of the content. That's where the invented detail causes the most damage.

---

## ONE THING THIS SYSTEM DOES THAT NO GENERIC SOCIAL MEDIA STRATEGY DOES

Most social media systems treat brand voice as a style guide. TC's system treats brand voice as the last line of defense before brand damage. Every other agent in the system — the Strategist, the Copywriter, the TikTok Growth Agent — produces output in TC's voice and has rules about that voice. But only one agent exists specifically to catch the other agents when they slip: the Brand Positioning + Voice Agent, which sits between every piece of creative output and Stacie's approval queue, holds a specific banned-phrase list that has been tested against real TC failures, and is explicitly prohibited from passing anything that "sounds like it was written by a marketing agency." No generic social media system has this. Generic systems use a style guide as reference material. TC's system uses a Brand Voice Agent as an active gatekeeper — and the gatekeeper has teeth: it can rewrite, return, or escalate to Stacie, but it cannot approve something that fails. The system distinguishes between voice drift (gradual, invisible, catastrophic for a premium brand) and voice failure (acute, detectable), and it has infrastructure for catching both. That is not a common design.

---

## RECOMMENDED NEXT ACTIONS (priority order)

1. Stacie: Add behavioral notes for Reba, Dolly, and Lainey to horse-roster.md — before any animal-specific content for these three is drafted or published
2. Stacie: Replace $XXX pricing placeholders in offer-memory.md with real numbers — before the campaign's Tier 4 comment/DM responses are deployed
3. Stacie: Reactivate @Tribal_Cowboy Business TikTok (profile photo, bio) — before March 23 if the first campaign TikTok post goes out that week
4. Orchestrator: Create a prerequisite-registry.md file and populate it with all unowned campaign tasks
5. Orchestrator: Define a parallel workflow completion protocol — what constitutes "done" for agents 1, 2, and 3 before agent 4 begins
6. Copywriter Agent: Add "cannot write behavioral claims for any horse with [ADD] status in horse-roster.md" as an explicit escalation trigger
7. Brand Positioning + Voice Agent: Add a third status tier — "Approved pending one-line revision" — with a documented process for who makes the revision
8. Website + SEO Agent: Verify current state of tribalcowboy.com/pony-parties and tribalcowboy.com/corporate-events before April 14

---

*Report generated: March 22, 2026*
*System version: Tribal Cowboy Social Media OS — 13 agents*
*Campaign status: Pre-launch — no content has been published*
*Filing location: `/Users/staciehuffhines/TribalCowboy-Social/insights/campaign-stress-test-march2026.md`*
