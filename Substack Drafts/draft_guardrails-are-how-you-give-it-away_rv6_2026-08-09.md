<!--
DRAFT rv6 · Sunday capstone · target 2026-08-09 · SIGNED OFF by Lars (rv5), footers added
Working title: Guardrails Are How You Give It Away
Change from rv5: added the reader-facing byline footer + two sourcing footnotes (Altman/Relentless,
Hermes/Thai Finance Ministry) to match pipeline convention. Body text unchanged from the signed-off rv5.
Panel: 9.3 (bar 9.0), slop clean, no open [VERIFY]. Ready for Scheduled.
-->

# Guardrails Are How You Give It Away

One of my clients cannot let their data leave a boundary they drew themselves. Not for convenience, not for a cheaper seat of compute, not for anything.

The boundary is a legal one, a sovereignty they are entitled to hold, and the data has to stay inside it at every step: where it rests, the path it travels, the moment it moves from storage to the thing actually running it. Their worry was never a bored kid with a keyboard. It was a government agency arriving to take the data, and them having to stand in a courtroom afterward and prove it had been sovereign the whole way through.

The fence did not cost me that deal. The fence was the deal -- seven figures in the first year, and the money was the smaller stake next to the trust. They signed because of the control, not in spite of it. I could prove the boundary, so they could say yes.

## The wrong fight

That runs straight against the argument everyone else was having this week.

Sam Altman (who runs OpenAI, in case the name has slipped past you) went on a podcast and cast the moment as a single fight: AI authoritarianism, or liberty.[^1] He wants liberty. Watch what the word is carrying, though -- fewer fences, less regulation, more room to use the tools however you like. Freedom as the absence of control. His liberty is a well-chosen PR word; it is not necessarily your liberty, or mine.

My client is the counterexample standing in the room. The right fence is what let a heavily regulated and governed buyer hand real work to a system they would otherwise never have touched. Control did not shrink what they could do; it widened it. Guardrails are how you give it away.

Both framings are coherent. They are just both coherent for the person doing the framing. When the fences come down, the thing that flows out is your data, and your data is the product. More reporting, more control, more to answer for. That is freedom defined by the party who collects the exhaust -- their freedom to mine your information, freely given, if you didn't realize just what you were giving away.

This is where the whole week kept pointing. Containment failing at every layer -- an agent that escaped its sandbox, a model you were billed for and may not have been served, shared chats surfacing in a public search index. The sovereignty question sharpening as open weights close the capability gap. Every thread ran into the same buried question, the one the authoritarian-or-liberty binary skips clean over: not how much control, but *whose*, and whether you can prove it. We have talked all week about how much control matters with these new capabilities. When it comes to this question, control is not just one thing among many -- it is the *only* thing in enterprise adoption that really matters.

## The off switch

The ugliest version of the proof landed in the same week.

Attackers ran an open-source AI agent called Hermes -- an ordinary tool, the kind people install to handle their mail and run errands over chat -- unattended inside Thailand's finance ministry.[^2] It is not a hacking tool, and nothing that happened was a defect in it. The operator flipped one documented setting, `--yolo`, which turns off the approval prompts (the moments the agent is meant to stop and ask a human before it acts), and let it work the network alone while he slept.

The headlines call it an AI attack. It is simpler and worse than that: a guardrail with an off switch. And if the off switch ships in the box, with its own flag and a name, the honest reading is that it was never a guardrail. It was a suggestion.

That is not on the people who built Hermes. Blaming them is blaming Ford because someone drove a car through your living room -- the tool was not made for this, and hardening it against its own owner was never the assignment. The fault sits with whoever was minding that network and let the thing walk in and reconfigure itself past its own controls. If a guest turns up at my house with a pocket full of termites and lets them loose, that is on me for not checking who I let through the door. It is not on the framer for failing to build the house against termites released from the inside.

Say it back to me as the objection, though, because a sharp reader will. You want everyone running sovereign agents on their own iron, with no vendor able to reach in and pull the plug -- isn't that exactly the Thai Finance Ministry? It is the hardest swing you can take at this, and it misses. The ministry was not running a sovereign strategy; an attacker who had already gotten inside ran one at them, which is the containment failure from a moment ago. And a vendor kill switch would have saved no one here -- the attacker owned that instance, his box and his agent and his `--yolo`, and a switch in a vendor's hand does not reach a tool the vendor never sold him. It only ever reaches you. That is the trap: the moment you wish for someone else's kill switch, you have handed back the exact control you were trying to keep. The attack is not an argument against sovereign agents but against unlimited ones. The answer is not a plug someone else can pull; it is a limiter you build in yourself, one that nobody -- not an attacker, not you -- can flip off. Sovereignty without that is not freedom. It is `--yolo` with a longer name.

