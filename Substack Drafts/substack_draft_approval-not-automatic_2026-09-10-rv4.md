# Approval Is Not Automatic

**Status: DRAFT rv4 -- Thursday, 10 September 2026. Drafted 8 Sep from the Thu 10 block of `References\week-plan_2026-09-07.md` (v1.1), the 5 Sep story-candidate addendum, and `References\research_trusted-access_2026-09-08.md` (all primaries fetched live 8 Sep), against the landed seven-day window rather than the plan's summary of it. ~2,985 body words (OVER the ~2,300 house norm -- flagged for his call, not trimmed; no length-aside deployed because Mon 7 used two beats of that device three days back). Em-dash-free; zero contractions in expository prose, direct address exempt; US spelling. NOT PANELLED. ONE [YOUR TAKE] OPEN. No open [VERIFY]. He pushes to Substack himself.**

**Series: Weekday feed (Thursday) · Thread: AI Attack Surface × Trust Boundaries · Register: the gate**

**HIS CALLS AT DISPATCH (8 Sep): open on the corrected asymmetry; print Google's 650+ partner figure annotated as self-reported.**

**Source: `research_trusted-access_2026-09-08.md` -- OpenAI Trusted Access for Cyber help centre; OpenAI "Path to Astra" (1 Sep); OpenAI "Expanding Daybreak as the Cyber Defense Window Narrows" (10 Aug); OpenAI "Daybreak for Frontline Defenders" (3 Sep); OpenAI Global Affairs (4 Sep); Anthropic "Introducing Claude Fable 5.1 and Claude Mythos 5.1"; Anthropic defenders blog; Google DeepMind Fairwind Program; Google "Introducing Gemini 3.8 Flash and 3.8 Flash Cyber" (2 Sep). All fetched 8 September 2026.**

**FIREWALL: this piece does not touch chain-of-thought monitorability, the system card's monitorability section, or Pachocki. That is Friday's, and Monday's scheduled piece is already in print promising it.**

---

Three frontier labs published new rules about who may use their cyber capability inside four days. My own morning brief called it a pattern.

It is not a pattern. I went and read what the three companies actually wrote, on their own pages, and they are doing three different things under one borrowed word. That matters more than it sounds like it should, because "trusted access" is about to start appearing in procurement documents, board packs and vendor questionnaires as though it described a single arrangement that a buyer could evaluate. It does not. And the differences are exactly the ones that decide whether your organization can get the capability at all.

A pharmacy runs three regimes at once. Most of what it sells is on the shelf: you pick it up, you look at the price on the box, you pay. Some of it sits behind the counter, where you have to ask, and the person serving you decides whether to hand it over and writes down that they did. And some of it you cannot have at all unless a third party who does not work for the pharmacy signs a piece of paper first. Three different regimes, in one shop, and the label on the box tells you almost nothing about which one you are in. Now imagine three pharmacies, in three countries, each with its own scheduling rules, each calling all of this "restricted," and a buyer trying to work out from the outside which medicine they can actually obtain.

That is the frontier cyber model market as of this week. And the reason to care on a Thursday is that the shelf price is the only one published anywhere.

## The pattern that is not there

Here is what my brief said on 5 September: *"All three major labs now ship in two speeds -- public capability and access-controlled capability."* It is a tidy sentence. It is the sentence most of the coverage landed on. It is wrong on tense for one lab and wrong on mechanism for another, and I would rather correct my own house than let that travel.

**Google is the only one of the three running a live, conditional, contractual program right now.** The Fairwind Program gates Gemini 3.8 Flash Cyber, and Google publishes what a participant signs up to. Applicants are vetted -- *"We vet all applicants to make sure they have a proven track record of ethical operations and research"* -- and accepted organizations take on written operational obligations: *"user-level authentication, phishing-resistant MFA, and applicable access controls,"* a restriction that *"Organizations may only grant Gemini 3.8 Flash Cyber access to internal cybersecurity, incident response, or penetration testing teams,"* a requirement that they *"must track employee access and use,"* and a flat prohibition on passing it on: *"we do not allow partner organizations to share, redistribute, or sell access."* Google says it currently works with *"over 650 partners globally."* That figure is Google's own, published on Google's page, and I could not find an independent count of it anywhere, so treat it as a company statement rather than a market measurement.

