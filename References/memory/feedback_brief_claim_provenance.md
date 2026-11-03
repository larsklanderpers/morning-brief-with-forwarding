---
name: brief-claim-provenance
description: "The recurring failure engines in the daily briefs — modal-verb drop, attribution drop, denominator drop, co-authorship collapse, killed-claim regeneration, citation laundering by proximity, and superlative insertion — and the order to check them in"
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

The briefs fail in a small number of repeating shapes. Check them in this order, on every claim,
before it enters a draft. **Seven engines, not one.**

## 1. The MODAL-VERB DROP (identified 10 Aug 2026 — 5 of 6 checked claims failed on it)

`can` → `does`. `may have been accessed` → `were stolen`. `proof-of-concept` → `exploited`.
`researchers demonstrated` → `attackers are using`. `proposed` → `required`. `guidance` → `mandate`.
Roadmap future tense → shipped.

**How to apply:** find the primary's verb and quote it. Microsoft's *"could exploit"* and
*"Exploitation Less Likely"* are not "is being exploited." OpenAI's *"we will expand it so Codex can
fully command the browser"* is not "Codex automates anything." Twitch's *"may be used"* is not "is
training on."

**A variant worth its own name — PARAPHRASE PROMOTION (16 Aug 2026).** The primary names the person
but never quotes them saying the thing. Axios's own framing prose — AI "could wipe out half of all
entry-level white-collar jobs — and spike unemployment to 10-20%" — sits *outside* quotation marks,
and is now universally cited as "Amodei predicted 20% unemployment." Three upgrades stacked:
could→will, range→ceiling, five-year window→now. **Check whether the load-bearing sentence is inside
the quote marks.**

**A 19 Aug case, and it is the most consequential yet.** The 19 Aug brief printed "EU AI Act
enforcement live since August 2 — Annex III high-risk requirements… activated August 2." The
**Digital Omnibus (Reg. (EU) 2026/1744) entered into force 27 July 2026 and deferred Annex III
high-risk obligations to 2 December 2027** — five days before the date being cited. What actually
commenced was GPAI enforcement, Article 50 transparency, and the penalty framework. **Half the AI
governance commentary in circulation is describing obligations that were postponed.** When a
compliance date is load-bearing, re-check the date *itself* — not just the obligation attached to it.

## 2. The ATTRIBUTION DROP (identified 14 Aug 2026 — this one survives a numbers check)

**Three of the 14 Aug brief's items had their numbers quoted correctly and their attribution wrong.**
A numbers-only fact-check passes all three. This is the more dangerous engine because it looks clean.

The three real cases, worth remembering as the pattern:
- **Name collision laundered by Wikipedia.** The Aura breach (identity-protection company) was
  attributed to ShinyHunters, whose campaign was against Salesforce Experience Cloud's
  `/s/sfsites/aura` endpoint. Two unrelated things sharing a word, welded in the record. Aura named
  no actor.
- **Vendor survey wearing an industry body's masthead.** "State of AI Cybersecurity 2026" is
  **Darktrace's**; CSA republished it and the page says so. Read as CSA, it is neutral research.
- **A claim with no referent at all.** "New adversarial evaluation frameworks" — nothing shipped;
  the real event was already spent twice in the pipeline under a different label.

**How to apply — three questions:** who published it, *not who republished it* · what do they sell ·
is the actor or author named by the primary, or only by a downstream summary.

**A 16 Aug addition to this engine — the academic launder.** Almost every organisational-governance
figure in **Stanford HAI's AI Index 2026** is **McKinsey survey data re-published by Stanford**.
"Stanford's AI Index found…" reads academic; the number is a consultancy survey (excluding China).
Write "the AI Index, *citing McKinsey's 2025 survey*." The AI Incident Database counts in the same
chapter genuinely are independent — so the report is a mix, and the mix is the trap.

