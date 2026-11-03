---
date_first_seen: 2026-08-10
date_updated: 2026-08-10
source: Dark Reading / Darktrace-AimPoint / IBM Ponemon / VentureBeat RSAC 2026 / CSA — flagged via shattered.io
url: https://venturebeat.com/security/rsac-2026-agentic-soc-agent-telemetry-security-gap
brief: cyber
threads: [AI Attack Surface, Trust Boundaries, Machine Identity]
beat: Cyber / Agentic AI / Detection
status: developing
used_in:
---

# "Agentic AI is the #1 attack vector, $4.7M a breach" — the number does not exist

**What happened.** The brief carried: *48% of security pros rank agentic AI the single most dangerous
vector, 92% concerned, $4.7M average breach cost*, sourced to **shattered.io**. Verified: **shattered.io ran
no survey.** It is an SEO stat-roundup site — anonymous-ish byline, no methodology, no disclosure, headline
formatted for search. Every number on the page is second- or third-hand.

**Why it matters.** The underlying phenomenon is real and better evidenced than the fake numbers. This note
exists so the real version gets used and the fake one never does.

## What each number actually is

- **48%** — a **Dark Reading readership poll** (Tara Seals, 30 Jan 2026). **No sample size, no field dates,
  no methodology published.** And it is a *prediction*, not a ranking. Verbatim: *"Nearly half (48%) of
  respondents believe agentic AI **will represent** the top attack vector for cybercriminals and nation-state
  threats **by the end of 2026**."* A forward-looking belief has been converted into a present-tense ranking
  of observed threats. **Do not write it as a ranking.**
- **92%** — **Darktrace, *The State of AI Cybersecurity 2026***, fieldwork by AimPoint Group, **n=1,540**,
  14 countries, Oct–Nov 2025. Real methodology. But **Darktrace's own press release headlines 76%** for
  AI-agent concern; the 92% in that release answers *"these threats are driving major upgrades to their
  defenses."* Darktrace's blog does render 92% as agent concern. Use **76%**, or state which question the
  92% answers. Darktrace **launched Darktrace / SECURE AI the same day** — the vendor sells the remedy.
- **$4.7M** — **no primary exists.** shattered.io's citation is the string "2026 agentic AI statistics
  compilation." The nearest real figure is **IBM *Cost of a Data Breach 2025*: $4.74M for organisations with
  HIGH levels of shadow AI** — which (a) measures shadow AI, i.e. employees pasting into unsanctioned
  chatbots, **not agents**; (b) is meaningless without its other arm, **$4.07M** for low/no shadow AI —
  the finding *is* the **$670K delta**, and quoting one arm destroys it; (c) was **superseded on 29 July
  2026**. IBM 2026: global average **$4.99M**, **AI-enabled malicious breaches ~$6M**, one in four malicious
  breaches AI-enabled. **If a number is needed, use IBM 2026's ~$6M.** It is measured, current and named.
- **The SIEM/EDR line** — *"built to detect anomalies in human behavior. An agent that runs code perfectly
  10,000 times in sequence looks normal"* — traces **verbatim to a dev.to post by a founder selling agent
  identity software**, closing with `pip install aip-identity`. shattered.io never says it. It is a vendor
  pitch, and technically shaky: repetitive machine behaviour is if anything *trivially* baselined.

## The real version, which is better

**Elia Zaitsev, CTO, CrowdStrike**, on the record (VentureBeat, RSAC 2026, 31 Mar 2026):

> "It looks indistinguishable if an agent runs Louis's web browser versus if Louis runs his browser.
> Distinguishing the two requires walking the process tree."

VentureBeat's own finding, same piece:

> "In most default logging configurations, agent-initiated activity looks identical to human-initiated
> activity in security logs."

> "No vendor shipped an agent behavioral baseline… neither defines what normal agent behavior looks like in
> a given enterprise environment."

**Cloud Security Alliance** (neutral body, 20 May 2026): *"Because AI agents can acquire permissions
dynamically and operate across many systems simultaneously, behavioral baseline is harder to establish for
agents than for human users."*

Scale, George Kurtz keynote: sensors see *"more than 1,800 distinct AI applications running on enterprise
endpoints, representing nearly 160 million unique application instances"* — into *"SIEM systems architected
for human-speed workflows."*

**So the gap is three things, and none of them is volume:**
1. **Attribution** — agent- and human-initiated actions are indistinguishable in default logs.
2. **No baseline** — nobody has defined normal agent behaviour, so there is nothing to deviate from.
3. **In-envelope abuse** — when the instructions are attacker-supplied, the resulting operations still sit
   inside the agent's legitimate permission and behaviour envelope.

That third one is the argument, and it is the same shape as *Every Gate Said Yes* (Mon 10 Aug): the control
answers correctly and the answer is not the question.

## Observations

- **2026-08-10** — First seen. Every headline figure failed verification; the underlying claim survived and
  improved. Fourth instance this fortnight of a brief item whose provenance chain ends at a company selling
  the remedy — see [[Capability restated as certainty]].

## Feeds

- [[AI Attack Surface]] — the detection gap, correctly stated
- [[Trust Boundaries]] — in-envelope abuse is the boundary that answers correctly
- [[Machine Identity]] — attribution is a machine-identity problem before it is a detection problem
- [[Capability restated as certainty]] — the pattern this is an instance of
- [[Convergence - attack surface attacker and attack]]

## Open

- The **21% runtime visibility** figure (VentureBeat Pulse) is **n=108, self-reported**. Directionally
  useful, statistically nothing. Attribute or drop.
- The **88%** "at least one agent-related security incident" figure has the same n=108 base. Same treatment.
- Worth a dig: has anyone actually shipped an agent behavioural baseline since RSAC? That is a genuine
  open question and would date the piece well.
