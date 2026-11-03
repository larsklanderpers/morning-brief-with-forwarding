# Research Note -- Its Own Computer (Thu 8 Oct, AI growth)
For: substack_draft_its-own-computer_2026-10-08 (not yet written) · Depth: deep · Date: 2026-10-07 (research run night of 6 Oct PT)

## Bottom line
- The load-bearing sentence SURVIVES at primary, as attribution: OpenAI's own page says each dot "works on its own cloud computer, while your computer and its contents stay separate unless you choose to connect it." Launch 29 Sep 2026.
- ⛔ **SELF-COLLISION, the biggest finding:** Sat 12 Sep *Nine Bots and One Computer* (Published) took apart exactly this claim for Grok Bot -- docs said "Each Bot has a computer"; his security-log read was ONE shared VM per account, "no implied security boundary here besides good behavior". The working title "Its Own Computer" restates the phrase he debunked. Thursday must either (a) callback to Sat 12 and ask the same question of Dots, or (b) re-title and move the spine off the machine. Per-dot vs per-account isolation for Dots is UNVERIFIED (no OpenAI doc states it; nobody has tested -- flaviocopes says outright he has no access).
- ⚠️ **Brief correction:** "Dots not offered in the EU or UK" is too broad. OpenAI's statement (via The Next Web): "For Pro users, the eligible markets do not currently include the European Economic Area, Switzerland or the UK." Business Premium gets it in all supported ChatGPT regions per TNW. Australia is not excluded.
- The jobs leg is the thinnest: there is no job-posting data for "agent manager / agent owner". What exists is HBR's Feb 2026 definition (Srinivasan & Wei) with one Salesforce example, and Gaspar's "nobody will own and maintain the knowledge" test (AI Daily Brief, 29 Sep). Sell it as a role forming, not a measured trend.

## What's solid (primary)
- **Dots, own cloud computer** -- openai.com/index/introducing-dots/ (29 Sep 2026): "Powered by GPT-6 Astra, they have their own cloud computer, learn from feedback over time, and can work towards your goals 24/7." / "Each dot works on its own cloud computer, while your computer and its contents stay separate unless you choose to connect it."
- **Dots, reach** -- same page: "over 4,000 apps" via plugins.
- **Dots, guardrails** -- same page: auto-review; "Certain sensitive tasks, such as changing a password, always stay with you"; monitoring can "pause or stop the dot's work". VentureBeat adds admin Custom Rules (permit / require approval / prohibit) and an Activity View.
- **Dots, availability and price** -- same page: "rolling out today in ChatGPT to Pro and Business Premium users in eligible markets. Enterprise users (including Edu and Healthcare) can try the beta when their workspace admin enables it." "Your first dot is included in your Pro or Business Premium plan at no extra cost." Free and Plus excluded.
- **Space** -- chatgpt.com/features/space/: "Keep work in one shared space, where you can tag in ChatGPT, Codex, or your dot to help." "Dots work natively across files in Space. Wherever you work with your dot -- in ChatGPT, Slack, or Microsoft Teams -- you can also ask it to keep the page up to date as plans change." Pro, Business, Enterprise.
- **Credentials** -- flaviocopes (reading OpenAI docs, untested): sign-in goes through a private form "the model never sees"; saved logins need confirmation before reuse. Treat as doc-reported, not tested.

## What's contested / watch out
- **EU/UK** -- Pro only, per OpenAI statement to TNW. NBC (robots-blocked, unreached) reportedly framed it as "Europe and the UK over regulatory concerns"; OpenAI gave NO reason (trendingtopics.eu confirms). Do not print a reason as OpenAI's.
- **Chesky / Airbnb "agents need their own OS"** -- TechCrunch 1 Oct. The headline is the reporter's. His direct words: "no one is developing a full operating system software developer kit"; the industry lacks "a true operating system built for AI", ideally "at the kernel level ... and all components like agents would interact with each other." That is an AI-native OS for agents to talk to each other, NOT "the agent gets its own machine". Usable only with his words, not the headline. "Multiplayer" / 3-6 months is reporter paraphrase.
- **Coworker framing** -- VentureBeat's line ("a persistent digital coworker: software that employees can delegate responsibility to") is the reporter's, not OpenAI's. Also: "delegate" is Wed 7's word and Sunday's frame -- do not lean on it Thursday.

