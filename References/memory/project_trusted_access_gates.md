---
name: trusted-access-gates
description: The 8 Sep 2026 dig into the three labs' cyber capability access programs — what the primaries actually say, and the four things the coverage got wrong
type: project
sources: [cowork-import]
imported_at: 2026-09-15T13:26:50Z
---

Research for the Thu 10 Sep 2026 piece "Approval Is Not Automatic". Full note:
`References\research_trusted-access_2026-09-08.md`. All primaries fetched live 8 September 2026.

## The four findings

1. **"Approval is not automatic" is OpenAI's own verbatim sentence**, from the Trusted Access for Cyber
   help centre article, not a phrase the week plan invented. The piece's title is a quotation.
2. **★★ Daybreak Blue is built on GPT-5.6 Sol, not Astra.** So is Daybreak Red (which adds a
   GPT-5.6-Cyber variant "to further reduce refusals"). Astra's advanced cyber capabilities went to
   "a small group of alpha testers, with access through Daybreak Blue expanding afterward." The
   defensive program every security team is pointed at runs the previous generation.
3. **All three access instruments start in the United States.** Anthropic's CVP explicitly and only
   ("Currently, it is only available to a set of US organizations, though we're coordinating with the US
   government to expand access"); OpenAI's $1B subsidy "starting with the United States"; Google's
   Fairwind is the only one that is neither US-scoped nor future-tense.
4. **The gated tier has no published price at any of the three.** Checked five pages. Recorded as a
   documented absence on five paths, never as "nobody publishes a price."

## The three instruments are not comparable

- **Google Fairwind** — live, contractual, published conditions (phishing-resistant MFA, access confined
  to internal cyber/IR/pentest teams, tracked employee use, no redistribution). "over 650 partners
  globally" is Google's own figure, single-source, no independent count located.
- **Anthropic CVP** — safeguard reduction, not a model tier. Mythos 5.1 "is identical to Fable 5.1, but
  it offers more permissive safeguards." Mythos-class access is future tense.
- **OpenAI Daybreak** — a staged rollout with a review step, in two tiers (Blue / Red), both on Sol.

**Why it matters:** "trusted access" is one borrowed word over three mechanisms, and it is heading into
procurement documents as though a buyer could evaluate it.

## What the coverage got wrong, including his own brief

- **His own 5 Sep AI brief asserts the false symmetry** — "All three major labs now ship in two speeds."
  Wrong on tense for Anthropic, wrong on mechanism. The Thu 10 piece corrects it in the text, by name.
- **"The most capable model went to the defenders first"** (TechCrunch paraphrase, carried into the 5 Sep
  addendum as the piece's opening image) is NOT supported by OpenAI's own text. Dead.
- **"$1B active in 20+ countries"** blends two different OpenAI statements four days apart — the
  subsidy's starting line and the program's existing footprint. His 5 Sep brief blended them.
- **Never rank the labs across frameworks.** The Critical designation is OpenAI's, under OpenAI's
  Preparedness Framework. Google's model card uses different vocabulary. Welding them is the
  INSTRUMENT WELD failure in [[brief-claim-provenance]].

## The reseller clause — his ground, in none of the coverage

OpenAI: access "cannot extend to third-party customers, external users, customer-facing workflows, or
downstream product traffic." **That removes the managed-services channel from the capability tier.**
An MSP cannot obtain it and run it for clients.

## How to apply

- This note's DO-NOT-PRINT list binds every later revision of the Thu 10 piece, not just v1.
- The gate (Thu 10) / glass (Fri 11) firewall: nothing here touches monitorability, chain-of-thought or
  Pachocki. See [[astra-monitorability-dig]].
- Re-check before any reuse: Anthropic's US-only line and Mythos tense are the most perishable facts in
  the note, and Anthropic says expansion is actively being coordinated.
