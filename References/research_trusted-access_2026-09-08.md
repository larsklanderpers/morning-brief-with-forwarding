# Research Note -- Trusted Access, Daybreak, and the three labs' capability gates
For: `substack_draft_approval-not-automatic_2026-09-10` (Thu 10 Sep) · Depth: deep · Date: 2026-09-08

**Firewall:** this note deliberately contains NOTHING on chain-of-thought monitorability, Pachocki, or
the CoT decline. That is Fri 11's piece (`research_astra-recurrent-depth_2026-09-04.md`). Nothing below
requires it.

---

## Bottom line

Every load-bearing claim in the plan's Thu 10 block is now footed at a vendor primary, and three things
changed. First, **the plan's own working title is a verbatim quote from OpenAI's help centre** -- *"OpenAI
reviews requests before enabling access. Approval is not automatic."* Second, **Daybreak Blue does not run
Astra.** It runs GPT-5.6 Sol, as does Daybreak Red; Astra's advanced cyber capabilities went to "a small
group of alpha testers," and the defensive programme the plan describes as going first is going first on
the *previous* model. Third, and strongest for an Australian reader: **two of the three access instruments start
in the United States** (⚠️ CORRECTED 9 Sep -- an earlier version of this line said all three, which this
note's own Fairwind section contradicts: Google states no geographic restriction. The Thu 10 draft
carried the error into a section header before the Round 4 panel caught it.) -- Anthropic's explicitly and only, OpenAI's $1B subsidy "starting with the United
States," and Google's the only one of the three that is neither US-scoped nor future-tense. The
asymmetry the 5 Sep addendum found is real and it survived an adversarial pass.

---

## What is solid

- **"Approval is not automatic" is OpenAI's own sentence.** *"Trusted Access for Cyber is the governance
  model for OpenAI Daybreak."* … *"OpenAI reviews requests before enabling access. Approval is not
  automatic."* -- [OpenAI Help Centre, Daybreak / Trusted Access for Cyber overview](https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview) (fetched 8 Sep 2026)
- **What OpenAI asks for.** Applicants may be asked about *"Your organization and cybersecurity
  capabilities. The defensive cybersecurity workflows you want to support. The OpenAI organization or
  workspace you expect to use. Verification or trust information needed to assess eligibility."* Access
  cannot extend to *"third-party customers, external users, customer-facing workflows, or downstream
  product traffic."* -- same page. **That last clause is a procurement fact: an MSP or reseller cannot
  pass the capability through to a client.**
- **★ Daybreak Blue is built on GPT-5.6 Sol, not Astra.** *"Daybreak Blue is the recommended starting
  point for most security teams. Built on GPT-5.6 Sol with Trusted Access for Cyber, it supports approved
  defensive workflows including secure code review, vulnerability triage, detection engineering, incident
  response, malware analysis, and patch validation."* -- same page.
- **Daybreak Red exists and the plan does not have it.** Blue is general-purpose models with defensive
  safeguards; Red *"provides access to our purpose-trained cybersecurity models for authorized
  vulnerability research, exploit validation, and security testing"*, including *"GPT-5.6-Cyber, available
  through Daybreak Red access, to further reduce refusals."* Access is controlled *"through identity
  verification, account security, monitoring, approved-use restrictions, and legal attestations."*
  -- [OpenAI, "Expanding Daybreak as the Cyber Defense Window Narrows"](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/), 10 Aug 2026.
- **Astra's cyber capability is staged behind alpha testers.** *"We plan to make Astra available soon, but
  access to its most advanced cybersecurity capabilities will be more limited."* … *"Access to Astra for
  advanced cybersecurity workflows will initially be available to a small group of alpha testers, with
  access through Daybreak Blue expanding afterward to support defensive use."* -- [OpenAI, "Path to Astra"](https://openai.com/index/path-to-astra/), 1 Sep 2026.
- **The Critical designation, in OpenAI's words, under OpenAI's framework.** *"We now believe Astra meets
  the Critical cybersecurity capability threshold under our Preparedness Framework, meaning that with the
  right tools and access, it can find previously unknown security flaws and develop ways to exploit them
  across many well-protected systems without a person guiding each step."* … *"It is the first model we
  are designating at this level, and requires stronger safeguards during development and before release."*
  -- same page.
- **★ Anthropic: US-only, future tense, confirmed at the primary and still true on 8 Sep.** *"The CVP
  currently provides access to certain Opus- and Sonnet-class models with reduced cyber safeguards for
  defensive security work. In the near future, this program will also include access to Claude
  Mythos-class models."* And, verbatim: *"Currently, it is only available to a set of US organizations,
  though we're coordinating with the US government to expand access to a broader set of domestic and
  international partners as quickly as possible."* -- [Anthropic, "Introducing Claude Fable 5.1 and Claude Mythos 5.1"](https://www.anthropic.com/claude-fable-and-mythos-5-1) (re-fetched 8 Sep 2026, unchanged).
  ⚠️ **The concession clause is mandatory** -- the 5 Sep addendum quoted only the first half. Printing
  "US-only" without "coordinating with the US government to expand" is quoting half a sentence.
