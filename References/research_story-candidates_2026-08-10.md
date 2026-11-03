# Research Note — Story candidates, Monday 10 August 2026 (verification pass)
For: vault intake + Fri 14 / Sat 15 / Sun 16 slots and the 17–23 week · Depth: deep on six claims · Date: 2026-08-10

## Bottom line

Twenty candidates across three briefs. Six were taken to primaries because they were the ones plausibly
headed for a draft. **Five of the six failed**, and four failed the *same* way: a source establishes that
something **can** happen and the summary hands you something that **is** happening. Two additional failure
modes showed up in the same batch — a **prediction restated as a ranking**, and a **figure detached from the
comparison that gave it meaning**.

The corrected versions are, in every case, better than the versions that failed. That is the finding worth
carrying: this is not a hygiene exercise, it is where the argument is.

**The single most time-critical item: Claude Code's auto mode becomes the default on 14 August — Friday.
Friday is an undrafted slot whose agreed spine is "whose job is the guardrail?"**

Full notes in the vault: `Vault\Writing\Signals\`.

---

## 1. Claude Code auto mode — VERIFIED, with two corrections

**Anthropic blog, 7 Aug 2026** — https://claude.com/blog/auto-mode-default-in-claude-code
**Docs** — https://code.claude.com/docs/en/permission-modes · https://code.claude.com/docs/en/auto-mode-config
**Engineering deep dive, 25 Mar 2026** — https://www.anthropic.com/engineering/claude-code-auto-mode
**Coverage:** [TechCrunch 9 Aug](https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/) · [Simon Willison 8 Aug](https://simonwillison.net/2026/Aug/8/auto-mode/) · [Help Net Security 10 Aug](https://www.helpnetsecurity.com/2026/08/10/anthropic-claude-code-auto-mode/)
**Flagged via:** The Anthropic Stack, "Claude Code Stops Asking First", 10 Aug 2026.

Docs, verbatim:
> "Starting August 14, 2026, auto mode becomes the default permission mode for new sessions on Pro, Max, and
> Team plans."

> "Auto mode lets Claude execute without routine permission prompts. A separate classifier model reviews
> actions before they run, blocking anything that escalates beyond your request, targets unrecognized
> infrastructure, or appears driven by hostile content Claude read. Explicit ask rules still force a prompt."

> "Auto mode reduces permission prompts but does not guarantee safety."

Engineering post, Anthropic's own line:
> "The 17% false-negative rate on real overeager actions is the honest number."

**Correction 1 — "stops asking" is wrong.** It stops asking *routinely*. `permissions.deny` is evaluated
before the classifier and cannot be overridden by it; `permissions.ask` forces a prompt the classifier cannot
auto-approve; ~40 categories are blocked with zero configuration (`curl | bash`, prod deploys and migrations,
IAM grants, force push, `terraform destroy`, `git reset --hard`, writes to secret managers/DNS/TLS, merging
unapproved PRs, disabling CI checks, printing live credentials, opening tunnels or reverse shells, **writing
to Claude Code's own session transcripts**). Circuit breaker: 3 consecutive or 20 total blocks and prompting
resumes. **The un-configured state is the tight one**; configuration mostly loosens it.

**Correction 2 — plan scope.** Pro/Max/Team only. **Enterprise, the API, Bedrock, Vertex/Agent Platform and
Microsoft Foundry remain opt-in.** Most regulated shops are untouched on the 14th. Omitting this inverts the
risk picture for exactly his readership.

**Newly unprompted:** local file ops in the working directory, dependency installs from lockfiles, read-only
HTTP, reading `.env` and sending credentials to their matching API, and **pushing to any branch of the repo
you are working in, including the default branch**, plus PR creation.

**The better story:** the July–August changelog is dense with permission-**bypass** fixes — hidden commands
in zsh `[[ ]]` regex conditionals (v2.1.221/222), commands padded with tabs or invisible Unicode (v2.1.223),
commands over 10,000 characters (v2.1.214), a PowerShell 5.1 bypass (v2.1.214), `bypassPermissions` in agent
definitions ignoring org policy (v2.1.223), dynamic `import()` escaping the workflow sandbox (v2.1.223). A
string-parsing gate leaking all summer. That is simultaneously the best argument for moving adjudication to a
model, and proof the prompt was never the control. Reported safety case: n=1,053 users, humans caught **13.6%**
of dangerous commands vs **89%** for auto mode — **[VERIFY] the exact sentences before printing these three
figures**; they are read here through a verification pass, not quoted from the post.

---

## 2. RovoBlast — REAL, but the brief welded two disclosures and got the vector wrong

**Varonis Threat Labs (Dolev Taler), DEF CON 34** — https://www.varonis.com/blog/rovoblast
**PromptArmor (separate issue)** — https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data
**The Hacker News** — https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
**SecurityWeek** — https://www.securityweek.com/critical-one-click-vulnerability-in-atlassians-rovo-ai-exposed-enterprise-data/
**CSO Online** — https://www.csoonline.com/article/4207306/one-click-flaw-in-atlassian-rovo-exposed-enterprise-data-via-prompt-injection-attack.html

- Vector is a **crafted link** abusing the **`rovoChatPrompt` URL parameter**, *not* a malicious Jira ticket.
  Varonis: "a single click on a link triggers the attacker's embedded instructions and forces Rovo to accept
  externally supplied parameters as trusted inputs within a user's session." Also: "**No jailbreaks, no
  permission bypass, and no warnings or confirmation.**"
- **Fixed server-side 8 July 2026**, reporter-validated (per THN's reading of the Bugcrowd record). **No CVE.**
  No Atlassian advisory found; SecurityWeek notes "*statement from Atlassian removed at Atlassian's request*".
- **Not exploited in the wild.** THN: "Neither disclosure reports evidence that either technique has been used
  against a real organization."
- Exposure is capped at the signed-in victim's own access — THN: "not a demonstrated tenant-wide authorization
  bypass."
- **The Jira-ticket detail came from PromptArmor's separate disclosure** — a poisoned uploaded document making
  Rovo submit Jira tickets and Confluence docs to an attacker site, working "even if an organization has
  disabled web search for Rovo." Disclosed 23 May, **reportedly still unpatched as of 5 Aug 2026**.
- **"Reported via Reddit r/netsec" — no trace. Do not cite Reddit.**

**Safe formulation:** In research disclosed at DEF CON 34, Varonis Threat Labs showed that a single click on a
crafted Atlassian link could hijack the Rovo AI assistant via its `rovoChatPrompt` URL parameter, causing it to
exfiltrate Jira and Confluence data the signed-in victim could access — no permission bypass needed. Atlassian
fixed it server-side on 8 July 2026. Separately, PromptArmor reported a document-upload injection against Rovo
that it said remained unpatched as of 5 August 2026. Neither has been observed exploited in the wild.

**Re-check the PromptArmor patch status immediately before drafting.** It is the load-bearing fact.

---

## 3. "Agentic AI #1 attack vector, $4.7M" — DO NOT USE. The real version is better.

**shattered.io ran no survey** (https://shattered.io/agentic-ai-security-2026/) — SEO stat-roundup page, no
methodology, no disclosure.

- **48%** = a **Dark Reading readership poll**, no n, no field dates, no methodology
  (https://www.darkreading.com/threat-intelligence/2026-agentic-ai-attack-surface-poster-child). Verbatim:
  "Nearly half (48%) of respondents believe agentic AI **will represent** the top attack vector for
  cybercriminals and nation-state threats **by the end of 2026**." **A prediction, not a ranking.**
- **92%** = Darktrace / AimPoint, **n=1,540**, 14 countries, Oct–Nov 2025 — real methodology. But **Darktrace's
  own press release headlines 76%** for AI-agent concern; the 92% there answers "these threats are driving
  major upgrades to their defenses." Darktrace launched **Darktrace / SECURE AI the same day**.
  https://www.darktrace.com/news/over-three-quarters-of-security-professionals-concerned-about-ai-agent-risk-new-darktrace-report-finds
- **$4.7M** = **no primary**. Nearest real figure is **IBM Cost of a Data Breach 2025: $4.74M for orgs with HIGH
  levels of shadow AI** — measures shadow AI not agents, is meaningless without its **$4.07M** counterpart (the
  finding is the **$670K delta**), and was **superseded 29 July 2026**. **IBM 2026: $4.99M global average,
  ~$6M for AI-enabled malicious breaches, one in four malicious breaches AI-enabled.**
  https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled,-costing-companies-6-million-on-average
- **The SIEM/EDR "10,000 identical operations" line** traces verbatim to a **dev.to post by a founder selling
  agent-identity software**, closing with `pip install aip-identity`. shattered.io never says it.

**The real, citable version** — https://venturebeat.com/security/rsac-2026-agentic-soc-agent-telemetry-security-gap

**Elia Zaitsev, CTO, CrowdStrike:** "It looks indistinguishable if an agent runs Louis's web browser versus if
Louis runs his browser. Distinguishing the two requires walking the process tree."

VentureBeat: "In most default logging configurations, agent-initiated activity looks identical to
human-initiated activity in security logs." And: "No vendor shipped an agent behavioral baseline."

**Cloud Security Alliance**, 20 May 2026: "Because AI agents can acquire permissions dynamically and operate
across many systems simultaneously, behavioral baseline is harder to establish for agents than for human users."
https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/

**So the gap is three things and none is volume:** attribution, missing baseline, in-envelope abuse.
(The **21%** runtime-visibility and **88%** incident figures are both **n=108 self-reported** VentureBeat Pulse.
Attribute or drop.)

---

## 4. SA royal commission into AI — REAL, announced today. Three corrections.

**SBS** — https://www.sbs.com.au/news/article/australia-is-getting-its-first-major-inquiry-into-ai-its-starting-in-south-australia/xmpt3koiy
**AAP via Canberra Times** — https://www.canberratimes.com.au/story/9327566/opportunity-risk-state-unveils-landmark-ai-inquiry/
**The Mandarin** — https://www.themandarin.com.au/318030-sa-royal-commission-to-test-ais-limits/
**Royal Commissions Act 1917 (SA)** — https://classic.austlii.edu.au/au/legis/sa/consol_act/rca1917224/index.html

- **Australia's first, NOT the world's first.** No source makes the world claim.
- **"October 2026", not "1 October"** — only techAU gives the day.
- **Report due 1 July 2027** (be precise).
- Three commissioners, **unnamed**, international search. **~$3M** — do not characterise what it buys.
- **Terms of reference are 4–6 weeks away.** The six-item scope list is a paraphrase of press-conference
  remarks, not a document. "The grid" is overstated — sources say **data centres and their energy and water use**.
- **No official name gazetted** (Letters Patent not issued). **No primary release retrievable** from
  premier.sa.gov.au yet — recheck in 24–48h.
- Powers: compel attendance and production, **three months' gaol** for refusal, warrants, not bound by rules of
  evidence — **and the findings bind nobody.** SA's 2016 Nuclear Fuel Cycle RC had its central recommendation
  abandoned.
- Federal timing verified: Albanese, 15 Jul 2026 — mandatory national AI standards, **legislation expected early
  2027**, Office of AI in PM&C, National Cabinet Aug 2026. Announced policy with a drafting body, **not a bill**.

Malinauskas, verbatim: "It is absolutely clear that the use of artificial intelligence is an exciting
opportunity to advance the cause of humanity." · "But it is also true that unchecked artificial intelligence
does represent a material risk to the way our society operates and a risk to the future of work if not thought
through carefully." · A **"fork in the road"**.

---

## 5. Anthropic / Australia — PARTIALLY VERIFIED. Fix the number and the attribution.

**AFP off Treasury FOI** — https://techxplore.com/news/2026-07-mulling-ai-investment-anthropic-lobbied.html
**AFR via Investing.com** — https://www.investing.com/news/stock-market-news/anthropic-plans-to-buy-14gw-australian-data-centre-capacity-afr-reports-4775509
**Australasian Lawyer** — https://www.thelawyermag.com/au/news/general/anthropic-ties-216bn-australian-investment-to-copyright-certainty-as-canberra-weighs-ai-reform/582104
**CAIRG** — https://www.ag.gov.au/rights-and-protections/copyright/copyright-and-artificial-intelligence-reference-group-cairg
**Gilbert + Tobin on the 15 Jul package** — https://www.gtlaw.com.au/insights/australian-government-announces-mandatory-ai-standards-for-large-scale-data-centres-and-new-office-of-ai

- **US$15 billion is the primary figure. A$21.6bn is a derived conversion** (÷0.694) — evidently the
  publication's own arithmetic. Write "US$15 billion (roughly A$21.6 billion)" or no number.
- **1.4 GW capacity tender**, min 1 GW live by end-2027, to CDC / AirTrunk / NextDC / Iren / Stack.
  **Procurement, not an Anthropic-owned build.**
- **The copyright link is Treasury's characterisation in its own FOI'd briefing notes.** Anthropic **did not
  respond** to AFP. The **"long tail"** detail checks out. Officials rejected the position.
- **Cut "the same play in the EU and UK"** — no documented basis for Anthropic specifically. The UK submissions
  under scrutiny were **OpenAI's and Google's**.
- Policy state solid: **no TDM exception**, refused repeatedly (Rowland Oct 2025; PC **final** report Dec 2025 —
  do not conflate with its interim report; Government response since). CAIRG consulting on statutory / collective
  / enhanced-voluntary licensing, **no model chosen**.
- Albanese verbatim: "No company should use Australian books, music, art or news to build or train AI without
  the artist's control… Anything less, is theft." Also: "No country has got this right yet."
- **[VERIFY]** the briefing-note wording against the FOI release — the syndicated quote is garbled. **Do not
  quote Jeff Bleich** without finding the original.

---

## 6. Token gray market — REAL research, wrong attribution, and the load-bearing claim is unestablished

**Okta Threat Intelligence, 4 Aug 2026** — https://www.okta.com/blog/threat-intelligence/free_tokens_for_sale/
**Unit 42, 6 Aug 2026** — https://unit42.paloaltonetworks.com/ai-token-jacking/
**Permiso, Oct 2024** — https://permiso.io/blog/exploiting-hosted-models
**Sysdig, May 2024 (origin of "LLMjacking")** — https://www.sysdig.com/blog/llmjacking-stolen-cloud-credentials-used-in-new-ai-attack
**The Hacker News, 5 Aug** — https://thehackernews.com/2026/08/poison-claude-sells-discounted-claude.html

- **No SecurityWeek article found.** "Chop shop" appears nowhere. Terms of art: Okta's **"gray market"**,
  Unit 42's **"transfer stations"**. Cite Okta and Unit 42.
- Okta, verbatim: "the service provider has full visibility into prompts, as those prompts must be forwarded
  to a model." Pricing: **5–15% of official per-token price**; startup credits of **$25,000–$100,000** abused.
- Unit 42, verbatim: "Attackers stole inadvertently exposed credentials and integrated them into a transfer
  station within minutes. This led to nearly a million dollars in charges before discovery."
- **Nobody has shown prompts ARE harvested.** Every source stops at capability. Unit 42: developers "risk having
  their sessions monitored and mined". Help Net: the provider "could accidentally leak or sell data."
- **Scale is hobbyist:** Poison Claude had **881 total users, 872 active** (from an exposed `/api/status`);
  ecomagent under 1,000. Unit 42's "tens of millions of API calls per day" is an unsourced capability estimate.
- **The best fact, and it cuts against the scare:** Permiso captured real prompts only because *they* enabled
  invocation logging on their own honeypot key — and documented that **`oai-reverse-proxy` defaults to not
  using a key if invocation logging is enabled.** The market has engineered around the only instrumentation
  that would produce evidence.
- The "employees' personal accounts are already in criminal hands" implication is **not sourced** — Okta's
  finding is largely fraud against providers; Unit 42's is stolen developer keys.

---

## 7. Private AI cost parity — DO NOT PRINT AS A COST CLAIM

**PetronellaTech** — https://petronellatech.com/blog/private-ai-deployment-guide-enterprise/ (Craig Petronella;
his firm sells private-AI deployment, hardware procurement and CMMC/HIPAA integration)
**LocalAIMaster** — anonymous "Research Team" byline, funnels to 22 paid courses ($9–$599)
**Pricing check** — https://www.aipricing.guru/openai-pricing/
**VRAM requirement** — https://vrlatech.com/gpu-requirements-llama-3-3-70b-local/

- **Survives:** ~46 GB VRAM for Llama 3.3 70B at Q4_K_M with 8K context; 2×RTX 4090 (48 GB) is the stated
  minimum; LocalAIMaster prices that box at **$9,880**. 50K queries/month ≈ **7.7 tokens/sec sustained**. So a
  ~$10K box *can* serve a 70B-class model — at 4-bit, ~8K context, ~2 GB headroom, no redundancy.
- **Fails:** Petronella says **100K+**, not 50K — **the 50,000 figure appears in neither source.** Break-even
  is asserted with no assumptions shown. At LocalAIMaster's own 800-in/400-out, 100K queries/month costs
  **~$600 on GPT-4o** (Petronella asserts $3,000–$8,000 — 5–13× too high), ~$640 on GPT-5.6 Terra, **~$64 on
  Luna**, ~$106 on hosted Llama 70B. At 50K queries that is ~$300/month → **~33 months against a $10K server,
  50–100 months net of Petronella's own admitted $100–$200/month power.** To hit 3–6 months you need
  **280,000–550,000 queries/month.**
- LocalAIMaster refutes itself: "if you're under 100M tokens/year, cloud usually wins on raw cost", break-even
  **1.94B tokens/year** vs Together's $0.88/M. 50K × 1,200 tokens = **720M/year**.
- **Models are two generations stale on both sides.** Llama 3.3 70B (Dec 2024), Qwen 2.5 72B (Sep 2024),
  **GPT-4o (mid-2024)**. Current open tier: Llama 4, Qwen 3 / Qwen 3 Coder, DeepSeek V3/R1, Mistral Large 3;
  open frontier reported ~15–25% behind GPT-5.
- **The defensible economic argument is per-seat licensing, not per-token inference** — Petronella's own honest
  paragraph puts the Copilot crossover at **100–150 users**. Plus vendor dependency (the parked "missing
  economic leg").

---

## Passed on, and why

- **Cowbell OMNI** (AI-native claims/underwriting) — vendor announcement; the "the tool assessing the risk is the
  tool generating the risk surface" line is brief commentary, not a fact. No vault note.
- **AI agent funding ~$1.8B / dozen deals** (AIApps.com) — aggregator, no deal list. Directionally fine as colour;
  not sourceable. No vault note.
- **Practitioner channel roundup** — the brief says nothing broke through. Agreed.
- **"How AI's Demand for Compute Could Disrupt America"** (AI Supremacy) — real thread, already covered by
  `research_off-balance-sheet-ai-debt_2026-08-01.md`. Parked, not vaulted.
- **"Your Team Will Believe the Layoff Headline Over Your Roadmap"** (Nate's Newsletter) — good companion to the
  Filby caution beat; parked in `SUBSTACK_IDEAS.md`, not vaulted, because it is a framing not a finding.
- **Carnegie / European governance gap** — appended to the Convergence signal note with a **[VERIFY]**; the paper
  itself was not retrieved. Worth pulling before use; Carnegie is a good primary.
- **TechLetters "Claude and DeepSeek become a cyberattack team"** — appended to the AISI note as a **caution**.
  The brief welds it to AISI and RovoBlast; neither supports multi-agent coordination in the wild.
