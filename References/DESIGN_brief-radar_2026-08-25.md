---
type: design-note
topic: Fixing killed-claim regeneration and repetition in the daily briefs — the "radar" step
date: 2026-08-25
status: PROPOSED. Nothing built into the tree. Demonstration run only; results in §3.
requested-by: Lars, 25 Aug 2026 — "how do we fix it? we talked about moving this to a standalone
  radar on the code side etc., what's our best way to fix this problem and get the daily reader
  cleaner for me?" Plus: "maybe we should date the articles in the board" (§7 — separable, do it first).
supersedes: the diagnosis in `feedback_brief_claim_provenance.md` §5, which names `briefing_agent.py`
  as the thing that does not read the do-not-print list. **That is true and irrelevant — see §1.**
---

# Design Note — The Brief Radar

## Bottom line, in five sentences

**1.** The corpus has been blaming the wrong component: `briefing_agent.py` does not generate these
briefs and has not for some time — the three morning briefs are produced by **agentic skill prompts**,
so the fix is not a Python patch to the generator.
**2.** Three different failures arrive each morning and they need three different mechanisms:
**regeneration** (a killed claim comes back), **repetition** (a topic already written about is offered
again), and **fresh error** (a new number that is simply wrong) — one of which a deny-list cannot
catch at all.
**3.** The right shape is a **post-generation annotator**, not a pre-generation prompt rule: one
implementation instead of three, it survives skill drift, it is deterministic where determinism is
possible, and it **annotates rather than edits** so nothing silently disappears.
**4.** I built the deny-list and ran it: **243 killed claims extracted from the existing corpus, 674
match strings, and 31 hits across today's three briefs after a precision pass** — including
**CVE-2026-68820 firing three separate kills in one brief**, one of them on its third regeneration.
**5.** The whole thing is cheap because **the store is derived, not authored** — the research notes
stay the source of truth, which is the only version that does not violate the standing "no second
store, no fourth copy" rule.

---

## §1 ⚠️ The diagnosis on file is aimed at the wrong component

`feedback_brief_claim_provenance.md` §5 says: *"the do-not-print lists live in `References\` and
**`briefing_agent.py` does not read any of them**. Each morning's generator starts from the open web
with no memory of what was killed."*

The second sentence is exactly right. The first names the wrong file, and it has been steering the
fix toward a Python change for a week.

**Evidence.** `briefing_agent.py::format_brief()` emits sections titled *🚨 Government Advisories ·
🇦🇺 Australian News & Regulation · 📧 Google Alert Articles · 📰 Security News · 🗣️ Community
(Reddit)*, numbers every item `### [n] Title`, and appends `*Flag for Substack: python
briefing_agent.py --flag n*` to each. **None of that appears in any recent brief.** Today's cyber
brief runs *🚨 Government Advisories · 📰 Top Security News · 🤖 AI & Security · 🗣️ Community Pulse
· 📌 Today's Signal*, with no item numbers and no flag lines. Its commentary is also far beyond what
that script can produce — it calls Haiku at `max_tokens=200` against RSS summary text.

**What actually runs:** three agentic skill prompts on a schedule (~11:41 UTC daily, consistently),
writing `Daily Briefs\brief_*.md`, `AI Briefs\ai_brief_*.md` and `AI Briefs\work_brief_*.md`. The
root-level `ai-morning-brief-skill.md` is the AI brief's spec — **and it is itself already a stale
snapshot**: it describes five lanes and a section list that today's brief does not match (today has
*📬 From the Substacks* and *📡 Social Intelligence*, which appear nowhere in that file). That is the
[[Charter Drift (3 copies)]] failure showing up again, in the brief pipeline this time.

**Two consequences, and they set the whole design:**
- **`briefing_agent.py` is legacy. Do not patch it.** Leave it; it is not in the path.
- **Do not put the fix in the skill prompts.** There are three of them, at least one has a stale
  copy on disk, and a prompt rule competes with twenty other instructions and degrades silently.
  **Anything we build has to work on the OUTPUT, where there is one format and three files.**

