# Who Controls the Model Controls Everything

**Status: Draft rv5 -- editor-panel round 1 applied; would score 8.6 unweighted by the flags, HELD AT 7.0 by two open [VERIFY]s. NOT panel-cleared, NOT ready for Scheduled. Round-1 fixes: laundered-statistic section moved back above the new signature-list section (the "arguments in costume" transition had been orphaned by the rv4 insert); "the absence is the evidence" softened to survive a hostile read (alternative explanations named, then the reported basis held); distillation, Moonshot and Huang glossed for a non-AI-insider reader; Huang's first-X-post detail attributed rather than asserted; one of three "not X, it's Y" constructions varied; close opener recast off the 29th's "Here is the..." pattern. Two open [VERIFY] flags (see foot) cap the panel at 7 per the standing accuracy rules. Changes from rv3: (1) lane 1 gets its turn -- the 24 Jul open-weights letter, the OpenAI/Anthropic/Google absence, and the Bessent/Kratsios escalation, all post-dating the 21 Jul sweep; (2) close rewritten off the story -- the reader's-calculus/news-cycle device was running four consecutive weekdays (27, 28, 29, 30) and is retired here per the 24 Jul rationing rule; (3) Wednesday's "sophisticated facilities manager" handoff now paid off in lane 3; (4) capability+cost beat added (1.4TB weights, $3/$15 API) -- "free" was doing unearned work; (5) appositive-gloss-then-consequence deployed at three points; (6) opener tightened to two declaratives after the epigraph. Target Thursday, 30 July 2026.**
**Series: Weekday feed**
**Thread: Ad Hoc Regulatory Regime (geopolitics / model governance)**
**Builds on: "The Kill Switch You Didn't Know About" (2 Jul); "The Regulators Just Got Fired" (3 Jul); Wednesday's AU vacuum; "Bring the Model Home" (24 Jul -- Kimi K3 continuity). Sets up Friday (what a control actually is).**
**Source spark: Axios "four shelved attempts" (20 Jul); the 25-signatory open-weights letter (24 Jul); Bessent sanctions threat (21 Jul); Kratsios distillation claim (22 Jul); Kimi K3 weights due 27 Jul; a16z 80% stat provenance; Hassabis frontier-gate essay (14 Jul); Lawfare "The Kill Switch and the Long Arm" (9 Jul) and "Knives Are Out for Open-Weight AI Models" (24 Jul); Mistral/Mensch Eurogroup (9 Jul). Detail in References\research_control-week-sweep_2026-07-21.md (Front 2), plus the 25 Jul additions noted at foot.**

---

"He who can destroy a thing, controls a thing."

That is Paul Atreides, in Frank Herbert's *Dune*. It is sharper political philosophy than the spice line everyone quotes. Control was never really about *holding* the thing. Anyone can hold something for a while. Real control -- the kind that makes emperors kneel -- comes from the credible power to *destroy* it. Paul doesn't win by hoarding the spice; he wins by convincing everyone he is willing to burn it to ash and take interstellar civilization down with it. The threat is the throne.

Now swap the spice for the model, because that is the fight this week has been circling, and watch Paul's doctrine break in two places at once. You cannot hold a model: the weights copy, endlessly, for nothing. And increasingly you cannot destroy one either -- you cannot burn a file that already sits on ten thousand hard drives in a hundred countries. The one lever that ever really conferred control, the power to end the thing, is the exact lever the most powerful people on earth are now grabbing at and finding disconnected from the machine.

Four times, the most powerful government on earth reached for the switch. Four times, it put the switch back down.

That is the real story of American AI policy this summer, and it only became visible last week. According to reporting nobody has denied, the Trump administration has now tried and shelved four separate ways to restrict Chinese open-weight AI models: Commerce weighed adding Chinese AI labs to the Entity List and didn't; an intelligence advisory warning companies off Chinese models was drafted and never released; a proposed executive order requiring US firms that host Chinese models to guarantee their security and take on the liability was shelved; and a set of Commerce rules aimed at the same models through supply-chain authorities was abandoned. Four reaches. Four retreats.

