# How often do the writers Lars follows publish, and how long are their pieces?

Prepared 2026-09-27. Sources: Gmail metadata (60 days) plus each publication's own Substack archive (API or archive page). Message bodies were not opened, and nothing in Gmail was changed.

## Method in brief

- **Inbox list.** Gmail query `from:substack.com newer_than:60d -from:no-reply@substack.com -from:larsklander@substack.com`, paged to the end: **615 threads from 137 sender publications** (Jul 30 to Sep 28). `pub+section@` was folded into `pub`, and `reaction@mg1` was dropped.
- **Read/important signal.** Per publication I counted threads that were READ (no UNREAD label), IMPORTANT or STARRED. Score = 3×starred + 2×read + 1×important. It is a relative ranking only.
- **Set measured.** Every publication with 4+ emails, plus Mollick, Nate, Lenny, Linas, Every, HCR and Krugman: 44 candidates. **27 were measured and 17 were UNREACHED.** Substack returned HTTP 429 or a robots.txt rate limit repeatedly on `*.substack.com`, even with pauses of several minutes. Custom domains mostly worked.
- **Cadence.** Cadence is posts per week over the span of posts I could retrieve, up to 90 days. For most publications the fetch tool only returned the latest ~12-16 posts, which is 1-8 weeks for frequent publishers. The window used is noted in each row.
- **Word counts.** "Median words" is Substack's `wordcount` field, ignoring posts under 50 words (video or audio stubs). Where only the HTML archive page loaded, there is no wordcount ("n/a").
- **Words per week** = posts/week × median words. **This is an estimate.**

## Table (sorted by read/important signal)

Signal legend: S = starred, R = read, I = important (counts of threads in 60 days).