---

## §2 Three failures, three mechanisms — they are not one problem

The single most useful thing this exercise produced. "Restatement" is three different defects
wearing one word, and only one of them is fixed by a deny-list.

| # | Failure | Example from this week | Mechanism that catches it | Catchable deterministically? |
|---|---|---|---|---|
| **A** | **Regeneration** — a claim a research note explicitly killed comes back as a finding | *"800%" FDE spike* (killed 23 Aug, back 24 and 25 Aug) · *CVE-2026-68820 as an RCE* (killed 14 Aug, back three times) | **Deny-list** matched against the brief text | **Yes — mostly.** 96% of kills have at least one distinctive literal |
| **B** | **Repetition** — the topic is not wrong, it has just already been written | CrowdStrike THR (spent Mon 10 Aug, offered again 24 Aug) · four-questions device (four pieces deep) | **Spent-index** built from `SUBSTACK_INDEX.md` + Published + Scheduled | **Yes**, on title/proper-noun overlap |
| **C** | **Fresh error** — a new number that is simply wrong, never killed because never seen | ⚠️ **Today: *"Challenger shows 48% of tracked 2026 layoffs attributed to AI."* The real figure is 112,713 of 477,033 = 24%. Doubled.** | **Nothing on the deny-list can see this.** Needs a numeric-consistency check against known corpus values, plus the engine 1–8 pattern rules | **Partly** — see §4.3 |

**Class C is the honest limit of the whole idea and it should be stated up front rather than
discovered later.** A deny-list is a memory of past mistakes. It cannot catch a mistake being made
for the first time. Today's 48% is exactly that, and it is arguably the worst item in today's intake
because it is confidently precise and completely new.

---

## §3 ★ The demonstration — I built the deny-list and ran it against today

Not a proposal. This ran, this morning, against the real files.

**Extraction.** 243 killed claims pulled out of `References\research_*.md` and
`week-plan_*.md`, each with a verdict, a correction, a kill date, a regeneration count, and 2–6
literal match strings. 674 match strings total.

| Verdict | Count |
|---|---|
| MISCHARACTERISED | 89 |
| UNSOURCED | 59 |
| REFUTED | 52 |
| MISATTRIBUTED | 26 |
| STALE | 17 |

**96% (234/243) carry at least one PRECISE literal** — a number, a CVE, a proper noun, or a
multi-word phrase. Only nine need semantic matching. **That is the finding that makes this cheap:
this is overwhelmingly a string problem, not a model problem.**

**Results against today's actual output**, after a precision filter (drop anything under 5 chars,
require a digit / a ≥12-char phrase / an identifier / a ≥9-char proper noun):

| File | Raw hits | After precision pass |
|---|---|---|
| `brief_2026-08-25.md` (cyber) | 18 | **10** |
| `ai_brief_2026-08-25.md` | 19 | **12** |
| `work_brief_2026-08-25.md` | 14 | **8** |
| Today's starred candidates | 3 | **1** |
| **Total** | 54 | **31** |

**The headline result, and it is damning:** in today's cyber brief, **`CVE-2026-68820` fires three
separate kills at once** —

> `[MISCHARACTERISED · regenerated ×3]` characterised as a remote / unauthenticated / wormable RCE
> `[REFUTED · regenerated ×2]` any sentence pairing it with "Task Host," "April," "ransomware" or "confirmed"
> `[MISATTRIBUTED · regenerated ×1]` Lazarus attribution presented as CISA's or Microsoft's rather than Check Point's

Today's brief calls it *"confirmed under active exploitation"* and leads with it. Others firing today:
`CPS 230` (twice), `CLOUD Act` (twice), `GLM-5.3`, `ShieldBreak`, `AA26-222A` Gunra sectors,
`Cloud Security Alliance`/Darktrace, `$200K–$630K` FDE comp, `56,000+ FDE jobs`, `6% wage premium`,
`10 December 2026` plural, `AI Index` governance figures.

