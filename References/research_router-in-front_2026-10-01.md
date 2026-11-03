# Research Note -- The Router in Front (Jev in front of Grok Bot)
For: **Sat 10 Oct 2026** (moved from Sat 3 on his word, 2 Oct), `substack_draft_<slug>_2026-10-10` · Depth: quick-to-medium · Date: 2026-10-01
Basis: his word 28 Sep that he has run it, shadow AND active. **His run is the piece. Nothing below substitutes for it.**

## Bottom line
- The recipe is verified at source and matches the 20 Sep mirror transcription word for word. Steps 6 and 7 (shadow first, read the logs, a kill switch, humans keep irreversible actions) are the usable half.
- Jev itself is footed at TypeSafe's own launch post: 15 Sep 2026, early access, $0.042 per million input tokens, output free. **The launch-date DO-NOT-PRINT is resolved** (15 Sep, at primary). Fri 25 already printed the date and price, so they are a callback here, not news.
- The speed and cost multiples are TypeSafe's own, and **TypeSafe itself says its evals "are on the higher end of real world gains"**. That vendor caveat is printable and more honest than any of the secondaries.
- The best counter-evidence is one builder's shadow log: Jev as a skill router for a strong model got 3 of 6 real prompts wrong, and the author concluded a weaker judge was advising a stronger one. Use it as the reason shadow mode exists.