**Anthropic is not shipping a second speed yet, and the mechanism is not a tier.** Its Cyber Verification Program *"currently provides access to certain Opus- and Sonnet-class models with reduced cyber safeguards for defensive security work. In the near future, this program will also include access to Claude Mythos-class models."* Read that as written. The thing being adjusted is the safeguard, not the model: Anthropic says Mythos 5.1 *"is identical to Fable 5.1, but it offers more permissive safeguards for vetted individuals and organizations."* Same model, different refusal behavior, and the top tier of the program is future tense.

**OpenAI is running a staged rollout, which is a third thing again.** Its own words: *"We plan to make Astra available soon, but access to its most advanced cybersecurity capabilities will be more limited,"* and *"Access to Astra for advanced cybersecurity workflows will initially be available to a small group of alpha testers, with access through Daybreak Blue expanding afterward to support defensive use."*

So: a contractual program with published conditions, a safeguard-reduction program with a future-tense top tier, and a staged release to alpha testers. Those are not three implementations of one idea. They are three instruments, and a buyer cannot line them up next to each other and compare them, because there is no column they share.

One thing that must not be done with any of this, and I want to be explicit because I have already seen it done: OpenAI's Critical designation is OpenAI's, made under OpenAI's own Preparedness Framework. *"It is the first model we are designating at this level."* Google's own model card for Gemini 3.8 Flash speaks an entirely different vocabulary, and says *"we are confident that Gemini 3.8 Flash is also unlikely to reach any T/CCLs."* Welding those two frameworks together to rank the labs produces a league table that does not exist. Every one of these companies sells access to these models, and every one of them wrote its own ruler.

## Approval is not automatic

The title of this piece is not mine. It is a sentence in OpenAI's help centre, and it is worth reading in full because it describes a governance relationship that most organizations have not noticed they entered.

*"Trusted Access for Cyber is the governance model for OpenAI Daybreak. It helps qualified enterprise customers and cybersecurity practitioners use OpenAI models more effectively for authorized cybersecurity work."* And then: *"OpenAI reviews requests before enabling access. Approval is not automatic."*

What gets reviewed is instructive. Applicants may be asked for information about *"Your organization and cybersecurity capabilities. The defensive cybersecurity workflows you want to support. The OpenAI organization or workspace you expect to use. Verification or trust information needed to assess eligibility."*

Sit with the first item for a second. A model vendor is assessing your organization's cybersecurity capabilities and deciding, on the strength of that assessment, what class of tool your security team is allowed to use. That is a supplier adjudicating the competence of its customer. There may be no better available answer -- I am not sure there is -- but it is a genuinely new shape of relationship and it is not one that appears on any risk register I have seen.

And there is a clause in there that almost nobody writing about this has picked up, because it only bites if you sell services rather than buy them. Access *"cannot extend to third-party customers, external users, customer-facing workflows, or downstream product traffic."*

That sentence removes the entire managed-services channel from the capability tier. A managed security provider cannot obtain this and run it on behalf of its clients. Every organization that reached the sensible conclusion that frontier cyber capability was something they would consume through a partner rather than build a team for is, on the current terms, on the wrong side of that line. The capability is available to organizations that already have a security function good enough to be assessed, and not available through the channel that exists precisely because most organizations do not have one.

Think about this for a minute: aside from the nanny-state implications of a vendor determining *your operational competence to run its product*, which is pretty staggering in and of itself (no, it's just too powerful, we can't trust you with it, unless you prove to us you are good enough), if you are a company like many that has said "our security estate is too mission critical to our operations and too specialized of a skill set to justify paying a staff member or members to do it, so we are having a trusted advisor do that work and have had for years", not only are you in a place where now YOU can't get the model, you're also in a place where your VENDOR can't get the model. Which, candidly, gives a whole new meaning to the phrase "market control."

## Daybreak Blue runs last quarter's model