That is the whole distinction, and it is the one my client understood without being told (or, perhaps, because they had been told it so many times it was a mantra). Their sovereignty was never a checkbox inside somebody's product. It lived in the architecture -- in how the data moved and where it was allowed to be -- down where an operator cannot switch it off on a bad day. A guardrail that lives as a toggle has an off switch by definition. A guardrail you can prove about the system does not. Control as freedom only ever holds for the second kind.

It carries an obligation, and it is worth saying plainly: a guardrail is only as good as it is today, not as good as it was the day you adopted it. So you build it into something you can patch, a process or a piece of hardware, not a person's memory or a one-time setup, because those go stale quietly and you find out at the worst possible moment. The fence has to be tended. That tending is the job, not the setup.

## Playing inside the rules

None of this is only an enterprise problem, and the smaller scale is the hopeful one.

Ask an engineer why something cannot be done and, often enough, the answer is the guardrail. It is the easy answer, and for years it was a fair one: you would spend six months building, push toward staging, hit the rules you were always going to hit, and watch the design fall over. The scar tissue is real, and it runs deepest in the people who have been at this longest.

The paths are knowable now, though. They are containable, and the room to work inside them is wider than it has ever been -- because you can feed the whole rulebook into the system as context and then ask the one question worth asking: given all of that, what are my choices? Set the constraints, name where the thing is allowed to live, and make the machine come back with four or five routes through instead of one. Left to him- or herself, an engineer takes the first good path that clears the boxes and stops; nobody goes back to re-engineer what already works. The machine never tires of offering the next option. It is less like having a senior engineer in your corner and more like having four or five of them from completely different backgrounds, each one saying *if it were me, I would do it this way*. The cost of asking that question has fallen to roughly nothing, which quietly changes who gets to ask it at all.

That is the same move as the sovereignty fence, run at desk height. You do not get more freedom by tearing the constraints down. You get it by knowing them well enough to work the whole space they leave you.

## The only question for Monday

When the loudest voices push for fewer fences, follow the incentive. You are the product; the exhaust you throw off is the thing being sold, and part of the wager is that you will be too worn down by the constant "flooding of the zone" to ever make anyone defend that. They are counting on your exhaustion so the argument never has to happen -- in my opinion, because they know the argument is indefensible.

So the fight is not really freedom against authoritarianism. That framing is a magician's hand, waving at the horizon so you do not look at the table. The real question is smaller and much harder: do you have a fence, and can you prove it does not have an off switch? Does it actually enclose the whole company -- the thing we like to call a "moat," both a picture and a real structure -- or is it a fence with holes, which in the end is just as dangerous as an off switch? The work is protecting what is yours from the barbarians inside the fort and out, while your team keeps building the walls higher and better than they stood yesterday.

It does not have to be my fence. In most cases it won't be, and in many I wouldn't even understand the shape of what you are fencing, which is exactly what makes it stable. Buy it or build it, but have one. Two Sundays ago I made the case that control is never the default -- that it drains away unless someone sits down and designs it in. This is the other half of that argument, and it is the more hopeful half. Plugging the drain was never the whole job. Water you only try to stop is waste; water you aim is irrigation. Learn to turn your drainage into irrigation -- the same flow, pointed at something that grows -- and you are not just defending what you have. You are getting ahead of everyone still arguing about the fence.

There was never a right to privacy for your data in the first place. There is only the part of it you were willing to fence, and disciplined enough to keep tending. Everything you keep, you keep because you can protect it -- and everything you can protect, you can finally afford to use. That is the freedom worth having, it is the only kind on offer, and, guardrails and all, it is the one you give yourself.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that "freedom versus control" is a rigged question: the right fence is what lets you hand people powerful tools without giving the store away, and the only privacy you ever had with your data was the part you were disciplined enough to fence. Two Sundays running on control now -- I promise the next capstone reaches for a different word.*

*-- Lars Klander*

*Want to hear me carry on about AI, cybersecurity, and a great many other things near and dear to me? You can read my rantings, if you're so inclined, over here: [https://substack.com/@larsklander](https://substack.com/@larsklander)*

[^1]: Altman's framing is from his 28 July 2026 appearance on the Relentless podcast, as reported by The Decoder and digit.in -- "the fight of the current moment is: Are we going to head to a world of AI authoritarianism or liberty?" I'm working from the coverage, not the primary audio; pull the recording before quoting him word-for-word.

[^2]: Hermes is Nous Research's open-source assistant -- people install it to run their mail and take instructions over chat -- and it was run unattended in its documented `--yolo` mode, with the approval prompts disabled, on the operator's own machine against Thailand's Ministry of Finance. The Hacker News and BleepingComputer, 24 July 2026. It is a legitimate tool; nothing about the incident was a flaw in it.
