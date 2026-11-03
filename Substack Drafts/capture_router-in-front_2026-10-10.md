# Interview Capture -- The Router in Front (working title)
Thread: personal AI / Grok Bot build · Beat: shadow mode before cutover · Date: 2026-10-09 · Slot: Sat 10 Oct
STATUS: Round 1 captured (his four bot reports, 26 Sep to 6 Oct, pasted 9 Oct). Round 2 open.

## ⚠️ The plan block is stale (finding)
- Plan says: Jev as an action router in front of Grok Bot, four lanes (proceed / dry run / ask human / skip), "run in shadow and then live".
- His build is: Jev as a **first-pass scorer** (KEY vs noise, 0.5 cutoff) across six inboxes, written ahead of the Inbox bot's morning read. **Still in shadow. Not live.** Earliest cutover review Mon 19 Oct, his call.
- So: "then live" cannot be printed, the bill-after-live question does not apply, and the four lanes are the public repo's, not his. The piece is shadow mode and the bar you set before you let it act.

## The take (one sentence, drafter's, his to change)
The model was never the hard part; shadow mode is where you find out what you actually meant by "important", and you write the bar down before you let it act.

## Meat (Pass 1) -- from his logs (bot reports, not his own words; do not quote as his voice)
- 26 Sep, first call: one call to jev-1.13 via OpenRouter, 354 ms, about $0.00002. Made-up newsletter scored 3% KEY, filed as marketing.
- 29 Sep: weekend backlog of ~1,370 messages scored, no errors, ~9 cents. First comparison vs the Inbox bot: v2 agreed about half the time, on only 27 matched emails. Inbox flagged receipts/invoices/payments; Jev scored them low. v2 marked every SQL "job failed" alert KEY -- 136 in one day; would have buried the digest. Scheduler misfiring: 2 of 12 planned runs happened (plumbing, not the model).
- 5 Oct, a clean shadow week: 5,408 emails, six inboxes, 14 runs, zero router or fetch errors, ~$0.72, median 155 ms. v3 marked 238 of 5,343 KEY (4.5%). Disagreement with the Inbox bot's blind baseline 6.2% (93.8% agreement on 1,477 matched) after ~5.7% the week before. Some of the gap is the baseline being wrong by his own 2 Oct rule.
- **The near-miss (strongest vein):** raising the cutoff 0.50 -> 0.55 would have cleared a class of crash-report noise, and would also have dropped a real person's request that scored exactly 0.50. Fix was wording in the question, not the threshold.
- 6 Oct, the bar: under 10% disagreement two weeks running (met: 5.7%, 6.2%), plus three conditions before cutover -- no coverage gaps for a full week (job-alert floods cutting fetches short in two inboxes); two weekly reviews on the current rules; no missed human asks in a spot-check of what Jev called noise ("the expensive kind of miss"). Mailboxes read-only throughout.
- His ruling 9 Oct: "there's a fair bit of tweakiness in there too but its all use case specific so probably doesn't need to be in the write-up." -> The rule-by-rule tuning (SQL rule, Calendly, dSYM, receipts) stays out. At most the SHAPE: the disagreements were about what he meant, not what it read.
- Economics (my arithmetic): $0.72 / 5,408 = about $0.00013 per email, about 13 cents per thousand. The 29 Sep backlog ran cheaper per message (~$0.000066). Router cost is a rounding error; the real cost is one missed human ask.
- Callback available: Sat 12 printed "three Outlook accounts and three Gmail accounts every single day" and "a family of bots". Six inboxes matches.

## His rulings, 9 Oct
- **The one wrong call = the 0.50 near-miss** ("there's your 'one wrong call'"). A real person's request that a cutoff change would have thrown as noise. Name stays out.
- **Sun 4 Knight router: make it a DELIBERATE callback** (one clause; Knight's story is not retold).
- **Numbers source:** the four bot reports he pasted are the evidence. Print them as what the bot reported to him, not as independently measured. OpenRouter activity export is the optional cross-check on cost and call count.

## Why he built it (his words, 9 Oct -- VERBATIM, voice calibration)
- "inbox storms were a problem"
- "I get so many emails. That, even with what Inbox Manager was doing, it was still overwhelming my ability to actually see the key emails. I still wasn't getting stuff prioritized sufficiently unless it came from one of my two partners, which was doing name matching, not actual qualification matching."
- Drafter read: the old filter knew WHO mattered (two partners, by name) but not WHAT mattered. Jev's job is to judge the message, not the sender. (Note: Sat 12 printed the customer "key watch list" -- that is the same name-matching; callback available, and it is the thing being superseded.)

## Round 2 rulings, 9 Oct
- **The bar is HIS, all of it**: under 10% disagreement two weeks running; no coverage gaps for a full week; two weekly reviews on the current rules; no missed human asks in a spot-check of what Jev called noise.
- **He has spot-checked Jev's noise himself.** (Finding: one line owed.)
- **Artemis = his Grok Bot chief of staff. NAME IT** (his: "a more personal story about a more personal action, so attaching the name to the Grokbot makes a certain amount of sense"). Spelling: ARTEMIS (his, 9 Oct; "Artimus" was dictation). Removed from DO-NOT-PRINT.

## Argument stress-test (Pass 2) -- to run in round 2
- Best counterexample: 93.8% agreement is against another bot, not against him. Agreement is not correctness.
- Skeptic: "you built a spam filter." Answer owed (his).

## DO NOT PRINT
- Simone Kulas (named sender); "PE AU", "US PE"; "Barrel Update Players"; "Route 66 NEW TRIGGER OFFERS"; OK2PLAY; any customer, employer or mailbox name. Same rule as Sat 26 (names out of text, blurred in graphics).
- "Live", "cut over", or any post-cutover number. It is in shadow.
- Research-note DO-NOT-PRINT list still binds (TypeSafe multiples, Linas, poster motive, who-copied-whom, Suryals).

## Open questions for Lars (round 2)
- Why build it: what does the Inbox bot get wrong or cost you without a first pass?
- Whose bar: the bot proposed the three conditions; is "under 10%, two weeks" yours?
- Artemis: who or what, and printable?
- Did you do the spot-check of what Jev called noise yourself?
