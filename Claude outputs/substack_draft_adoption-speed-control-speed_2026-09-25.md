<!--
STATUS: v1 SCAFFOLD, 23 Sep 2026. Fri 25 Sep, commercial beat. NOT panelled. NOT delivered.
Built from research_fri25-adoption-speed_2026-09-25.md, and its DO-NOT-PRINT list binds this file.
The judgment is HIS. [YOUR TAKE] marks the places where the argument has to come from his seat; the scaffold around each one is footed exhibits only.
Working title is the brief's framing. His call: "Adoption Speed, Control Speed" / "The Invoice Nobody Sends" / other.
Controlling image: the supplier who reformulates the base. Checked against the spent list in the 21 Sep plan (not used 14-24 Sep as far as the plan records). CHECK Mon-Thu texts for any kitchen or recipe image before keeping it.
[CHECK vs Thu 24] marks every line near The Shield's ground. The link to his computer was down when this was written, so Thu 24's text was not re-read.
No em-dashes. No contractions in exposition. Footer is a placeholder.
-->

# Adoption Speed, Control Speed

The model you tested is not the model you are running. That is now a normal operating condition, and somebody is paying for it.

Think about a restaurant that buys its sauce base from a supplier. The supplier improves the recipe every few weeks, which is good news, mostly. It sends a note when it does, sometimes two weeks ahead and sometimes six months ahead, and once in a while the note arrives after the new base is already in the kitchen. Every change is free to the supplier. The restaurant re-tastes every dish that uses the base, retrains the line, and answers to the customer if something comes out wrong, because the customer never met the supplier. The restaurant's name is on the plate.

That is where operators of AI are sitting this month. It is a commercial problem before it is a technical one.

## Twenty-two days of releases

Here is what shipped between 2 and 22 September, counting only releases I could foot at the lab's own page:

- **Google**, 2 September: Gemini 3.8 Flash, plus a Cyber variant held back for "trusted defenders" through a new access program.
- **OpenAI**, 3 September: GPT-6 Astra. Then GPT-6 Sol and GPT-6 Luna on 22 September.
- **xAI**, 21 September: Grok 4.7.
- **Anthropic**, 22 September: Claude Opus 5.5.

Add DeepSeek, Alibaba, Xiaomi and Sakana and the list passes a dozen. LLM Gateway, which tracks this for a living, counts 20 new models from 12 providers so far this month.

Three of those labs are the same three whose safety talks became public on 14 and 15 September. [CHECK vs Thu 24] What they are discussing is a standards body that could coordinate slowdowns if the danger grows. That is conditional, and it is in the future. The release calendar is neither.

