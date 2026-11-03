# Research Note — Microsoft-Decision-1 (Microsoft's decision model, Foundry + OpenRouter)
For: unassigned (follow-on to Sat 10 "router-in-front"; candidate callback / Note / later Saturday) · Depth: deep · Date: 2026-10-10

## Bottom line
Microsoft launched Microsoft-Decision-1 on 9 Oct 2026 (public preview in Foundry, live on OpenRouter). It is a Jev-class "decision model": you give it a fixed set of options and it returns a calibrated probability for each, with no generated text. It is post-trained on Alibaba's open-weight Qwen3.5-9B and priced at exactly Jev's rate ($0.042 per million input tokens, output free). The product facts are solid at primary. The performance claims are Microsoft's own benchmark, and the headline speed numbers are not like-for-like (its own latency was measured inside Foundry; the rivals' came from JevBench), so attribute them and do not assert them. The real story for Lars's readers is that the category got commoditised in about three weeks. The price floor is now about $40 per billion tokens, so the buying questions become calibration, provenance, data zone and how portable the API is.

## What's solid
- Launch date 9 Oct 2026; author Achint Srivastava, VP of Software Engineering, Office of the CTO. [commandline.microsoft.com/microsoft-decision-1-model-foundry] (PRIMARY)
- Status: "public preview" in Foundry. [techcommunity.microsoft.com … /4562742] (PRIMARY)
- Base model: "we post trained Qwen3.5-9B for fast, single-pass decision scoring and will soon rebase it on other models, including Microsoft AI (MAI) and OpenAI." [Microsoft post] (PRIMARY; The Register 10 Oct confirms)
- Price: $0.042 per million input tokens, output free. Identical in the Foundry US Datazone and EU Datazone. [Microsoft post; Foundry blog pricing table] (PRIMARY)
- Same posted price as Jev ($0.042/M in, output free; Jev launch post 15 Sep). [typesafe.ai launch post, already footed in research_router-in-front_2026-10-01.md] (PRIMARY both sides)
- Text in only, structured decisions out; 32,768-token context; released Oct 9. [openrouter.ai/microsoft/microsoft-decision-1]
- On OpenRouter it runs on the **OpenRouter Decisions API, not chat completions**: "chat completions SDKs will not work with it". Question types in the sample: `noul` (0–1 probability), `choice` (with full distribution), `score`. The page links to TypeSafe's "System One" docs. [OpenRouter model page]
- Supported decision types per Microsoft: yes/no, multiple-choice, rating, and rubric grading of AI responses and agent actions. [Microsoft post]
- Robustness claim, with method stated: eight perturbations per request; the decision flips on 1.3% on average, and zero flips when option descriptions are paraphrased or options reversed or shuffled. [Microsoft post] (vendor-measured)
- Safety test: 5,250 requests across 11 benchmarks (harmful content, jailbreak, prompt injection). No numbers given, only "successfully refused harmful behavior while retaining a high degree of utility". [Microsoft post] (vendor-measured, no figures)
- Post carries an editor's note: "updated from the original to add benchmarks for Jev on accuracy and calibration." So **Jev's accuracy and calibration were missing from the first version.** [Microsoft post]

## Microsoft's benchmark table (as of the updated post) — attribute every number
| Model | Avg accuracy (36 benchmarks, 147,137 Qs) | p50 latency | Calibration (100 = perfect) |
|---|---|---|---|
| Microsoft-Decision-1 | 83.5% | 85 ms (p95 125 ms)* | 92.2 |
| Jev 1.13.0 | 82.3% | 240 ms | **93.7** |
| Quyet-1.0-Large | 81.9% | 380 ms | 93.1 |
| Surogate Rune 26B-A4B | 79.7% | 380 ms | 91.8 |
| GPT-6 Luna Decisions (OpenAI) | 79.4% | 300 ms | 89.9 |
| deck-31B | 77.8% | 400 ms | 83.5 |
| H2O-Lightning-4B v1.1 | 77.2% | 210 ms | 91.8 |
| Strands-Decider 2B (AWS) | 54.8% (23 of 36 only) | not measured | not scored |
| GPT-6 Sol (LLM reference) | not ranked | 3.01 s | not scored |
*Microsoft's footnote: its own latency was "measured through Foundry in the same region". The others are the "JevBench v1.6.1 adjusted median (p50), checked Oct 7".
- Microsoft's own read: first on accuracy, fastest measured, **third on calibration, 1.5 behind Jev**.