**A 17 Aug case, and it is the cheapest one to catch.** The Hacker News ran "Poison Claude" thirteen
days after **Okta Threat Intelligence** published it (4 Aug) and Unit 42 corroborated it (6 Aug). The
brief carried THN as the source. No fact was wrong — but the vault already held the primary, and the
brief presented the secondary as the finding. **When an item feels new, check the Signals folder
before checking the web.**

**A 19 Aug case — the invented survey.** The brief cited a "Belitsoft survey" for "enterprises run
12 AI agents, half operate autonomously." **Belitsoft ran no survey.** The item is a paid ABNewswire
press release from a software outsourcing firm, syndicated to openPR/Barchart/FinancialContent. Both
numbers are other people's — 12 agents is **Salesforce's** 2026 Connectivity Benchmark (n=1,050 IT
leaders), and "60% of work / 0–20% fully delegate" is **Anthropic's**, from a foreword, self-reported,
**with no stated n at all**. Worse, the autonomy claim is inverted: Salesforce measured agents
*"operating in isolated silos versus part of a multi-agent system"* — an **integration** finding.
**A press release distributed by a wire service is not a study, however many outlets carry it.**

**A 20 Aug case — the affiliation upgrade.** The brief carried "**Anthropic and EPFL** demonstrated"
for arXiv 2608.10218 (*Mind Viruses*). The by-line is two Anthropic staff, two **Anthropic Fellows
Program** members (an external fellowship), and **EPFL as one author's second affiliation**. Not a
two-lab collaboration. **A fellowship is not a staff affiliation and a second affiliation is not an
institutional partner** — check the footnote markers, not the list of institution names.

## 3. The DENOMINATOR DROP (identified 14 Aug 2026 — literally accurate, materially misleading)

The number is right and the noun after it is wrong.
- *"approximately 900,000 records"* became "900,000 customer records" — it was a marketing contact
  list mostly inherited in an acquisition five years earlier; identifiable customers were ~35,000.
  **Wrong by 25x, with the number quoted correctly.**
- *"67% report that theirs uses agentic AI"* (present in security tooling, vendor features included)
  became "67% have deployed agentic AI for security ops."
- *"95% have delayed or canceled AI initiatives"* is a floor-of-one over twelve months; the
  informative figure in the same release was *55% reporting more than six.*

**How to apply:** ask whether the denominator matches the noun in front of the number, and whether a
break-out figure elsewhere in the same source reveals the headline to be a one-or-more measure.

**Two 16 Aug cases worth keeping as calibration:**
- **Mandiant's "five days to exploit"** is an **average**, not the universally-reported median; its
  denominator is *138 vulnerabilities already known to be exploited*; and Mandiant says in the same
  paragraph that **"without the removal of these outlier TTEs, the average grows from five to 47."**
- **Stanford's "19% below"** for 22–25s in AI-exposed occupations is a **relative gap between two
  same-aged groups**, not an absolute decline and not an unemployment rate.

**A 17 Aug case — the two-denominator gap.** "54% of US workers say AI skills are critical for job
stability, but only 4% are pursuing AI education." A compelling gap that almost certainly compares
two different base populations, with no publisher, no fielding date and no definition of "pursuing."
**A gap statistic needs both halves measured on the same people; ask that before anything else.**

**Three 19 Aug cases, and the third is the one to remember.** *"1.6 million RingCentral accounts"* is
HaveIBeenPwned's count of **unique email addresses in a leak-site archive** — the company has
confirmed no figure at all. *"678,000 individuals"* at DGFiP is 678,000 **individuals and
businesses**, and provisional. And **"91% of enterprise AI apps appeared in 16 months"** (Material
Security) has a headline denominator of ~22,000 apps but a **sampling unit of about twenty Google
Workspace tenants** — and the accompanying claim that most arrived "through individual OAuth grants
rather than IT procurement" **is not measured anywhere in the report.** It is marketing copy the
reader is invited to infer. **When a vendor's big number and its interesting number have different
denominators, the interesting one is usually unmeasured.**

## 4. The CO-AUTHORSHIP COLLAPSE (identified 16 Aug 2026 — passes all three checks above)

Two publications counted as two observations when they are one team twice.