| # | Publication (sender) | Author | Posts/wk (window) | Median words | Format mix / paid share | Inbox emails 60d | Signal (S/R/I → score) |
|---|---|---|---|---|---|---|---|
| 1 | Nate's Newsletter (natesnewsletter) | Nate B Jones | ~3.8 (Sep 7-22; Jul 2-13 sample the same) | 4,405 | All "podcast" type (audio plus full written essay), incl. weekly "Executive Briefing"; 100% paid/founding | 16 | 1/5/11 → 24 |
| 2 | Ken Huang (kenhuangus) | Ken Huang | 7.0 (Sep 12-26) | 2,903 (many 7-9k) | All written; 73% paid | 14 | 3/5/2 → 21 |
| 3 | Opinion AI (opinionai) | n/a | 5.8 (Sep 10-27) | 2,501 | 14 written + 1 short audio; 93% paid | 11 | 2/4/5 → 19 |
| 4 | AI blew my mind (aiblewmymind) | n/a | 1.4 (Jul 16-Sep 24) | 3,255 | All written; 53% paid | 9 | 2/5/1 → 17 |
| 5 | How to AI (ruben) | Ruben Hassid | 1.9 (Apr 30-Jun 24; **stale cache**) | 1,717 | All written, free | 4 | 2/3/4 → 16 |
| 6 | Lenny's Newsletter (lenny) | Lenny Rachitsky | 0.9 written essays (11 in 90d); podcast episodes on top (not in archive view) | n/a | Weekly essay plus podcast and How I AI episodes | 15 | 1/4/5 → 16 |
| 7 | Build to Launch (buildtolaunch) | n/a | 1.6 (Jul 27-Sep 26) | 4,545 | All written; 87% paid | 6 | 1/3/6 → 15 |
| 8 | LearnAIWithMe (gencay) | Gencay | 4.1 (Sep 4-28) | 949 | All written; 73% paid | 11 | 2/1/6 → 14 |
| 9 | excellentprompts | n/a | UNREACHED | n/a | n/a | 20 | 0/6/2 → 14 |
| 10 | Smart Prompts For AI (smartpromptsforai) | n/a | 12.8 posts (Sep 22-28), about 7 written + 6 audio | 870 (written ~1,200; audio ~600) | 50/50 written and podcast; written posts paid | 34 | 1/4/2 → 13 |
| 11 | theaicorner1 | n/a | UNREACHED | n/a | n/a | 21 | 1/2/4 → 11 |
| 12 | AI Supremacy (aisupremacy) | Michael Spencer | 3.0 (Sep 11-25) | 2,146 | All written; 100% paid | 5 | 1/2/4 → 11 |
| 13 | The Agent Stack (agentstackai) | n/a | 2.8 (Aug 25-Sep 27) | 1,660 | All written; 21% paid | 6 | 2/1/2 → 10 |
| 14 | Linas's Newsletter (linas) | Linas Beliūnas | ~6 (11 posts Aug 5-17; partly stale) | n/a | Written | 4 | 1/1/4 → 9 |
| 15 | Letters from an American (heathercoxrichardson) | Heather Cox Richardson | ~7 letters/wk; 2-2.5 posts/day incl. video/chat stubs (Jul 4-10 and Aug 26-30 samples) | ~1,450 (letters) | ~1 letter/day plus daily video; free | 23 | 0/0/9 → 9 |
| 16 | The AI Leadership Edge (theaileadershipedge) | n/a | ~3 (11 posts Jul 12-Aug 6; stale) | n/a | Written | 8 | 0/1/6 → 8 |
| 17 | The Pragmatic Engineer (pragmaticengineer) | Gergely Orosz | 2.9 (Aug 26-Sep 24): about 1 Pulse, 1 deep dive and 1 podcast each week | n/a | Mixed written and podcast | 8 | 1/2/1 → 8 |
| 18 | ainutpam | n/a | UNREACHED | n/a | n/a | 5 | 1/2/1 → 8 |
| 19 | Sabrina Ramonov (sabrinaramonov) | Sabrina Ramonov | 2.2 (Aug 12-Sep 26) | 983 | All written, free | 6 | 0/2/3 → 7 |
| 20 | theslowai | n/a | UNREACHED | n/a | n/a | 8 | 0/0/6 → 6 |
| 21 | The Argument (theargument) | multi-author magazine | 6.5 (Sep 12-27) | 2,202 (two features 15-18k) | All written; 47% paid | 16 | 0/1/4 → 6 |
| 22 | Code Like A Girl (codelikeagirl) | multi-author | 3.0 (Aug 26-Sep 25) | 1,978 | All written, free | 6 | 0/1/3 → 5 |
| 23 | theanthropicstack, emergingai, aiagentssimplified | n/a | UNREACHED | n/a | n/a | 9 / 13 / 9 | → 5 each |
| 24 | The AI Maker (aimaker) | n/a | 3.1 (Jul 12-28; **stale cache**) | 3,412 | 5 written + 3 podcast; 38% paid | 14 | 0/1/2 → 4 |
| 25 | theaibreak, opencloudai, exploringchatgpt, endlessurgency, aigeniuslab | n/a | UNREACHED | n/a | n/a | 6 / 11 / 8 / 12 / 6 | → 4 each |
| 26 | One Useful Thing (oneusefulthing) | Ethan Mollick | **0.3** (4 posts in 90 days; 15 posts in 10 months) | 1,856 | All written, free | 1 | 0/1/1 → 3 |
| 27 | Why Try AI (whytryai) | Daniel Nest | 2.1 (Aug 16-Sep 24): 1 essay + 1 "Sunday Rundown" roundup each week | n/a | Written, half link roundups | 4 | 0/0/2 → 2 |
| 28 | Drop Site News (dropsitenews) | newsroom | 12.2 (Sep 19-27) | 2,787 | Written reporting, free | 9 | 0/0/2 → 2 |
| 29 | Transformer (transformernews) | Shakeel Hashim | 3.2 (Aug 28-Sep 25) | 2,885 | All written, free | 5 | 0/0/1 → 1 |
| 30 | Paul Krugman (paulkrugman) | Paul Krugman | ~7 (11 posts Aug 31-Sep 10, incl. ~2 videos/wk) | n/a | Mostly written plus video | 10 | 0/0/1 → 1 |
| 31 | Understanding AI (understandingai) | Timothy B. Lee | 1.1 (14 posts in 90d) | 2,594 | Written; 60% paid | 8 | 0/0/0 → 0 |
| 32 | The Borowitz Report (borowitzreport) | Andy Borowitz | 5.8 (Sep 9-27) | 137 | Short satire; 19% paid | 8 | 0/0/0 → 0 |
| 33 | Every (every.to, not Substack) | multi-author (Dan Shipper et al.) | ~7.8 (20 posts Sep 8-25) | n/a | Written, several columnists | 0 (not via Substack) | n/a |
| 34 | aigoldrushh, artificialcorner, amerex, aitechin, tmindset, alesiazakharova | n/a | UNREACHED | n/a | n/a | 5-6 each | 0-3 |

## Findings

