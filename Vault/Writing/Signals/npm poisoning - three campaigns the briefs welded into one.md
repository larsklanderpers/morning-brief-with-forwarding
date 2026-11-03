---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: CrowdStrike 2026 Threat Hunting Report / SafeDep / OpenSourceMalware / Socket / Aikido
url: https://www.crowdstrike.com/en-us/press-releases/crowdstrike-2026-threat-hunting-report/
brief: cyber
threads: [Supply Chain, AI Attack Surface]
beat: Cyber / npm / DPRK
status: signal
used_in:
---

# npm poisoning — three campaigns the brief welded into one

**What happened.** The 7 Aug brief reported "DPRK's NullReceiver: 131 AI framework packages poisoned,
353 versions across 79 names, evolved EtherHiding." That single sentence fuses **three unrelated
incidents** that share nothing but a registry. Unpicked, each is better than the composite:

**(a) 131 packages — CrowdStrike, and it is June's story.** Actor is **STARDUST CHOLLIMA**, not Famous
Chollima (that is CrowdStrike's insider-IT-worker cluster). Verbatim: STARDUST CHOLLIMA *"injected a
malicious npm package into 131 trusted Mastra AI frameworks."* That is the **17 June 2026 @mastra scope
takeover**, not an August event. **No mention of NullReceiver, EtherHiding, BeaverTail or InvisibleFerret
appears anywhere in CrowdStrike's release or blog.** SafeDep's independent detail on the same incident is
the good material: **143 @mastra packages** compromised through a **dormant contributor account
(`ehindero`) that held scope access for 16 months without revocation**; stage-2 RAT scans for **166 wallet
extensions**, persists via fake NVM LaunchAgent/systemd units, beacons every 10 minutes. SafeDep's killer
line: *"Mastra ships its real releases from CI through npm's trusted publisher flow, and each one carries
SLSA provenance attestations. The attacker pushed the malicious versions from a personal token and dropped
the provenance."* **Provenance existed; its absence was not enforced.** That is the whole argument.

**(b) NullReceiver — real, tiny, and a technique story.** Research by **OpenSourceMalware (Paul McCarty)**,
published **5 Aug 2026** — not SafeDep, not CrowdStrike. **Seven npm packages**, downloads in the hundreds
to low thousands (tailwindcss-anim 1,357; tailwind-anim 1,301; bianira-ui 109). The evolution: classic
EtherHiding hides payloads in smart contracts on BNB Smart Chain; NullReceiver encodes the **C2 IP in the
recipient address of zero-value Ethereum transfers** — no contract, no on-chain payload, just a lookup.
First transaction 27 Jul, packages published 28 Jul. Quotable: *"NullReceiver never reuses a destination.
Every lookup is a brand-new, throwaway address that's never been seen before."* GBHackers' counterpoint is
better: **the attacker wallet is reused even though the destinations aren't**, so the "unblockable" channel
leaks a persistent trail. DPRK attribution is **REPORTED**, not confirmed.

**(c) 353 versions / 79 names — the keyv worm, 4 Aug, and it is not DPRK.** Self-propagating
**Shai-Hulud-family** worm. Counts diverged fast and by vendor, which is itself the story: SafeDep initial
**353 versions / 79 names**, SafeDep same-day update **1,684 versions / 420 names across nine orgs**;
Aikido **868+ packages / 1,381 versions**; Socket **442 versions / 353 names**. Mechanism: `preinstall`
running `node setup.mjs`, a **727,680-byte compiled Bun bundle**, propagating **between organisations every
2–7 minutes**, cross-org burst complete in **~30 minutes**. Harvests GitHub, npm, cloud, Vault, K8s creds,
private keys, **and GitHub Actions runner memory**.

## The CrowdStrike numbers, corrected and quotable

- **"In 1H 2026, 88% of CrowdStrike-observed exploitation of vulnerabilities with a public PoC was
  conducted within 48 hours."** — use this, it is the primary framing.
- The 24-hour claim is real but **narrower than the brief**: China-nexus **VAULT PANDA** and **GENESIS
  PANDA** *"moved even faster, launching deliberate attacks within 24 hours of disclosure."* Two named
  actors, and **disclosure**, not "public PoC." Do not generalise to "China-nexus actors."
- 87% of identified software-registry threats in 1H 2026 involved npm. **ALTERED SPIDER compromised 300+
  dependencies in a single day.** One LLMJacking campaign sent **~200,000 model requests in two minutes**.
  Device-code phishing **15x** in six months; vishing **2x**. AI-agent-triggered detection leads growing at
  **2.5x** the rate of human-triggered ones.
- Adam Meyers: *"The organizations that succeed will secure AI as aggressively as they adopt it and use AI
  to defend at the speed of the adversary."*
- **The "AI-generated disposable phishing infrastructure" stat does not exist in the report.** No
  domain-churn or infrastructure-lifecycle figure in the release, the blog, or Black Hat coverage.
  **Do not write that claim.**

## Observations

- **2026-08-07** — First seen. The unpicking is worth more than the composite: (a) gives you *provenance
  that existed and wasn't enforced*, (b) gives you *unblockable-by-design C2 that still leaks*, (c) gives you
  *four vendors counting the same worm four different ways within 24 hours*, which is a live argument about
  whether anyone can actually scope a registry incident while it is happening.

## Feeds

- [[Supply Chain]] — three distinct mechanisms, one registry
- [[TeamPCP - the security toolchain became the supply chain]] — Shai-Hulud family link, Bun 1.3.13 overlap
- [[AI Attack Surface]] — AI frameworks as the chosen target; LLMJacking at 200k requests / 2 min

## Open

- Sapphire Sleet / BlueNorbow attribution for the Mastra takeover is explicitly *unconfirmed* by SafeDep ("tradecraft overlap is close"). **[VERIFY]** before naming an actor in a draft.
