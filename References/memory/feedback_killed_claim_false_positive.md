---
name: killed-claim-false-positive
description: "The mirror of engine 5 — a do-not-print entry that was WRONG, propagated into four documents, and was never re-tested because skepticism reads as rigour. Second case 9 Sep 2026: a true figure killed by searching the perpetrator's primaries and not the victim's"
type: feedback
sources: [cowork-import]
imported_at: 2026-09-15T13:26:00Z
---

**Identified 23 Aug 2026, on the Allie Miller "34 agents" entry.** This is the eighth engine and it
runs in the opposite direction to the seven in [[brief-claim-provenance]].

## The case

The 14 and 16 Aug digs killed "Allie Miller runs 34 AI agents": *"No primary states 34. Her public
figures are 7, 20 and 25, never 34. 'Escalate only what needs her' appears in no primary source at
all. No Greg Isenberg episode could be located."*

**Three of those four assertions were false when written.** The 23 Aug pass, plus an adversarial
refutation pass instructed to kill the reversal, established:

- The Isenberg video exists — YouTube oEmbed returns channel **Greg Isenberg**, title
  **"I Run 34 AI Agents with a 3-Word Prompt."** The title itself is the primary.
- Apple Podcasts show notes, pulled from Isenberg's own RSS and fetched **identically from US and GB
  storefronts** to rule out an aggregator artefact: *"Allie runs a workforce of 34 AI agents led by
  an AI chief of staff named Simon, plus six directors named after Friends characters."*
- *"escalate only what needs her"* is verbatim on **her own subdomain**,
  `events.alliekmiller.com/mark-replay`.
- "7, 20 and 25" were **earlier snapshots of a growing count.** The kill read a time series as a
  contradiction.

**Two carve-outs survive:** the Stripe/calendar/email/transcripts access list (one untraceable
caption) and "do smart things" as a quotation (only in AI-generated aggregator summaries).

## ★★ SECOND CASE, 9 Sep 2026 — and the mechanism is new

**In the morning I killed "17,600 attacker actions / 6,280 clusters"** — the figure the pipeline had
called "the doubles-the-impact number" since July — recording it as *"could not be found in any OpenAI
primary"* and *"secondary-only (TechTimes, 29 Jul)."* **By the afternoon it was verified as real, in a
primary, and the July note was vindicated.**

It is in **Hugging Face's own technical timeline**, `huggingface.co/blog/agent-intrusion-technical-
timeline`, complete with the forensic window `2026-07-09 02:28 UTC` to `2026-07-13 14:14 UTC`.

★ **The mechanism, and it is worth its own name: I searched the PERPETRATOR's primaries and concluded
absence without searching the VICTIM's.** The dig read OpenAI's incident report, OpenAI's technical
report and OpenAI's system card, found nothing, and wrote a kill. **The company whose agents did the
attacking has no reason to publish the forensic action count. The company that was attacked reconstructed
it, and published it, on its own domain, five weeks earlier.**

**The generalised rule: an incident has at least two first parties, and a kill on absence is only sound
once you have searched every one of them.** Perpetrator, victim, evaluator, regulator, and any third
party that filed. Check each surface before writing "no primary states X."

⚠️ **And the correction had already propagated.** The false kill went into the morning research note's
§9, into the week-plan addendum, and into project memory as a "correction owed to
`research_openai-hf-copilot_2026-07-31.md`" — three documents in one morning, telling a future session
that a true figure was unsourced. **This engine propagates exactly as fast as engine 5 does.**

★ **A second, smaller instance the same day:** three items recorded as "could not verify" were **403 /
paywall / 429 transport failures**, not absences — see [[absence-verification]]'s 9 Sep amendment. **Both
failures share a root: a negative result was written down without asking what would have had to be true
for the search to find it.**

## Why this is structurally worse than a regenerating false claim

Every engine in [[brief-claim-provenance]] describes the record becoming **more confident than the
evidence**. This one describes it becoming **more skeptical than the evidence** — and because
skepticism reads as rigour, **nothing in the existing check catches it.** A killed claim gets
re-tested every time it regenerates. **A do-not-print entry is never re-tested; it is inherited.**

It propagated exactly like a regenerating claim would: from one research note into
`week-plan_2026-08-17.md`, `week-plan_2026-08-24.md`, and three `read-only-first` drafts including
the scheduled 25 Aug piece. (The piece *body* correctly omitted the number, so nothing wrong shipped.)

## How to apply

**1. Two kinds of kill, marked differently, always.**
- A kill from **contradicting evidence** ("the primary says Y, not X") is **durable**.
- A kill from **absence of evidence** ("no primary states X") is **provisional**. Write it as
  *"not found as of &lt;date&gt; — re-check before reuse,"* **never** *"the do-not-print stands."*

**2. Before killing on absence, check the subject's own surface.** The 14 Aug search covered the
surfaces that talk *about* her and missed her own domain, her own captions, and a podcast published
two days earlier. **This is the fifth question in the four-minute check, and it runs in both
directions: did you look on the subject's own surface, or only on the surfaces that discuss them?**

**★ 2b (9 Sep). For an INCIDENT, "the subject's own surface" is plural.** Perpetrator, victim,
evaluator, regulator, filer. **Name them before you search, and say which ones you checked in the kill
itself.** A kill that names only one first party is provisional on its face.

**3. "An aggregator carried it" is not disproof.** Podcast Rex (footer: *"Compiled by Rex AI"*) and
Listen Notes are LLM-summary sites and were correctly distrusted — but the text they carried was the
publisher's own RSS, not invented. **The alphaXiv trap requires finding the publisher's surface, not
discarding the claim.**

**4. Platform-blocked ≠ nonexistent.** X, TikTok, LinkedIn and Instagram cannot be fetched. A real,
circulating claim still leaves **search-index snippets reproducing the post body**. Search the
distinctive string before concluding absence — and if even that returns nothing (as with the Stripe
caption), *then* the kill is sound. **★ 9 Sep: and a 403 or a paywall is not a platform block either —
escalate to Firecrawl before recording anything. See [[absence-verification]].**

**5. ★ Re-run your own kill list before the note ships.** On 9 Sep, one pass over the day's own
"could not verify" items overturned four of them. **The cheapest verification in the pipeline is
re-testing the negatives you just wrote.**

**Why it matters to Lars specifically:** his whole Saturday thread is about how the record gets
wrong. The machinery built to stop engine 5 caused this one. That is a first-hand, dated case only he
can write — filed in `References\research_story-candidates_2026-08-23.md` §0 and §11, and now with a
second dated instance in `References\research_story-candidates_2026-09-09.md` and
`References\research_openai-safety-function_2026-09-09.md`.
