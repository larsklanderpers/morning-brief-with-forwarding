# Every Correction You Make Is Feeding Them

**Status: Draft rv1 -- editor-panel round 1 applied (round 1 scored 8.86; fixes 1-14 + skeptic-rebuttal close in). Target Tuesday, 28 July 2026. Awaiting Lars's read.**
**Series: Weekday feed**
**Thread: AI Sovereignty / NEW: Ambient AI Privacy Drain (Piece 1 of 4)**
**Builds on: Monday's "Fifty Agents. Five Humans." (27 Jul); "Not Where It Lives. Where It Thinks." (10 Jul); "You Are the Product" (30 Jun); Sunday's capstone "The Model Was Never the Hard Part" (26 Jul). Sets up Friday (the enforcement layer) and Ambient Pieces 2-4.**
**Source spark: Nadella's "Reverse Information Paradox" essay (12 Jul, via X); The New Stack + IQ Source critiques; Trinidad v. OpenAI (IPWatchdog, Apr 2026). Fact-check: References\research_control-week-sweep_2026-07-21.md -- quotes verified against the essay text; no provider policy has changed in response as of 21 Jul.**

---

Your best analyst corrected an AI's draft three times this morning. The corrections were worth more than the draft.

That is the whole story today, and I want you to hold onto how ordinary that scene is while we walk through what it actually costs. Nobody uploaded a file they shouldn't have. Nobody pasted source code into a chatbot. Nobody broke a policy. Someone competent just did their job -- looked at what the machine produced, knew better, and fixed it. Yesterday I told you those two-to-five humans supervising the agent factory are the control layer. Today I have to tell you what their control work produces, and where it goes. It's the first of four pieces I'll be writing on what I've started calling the ambient AI privacy drain, and today's job is the problem itself.

In mid-July, Satya Nadella, CEO of Microsoft, published an essay that named it. He calls it the Reverse Information Paradox, and coming from the man whose company sells Copilot, it reads less like thought leadership and more like a confession with the serial numbers filed off. Models learn from what he calls exhaust: "the prompts people write, the tools agents use, and especially the corrections people make when the model is wrong." His summary line deserves to be quoted whole, because I could not put it more plainly: "you essentially pay for intelligence twice, once with money, and again with something even more valuable: the proprietary knowledge you must reveal to make that intelligence useful."

You pay twice. At least. And more importantly -- you keep paying twice, over and over again, every time the context is re-interpreted, every time the agent runs the same process for you each morning, every recurring task run on a closed-weight model learns from every iteration. And it costs you to run and you lose your IP with every turn.

## The apprentice who works for someone else

Here is the analogy I keep landing on. Imagine you hired the most gifted apprentice in the world. Tireless, fast, never takes a sick day. There's one clause in the contract you skimmed: the apprentice is employed by another firm, reports back nightly, and never forgets a thing you showed them.

Every time your senior people correct that apprentice -- no, we don't price it that way; no, that client hates that phrasing; no, compliance would never clear that -- they are doing the most valuable kind of teaching there is. Not the textbook knowledge. The judgment. The twenty years of "I've seen this go wrong before" that we spent two weeks in July establishing as the load-bearing asset. Except the student writes it all down, takes it home each night, and the notebook stays there.

That is what a correction is. It is the distilled difference between what a generic model knows and what *your business* knows. And under the standard arrangement, it flows one way. The asymmetry is the part even the essay underplays: your provider learns about your operation continuously, and you learn precisely nothing about what is done with it.

## Not a breach. Worse.

I want to be careful here, because the security-newsletter reflex is to file this under data leakage, and that framing undersells it badly.

A breach is an event. It has a timestamp, a scope, a disclosure obligation, an incident channel. This has none of those. No single interaction crosses a line: this prompt is innocent, that correction is trivial, this document summary is routine. *There is no moment at which anyone made a decision a policy could have caught, which is exactly why your policies haven't caught it.* 

But run the aggregation. Five hundred people, each having thirty AI interactions a day -- Copilot in the spreadsheets, an assistant in the chat channels, a chatbot on every phone. Within a quarter, the accumulated exhaust describes your operating model: what your people escalate and what they wave through, who approves what, how you price, which clients get the careful language, what your internal shorthand means, where your margins actually live. Not your PII (that, ironically, is the one thing everyone learned to protect years ago -- a regulation for personal information in every jurisdiction, and effectively none for this). Your *how*. The thing that was never in any single document, assembled from ten thousand fragments not one of which was, alone, worth protecting, or even risky enough to ask the question. That means *no policy will ever catch it.*

I wrote a month ago, in "You Are the Product," that we gave the old platforms our attention and we are giving AI our cognition. This is the enterprise version of that sentence. And it sharpens the question I asked in "Not Where It Lives. Where It Thinks.": the sovereignty problem was never just where the model reasons. It's where your judgment accumulates. The moat you spent a decade digging is now a plume of exhaust, and the vendor is downwind with a collector.

## About the messenger

