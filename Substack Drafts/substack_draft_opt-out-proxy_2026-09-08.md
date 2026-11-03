# Your Opt-Out Has an Owner

**Status: DRAFT v1 -- Tuesday, 8 September 2026 (Diversion #1, ground game; short/operational). NOT PANELLED. ~2,550 body words. Em-dash-free; zero contractions outside quoted speech; US spelling. NO open [VERIFY]. ONE open [YOUR TAKE]. He pushes to Substack himself.**
**Series: Weekday feed (Tuesday) · Thread: Ad Hoc Regulatory × Machine Identity · Tier 0 bookend: THIRD entry in the set (Tue 1 first, Sat 5 second), naming Tue 1's skill.**
**Source: References\week-plan_2026-09-07.md Tue 8 block + its 5 Sep AMENDMENT · References\research_opt-out-proxy_2026-09-05.md (all facts footed at primaries 5 Sep) · the six landed pieces Tue 1 - Sun 6, read in full.**

**★ TITLE CHANGED FROM THE PLAN. "Somebody Else Holds Your Opt-Out" echoes Fri 4's "Somebody Repriced the Patch" four days back. Revert freely if he wants the plan's title.**

**ACCURACY DECISIONS MADE IN THIS DRAFT, all from the 5 Sep research note:**
**1. The plan's "reaches the laptop" / "reaching onto personal hardware" framing is NOT used -- it is wrong on mechanism and the piece corrects it in text, at the primary.**
**2. The delete asymmetry (cloud deletable, local not) leads instead of the six-year tail. It is the better fact and it is the thesis in one sentence.**
**3. "Beta" is not used. Cowork and Claude Code endpoints are stable; only Science and M365 are beta.**
**4. The CPO quote is CUT. Twitch's own FAQ makes the concession better and at a primary.**
**5. Consent claim is written narrow: "the documentation describes no user notification, consent or opt-out path." NOT "there is no consent."**
**6. Twitch geo written as a DOCUMENTED ABSENCE only. The piece does not assert what EU/UK/AU users see in the product.**
**7. "May be used," never "is training on." Not "began by default" -- the change is the addition of a control.**

**WINDOW DISCIPLINE (Tue 1 - Sun 6 read in full):**
**- ZERO comma-and-clause section headers (the form hit 15 of 35 in the window and forced renames on Sun 6). All headers are bare noun phrases or imperatives, the least-worn shapes.**
**- "nobody" appears ZERO times in the title, headers and close, and twice in the body. It ran ~40 times in the window.**
**- ONE negate-then-correct in the whole piece, spent at the close where it is load-bearing. The device ran 22+ times in the window.**
**- ZERO "here is the" attention-frames (10 in the window, cut 3->2 by Sun 6's panel).**
**- The action is a LOOK-UP, not a write-down (Tue 18 and Tue 25 both wrote something down; Tue 1 refused a third) and not a sort (Tue 1 owns two columns). It is an inventory, and his own law licenses a list for exactly that.**
**- NO bold-imperative Find/Then/And block. That sequencing ran three times in five days.**
**- Gaming set piece deliberately omitted: Wed 2 and Fri 4 both ran one, and a third in a week is formula.**
**- Self-reference to this pipeline held to ONE clause, per the plan (it ran Mon 17; a third would be a tic).**
**- Close avoids every burned shape: "only person in [container]", "not on anybody's list but yours", "nobody is going to hand you", the bill, the rubric, the job description, the year-and-a-name.**
**- ICO and CNIL deliberately not used. Both spent Tue 1 / Wed 2.**

---

You have an opt-out. Somebody else decides whether it ever gets used.

I want to be clear at the top that this is not a piece about a company behaving badly. The two instruments I am going to walk you through are both documented, both working exactly the way their documentation says they work, and neither one is hiding. That is what makes them worth your time. The control is real. It is written down. It is simply held by somebody other than the person the data is about, and once you have seen that shape you will start finding it in places you had not thought to look.

The sort last Tuesday was into two columns: the things you would notice coming back wrong, and the handful where the only thing standing between wrong and shipped is you reading it and feeling like it is fine. That sort assumed something today's does not. Before you can ask whether you would catch it, you have to know who is permitted to switch the thing off, and for a good deal of what is running against your data this morning the honest answer is a party you have never spoken to.

Two of these shipped within days of each other in the middle of August. One is enterprise and squarely my own turf. The other is a video platform. They are the same shape, and the consumer one is easier to see, which is why it comes second.

## The record you cannot delete

Anthropic's Compliance API returns the transcripts of sessions your people run in Claude Cowork and Claude Code, on their own machines. Since August the coverage has widened. It now also reaches the Claude Science desktop app and the Claude add-ins for Excel, PowerPoint, Word and Outlook, which is to say it reaches the documents your finance team is drafting in the applications they have always drafted them in.

Start with what it is not, because the obvious reading is wrong and a technical reader will call you on it. Nothing is installed on the laptop. There is no agent, no endpoint tooling, no inspection of the device at all. The documentation is direct about this:

> "For local sessions, Anthropic records each conversation server-side as its requests reach the Claude API; nothing is installed on the device, and nothing is collected beyond the requests the client already sends to the Claude API."

The word local names where the session runs. The capture happens somewhere else, on traffic the client was already sending. That is a quieter mechanism than the one most people picture, and if you have been watching your endpoints for an agent you have been watching the wrong place.

What comes back is the conversation. Prompts, responses, tool calls, and the text of tool results, which means the contents of files the assistant read, in text, along with your project instruction files. Thinking blocks are never included and the system prompt is never returned. Images and PDFs come back as a placeholder. And there is one sentence in there that is more use to a security team than most vendor documentation manages in a page: "Nothing masks URLs, credentials, or personal data in that content, so treat transcripts as sensitive."

An honest limit is stated alongside it, and it should travel wherever the fact travels: "Local session transcripts show what Claude was asked to do and what it returned, not what happened on the device." Activity that never reaches the API is not captured. It is a record of a conversation.

Retention is six years from capture by default, or your organization's own conversation retention period where a finite one is set, and where more than one is configured the shortest applies. There is a wrinkle in that worth carrying: shortening the period takes effect immediately for what can be read back, while lengthening it later does not restore anything that has already expired. The setting ratchets one way.

Then the part that is the whole piece.

The endpoints are read-only, and sessions cannot be deleted through them. Sitting inside that is an asymmetry I read twice because I did not believe it the first time. A Cowork session that ran in the cloud is retained for six years *unless a user deletes the session sooner*, and once they do it is gone and it is not recoverable through the API. A session that ran on the person's own machine has no equivalent path. For the Office add-ins the documentation says it outright: deleting the conversation in the add-in happens only on the client, so the session stays listed until retention removes it.

You can delete the one that ran in a data center. You cannot delete the one that ran on your own laptop.

Last Tuesday's piece happened to carry the exact inverse of that, in OpenAI's Computer History feature, where the memory files sit on your own filesystem until you delete them. Same category of product, two weeks apart, opposite arrangement, and no way for a buyer to reason from one to the other. That is the part that should bother you more than either arrangement on its own.

## Where the consent question actually sits

Capture is tied to the Compliance API being enabled for the organization, and it applies while people are signed in with their enterprise account. Enablement happens once, by the primary owner, and it cascades from the parent organization down to every linked one.

I went looking for the user's side of that and want to report what I found precisely, because the loose version is a claim I cannot stand up. Across four of Anthropic's documentation pages -- the session endpoints, the FAQ, the API overview and the integration guidance -- there is nothing about notifying, informing or obtaining consent from the people whose sessions are captured. The same pages carry careful and quite specific guidance on SIEM correlation, on legal hold, and on chain of custody for exported records.

That absence is a real observation and it is a limited one. These are administrator-facing documents. Telling your staff sits with you, under whatever law applies where they work, and a vendor's API reference is not where you would look for it. So the sentence I will stand behind is the narrow one: the documentation describes no user notification, consent or opt-out path. Whether one exists in your building is a question about your building, and you already know whether anybody has asked it.

Worth naming the economics, because there are none. No new key, no new scope, no new setting and no client update -- the documentation says exactly that. The capability arrives inside a product the organization has already bought, and one person turns it on. Extending a six-year record across every Word document and Outlook draft your people touch with an assistant costs a toggle.

<!-- [YOUR TAKE]: this is the spot for the view from the other side of the switch. You have been the person holding the admin toggle over other people's work. What is that actually like to be handed, what did you do about telling anyone, and what did the conversation with HR or legal look like if there was one? -->

I will say plainly that this newsletter is assembled with one of the tools I am describing.

## Chatting on somebody else's stream

Now the consumer version, which is the same structure with the volume turned up.

In the middle of August, Twitch added a setting called Training for Generative AI. Note the verb, because the tense matters and most of the coverage got it wrong, including a summary that came across my own desk: the toggle is new, the permission in the privacy notice is not. What changed is that a control appeared, not that a practice started.

Twitch defines the scope in its own help article: "Your stream and the stream's chat, your VODs, your Clips, Highlights, and any text or images on your Channel may be used." May be used, throughout. Twitch nowhere says content has been used, and the difference is not pedantry, it is the difference between a permission and a report.

Then the sentence that made me want to write this:

> "If you chat on someone else's stream, their opt-out preferences govern if that chat can be used for training."

You typed it. It is your sentence, in your words, under your name. Whether it becomes training data is decided by the person whose channel you were standing in, who has never met you and whose incentives, as Twitch itself describes them in the same paragraph, run toward growth and monetization. Your consent is delegated upward, silently, to somebody with a business reason to leave the switch where it is.

Opting out is prospective only. Twitch is clear that content "will not be used in future training," which leaves any model already trained exactly where it is.

And a documentation detail that I keep turning over. The Privacy Choices page is the page Twitch's own privacy notice points you to when you want to know what choices you have. I read it on Friday. It says "Last modified on 05/17/2023," and it does not contain the word generative, or training, or AI. The most consequential new choice on the platform is absent from the canonical document about your choices, three weeks after the toggle shipped and considerably longer after the permission did.

I looked for a geographic carve-out, because the obvious question for anyone reading this outside the United States is whether the European or Australian default is different. Twitch documents none. The setting text is identical when the help article is served in British English, the privacy notice never names generative AI training at all, and the notice's own jurisdictions section carries only representative designations and a minimum-age provision. What I can tell you is that Twitch documents no geographic exception. What I cannot tell you is what the settings screen looks like on an account in Dublin, and I am not going to pretend those are the same statement.

## The improvement is real

I want to give the other side its full weight, because I think it is stronger than a piece like this usually admits.

On Wednesday the complaint was an absence. A vendor shipped a recording feature and documented nothing about retention, training use, or an administrator switch. Both of today's instruments are the opposite of that. Anthropic documents the retention period, the exclusions, the truncation limits, the error semantics and the boundary of what the record can and cannot show, and it tells you in writing to treat the transcripts as sensitive. Twitch tells you, in the help article, that a viewer's chat is governed by the channel owner, which is a fact it had every commercial reason to leave unstated.

The Compliance API in particular is the artifact the last three weeks of this newsletter kept arguing for. If your position is that agents need an audit trail before they should be allowed near anything that matters, this is what that looks like when somebody actually builds it: an endpoint, a scope name, a retention period, and a chain-of-custody procedure. You do not get to demand the governance layer and then be surprised when it is a governance layer.

Twitch is also honest in a place it did not have to be, in an FAQ answer about why you cannot opt out of every use of AI on the platform:

> "Some of it runs the service itself, the same way our servers and our code do. Some of it keeps the service secure. And some of it, like AutoMod, protects the whole community. Turning those off for one person would weaken safety and security for everyone else on the platform, so they are not individual settings."

That is a better argument than most companies bother to make, and it happens to be true. Amazon owns Twitch and Amazon is the beneficiary of the training, and I will name that rather than leave you to find it. It does not make the paragraph above less correct.

## Look up who holds yours

The skill today is a look-up, and it takes about twenty minutes.

Pick the systems that actually carry something of yours or your people's, and for each one answer a single question in writing: who is the party that can exercise the control, and have they ever been asked to. Not what the policy says. Who.

The answers tend to sort into a small number of shapes, and it is worth seeing them next to each other:

- **Your employer's tenant administrator.** The assistant settings, the compliance toggles, the retention period. One person, cascading down.
- **The platform, by default.** Anything where the control exists but its factory position was chosen by the vendor and nobody in your organization has revisited it.
- **A third party you have no relationship with.** The channel owner, the group admin, the meeting host who turned recording on, the customer whose tenant your contractor account lives in.
- **Nobody, currently.** The control is documented, it works, and the person it would protect has not been told it exists.
- **You.** Which does happen, and is the case worth confirming rather than assuming.

Then count how many landed in the middle three. In my experience it is more than people expect, and the interesting part is not the total. It is that almost every one of them is a control somebody could pull today, at no cost, and has not, because pulling it was never on their list and there is no mechanism by which your preference would reach them.

That is the operational version of all this. The gap is rarely a missing capability. The gap is that the capability sits with a party who has no channel to hear from you and no reason to act if they did.

## The point

The session that ran in the cloud, you can delete. The session that ran on your own laptop, you cannot. It is documented, it is not hidden, and it is the reverse of what almost everyone would guess.

That is the shape to go looking for. Not the control that is missing, which is easy to spot and satisfying to complain about, but the one that is right there in the documentation, working exactly as described, sitting in the hands of somebody who has never had a reason to touch it.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the controls over your data increasingly exist, are documented, and are held by somebody other than you -- that Anthropic's Compliance API lets you delete a session that ran in a data center but not one that ran on your own machine, that Twitch hands your chat consent to whoever's channel you typed in, and that the useful question is no longer whether a control exists but who is holding it and whether anyone has ever asked them to use it.*
