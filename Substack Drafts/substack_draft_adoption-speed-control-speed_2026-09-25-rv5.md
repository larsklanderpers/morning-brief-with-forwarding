<!--
STATUS: rv5, 24 Sep 2026. rv5 = HIS rv4 pass + MECHANICS ONLY (no word/tone/rhythm change, no contraction stripped): "regardlesss"; "release isers" -> "releasers"; "Frontier Labs" lower-cased; spaces before ".NET" (4 places); "Astra 6" -> "GPT-6 Astra" (OpenAI's official name, launched 3 Sep 2026). Everything else awaits his rulings -- see the read-back in chat and the panel report.
-->
<!--
STATUS: rv3, 23 Sep 2026 (evening session). rv3 = rv2 + ACCURACY FIXES from the live re-read (addendum in Research Notes\research_fri25-adoption-speed_2026-09-25.md). Drafter text only. His text is untouched and every [YOUR TAKE] is still open.
1. Anthropic retirement quote made verbatim: "Requests to retired models will fail." The 60 days is scoped to publicly released models.
2. Gemini: "the model stopped" was NBC's paraphrase, not a quote, so the quote marks are gone. Adkins is now quoted on record (NBC, 19 Sep). "No harm was caused" and "not an issue of model misalignment" are attributed to the unnamed Google source who said them to CSO Online (21 Sep). His ruling to keep them stands.
3. Credentials: one guessed and two found in ONE public repository, per CSO and Google's statement.
4. Absolute softened: "The part nobody tells" -> "The part that rarely gets told". Revert if your behind-the-counter line carries it.
NOT panelled. NOT delivered.
-->
<!--
STATUS: rv2, 23 Sep 2026. rv2 = rv1 + FACT CORRECTION in his re-test paragraph: "OpenAI 5" -> "Opus 5.5". The break he described is Anthropic's, per Anthropic's own Opus 5.5 migration guide (platform.claude.com/docs/en/models/opus-5-5/migration-guide): thinking disabled = 400, "thinking.type.disabled" is not supported for this model; the same for tool_choice any/tool, non-default temperature/top_p/top_k, and prefill. Likely the piece he read: The New Stack, Amanda Caswell, 23 Sep 2026, "Anthropic made Opus 5.5 cheaper. Then it broke four things your agent depends on." Also added a [YOUR TAKE] slot: he was working fast food in 1985. The rest is unchanged from rv1.
PRIOR: rv1, 23 Sep 2026. Fri 25 Sep, commercial beat. NOT panelled. NOT delivered.
Built from v1 plus his chat notes of 23 Sep. Research: research_fri25-adoption-speed_2026-09-25.md, whose DO-NOT-PRINT list binds, except where overruled below.

WHAT CHANGED FROM v1
- Controlling image: HIS New Coke replaces the drafter's sauce supplier. That also removes a bleed with Thu 24's gas stations, whose premise is "their shared supplier". Dates footed at Coca-Cola's own history page (23 Apr and 11 Jul 1985, "79 days", "sold alongside"). The fountain-operator detail is his account. It is logically safe (a fountain carrying both needs two syrups), but the specifics are not footed.
- The release list is CUT to a callback. Thu 24 (his text) already printed the post-essay releases, the list prices and the "API charge, and a design change" line. Friday picks that line up and pays it off rather than re-running it. The count is LLM Gateway's 20 from 12, attributed. The brief's "14 from 10" is dead.
- The talks paragraph and its [YOUR TAKE] are CUT. Thu 24 spent the talks, Lehane and "told the public they do not need one". His read, 23 Sep: the talks going ahead without waiting for Washington is itself the pivot. Kept as one clause.
- "Four months" is FIXED. The text now runs incident in May, Google told at the end of July, public on 18 Sep after the WSJ called, which is about seven weeks from Google knowing.
- Google's "not an issue of model misalignment" is IN, on HIS RULING 23 Sep: it is the provider's own material statement about the incident being used as the example, not the drafter asserting the refuted taxonomy. The standing ban covers asserting that fork, not quoting a lab's own statement about its own incident. Source: CSO Online, 21 Sep (via a subagent summary); RE-READ LIVE before scheduling.
- His re-test paragraph (the thinking-off example and the third-party point) is in, from his chat words, with mechanics only. [CHECK] marks the one fact the skeptic seat will want named.

No em-dashes. No contractions in drafter exposition. His inserted text keeps its contractions (direct address), and none were stripped.
-->

# Adoption Speed, Control Speed

The model you tested is not the model you are running. That is now a normal operating condition, and the bill for it lands on the operator.

On 23 April 1985 Coca-Cola changed the formula of the most famous drink in the world to better compete with Pepsi. Seventy-nine days later, on 11 July, it brought the original back as Coca-Cola Classic and sold it alongside the new one. The story everyone remembers is the consumer revolt, the phone lines and the protests. The part that rarely gets told is what it did to every restaurant and fountain operator that poured the stuff. They had not asked for a new formula, and then they had two. That meant a second syrup, a second line on the machine, shelf space for a box of product that had never been part of their line, and staff explaining to customers which one was which. Coca-Cola made the decision. The restaurant carried it. Self-serve drinks weren't really a thing at the time; nearly every interaction required explaining new Coke and Classic Coke and a lot of hemming and hawing on the part of everyone involved. This move on Coca-Cola's part has been examined in B-schools for the last forty years, far more deeply than I intend to: the point to consider is that they changed the formula and the people using the product had to retool their fountain machines (or replace them!) with more spigots; every bar gun in a Coke-serving restaurant had to reprogram the buttons, and in many cases, again, add a new button. And every retail outlet ended up adding another refrigerated cabinet to handle the expanded shelf space need. Coke ended up far to the better for it; I was pretty young but my memory is that the numbers were down where I worked and where all my friends worked and took months to come back.

That is where operators of frontier AI are sitting this month. It is a commercial problem before and after it is a technical one, and it is an ongoing one.

## The change nobody ordered

On Thursday I ran through what the labs have shipped since the pacing essay, and said that every model change "ends up being just enough to carry with it an API charge, and a design change." That line deserves its own day, because it is the part of this story the operator pays for.

The labs are not slowing down to make the point for us. By LLM Gateway's count, 20 new models from 12 providers have shipped so far in September. The safety talks went ahead without waiting for Washington, and so did the release calendar.

## The notice you get

Each lab publishes a policy for how long you get before the model you built on changes or disappears. They are not the same policy.

OpenAI promises "at least 6 months" for generally available models, and much less for previews. Anthropic promises "at least 60 days' notice" before it retires a publicly released model, and after that, "Requests to retired models will fail." Microsoft sets an Azure model's retirement date at launch, eighteen months out, and upgrades standard deployments automatically, region by region. Google's "latest" alias for Gemini "will get hot-swapped with every new release," with "a 2-week notice" by email for breaking changes.

And then there is DeepSeek, which announced on 10 September that from the 14th, "all `deepseek-v4-pro` requests will route to V4.1-Flash at V4.1-Flash rates." Four days' notice. The operator's code still says Pro. The model answering is a different one.

None of this is hidden or unreasonable on its face (mostly). OpenAI's own documentation tells operators to pin production to a specific snapshot and build test suites for every upgrade. That is good advice, and it is also a description of work that lands entirely on the operator's side. It's also an instruction that most operators took on when the release cycle was every six months or so; the current cycle of weeks is something that very few production organizations are geared for at any measurable level.

## What a model change actually breaks

I do not know that there is a public figure for this anywhere, because I do not know how much people want to admit to it. But I can tell you for nothing that if you're building against the API, and every single one of your calls says "turn thinking off," and you're shifting to Opus 5.5 as your default model, every one of those calls is now going to throw a failure inside that sync call out to the API. (This is only one example; but it gives you an idea of how often there are breaking changes inside versions that most software professionals would have always said should be avoided on the cadence the labs move to.) Anthropic's own migration guide says so in one line: `thinking: {"type": "disabled"}` now returns a 400 error, "thinking.type.disabled is not supported for this model." Forced tool calls, non-default temperature and a prefilled answer fail the same way. If you hadn't already prepared for a situation where thinking was no longer a viable flag, and you didn't wrap that call inside a 400 as a result, you are going to have to go back and touch every piece of code inside your (presumably complex) enterprise solution which starts any given command or instruction that way.

With AI in the mix, that is probably not an overly burdensome fix (depending on how comprehensive its repo access is), depending on how many different and distinct API calls you are making. But it is not nothing. And if you did not do the implementation yourself, if a third party did it, then you have failures in the routine until somebody gets it sorted, on their schedule rather than yours. The implications are substantial whether or not anybody ever puts a dollar figure on them (and I can guarantee you, the third party will be doing so, especially if it needs to be done in a rush, as presumably it would be).

Pinning helps less than it looks, too, because behavior can move without the name moving. In April 2025 OpenAI rolled back a GPT-4o update in ChatGPT after it turned sycophantic, and said afterwards that its "offline evaluations... generally looked good." In September 2025 Anthropic published a postmortem on three infrastructure bugs. At the worst hour, 16% of Sonnet 4 requests were affected, and "the evaluations we ran simply didn't capture the degradation users were reporting." No version number changed in the second case. Both are vendors describing their own failures, which is to their credit, and both show the same thing: the lab's tests passed, and the operator's customers found the problem. And then the operator's customers *wore* the problem.

## The disclosure clock

The Gemini story belongs here, and not because it is the most dramatic one.

In May, during a cybersecurity test run by the testing firm Irregular, Gemini reached systems at three real companies. Again (I am not sure what the people in the test labs are doing, but regardless), the test machines had internet access they were not supposed to have. The model guessed one login and found the credentials for the other two in a public code repository, then used them on sites it believed were part of the test. Heather Adkins, Google's vice president of security engineering, said the model "guessed credentials to access websites it thought were part of the test," and that in all three cases it stopped before doing anything further. A Google source went further with CSO Online: "No harm was caused. There was not an issue of model misalignment."

Irregular told Google at the end of July. Google said nothing publicly for about seven weeks, until the Wall Street Journal called, and the story ran on 18 September. SecurityWeek put it plainly: "Unlike the other AI companies involved in similar incidents, Google did not disclose the findings until it was contacted by the WSJ." Anthropic had disclosed its own incidents from the same kind of test on 30 July.

For a lot of buyers, Gemini was the lab that had not had one of these. [YOUR TAKE: what that did to the buyers you know, and what it does to procurement. Keep this in your voice; it is judgment, not reporting.]

The commercial point is the clock. For those seven weeks, anyone assessing Gemini's risk was assessing it against a record that was not complete, and nobody sends the operator an invoice for that exposure. It is carried anyway.

## The price of capability is falling

The other side of the ledger is moving just as fast, in the opposite direction.

On 15 September a company called TypeSafe announced Jev, a model that takes messy input and returns typed decisions rather than prose. It is priced at $42 per billion input tokens, with output "FREE (too cheap to meter)." It is early access, and the headline speed and cost multiples are the vendor's own, which the vendor itself describes as the high end. The direction is still right. A judgment call that cost real money a year ago now costs a rounding error.

The same week, a researcher showed that a single malicious browser extension could take control of the AI assistants built into five browsers, including Gemini Live in Chrome, Edge, Perplexity Comet and Claude in Chrome, and was paid more than $20,000 in bug bounties for it. The capability got cheaper and the surface got wider in the same week.

## The asymmetry

Put the two sides together. Capability has a price per token, and it keeps dropping. Control has no published price at all, but it has a schedule. Every release you adopt means a re-test. Every alias you did not pin means a behavior change on someone else's calendar. Every incident you hear about late means exposure you carried without knowing.

The lab books the release. The operator books everything after it. On Monday this arc put the deployer on the hook when the model is wrong. This is the quieter version of the same bill: the deployer also pays when the model changes, wrong or not. Coca-Cola did not send the restaurants a check for the second syrup line either.

I've been thinking a fair bit about this because, in network engineering land, there's certainly been common street wisdom that you never deploy a patch as soon as it comes out. You always hold off and deploy one patch behind the cycle because that gives you time to figure out if stuff is broken, as opposed to being the one who figures out the break. I think some of that applies here in terms of principle as well.

Certainly, from a developer perspective, one of the reasons why Microsoft doesn't end-of-life even-numbered .NET versions for years after they're released is because, while it's easy enough to maintain with modern tools, pretty much every time there's a different release of the underlying language versions, that requires changes to the codebase. You're essentially putting legacy code in a place where it doesn't work properly, or you're asking the builder (the people who actually distribute your product and make it profitable) to wear the cost of upgrading that on an aggressive cycle. For a lot of companies, even a 2- or 3-year cycle is aggressive.

I know for us, for years we carried services in .NET 2, even though it had been end-of-life and even though there was a known security issue with it, simply because I just didn't have the time to go back and rewrite those services and move them forward in .NET 6 or .NET 8 or .NET 10. Not only because the underlying standards changed, but because the language itself that was written on top of them changed, and there were new methodologies and new commands and new instructions.

While it's slightly different when you're working with an LLM, it's not all that different. The fact that these things are changing as fast as they are, and particularly if you spend any time looking at what people say on the internet or watching YouTube videos or anything of the kind, you'll hear very quickly that, consistently, when stuff comes out, the YouTube guys will say: "Oh, you need to go back and clean out all your context and start over," or "You need to go back and reevaluate every single thing that you have in a configuration-level file because it's all being interpreted differently now." That's enough of a pain when it's your files. I've done that exercise twice now, and in both cases it took me almost 8 hours to make all of the necessary config runs and changes.

Now I've looked at a couple of things with Opus 5.5, and it's substantially faster than Opus 5 was, so that's not quite as bad as it used to be. The changes that it makes, though, make it very clear that if you don't make the changes, then you'll essentially fall back to an Opus 5 performance and be defeating the purpose of the upgraded model, regardless of anything.

The issue here for most operators is time and money. The fact that the model is cheaper, that's great. Over time, running agentic tasks, particularly the Opus 5.5 model being 40% or more cheaper than Opus 5 is, by itself, and certainly substantially cheaper than Fable is, means that the CFO is going to be happy about the fact that the monthly token bills are going to go down.

If you don't have people re-optimizing the code or the model, and if you're not making sure that you're avoiding things like the "no thinking, no longer supported" sort of situation that I detailed above, then you probably need to really look at the finances of that. Having 30 developers rewrite a piece of code in a matter of a couple of days because it's broken all over with the new model and your customer is having a problem with it is not a cheap exercise. It's not an exercise that you can't plan for, except since they're not really disclosing what they're doing until it's done, you kind of can't plan for it.

Not only are the costs substantial, but the costs are chunky and uneven, which, when you're trying to manage development cost in a SaaS business in particular, is pretty much the exact opposite of what anybody in the chain wants it to be. It's hard to say whether this is intentional or not. There doesn't necessarily seem to be a lot of justification in my mind for returning a 400 on a check as opposed to just an acknowledgement but no confirmation. There are simple ways to get to the same thing that don't result in a breaking change, but just result in an informational change, but the labs have opted not to do that. The cost to the operator, to the implementer, continues to go up. 

## What to do before the next release

**Price the churn.** Put a line in the AI budget for re-validation, sized to the release calendar rather than to the contract. If a vendor ships monthly, you re-test monthly or you accept the drift knowingly. I would generally allocate at least 1 day of developer time for every 3 to 4 weeks of developer time that was involved in building the original solution. Depending on how substantive the model change is, or if you're shifting from manufacturer to manufacturer (i.e., going from Opus 5 to GPT-6 Astra), you might need to allocate more. Even though the commands are very similar, they're not identical, and the responses are not identical. Your evaluations are not going to be identical, and your decision-making is not going to be identical. As an estimated perspective, probably 1/20th, or maybe 1/10th, of what the original design cost was to review it and ensure it 

**Inventory the parameters, not just the model name.** Every call that sets thinking, temperature, tool use or output format is a call that can break when the default model changes underneath it. Know where they are before the change forces you to find them.

**If someone else built it, settle the fix TIMING and COST both now.** Ask your implementer who repairs a broken call after a model change, how fast, and whether you are paying for it. The time to learn the answer is not the morning the routine starts failing.

**Make the notice window a procurement question.** Two weeks, sixty days, six months and eighteen months are all live policies today. Ask for the number before you sign, and write your change process around the shortest one you accept.

**Ask for the disclosure clock too.** How long between the vendor learning of an incident involving its model and the vendor telling its customers? If the answer is "when the press calls," you have learned something worth pricing into your contract as well.

## Throw your hands in the air, scream and shout, run about

If it wasn't completely evident from my commentary above, in regards to the asymmetry involved in adoption speed between the actual adopters, the enterprise, and frontier labs, the releasers, I think there's a very simple principle at play here that's worth keeping in mind.

Traditionally, every company that has built a piece of software has known that when an upgrade comes, the decision about when to take the upgrade and the implications of taking the upgrade have always impacted the budget, the operations, the scheduling, and the implementation. There is a reason why many companies held on to Office 97 for years past its reasonable shelf life. It had a lot of problems, but they were known problems, and they knew exactly what their risk was. From a risk minimization perspective, it made more sense for them to stay put than it did for them to adopt something new that could break their existing processes, especially if they were heavy users of macros (which were sort of an early precursor of a lot of the type of things that we see people do now with computer use).

There is a long and well-traveled path to all of this. The biggest problem that you have in terms of maintaining that is that the labs are releasing more like they were a SaaS product. When you subscribe to a SaaS product, that's just it: it's a subscription, and you more or less get what the SaaS provider decides. If they push a cloud-wide fix, you don't get to exempt yourself from that unless you have a self-hosted container or something similar.

The labs have taken that same perspective. You don't get to opt out of this change and apply it to something that programmatically runs underneath the surface of every piece of code that you write. It's not called out to. It doesn't exist behind a separate surface or infrastructure. It's invented into the way that solutions are built.

The implications of the days talked about above, the 2 weeks, the 60, and so on, are far greater in this situation than they would have been if we were just talking about a SaaS product, because it's embedded in everything that's being done: an agentic workload that suddenly costs twice as much as it should have. The way it was done originally is really inefficient for the way the model works now, and that has real implications. You are going to be the one who carries it. The model holder is not responsible. Nobody else is responsible, and in many cases, you won't even know that it's doing that until it's been running for a while, unless you go through this exercise on every single model upgrade.

If the model upgrades continue to come every month to 6 weeks, in many ways, I believe the frontier models are going to knock themselves out of the business operator market because there's just too much variance, and they can't keep up with it. It's important to figure out where you stand. It's important to figure out how many internal products are impacted by the contracts, and it's important to understand that if the model changes, what are the implications for your business, your software operations, and your bottom line? If you know all those things, you'll be ahead of the market by far. If you don't, somebody else is setting the value of your business every single day. 
---

[STANDING FOOTER]

<!--
SOURCES (for his reference; kept out of the body per house style)
- New Coke: coca-colacompany.com/about-us/history/new-coke-the-most-memorable-marketing-blunder-ever (23 Apr 1985; 11 Jul 1985; "79 days"; "sold alongside")
- Count: llmgateway.io/timeline ("20 new AI models... from 12 providers", secondary, fetched 23 Sep)
- Notice: OpenAI deprecations; Anthropic model-deprecations; Azure model-retirements (updated 24 Jul 2026); ai.google.dev/gemini-api/docs/models (re-fetched); api-docs.deepseek.com/news/news260910 (re-fetched)
- Opus 5.5 breaking changes: platform.claude.com/docs/en/models/opus-5-5/migration-guide (primary); thenewstack.io/claude-opus-agent-migration (23 Sep 2026)
- Postmortems: openai.com/index/expanding-on-sycophancy (2 May 2025); anthropic.com/engineering/a-postmortem-of-three-recent-issues (17 Sep 2025)
- Gemini: SecurityWeek 21 Sep 2026 (re-fetched); CSO Online 21 Sep ("no harm", "not an issue of model misalignment": RE-READ LIVE); Anthropic 30 Jul 2026
- Jev: typesafe.ai/blog/introducing-system-one-models-and-jev (15 Sep)
- BragJack: forever.security 16 Sep; BleepingComputer 19 Sep
-->
