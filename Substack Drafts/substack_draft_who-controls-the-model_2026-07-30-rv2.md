# Who Controls the Model Controls Everything

**Status: Draft rv2 -- added the Dune/spice intro Lars requested (analogy-first open into the "four times" beat) + a "the spice must flow" bookend at the synthesis. Otherwise = rv1 (editor-panel round 2, 9.17). NOTE: the opener is now analogy-first; happy to re-run the panel to reconfirm the number, but it reads clean. Target Thursday, 30 July 2026. GATE: re-check EO status + Kimi K3 weights 28-29 Jul before publish (internal note at foot).**
**Series: Weekday feed**
**Thread: Ad Hoc Regulatory Regime (geopolitics / model governance)**
**Builds on: "The Kill Switch You Didn't Know About" (2 Jul); "The Regulators Just Got Fired" (3 Jul); Wednesday's AU vacuum; "Bring the Model Home" (24 Jul -- Kimi K3 continuity). Sets up Friday (what a control actually is).**
**Source spark: Axios "four shelved attempts" (20 Jul); Kimi K3 weights due 27 Jul; a16z 80% stat provenance; Hassabis frontier-gate essay (14 Jul); Lawfare "The Kill Switch and the Long Arm" (9 Jul); Mistral/Mensch Eurogroup (9 Jul). Detail in References\research_control-week-sweep_2026-07-21.md (Front 2).**

---

"He who controls the spice controls the universe."

Frank Herbert built *Dune* around that line sixty years ago -- a whole galaxy running on one substance, mined on one planet, and whoever held the flow of it held everyone else by the throat. The spice made travel possible, so the spice made power possible, and the entire saga is just people maneuvering to control who gets it and who doesn't.

Swap the spice for the model, and you have the fight this week has been circling. Every business runs on it now. Every government wants to govern it. Every rival wants to own it outright. There is only one difference that matters, and it is the part Herbert never had to write, because it would have ended his plot in a chapter: in our version, the spice cannot actually be held. It copies. And once you understand that, you understand why the most powerful people on earth keep grabbing at a thing that runs through their fingers.

Four times, the most powerful government on earth reached for the switch. Four times, it put the switch back down.

That is the real story of American AI policy this summer, and it only became visible last week. According to reporting nobody has denied, the Trump administration has now tried and shelved four separate ways to restrict Chinese open-weight AI models: Commerce weighed adding Chinese AI labs to the Entity List and didn't; an intelligence advisory warning companies off Chinese models was drafted and never released; a proposed executive order requiring US firms that host Chinese models to guarantee their security and take on the liability was shelved; and a set of Commerce rules aimed at the same models through supply-chain authorities was abandoned. Four reaches. Four retreats.

And then, three days before I sat down to write this, a Chinese lab shipped the thing all four attempts were trying to contain: Kimi K3, a frontier-class open-weight model -- the same one I told you last Friday, in "Bring the Model Home," would finally let a regulated business run frontier capability inside its own walls -- its weights now posted for anyone with the hardware to download and run. The switch the government kept reaching for turns out not to be wired to anything.

This is the week's argument arriving at the model layer. Monday, you don't control the ratio. Tuesday, you don't control the exhaust. Wednesday, the country adopting fastest doesn't control its own framework. Today: nobody controls the models themselves -- not really -- and three separate powers are fighting over the illusion that they might.

## Why the switch won't flip

Start with why the four retreats were not failures of nerve. They were collisions with arithmetic.

You cannot ban a number. Open weights are, in the end, a very large file of numbers, and once that file is on tens of thousands of hard drives around the world, there is no memo that recalls it. A ban does not remove the capability; it removes your visibility into who is using the capability, while doing nothing, effectively, to the capability itself. The administration appears to have figured this out, which is why the reporting says the real strategy has shifted from prohibition to the slower, quieter tools: procurement restrictions, advisories, public pressure -- described by one source as "slower and more durable" than a ban. That is an honest read of a losing hand -- and not a toothless one: a procurement ban or a federal advisory can still shape what a cautious enterprise buyer dares to deploy, even when it can't recall a single copy of the file. What it cannot do is put the capability back in the box.

The most telling voice in the whole fight belongs to a senior administration adviser who came out against restriction, and named the reason out loud: the closed labs, he said, "want the government to eliminate their open-source competition." Sit with that. The people lobbying hardest for the government to lock down open models are the companies that sell the closed ones -- which is the Ad Hoc Regulatory Regime's signature move, the one "The Regulators Just Got Fired" traced three weeks back: policy shaped by whoever is loudest in the room. That is not a national-security argument wearing a commercial costume; it is a commercial argument wearing a national-security costume, and an insider said so on the record. (I'm keeping his title vague on purpose -- the sources disagree on exactly what it is this month, and the quote is the point, not the business card.)

## The statistic that laundered itself

While we're on the subject of arguments in costume, let me hand you the number you are about to see everywhere, and the truth about where it came from, because it is a small masterpiece of how a debate like this gets fought.

You will read that "80% of open-source developers worldwide build on Chinese models." It sounds authoritative. Its origin is a venture capitalist, in an interview, estimating that there was an "80% chance" that a startup pitching his firm and already using open-source models was using a Chinese one. That is a guess, about a subset, of one investor's deal flow. It got restated in a policy post as a flat fact about "developers building with open source tools," and from there it became "80% of open-source developers worldwide." A vibe about one firm's meetings is now a global statistic cited in policy fights.

