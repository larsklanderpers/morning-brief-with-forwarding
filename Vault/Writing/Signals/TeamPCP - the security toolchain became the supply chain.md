---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: Microsoft Security / JFrog / SafeDep / Trend Micro / Palo Alto
url: https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/
brief: cyber
threads: [Supply Chain, AI Attack Surface, Machine Identity]
beat: Cyber / Supply Chain / Developer Tooling
status: signal
used_in:
---

# TeamPCP — when the vulnerability scanner is the vulnerability

**What happened.** One campaign, self-named **TeamPCP**, walked through the security and developer
toolchain over five weeks:

- **Trivy (Aqua Security) — 19 Mar 2026.** Compromised maintainer credentials with **tag write access**,
  used to **force-push malicious commits onto existing version tags** in `trivy-action` and `setup-trivy`
  — so teams pinned by tag, the recommended hygiene, pulled the malware. Malicious: **v0.69.4**.
  Harvested AWS IAM creds, GCP service-account keys, Azure env vars, GitHub and npm tokens, K8s secrets,
  SSH keys, DB strings.
- **Checkmarx KICS + LiteLLM — 23–24 Mar 2026.** LiteLLM was compromised **using credentials stolen in
  the Trivy incident** (JFrog).
- **Bitwarden CLI — 22 Apr 2026.** `@bitwarden/cli@2026.4.0`, malicious window **21:18–21:22:59 UTC —
  about four minutes.** Vector was a poisoned GitHub Actions workflow (`publish-cli.yml`) that swapped
  the package and exfiltrated the npm publish token. Payload stole GitHub/npm/SSH/cloud creds, `.env`,
  shell history — **and AI tool configs: `.claude.json`, `.claude/mcp.json`, `.kiro/settings/mcp.json`.**
- Later spread to Docker Hub, the VS Code marketplace and PyPI.

**Why it matters.** Microsoft's sentence is the piece: *"Threat actors leveraged access from a prior
incident that was not fully remediated to inject credential-stealing malware into official releases."*
Incomplete remediation is the connective tissue — same failure mode as the N-central incomplete patch,
one layer up. And the Bitwarden payload going after **MCP config files** is the first clean evidence
that agent configuration is now a named collection target, not a theoretical one. That links this
directly to [[MCP servers as supply chain - the numbers are in]].

## Verified 2026-08-07 — the brief's downstream victims are wrong

**"OpenAI and Vercel identified as downstream victims" does not survive checking. Do not reuse it.**

- **Vercel is a separate incident.** Disclosed 19 Apr 2026, began ~Feb 2026. Vector was a compromised
  **OAuth application at Context.ai**, a third-party analytics vendor infected with **Lumma Stealer**,
  whose token reached a Vercel employee's Google Workspace and thence customer environment variables.
  No npm package, no GitHub Action, no TeamPCP.
- **OpenAI is not a victim at all.** The only trace: a Vercel customer received an **OpenAI leaked-API-key
  notification on 10 Apr 2026**, nine days before Vercel disclosed. OpenAI is the *detector*, not the breached.
- **Shai-Hulud lineage is a researcher inference, not attribution.** Aikido and Lyrie link TeamPCP to the
  Shai-Hulud family on shared Claude Code / VS Code hooks and identical **Bun 1.3.13** download patterns —
  the same Bun version in the Bitwarden payload. Strong technical thread; still inference. **[VERIFY] open.**

## Observations

- **2026-08-07** — First seen via the 7 Aug cyber brief, which grouped the three vendors correctly and attached the wrong victims. The four-minute Bitwarden window is the number that will land with a technical reader: your entire detection budget for that class of event is 240 seconds.

## Feeds

- [[Supply Chain]] — the strongest single example in the thread
- [[MCP servers as supply chain - the numbers are in]] — the payload went looking for `mcp.json`
- [[Machine Identity]] — every stage turned on a token or a maintainer credential, never a person

## Open

- The pinned-by-tag detail deserves its own argument: the advice everyone gives (pin your actions) failed because tags are mutable. Pin by SHA is the actual control, and almost nobody does it.