## What's contested / watch out
- **Speed multiples are not like-for-like.** "35x faster than GPT-6 Sol", "2.5x faster than H2O" and The Register's derived "2.8x faster than Jev" compare Microsoft's in-region Foundry number with JevBench's adjusted medians for everyone else. OpenRouter's live provider table shows Microsoft-Decision-1 (via Azure) at **0.27 s p50**, about 3x Microsoft's 85 ms and slightly slower than the 240 ms JevBench lists for Jev. One HN tester (Topfi, 10 Oct) found it "very comparable" to Jev, cheaper per run (0.72x) but with different latency (283 ms vs 369 ms p50; the comment is ambiguous about which model was which). Anecdotal, n=1. **Print rule: "Microsoft says it is the fastest it measured"; never "35x faster" as fact.**
- **The accuracy lead is 1.2 points, on Microsoft's own suite** ("36 additional public and private benchmarks"). Private benchmarks can't be reproduced. JevBench itself is a third-party leaderboard (Benchmark Heaven), but the 36-benchmark comparison is Microsoft's run. Treat it as a near-tie with Jev, not a win.
- **Calibration is the number that matters for a router, and Jev leads on it** (93.7 vs 92.2, Microsoft's own table). That point was missing from launch coverage that used the original post: The Register reports Decision-1 as "second (behind Quyet-1.0-Large) in confidence score", which matches neither the current table nor Jev's row.
- **Secondaries garbled the internal case studies.** Primary text: Xbox Research, more than 10,000 feedback items, "competitive on quality with GPT-6 Sol while running over 14 times faster and 200 times less expensive." Startup Fortune says "competitive with GPT-5 … 80 to 100 times faster" and that OpenRouter access is "coming" (it is live). The Register says "more than 20x cheaper than GPT-6 Sol in text classification". **Use only the primary wording.**
- **"Copied the price"** (Startup Fortune) is an inference. FourWeekMBA: "We have no information on how either company set its price." Print it as "the same posted price", which is a fact; motive is speculation.
- **The Qwen question.** Simon Willison on HN: "I guess the fear of Chinese models is finally subsiding." The Register leads its headline with it. For a CISO audience, separate the two risks. The data does not go to China: it runs in Azure US/EU data zones. The open question is **model provenance and supply chain** (a fine-tune of a third-party base, with no published training-data or red-team detail beyond the safety test). Microsoft has not said why it will rebase on MAI/OpenAI. Don't speculate on motive.

## Couldn't verify
- Nadella's X post text beyond the search snippet ("…We're already testing it across Microsoft for everything from incident…"). X not fetched. Use the commandline post instead.
- Whether Jev on OpenRouter uses the identical `noul/choice/score` request shape, so that switching is a model-string change. OpenRouter's Jev page returned no content to the scraper. **Lars can confirm from his own Jev router code in one look.**
- Real per-call cost versus Jev. The posted price is identical, but tokenizers differ, so the cost per email can differ (the HN tester's 0.72x hints at this). Not established. His own shadow run can measure it.
- Any number behind the safety and incident-response claims ("performed better and faster than an LLM"). None published.
- Whether Microsoft is an investor in TypeSafe: FourWeekMBA lists a16z (lead), Sequoia, DCVC and angels for the $870M Series A at $7.5B. No Microsoft named. Absence of evidence only.

## The economics
- Posted input price per million tokens, decision-model class, as of 10 Oct:
  - Cloudflare Clef-flash **$0.038** (cut from $0.09 on 9 Oct; hosted context shrunk to 24k; open weights) [FourWeekMBA citing Cloudflare post + Workers AI docs]
  - Microsoft-Decision-1 **$0.042** [Microsoft]
  - Jev **$0.042** [TypeSafe]
  - OpenAI Decisions API **$0.10** [footed in research_router-in-front addendum]
  - Output free across all four.
- In Lars's units: a ~1,000-token email costs about $0.000042 to score on Jev or Decision-1, so a million scored emails is about **$42**. On OpenAI's Decisions API the same million is about **$100**; on Clef-flash about **$38**. At these prices the bill stops being the decision. **The cost of being wrong (Sophos, 29 Sep: "cheaper decisions are only a bargain if the mistakes don't cost more than the automation saves") and the cost of switching are the decision.**
- Speed of commoditisation: Jev 15 Sep → AWS Strands-Decider (≈1 Oct, open source) → OpenAI Decisions API public beta 6 Oct → Cloudflare price cut + Microsoft-Decision-1 9 Oct. **Four big platforms matched a startup's category in 24 days**, the same week the startup raised $870M at $7.5B.

## Drop-in facts (each sourced)
- "Microsoft-Decision-1 … available in Microsoft Foundry and through OpenRouter … designed for routing, classification, prioritization, verification, and workflow control." [Microsoft, 9 Oct 2026]
- "To build Microsoft-Decision-1, we post trained Qwen3.5-9B … and will soon rebase it on other models, including Microsoft AI (MAI) and OpenAI." [Microsoft]
- "Input tokens cost $0.042 USD per million tokens. Output tokens are free." [Microsoft], the same posted price as Jev. [TypeSafe, 15 Sep]
- By Microsoft's own table it is first on accuracy (83.5%) but "third on calibration, 1.5 behind Jev." [Microsoft]
- "The probability itself is part of the API, not just a ranking score … a 90% prediction should be right about nine times out of 10." [Microsoft]
- "Adding just 100 milliseconds to each of 20 sequential decisions adds two seconds to the overall workflow." [Microsoft]
- Public preview in Foundry, US and EU Datazone deployments at the same price. [Microsoft Foundry blog]
- On OpenRouter it uses the Decisions API, and "chat completions SDKs will not work with it." [OpenRouter]

## Angles this opens
- **Direct sequel to Sat 10 "router-in-front".** That piece ends "Which one wins is a question for another day." Two days later the list has a fourth name. The honest answer from his own method is that you don't pick on a vendor table: you **shadow it against Jev on the same mail** (his prompts 1–3 already do exactly this), and you watch calibration below the 0.5 line, not accuracy. It's a natural Note or a short Saturday follow-up. The Sat 17 expense-reports piece could mention it in a line; it is text-only, so it doesn't change the images point (OpenAI's API still wins there).
- **CISO angle:** a frontier vendor shipping a Chinese open-weight fine-tune into a "secure, trusted environment" is a supply-chain-governance question, not a data-residency one. It connects to Thu 1 Oct "model onto desk" (Foundry Local, open models on the machine) and to the idea that the decision layer sits in front of agents as a control point (agent controls, safety screening). Who validated the control?
- **Platform-economics angle (his cost framing):** distribution beats invention. The startup defined the category; the platforms matched the price in weeks. That connects to Fri 02 "wrapper shop".
