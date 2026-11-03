---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: Fudan measurement study (arXiv 2605.22333) / Censys / Trend Micro / Invariant Labs / Trail of Bits / NSA
url: https://arxiv.org/abs/2605.22333
brief: cyber
threads: [Supply Chain, AI Attack Surface, Trust Boundaries]
beat: Cyber / MCP / Agentic Infrastructure
status: developing
used_in:
---

# MCP servers as supply chain — the numbers are finally in

**What happened.** The community framing in the 7 Aug brief — *"AI agent security in 2026 is a supply
chain problem first, a prompt injection problem second"* — now has empirical backing it lacked six months
ago. The load-bearing citation is a **Fudan University measurement study** (arXiv 2605.22333, submitted
21 May 2026): **7,973 live remote MCP servers identified, 40.55% expose tools without authentication.**
Of **119 testable OAuth-enabled servers, every single one had at least one flaw** — 325 flaws total,
**dynamic client registration flaws in 96.6%**. Nine CVE IDs obtained through disclosure.

**Why it matters.** This is the rare case where the scary framing is *under*-stated. Not "some MCP servers
are misconfigured" — **two in five remote MCP servers on the public internet hand you their tool list with
no authentication at all**, and of the ones that did implement OAuth, none got it right.

## The corroborating scans

- **Censys** (24–28 Apr 2026): **12,520 internet-accessible MCP services, 8,758 unique IPs, 56 countries.**
  1,776 in "Data & Knowledge" including *"direct database query interfaces"*; **687 "System Control" services
  exposing command execution.** Censys: organisations are *"deploying these systems faster than they are
  developing the operational understanding and security controls needed to secure them safely."*
- **Trend Micro** (28 Apr 2026): **1,467 exposed servers, up from 492 in Jul 2025** — a 3x rise in nine
  months; 1,227 still legacy SSE.
- **Knostic** (17 Jul 2025): of 119 manually verified servers, **all 119** granted access to internal tool
  listings without authentication.
- **Trend Micro code sweep** (28 May 2026), 19,000+ repos / 566,845 files: **~4% of MCP server repos contain
  exploitable vulnerabilities** (range 3.1–8.6%). Of 93 confirmed cases: **SQLi 26%, RCE 22.5%, path traversal
  19%, auth bypass 7.5%.** And the detail worth a paragraph: **42.6% of the confirmed-vulnerable repos show
  signs of AI code generation.**

## The attack classes and who named them first

| Class | First documented | Date |
|---|---|---|
| Command injection / path traversal / SSRF in server code | Equixly | 29 Mar 2025 |
| Tool poisoning, rug-pull description mutation, cross-server shadowing | Invariant Labs | 1 Apr 2025 |
| "Line jumping" — attack lands before any tool is invoked | Trail of Bits | 21 Apr 2025 |
| Plaintext credential storage across MCP tooling | Trail of Bits | 30 Apr 2025 |
| Lethal trifecta (private data + untrusted content + external comms) | Simon Willison | 16 Jun 2025 |
| Confused deputy, token passthrough, session hijack | MCP spec itself | Jun 2025 → 2025-11-25 |

Best lines: Trail of Bits — **"This effectively transforms the 'human-in-the-loop' security model into
'human-as-the-rubber-stamp'."** That is [[Anthropic Deputy CISO field guide to governing agentic AI]]'s
blast-radius question with the answer already given. Equixly — *"MCP servers can be called by anyone, not
just LLMs."* MCP spec, normative: *"MCP servers MUST NOT accept any tokens that were not explicitly issued
for the MCP server"* and *"MCP Servers MUST NOT use sessions for authentication."*

## Incidents and CVEs worth having on file

- **CVE-2025-49596** — Anthropic MCP Inspector, **9.4**, CSRF from any web page → MCP commands over stdio. Fixed 0.14.1.
- **CVE-2025-6514** — `mcp-remote`, **9.6**, OS command injection via crafted `authorization_endpoint`. **437,000+ downloads** at disclosure.
- **CVE-2025-54136 "MCPoison"** — Cursor. Check Point: *"Once a MCP is approved, Cursor never checks it again, even if the commands inside it are silently changed later."* The rug-pull class, weaponised.
- **CVE-2026-47751** — `anthropics/claude-code-action`, attacker-controlled checkout + default project settings = an attacker-supplied **`.mcp.json`** executing with all workflow secrets.
- **postmark-mcp** (v1.0.16, 17 Sep 2025) — first confirmed malicious MCP server in the wild, BCC'd every outbound email. **1,643 downloads.**
- **Asana MCP** — logic flaw, not intrusion; ~**1,000 customers'** task data, comments, files and chatbot queries cross-exposed for six weeks.
- **Ruflo CVE-2026-59726 ("RufRoot")** — **CVSS 10.0**, Noma Labs, 29 Jul 2026: unauthenticated POST to the MCP Bridge on **port 3001** = container command execution, **233 tools exposed over HTTP with no auth**. Quotable: *"No token, no API key, no header check, no IP allowlist. Nothing."* **Note: Noma demonstrates a PoC against test deployments and does NOT claim in-the-wild exploitation** — SecurityWeek's "exploited to spawn rogue AI swarms" runs ahead of the primary. The 7 Aug brief inherited that framing.