And then, three days before I sat down to write this, a Chinese lab shipped the thing all four attempts were trying to contain. `[VERIFY]` Kimi K3 -- a 2.8-trillion-parameter open-weight model, the same one I told you last Friday, in "Bring the Model Home," would finally let a regulated business run frontier capability inside its own walls -- had its weights posted for anyone to download. The switch the government kept reaching for turns out not to be wired to anything.

This is the week's argument arriving at the model layer. Monday, you don't control the ratio. Tuesday, you don't control the exhaust. Wednesday, the country adopting fastest doesn't control its own framework. Today: nobody controls the models themselves -- not really -- and three separate powers are fighting over the illusion that they might.

## Why the switch won't flip

Start with why the four retreats were not failures of nerve. They were collisions with arithmetic.

You cannot ban a number. Open weights are, in the end, a very large file of numbers, and once that file is on tens of thousands of hard drives around the world, there is no memo that recalls it. A ban does not remove the capability; it removes your visibility into who is using the capability, while doing nothing, effectively, to the capability itself.

Though "free" is doing quiet work in that sentence. The K3 weights run to roughly 1.4 terabytes -- a download, not a deployment; the hardware to serve a 2.8-trillion-parameter model at any useful speed still costs real money, which is why most people who want it will rent it at three dollars in and fifteen dollars out per million tokens rather than run it themselves. So the file is free and the capability is not. Not yet. But that gap is a cost curve, and cost curves in this industry have run one direction for four years, which means a restriction does not have to outrun today's price -- it has to outrun the price in eighteen months, when the same weights fit on hardware a mid-sized business can sign a purchase order for. That is the arithmetic nobody in this fight has an answer to.

Which is why the reporting says the real strategy has shifted from prohibition to the slower, quieter tools: procurement restrictions, advisories, public pressure -- described by one source as "slower and more durable" than a ban. That is an honest read of a losing hand -- and not a toothless one: a procurement ban or a federal advisory can still shape what a cautious enterprise buyer dares to deploy, even when it can't recall a single copy of the file. What it cannot do is put the capability back in the box.

The most telling voice in the whole fight belongs to a senior administration adviser who came out against restriction, and named the reason out loud: the closed labs, he said, "want the government to eliminate their open-source competition." Sit with that. The people lobbying hardest for the government to lock down open models are the companies that sell the closed ones -- which is the Ad Hoc Regulatory Regime's signature move, the one "The Regulators Just Got Fired" traced three weeks back: policy shaped by whoever is loudest in the room. That is not a national-security argument wearing a commercial costume; it is a commercial argument wearing a national-security costume, and an insider said so on the record. (I'm keeping his title vague on purpose -- the sources disagree on exactly what it is this month, and the quote is the point, not the business card.)

## The statistic that laundered itself

While we're on the subject of arguments in costume, let me hand you the number you are about to see everywhere, and the truth about where it came from, because it is a small masterpiece of how a debate like this gets fought.

You will read that "80% of open-source developers worldwide build on Chinese models." It sounds authoritative. Its origin is a venture capitalist, in an interview, estimating that there was an "80% chance" that a startup pitching his firm and already using open-source models was using a Chinese one. That is a guess, about a subset, of one investor's deal flow. It got restated in a policy post as a flat fact about "developers building with open source tools," and from there it became "80% of open-source developers worldwide." A vibe about one firm's meetings is now a global statistic cited in policy fights.

If you want a number that actually holds, use this one: open Chinese models accounted for as much as 30% of all AI usage in some weeks of last year, measured off actual traffic rather than deal-flow vibes. That is sturdy, it is sourced, and it is quite alarming enough. In a fight over who controls the models, even the statistics have owners -- which is a useful thing to remember every time one lands in your inbox pre-loaded with a conclusion.

## Then the quote became a signature list

And then last week the commercial argument stopped being one adviser's opinion and became a document with names on it.

