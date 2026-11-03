---
name: estimand-substitution
description: "Engine 8 of the provenance failures — a research team silently changing WHICH estimator it headlines between versions; plus the wider discipline of checking what quantity an instrument actually estimates before stacking it beside another one"
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

**Identified 24 Aug 2026, from the displacement dig (`References\research_displacement-science_2026-08-24.md`).**
This is **engine 8** of [[brief-claim-provenance]], and unlike engines 1–7 the failure is **upstream of
the brief entirely** — it happens inside the research organisation, and every downstream account
inherits it faithfully.

## The rule

**Before quoting a number from a research series, check whether the SERIES changed instruments
between versions. And before putting two sources in the same sentence, check that they estimate the
same quantity.**

## Why: the case that named it

Stanford's *Canaries in the Coal Mine?* has three versions, and the headline number changed estimator
between them:

| Version | Data through | Headline | **What the number IS** |
|---|---|---|---|
| Aug 2025 | Jul 2025 | 13% | Poisson event-study coefficient, firm-time fixed effects |
| Nov 2025 | Sep 2025 | 16% | same estimator |
| **Aug 2026** | Jun 2026 | **19%** | **raw descriptive divergence, NO controls at all** |

The authors are honest about it in print — *"Earlier versions of this study headlined regression
estimates adjusting for firm-level shocks… **We now emphasize the simpler descriptive divergence,
which requires no modeling choices**"* — and give the like-for-like sequence as **15% → 19%**. Their
stated reason: *"the firm fixed-effects estimates are more sensitive than the raw descriptive results."*

**So "the estimate rose from 13% to 19%" charts two different instruments as one trend line, and it
is now the standard framing everywhere.** Nothing was dropped, nothing was added, no citation is
wrong. Engines 1–7 all pass it.

**And in the same paper, both signs of the story sit in one table:** ages 22–25, most-exposed
quintile, **−0.179 (SE 0.036) with no controls**, and **−0.080 (SE 0.057), not significant, with the
full control set.** Print both or print neither.

## How to apply

1. **When a research series updates, diff the METHOD section, not just the number.** A moving headline
   with a stable method is news; a moving method is not a trend.
2. **Before writing "X and Y both found," write down what each one's denominator is.** If they differ,
   they cannot corroborate and they cannot contradict. From the same dig, four sources routinely
   stacked into one paragraph:
   - **Budget Lab at Yale** — rate of change in the *occupational composition of the whole labour
     force* (dissimilarity index, CPS).
   - **Stanford Canaries** — *relative employment of ages 22–25* in exposed vs unexposed occupations
     (ADP balanced panel).
   - **Indeed Hiring Lab** — *flow of new vacancies posted* on one job board.
   - **ADP Research** — *monthly separation flow rate* (quits + layoffs ÷ lagged employment).
   No two share a denominator. **The "20x disagreement between serious institutions" was largely an
   estimand mismatch, not a disagreement.**
3. **Check whether each lab has already told you what its instrument cannot see.** Yale says in print
   the CPS is *"somewhat underpowered for subgroup analysis"* of exactly the cohort Stanford measures.
   Stanford's own Fact 1 is the economy-wide null. **Those are the same statement from two ends** —
   staging them as opposing camps manufactures a fight neither is having.
4. **Level vs counterfactual is the same error in miniature.** Stanford's 19% is a *shortfall against a
   counterfactual*, not a decline in a level. Amodei's claim is a level claim. Conflating them is the
   most common error in the commentary and it is worth naming in the draft rather than avoiding.

## The generalisation, and it is the reason this earns a file

> **A number with no error bars is not more precise than one with wide ones. It is less.**

Challenger's AI-attributed layoff count publishes no sampling frame, no confidence interval, no
methodology, no revision policy and no reconciliation to actual separations — and it is treated as
harder evidence than BLS series that publish all five. **Absence of a stated uncertainty reads as
certainty.** That is the same illusion as engine 6 (a good-looking citation doing the work of
provenance), one level up: a clean-looking number doing the work of precision.

Companion check, from the same dig: **what is the instrument's resolution against the claimed
effect?** BLS's own published threshold is that one month's change in household employment must
exceed **678,000** before the agency will call it real; the entire seven-month AI-attributed layoff
total is **112,713**. When the effect is inside the noise band of every instrument, the honest
sentence is *"an effect of this size could not be detected by these instruments"* — **never** "the
effect is smaller than the error bars," which claims to know the effect.

## Two attribution corrections found the same day, both engine-2 shapes

- **"Seniority-biased technological change" is NOT Indeed Hiring Lab's term or finding.** Indeed
  *hyperlinks* it once, to Hosseini Maasoum & Lichtinger (Harvard, SSRN 5425555), as a possibility
  that survives their own rebound result.
- **ADP does not claim to be measuring AI.** Its Feb 2026 dynamism piece contains no AI identification
  strategy at all, and the author's own caveat is that low turnover is sign-ambiguous. Putting it in a
  list of "AI measurements" does work the source refuses to do. (And **"low-hire, low-fire" is from
  ADP's 14 Oct 2025 post, not the Feb 2026 one.**)
