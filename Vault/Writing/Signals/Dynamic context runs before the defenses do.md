---
date_first_seen: 2026-08-17
date_updated: 2026-08-17
source: Datadog Security Labs / Koi Security / Antiy CERT / Unit 42 / Reversec / CSA / OWASP / NVD
url: https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/
brief: cyber
threads: [AI Attack Surface, Trust Boundaries, Supply Chain, Practitioner - Coding Ground Truth]
beat: AI / Agentic / Skill poisoning / Prompt injection
status: developing
used_in: substack_draft_repo-policy_2026-08-19 (Wed 19 Aug 2026)
---

# Dynamic context runs before the defenses do — and the defenses never get a turn

**What happened.** Datadog Security Labs (Nick Frichette, Ryan Simon), *Malicious Coding Agent
Skills and the Risk of Dynamic Context*, **11 May 2026**. A malicious coding-agent skill can abuse
**dynamic context commands** to execute **before model-level prompt injection defenses can
intervene**.

**Why it matters, and it is the reason this note exists.** Every prompt-injection defense worth
having is a *refusal*. The model reads hostile content, recognizes it, declines. That entire class of
protection assumes the model gets a turn. **Dynamic context does not give it one.** The command runs
during context assembly, so by the time anything capable of refusing is looking at the session, the
thing it would have refused has already happened. There is no decision to make. There is a result.

That is architecturally different from every injection story in this corpus. GhostJacking poisons what
the agent *reads* and gets a bad tool call out of it — bad, but still downstream of a model deciding
something. This is upstream of the deciding.

**The consequence for the argument, not the attack:** this is the strongest available proof that
model-level safety is the wrong layer, full stop, and therefore the strongest available argument for
the harness — external control that cannot be reasoned with because it is not doing any reasoning.
See [[Trust Boundaries]]. It resolves rather than merely alarms, which is rare in this beat.

## The wording that is safe to print

Datadog's own **title and meta description** carry the substance: *"how malicious Claude Code skills
can abuse dynamic context commands to execute before model-level prompt injection defenses can
intervene."* Title, date and authorship verified.

⚠️ **The circulating sentence — "Dynamic context commands run before the model sees the skill at all.
When that happens, model-level prompt injection defenses never get a chance to intervene" — is
The Hacker News quoting Datadog** (ThreatsDay, 6 Aug 2026), not Datadog's own prose read at source.
The article body would not render through the research environment. **Paraphrase and attribute to
Datadog; do not present that sentence as a quotation until somebody opens the original in a browser.**

⚠️ Datadog's finding is **PROOF OF CONCEPT.** Not an in-the-wild incident.

## The exploitation record, which is real but is a different shape

Kept in this note deliberately, because the two halves are always going to be cited together and
splitting them is how the scope error happens.