**Runtime: under a second. Cost: nothing. No model call.**

⚠️ **And the precision is not yet good enough to ship silently.** The raw pass fired on generic
strings — `malware`, `sandbox`, `stole`, `WARN`, `Hacker News`. That is a match-string quality
problem, not a design problem, and it is why **the radar annotates and never suppresses** (§4.2).

---

## §4 The design

### 4.1 Shape: a post-generation annotator, standalone, deterministic-first

```
  three brief skills  ──►  Daily Briefs\ · AI Briefs\        [UNCHANGED. Do not touch them.]
                                    │
                                    ▼
                              radar.py                        [new · standalone · no model call
                                    │                          in the default path]
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
      killed-claims.json     spent-index.json        pattern rules
      (DERIVED from          (DERIVED from           (engines 1–8, regex)
       References\)           SUBSTACK_INDEX +
                              Published + Scheduled)
                                    │
                                    ▼
                       radar_YYYY-MM-DD.md   +   flags consumed by the Brief Tracker
```

**Post-generation, not pre-generation.** Four reasons, in order of weight:
1. **One implementation, not three.** The brief skills stay untouched, so nothing has to be kept in
   sync across three prompts and their stale copies.
2. **It survives skill drift** — the failure mode already documented twice in memory.
3. **It is deterministic.** A prompt rule is a suggestion the model weighs against everything else in
   its context. A string match is not.
4. **It cannot hallucinate a kill.** The worst case is a false positive you can see and dismiss.

### 4.2 ★ It annotates. It never deletes.

**Non-negotiable, and the reason is [[Killed-Claim FALSE POSITIVE]].** A do-not-print can be wrong.
The 23 Aug session established that an absence-kill is provisional and that skepticism reads as
rigour, so a bad kill never gets re-tested. **A radar that silently suppressed items would make that
failure permanent and invisible.** So: every item stays in the brief, with a badge and a one-line
reason, and the kill's own date attached.

Four badge classes:

| Badge | Meaning | Action implied |
|---|---|---|
| 🔴 **KILLED** | Matches a do-not-print. Shows the claim, the correction, the kill date, the source note, and the regeneration count | Read the correction before using |
| 🟡 **SPENT** | Topic published or scheduled on date X | Read the prior piece before re-writing |
| 🟠 **CHECK** | Pattern hit — superlative with no primary, modal upgrade, engagement metric as evidence, date-trap tell | Four-minute check |
| ⚪ **STALE KILL** | The kill is an absence-kill older than N days and has never been re-tested | **Re-test the kill, not the claim** |

**That fourth badge is the one nobody builds and it is the one that keeps the instrument honest.**
**58 of the 243 kills (24%) rest on absence of evidence** and carry `expiry_risk: high` — things like
*"Mitiga's PromptLogger report is not publicly locatable"* or *"ASIC's own words were never verified."*
Those are exactly the ones that can quietly become wrong. Suggested expiry: **45 days**, then the
radar surfaces it for re-test rather than firing it as a kill.

### 4.3 What handles class C (fresh error)

Two cheap mechanisms, neither of which needs a model:

**(a) A watched-numbers table.** A small set of figures the corpus has verified and expects to see
quoted — Challenger YTD totals and the AI share, BLS payroll levels, the Stanford 19%, the
denominator counts. When a brief prints a number *near* one of these but not equal to it, flag
🟠 CHECK. **Today's 48% would have fired against a known 24%.** This is maybe forty lines of code and
it catches the single worst item in today's intake.

**(b) Engine 1–8 regex rules.** The cheapest three, in order of documented frequency:
- **Superlative insertion (engine 7):** `first|unprecedented|largest|no one has|marks the first time`
  → 🟠 CHECK, always. Documented as manufactured-in-the-summarising-step, so no source diff catches it.
- **Engagement-as-evidence:** `\d+ (points|upvotes|comments)` used as a significance claim.
- **Date-trap tells (the four documented instances):** an old model list (`GPT-4`, `Claude 2`,
  `PaLM-2`, `Llama 2`) in an item presented as current; or a source URL whose year path is not this
  year while the item sits under "Today's Signal."