This is the part that changed the piece while I was writing it, and it is the single most useful fact in here. It's the part that caught me so by surprise that I had actually written a completely different description of the problem.

Nearly all of the coverage of Astra's launch said some version of "the defenders got it first." OpenAI's own documentation does not say that. Its help centre says: *"Daybreak Blue is the recommended starting point for most security teams. Built on GPT-5.6 Sol with Trusted Access for Cyber, it supports approved defensive workflows including secure code review, vulnerability triage, detection engineering, incident response, malware analysis, and patch validation."*

**Built on GPT-5.6 Sol.** Not Astra. There is a second tier, Daybreak Red, which *"provides access to our purpose-trained cybersecurity models for authorized vulnerability research, exploit validation, and security testing,"* including a variant OpenAI describes as being there *"to further reduce refusals"* -- and that one is built on Sol as well. NEITHER is built on Astra. Arguably the most capable model ever released, and the defensive program is not running it.

So line up the actual state of play on the day I am writing this. The model OpenAI describes as being able to *"find previously unknown security flaws and develop ways to exploit them across many well-protected systems without a person guiding each step"* is with a small group of alpha testers. The defensive program that every security team is being pointed at is running the previous generation. And expansion of Astra into that defensive program is described in the future tense.

I want to be careful about what I am accusing anyone of here, which is nothing. Staging a Critical-rated capability slowly is a defensible thing to do, and I would probably do the same. The point is narrower and it is about what you were told. If your read of last week was "the good model went to the defenders," the vendor's own documentation says otherwise, and the gap between those two readings is exactly the size of the gap between a press cycle and a help centre article.

## All three start in America

If you are reading this from Sydney or Brisbane, this is the section that costs you something.

Anthropic, verbatim: *"Currently, it is only available to a set of US organizations, though we're coordinating with the US government to expand access to a broader set of domestic and international partners as quickly as possible."* Give them the credit for writing that down plainly, and for saying what the path forward is. But read the path: expansion of a commercial program's geography runs through coordination with a national government. That is not a sales pipeline. That is an export posture.

OpenAI's billion-dollar subsidy has the same shape. The company committed *"$1 billion in subsidized Daybreak access to help resource-constrained cyber defenders"* -- state and local government, critical infrastructure operators, nonprofits, open-source maintainers -- *"starting with the United States,"* with expansion to partner countries described as coming, and the whole thing *"targeting it to be consumed over the next six months."* Water utilities and regional banks are named. Australian water utilities and regional banks are not, yet.

There is a wrinkle worth flagging so you do not repeat the version I first wrote down. OpenAI's policy blog says *"Daybreak is already active in more than 20 countries and multilateral institutions."* Both statements are OpenAI's, four days apart, and they are about different things: the program has a footprint, and the subsidy has a starting line. My own brief blended them into "a $1B commitment active in 20+ countries," which is not what either page says. If you see that formulation somewhere else this week, it came from the same blend. It's good for the public relations message, but as far as I can tell, it is absolutely not an accurate rendering.

Google is the exception. The Fairwind page names its priority sectors -- governments and national cyber authorities, critical infrastructure operators in healthcare, telecommunications, energy and financial networks, and core technology platforms -- and states no geographic restriction at all. Which means that for an Australian critical infrastructure operator, the one program of the three that is live, conditional and open to apply to today is the one attached to the model that its own vendor describes in the most modest terms. It's a good model, and it's strong, but it's still second tier compared to Mythos 5.1 or Astra. So your best option is still not the front-runner.

## What none of the three will quote you

Now the part that should have been the easiest to research and turned out to be the hardest.

The general models have published prices, and they move. Astra is on the API at ten dollars per million input tokens and fifty per million output. Gemini 3.8 Flash is seventy-five cents in and three dollars seventy-five out, and Google has already published the date that doubles: an introductory rate through 31 December 2026, then a dollar fifty and seven fifty. You can put that in a budget. You can model a year of it.