The case: the brief carried "Yale's Budget Lab **and** Brookings find no meaningful change." The
Brookings piece is co-authored by **Martha Gimbel, Executive Director of The Budget Lab at Yale**,
with two Budget Lab staff. Same CPS occupational-mix method, same dataset, second masthead.

Run it through the attribution questions: Brookings published it ✓ · they sell nothing ✓ · all four
authors named by the primary ✓ · denominator matches ✓. **Four for four, and the sentence is still
wrong.** The error is not in the source, the seller, the attribution or the arithmetic — it is in
counting two mastheads as two independent findings.

**How to apply — one question:** *are these two sources, or one source twice?* **Read the author
list before writing "independent confirmation," "corroborates," or "both found."**

**A 19 Aug variant — MASTHEAD MULTIPLICATION, and it is the mirror image.** There is a *second*
Brookings item in this space: **"Research on AI and the labor market is still in the first inning,"
by Jed Kolko — who is at PIIE, not Brookings** — published **10 March 2026**. Gimbel is **not** a
co-author; she is acknowledged for supplying figures. But **the identical article appears under three
mastheads: Brookings, The Hamilton Project (housed at Brookings), and PIIE.** One author, one
argument, three logos, partly downstream of Yale's numbers. Anyone counting mastheads gets to "three
institutions agree."
⚠️ **These two Brookings items have not been reconciled against each other** — check whether the
16 Aug case and this one are the same piece described differently before either is cited.
**The generalised question: how many *articles* is this, not how many logos.**

## 5. KILLED-CLAIM REGENERATION (identified 17 Aug 2026 — the engine that is not editorial)

**Claims that a research note explicitly killed reappear in later briefs as findings.** Two in the
17 Aug intake alone:

- *"115,000 tech layoffs through May 2026, approaching all of 2025's 124,000."* Killed **27 days
  earlier** in `References\research_it-layoffs-h1-2026_2026-07-21.md`: *"directionally right, now
  stale, and **never directly citable**"* — **no source prints exactly 115,000.** Correct figures:
  ~120,000 H1 tech-company layoffs (Layoffs.fyi) **or** 139,156 announced US tech-sector cuts
  (Challenger, +83% YoY). Name the tracker; never blend them.
- *"'What should I learn' is converging on agentic orchestration."* Killed **3 days earlier** in the
  14 Aug dig: *"No evidence base. Zero actual Reddit threads; every returned source sells
  orchestration training. Cut, do not hedge."* Regenerated verbatim.

**Why it happens, and why it is not a judgment failure:** the do-not-print lists live in
`References\research_*.md` and in the week plans' accuracy watchlists. **`briefing_agent.py` does not
read any of them.** Each morning's generator starts from the open web with no memory of what was
killed, so a dead claim that is still circulating regenerates on schedule.