- **Anthropic's mechanism is safeguard reduction, not a model tier.** *"Claude Mythos 5.1 is identical to
  Fable 5.1, but it offers more permissive safeguards for vetted individuals and organizations."* -- same
  page. Corroborated at [claude.com/blog/bringing-claude-mythos-5-to-more-defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders): *"reduced safeguards, minimizing interruptions for accepted teams doing legitimate cybersecurity work on systems they're authorized to protect."*
- **★ Google Fairwind is the only one of the three with written operational-security obligations on the
  buyer.** *"We vet all applicants to make sure they have a proven track record of ethical operations and
  research."* Participants must maintain *"user-level authentication, phishing-resistant MFA, and
  applicable access controls"*; *"Organizations may only grant Gemini 3.8 Flash Cyber access to internal
  cybersecurity, incident response, or penetration testing teams"*; they *"must track employee access and
  use"*; and *"we do not allow partner organizations to share, redistribute, or sell access."*
  -- [Google DeepMind, Fairwind Program](https://deepmind.google/fairwind-program/) (fetched 8 Sep 2026).
- **Fairwind's priority sectors are named:** *"Governments and national cyber authorities"*, *"Critical
  infrastructure operators"* (healthcare, telecommunications, energy, financial networks), and *"Core
  technology platforms."* No geographic restriction appears on the page.
- **Gemini 3.8 Flash Cyber has no published price; the base model's price doubles at year end.** Flash is
  *"$0.75 per million input tokens and $3.75 per million output tokens"* introductory through 31 Dec 2026,
  rising to $1.50/$7.50. The Cyber variant is *"available to trusted defenders through our new Fairwind
  Program"* with no separate price published. -- [Google, "Introducing Gemini 3.8 Flash and 3.8 Flash Cyber"](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/), 2 Sep 2026.
- **The $1B is subsidised access, not money, and it starts in the US.** *"$1 billion in subsidized Daybreak
  access to help resource-constrained cyber defenders"*, for *"state and local governments, critical
  infrastructure operators, nonprofits, open-source maintainers, and supporting organizations"*, *"starting
  with the United States"* with plans to expand to partner countries, *"targeting it to be consumed over
  the next six months"*, plus an MS-ISAC pilot for *"state, local, tribal, and territorial cyber
  defenders."* -- [OpenAI, "Daybreak for Frontline Defenders"](https://openai.com/index/daybreak-for-frontline-defenders/), 3 Sep 2026.

---

## What is contested / watch out

- ⚠️ **"$1B across 20+ countries" is a blend of two OpenAI statements and must not be printed as one.**
  The product page (3 Sep) says the $1B subsidy starts with the United States. The policy blog (4 Sep) says
  *"Daybreak is already active in more than 20 countries and multilateral institutions"* and calls the
  money a *"$1 billion global commitment"*, *"building on OpenAI's cybersecurity partnerships and outreach
  in more than 35 countries."* -- [OpenAI Global Affairs](https://openaiglobalaffairs.substack.com/p/astra-puts-more-within-reach). Both are OpenAI's. The programme's footprint and the
  subsidy's footprint are different things. **Print them separately or not at all.** Lars's own 5 Sep AI
  brief already blended them ("$1B … active in 20+ countries").
- ⚠️ **HIS OWN BRIEF ASSERTS THE FALSE SYMMETRY.** The 5 Sep AI brief's strategic take reads *"All three
  major labs now ship in two speeds -- public capability and access-controlled capability."* On the
  primaries that is wrong on tense for Anthropic's Mythos tier and wrong on mechanism (safeguard
  reduction, not a tier). If the piece quotes the brief it inherits the error; if it *corrects* the brief
  it has an honest opening. The correction is the better move and it is his own house catching it.
- ⚠️ **Press summaries diverge from OpenAI's own text on who gets Astra.** CSO Online (via the 6 Sep AI
  brief) says Astra was *"initially gated behind Daybreak … then expanding to paid consumer and enterprise
  accounts."* TechCrunch (via the 5 Sep addendum) said it was *"available Thursday to OpenAI customers that
  use Daybreak."* OpenAI's own page says **alpha testers first, Daybreak Blue after.** Where they
  disagree, use OpenAI's. The "defenders got it first" opening image is weaker than the addendum thought
  and needs rewording -- see DO NOT PRINT.
- **The 650+ partner figure is Google's own and single-source.** *"We currently work with over 650 partners
  globally"* -- Google, on Google's page. No independent count located. Attribute it in text or leave it.
- **Google's CCL line was not re-verified today.** The 5 Sep addendum quotes Google's *model card* saying
  3.8 Flash is *"unlikely to reach any T/CCLs."* The 2 Sep launch blog carries no CCL sentence at all, and
  the model card itself was not fetched for this note. Treat as second-hand until someone opens the card.

