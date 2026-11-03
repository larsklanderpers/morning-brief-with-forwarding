# Research note -- Wed 21 Oct 2026 -- The Post Room (working)  [cyber, opens THE AFTERLIFE OF A HANDOVER]

Written 21 Oct 2026, Wed 21 day chat. All primaries read at the page on 21 Oct (live fetch, maxAge 0).

## SOLID (primary, read at the page)

**BAE / Bankruptcy Noticing Center**
- AO of the US Courts, notice "Cybersecurity Incident Disrupting Bankruptcy Court Operations", published 15 Oct 2026. https://www.uscourts.gov/data-news/judiciary-news/2026/10/15/cybersecurity-incident-disrupting-bankruptcy-court-operations
  - "The BNC produces and transmits bankruptcy notices for all federal bankruptcy courts around the country, and BAE Systems operates BNC systems and websites on behalf of the Federal Judiciary."
  - "all access to the BNC systems and websites ... are unavailable at this time, including bnc.uscourts.gov, bankruptcynotices.uscourts.gov, notices.uscourts.gov, and the National Creditor Registration Service."
  - "The incident has also halted the BNC's production and distribution of bankruptcy notices for bankruptcy courts."
  - "BAE is actively investigating this incident and working to restore operations." No update on the page as of 21 Oct.
- US Bankruptcy Court, S.D. Illinois, General Order 26-4, 15 Oct. https://www.ilsb.uscourts.gov/news/general-order-26-4-re-bankruptcy-noticing-center-service-bnc-interruption
  - Disruption "began on October 9, 2026" (so six days before the AO's public notice).
  - "parties should not rely on the BNC to transmit notices. Parties should themselves provide notification of important or time-sensitive bankruptcy events". "It is unknown when the disruption will be resolved".
- US Bankruptcy Court, E.D. New York, update 16 Oct. https://www.nyeb.uscourts.gov/news/update-regarding-bnc-service-disruption-and-accessing-list-creditors-cmecf
  - "nationwide service disruption since October 9, 2026, affecting all U.S. Bankruptcy Courts." "we do not have an estimated date or time for restoration". "Do Not Rely on BNC Confirmations". Mailing matrices: dig them out of the docket by hand.
  - CM/ECF and NEFs (email to registered filers) unaffected: the people who lose notice are the ones on paper -- pro se debtors and unrepresented creditors.
- US Bankruptcy Court, E.D. Michigan, Administrative Order 26-18 (supplemental), signed 21 Oct 2026 by Chief Judge Daniel S. Opperman. https://www.mieb.uscourts.gov/sites/mieb/files/news/Administrative%20Order%20%2326-18%20Re%20Supplemental%20Order%20Re%20BNC%20Service%20Interruption%2010-21-26.pdf
  - "Because the Court is unsure how long the outage may last ... temporary procedures are necessary".
  - Debtor "shall serve the official notice of commencement of the case and meeting of creditors ... within 3 business days of the petition filing."
  - The debtor's distribution "does not relieve the Clerk of any nondelegable duty."
  - "Parties shall not presume that a document transmitted to the BNC for processing has been delivered."
  - "No adverse action should be premised on a failure to respond to a notice whose legally sufficient delivery cannot be established."
  - Postage and copy costs "may, with Court approval, be imposed against the estate or client".
  - Upon restoration, coordinate "to avoid duplicate or inconsistent notices and address any outstanding backlog."
- **Arithmetic:** 9 Oct to 21 Oct = 12 days down, still no restoration date in any primary read.

**BeyondTrust / CVE-2026-102764**
- CISA alert, 16 Oct 2026. https://www.cisa.gov/news-events/alerts/2026/10/16/cisa-urges-patching-critical-vulnerability-beyondtrust-remote-support
  - Auth bypass, Remote Support (formerly Bomgar) <= 26.2.3; actors "gain initial access, then establishing persistence, escalating privileges, and moving laterally." Added to KEV 16 Oct.
  - Self-hosted: "conduct network and memory forensics". If compromise suspected: isolate, image, forward logs, hunt, then "Rebuild from a known-good state and apply the BT26-05-RS patch. Then rotate every credential the appliance stored or injected, revoke all active support sessions, and review new multifactor authentication registrations on privileged accounts." **The plan's must-survive sentence is footed verbatim.**
- BeyondTrust advisory BT26-05, issued 15 Oct, CVSSv4 9.3. https://www.beyondtrust.com/trust-center/security-advisories/bt26-05
  - "As of Oct 9, 2026, a patch ... has been applied to all Remote Support SaaS customers." Self-hosted must patch manually unless on auto-update. (Brief said 8 Oct; vendor's page says 9 Oct. Use 9 Oct.)
- Mandiant / GTIG, "ARMORY CASTLE Exploits BeyondTrust", 15 Oct. https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust
  - Zero-day exploitation "in late August 2026"; actor "a suspected PRC-nexus espionage threat actor (formerly tracked as UNC5221)".
  - "This gave them access to every credential the appliance stored or brokered".
  - Attempted to dump the appliance's own credential vault with BeyondTrust's native `bt-secrets` CLI.
  - "Every endpoint touched is in scope for downstream hunting."

## SINGLE-SOURCE / SECONDARY (attribute or leave out)
- "August 29" first compromise: Tech Insider citing a GTIG timeline. GTIG page read says "late August". Print "late August".
- WSJ Pro: courts "forced ... to adopt emergency measures" (paywalled, excerpt only). Not needed: the court orders are primary.
- Rescana: incident "as early as October 9" (consistent with courts). No ransomware, data theft or vector confirmed anywhere as of 16-21 Oct. **Do not print any.**
- BAE: "isolated to the BNC system" (dig.watch, attributed to BAE). Attribute if used.
- CrowdStrike name "Warp Panda" (brief). Not needed.

## COMMERCIAL INTERESTS TO NAME
- Mandiant is Google; it sells incident response and found this during an IR engagement. BeyondTrust sells the product and the "what security teams need to know" blog.

## COLLISION NOTES
- Wed 14 used a *different* BeyondTrust remote-support flaw as GTIG's speed-of-exploitation example (six groups in a week). Today: one clause separating them; the lesson is the keys the box held, not the patch order.
- Wed 7 used "handed over" for delegation at the grant. Today is after the grant. Say so once.

## DO-NOT-PRINT
- Any ransomware, data-theft or attack-vector claim on BAE.
- "Aug 29" as fact.
- Any claim BNC is restored (not as of 21 Oct).
- "blast radius", vault-as-image (Wed 14), heist, crew.

## UNREACHED
- KEV catalog entry page itself (CISA's alert states the add; sufficient).
- Any AO update after 15 Oct (none on the notice page).