Now, the part that has to be said once so we can move on. This warning comes from the chief executive of the company that sells Copilot -- effectively the most ambient enterprise AI going. The same essay that names the paradox proposes the fix: a "trust boundary," inside which your data, your traces, your corrections, and your organizational memory accumulate to *you*. And Microsoft would be delighted to sell you the infrastructure on which to build one. Critics noticed almost immediately that the remedy deepens exactly the platform dependency the warning describes; Microsoft's on-record defense, for what it's worth, is that Copilot accesses your data but doesn't train its foundation models on it. Note what that defense covers: training the foundation model. Note what it doesn't: the telemetry, the feedback signals, the product-improvement clause your agreement almost certainly contains.

I am not interested in litigating Microsoft here. I am interested in what it means when the person with the best view of the machine tells you the machine works this way. When the casino owner writes an essay warning that the house always wins, you can question his motives all day long. You should still stop assuming you're the house.

## Don't expect the courts to catch you

If you're waiting for the legal system to backstop this, there's a case you should know about, because it is ugly in an instructive way.

In *Trinidad v. OpenAI*, a plaintiff claimed ChatGPT usage had exposed her trade secrets and sued under the Defend Trade Secrets Act. The court dismissed the claim, and the reasoning is the part that matters: by using the tool, she had *voluntarily shared* the information with OpenAI, and accepting terms of service with no confidentiality protections extinguished the trade-secret right. Honest caveats, because I flag them for others and won't skip them for myself: the plaintiff was pro se (representing herself, without a lawyer), and the facts were unusual, so this is a weak precedent -- but a strong illustration. The doctrine it gestures at is old and settled: a secret you voluntarily hand to a third party without confidentiality protection stops being a secret. Nobody in your building thinks of a correction as a voluntary disclosure. The law has no such sentimentality. And one tier up the food chain: Apple is now suing OpenAI over alleged trade-secret theft. The people with the most expensive secrets have noticed.

The deeper legal problem is Piece 3 of this series, so I'll leave it teased: the entire doctrine of trade-secret protection assumes disclosure is an *event*. Ambient exhaust is not an event. Our legal categories are shaped for the wrong physics. And if you think we ended up with the Ad Hoc Regulatory Regime because politics and the law move quickly to catch up with changes on the ground, well, there are a number of frontier labs who have a bridge they would like to sell you.

## The boundary around nothing

Here is the strongest objection to Nadella's fix, and it deserves its own paragraph or two. An analyst outfit called IQ Source put it in a line I can't beat: *"A boundary around nothing is still nothing."*

A trust boundary presumes you can inventory what's inside it. What, precisely, is your institutional know-how? Which corrections carry it? Which of your peoples hundreds of daily interactions are the ones painting the picture? Sunday's capstone ("The Model Was Never the Hard Part") argued that the account you can keep of a machine is the fence around it -- but a fence is drawn around something you can name. Most organizations have never once written down what their operational judgment actually consists of, where it lives, or which systems it now flows through. You cannot protect an asset you have never listed. The vendors will happily sell you the wall anyway. *Making sure you determine what it should contain is, and always will be, your responsibility.* The difference is that now there is an always-on drain that just consumes, always, regardless of your interventions, anything that goes down it. Think about Chartreuse — only two monks alive know it, 250+ years, one holds the only key to the safe. Now compare that to the drain *inside the safe of your enterprise*, where the AI can ALWAYS tell you EXACTLY what the components are (let's call them, say, "tokens"). In such a world, even the monks can't save you.

What the exhaust actually contains -- including the newest kind, because the interfaces are going voice-first and always-listening; the exhaust is getting a microphone -- is Piece 2.

## Six months of corrections

So here is the Tuesday assignment, and unlike most of what I write about, this one costs you nothing but an uncomfortable hour.

**Find out what your agreement actually says.** Somewhere in your enterprise AI contract -- Copilot, Claude, ChatGPT Enterprise, Amazon Bedrock, all of them -- there is language about what the provider may do with your prompts, your telemetry, your feedback signals, your corrections. Someone in your building signed it. Ask them the question in plain words: what is the provider entitled to do with the last six months of our corrections? Not your documents. Not your PII. Your *corrections* -- the judgment layer. In my experience the first answer will be "let me get back to you," and the second answer will be longer and less comfortable than anyone expected -- if you can actually manage to get it at all (because the shape of the problem is so very different from what anyone will have asked about a contract before, no one even has a frame of reference).

**Then ask the harder internal question.** If the answer came back "everything flows to the provider" -- would you even be able to say what you'd lost? Would *anyone* in your business be able to say what you'd lost? Would *the people who lost it* be able to say what you'd lost? That inventory -- what your know-how is, where it leaks -- is the real work, and it is Piece 2's whole subject.

Because the asymmetry only compounds. Every day your organization gets marginally more legible to your provider, and your provider gets not one bit more legible to you. Nadella, to his credit, said the quiet part: you are paying twice. The first invoice arrives monthly with line items. The second one is being collected continuously, in a currency you've never audited, under terms you've probably never read. Friday I'll show you what an actual control on that flow looks like -- not a policy PDF, an execution rule that denies the operation.

But today, just the calculus question, and it's Nadella's own, turned around to face you: knowing that every correction your best people make is feeding someone else's asset -- does that change what you route through these tools, and what you'd pay to keep the learning loop at home? Or is it just one more warning from one more CEO, buried in a news cycle that never even seems to pause, let alone stop?

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the most valuable thing your company produces this year may be the corrections your people make to someone else's model -- and you're giving them away with the subscription.*