---

## Could not verify

- **No price for the gated tier at any of the three labs.** Checked three OpenAI pages (the Trusted Access
  help centre overview, "Expanding Daybreak", "Daybreak for Frontline Defenders"), the Fairwind programme
  page, and the Gemini 3.8 launch blog. **None carries a price for the gated capability.** Recorded as a
  documented absence on five paths, not as an assertion that no price exists anywhere. Do not write
  "nobody publishes a price"; write what was checked.
- **Whether any Australian organisation is in any of the three programmes.** Not searched at a primary and
  not assertable either way. Do not claim Australian exclusion from Fairwind -- Google states no
  geographic limit. The US-only fact belongs to Anthropic's CVP alone.

---

## The economics

The published-price stack has a hole in exactly one place, and it is the place that matters to a buyer.
Astra's general API rate is $10 / $50 per million tokens; Gemini 3.8 Flash is $0.75 / $3.75 and already
scheduled to double on 1 January 2027. Both are on a pricing page. **The cyber tier is not on any pricing
page at any of the three labs.** You can budget for the model you are allowed to buy and you cannot budget
for the model you have to apply for.

And the subsidy is a rate, not a fund: $1B of access *"targeting it to be consumed over the next six
months"* is roughly $167m a month of somebody else's inference, aimed first at US state and local
government and US critical infrastructure. For a CPS 230 reader the question is not whether the gate is
reasonable. It is that the capability's price, its availability date, and its geography are all set
outside the contract, by a party the buyer cannot negotiate with, and none of the three can be
diligenced from a published document.

---

## Drop-in facts (each already footed above)

- *"OpenAI reviews requests before enabling access. Approval is not automatic."* -- OpenAI Help Centre.
- *"Daybreak Blue … Built on GPT-5.6 Sol."* -- OpenAI Help Centre. **The defensive tier is last year's model.**
- *"a small group of alpha testers, with access through Daybreak Blue expanding afterward."* -- Path to Astra.
- *"It is the first model we are designating at this level."* -- Path to Astra.
- *"Currently, it is only available to a set of US organizations, though we're coordinating with the US
  government to expand access to a broader set of domestic and international partners as quickly as
  possible."* -- Anthropic.
- *"Organizations may only grant Gemini 3.8 Flash Cyber access to internal cybersecurity, incident
  response, or penetration testing teams"* and *"must track employee access and use."* -- Fairwind.
- Access *"cannot extend to third-party customers, external users, customer-facing workflows, or
  downstream product traffic."* -- OpenAI Help Centre. **The reseller clause.**
- *"$1 billion in subsidized Daybreak access … starting with the United States … targeting it to be
  consumed over the next six months."* -- OpenAI.

---

## ⛔ DO NOT PRINT (binds every revision of this piece, not just v1)

1. **"The most capable model went to the defenders first."** OpenAI's own text says alpha testers first and
   Daybreak Blue after, and Daybreak Blue runs Sol. The addendum's opening image is built on a TechCrunch
   paraphrase that the vendor primary does not support. **The true version is sharper anyway: the
   defenders' programme is running on the previous model while the Critical-rated one sits with alpha
   testers.**
2. **"All three labs ship in two speeds."** False on tense and mechanism. Correct it, do not repeat it.
3. **Any ranking of the three labs by capability tier.** The Critical designation is OpenAI's, under
   OpenAI's Preparedness Framework. Google's CCL language is a different framework. Welding them ranks two
   companies on one scale that does not exist.
4. **"$1 billion across more than 20 countries."** Two separate OpenAI claims. See contested.
5. **Anything about chain-of-thought, monitorability, or Pachocki.** Friday's, and Friday is locked and
   already promised in print by Monday's scheduled piece.
6. **"Nobody publishes a price."** Say what was checked and what was not on it.

---

## Angles this opens

- **Callback available to Thu 3 Sep, "The Number Nobody Can Produce"** -- that piece asked who inside your
  building gets to say "critical." This one is the same word decided outside your building, by a vendor,
  under a framework you did not write and cannot audit. Same word, different building. ⚠️ Check the closes
  and the "who gets to say" construction against Thu 3 before using it; it ran five days back.
- **The reseller clause is his ground and nobody else's.** *"Access cannot extend to third-party customers
  … or downstream product traffic"* means the managed-services model does not reach the capability tier at
  all. That is a first-person procurement fact he can hold, and it is not in any of the coverage.
- **Signpost to Fri 11 is mandatory:** the gate on the front; Friday is the window. Gate, then glass.
- ⚠️ **Register adjacency with Tue 8** (`opt-out-proxy`), which landed as *a real control held by somebody
  else who has no reason to act*. Thursday must differentiate on mechanism -- three instruments a buyer
  cannot compare, and a price nobody can find -- rather than on the held-by-someone-else move.