I checked five pages for the price of the gated tier -- OpenAI's Trusted Access overview, its Daybreak expansion announcement, its frontline defenders announcement, Google's Fairwind program page, and Google's Gemini 3.8 launch post. None of the five carries a price for the gated capability. I am not going to tell you no price exists anywhere, because that is a claim about the whole internet and I checked five pages. I will tell you that a buyer following the obvious path from the announcement to the program page does not arrive at a number.

And the subsidy is not a fund, it is a rate. A billion dollars of access targeted for consumption over six months is roughly a hundred and sixty-seven million a month of somebody else's inference, allocated by a private company against its own eligibility criteria, starting in one country. Whatever else that is, it is not something you can apply for in a budget cycle. And it's certainly not something you can build a forward-looking defense budget around.

So the honest summary of the commercial position is this: the capability's eligibility is a vendor's review, its price is unpublished, its availability date is a vendor's future tense, and its geography is set by an export posture. Four of the terms that matter most to a buyer are outside the contract, and the party setting them is not at the table.

## Where this leaves you on Monday morning

**Find out which of the three you can actually apply to, and do it before you need it.** Fairwind is live and takes applications now, and the conditions are published, which means you can read them before you commit rather than after. The others are worth registering interest in on the same principle. An access review that takes weeks is a problem you want to have already had.

**Read the operational conditions as contract terms, because that is what they are.** Google's requirements -- phishing-resistant MFA, access confined to named internal teams, tracked employee usage, no redistribution -- are obligations your organization takes on, and at least two of them are things a mid-sized security team may not currently be able to evidence. Work out whether you could pass before you find out that you cannot.

**Check whether your capability strategy runs through a partner, and whether that still works.** If the plan was to consume frontier cyber capability through a managed provider, OpenAI's downstream-traffic clause says that path is closed for now on their side. That is a strategy question, not a procurement one, and it belongs in front of whoever owns the security roadmap this quarter.

**Write down which vendor's framework you are relying on, by name.** Not "we use a Critical-rated model." The designation, the framework, the version and the company. When somebody asks you in eighteen months what assurance you were leaning on, "the vendor said it was fine" is not an answer and neither is a rating you cannot attribute.

## "This is just a sensible safety rollout"

That is a fair enough objection, though I think the real point here is a bit more subtle than that. Every one of these companies is gating a capability that can, on its own vendor's assessment, find unknown flaws in defended systems without a human directing each step. Gating that is the responsible move, without question. Publishing the conditions, as Google has, is better than not publishing them. Saying plainly that you are US-only for now, as Anthropic has, is more honest than a vague "limited availability." Committing a billion dollars of subsidized access to under-resourced defenders is a real thing to do and I have no interest in being cynical about it.

My argument is not that the gates are wrong. It is that four material terms of a control that regulated organizations are increasingly relying on -- who qualifies, what it costs, when it arrives, and which countries it reaches -- are set entirely outside the buyer's contract, by three companies using three incompatible instruments, and that this is now a supply position rather than a product decision. You can think the gates are correct and still notice that you cannot plan against them. Those are not the same finding, and only one of them shows up in a risk register. Unfortunately, it is the one that is far worse for you as the operator.

## The gate is the product

Tomorrow I am taking the other half of this, which is what you can still see once you have been let in. Today is the front door and who holds it. Friday is the window, and what the vendor has said in writing about how clear the glass is.

The thing to carry out of today is smaller and more awkward than a policy argument. For most of the last half-decade, the frontier capability arrived and the only question was what it cost. Now the capability arrives and the first question is whether you are eligible, the second is what you would have to sign, the third is whether your country is on the list, and the price is not published at all. The shelf is the only part of the shop with a price on the box, and the shelf is not where the capability is. Nobody voted for that arrangement and nobody is hiding it either. It is written down, on three help pages, in three different vocabularies. It does not read like a supply decision, because it reads like an eligibility form. Somebody at the other end reviews it. Approval is not automatic.

---

*Thanks for reading. I know these run long and land dense, and I would rather give you the document than the summary of it.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that three frontier labs have built three incomparable instruments for deciding who may use their cyber capability, that the terms buyers care most about sit outside the contract entirely, and that a control you cannot price, schedule or apply for is a supply position rather than a safeguard.*
