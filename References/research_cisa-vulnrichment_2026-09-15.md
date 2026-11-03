# Research Note — CISA Vulnrichment
For: no draft yet (explainer ask) · Depth: deep dig (explainer level) · Date: 2026-09-15

## Bottom line
Vulnrichment is CISA filling in the blanks on other people's CVE records. A CVE record arrives from the vendor or researcher who filed it (the CNA), often missing a severity score, a weakness type, or any signal about whether it matters. Since May 2024 CISA has added that missing context in a separate, clearly labelled section of the official CVE record (the "CISA ADP" container), never overwriting the filer's data. The main thing it adds is three SSVC questions: is it being exploited, can the attack be automated, and how much control does the attacker get. Trust level: the mechanics are solid (primary source: CISA's own repo); current scale and coverage in 2026 I could not stand up.

## The analogy
The CVE record is a police report filed by whoever found the problem. Some filers write a thorough report; many write two lines. NIST's NVD used to be the detective who read every report and added the analysis. When NVD fell behind, CISA started attaching its own signed addendum to the reports — not rewriting them, just stapling a page to the back that says "being exploited: yes/no; automatable: yes/no; impact: partial/total."

## What's solid
- **What it is.** "The CISA Vulnrichment project is the public repository of CISA's enrichment of public CVE records through CISA's ADP (Authorized Data Publisher) container." — [cisagov/vulnrichment README](https://github.com/cisagov/vulnrichment)
- **It never overwrites the filer.** "At no point will CISA overwrite the originating CNA's data in the original CNA container in the CVE record." If the CNA later supplies its own CVSS/CWE, CISA removes its version. — [README](https://github.com/cisagov/vulnrichment)
- **What gets added, per analyzed CVE:**
  - SSVC decision points: *Exploitation* (none / PoC / active), *Automatable* (yes / no), *Technical Impact* (partial / total). — [README](https://github.com/cisagov/vulnrichment)
  - CVSS v3.1 score, where the CNA left it out and there is enough evidence. — [README]
  - CWE (weakness type), where determinable. — [README]
  - A KEV flag if the CVE is on the Known Exploited Vulnerabilities catalog. — [README]
  - CPE (affected-product strings): **stopped 10 Dec 2024**; older records may still carry them. — [README]
- **Launch and why.** Announced 9 May 2024 amid the NVD backlog; at that point NIST had processed 4,523 of 14,280 CVEs received that year, and CISA had enriched ~1,300. — [Help Net Security, 9 May 2024](https://www.helpnetsecurity.com/2024/05/09/cisa-vulnrichment-cve-enrichment/); [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/cisa-launches-vulnrichment-program/)
- **NVD passes it through.** NIST has surfaced CISA ADP data via the NVD 2.0 API since July 2024. — [Bishop Fox, 22 Apr 2026](https://bishopfox.com/blog/understanding-the-cve-ecosystem-and-nists-changing-role)
- **How to consume it.** It is already inside the live CVE record (CVE Services API / CVE JSON), also via the GitHub repo; no need to fork. — [README]
- **Why it matters more now.** On 15 Apr 2026 NIST moved NVD to prioritized enrichment: KEV entries, federal-use software, and EO 14028 "critical software" first; everything else is "Lowest Priority – not scheduled for immediate enrichment." CVE submissions grew 263% from 2020 to 2025. — [NIST, 15 Apr 2026](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth)
- **SSVC is now federal policy vocabulary.** BOD 26-04 (June 2026) pins federal KEV remediation triage on SSVC-style factors (exposure, automatable, total control, active exploitation), with 3 / 14 / 60-day tiers. — [runZero, 10 Jun 2026](https://www.runzero.com/blog/bod-26-04/); [Nucleus, 18 Jun 2026](https://nucleussec.com/blog/navigating-requirements-cisa-bod-26-04/). *Note: neither secondary says BOD 26-04 uses Vulnrichment data as its input — the link is shared vocabulary, not a stated dependency. CISA's own BOD page returned 403.*

## What's contested / watch out
- **SSVC has five decision points; Vulnrichment publishes three.** Mission Prevalence and Public Well-being Impact are organization-specific, so CISA cannot fill them in for you. Launch-era coverage (e.g. [WaterISAC](https://www.waterisac.org/cisa-announces-cve-vulnrichment-program-fill-cve-enrichment-gap)) lists all five, which blurs this. The README lists three. Say "three", and note the reader supplies the other two. — [CISA SSVC page](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc)
- **Did it dent the backlog?** VulnCheck (Sep 2024) credited NVD's use of Vulnrichment CVSS as "a notable success" (85.9% of CVEs since 12 Feb 2024 had a CVSS record) but noted NVD had "not incorporated all data from Vulnrichment." — [VulnCheck](https://www.vulncheck.com/blog/nvd-backlog-exploitation-lurking). Phoenix Security (Jul 2024) cited ~200/day enrichment yet a growing backlog; its arithmetic is internally inconsistent, so do not print its numbers. — [Phoenix](https://phoenix.security/nvd-backlog-burndown-update/)
- **CISA as the only ADP.** Bishop Fox says CISA remains the sole approved ADP, which caps ecosystem capacity. One source; not independently confirmed.
- **It is not the go-to in practitioner guidance.** CSA's April 2026 note on NVD changes lists EPSS, VulnCheck NVD++, OSV and GHSA as alternatives and never mentions Vulnrichment. — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-nvd-enrichment-changes-enterprise-vul/). An absence in one note, not proof of irrelevance.

## Couldn't verify
- **Is it still actively enriching in Sep 2026, and at what volume?** GitHub commit history was blocked (robots.txt); CISA's program page and "Unlocking Vulnrichment" page returned 403. A spot-check of a 9 Sep 2026 Chrome CVE on a third-party aggregator showed no SSVC values — one record, not evidence of a halt.
- **Which CVEs CISA chooses to enrich.** The README says "every analyzed CVE" gets SSVC, which implies a subset, but I found no published selection rule. Do not infer one.
- **Whether BOD 26-04 or CISA's FY24–25 Vulnerability Review cites Vulnrichment.** Both primaries 403'd; the secondary on the Review found no mention.
- **Local corpus:** the folder shell failed to start, so Briefs/References were not searched for prior coverage.

## The economics
No cost figures exist in the sources. The economic story is labour-shift: NIST's model of central analysts enriching every CVE broke under 263% volume growth, and triage cost is being pushed downstream to every defender. Vulnrichment is free, government-supplied triage signal that partly offsets that — but only for the CVEs CISA analyzes, and only for the three universal questions. The organization-specific two (how prevalent is this in *my* estate, what is the public impact) remain the defender's cost.

## Drop-in facts
- "At no point will CISA overwrite the originating CNA's data." — [cisagov/vulnrichment](https://github.com/cisagov/vulnrichment)
- CISA launched Vulnrichment in May 2024, when NIST had processed 4,523 of the 14,280 CVEs received that year. — [Help Net Security](https://www.helpnetsecurity.com/2024/05/09/cisa-vulnrichment-cve-enrichment/)
- CVE submissions rose 263% between 2020 and 2025. — [NIST](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth)
- Since April 2026, NVD labels non-priority CVEs "Lowest Priority – not scheduled for immediate enrichment." — [NIST]
- Vulnrichment stopped adding CPE strings on 10 December 2024. — [README]

## Angles this opens
- "Who reads the police report now?" — NVD triage (Apr 2026) + BOD 26-04 (Jun 2026) + Vulnrichment together describe enrichment moving from one central analyst to a patchwork of signals, with the context-specific judgment landing on the reader's own team.
- SSVC's split between the three questions a government can answer for you and the two only you can answer is a clean frame for a CISO piece.
