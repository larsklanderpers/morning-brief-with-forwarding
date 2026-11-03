# Research Note -- Cheap Enough to Read Everything
For: Thu 15 Oct 2026 (week-plan_2026-10-12.md, Thu 15 block) · Depth: deep · Date: 2026-10-14

## Bottom line
The price point is SOLID at Anthropic's own pages: Haiku 5.5 (7 Oct 2026) is $0.10 / $0.50 per million input/output tokens for prompts up to 100,000 tokens, against $1 / $5 for Haiku 4.5. The "tenth" is the sticker; Anthropic's own footnote puts the average bill at "around 75% less", because the new tokenizer counts the same text as ~30% more tokens and long prompts pay 5x. The provenance half is NARROWER than the plan: Google's SynthID Detector (open to everyone 7 Oct) and OpenAI's verify page check images, video and audio only. **Nobody offers the public a text check.** Text, which is most of what a counterparty sends you, is the part provenance cannot yet help with. That limit is the honest centre of point 2.

## What's solid
- **Haiku 5.5 released 7 Oct 2026**, "designed for high-volume, cost-sensitive tasks ... summaries, compactions, database queries, and classification requests." [anthropic.com/claude-haiku-5-5]
- **Pricing, prompts up to / over 100k tokens:** input $0.10 / $0.50; output $0.50 / $2.50; cache reads $0.01 / $0.05. Haiku 4.5: $1.00 in, $5.00 out. [same; platform.claude.com/docs/en/about-claude/pricing]
- **Batch:** $0.05 in / $0.25 out per MTok up to 100k. [pricing page]
- **Footnote 2, verbatim:** "Claude Haiku 5.5 is priced 90% lower than Claude Haiku 4.5 for requests up to 100,000 tokens, and 50% lower for requests over 100,000 tokens. On Haiku 4.5, 90% of requests fell into the former category. This calculation also accounts for changes ... in how many tokens are used to complete a given piece of work: Haiku 5.5 has an updated tokenizer ... which means it uses slightly more tokens per task." Headline: "On average, it now costs around 75% less to run." [announcement]
- **Tokenizer, verbatim:** "the same input text produces approximately 30% more tokens on Claude Haiku 5.5 than on Claude Haiku 4.5. The exact increase depends on the content." Also: "Cost estimates made from Claude Haiku 4.5's token counts need recomputing." Large images: a 2,000x1,500 image "costs about 2.5 times as many visual tokens." [platform.claude.com/docs/en/models/haiku-5-5/migration-guide]
- **The 100k cliff, verbatim:** "a request over the threshold pays the higher prices even when part of its prompt is a cache hit." [pricing page]
- **Safeguards:** Haiku 5.5's cyber safeguards "permit a wider range of defensive tasks than our safeguards for Sonnet 5.5, but they still block penetration testing and other techniques more likely to be used by attackers." [announcement] -- relevant to the arc: the cheap model is shaped toward the defender's reading job, not the attacker's.
- **SynthID Detector open to everyone, 7 Oct 2026** (Pushmeet Kohli, Google DeepMind): "anyone can easily check if an image, video, or audio file was made with AI from Google or our partners, including OpenAI, NVIDIA, Kakao, and soon, Apple." Available "globally in English." Over 180 billion images and videos watermarked to date. [blog.google ... /synth-id-ai-content/]
- **OpenAI verify page:** checks images and audio for C2PA and SynthID; "does not currently support text verification"; text check by application only via the Content Provenance API. "No signal" can mean metadata stripped, watermark degraded, legacy model, or "another company's model, which the tool currently does not detect." C2PA "can be removed." [openai.com/research/verify/]
- **Claude text watermark:** detection API in **private preview**, for eligible organizations under EU law (regulators, media, researchers, obligated enterprises). Haiku 5.5 is watermarked. "A watermark can only determine that Claude was likely involved ... It cannot distinguish 'Claude wrote this' from 'Claude heavily edited this.'" [support.claude.com article 16266773; anthropic.com/news/claude-text-watermark; BleepingComputer quote]
- **EU AI Act Art. 50(2), verbatim (Commission AI Act Service Desk, consolidated text as at 27 Jul 2026):** "Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible ..."
- **Timing (Commission timeline page):** Article 50 applies 2 Aug 2026; 2 Dec 2026 is the "transitional deadline for certain providers ... already placed on the market before 02 Aug 2026, to comply with Article 50(2)." [ai-act-service-desk.ec.europa.eu timeline]