## Couldn't verify
- **One VM per dot vs one per account** -- no OpenAI doc, system card or tester settles it. Cannot print "each dot is isolated". Can print OpenAI's sentence, attributed, and say what Sat 12 found for Grok Bot. This is a [YOUR TAKE] / test opportunity if he has a Pro or Business Premium seat.
- **Decisions API** -- no openai.com doc reached; New Stack: limited preview, pricing at broad rollout, ~150ms. Secondary only. Also collides with Sat 10 (Jev decision router) -- leave it to Saturday.
- **Pro 500 tier** -- Decrypt: $500/month bundled with Ultrafast; pricing page not reached. Fri 9 territory anyway.
- **"Bot onboarder" (@distortgeekin, X article 30 Sep, "Grok Bot: How to Hire Your First AI Employee")** -- full text unreached (Firecrawl now refuses x.com, contra the house note). Excerpt only: "Nobody hires a person by handing them the company card on day one". Musk amplified it. It is a GROK BOT guide: collides with Sat 10 and Sat 12. Avoid or one clause.
- **"Fastest-growing job title of 2026: AI agent manager"** (Interview Guys) -- NO source behind it. LinkedIn Jobs on the Rise 2026 unreached (robots). Do not print "fastest-growing".
- **Microsoft 7 Oct Windows + Surface event** -- runs today; previews (Windows Central, Windows Latest 3 Oct) point at local AI agents in the OS and Surface Laptop Ultra. Re-sweep morning of 8 Oct; one paragraph max, correct forward if it changes Thu 1.

## The economics
- First dot "at no extra cost" inside Pro ($200/mo) or Business Premium; extra-dot pricing undisclosed (VentureBeat). So today the marginal cost of a standing machine-plus-browser-plus-4,000-connectors is zero on top of a seat you already pay for -- the cost is in the seat and in whatever it touches. Pro allowance for Work/Codex cut from 30 Oct (Latent Space, secondary) -- Fri 9's ground, mention only if needed.
- Grok Bot comparison (Sat 12): one shared computer per account at subscription price. Two vendors, same pitch, different (or unknown) isolation -- that IS the reader's buying question.

## Drop-in facts
- "Each dot works on its own cloud computer, while your computer and its contents stay separate unless you choose to connect it." -- OpenAI, Introducing dots, 29 Sep 2026.
- "Certain sensitive tasks, such as changing a password, always stay with you." -- same.
- "Your first dot is included in your Pro or Business Premium plan at no extra cost." -- same.
- "For Pro users, the eligible markets do not currently include the European Economic Area, Switzerland or the UK." -- OpenAI statement, via The Next Web.
- "Dots work natively across files in Space ... you can also ask it to keep the page up to date as plans change." -- chatgpt.com/features/space.
- Gaspar's wait signal: "nobody will own and maintain the knowledge (the agent drifts within weeks, sometimes days)" -- AI Daily Brief, 29 Sep (podcast; attribute to Nufar Gaspar on the show).
- HBR, 12 Feb 2026, Srinivasan & Wei, "To Thrive in the AI Era, Companies Need Agent Managers": Salesforce support agent manager Zach Stauber, "I start and end my day in dashboards, scorecards, and agent observability monitoring." No quantitative data in the piece.

## DO NOT PRINT
- "Dots not available in the EU/UK" unqualified; any reason for the exclusion as OpenAI's.
- "Each dot is isolated / has its own separate VM" as fact.
- Chesky's TechCrunch headline as his quote.
- "Fastest-growing job title"; any agent-job count.
- Decisions API detail (Sat 10's); Pro 500 detail (Fri 9's); GPT-6.1 Astra shelving (Wed 7 DNP); Mollick swarm (Sun 4).

## Angles this opens
- **Re-angle candidate (drafter's suggestion, his call):** Thursday as the up-side sequel to Sat 12 -- "a month ago the marketing said each bot had its own computer and it didn't; OpenAI now says each dot does; here is why that would be a good thing and the one question to ask before you believe it". Keeps it least-dry, gives Sunday its onboarding leg (someone owns the machine), and turns his own finding into the hook instead of a contradiction.
- Gaspar's knowledge-owner test is the cleanest "new job" evidence: the role is the person who keeps the agent right, and it starts inside a job you already have.