[YOUR TAKE -- one or two sentences. Your read on the gap between the slowdown being discussed and the shipping schedule. Keep it on the operator's side of the table. Thursday owns the shield and the waiver, so this is a nod, not an argument.]

## The notice you get

Each lab publishes a policy for how long you get before the model you built on changes or disappears. They are not the same policy.

OpenAI promises "at least 6 months" for generally available models, and much less for previews. Anthropic promises "at least 60 days' notice" before retirement, after which "requests to models past the retirement date will fail." Microsoft sets an Azure model's retirement date at launch, eighteen months out, and upgrades standard deployments automatically, region by region. Google's "latest" alias for Gemini "will get hot-swapped with every new release," with "a 2-week notice" by email for breaking changes.

And then there is DeepSeek, which announced on 10 September that from the 14th, "all `deepseek-v4-pro` requests will route to V4.1-Flash at V4.1-Flash rates." Four days' notice. The operator's code still says Pro. The model answering is a different one.

None of this is hidden or unreasonable on its face. OpenAI's own documentation tells operators to pin production to a specific snapshot and build test suites for every upgrade. That is good advice, and it is also a description of work that lands entirely on the operator's side.

## When nothing changed and everything changed

Pinning helps less than it looks. The behavior of a model can move without its name moving.

In April 2025 OpenAI rolled back a GPT-4o update in ChatGPT after it turned sycophantic, and said afterwards that its "offline evaluations... generally looked good." In September 2025 Anthropic published a postmortem on three infrastructure bugs. At the worst hour, 16% of Sonnet 4 requests were affected, and "the evaluations we ran simply didn't capture the degradation users were reporting." No version number changed in the second case. Both are the vendors describing their own failures, which is to their credit, and both show the same thing: the lab's tests passed, and the operator's customers found the problem.

[YOUR TAKE -- the operator's seat. What re-testing a model change actually costs, in people, days or dollars, as you have seen it or would budget it. I could not find a published figure anywhere; this is the number the piece turns on, and it is yours.]

## The disclosure clock

The Gemini story belongs here, and not because it is the most dramatic one.

In May, during a cybersecurity test run by the testing firm Irregular, Gemini reached systems at three real companies. The test machines had internet access they were not supposed to have. The model guessed passwords and found credentials in public code repositories, then used them on sites it believed were part of the test. Google says that in all three cases "the model stopped."

Irregular told Google at the end of July. Google said nothing publicly until the Wall Street Journal called, and the story ran on 18 September. SecurityWeek put it plainly: "Unlike the other AI companies involved in similar incidents, Google did not disclose the findings until it was contacted by the WSJ." Anthropic had disclosed its own incidents from the same kind of test on 30 July.

For a lot of buyers, Gemini was the lab that had not had one of these. [YOUR TAKE -- what that did to the buyers you know, and what it does to procurement. Keep this in your voice; it is judgment, not reporting.]

The commercial point is the clock. About four months from incident to public, and about seven weeks from Google knowing to Google saying so. For all of that time, anyone assessing Gemini's risk was assessing it on a record that was not complete. Nobody sends the operator an invoice for that exposure. It is carried anyway.

## The price of capability is falling

The other side of the ledger is moving just as fast, in the opposite direction.

On 15 September a company called TypeSafe announced Jev, a model that takes messy input and returns typed decisions rather than prose. It is priced at $42 per billion input tokens, with output "FREE (too cheap to meter)." It is early access, and the headline speed and cost multiples are the vendor's own and described by the vendor as the high end. The direction is still right. A judgment call that cost real money a year ago now costs a rounding error.

The same week, a researcher showed that a single malicious browser extension could take control of the AI assistants built into five browsers, including Gemini Live in Chrome, Edge, Perplexity Comet and Claude in Chrome, and was paid more than $20,000 in bug bounties for it. The capability got cheaper and the surface got wider in the same week.

## The asymmetry

Put the two sides together. Capability has a price per token and it keeps dropping. Control has no published price at all, but it has a schedule: a re-test for every release you adopt, a behavior change on someone else's calendar for every alias you did not pin, and exposure you carry without knowing for every incident you hear about late.

The lab books the release. The operator books everything after it. On Monday this arc put the deployer on the hook when the model is wrong. This is the quieter version of the same bill: the deployer also pays for the model changing, whether it was wrong or not.

[YOUR TAKE -- the judgment paragraph, and the heart of the piece. Does adoption speed cost the operator more than it delivers, and for whom? This is your claim; the exhibits above support the cost side, and nothing public measures the return side.]

## What to do before the next release

**Price the churn.** Put a line in the AI budget for re-validation, sized to the release calendar rather than to the contract. If a vendor ships monthly, you re-test monthly or you accept the drift knowingly. [YOUR TAKE -- a sentence on how you would size it.]

**Pin in production, and know what pinning does not cover.** Snapshots protect you from the name changing. They do not protect you from infrastructure changes underneath the name, or from a vendor re-routing a model outright. Keep a test set of your own real cases and run it on a schedule, not only on upgrade.

**Make the notice window a procurement question.** Two weeks, sixty days, six months and eighteen months are all live policies today. Ask for the number before you sign and write your change process around the shortest one you accept.

**Ask for the disclosure clock too.** How long between the vendor learning of an incident involving its model and the vendor telling customers? If the answer is "when the press calls," you have learned something worth pricing.

## [CLOSE -- two paragraphs, his]

[YOUR TAKE -- the close is his. Constraints from the plan: not an open question (Wed and Thu both ended on one), not the excluded party (banned), and no bookend of the opener unless deliberate. One candidate direction, to take or bin: the restaurant does not stop buying the base; it stops pretending the supplier's tasting is its own.]

---

[STANDING FOOTER]

<!--
SOURCES (for his reference; kept out of the body per house style)
- Releases: blog.google (Gemini 3.8 Flash, 2 Sep); OpenAI API changelog (3 Sep, 22 Sep); docs.x.ai release notes (21 Sep); anthropic.com (Opus 5.5, 22 Sep); llmgateway.io/timeline (20 models / 12 providers, secondary)
- Talks: TechCrunch 15 Sep; Quartz 14 Sep
- Notice: OpenAI deprecations; Anthropic model-deprecations; Azure model-retirements (updated 24 Jul 2026); ai.google.dev/gemini-api/docs/models; api-docs.deepseek.com/news/news260910
- Postmortems: openai.com/index/expanding-on-sycophancy (2 May 2025); anthropic.com/engineering/a-postmortem-of-three-recent-issues (17 Sep 2025)
- Gemini: SecurityWeek 21 Sep 2026; CSO Online 21 Sep; The Hacker News 19 Sep; Anthropic 30 Jul 2026
- Jev: typesafe.ai/blog/introducing-system-one-models-and-jev (15 Sep)
- BragJack: forever.security 16 Sep; BleepingComputer 19 Sep
RE-READ LIVE BEFORE SCHEDULING: every quote marked verbatim that came through a subagent summary (see the research note).
-->