## What's solid
- **The post, at x.com (Chrome, read 1 Oct 2026):** @0xCodila, Sat 19 Sep 2026, 3:09 PM PT. Text identical to the intake note's mirror copy, including "2028" and "install it as soon as possible". Quote-tweets his own 18 Sep article "Jev Engineering: Full 10-Step Roadmap...". Engagement now ~381.7K views, ~5.6K bookmarks (moves; do not print as fixed). [https://x.com/0xCodila/status/2101433560796467348]
- **Jev, at primary:** "Sep 15, 2026", by "Diogo Almeida, founder, TypeSafe"; "available today in early access"; developers brought "off the waitlist as quickly as we can"; "$0.042 / MTok ($42 per billion tokens)" input, output "FREE (too cheap to meter)"; end-to-end "70ms-500ms"; returns type-safe structured values with "calibrated probabilities and confidence scores"; Jev "gives up string generation". [https://typesafe.ai/blog/introducing-system-one-models-and-jev]
- **The router pattern exists as public code**, independent of the post: `colinmcdermott/grok-jev-router`, tagline "Jev decides, Grok Bot executes, humans control irreversible actions." Four actions: `proceed`, `dry_run`, `ask_human`, `skip`. Starts in shadow mode to "compare what Jev said with what the bot did before anything depends on it". Hard-coded rules override Jev for money-spending, critical-risk, irreversible, looping or low-confidence cases and send them to a human. Daily JSONL logs in `logs/`; `config.json` holds `enabled` and `mode` (shadow/active); kill switch `python3 router.py off`. Measured 20 Sep: ~536-580 ms per decision, ~$0.000046 per call, jev 1.13.0. No affiliation stated. [https://github.com/colinmcdermott/grok-jev-router]
- **The counter, at primary:** `shimo4228/jev-skill-router` (Claude Code plugin, shadow by default: "records what it would have suggested and injects nothing"). 21 Sep, jev-1.13.0: scripted single-intent 6 of 6 sensible; real session with 50-59 skills, 3 sensible and 3 wrong of 6. Conclusion: "a weaker judge advising a stronger one that already sees the same descriptions." [https://github.com/shimo4228/jev-skill-router]

## What's contested / watch out
- **Who wrote the pattern first.** Step 7's wording and the colinmcdermott tagline are nearly identical. Which came first is not established. Do not say the post copied the repo or the other way round. The post's "repo below" link was not resolved.
- **The recipe is being cloned.** A search result shows @maestrooth posting a near-identical recipe ("takes just 5 minutes"). Seen only as a search-result title, not read at source. If used, re-read it first. It fits the "six clones in 48 hours" story from the 21 Sep brief (secondary, The Anthropic Stack).
- **"Calibrated" is TypeSafe's word.** Secondaries (The AI Corner 21 Sep; Neha Kabra, 26 Sep brief) argue confidence is not accuracy. Fair framing, but secondary. Do not foot the calibration point to them. His own logs are the better evidence.
- **The poster's interest is undisclosed.** Bio: "AI - researcher & coder | writing about what I use myself". Print nothing about motive.

## Couldn't verify
- Any independent benchmark of the 193.6x / 444.6x (or the rounded "200x / 400x"). None found. `Suryals/jev-router-lab` intends a Jev vs Qwen3.8-27B vs Claude Sonnet 5 shadow eval but has **no results** (10 synthetic alerts, marked not to be trusted).
- Firecrawl is broken in this session (client-side schema error, also seen in the 27 Sep work brief). x.com was read through his Chrome instead. Update `reference_x_com_via_firecrawl.md`.

## The economics
- Price: $0.042 per million input tokens, output free (primary). One builder measured about $0.000046 per routing call, roughly 22,000 decisions for a dollar (that is my arithmetic on his figure).
- The real cost question for a personal bot is not the router's price. It is the price of the expensive things the router stops (an unneeded browser session, a research fan-out, a retry loop, a spare bot) and the price of one wrong `proceed`. **His logs are the only numbers that count here.** Ask him for: shadow agreement rate, how many calls it diverted, a wrong call it would have made, and what the bill did after he turned it active.

## Drop-in facts
- "On 15 September TypeSafe put Jev into early access" -- already printed Fri 25. Callback only. [typesafe.ai blog]
- TypeSafe's own caveat: its workflow evals "are on the higher end of real world gains". [typesafe.ai blog]
- Four lanes: proceed, dry run, ask a human, skip. [colinmcdermott/grok-jev-router]
- One builder's shadow run: 3 of 6 real prompts routed wrong; "a weaker judge advising a stronger one". [shimo4228/jev-skill-router, 21 Sep]

## DO NOT PRINT (binds every rv of Sat 3)
- 200x / 400x or 193.6x / 444.6x as fact. Attribute them to TypeSafe with its own caveat, or leave them out.
- Anything from Linas's paywalled guide.
- The poster's motive; follower or view counts as fixed figures.
- Who-copied-whom between the post and the repo.
- Suryals' lab as a result (it has none).

## Spent / collision watch (window was 26 Sep to 10 Oct; RE-RUN for 3 to 17 Oct now that it is Sat 10)
- Fri 25 printed Jev's date and price. Do not re-announce.
- Sat 26 images only: bouncer/door, layer one/two, widget, ten-then-five, fireworks. **Step-by-step build and caution guidance (shadow first, test each step, checkpoints, humans keep irreversible actions) are NOT a collision: his ruling 1 Oct 2026, "they are prudent usage". Use them freely.** Verbatim reuse is still called out: do not reprint Sat 26's exact wording ("one step at a time", "stop for me to test after each", "save a checkpoint every time a step works").
- Mon 28 "the line" and the dashboard image (Mon/Tue).
- Sat 19 "control plane". It is out of the 7-day window, but the router sits in the same mental slot, so do not rename it as one.

## Angles this opens
- Callback to Sat 19's promise ("we will come back to [Grok Bot] now that I have further pushed the edges") and Sat 26's printed "next week ... Grok Bot". Both are discharged.
- Sun 4 craftsmanship spine: the router is a check per unit at the cheapest price there is, and shadow mode is craft before volume. Hand Sunday the line. Do not spend it on Saturday.
- Vault signal "Two visions for agentic routing" (small local model calling up). He now has a lived answer.

## ADDENDUM 9 Oct 2026 (Sat 10 day chat) -- OpenAI Decisions API, footed at primary
- Guide: https://developers.openai.com/api/docs/guides/decisions (read 9 Oct via Firecrawl, live). Three question types: `predicate` ("probability: an estimate from 0 to 1 that the condition is true"), `choice` (one of your supplied values, with probabilities and a confidence field), `score` (ordered levels; "the probability-weighted average of the level indices", so it "can fall between levels"). "Each question can use a different type." Text and image input (images inline base64 only). Refusal is a returned answer type. Pricing: "With gpt-6-luna, input costs $0.10 per 1M tokens. You pay only for input tokens"; regional/long-context multipliers apply. ZDR and HIPAA for eligible customers.
- Availability: public beta for all developers, community announcement 6 Oct 2026 (community.openai.com/t/.../1403877, posted by a community "Leader", not confirmed staff; the guide is the primary). Speed claim "up to 10x faster than GPT-6 Luna through the Responses API" is OpenAI's own; print only as the seller's claim.
- Firecrawl WORKS again in this session (scrape and search, 9 Oct). The 30 Sep breakage is cleared here.
- DO NOT PRINT: the 10x figure as fact; any Decisions-vs-Jev quality verdict (none measured).

## ADDENDUM 9 Oct 2026, 15:14 (Sat 10 day chat) -- Jev vs Decisions API: images
- **His point (9 Oct, his words):** "The biggest difference between Jeff [Jev] and the Decisions API is that the Decisions API can actually look at an image and give you a score on the image, whether it's yes/no, a rubric, whatever else. It can do that against images, whereas Jeff can only do text."
- **Footed both sides at primary, 9 Oct:**
  - Decisions API takes text AND image input (images as inline base64 data URLs only; hosted URLs and file_id not supported); predicate / choice / score all apply. [developers.openai.com/api/docs/guides/decisions]
  - Jev is text-only for now. TypeSafe's launch post: inputs are "Unstructured data (e.g. text) with an emphasis on structured program state" and "The demo is on structured state as a data structure with text, not on images (yet…)". [typesafe.ai/blog/introducing-system-one-models-and-jev]
- **Proposed line (offered, NOT placed; he is editing the Doc himself):** "The difference that matters to me is that the Decisions API can look at an image and score it, whether that is a yes or no, a rubric, or whatever else you set up. Jev only does text, at least for now; TypeSafe's own launch post says its demo is 'not on images (yet…)'."
- **Placement suggested:** the Decisions [YOUR TAKE] slot in "A second reader, and a bigger field".
- **Print rule:** say "only text, at least for now" or quote TypeSafe's "(yet…)". Never print "Jev cannot do images" as a permanent fact.