If you want a number that actually holds, use this one: open Chinese models accounted for as much as 30% of all AI usage in some weeks of last year, measured off actual traffic rather than deal-flow vibes. That is sturdy, it is sourced, and it is quite alarming enough. In a fight over who controls the models, even the statistics have owners -- which is a useful thing to remember every time one lands in your inbox pre-loaded with a conclusion.

## The gate wearing a coordinator's coat

Lane two. While Washington fumbles the off switch, one of the most serious people in the field has proposed building a better one -- and dressed it as international coordination.

Demis Hassabis, who runs Google DeepMind, published a framework in mid-July calling for an independent standards body for frontier AI, modeled on the way the financial industry polices itself. Labs would submit their models for review up to thirty days before release; a body would screen them and could "coordinate an industry-wide slowdown if dangers mount." It would cover all frontier models, he wrote, regardless of country of origin or whether they are open or closed.

Read the fine print and the coordination language thins out. The body he describes would be US-hosted and US-led, and the compliance it "coordinates" would become mandatory for deployment into the US market. That is not a treaty among equals. That is a proposal about who holds the gate, written by someone standing near the front of the line to hold it. It may even be a good idea -- a real review body for frontier models is not a crazy thing to want. But call it what it is: a bid for control of the chokepoint, not a retreat from the idea of a chokepoint. The same adviser who torched the restriction push torched this too: "The rest of the world won't play by our rules if we bog ourselves down."

## The fear, and the company selling relief from it

Lane three, and this is the one that should feel familiar, because I wrote its prequel four weeks ago.

In "The Kill Switch You Didn't Know About," I told you the US government had, for the first time, used export controls to reach into the market and pull a working AI model out of it -- foreign access to two frontier models suspended by directive, no warning, no vote. That was not a hypothetical. A careful legal writer at Lawfare confirmed the mechanism this month and put the principle plainly: only Washington can make the assurances a foreign buyer wants, and only by binding itself -- which it has shown it will not reliably do.

So a market has opened for exactly that fear, and Europe's Mistral is standing in it. Its CEO told EU finance ministers this month that Europe has roughly two years to build its own competitive AI compute before dependence on American providers becomes structural and very hard to reverse -- and in the same stretch, Mistral is shipping its own frontier open-weight model and positioning itself as the sovereign alternative for anyone who does not want a foreign memo able to switch their capability off. The kill switch I warned about at the start of the month is now, four weeks later, a European sales pitch. That is how fast a control problem becomes a business model.

## Three lanes, one missing thing

Step back and the three fights rhyme. Washington wants to control which models exist and can't enforce it. Hassabis wants to control the gate they pass through and is honest enough to design it. Mistral wants to monetize the fear that someone else controls the switch. Three different hands reaching for the same lever -- the right to decide what AI runs, where, and for whom -- and not one of them is operating inside a framework anyone agreed to. Everybody is improvising, at the scale where improvisation used to be unthinkable.

Yesterday I showed you a country adopting AI at six times the expected rate with its rulebook still a promise. Today is the same picture one level up: the superpowers doing model policy by directive, reversal, and press release, while the capability itself slips out the back door onto everyone's hard drives. The spice must flow. Herbert was right about that part -- he just never imagined it would flow for free.

## So, Thursday

You do not get a vote in any of these three fights. That is the uncomfortable part, and I am not going to pretend otherwise. But you do get to decide your exposure to how they resolve, and that decision is available to you right now, in daylight.

**It is an inventory question, the same shape as Monday's and Tuesday's.** Which models does your business actually depend on? Whose jurisdiction are they governed by? If one of them gets pulled off the market by a memo next quarter -- the way two of them already were -- what is your fallback, and how fast can you reach it? A business with exactly one model dependency, from one vendor, under one export regime, is a padlock waiting for a reason. A business that knows its options and has spread its supply on purpose is not.

And none of that inventory means anything unless something in your stack can actually enforce the choices you make from it -- which is Friday, and the last question of the week: what does a control actually look like when someone finally builds one, instead of announcing one.

For today, the calculus is just this. The people fighting over who controls the models are not going to protect you, and they are not really trying to. So knowing that -- does it change what you'd pay to control your own exposure, before the next memo lands? Or is it one more geopolitical headline to file away, buried in a news cycle that never even seems to pause, let alone stop?

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that three separate powers are fighting for control of the AI models -- and the one thing none of them can actually deliver is control.*

<!-- [Lars/editors -- pre-publish gate]: Dated Thu 30 Jul, drafted 23 Jul off the "three concurrent lanes" gate. Before it ships, re-check (per week plan): (1) whether the open-weights EO broke or moved by ~29 Jul -- if it BROKE, it becomes the lede and this restructures around it; if still stalled, the "four shelved attempts" framing holds. (2) Kimi K3 weights were promised 27 Jul -- confirm they actually shipped before the "three days before I sat down" line + the "Bring the Model Home" callback run. (3) Sacks's exact title is contested across sources -- kept generic on purpose; confirm before adding a title. Full detail: References\research_control-week-sweep_2026-07-21.md Front 2. -->
