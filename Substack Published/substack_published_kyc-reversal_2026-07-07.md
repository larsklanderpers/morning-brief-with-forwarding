# Welcome to the Other Side of the Form

**Status: Draft**
**Target: Monday 7 July 2026**
**Series: Part 3 — The Ad Hoc Regulatory Regime**
**Preceding pieces: "The Kill Switch You Didn't Know About" (2 July), "The Regulators Just Got Fired" (3 July)**

---

You've been doing this for decades.

You know the form. You built the form. Source of funds. Politically exposed persons. Beneficial ownership. Enhanced due diligence for high-risk customers. You've sat on the operator's side of KYC since before most of your staff were old enough to walk into one of your venues.

Now someone wants you to fill one out.

---

When Anthropic's Fable 5 came back online this week — after 19 days dark, courtesy of a US Commerce Department letter — the company signalled it was considering requiring KYC verification as a condition of access. Not for individuals. For businesses. For organisations like yours.

The details are still forming. But the direction is clear: the world's most capable AI vendor is exploring what it would mean to know its customer.

Here is what actually happened in those 19 days, because the mechanics matter for the argument that follows.

On June 12, the US Commerce Department's Bureau of Industry and Security ordered Anthropic to suspend access to both Fable 5 and its underlying model, Mythos 5, for all foreign nationals — including Anthropic's own non-citizen staff. The trigger was an Amazon research report describing a technique that could prompt Fable 5 into revealing the cybersecurity capabilities of the Mythos model underneath it: specifically, getting the model to flag software vulnerabilities and, in one case, write code demonstrating how a flaw could be exploited.

The government's position: this constituted a guardrail bypass with national security implications. A technology export control, written for semiconductors and satellite hardware, applied to a text-based interface.

Anthropic's position was that the technique was narrow and that comparable jailbreaks existed for other publicly available models — models not subject to any equivalent restriction. They were not alone in this view. Katie Moussouris, founder and CEO of Luta Security and one of the few outside experts who actually reviewed the underlying research, wrote an open letter signed by more than 100 cybersecurity professionals. Her assessment was unambiguous: "That is not a guardrail bypass."

The ban was lifted on June 30. Commerce Secretary Howard Lutnick cited Anthropic's close cooperation with government as the trigger. What cooperation looked like, concretely, was this: Anthropic trained a new classifier — a filter designed specifically to block the technique described in the Amazon report — and demonstrated it suppressed that technique in more than 99% of attempts. Fable 5 returned globally on July 1.

Now read that sequence back through the lens of what you know about compliance frameworks.

The rules that triggered the shutdown were not published. The criteria for what constitutes a prohibited "guardrail bypass" were not defined in any statute. More than 100 domain experts publicly disputed whether the trigger met any reasonable definition of the thing it was supposed to be. The appeals mechanism available to Anthropic — a private company whose employees and customers were cut off without notice — was essentially: negotiate with the Secretary of Commerce until he is satisfied. Which Anthropic did. And it worked.

To restate what that means: a Fortune 500 technology company had its global product pulled for 19 days because an unpublished rule, interpreted by a non-expert, applied a regulation designed for physical goods to a text interface — and the resolution mechanism was a private negotiation that produced a 99% classifier, the adequacy of which was assessed by the same department that imposed the ban.

If you run a compliance function, you can feel what's wrong with this. There are no published criteria. No independent assessment. No appeals body. No legal definition of what passes. The "standard" is whatever satisfies the regulator in that moment.

If you operate in clubs or gaming in Australia or the United States, you've had a front-row seat to the evolution of "know your customer" for years. The Anti-Money Laundering and Counter-Terrorism Financing Act has been shaping your compliance obligations since 2006. AUSTRAC has been the most active financial intelligence regulator in the country. You've invested in identity verification infrastructure, transaction monitoring systems, and responsible gambling controls that most banks would be embarrassed to compare themselves against.

You are not naive about KYC. You are, in many respects, its most experienced practitioner.

Which is exactly what makes this interesting.

---

## When You're On the Other Side of the Form

When you do KYC, you collect data. You run checks. You make decisions. And those decisions determine whether someone can access your services.

When Anthropic does KYC on you, they collect data about your business — its scale, its use cases, the nature of the AI workflows you intend to run. They run checks. And they make a decision about whether you can access theirs.

The asymmetry is striking, but it's the second-order implications that should concern you.

When you decline a customer under AML/CTF obligations, there are rules. Published ones. The criteria for enhanced due diligence are legislated. Your decisions are subject to AUSTRAC oversight. You can be audited. Your customer has rights. The whole system operates within a published framework, administered by an accountable regulator.

When Anthropic decides whether your business passes their KYC process, the criteria are not published. There is no independent oversight body. There is no appeals mechanism. There is no legal definition of what counts as "high risk" to an AI vendor. And as we just established — the export control regime they're now operating under has no published rules either. A hundred cybersecurity experts can sign an open letter saying the trigger wasn't real, and it doesn't matter. The standard is what the regulator decides it is, in the moment, in private.

You are very familiar with the power of a gatekeeper decision. You've made them. The question you need to sit with is what it means to be subject to one when the gatekeeper is accountable to nobody you can name.