## What's contested / watch out
- **"1 million verification requests a day"** -- the 9 Oct brief attached it to the Detector. Google's text attaches it to the **built-in verification features in Search, the Gemini app, and Chrome**, not the Detector. Print it that way or not at all.
- **"Interoperable"** is the law's word; in practice each detector reads its own vendor family (SynthID covers Google + partners; Claude's marks need Anthropic's key; Microsoft and Meta run separate schemes per the 9 Oct brief, secondary). The gap between the statute's "interoperable" and the shipped tools is fair comment, attributed.
- **Feb 2027 interoperability date** appears only in a law-firm memo (Paul, Weiss). Not on the Commission page. DO NOT PRINT.
- **Sign-in requirement** for the Detector (Google, OpenAI or Apple account) -- Engadget via TNW, secondary. Optional colour; attribute if used.

## Couldn't verify
- Any independent (non-Anthropic) measurement of Haiku 5.5's real bill vs the 75%. Use Anthropic's figure, attributed, and name the interest (Anthropic sells the model).

## The economics (drafter's arithmetic from the published rates -- label as arithmetic, not a vendor claim)
- A 40,000-token contract read and summarized (2,000 tokens out) on Haiku 5.5: input $0.004 + output $0.001 = **about half a cent**.
- Same text on Haiku 4.5 (about 30,800 tokens under the old tokenizer; ~1,540 out): $0.031 + $0.008 = **about 4 cents**. Roughly 8x, not 10x, on this shape.
- A 130,000-token master agreement with schedules crosses the cliff: 130,000 x $0.50 = **6.5 cents in**. Still trivial in dollars, five times the per-token rate. Splitting it under 100k is the practical move.
- Batch halves all of it if the reading can wait.
- The cost that did not fall: the person who has to read the flag the model raises.

## Drop-in facts
- "Haiku 5.5 is priced 90% lower than Claude Haiku 4.5 for requests up to 100,000 tokens" / "On average, it now costs around 75% less to run." [Anthropic, 7 Oct 2026]
- "the same input text produces approximately 30% more tokens" [Anthropic migration guide]
- SynthID Detector: "anyone can easily check if an image, video, or audio file was made with AI from Google or our partners" [Google, 7 Oct 2026]
- OpenAI: verify page "does not currently support text verification." [openai.com/research/verify]
- Art. 50(2): outputs "marked in a machine-readable format and detectable as artificially generated or manipulated" ... "effective, interoperable, robust and reliable as far as this is technically feasible" [AI Act]

## DO-NOT-PRINT
- "1 million a day" attached to the Detector.
- Feb 2027 interoperability date.
- "Haiku 5.5 is a tenth of the price" without the bill caveat in the same paragraph.
- Any claim that Claude text can be checked by the public.
- Sat 10's six-thousand-emails figure or any per-week inbox cost.

## Angles this opens
- Sun 18: the defender's collapse is real, but the provenance half shows where it stops -- text. The rules re-priced for a tireless counterparty cannot lean on "we can tell what's machine-made" for text yet.
- Wed 14 callback (if Wed lands): the cheap model's safeguards permit the defender's reading and block the pentest. One clause, only if Wed 14 prints ARTEX.

## ADDENDUM 15 Oct 2026 -- OpenAI text watermark (his rv1 added it; footed)
- OpenAI, 5 Oct 2026, "Our approach to EU text provenance rules" (openai.com/index/eu-text-provenance/): "Over the coming weeks, we will add an invisible watermark to eligible ChatGPT and Codex text output in the European Union." EU only. Method: textGrain (technical report with UPenn and Yale).
- OpenAI, via TechCrunch 5 Oct: a missing watermark "does not prove human authorship"; watermarks "can indicate that an OpenAI system generated or processed part of a passage, but not how much human judgment, editing, or creativity went into it." Replacing 10% of words with synonyms dropped detection from about 92% to 66% (OpenAI's test, per TechCrunch).
- The v1 research pass missed this. It does not change the "no public text check" finding: OpenAI's text detection is still by application.
- His wording "in their documents" should read "text output, EU only, rolling out over the coming weeks".
