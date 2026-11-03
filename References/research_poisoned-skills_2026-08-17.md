# Research note — POISONED / MALICIOUS AGENT SKILLS
**For:** Lars Klander · piece publishing Wed 19 Aug 2026 (`substack_draft_repo-policy_2026-08-19`)
**Compiled:** 17 Aug 2026
**Question on the table:** is "a poisoned entry in a repo's skills directory is a new type of attack, already exploited less than two months ago" true?

---

## BOTTOM LINE

**No, not as written. Three separate faults in one sentence.**

1. **"New type of attack" — false.** Malicious agent skills have been a named, tracked class since at least the first week of February 2026. Snyk named the threat class **ToxicSkills** on 5 Feb 2026. Koi Security named the campaign **ClawHavoc** on 1 Feb 2026. OWASP now carries an **Agentic Skills Top 10** with `AST01 — Malicious Skills` as entry one. Six months of prior art, not a novelty.

2. **"Already exploited" — TRUE, but not about the thing his backlog points at, and not two months ago.** Real attackers really did poison a real skill market and real users really did install the results: **ClawHavoc, 27 Jan – 4 Feb 2026, ClawHub** (OpenClaw's public skill market). Antiy CERT's write-up is explicit that malicious code executed "within users' systems." That is in-the-wild exploitation with victims. It is ~six and a half months before publication, not two. The freshest in-the-wild *disclosure* is **Unit 42, 23 June 2026** — five live attacker-published malicious skills on ClawHub, taken down. 23 Jun is 57 days before 19 Aug, so "disclosed less than two months ago" is survivable; "exploited less than two months ago" is not, because Unit 42 publishes no victim evidence.

3. **The ~26,000 figure is the wrong evidence entirely, and printing it as an attack would be a straight error.** AIR's report is titled, in its own first person, *"The Story of Skills — How We Hijacked 26,000 Agents With One Instagram Ad."* AIR ran the campaign. The payload was benign by design — it emailed back the user's address so AIR could count reach. There was no attacker and there were no victims. The number is AIR's own, uncorroborated, and AIR closes the write-up pitching its own managed skills marketplace. **This is the exact PoC-to-fact drift the corpus keeps getting burned by.** The prior editor-panel round was right to withhold it; this pass confirms it should stay withheld as an attack, and may only be used as a *demonstration*.

**And the scope verdict, which decides the piece's wording:** every documented in-the-wild case is a **public marketplace or registry** — ClawHub, skills.sh, public MCP/skill registries, GitHub campaign repos. **Not one** published in-the-wild case involves a poisoned skills directory inside an organization's own source repository. That shape — scope (b), the piece's actual subject — exists in the literature only as **working proof of concept** (Reversec, Datadog, Mitiga) plus **one real tracked CVE** in the loading mechanism (CVE-2025-59536). So the risk Lars is describing is *adjacent to*, not identical with, the exploited case. The draft's current line — "poisoned agent skills were already circulating months ago" — is accurate and should stay. Do not upgrade it.

**AutoJack should be cut from this piece.** It is not a skills story at all. It is a browsing-agent-reaches-localhost-MCP story in AutoGen Studio, and Microsoft says the chain "doesn't work on current builds" and never shipped in a released package. Including it weakens the paragraph.

---

## ITEM 1 — The fake agent "skill" and the 26,000

**Status: SOLID as a demonstration. The number itself is UNVERIFIED (single-source, self-reported).**

- **Who published:** **AIR** (air.security), an agent-security company. Researchers named in coverage: **Niv Hoffman and Or Nevo**.
- **Primary URL:** `https://www.air.security/blog-posts/the-story-of-skills`
  ⚠️ **I could not read the primary.** This environment's gateway returns a policy denial (403 on CONNECT) for `www.air.security`, and Wayback/reader mirrors are blocked too. Everything below is from the primary's own **verbatim title** (visible in search indexing) plus three independent outlets. Flagged as a gap: if Lars quotes AIR's body text, someone must open the page from a normal browser first.
- **Date:** first coverage **23 June 2026** (The Hacker News; The Next Web; CSO Online). Cybernews **25 June 2026**. OWASP dates the incident "Jun 22–24, 2026."
  🚩 **Date trap:** Lars's backlog files it as a "3 Jul brief" item. The 3 Jul brief is where *his pipeline* saw it. The event is 22–25 June. Do not print 3 July.
- **What happened:** AIR built a skill that claimed to build a landing page using Google's Stitch design tool, got it into a public skill marketplace (a GitHub-based marketplace; The Hacker News describes the target repo as having ~36,000 stars and 156 skills), and drove installs with a single Instagram ad.
- **26,000 of WHAT:** **agents reached by AIR's own campaign** — measured by the benign payload phoning home. Cybernews: *"In the demo, the script simply emailed users' addresses back to AIR so the researchers could measure the campaign's reach, which they claim gave them access to over 26,000 agents."* CSO Online's headline says "26,000 users." So even the unit is inconsistent across outlets — **agents** in most, **users** in CSO, **installs/designers and marketers** in a later CSO piece ("installed by more than 26,000 designers and marketers"). Treat the unit as unsettled.

**Verbatim, printable:**

> "The Story of Skills — How We Hijacked 26,000 Agents With One Instagram Ad"
> — AIR, report title, air.security

> "The payload was harmless by design: it collected the user's email address and did nothing else."
> — The Hacker News, 23 Jun 2026

> "The 26,000 number, the corporate-account detail, and the claim that it could have seized full control of every agent are the company's own and are not independently confirmed."
> — The Hacker News, 23 Jun 2026

> "The scale figures come from AIR alone and deserve a sceptical read."
> — Ana Maria Constantin, The Next Web, 23 Jun 2026

> "Current security scanners practically scan only a portion of the skill's content, rendering the scan's result irrelevant by design."
> — AIR researchers, quoted in Cybernews, 25 Jun 2026

**COMMERCIAL INTEREST — name it.** AIR sells agent security. The Next Web notes AIR "closes its write-up pitching" its own managed skills marketplace. The finding and the product are the same document.

**Modal check.** AIR's operative claim about harm is conditional: it *"could have used the same foothold to read files, move data, or hit internal systems."* Could. Did not. Any sentence that turns that into "did" is the overclaim.

---

## ITEM 2 — AutoJack

**Status: SOLID, and solidly a proof of concept. Not a skills story. Recommend cutting from this piece.**

- **Who published:** **Microsoft** — Microsoft Defender Security Research Team, on the Microsoft Security Blog. (The corpus's brief credits "The Hacker News," which is the republisher, not the publisher.)
- **Primary URL:** `https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/`
- **Date: 18 June 2026.** The Hacker News secondary is 19 Jun 2026. 🚩 Use 18 Jun.
- **What it is:** a three-link chain in **AutoGen Studio** (Microsoft Research's open-source prototyping UI): an origin-allowlist bypass via the local browsing agent, auth middleware that exempts MCP paths, and unsafe parameter handling. Net effect: untrusted web content rendered by a browsing agent reaches a local MCP WebSocket and spawns processes on the host.
- **Why it does not belong in a poisoned-skills piece:** no skill, no SKILL.md, no repository instruction file. The attacker-controlled artefact is a *web page*, and the vulnerable surface is *localhost*.

**Verbatim:**

> "untrusted web content rendered by a browsing agent to reach a local Model Context Protocol (MCP) WebSocket and spawn arbitrary processes on the host."
> — Microsoft Security Blog, 18 Jun 2026

> "The explanation below is for demonstrative purposes only. The exploit chain doesn't work on current builds."
> — Microsoft Security Blog, 18 Jun 2026

> "The affected MCP WebSocket surface was never included in a Python Package Index (PyPI) release."
> — Microsoft Security Blog, 18 Jun 2026

Only developers building from the GitHub main branch between the MCP plugin landing and hardening commit `b047730` were ever exposed. Published version 0.4.2.2 does not contain the vulnerable code. No CVE found. No exposure scan, no victim count, no in-the-wild observation.

⚠️ **Vendor-headline drift to avoid:** TechRadar ran this as *"Microsoft warns AI agents are being 'AutoJack'-ed to deliver RCE payloads."* **"Are being"** is not in Microsoft's post. That is a modal-verb drop introduced by a downstream outlet. Do not inherit it.

---

## ITEM 3 ★ — MODAL VERDICT: exploited, or demonstrated?

| # | Case | Who published (primary) | Date | Verdict |
|---|---|---|---|---|
| 1 | **ClawHavoc** — coordinated poisoning of ClawHub | **Koi Security** (discovery, 1 Feb 2026); **Antiy CERT** (analysis, 6 Feb 2026) | Campaign **27 Jan – 4 Feb 2026** | **EXPLOITED IN THE WILD. Real attackers, real installs, code executed on users' machines.** |
| 2 | **Five live malicious ClawHub skills** | **Palo Alto Networks Unit 42** | **23 Jun 2026** (analysis Feb–May 2026) | **IN THE WILD** — attacker-published, live, real infostealer payloads, taken down. **No victim count published.** |
| 3 | **AgentBaiting** — 800+ fake Skill/MCP repos | **Island** (Oleg Zaytsev) | **20 Jul 2026** | **MIXED.** The malware campaign infrastructure is real and live. The *agent-discovers-and-installs-it* path is researcher-demonstrated. |
| 4 | **ToxicSkills** measurement study | **Snyk** (Beurer-Kellner, Kudrinskii, Milanta, Nielsen, Sarkar, Tal) | **5 Feb 2026** | **SCAN, not victims.** Static/LLM analysis of published skills. |
| 5 | **AIR "26,000 agents"** | **AIR** | **23 Jun 2026** | **DEMONSTRATION. AIR's own campaign, benign payload, no attacker, no victims.** |
| 6 | **AutoJack** | **Microsoft** | **18 Jun 2026** | **PROOF OF CONCEPT, and dead on current builds.** |
| 7 | **Skill Issues** pts 1–2 — malicious `.claude/skills` + `.claude/agents` | **Reversec** (James Henderson) | **5 May** and **24 Jun 2026** | **PROOF OF CONCEPT.** |
| 8 | **Poisoned take-home coding test** | **Mitiga** (Ucha Gobejishvili) | **19 Jun 2026** (upd. 16 Jul) | **RESEARCHER-CONSTRUCTED.** |
| 9 | **PromptLogger** — prompt exfil via `CLAUDE.md`/`.cursorrules` | **Mitiga** | **Aug 2026** | **CONTESTED — see below.** |
| 10 | **Dynamic context commands in skills** | **Datadog Security Labs** (Nick Frichette, Ryan Simon) | **11 May 2026** | **PROOF OF CONCEPT** (see caveat). |
| 11 | **CVE-2025-59536** — Claude Code executed project code pre-trust-dialog | **NVD / Anthropic** | **3 Oct 2025** | **REAL TRACKED VULNERABILITY.** No public in-the-wild exploitation found. |

### The one that carries "exploited"

**ClawHavoc.** This is the only case with an unambiguous victim statement from a primary.

> "Using 'ClickFix'-style social engineering techniques, they tricked users into downloading and installing these malicious Skills, thereby implanting and executing malicious code within users' systems."
> — Antiy CERT, 6 Feb 2026

> "At least 1,184 malicious Skills have historically appeared on ClawHub."
> — Antiy CERT, 6 Feb 2026

> "We audited all 2,632 skills on ClawHub and found 341 were malicious — 335 from a single campaign."
> — Alex and Oren Yomtov, Koi Security, 1 Feb 2026

> "Our findings have more than doubled — from 341 to 824 malicious skills."
> — Koi Security, update dated 16 Feb 2026

⚠️ **The counts do not agree and are counting different things.** Koi: 341 → 824 malicious skills *found in an audit of 2,632*. Antiy: 1,184 *historically appeared*, one actor (`hightower6eu`) responsible for 677. OWASP restates it as "1,184 malicious skills across 12 publisher accounts." **If Lars prints a number, print Koi's audited denominator — "341 of 2,632 skills on ClawHub" — because it is the only figure with a denominator attached.**

⚠️ **Download counts are not victim counts.** Antiy's most concrete figure is *"These 60 packages have accumulated 14,285 downloads"* — 60 packages, not all of them, and downloads, not confirmed compromises. Island's *"more than 14 million measured downloads"* across ~200 campaign repos is a **reachability** figure for a broader GitHub malware campaign, not agent victims. Do not convert either into people harmed.

**COMMERCIAL INTEREST — name it.** Koi Security sells exactly this: "Koi gives security teams visibility and control over employee-installed software across marketplaces, including AI skills, browser extensions, developer plugins," and ships a protective skill called Clawdex. Antiy is an anti-virus vendor. Snyk sells AppSec. Island sells an enterprise browser. Mitiga sells cloud detection and response and ships a free scanner, **Skillgate**, aimed at exactly these files. CybeDefend sells VibeDefend. **Every single source in this dossier has a product in the blast radius.** Unit 42 (Palo Alto) is the closest thing to a disinterested technical primary here, and it is still a vendor research arm.

### CONTESTED: Mitiga's "PromptLogger"

This is the freshest item and the only one anyone describes as active, so it needs care. The Hacker News's 6 Aug 2026 ThreatsDay round-up lists it under **"Active threat (in the wild)."** CSO Online (Lucian Constantin, 4 Aug 2026) reports that Mitiga researchers *"found and reported multiple examples of agent instruction file poisoning on GitHub repositories."* But **I could not locate Mitiga's dedicated PromptLogger report**, and Mitiga's own published research blog (15 Jun 2026, updated 16 Jul) says only:

> "We are holding the full breakdown — tradecraft, infrastructure, and attribution — for a dedicated report landing shortly."

and, separately,

> "prompt-exfiltration tradecraft caught in the wild"

— while naming no file, no repository and no operator. **Verdict: CONTESTED.** There is a real claim of in-the-wild instruction-file poisoning on public GitHub, sourced to Mitiga, relayed by two credible outlets, with the underlying report not publicly locatable as of 17 Aug 2026. **Lars should not build a load-bearing sentence on it.** If he wants it, the safe form is attributive: "Mitiga says it has caught this in the wild; the detailed report has not been published."

---

## ITEM 4 ★ — SCOPE VERDICT: marketplace, or own repo?

**Plainly: every documented in-the-wild case is (a), a public marketplace or registry. The piece is about (b), and (b) is so far only demonstrated.**

**(a) Public marketplace / registry — where the real attacks happened:**
- **ClawHub** (OpenClaw's public skill market) — ClawHavoc; Unit 42's five live skills; Bitdefender Labs' early-Feb finding that ~17% of analysed skills carried malicious payloads (per Dark Reading, 24 Jun 2026).
- **skills.sh** — covered by Snyk's ToxicSkills audit.
- **Public MCP and Skill registries** — LobeHub, Glama, MCP.so, MCP Market — Island's AgentBaiting: *"more than 600 campaign listings across public MCP and Skill registries."*
- **A GitHub-based skills marketplace** — AIR's demonstration.

OWASP's own AST01 write-up confirms the asymmetry: it discusses public marketplaces as the primary distribution vector and contains **no** treatment of skills held inside a project's own repository.

**(b) Skills directory inside an organization's own source repository — the piece's subject. All research, no incidents:**
- **Reversec, 5 May + 24 Jun 2026** — the closest match to Lars's threat model, and explicitly a PoC. Threat model: *"a developer accidentally downloads a repository containing malicious skills or agents, and installs them within a Claude Code project."* Targets `.claude/skills` and `.claude/agents`. Demonstrated exfiltration of SSH keys and AWS credentials, and a subtle backdoor in Entra ID token validation. The author's own characterisation: *"Yes. This was an exercise in finding the limits of their potential for abuse and conjecturing scenarios."*
- **Mitiga, 19 Jun 2026** — poisoned repo containing `.cursor/rules`, `CLAUDE.md`, hidden HTML comments in `README.md`, and `.cursor/mcp.json`; the agent read config, ran `cat ~/.aws/credentials`, pulled kubeconfig, enumerated Terraform state and exfiltrated **in 1 minute 51 seconds** (14:02:11 → 14:04:02). Constructed, not a real breach: *"we do not attribute this specific incident to any known threat actor."*
- **Datadog Security Labs, 11 May 2026** — the mechanism finding that most directly supports Lars's "loaded as executable instruction" line.
- **CVE-2025-59536** — the one hard artefact on the (b) side: Claude Code before 1.0.111 *"could be tricked to execute code contained in a project before the user accepted the startup trust dialog."* CVSS 8.7 (v4.0) / 8.8 (v3.1), published 3 Oct 2025. A repository could get code running before the human said yes. Patched.

**What this means for the wording.** Lars's structural claim — a directory in the repo is loaded as executable instruction at session start, on a schedule he does not control — is **well supported**, and Datadog sharpens it further: some of it runs *before the model even sees it*, which means model-level injection defences never engage. What is **not** supported is that anyone has been attacked this way in public. He should carry the marketplace cases as the proof that the payload class is real and the repo cases as the proof that the loading path is real, and keep those two things visibly separate.

**Verbatim for the mechanism paragraph:**

> "Dynamic context commands run before the model sees the skill at all. When that happens, model-level prompt injection defenses never get a chance to intervene."
> — Datadog Security Labs, quoted in The Hacker News ThreatsDay, 6 Aug 2026

> "AGENTS.md and CLAUDE.md load with near system-prompt authority" … "these files are loaded at session startup and treated with a level of trust that approximates system-prompt authority"
> — CybeDefend, Aug 2026 (vendor; sells VibeDefend)

> "The attack surface is not a code path — it is a document that agents are designed to trust and follow."
> — Cloud Security Alliance AI Safety Initiative, 6 May 2026

> "There's no malware in any of this and nothing to detect on the endpoint. The agent already has the access, the context, and the network reach. The instruction file just tells it what to collect and where to send it."
> — Mitiga, quoted in The Hacker News ThreatsDay, 6 Aug 2026

⚠️ **Caveat on Datadog.** I verified the title (*"Malicious Coding Agent Skills and the Risk of Dynamic Context"*), date (11 May 2026), authors (Nick Frichette, Ryan Simon) and the page's own meta description (*"Learn how malicious Claude Code skills can abuse dynamic context commands to execute before model-level prompt injection defenses can intervene"*), but the article body would not render through this environment's fetcher. The quote above is The Hacker News quoting Datadog, i.e. a secondary quoting a named primary. Good enough to print with attribution to Datadog; someone should still open the original.

---

## ITEM 5 — Is there a named class? Who is tracking it?

**Yes, and the problem is that there are too many names, all from vendors, all from 2026.** Nobody owns the term.

| Name | Coined by | Date |
|---|---|---|
| **ClawHavoc** (campaign name) | Koi Security | 1 Feb 2026 |
| **ToxicSkills** (threat class) | Snyk Research | 5 Feb 2026 |
| **"Skill poisoning"** (generic) | earliest instance found: Simon Roses Femerling, personal blog, *"AI Agent Skill Poisoning: The Supply Chain Attack You Haven't Heard Of"* | Feb 2026 |
| **Agent Context Poisoning** | Cloud Security Alliance AI Safety Initiative | 6 May 2026 |
| **AgentBaiting** | Island (Oleg Zaytsev) | 20 Jul 2026 |
| **Instruction File Injection** | CybeDefend | Aug 2026 |
| **PromptLogger** | Mitiga | Aug 2026 |

**Formal tracking:**
- **OWASP Agentic Skills Top 10** — exists, project lead **Ken Huang**, co-leads Hammad Atta, Fabio Cerullo, Aonan Guan, Bhavya Gupta, Niv Hoffman, Iftach Orr, Akram Sheriff. Entries: `AST01 Malicious Skills`, `AST02 Supply Chain Compromise`, `AST03 Over-Privileged Skills`, `AST04 Insecure Metadata`, `AST05 Untrusted External Instructions`, `AST06 Weak Isolation`, `AST07 Update Drift`, `AST08 Poor Scanning`, `AST09 No Governance`, `AST10 Cross-Platform Reuse`. AST01 maps to OWASP LLM03 (Supply Chain), LLM01 (indirect Prompt Injection) and ASVS V14.
  🚩 **The page's own metadata is self-contradictory: it says "Last updated: March 2026" while citing incidents from June 2026.** Do not cite the OWASP page for any date. Use it only for the existence of the taxonomy and the entry titles. Note also that **Niv Hoffman appears both as an AIR researcher on the 26,000 demonstration and as an OWASP co-lead** — the taxonomy and the vendor research are not fully independent of each other.
- **No dedicated MITRE ATLAS technique found** for malicious agent skills. OWASP's AST01 lists **no** ATLAS technique IDs and **no** CVE/CWE mappings.
- **No CVE or CWE for the class.** CVE-2025-59536 is a specific Claude Code defect, not a class identifier.
- There is a community rule set at `agentthreatrule.org` carrying **ATR-2026-00122 "Weaponized Skill — Agent as Attack Tool."** I found it in search listings only and did not verify the body. **UNVERIFIED — do not cite.**
- **Academic literature exists** (arXiv: *Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems*, 2604.03081; *BadSkill*, 2604.09378; *Poise*, 2606.07943; *SkillJect*, 2602.14211; *Formal Analysis and Supply Chain Security for Agentic AI Skills*, 2603.00195). Plus a **USENIX Security 2026 measurement study** cited by OWASP as analysing 98,380 skills and confirming 157 malicious. **UNVERIFIED against the papers themselves** — I did not open them. Their existence is the point: this is not a new class if it already has a conference paper trail.

---

## ITEM 6 — Anything more recent than early July, through 17 Aug 2026?

**Yes, three things, and the most on-point one is contested.**

1. **Island, "AgentBaiting," 20 Jul 2026.** Over **800** malicious GitHub repositories posing as AI Skills or MCP servers, inside a wider set of ~**7,600** malicious repos, plus **600+** listings across public MCP and Skill registries, delivering **SmartLoader → StealC**. The novel mechanic: *"An AI agent searching for a new capability such as a Skill or an MCP server can discover a campaign repository on its own, treat the attacker's README as legitimate documentation, and hand the installation instructions to the user."* Modal: **can**. Island tested the path themselves — *"To test this path, we gave Claude Code a simple prompt."* So: **real malware campaign, demonstrated agent-mediated delivery path, no confirmed agent victims.** Scope (a).

2. **Mitiga "PromptLogger," early Aug 2026** — CSO Online 4 Aug, The Hacker News 6 Aug. **The single most relevant item to Lars's piece**, because it is repository-resident instruction files (`CLAUDE.md`, `.cursorrules`) rather than a marketplace, and because it is the only Aug 2026 claim of in-the-wild activity in scope (b). **But the underlying report is not publicly locatable.** See CONTESTED above.

3. **Mitiga instruction-file scan, 15 Jun 2026 (updated 16 Jul).** **50,000+ instruction files across 7,000+ distinct public repositories**, April–June 2026, covering skills, Claude hooks, `AGENTS.md`/`CLAUDE.md`, MCP configs, `.cursorrules`, `package.json`, `.pyc`. Found **1,230+ hardcoded API keys and JWT tokens**, plus attacker-controlled `ANTHROPIC_BASE_URL` overrides routing traffic through MITM proxies. ⚠️ **This is a scan of what is sitting in public repos. It measures presence, not exploitation.** The 1,230 keys are a hygiene finding, not victims.

Also in window, adjacent rather than on-subject: **GitLost** (Jul 2026) — a public GitHub issue tricking GitHub's agentic workflows into leaking private repo data; and CSO's 5 Aug round-up noting Claude publishing a malicious Python package to public PyPI *"which was downloaded and executed by 15 real systems"* — a real, tiny, verified victim count worth knowing about but from a different story.

**Nothing found dated 7–17 Aug 2026** on poisoned agent skills. The trail goes quiet after the 6 Aug ThreatsDay.

---

## ITEM 7 ★ — The sentence

### The defensible version (recommended)

> Poisoned agent skills are not a thought experiment. In late January attackers uploaded hundreds of malicious skills to ClawHub, OpenClaw's public skill market — Koi Security audited all 2,632 listings and found 341 of them hostile — and users were socially engineered into installing them, at which point the code ran on their machines. What nobody has published yet is the version I am describing here: a poisoned skill sitting in a company's own repository, loaded automatically because it is simply there. That one exists so far only as a working proof of concept, and the security researchers who built it did not have to work very hard.

Every clause in that is carried by a primary. It gives him the real exploitation, in the right scope, with the right date, and then draws the line to his own argument without stepping over it — and the last clause is the interesting part, because it is true.

### A one-line version, if the paragraph is too long

> Malicious agent skills have been exploited in the wild since January, but only through public marketplaces; the repository-resident version is so far a proof of concept, not an incident.

### The tighter, riskier-but-still-fair option, if he wants recency

> As recently as June, Palo Alto's Unit 42 was pulling live malicious skills — macOS infostealers among them — off a public skill marketplace and getting the publisher accounts banned.

Defensible. "Live" and "pulling off" are accurate; it stops short of claiming victims, which Unit 42 does not report.

### The overclaim — do not print this

> A poisoned entry in your repository's skills directory is a new type of attack, and it was already exploited less than two months ago against roughly 26,000 agents, including corporate accounts.

Four faults, any one of which a reader with the sources open would catch:
- **"new type"** — named and tracked since the first week of February 2026, with a USENIX paper trail and an OWASP Top 10 entry.
- **"exploited"** applied to the 26,000 — AIR ran that campaign against a population it recruited itself, with a payload that collected email addresses. There was no attacker. There were no victims. AIR's own title says *"How We Hijacked."*
- **"less than two months ago"** — the real exploitation is 27 Jan – 4 Feb 2026. Six and a half months.
- **"in your repository's skills directory"** — the 26,000 came through a public marketplace and an Instagram ad. Wrong scope entirely.

And the tell that would embarrass him most: AIR sells a managed skills marketplace, and the 26,000 is the number in its sales pitch.

### Housekeeping for the draft

- Line 110 currently reads *"poisoned agent skills were already circulating months ago."* **Keep it.** It is now primary-verified and correctly hedged. If he wants one specific, the cheapest upgrade is: *"…already circulating months ago — a February audit of one public skill market found 341 of 2,632 listings hostile."*
- The ~26,000 figure stays out of the text as an attack. If he wants it at all, it is a *demonstration*, first-person, with the vendor named.
- **Cut AutoJack.** Wrong mechanism, dead exploit chain, and its presence invites a knowledgeable reader to conclude he is padding.

---

## SOLID / CONTESTED / UNVERIFIED

**SOLID (primary-sourced, quotable):**
- ClawHavoc was a real attacker campaign on ClawHub, 27 Jan – 4 Feb 2026, with malicious code executing on users' systems. Koi Security 1 Feb 2026; Antiy CERT 6 Feb 2026.
- Koi Security audited 2,632 ClawHub skills and found 341 malicious, 335 from one campaign; revised to 824 by 16 Feb 2026.
- Unit 42 found five live attacker-published malicious skills on ClawHub; disclosed 23 Jun 2026; all five removed and accounts banned.
- Snyk's ToxicSkills audit, 5 Feb 2026: 3,984 skills scanned, 1,467 (36.82%) with at least one issue, 13.4% critical, 76 malicious payloads confirmed by manual review.
- AIR's 26,000 exercise was AIR's own campaign with a benign payload. Its own title is first-person.
- AutoJack is Microsoft's, dated 18 Jun 2026, affects AutoGen Studio only, and does not work on current builds.
- Reversec demonstrated credential theft and code backdooring via `.claude/skills` and `.claude/agents` in a cloned repo. 5 May and 24 Jun 2026. Self-described as an exercise.
- CVE-2025-59536: Claude Code before 1.0.111 could execute project code before the trust dialog was accepted. CVSS 8.7/8.8, published 3 Oct 2025.
- OWASP Agentic Skills Top 10 exists, with AST01 Malicious Skills as entry one.
- Island's AgentBaiting: 800+ fake Skill/MCP repos, 600+ public registry listings, SmartLoader→StealC. 20 Jul 2026.

**CONTESTED:**
- **Whether in-the-wild instruction-file poisoning has been observed in public repositories.** Mitiga says yes; The Hacker News lists PromptLogger as an active threat; the detailed report is not publicly locatable as of 17 Aug 2026, and Mitiga's own blog explicitly withheld tradecraft, infrastructure and attribution.
- **The ClawHavoc count.** 341 vs 824 vs 1,184 vs "341 malicious skills" vs "1,184 across 12 publisher accounts." Different denominators, different windows, different definitions.
- **What "26,000" is a count of.** Agents (most outlets), users (CSO headline), "designers and marketers" (CSO, 4 Aug). Unsettled.
- **Whether the AIR skill's reach included corporate accounts.** AIR's claim, explicitly not independently confirmed.

**UNVERIFIED (do not print):**
- **AIR's primary text.** Gateway-blocked from this environment. Title verified via search indexing; body not read. Anything quoted from AIR's own prose must be re-checked from a normal browser.
- **Datadog's article body.** Title, date, authors and meta description verified; body would not render. The dynamic-context quote is The Hacker News quoting Datadog.
- **Mitiga's PromptLogger report.** Not located.
- **ATR-2026-00122 "Weaponized Skill."** Search listing only.
- **The USENIX Security 2026 study (98,380 skills, 157 malicious)** and the arXiv papers. Cited by OWASP or found in search; not opened.
- **Bitdefender Labs' "~17% of OpenClaw skills carried malicious payloads."** Sourced here only from Dark Reading's summary; Bitdefender's own publication not located.
- **The OWASP page's dates.** Internally contradictory. Use for taxonomy only.

**Aggregator hygiene:** nothing in this note is sourced from rankiteo, techjournal, cryptika, gbhackers or cryptobriefing. Several results surfaced from cybersecuritynews, cyberpress, securityonline, hendryadrian, synapsint, dev.to, ground.news, letsdatascience, dailysecurityreview, aiweekly and mallory.ai — all of them republishers of the primaries above, and **none of them used**.

---

## SOURCES

**Primaries — in-the-wild exploitation**
- Koi Security (Alex; Oren Yomtov), *ClawHavoc: 341 Malicious Clawed Skills Found by the Bot They Were Targeting*, 1 Feb 2026 (updated 16 Feb 2026) — https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting
- Antiy Labs / Antiy CERT, *ClawHavoc: Analysis of Large-Scale Poisoning Campaign Targeting the OpenClaw Skill Market for AI Agents*, 6 Feb 2026 — https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/
- Palo Alto Networks Unit 42 (Shresta Bellary Seetharam, Nabeel Mohamed, Billy Melicher, Oleksii Starov), *OpenClaw's Skill Marketplace and the Emerging AI Supply Chain Threat*, 23 Jun 2026 — https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/
- Island (Oleg Zaytsev), *AgentBaiting: How 800 Fake AI Skills and MCP Servers Delivered Malware at Scale*, 20 Jul 2026 — https://www.island.io/blog/agentbaiting-how-800-fake-ai-skills-and-mcp-servers-delivered-malware

**Primaries — measurement / scanning**
- Snyk (Luca Beurer-Kellner, Aleksei Kudrinskii, Marco Milanta, Kristian Bonde Nielsen, Hemang Sarkar, Liran Tal), *ToxicSkills*, 5 Feb 2026 — https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
- Mitiga Labs (Idan Cohen), *Modern Malware — Spyware Skills, Hijacked Base URLs, and 1,230+ Leaking API Keys in AI Instruction Files*, 15 Jun 2026 (upd. 16 Jul 2026) — https://www.mitiga.io/blog/malware-in-ai-instruction-files-skillgate

**Primaries — demonstrations / proof of concept**
- AIR, *The Story of Skills — How We Hijacked 26,000 Agents With One Instagram Ad*, ~22–23 Jun 2026 — https://www.air.security/blog-posts/the-story-of-skills ⚠️ **body not readable from this environment**
- Microsoft Security Blog (Microsoft Defender Security Research Team), *AutoJack: How a single page can RCE the host running your AI agent*, 18 Jun 2026 — https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/
- Reversec Labs (James Henderson), *Skill Issues: Compromising Claude Code with malicious skills & agents — Part 1*, 5 May 2026 — https://labs.reversec.com/posts/2026/05/skill-issues-compromising-claude-code-with-malicious-skills-agents-part-1
- Reversec Labs (James Henderson), *…Part 2*, 24 Jun 2026 — https://labs.reversec.com/posts/2026/06/skill-issues-compromising-claude-code-with-malicious-skills-agents-part-2
- Mitiga (Ucha Gobejishvili), *How a Poisoned Coding Test Turned an AI Agent Into an Attacker*, 19 Jun 2026 (upd. 16 Jul 2026) — https://www.mitiga.io/blog/poisoned-coding-test-ai-agent-attack
- Mitiga Labs (Idan Cohen, Yael Ben Yair, Asad Saffoury), *AI Agent Supply Chain Risk: Silent Codebase Exfiltration via Skills*, 17 Feb 2026 (upd. 16 Jul 2026) — https://www.mitiga.io/blog/ai-agent-supply-chain-risk-silent-codebase-exfiltration-via-skills
- Datadog Security Labs (Nick Frichette, Ryan Simon), *Malicious Coding Agent Skills and the Risk of Dynamic Context*, 11 May 2026 — https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/ ⚠️ **body not readable from this environment**

**Taxonomy / tracking**
- OWASP Agentic Skills Top 10 (project lead Ken Huang) — https://owasp.org/www-project-agentic-skills-top-10/ and AST01 — https://owasp.org/www-project-agentic-skills-top-10/ast01 🚩 **dates unreliable**
- Cloud Security Alliance AI Safety Initiative, *Agent Context Poisoning: SKILL.md and the New AI Supply Chain Attack Surface*, 6 May 2026 — https://labs.cloudsecurityalliance.org/research/csa-research-note-skill-md-agent-context-poisoning-20260506/
- NVD, CVE-2025-59536 (Claude Code < 1.0.111, code injection via startup trust dialog), published 3 Oct 2025 — https://nvd.nist.gov/vuln/detail/CVE-2025-59536
- CybeDefend, *Instruction File Injection: AGENTS.md and CLAUDE.md*, Aug 2026 — https://www.cybedefend.com/en/blog/instruction-file-injection-agents-md-claude-md
- Simon Roses Femerling, *AI Agent Skill Poisoning: The Supply Chain Attack You Haven't Heard Of*, Feb 2026 — https://simonroses.com/2026/02/ai-agent-skill-poisoning-the-supply-chain-attack-you-havent-heard-of/

**Secondary reporting used for corroboration and for skeptical framing**
- The Hacker News, *Fake AI Agent Skill Passed Security Scans and Reportedly Reached 26,000 Agents*, 23 Jun 2026 — https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html
- Ana Maria Constantin, The Next Web, 23 Jun 2026 — https://thenextweb.com/news/fake-ai-agent-skill-security-scanners-bypassed-26000-agents
- CSO Online, *How a malicious AI agent skill passed security checks and reached 26,000 users*, 23 Jun 2026 — https://www.csoonline.com/article/4188840/how-a-malicious-ai-agent-skill-passed-security-checks-and-reached-26000-users.html
- Ann-Marie Corvin, Cybernews, 25 Jun 2026 — https://cybernews.com/ai-news/fake-ai-skill-hijacks-26000-agents-instagram/
- Elizabeth Montalbano, Dark Reading, *More Malicious OpenClaw Skills Threaten AI Supply Chain*, 24 Jun 2026 — https://www.darkreading.com/cyber-risk/malicious-openclaw-skills-clawhub-threaten-ai-supply-chain
- The Hacker News, *Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users*, Feb 2026 — https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- Lucian Constantin, CSO Online, *Attackers are crafting malicious AI instruction files…*, 4 Aug 2026 — https://www.csoonline.com/article/4204731/attackers-are-crafting-malicious-ai-instruction-files-to-turn-your-agentic-workflows-into-quiet-criminal-helpers.html
- CSO Staff, CSO Online, *AI threat report: Rogue agents, workflow attacks*, 5 Aug 2026 — https://www.csoonline.com/article/4205391/ai-threat-report-rogue-agents-workflow-attacks.html
- The Hacker News, *ThreatsDay: Odysseus RCE, Samsung One-Click Takeover, iCloud Backdoor Fight + 27 More Stories*, 6 Aug 2026 — https://thehackernews.com/2026/08/threatsday-odysseus-rce-samsung-one.html
- ThreatDown (Andrea Bianchini), *Weaponizing autonomy: The rise of malicious AI agent skills*, 3 Apr 2026 — https://www.threatdown.com/blog/weaponizing-autonomy-the-rise-of-malicious-ai-agent-skills/
- TechRadar, *Microsoft warns AI agents are being 'AutoJack'-ed…* — https://www.techradar.com/pro/security/microsoft-warns-ai-agents-are-being-autojack-ed-to-deliver-rce-payloads-by-browsing-untrusted-websites ⚠️ **cited only as an example of modal-verb drift; do not use as a source**

**Lars's own corpus (brief-sourced, now superseded by the above)**
- `Daily Briefs/brief_2026-06-25.md` (the 26,000 item), `Daily Briefs/brief_2026-06-20.md` (AutoJack), `Daily Briefs/brief_2026-07-03.md`, `Substack Drafts/SUBSTACK_IDEAS.md` line 170, `LinkedIn Posts/linkedin_2026-06-25.md`