---

## The De-Risking Analogy

Here's a comparison that will land differently depending on which side of it you've been on.

In the years following the global financial crisis, major banks in Australia, the United States, and the United Kingdom went through a period called "de-risking." Faced with enormous AML penalties and reputational pressure, they quietly began exiting customer relationships in industries they considered high-risk. Gambling was on the list. Cash-heavy businesses were on the list. Certain remittance providers. Certain charities with international operations.

De-risking wasn't announced as a policy. There were no published criteria. Businesses simply received letters — sometimes quite terse — informing them their banking facilities would be discontinued. In Australia, the impact fell hardest on small gaming operators, foreign exchange businesses, and charities operating in conflict zones. The clubs sector, depending on its banking relationships, had a front-row seat.

The parallel to AI is not exact. But it's close enough to be instructive.

AI vendors facing regulatory and geopolitical pressure — from export controls, congressional scrutiny, and an increasingly politicised national security conversation — now have structural incentives to de-risk their own customer bases. That may mean declining to serve certain industries. It may mean adding friction — KYC requirements, usage attestations, ongoing reporting obligations — that make some business relationships more trouble than they're worth.

The gambling and gaming sector is already on the sensitive list for most financial institutions. It would be naive to assume it won't appear on AI vendor risk matrices too.

---

## What Happened to the People Who Were Supposed to Prevent This

Part 2 of this series covered *Trump v. Slaughter* — the Supreme Court ruling that stripped independent agencies of the job security protection that made them independent. The FTC, the FCC, the NLRB: their commissioners can now be fired for disagreeing with the executive branch.

The reason that matters here is simple: if an AI vendor decides to de-risk your industry, the regulatory body that might have protected you — the FTC, in the US context — is no longer structurally independent of the political winds that also blew Fable 5 offline in June.

There is no appeals mechanism. There is no independent regulator with the mandate, the technical expertise, and the political protection to hold an AI vendor's gatekeeper decisions to account. At the precise moment when AI vendors are acquiring the power to grant or deny access to frontier capability — capability that is rapidly becoming a competitive necessity — the regulatory architecture that might constrain that power has been substantially weakened.

In Australia, AUSTRAC and APRA operate under a different constitutional structure. The Australian regulatory bodies that could, in theory, have something to say about AI vendor access decisions — ACCC, OAIC, ASIC — have not yet developed that mandate. The National AI Plan explicitly chose not to create it.

So there is a gap. And it is not a theoretical one.

---

## What This Actually Means for Your Business

Three things are worth thinking through now, before AI vendor KYC becomes standard practice.

**First: understand your dependency.** If frontier AI is embedded in your operations — customer service, compliance assistance, marketing, fraud detection — map which functions depend on which vendors. The Fable 5 outage showed that 18 days without access is survivable for most organisations. What is your 18-day continuity plan? Do you have one?

**Second: document your use cases.** When AI vendors come to know their customers, they will want to understand what those customers are doing with their models. Your ability to articulate your AI use cases — clearly, accurately, and in compliance terms — will determine how that conversation goes. "We use it for customer service and internal search" is a very different risk profile than "we're still figuring it out." Know what you're doing before someone asks.

**Third: track the open-weight alternatives.** The Fable 5 episode demonstrated something the open-source community has been saying for years: a model you can run yourself cannot be de-listed by a government letter. GLM-5.2 — a 753-billion-parameter open-weight model — went public under MIT license this week. It beats GPT-5.5 on coding benchmarks at one-sixth the cost, runs on hardware you control, and cannot be de-listed by a US government letter. OpenAI released open-weight models under Apache 2.0. Mistral is building sovereign European AI infrastructure. The "we have no alternative to cloud AI" assumption is eroding fast.

You've been in the identity verification business for decades. You understand that access to services can be conditional, that conditions change, and that the rules of the game are written by whoever has the power to write them.

The AI access regime is still being written. The question is whether your business will be in the room when it is, or whether you'll receive a letter on a Friday afternoon informing you of the outcome.

---

---

*Part 1: "The Kill Switch You Didn't Know About" — the June 12 export control order and what it means for any business running frontier AI.*
*Part 2: "The Regulators Just Got Fired" — Trump v. Slaughter, independent agencies, and the regulatory vacuum inside which AI vendors now operate.*

*Additional sources added July 2: [Anthropic Restores Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls](https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html) (The Hacker News); [Washington Called Anthropic's Fable 5 a Security Threat. The Only Expert Who Read the Research Disagrees.](https://easternherald.com/2026/07/02/anthropic-fable-5-restored-us-export-controls-fix-code-jailbreak/) (Eastern Herald); [Anthropic Redeploys Claude Fable 5, Adds New Cybersecurity Classifier](https://www.marktechpost.com/2026/07/01/anthropic-redeploys-claude-fable-5-on-july-1-after-us-export-controls-lift-adds-new-cybersecurity-classifier/) (MarkTechPost); [Cybersecurity experts don't think Fable 5 presents a unique threat](https://cyberscoop.com/cybersecurity-experts-anthropic-fable-5-not-unique-ai-threat/) (CyberScoop).*