**What is explicitly OUT of scope.** Do not try to automate engines 2, 3, 4 or 6 — attribution drop,
denominator drop, co-authorship collapse, citation laundering. Those need the primary opened. The
radar's job is to **narrow the manual pass from every item to the flagged ones**, not to replace it.

### 4.4 The two derived stores — and why "derived" is the whole trick

The standing rule from [[Week-Shaping Skills]] is **no second store, no fourth copy.** A hand-authored
killed-claims file would violate it immediately and drift within a fortnight.

**So both stores are build artifacts, like a compiled index — generated, never edited:**

- **`killed-claims.json`** ← generated from the do-not-print blocks in `References\research_*.md` and
  the week plans' accuracy watchlists. **The research notes remain the single source of truth.** Kill
  something in a research note; it is on the deny-list the next morning.
- **`spent-index.json`** ← generated from `SUBSTACK_INDEX.md` + `Substack Published\` +
  `Substack Scheduled\`. Title, date, thread, and the proper nouns each piece used.

**The one cost worth naming honestly:** extraction currently needs a model pass, because the
do-not-print blocks are prose and the section number varies (§10 in the story-candidate notes, §6 in
the displacement note, inline ❌ elsewhere). **That backfill is already done — it produced the 243
items above.** Going forward the fix is a convention: have the research-assistant skill emit a fenced
machine-readable block at the end of every note. After that, extraction is `grep`, and the model pass
is only needed to re-backfill if the convention slips.

---

## §5 What I considered and rejected

| Option | Why not |
|---|---|
| **Patch `briefing_agent.py` to read the kill list** | It does not generate the briefs. Pure waste — and this is what the corpus's own diagnosis has been pointing at. |
| **Add a "check the do-not-print list" instruction to the three brief skills** | Three copies to maintain, at least one already drifted, and a prompt rule degrades against twenty competing instructions. It also cannot be tested. |
| **One hand-authored killed-claims master file** | Violates "no second store." Drifts from the research notes within two weeks, and then nobody knows which is authoritative. |
| **Have the radar rewrite the brief** | Breaks [[Killed-Claim FALSE POSITIVE]]. A wrong kill would become permanent and invisible. Annotate only. |
| **Do the whole thing with a model pass over each brief** | Slower, costs money daily, and can hallucinate a kill that was never made. Use the model only for the 4% of claims with no distinctive literal, and only on the residue. |
| **Fold it into the Brief Tracker rebuild** | Couples a data problem to a UI problem. The tracker should *render* flags, not compute them. Keep `radar.py` standalone so it can be run and tested on any past brief. |

---

## §6 ★ Regression-testing it — the thing that makes this trustworthy

`radar.py` should be runnable against **any historical brief**, because we already know the answers.
The corpus records the dates on which specific claims were killed and the dates they came back.

**That gives a free labelled test set.** Run the radar over `Daily Briefs\` and `AI Briefs\` for
14–25 Aug and check it catches the documented regenerations: the 115K layoffs figure, the CSA/Darktrace
attribution on 20 Aug, CVE-2026-68820 on 17/19/25 Aug, the meta-skills claim on 17 and 23 Aug, "800%"
on 24 and 25 Aug. **If it does not catch those, the match strings are wrong and we find out before
trusting it.** No other component in this pipeline has a regression test; this one can have one for
free.

---

## §7 ⚡ The separable cheap win — dates on the board. Do this first.

Lars, 25 Aug: *"maybe we should date the articles in the board so we have some context about how fresh
something is even separate from the full fix."* **Correct, and it is independent of everything above.**

**It also attacks a documented engine on its own.** The date trap has **four recorded instances** —
ETH Zurich's 2023 profile-inference study run as August 2026 news (a 34-month error), Airbnb's FY2020
marketing cut, Shopify's Feb 2023 meeting purge, and the CSA/Darktrace April 2026 survey run as a
same-day finding. Every one would have been visible at a glance with a publication date on the card.

**Two changes, both small:**
1. **The three brief skills emit a structured date per item** — one line, `**Published:** YYYY-MM-DD`,
   next to the existing `**Source:**`. Where the publication date genuinely cannot be determined,
   emit `**Published:** unknown` rather than omitting it — *unknown* is information.
2. **`outputs_build/build.py` renders age on the card** — the date plus a computed age badge.
   Suggested thresholds: **≤2 days** plain · **3–7 days** amber · **>7 days** ⏳ with the age in days ·
   **unknown** a distinct grey badge, because an undated item is the one most likely to be a date trap.

**Sort or filter by age** falls out of it for free, which is what makes the board a reader rather
than a list.

⚠️ **One caveat:** this is the *publication date of the source*, not the date the brief picked it up.
Those differ by exactly the amount that matters. Do not let the skill default to today's date when it
cannot find one.

---

## §8 Build order, and what each step costs

| Step | What | Cost | Value |
|---|---|---|---|
| **0** | **Dates on the board** (§7) | Small — one line per item in three skills, one badge in `build.py` | Immediate, visible every morning, kills a documented engine |
| **1** | Commit `killed-claims.json` (**already generated — 243 items**) + a 30-min precision pass on the noisy match strings | Nearly zero | The store exists |
| **2** | `radar.py`, deny-list only, output = `radar_YYYY-MM-DD.md` | Half a day | Catches class A. **31 flags on today alone** |
| **3** | Regression-run it over 14–25 Aug (§6) | An hour | Proves it before it is trusted |
| **4** | `spent-index.json` + 🟡 SPENT badges | Half a day | Catches class B — the "I already wrote this" repetition |
| **5** | Watched-numbers table + the three regex rules (§4.3) | Half a day | Catches the worst of class C. **Would have caught today's 48%** |
| **6** | ⚪ STALE KILL expiry surfacing | Small | Keeps the deny-list from becoming a ratchet |
| **7** | Tracker renders the badges inline | Depends on the tracker | The point of the whole thing — flags where he reads |
| **8** | Research-assistant emits a fenced do-not-print block | Small | Extraction becomes `grep` forever after |

**Steps 0–2 are the 80%.** Everything after is refinement.

⚠️ **Scheduling `radar.py` to run after the briefs is RED** — new standing automation is Lars's call.
Until then it runs on demand, which is enough to prove it.

---

## §9 Open decisions — his call, not mine

1. **Where does `radar.py` live?** Project root beside the other scripts is the obvious answer, but
   root is outside the GREEN zone in `CLAUDE.md`. Say the word and it goes in.
2. **Does the radar annotate the brief files in place, or write a sidecar `radar_*.md`?** Sidecar is
   safer (the briefs stay pristine, and the radar can be re-run) but means two files to read. **My
   recommendation: sidecar until the tracker renders the badges, then the tracker is the reader and
   the sidecar is just data.**
3. **The STALE KILL expiry window.** 45 days is a guess. It should probably be shorter for
   absence-kills on fast-moving vendor claims and longer for structural ones.
4. **Does the radar run on the briefs, on the starred candidates, or both?** Both is right — the
   briefs are where errors enter, the candidates are where they reach a draft — but the candidate
   list is generated in the tracker, so that half depends on step 7.

## §10 Housekeeping found along the way

⚠️ **`CLAUDE.md`'s "Current week plan" pointer is stale.** It names
`References\week-plan_2026-08-17.md` as current; that window closed 23 Aug. Should point at
`week-plan_2026-08-24.md` (and `week-plan_2026-08-31.md` from Monday). Not fixed — `CLAUDE.md` is not
in the GREEN list and it is the file that defines the GREEN list.

⚠️ **`ai-morning-brief-skill.md` at the project root is a stale snapshot** of the installed AI-brief
skill — its section list no longer matches what the brief emits. Same class as the three-copies charter
drift. Worth reconciling or deleting so nobody edits it believing it is live.
