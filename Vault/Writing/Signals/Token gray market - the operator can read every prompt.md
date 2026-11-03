---
date_first_seen: 2026-08-10
date_updated: 2026-08-17
source: Okta Threat Intelligence (4 Aug 2026) / Palo Alto Unit 42 (6 Aug 2026) / Permiso (2024) / Sysdig (2024) / The Hacker News (17 Aug 2026, secondary)
url: https://www.okta.com/blog/threat-intelligence/free_tokens_for_sale/
brief: cyber
threads: [AI Sovereignty, Trust Boundaries, Machine Identity]
beat: Cyber / Shadow AI / LLMjacking
status: developing
used_in:
---

# The token gray market — the operator *can* read every prompt

**What happened.** Two independent teams published the same week. **Okta Threat Intelligence** (Jeremy Kirk,
Mathew Woodyard, 4 Aug 2026) documented named resellers — **"Poison Claude"**, ecomagent.in — charging
**5–15% of official per-token price**, stocked by fraudulent signups farming free trial credits, abuse of
**startup credit programmes ($25,000–$100,000)**, resold static API keys, and **reverse-proxy aggregation**
routing customers through pooled accounts. **Unit 42** (6 Aug 2026) documented **"transfer stations"** built
on the open-source `new-api`/`one-api` stacks, stocked by infostealers, scraped repos and npm supply-chain
worms (Shai-Hulud, Miasma), sold on Chinese marketplaces including Taobao.

Okta, verbatim, and this is the whole point:

> "the service provider has full visibility into prompts, as those prompts must be forwarded to a model."

**Why it matters.** It is a **shadow-AI story wearing a cybercrime costume**. If an employee is buying
cut-rate frontier access, the prompts go through an intermediary whose business model is unmetered
visibility. That is a data-governance failure with no breach, no incident and no alert.

## What the brief got wrong

- **SecurityWeek attribution: not found.** No SecurityWeek article matching "AI Token Chop Shops"; the phrase
  "chop shop" appears nowhere in the literature. The terms of art are Okta's **"gray market"** and Unit 42's
  **"transfer stations."** Actual coverage: The Hacker News (5 Aug), Cybernews, IT Pro, Help Net Security
  (all 6 Aug). **Cite Okta and Unit 42 directly.**
- **"Pool stolen Claude/GPT/Gemini accounts" overstates it.** Okta's headline finding is largely **fraud
  against the providers** — fake signups, abused startup credits. Unit 42's is **stolen developer API keys**.
  Neither describes pooling of ordinary consumers' personal chat accounts. The "your employees' personal
  accounts are already in criminal hands" implication is not sourced.
- **"Prompts are harvested" is not established by anyone.** Every source stops at capability. Unit 42:
  developers *"risk having their sessions monitored and mined."* Help Net: the provider *"could accidentally
  leak or sell data."* Okta frames distillation as a structural **incentive**, not an observed practice.
  See [[Capability restated as certainty]].
- **Scale is hobbyist.** From an exposed `/api/status` endpoint, Poison Claude had **881 total users, 872
  active**. Ecomagent, under 1,000. Unit 42's "tens of millions of API calls per day" is an unsourced
  capability estimate; the ~$1M figure is a single incident.

## The genuinely sharp facts

- Unit 42, verbatim: *"Attackers stole inadvertently exposed credentials and integrated them into a transfer
  station within minutes. This led to nearly a million dollars in charges before discovery."*
- **Permiso, Oct 2024** — the one case of real captured prompts, and it cuts *against* the harvesting story:
  they captured it *"in a honeypot environment where Invocation logging was enabled"*, seeing **over 75,000
  successful model invocations** — and documented that **`oai-reverse-proxy` is configured by default to not
  use an access key if Invocation logging is enabled.** The tooling actively avoids keys that log. That is a
  better detail than anything in the brief: *the market has already engineered around the only mechanism
  that would produce evidence.*

That last line is the honest, publishable version. Not "your prompts are being read" — **"the only
instrumentation that could tell you is the thing the market is built to avoid."**

## Observations

- **2026-08-10** — First seen, mis-sourced and overstated. The corrected version pairs directly with the
  same morning's `References\research_shadow-ai-global-stats_2026-08-10.md`, which found four of five
  shadow-AI percentages restated on the wrong denominator. Two shadow-AI evidence failures, same day.

## Feeds

- [[AI Sovereignty]] — inference through an unaccountable intermediary is the sovereignty problem in
  miniature, arriving via expense claim rather than procurement
- [[Trust Boundaries]] — an intermediary nobody drew on the diagram
- [[Machine Identity]] — stolen static API keys are machine credentials outliving their purpose
- [[Capability restated as certainty]]
- [[You cannot rent an audit trail]] — you cannot audit a hop you do not know exists

## Open

- **[VERIFY] before use:** the Bleich-style "employees are doing this" leap has no source. If he wants the
  workplace angle, it needs its own evidence — the Okta/Unit 42 research is about developers and fraudsters,
  not staff.
- Is there any enforcement action against a transfer-station operator? That would move this from structural
  to consequential.

---

## Update — 17 Aug 2026: it reached the secondaries, and the window is closing

The Hacker News ran "Poison Claude" today, thirteen days after Okta. Under the standing attribution
check this adds **no fact** — it is the secondary republishing the primary this signal already holds —
but it changes the signal's economics.

**This has been unspent for a week and its "nobody has written this" advantage is now largely gone.**
Once a story reaches THN, the enterprise-AI-policy angle will be covered within days by people with
no particular insight into it. **Place it or consciously retire it.**

**The angle that is still unclaimed** is not the fraud, which everyone will now write. It is the
**shadow-AI supply chain**: cheap access is not merely unapproved, it is an interception point, and
every prompt sent through it carries whatever the employee pasted in. That reframes shadow AI from a
policy-compliance problem into a **data-egress** problem, which is the version that matters to a
regulated buyer. Okta's own sentence is still the load-bearing one:

> "the service provider has full visibility into prompts, as those prompts must be forwarded to a
> model."

**Recommended placement: a 7 Sep lead, paired with Trusted Access for Cyber** — the vendor gating
access to capability at the front door, and the gray market selling a side door where the prompts are
the product. See `References\research_story-candidates_2026-08-17.md` §7, Spine A.
