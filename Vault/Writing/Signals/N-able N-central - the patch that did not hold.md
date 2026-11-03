---
date_first_seen: 2026-08-07
date_updated: 2026-08-07
source: N-able / CISA KEV / Huntress / Rapid7 / The Register
url: https://www.n-able.com/blog/n-central-security-update-august-6-2026
brief: cyber
threads: [Supply Chain, Trust Boundaries, AI Attack Surface]
beat: Cyber / MSP / Exploitation
status: signal
used_in:
---

# N-able N-central — the patch that did not hold

**What happened.** Pre-auth authentication bypass in N-central, exploited in the wild against MSPs.
N-able's own Adlumin MDR caught it at a customer on **31 July**. Attackers used the bypass to gain
admin, then drove N-central's built-in **Take Control** remote-access feature into managed endpoints,
then registered a **Cloudflare tunnel** so they kept their foothold after N-central access was revoked.
Hotfix 1 (2026.3.1.7, 2 Aug) was superseded by Hotfix 2 (**2026.3.1.10, 6 Aug**). Ten attacker IPs published.

**Why it matters.** The detail the brief flattened is the whole story: **CVE-2026-18577 is the
incomplete patch for CVE-2026-18556**, not a sibling bug. NVD wording: *"An incomplete patch for
CVE-2026-18556 allows for authentication bypass and account takeover in N-central Versions through
2026.3.1."* The vendor shipped a fix and the attackers walked around it. That is a different argument
from "patch faster" — it is *the remediation itself was the attack surface*, which is the sharpest
available version of the trusted-layer thesis.

## Verified 2026-08-07 — three corrections to carry

- **CVSS is not 9.8.** 18577 = **8.1** (AV:N/**AC:H**/PR:N/UI:N/C:H/I:H/A:H), published 2 Aug.
  18556 = **7.4** v3.1 / 8.2 v4.0, published 1 Aug. Note `AC:H` on both — exploitation was rated
  *not trivial*, and it happened anyway. Do not write "critical 9.8."
- **KEV dates split**, they were not a pair: 18577 added **3 Aug** (fed due date 6 Aug);
  18556 added **4 Aug** (due 7 Aug), alongside Apache Tomcat CVE-2026-34486 and IBM Langflow
  CVE-2026-9198. The Register: *"Feds get 3 days to patch."*
- **Nobody has published a victim count.** N-able says only *"a limited number of customers have been
  identified as impacted"* and **declined to give The Register figures**. Huntress had **one** confirmed
  compromised org in its partner base. There is also **no public figure for endpoints per N-central
  instance** — do not assert one. **[VERIFY] closed as: unavailable, write the gap not a number.**

**The patch-lag telemetry is the usable number** (Huntress, confirmed): 3 Aug 00:45 ET — **55.6%** of
reachable partner cloud servers unpatched; by 14:15 ET the same day — **13.6%**. Fourteen hours to go
from half-exposed to one-in-seven, which is a *good* result and still leaves the tail.

## The comparison set, held honestly

- **Aug 2025 N-central (CVE-2025-8875 / 8876, KEV 13 Aug 2025):** both required **authentication**.
  N-able used near-identical language then — *"a limited number of on-premises environments."*
  The 2026 pair is materially worse: pre-auth, and it defeated the vendor's own first patch.
- **Kaseya VSA, 2 Jul 2021:** ~60 MSPs, 800–1,500 downstream businesses, REvil, $70M demand.
- **Same door, different intent.** Kaseya was mass ransomware in a day. The 2026 activity so far reads
  as targeted access-and-persistence — tunnel, DC recon — not encryption. "Kaseya again" overclaims on
  current evidence; **"the same door, different intent"** is defensible and is the better line anyway.

## Observations

- **2026-08-07** — First seen. The incomplete-patch relationship and the Cloudflare-tunnel persistence are the two keepers. Persistence via a legitimate-looking outbound tunnel is the same move that makes egress filtering, not patching, the control that would have mattered.

## Feeds

- [[Supply Chain]] — the MSP's management plane as inherited trust
- [[Trust Boundaries]] — Take Control *is* the boundary; it was designed to be crossed
- [[AI Attack Surface]] — Collapsed Timelines: 3-day federal patch window, hours of real exposure

## Open

- The unwritten piece here is **remediation as attack surface**: hotfix 1 created a false all-clear that some MSPs will have reported to customers as "patched." Who owns that disclosure downstream?