On 24 July, twenty-five companies signed a public letter urging Washington against "premature restrictions on downloadable AI models." Nvidia. Meta. Microsoft. Mistral. Hugging Face. Dell, IBM, Palantir, CrowdStrike, Replit, Perplexity, Andreessen Horowitz, Y Combinator, the Linux Foundation. Nvidia's Jensen Huang -- in what was reportedly the first post he has ever made on X -- signed on with a line worth keeping: "The world needs both frontier closed models and frontier open models."

Now read the other list, the one nobody printed. OpenAI did not sign. Anthropic did not sign. Google DeepMind did not sign. You could put that down to lawyers, or timing, or simple reluctance to stand inside a coalition Nvidia convened. Except that those three are the same companies the reporting has pressing Washington to restrict open-weight models in the first place. So when twenty-five of their peers put the opposite argument on the record, all three of them found somewhere else to be that afternoon.

You no longer need the adviser's quote. The signature page makes his argument for him.

And the retreat, it turns out, was a pause and not a policy. Inside a fortnight the Treasury Secretary said sanctions and Entity List designations were "on the table" for Chinese AI labs, claiming watermarks from US language models had turned up inside Chinese ones; the White House science director accused Moonshot -- the Chinese lab behind K3 -- of "large-scale, covert industrial distillation" (training your model on another model's outputs, which is either standard practice or industrial theft depending entirely on who is describing it). Four quiet shelvings, then two weeks of very loud threats, with US-China talks not scheduled until September. Read that as a strategy resolving if you like. It looks to me like a government arguing with itself at volume, which is the Ad Hoc Regulatory Regime doing the only thing it reliably does.

## The gate wearing a coordinator's coat

Lane two. While Washington fumbles the off switch, one of the most serious people in the field has proposed building a better one -- and dressed it as international coordination.

Demis Hassabis, who runs Google DeepMind, published a framework in mid-July calling for an independent standards body for frontier AI, modeled on the way the financial industry polices itself. Labs would submit their models for review up to thirty days before release; a body would screen them and could "coordinate an industry-wide slowdown if dangers mount." It would cover all frontier models, he wrote, regardless of country of origin or whether they are open or closed.

Read the fine print and the coordination language thins out. What he is describing is a standards body -- US-hosted, US-led, funded by the industry it screens, and enforcing compliance that becomes mandatory for deployment into the US market. Then notice what that arrangement actually is. It is not a treaty among equals; it is a proposal about who holds the gate, written by someone standing near the front of the line to hold it.

It may even be a good idea -- Hassabis is not a crank, and a real review body for frontier models is not a crazy thing to want. But call the proposal what it is: a bid for control of the chokepoint, not a retreat from the idea of a chokepoint. The same adviser who torched the restriction push torched this too: "The rest of the world won't play by our rules if we bog ourselves down."

## The fear, and the company selling relief from it

Lane three, and this is the one that should feel familiar, because I wrote its prequel four weeks ago.

In "The Kill Switch You Didn't Know About," I told you the US government had, for the first time, used export controls to reach into the market and pull a working AI model out of it -- foreign access to two frontier models suspended by directive, no warning, no vote. That is Paul's rule working exactly as written: the power to destroy access was real, and for a moment it was absolute -- because those were closed models, gated behind a company the government could actually reach and lean on. That was not a hypothetical. A careful legal writer at Lawfare confirmed the mechanism this month and put the principle plainly: only Washington can make the assurances a foreign buyer wants, and only by binding itself -- which it has shown it will not reliably do.

So a market has opened for exactly that fear, and Europe's Mistral is standing in it. Its CEO told EU finance ministers this month that Europe has roughly two years to build its own competitive AI compute before dependence on American providers becomes structural and very hard to reverse -- and in the same stretch, Mistral is shipping its own frontier open-weight model and positioning itself as the sovereign alternative for anyone who does not want a foreign memo able to switch their capability off. The kill switch I warned about at the start of the month is now, four weeks later, a European sales pitch. That is how fast a control problem becomes a business model.

Yesterday I borrowed a phrase for what Australia is quietly becoming: a sophisticated facilities manager -- a country that hosts the racks, cuts the ribbon, and calls the hosting sovereignty. Mistral's whole argument is that Europe has about two years before it becomes the same thing at continental scale. Carry that distinction into today, because it is the one that matters. Hosting the building is not controlling the model. You can own every rack in the data center, meet every energy condition, sign every memorandum, and still not own the decision about whether the thing running inside it is allowed to keep running -- because that decision lives in a jurisdiction where you do not get a vote.

## Three lanes, one missing thing

Step back and the three fights rhyme. Washington wants to control which models exist and can't enforce it. Hassabis wants to control the gate they pass through and is honest enough to design it. Mistral wants to monetize the fear that someone else controls the switch. Three different hands reaching for the same lever -- Paul's lever, the power to destroy or deny, because that was always the only control that truly counted -- and every one of them is closing on a lever that open weights have quietly cut. Not one is operating inside a framework anyone agreed to. Everybody is improvising, at the scale where improvisation used to be unthinkable.

Yesterday I showed you a country adopting AI at six times the expected rate with its rulebook still a promise. Today is the same picture one level up: the superpowers doing model policy by directive, reversal, and press release, while the capability itself slips out the back door onto everyone's hard drives. You cannot hold the spice, and now you cannot burn it either. The spice must flow -- Herbert was right about that part; he just never imagined it would flow for free.

## So, Thursday

You do not get a vote in any of these three fights. That is the uncomfortable part, and I am not going to pretend otherwise. But you do get to decide your exposure to how they resolve, and that decision is available to you right now, in daylight.

**It is an inventory question, the same shape as Monday's and Tuesday's.** Which models does your business actually depend on? Whose jurisdiction are they governed by? If one of them gets pulled off the market by a memo next quarter -- the way two of them already were -- what is your fallback, and how fast can you reach it? A business with exactly one model dependency, from one vendor, under one export regime, is a padlock waiting for a reason. A business that knows its options and has spread its supply on purpose is not.

**Then price the fallback, because an option you cannot afford is not an option.** "We could self-host an open model" is a sentence, not a plan, until somebody in your building has costed the hardware, the people, and the eighteen months of depreciation. Do that arithmetic while it is cheap to do on paper. The businesses that get hurt by any of these three fights will not be the ones that picked wrong; they will be the ones that never learned what picking again would cost.

And none of that inventory means anything unless something in your stack can actually enforce the choices you make from it -- which is Friday, and the last question of the week: what does a control actually look like when someone finally builds one, instead of announcing one.

Three fights, and three sets of people certain they will be the ones holding the lever. Not one of them has stopped to check whether the lever is still attached to anything.

You cannot fix that, and nobody is going to fix it for you. What you can do is decline to build your business on the assumption that any of the three of them wins. Because there will be no memo telling you they've worked it out -- the memo, when it comes, will be the one that takes your model away.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that three separate powers are fighting for control of the AI models -- and the one thing none of them can actually deliver is control.*

<!-- [Lars/editors -- PRE-PUBLISH GATE: TWO OPEN [VERIFY] FLAGS AS OF 25 JUL]

(1) [VERIFY] KIMI K3 WEIGHTS -- BLOCKING. The paragraph beginning "And then, three days before I sat down to write this" asserts as accomplished fact that the K3 weights shipped. As of 25 Jul they have NOT. Announced 16 Jul (API only); weights promised 27 Jul, confirmed still-pending by coverage on 19 and 24 Jul. The draft was written forward from the 21 Jul sweep and states a future event in the past tense. On 27 Jul this resolves one of three ways: weights ship as promised -> delete the flag, sentence stands as written; weights slip -> the "three days before I sat down" line and the "Bring the Model Home" callback both have to be recast in the future tense, and the lede's force drops; weights ship partial/gated -> rewrite the sentence to match. Do not promote to Scheduled with this flag open.

(2) [VERIFY] EO STATUS 28-29 JUL -- cannot be checked before those dates. Original gate. Note the picture has already moved twice since the 21 Jul sweep: the 24 Jul open-weights letter and the Bessent/Kratsios escalation are both now IN the draft (new section "Then the quote became a signature list"). Re-sweep on 29 Jul; if an EO actually lands, it becomes the lede and lane 1 restructures around it.

RESOLVED THIS PASS (no longer open):
- Four shelved EO attempts -- traceable to Axios, 20 Jul. Holds.
- Hassabis gate -- traceable to his 14 Jul essay + same-day Axios interview. Holds.
- Mistral kill-switch -- traceable to Lawfare, 9 Jul (Fable/Mythos export-control suspension) + Mensch to the Eurogroup, 9 Jul. Holds. Mensch is paraphrased, not quoted -- no transcript exists; keep it that way.
- Sacks title -- still contested across sources; still deliberately generic in the text. Do not add a title.
- 1.4TB / $3-$15 per M tokens -- secondary sourcing (24 Jul trade coverage); the 1.4TB is consistent with 2.8T params at 4-bit. Low risk, but it is a number in a piece about laundered numbers, so soften or cite if the panel objects.

NEW SINCE THE 21 JUL SWEEP (added this pass, not in References\research_control-week-sweep_2026-07-21.md):
- 24 Jul: 25-signatory open-weights letter. Absent: OpenAI, Anthropic, Google DeepMind (TechCrunch also lists SpaceX). TechCrunch, Tom's Hardware, CNBC, all 24 Jul.
- 21 Jul: Bessent -- sanctions/Entity List "on the table"; "watermarks of our US large language models on many of the Chinese models." CNBC 21 Jul; also in ai_brief_2026-07-23.
- 22 Jul: Kratsios -- Moonshot "large-scale, covert industrial distillation." Lawfare 24 Jul; also in ai_brief_2026-07-23 via Machine Times.
- US-China AI talks scheduled September (Reuters, 21 Jul).
- Available but unused: the Hugging Face incident (frontier models' guardrails blocked defenders analysing an attack; GLM 5.2 did the job). Strong concrete beat for the "open models broaden defensive capability" argument if the panel wants lane 1 to carry more weight. In ai_brief_2026-07-23 + Lawfare 24 Jul.

LENGTH -- LARS'S CALL. Body is ~2,720w against a house norm of 2,000-2,330 (rv3 was 2,029; Wed 29 Jul is 2,330; Tue 28 Jul is 2,037). The week plan targets 1,500-1,800, which no piece this week actually hits. The new material adds ~700w. If you want it back inside the norm, the cleanest cut is one of the two sections that do the same job: "The statistic that laundered itself" and "Then the quote became a signature list" both argue that the case for restriction is commercially owned. The stat section proves it by provenance; the signature section proves it by who wouldn't sign. My read is the signature list is the stronger and more current of the two and the stat section could compress to a single paragraph -- but the stat section is your material and the 80% number is about to be everywhere, so I have not cut it.

ROOT CAUSE OF THE REPEATED CLOSE -- WORTH FIXING AT SOURCE. The editor-panel skill's own Seat 1 checklist still states the close should carry "the reader's-calculus question... naming news-cycle fatigue in the same breath" as a standing requirement. That is the pre-24-Jul rule. Your 24 Jul correction made it a rationed conditional callback, and the memory note supersedes the skill file -- but the skill has been marking its absence as a voice miss on every piece, which is very likely why the device ran four weekdays straight. The skill file at Writing Flow\ needs the same correction the memory note got, or the panel will keep pushing every close back toward the formula. Say the word and I will produce the corrected skill.

VOICE NOTE -- CLOSE DEVICE RETIRED HERE. The reader's-calculus / "news cycle that never even seems to pause" close ran Mon 27, Tue 28, Wed 29 and was drafted again for Thu 30, making four consecutive weekdays on one device. Per the 24 Jul rule (rationed callback, once or twice a week, worded fresh, never a formula) it is cut from this piece and the close is derived from the story instead. Mon/Tue/Wed left untouched -- 27 and 28 are Scheduled, 29 is signed off; flagged to Lars, his call.
-->