- **ClawHavoc, 27 Jan – 4 Feb 2026, ClawHub** (OpenClaw's public skill market). **Real victims.**
  Antiy CERT, 6 Feb 2026: *"Using 'ClickFix'-style social engineering techniques, they tricked users
  into downloading and installing these malicious Skills, thereby implanting and executing malicious
  code within users' systems."*
- **Koi Security, 1 Feb 2026** — the only count with a denominator: *"We audited all 2,632 skills on
  ClawHub and found 341 were malicious — 335 from a single campaign."*
- **Unit 42, disclosed 23 Jun 2026** — five more live malicious ClawHub skills. No victim count
  published.
- **Named class since the first week of Feb 2026.** OWASP Agentic Skills Top 10, **AST01 Malicious
  Skills** (project lead Ken Huang; 🚩 dates on the OWASP pages are unreliable).
- **CSA AI Safety Initiative, 6 May 2026** — *Agent Context Poisoning: SKILL.md and the New AI Supply
  Chain Attack Surface.* Closest thing to a disinterested corroboration in the whole dossier.
- **CVE-2025-59536** — Claude Code < 1.0.111 could be tricked into executing code contained in a
  project *before the user accepted the startup trust dialog.* CVSS 8.7. The one hard artifact in the
  loading mechanism itself.

## ★ THE SCOPE LINE — the single most important thing in this note

**Every documented in-the-wild case is a PUBLIC MARKETPLACE OR REGISTRY.** Somebody browsed, chose,
and installed. ClawHub, skills.sh, public MCP/skill registries, GitHub campaign repos.

**A poisoned skill resident in an organization's OWN repository — loaded automatically because it is
simply there — is PROOF OF CONCEPT ONLY** (Reversec, Datadog, Mitiga). Reversec's James Henderson
describes precisely that threat model and labels it himself: *"Yes. This was an exercise in finding
the limits of their potential for abuse and conjecturing scenarios."*

**So: the payload class is proven by the marketplace cases. The loading path is proven separately.
Nobody has published the two together in the wild.** Carry them as two facts. Any sentence that
merges them is an overclaim, and it is the specific overclaim this beat invites.

## Do not print

- **"~26,000 agents" as an attack.** AIR ran that campaign **itself**, with a benign payload. Its own
  title: *"The Story of Skills — How We Hijacked 26,000 Agents With One Instagram Ad."* AIR sells a
  managed skills marketplace. The Hacker News, 23 Jun 2026: *"The 26,000 number, the corporate-account
  detail, and the claim that it could have seized full control of every agent are the company's own and
  are not independently confirmed."* **DATE TRAP:** filed in `SUBSTACK_IDEAS.md` as the 3 Jul brief;
  the event is **22–25 Jun 2026**.
- **AutoJack.** Dead. Not a skills story — a browsing-agent-to-localhost-MCP chain in AutoGen Studio,
  and Microsoft says it does not work on current builds. Never shipped in a release.
- **Mitiga's PromptLogger (Aug 2026)** as in-the-wild instruction-file poisoning on GitHub. CSO and THN
  characterize it that way; the underlying report is not publicly locatable. Freshest and most
  on-point, therefore most tempting. Do not build on it.
- **"A whole new type of attack."** Named and tracked since February.

## ★ Unspent, and it is a piece of its own

**Every source in this space has a product in the blast radius** — Koi, Antiy, Snyk, Island, Mitiga,
CybeDefend, AIR. Unit 42 is closest to disinterested and is still a vendor arm. And **Niv Hoffman is
both an AIR researcher on the 26,000 demonstration and an OWASP Agentic Skills co-lead** — so the
taxonomy and the vendor research behind it are not independent of each other.

That is the same pattern as [[CLOUD Act Australia - the exposure predates the agreement]], where every
appearance of a legal claim traced to a company selling the remedy. **The market is generating its own
facts, and now also its own standards body.** Strong candidate for a standalone piece; do not spend it
as a clause.

## Observations

- **2026-08-17** — First flagged by Lars on reading the Datadog ordering finding in the Wed 19 draft
  ("holy shit that's dangerous"). The mechanism, not the marketplace record, is what made him stop.
  Full research dossier: `References\research_poisoned-skills_2026-08-17.md` (17 Aug, 68 tool calls,
  primaries reached except two noted below).
- ⚠️ **Two primaries were gateway-blocked** from the research environment and remain unread at source:
  **Datadog's article body** and **AIR's own prose**. Titles, dates, authors and meta descriptions
  verified. Anything quoted from either must be re-checked from a normal browser.

## Feeds

- [[AI Attack Surface]] — upstream of the model's decision, which is a new position on this thread
- [[Trust Boundaries]] — the strongest argument yet that model-level defense is the wrong layer
- [[Supply Chain]] — the marketplace half; first real beat on this thread since Cordyceps
- [[Practitioner - Coding Ground Truth]] — it lands in the repo, on his own turf
- [[Ghostjacking - the reviewer never sees that manipulation happened]] — adjacent but downstream:
  that one poisons what the agent reads, this one runs before anything reads
- [[CLOUD Act Australia - the exposure predates the agreement]] — same vendor-generating-its-own-facts
  pattern

## Open

- **Does dynamic context execute in the repo-mounted skills path**, specifically — the `.claude/skills`
  discovery-at-session-start route — or only on installed/marketplace skills? The piece assumes the
  mechanism is general. **Nobody has published on that exact combination**, which is precisely why it
  is the interesting question. Needs the Datadog body read at minimum, and probably a test.
- Is there an in-the-wild case of repo-resident skill poisoning that simply has not been written up?
  Standing watch item.
- CybeDefend, *Instruction File Injection: AGENTS.md and CLAUDE.md*, Aug 2026 — most on-point source
  found and a vendor selling the remedy. Usable only with the commercial interest named.