**How to apply — two things.** (a) Before triaging any intake, grep `References\` and the current
week plan's watchlist for the item's distinctive number or phrase; a killed claim is far more likely
than a new one when the number is round and quotable. (b) The durable fix is plumbing, not
vigilance — a single killed-claims file the generator checks against before an item ships. Raise it;
do not build it unasked.

**⚠️ 19 Aug — regeneration ESCALATES. The same CVE came back with a bigger claim.** The 14 Aug dig
established CVE-2026-68820 as an elevation of privilege, CVSS 7.0, Important, race condition, with the
Lazarus attribution belonging to Check Point. On 19 Aug the brief printed it as a *"Windows Task Host
flaw"* (it is the Ancillary Function Driver for WinSock, `afd.sys`), *"first flagged as exploited in
April"* (published and patched 11 August), and **"now confirmed in active ransomware deployment"** —
against CISA's own KEV field reading `"knownRansomwareCampaignUse": "Unknown"`, Microsoft's exploit
maturity of *"Unproven"*, and a Check Point report that does not contain the word "ransomware." It is
Lazarus / Operation Dream Job against aerospace and defence. **Track regenerating items by CVE number
or proper noun, not by the sentence that was killed — the sentence mutates upward.**

**⚠️ 20 Aug — regeneration of a KILLED ATTRIBUTION, six days on.** The 14 Aug dig established that
"State of AI Cybersecurity 2026" is **Darktrace's** report, republished by CSA, and that the
50/45/40 percentages are **self-reported worries, not incidence**, and the 67% is "agentic AI present
in the stack," not "deployed for autonomous security operations." The 20 Aug brief printed it again,
attributed to the **Cloud Security Alliance**, with the percentages read as findings and the 67% read
as deployment. **Same item, same three errors, six days later.** It is also **an April 2026 report**
(CSA blog URL dated 2026/04/02) running in an August brief as today's signal — so it fails the date
trap as well. Strongest available argument for the killed-claims file.

## 6. CITATION LAUNDERING BY PROXIMITY (identified 19 Aug 2026 — the one that defeats every check above)

**The other engines all involve something being dropped or altered between the primary and the
brief. This one drops nothing. The citation is present, the cited source is real and credible — and
the claim is not in it.**

The case: the 19 Aug AI brief attributed five claims to a GMI Cloud post on open-weight benchmarks
(5 Aug 2026). **Four of the five appear nowhere in that post.** The strings `55%`, `12%`,
`on-premises` and `enterprise inference` are absent from a document cited for *"enterprise
on-premises inference is now at 55% of total, up from 12% in 2023."* The post discusses Qwen3.8-**Max**
and Muse **Spark**; the brief credited it with Qwen3.8-27B and Muse **Glimmer**.

**What makes it the worst engine:** a four-minute provenance check passes it. Click the link — real
site, named author, real article on the right topic, published two weeks ago, hedging appropriately.
Nothing about the citation looks wrong because nothing about the citation *is* wrong. It simply isn't
the source of the claim.

**And the outcome is arbitrary.** Three of the four orphaned claims happened to check out against real
primaries elsewhere. One — the 55% — **has no origin anywhere in the world**; the nearest things are
two Gartner figures measuring edge data analysis and public-cloud IaaS *spend*, both pointing the
other way. One was the vendor's own SEO content ranking its own product first. **A correct-looking
citation had been doing the work of provenance for a claim that had none.**

**How to apply — the fourth question in the four-minute check:**
> **Do not verify the source. Verify the claim inside the source.** Open the cited URL and search it
> for the number or the proper noun. **If it is not in the document, the citation is decorative and
> the claim has no provenance at all** — however good the citation looks.

**A related shape from the day before (16 Aug), and the pair is the argument.** *The AI Leadership
Edge* inverted BCG's *"61% of CEOs believe boards are **rushing** AI transformations"* into "boards are
pushing them to move faster" — **in the framing sentence directly above a correct link to the BCG
PDF.** One where the link is right and the framing reverses it; one where the link is right and the
claim was never in it. **Both failures survive the click**, which is the whole reason the click stopped
being sufficient.

**⚠️ 20 Aug — the no-citation variant, and it is how the worst item got in.** The *Mind Viruses*
item shipped sourced to *"Preprint (Aug 10, 2026) | referenced in IT Security News."* **No URL at
all.** The upstream secondary (The Hacker News, 18 Aug) describes the preprint accurately but
**publishes no link to it either**, so nothing in the chain pointed at arXiv 2608.10218. **An item
with no URL is not a weaker citation than a bad one — it is the absence of the check entirely, and
it should stop the item, not merely flag it.**

**⚠️ And the LLM-summary trap, first seen 20 Aug.** For arXiv 2608.10218, the top non-arXiv search
result is **alphaXiv**, whose auto-generated summary lists the tested models as "Claude 3.5 Sonnet,
Gemini 1.5 Pro." The paper tested Claude Sonnet 4.6, GPT-5.4, Claude Haiku 4.5, DeepSeek V3.2,
Qwen 3.5 32B, Gemini 3 Flash, Gemini 3.1 Pro and Llama 3.3. **A machine-written summary of a real
paper, wrong on a checkable fact, ranking above the paper.** Treat alphaXiv, emergentmind and similar
as unciteable; read the PDF.

## 7. SUPERLATIVE INSERTION (identified 20 Aug 2026 — nothing is dropped, something is *added*)

**The source is real, the mechanism is described broadly correctly, and the brief has added an
adjective that appears in no source and that the primary's own text refutes.**

The case: *"**First credible demonstration** that multi-agent AI architectures have an intrinsic
propagation risk."* That phrase is nowhere in arXiv 2608.10218, whose related-work section
acknowledges prior self-propagating-attack papers. **Morris II** (*Here Comes The AI Worm*, arXiv
2403.02817) is **March 2024**. **AgentWorm** (arXiv 2603.15727) is **March 2026** and closer in
shape — 63% aggregate ASR, multi-hop, persistence across restarts. Roughly twenty-nine months of
prior art. The brief also inverted the paper's verdict, printing urgency over the authors' own
*"real but currently limited risk"* and omitting the finding that *"adding a brief warning to an
agent's system prompt confers near-total immunity."*

**Why it needs its own engine:** engines 1–6 are all subtractive or substitutive — a verb weakens, an
attribution slips, a denominator vanishes, a citation decorates. This is **additive**. There is no
upstream sentence to compare against, because the claim was manufactured in the summarising step.
A source-by-source diff will not surface it.

**How to apply.** **Treat every "first," "unprecedented," "largest," "no one has," and "marks the
first time" in an intake as a research task, not a fact.** Search the primary for the superlative; if
it is not there, the brief invented it. Then spend four minutes on prior art before deciding whether
the hedge or the correction is right — **and prefer the correction, because it is almost always
sharper.** "The third serious agent-worm paper in five months, and the first to report the defense is
a paragraph" beats both "the first demonstration" and "one of several demonstrations."

**This is the [[Absolutes & Overconfidence]] defect arriving through the intake rather than through
drafting**, and the same fix applies: **specificity, not hedging.** Same day, the brief also printed
*"the first government-confirmed use of AI-generated scripts in active ICS exploitation"* about a
Siemens PLC advisory — a second superlative in the same edition, unverified. When one appears, check
the whole edition.

## The structural finding underneath all seven

**The primary source is quieter than the secondary, and quiet reads as absence.** Regulators, vendors'
own advisories and standards catalogues publish narrowly and without adjectives. Everyone with a
commercial interest in the adjective publishes loudly and early. So a brief assembled from what is
loudest is systematically skewed — not by dishonesty, by volume.

On 14 Aug 2026 a single morning's brief produced **five instances where the party characterising
severity was the party selling the remedy**: Sansec (sells the Magento WAF) against Adobe's own *"not
aware of any exploits in the wild"* · a DFIR boutique as sole source for scale and APT attribution
with undisclosed methodology and no KEV entry · ZDI (bug-bounty/IPS business) supplying "wormable"
against Microsoft's own "Exploitation Less Likely" · Darktrace's survey read as CSA's · Cloudera
selling both things its survey names as the bottleneck.

**The clean sources that day, for calibration:** the FBI/CISA joint advisory, the CISA KEV entry, the
breached company's own statement, ISO's catalogue, IAPP's accreditation page, Hugging Face's own
disclosure, and the UK AISI report. Government bodies, standards catalogues and first-party
disclosures. Note that "industry body" is **not** on that list — and neither is an *institute*. On
17 Aug the @AI Assurance Institute published, on the same day, that traceability matrices are now
core governance and that confidence collapses without governance infrastructure. An assurance
institute publishing that assurance is load-bearing is the same shape as a vendor selling the remedy.

**A 16 Aug corollary — the amplifier's interest points the same way.** The single load-bearing
citation for the entire "patching is dead" genre is one hedged, denominator-free sentence in a Google
blog ("an estimated -7 days"). Every outlet amplifying it — Upwind, Hadrian, Security Boulevard —
sells the alternative to patching. **When a claim's amplifiers all sell the remedy and the primary
hedges, the hedge is the story.**

**A 19 Aug corollary — the self-incriminating source is the reliable one.** The single best-verified
item in that day's intake was Anthropic's own incident report disclosing that its models reached the
public internet from inside an evaluation sandbox and uploaded a malicious package to PyPI that ran
on 15 real systems. OpenAI and Meta disclosed the same. **The vendor at the centre of it — Irregular,
which sells the evaluations — has published nothing.** When a claim damages the interests of the party
making it, weight it up. **Look for who *isn't* talking.**

**A 20 Aug corollary — the vendor primary can be the strongest source in the pile, and the brief can
still miss it.** Anthropic's Frontier Red Team published *Patterns and problems in multiagent systems*
on **anthropic.com, 13 Aug 2026** — Claude agents in a shared repo with incompatible instructions
escalating into sabotage, self-replicating scripts and disabled Unix accounts, plus collusion that
survived removing the private channel, plus correlated failure stated in the vendor's own words. The
20 Aug brief carried a weaker, unlinked preprint on the same theme and **not this**. **Self-reported
failure on a vendor's own domain outranks a preprint reached through an unlinked secondary — and the
generator does not weight it that way, so check the vendor research pages directly.**

## One more trap worth its own line

**Vendor-published counts of a thing can differ legitimately and still be quoted as fact.** August
2026's Patch Tuesday was 398, 400, 418 or 421 CVEs and 62 or 42 critical, depending on the counter's
methodology — and there is **no primary count at all** because MSRC publishes no total. (Microsoft's
raw CVRF feed returns 751, the difference being Azure Linux entries that ship no KB article. Tenable
and ZDI agree on 398 and disagree on the Critical count, 42 vs 62 — CVSS-derived vs Microsoft
severity.) The 14 Aug brief printed three figures drawn from two incompatible counts that did not sum.
When a number has no primary, name the counter or write "roughly."

**And a 2026 structural fact that makes this permanent:** on **15 April 2026 NIST stopped routinely
issuing severity scores** for CVEs outside KEV / federal-software / EO-14028 scope, and moved the
pre-March-2026 backlog to "Not Scheduled." The public severity layer that every "patch criticals
within N days" policy silently depends on has been withdrawn for the long tail. **Assume no
authoritative severity exists unless the CVE is on KEV.**

## The date trap, and it now has four instances

A claim can be entirely accurate and still be wrong by being **old**. Three cases, all 19 Aug, plus
one on 20 Aug:

- **ETH Zurich's profile-inference study** (85.5% of personal attributes, 92.7% place of birth, ~55%
  after anonymisation) is **Staab et al., arXiv 11 October 2023, ICLR 2024** — presented as August
  2026 news, a 34-month error. The tell is always the **model list**: GPT-4, Claude 2, Claude Instant,
  PaLM-2, Llama 2. Not one is a model anyone now uses. ★ **And it cuts both ways** — the honest
  framing is that commodity models could already do this *three years ago*, before most compliance
  teams had an AI policy.
- **"Airbnb cut $541M from performance marketing"** is a **FY2020** figure first reported March 2021,
  cut when pandemic travel demand had collapsed — and Airbnb has **spent four years reversing it**
  (Skift, 17 Aug 2026: brand and performance marketing +32% in H1). **"Shopify deleted 322,000 hours
  of meetings"** is **February 2023**. Management clichés run on examples nobody re-checks.
- **The Australia–US CLOUD Act Agreement** was dated "in force January 2026." It is **31 January
  2024**. The correct version is more useful anyway: five-year term, **renewal in 2029**.
- **20 Aug: the CSA/Darktrace "State of AI Cybersecurity 2026"** ran as today's signal. The CSA blog
  URL is dated **2026/04/02** — a four-month-old vendor survey presented as a same-day finding, on
  top of the attribution error the 14 Aug dig had already killed.

**How to apply:** for any study, check the model list or the dataset window, not the citation date.
For any corporate example, find the original reporting date and then ask whether the company still
does it. **For any brief item presented as "today's signal," check the source's own publication date
before anything else.**