## The governance answer is arriving — and the SBOM update is the AU hook

- **NSA/AISC, 20 May 2026** — first national-security-agency MCP guidance. *"Established cyber defense
  strategies unfortunately do not adequately address these new risks"*; *"adopters are advised to proceed
  with caution."*
- **OWASP MCP Top 10** (Phase 3 beta). Shape of the list is itself evidence: **7 of 10 are access-control,
  supply-chain or config; only 3 are injection.** MCP04 is *Software Supply Chain Attacks*; MCP09 is
  *Shadow MCP Servers*.
- **2026 Minimum Elements for an SBOM**, published **29 July 2026**, CISA/NSA/FBI-led and
  **co-sealed by ASD's ACSC** plus 17 other agencies (the brief's "ACSC joint SBOM update this week" —
  ACSC's own posting landed the first week of August). What changed: **10 new required fields including
  SBOM Author Signature, Component Hash Value and Hash Algorithm**; "Supplier Name" → **"Component Producer"**
  because the old term *"proved ambiguous in practice"*; "Depth" → **"Coverage"** now requiring horizontal
  breadth; SWID tags dropped. **Signatures and hashes — attestation and integrity — are exactly the machinery
  the supply-chain framing needs.** Nothing in it is MCP- or AI-specific.

## The counter-argument, which is stronger than it looks

Every high-impact MCP incident to date ran through **legitimate, first-party, vendor-operated servers** —
GitHub, Supabase, Atlassian, Asana. Nothing was poisoned or typosquatted. The only confirmed malicious MCP
package in the wild had **1,643 downloads**; Asana alone touched **~1,000 organisations**. Perfect
supply-chain hygiene would have prevented **none** of them. Invariant — who *coined* tool poisoning — says
of the GitHub exfiltration: *"this is not a flaw in the GitHub MCP server code itself, but rather a
fundamental architectural issue that must be addressed at the agent system level."* Willison: *"even a
trustworthy WhatsApp MCP server becomes dangerous"* once someone can message you.

**The honest thesis, and it is a better one:** we frame it as supply chain **because that is the part we can
actually govern this quarter**. Prompt injection is unsolved and therefore not actionable; 40.55% of remote
MCP servers exposing tools without authentication is actionable on Monday. And the CVEs bear it out —
CVE-2025-6514, CVE-2025-49596, the 26% SQLi / 22.5% RCE sweep are **ordinary appsec failures with no LLM
anywhere in the exploit path**. Supply chain wins on tractability, not on incident share. Say that out loud
and the piece is stronger than the community framing it started from.

## Observations

- **2026-08-07** — First seen as a Community Pulse item. Turned out to be the best-evidenced signal of the day. The Fudan 40.55% and the Trend Micro "42.6% of vulnerable repos show AI-generation traits" are the two numbers to build on.

## Feeds

- [[Supply Chain]] — the AI-native instance of the thread
- [[AI Attack Surface]] — the exposed-tool inventory is the attack surface
- [[Trust Boundaries]] — "human-as-the-rubber-stamp" is the GhostApproval argument, verbatim, from a security firm
- [[TeamPCP - the security toolchain became the supply chain]] — the Bitwarden payload collected `.claude/mcp.json`
- [[d1g1t wealth management MCP connector]] — a regulated-industry MCP deployment to test all this against

## Open

- **[VERIFY] before use:** "106 zero-days / 67 CVEs from 40,000 repos (VIPER-MCP)" and "30 CVEs in 60 days" are aggregator claims with no reachable primary. Equixly's 43% command-injection figure has **no published denominator** — if it goes in a draft the sentence must say so.
- No credible enterprise-deployment census exists. The honest formulation: internet-exposure counts (12,520) and repo counts (19,000+) are **floors, not populations**.
