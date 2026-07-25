# Welcome to the Other Side of the Form

**Status: In editing — v2 (structural revision)**
**Target: Monday 6 July 2026** *(note: original header said Monday 7 July — July 7 is a Tuesday; Sunday's capstone promised "Monday")*
**Series: Part 3 — The Ad Hoc Regulatory Regime**
**Preceding pieces: "The Kill Switch You Didn't Know About" (2 July), "The Regulators Just Got Fired" (3 July), teased in "Nobody Gave You a Week" (5 July)**

---

You've been doing this for decades.

You know the form. You built the form. Source of funds. Politically exposed persons. Beneficial ownership. Enhanced due diligence for high-risk customers. You've sat on the operator's side of KYC since before most of your staff were old enough to walk into one of your venues.

Now someone wants you to fill one out.

---

When Anthropic's Fable 5 came back online last week -- after 19 days dark, courtesy of a US Commerce Department letter -- the company signalled it was considering requiring KYC verification as a condition of access. Not for individuals. For businesses. For organisations like ours.

The details are still forming. But the direction is clear: the world's most capable AI vendor is exploring what it would mean to know its customer.

Here is what actually happened in those 19 days, because the mechanics matter for the argument that follows -- and because every step of the sequence will be familiar to anyone who has ever run a compliance function.

On June 12, the US Commerce Department's Bureau of Industry and Security ordered Anthropic to suspend access to both Fable 5 and its underlying model, Mythos 5, for all foreign nationals -- including Anthropic's own non-citizen staff. The trigger was an Amazon research report describing a technique that could prompt Fable 5 into revealing the cybersecurity capabilities of the Mythos model underneath it: getting the model to flag software vulnerabilities and, in one case, write code demonstrating how a flaw could be exploited. The government's position: a guardrail bypass with national security implications, enforceable under export controls written for semiconductors and satellite hardware.

More than 100 cybersecurity professionals, organised by Katie Moussouris of Luta Security -- one of the few outside experts who actually reviewed the underlying research -- signed an open letter with an unambiguous assessment: "That is not a guardrail bypass."

It didn't matter. The ban lifted on June 30 because Anthropic trained a new classifier, demonstrated it suppressed the technique in more than 99% of attempts, and satisfied the Secretary of Commerce. Fable 5 returned globally on July 1.

Now read that sequence back through the lens of what you know about compliance frameworks.

The rules that triggered the shutdown were not published. The criteria for what constitutes a prohibited "guardrail bypass" were not defined in any statute. More than 100 domain experts publicly disputed whether the trigger met any reasonable definition of the thing it was supposed to be. The appeals mechanism available to Anthropic was, in its entirety: negotiate with the Secretary of Commerce until he is satisfied. Which Anthropic did. And it worked.

If you run a compliance function, you can feel what's wrong with this in your bones. No published criteria. No independent assessment. No appeals body. No legal definition of what passes. The "standard" is whatever satisfies the regulator in that moment.

If you operate in clubs or gaming, you've had a front-row seat to the evolution of "know your customer" for two decades. The AML/CTF Act has been shaping our compliance obligations since 2006. AUSTRAC is the most active financial intelligence regulator in the country. We've invested in identity verification infrastructure, transaction monitoring, and responsible gambling controls that most banks would be embarrassed to compare themselves against.

You are not naive about KYC. You are, in many respects, its most experienced practitioner.

Which is exactly what makes this next part interesting.

---

## When You're On the Other Side of the Form

When you do KYC, you collect data. You run checks. You make decisions. And those decisions determine whether someone can access your services.

When Anthropic does KYC on you, they collect data about your business -- its scale, its use cases, the nature of the AI workflows you intend to run. They run checks. And they make a decision about whether you can access theirs.

The asymmetry is striking, but it's the second-order implications that should concern you.

When you decline a customer under AML/CTF obligations, there are rules. Published ones. The criteria for enhanced due diligence are legislated. Your decisions are subject to AUSTRAC oversight. You can be audited. Your customer has rights. The whole system operates within a published framework, administered by an accountable regulator.

When an AI vendor decides whether your business passes their process, the criteria are not published. There is no independent oversight body. There is no appeals mechanism. There is no legal definition of what counts as "high risk" to an AI vendor. And as the 19-day saga just established, the export control regime the vendor itself operates under has no published rules either. The standard is what the regulator decides it is, in the moment, in private -- all the way up the chain.

You are very familiar with the power of a gatekeeper decision. You've made thousands of them. The question you need to sit with is what it means to be subject to one when the gatekeeper is accountable to nobody you can name.

---

## The Form Already Exists. You Just Can't See It.

Here's the part that should reframe how you read the KYC announcement -- and it's not the part the commentary has focused on.

The approval regime is already running. It just doesn't have a form.

When Commerce Secretary Lutnick reinstated Mythos 5 on June 26, he reinstated it for roughly 100 approved companies and federal agencies. When OpenAI released GPT-5.6 -- Sol, its most capable coding and cybersecurity model -- access went to approximately 20 companies, approved by the US government, during a "preview period" that Sam Altman conceded was "not our preferred long term model."

Think about what being on one of those lists means. Somebody assessed those organisations. Somebody weighed their risk profile, their use cases, their relationship with government, their nationality. A due diligence process ran, criteria were applied, and a decision was made about each of them.

That's KYC. It's just KYC with no form, no published criteria, no way to apply, and no way to know why you're not on the list.

And this is where two decades on the operator's side of the form gives you an insight the commentators don't have. Everyone else reads "AI vendor KYC" as an imposition. You know better. A form you can see -- with fields you can read, criteria you can prepare for, a submission you can complete -- is a gift compared to a list you can't get on. The worst gatekeeper isn't the one with a demanding form. It's the one with no form at all, making decisions in a room you're not in, on criteria that don't exist on paper.

The problem with Anthropic's KYC proposal isn't that it formalises gatekeeping. Formalising it would be the first improvement in this entire saga. The problem is everything around the form that still wouldn't exist: the oversight, the appeals, the published risk criteria, the accountable regulator. The form without the framework.

We know exactly what that's worth, because we've spent twenty years operating the full version.

---

## What the Form Will Ask

You can already sketch the fields, because vendor KYC will converge on the same architecture as financial KYC. It always does. Map them across:

**Beneficial ownership** becomes: who ultimately controls your organisation, and in which jurisdictions? A club with straightforward Australian ownership will find this easy. Organisations with layered structures, foreign investors, or state-linked shareholders will find it decisive.

**Source of funds** becomes source of data: what flows into the model, and where does the output go? Whose personal information is in your prompts? Which jurisdictions does your data touch? You've asked the money version of this question at every enhanced due diligence trigger for years.

**Customer risk rating** becomes industry risk rating -- and here's the uncomfortable one. Gambling has sat on every bank's heightened-risk matrix since the de-risking era. It would be naive to assume the same matrix won't be copied, more or less wholesale, into AI vendor risk frameworks. We start this game already flagged.

**Enhanced due diligence** becomes use-case scrutiny: anything touching cybersecurity tooling, biometric processing, surveillance, or -- yes -- gambling-related decision systems will draw the long-form questions.

**Ongoing monitoring** becomes usage telemetry and periodic attestations: not just "who are you" at onboarding, but "what are you doing with it" continuously, forever.

And the last field is the one to sit with. In the AML world, reporting entities file suspicious matter reports with AUSTRAC. In the AI world, your vendor -- watching your usage telemetry under its government framework agreement -- is the reporting entity. Commerce is its AUSTRAC. You are the transaction.

You've been the reporting entity for twenty years. Monday morning's realisation is that in the AI access regime, you're the customer being reported on.

---

## The De-Risking Analogy

Here's a comparison that will land differently depending on which side of it you've been on.

In the years following the global financial crisis, major banks in Australia, the United States, and the United Kingdom went through a period called "de-risking." Faced with enormous AML penalties and reputational pressure, they quietly began exiting customer relationships in industries they considered high-risk. Gambling was on the list. Cash-heavy businesses were on the list. Certain remittance providers. Certain charities with international operations.

De-risking wasn't announced as a policy. There were no published criteria. Businesses simply received letters -- sometimes quite terse -- informing them their banking facilities would be discontinued. In Australia, the impact fell hardest on small gaming operators, foreign exchange businesses, and charities operating in conflict zones. The clubs sector, depending on its banking relationships, had a front-row seat.

The parallel to AI is not exact. But it's close enough to be instructive.

AI vendors facing regulatory and geopolitical pressure -- from export controls, congressional scrutiny, and an increasingly politicised national security conversation -- now have structural incentives to de-risk their own customer bases. That may mean declining to serve certain industries. It may mean adding friction -- KYC requirements, usage attestations, ongoing reporting obligations -- that make some business relationships more trouble than they're worth.

The gambling and gaming sector is already on the sensitive list for most financial institutions. It would be naive to assume it won't appear on AI vendor risk matrices too.

---

## What Happened to the People Who Were Supposed to Prevent This

Part 2 of this series covered *Trump v. Slaughter* -- the Supreme Court ruling that stripped independent agencies of the job security protection that made them independent. The FTC, the FCC, the NLRB: their commissioners can now be fired for disagreeing with the executive branch.

The reason that matters here is simple: if an AI vendor decides to de-risk your industry, the regulatory body that might have protected you -- the FTC, in the US context -- is no longer structurally independent of the political winds that also blew Fable 5 offline in June.

In yesterday's capstone I called this the fourth clock: the institution that was supposed to impose stable, published time on everyone else's decisions has been captured by the same volatility it was built to dampen. For the KYC question specifically, that means there is no referee. At the precise moment AI vendors are acquiring the power to grant or deny access to frontier capability -- capability that is rapidly becoming a competitive necessity -- the regulatory architecture that might constrain that power has been substantially weakened.

In Australia, AUSTRAC and APRA operate under a different constitutional structure. But the Australian regulators that could, in theory, have something to say about AI vendor access decisions -- ACCC, OAIC, ASIC -- have not yet developed that mandate. The National AI Plan explicitly chose not to create it.

So there is a gap. And it is not a theoretical one.

---

## What This Actually Means for Your Business

Sunday's argument applies here with full force: pre-decide. Vendor KYC is coming on somebody else's schedule, with criteria you won't get to review in advance. The organisations that navigate it well will be the ones holding a completed file before the form arrives. Four things belong in that file.

**Understand your dependency.** If frontier AI is embedded in your operations -- customer service, compliance assistance, marketing, fraud detection -- map which functions depend on which vendors. The Fable 5 outage showed that 19 days without access is survivable for most organisations. What is your 19-day continuity plan? Do you have one?

**Document your use cases.** When AI vendors come to know their customers, they will want to understand what those customers are doing with their models. Your ability to articulate your AI use cases -- clearly, accurately, and in compliance terms -- will determine how that conversation goes. "We use it for customer service and internal search" is a very different risk profile than "we're still figuring it out." Know what you're doing before someone asks.

**Assemble the dossier now.** You already know how to build a compliance file, because you've required thousands of them from others: ownership structure, data flows, use-case register, risk assessment, controls. Build your own AI version this quarter, before any vendor asks. When the form arrives -- from Anthropic, from OpenAI, or from a vendor that hasn't announced it yet -- you return it in days, not months. In a de-risking environment, the customer who responds cleanly and quickly is the customer who keeps their facility. You've watched that exact dynamic from the other side of the desk.

**Track the open-weight alternatives.** The Fable 5 episode demonstrated something the open-source community has been saying for years: a model you can run yourself cannot be de-listed by a government letter. GLM-5.2 -- a 744-billion-parameter open-weight model released under MIT licence last month -- beats GPT-5.5 on coding benchmarks at a fraction of the cost and runs on hardware you control. OpenAI has released open-weight models under Apache 2.0. Mistral is building sovereign European AI infrastructure. The "we have no alternative to cloud AI" assumption is eroding fast.

---

You've been in the identity verification business for decades. You understand that access to services can be conditional, that conditions change, and that the rules of the game are written by whoever has the power to write them.

You also understand something subtler, because you've held the pen: the form was never really about the fields. It was about who decides what a passing answer looks like.

The AI access regime is still being written. The question is whether your business will be in the room when it is, or whether you'll receive a letter on a Friday afternoon informing you of the outcome.

You know which side of the form you'd rather be on. Start filling it out now.

---

*Part 1: "The Kill Switch You Didn't Know About" -- the June 12 export control order and what it means for any business running frontier AI.*
*Part 2: "The Regulators Just Got Fired" -- Trump v. Slaughter, independent agencies, and the regulatory vacuum inside which AI vendors now operate.*
*Sunday capstone: "Nobody Gave You a Week" -- the four clocks, and why pre-deciding is now a governance requirement.*

*Additional sources added July 2: [Anthropic Restores Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls](https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html) (The Hacker News); [Washington Called Anthropic's Fable 5 a Security Threat. The Only Expert Who Read the Research Disagrees.](https://easternherald.com/2026/07/02/anthropic-fable-5-restored-us-export-controls-fix-code-jailbreak/) (Eastern Herald); [Anthropic Redeploys Claude Fable 5, Adds New Cybersecurity Classifier](https://www.marktechpost.com/2026/07/01/anthropic-redeploys-claude-fable-5-on-july-1-after-us-export-controls-lift-adds-new-cybersecurity-classifier/) (MarkTechPost); [Cybersecurity experts don't think Fable 5 presents a unique threat](https://cyberscoop.com/cybersecurity-experts-anthropic-fable-5-not-unique-ai-threat/) (CyberScoop).*