**1. Cadence buckets (the 27 measured publications).**
- **5+ per week: 10.** Drop Site, Smart Prompts, HCR, Ken Huang, The Argument, Opinion AI, Borowitz, Krugman, Linas, Every.
- **2-4 per week: 11.** LearnAIWithMe, Nate, AI Maker, AI Supremacy, Code Like A Girl, Transformer, Pragmatic Engineer, Agent Stack, AI Leadership Edge, Sabrina Ramonov, Why Try AI.
- **About weekly (1-2 per week): 5.** AI blew my mind, Build to Launch, How to AI, Understanding AI, and Lenny (written essays).
- **Less than weekly: 1.** Mollick.

**2. Few long-form writers publish daily.** Nine publications have a median of 2,500+ words.
- **Daily or near-daily: 3.** Only three of the nine publish long pieces daily or near it: Ken Huang (7/wk, ~2.9k, mostly paid), Opinion AI (5.8/wk, ~2.5k, 93% paid), and Drop Site, which is a staffed newsroom.
- **Two to four times a week: 4.** Nate (~4/wk at ~4.4k) is the heaviest single-author long-form voice here. Transformer, AI Supremacy (at 2,146 words it is not quite 2,500) and AI Maker also sit in this band.
- **About weekly or less: 4.** Build to Launch (4.5k), AI blew my mind (3.3k), Understanding AI (2.6k) and Mollick (1.9k at 0.3/wk).

**3. Words per week (estimates: posts/week × median words).**

| Publication | Est. words/week | Note |
|---|---|---|
| Drop Site | ~34k | multi-author newsroom |
| Ken Huang | ~20k | |
| Nate B Jones | ~17.5k | |
| Opinion AI | ~14.5k | |
| The Argument | ~14.5k | multi-author |
| Smart Prompts | ~11k | |
| AI Maker | ~10k | |
| HCR | ~10k | letters only |
| Transformer | ~9.4k | |
| **Lars** | **~24k** | **estimate: 7 × ~3,500** |

Lars's ~24k words a week is more than every single-author publication measured. Only a staffed newsroom writes more. At his length, he is also above Nate's pace.

**4. The pattern.** Daily writers who stay daily at scale mostly write **short or formulaic** pieces:
- satire (Borowitz ~140 words);
- prompt packs (Smart Prompts ~900 to 1,200; LearnAIWithMe ~950);
- a single diary-style letter (HCR ~1,450).

Alternatively, they are **multi-author outlets** (The Argument, Every, Drop Site). **Long-form essayists are mostly weekly or 2-4 a week.** The two daily long-form single-author exceptions (Ken Huang, Opinion AI) are almost entirely paywalled. A common structure among the 2-4 a week group is **one flagship essay plus one lighter format**:
- Why Try AI: essay plus Sunday Rundown;
- Pragmatic Engineer: Pulse plus deep dive plus podcast;
- Lenny: essay plus podcast.

**5. What Lars reads most.** The four highest-signal publications (Nate, Ken Huang, Opinion AI, AI blew my mind) publish between 1.4 and 7 times a week at 2.5-4.4k words. **Nate at ~4 a week** is the closest model of a high-signal, long-form, non-daily cadence. Mollick, whom Lars cites often, publishes roughly **once a month**.

## Methodology limits (read before relying on these numbers)

- **Inbox volume is not publishing cadence.** Emails can be section-specific (`+podcast`, `+deepdives`) or skipped posts, and threads can be deleted or archived. Lenny's podcast episodes and Krugman's videos, for example, were counted differently in the inbox and in the archive.
- **Short windows.** Rates for high-volume publications come from 1-4 week windows, not the full 90 days, because the fetch tool returned only ~12-16 posts per call and paging was blocked by rate limits. A few views were **served stale from cache** (HCR in July, AI Maker in July, How to AI in April-June, Linas and AI Leadership Edge in parts of July-August). They show those publications' normal cadence, not the latest 90 days.
- **Wordcount gaps.** Substack's `wordcount` was missing wherever only the HTML archive page loaded (Lenny, Pragmatic, Linas, Krugman, Every, Why Try AI, AI Leadership Edge). For paid posts, it reflects the full post as Substack records it. Nate's posts are typed "podcast" but carry full essay-length text.
- **17 of 44 candidates are UNREACHED.** These are mostly the high-volume prompt and tool newsletters: excellentprompts, theaicorner1, emergingai, endlessurgency, opencloudai, and others. Their cadence is unknown; the inbox counts are the only evidence.
- **The read/important signal is noisy.** Gmail's IMPORTANT label is set automatically, and some "read" threads may have been opened only to forward. Treat it as directional.
