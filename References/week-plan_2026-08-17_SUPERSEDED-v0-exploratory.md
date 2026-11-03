---
type: week-plan
week: 2026-08-17 → 2026-08-23
status: EXPLORATORY (v0 — shape proposal, 2 Aug 2026, off the 2 Aug story candidates)
capstone: 2026-08-23 (spine not locked — see fork)
experiment: TWO diversions (Tue ground game + Sat long form)
---

# Week Plan — Aug 17–23, 2026 (exploratory)

**The reader-state premise.** Lars, 2 Aug: *"everyone is asking me what to do."* That is the
week. The last three weeks argued that control is a design decision, that guardrails are how
you give power away, and that you can locate your own. The audience has finished the "is this
real" phase. Today's AI Work brief names the same turn independently: *the community is moving
from anxiety to operations.* This week answers the question they are actually asking.

**The experiment (Lars, 2 Aug):** run diversions on **Tuesday and Saturday**, not just Saturday.
Tuesday = ground game (short, one thing to do this week). Saturday = long form (the map).

---

## The structural read — what two diversions actually does

Worth deciding on purpose, because the shape changes more than it looks:

1. **The capstone math changes.** Aug 3–9 ran three tributaries Mon–Fri. With two light days you
   get **four heavy weekdays**, so two or three tributaries maximum. That is fine, but it has to
   be chosen rather than discovered on Thursday.

2. **Make Tue and Sat one arc, not two tangents.** The strongest version pairs them:
   **Tuesday is the rep, Saturday is the training plan.** Tuesday hands the reader one small win
   this week; Saturday earns the bigger ask because they already had the win. Two unrelated light
   pieces would read as the feed losing its spine. One arc reads as deliberate design.

3. **The emotional shape improves.** Old rhythm: five heavy, one relief. New rhythm:
   hard (Mon) → relief (Tue) → constructive (Wed) → honest (Thu) → sharp (Fri) → relief (Sat)
   → synthesis (Sun). The heavy block never runs more than three days. This is probably the
   real argument for the experiment, more than the doom-fatigue one.

4. **Thread rotation is deliberately unbalanced.** As drafted, Shape of Work carries 3 of 7 slots
   (Tue, Thu, Sat). That is an overweight. Lars asked for it explicitly ("particularly like the
   shape of work themes that seem to be emerging"), so it is a choice — but name it, because the
   standing rule is to check rotation, and Ad Hoc Regulatory and Attack Surface each get one slot.

---

## ⚠️ The fork — capstone spine (cannot settle without the Aug 10–16 map)

Two viable spines. Which one wins depends on whether the 10–16 week already spends the
control/governor argument.

**Spine A (recommended if 10–16 stays off it): "The Window Just Changed Shape."**
The question stopped being *should I figure this out* and became *who do I help now that I have.*
Anchors: Mollick's agent guide reaching the non-early-adopter audience, Forward Deployed Engineer
+729% YoY as the market's own answer to "what does the Orchestrator look like on a job board,"
1.3M new roles, the archetype convergence. This capstone answers the question everyone is asking
him, and the answer is not a tool — it is a position.

**Spine B: "What Is the Governor, and Who Can Reach It?"**
The disclosure-layer / control-layer gap, straight off today's AI Signal. Heavier, and a direct
continuation of the sign / camera / governor ladder (31 Jul) and *Control You Can Locate* (5 Aug).
Better if 10–16 ran light on sovereignty; redundant if the 16th already capstoned on control.

**Note:** I could not find a week-plan file for 10–16 Aug anywhere on disk — only
`References\week-plan_2026-08-03.md` exists. If that map lives in a prior conversation rather
than a file, it is worth writing down, because this fork is gated on it.

*Below assumes Spine A, with Friday holding the governor argument as the bridge.*

---

## Mon Aug 17 — Nobody Can Triage 46,872 Bugs
- **Thesis:** AI-accelerated discovery broke the prioritisation heuristic. When the finder is a
  machine and the fixer is a human, "patch the criticals first" stops being a strategy and starts
  being a queue you never reach the end of. The answer is not faster triage. It is blast radius.
- **Material:** Chrome 149–151 — 1,072 bugs, then 370 more, **349 of them found by Google's own AI
  tooling**; more than the prior 23 updates combined. NVD at 46,872 CVEs in 2026, nearing 2025's
  full-year total.
- **The sharpest beat:** the vendor's own machine is outpacing the vendor's own humans. That is
  the whole story in one sentence, and it is not a Google problem.
- **Skeptic-proofing (do this early):** more bugs found is *good*. The piece is not "Chrome is
  broken." It is "the heuristic broke." Say so before a reader says it for you.
- **Thread:** AI Attack Surface → Trust Boundaries.
- **Callback:** *A Policy Isn't a Control. An Execution Rule Is.* (31 Jul) — sandboxing, least
  privilege and segmentation are exactly execution rules. Severity ratings are the sign.
- ⚠️ **Verify before draft:** the 46,872 figure and the "nearing 2025's full-year total" claim
  against NVD primary; per-release bug counts against Google's own release notes.

## Tue Aug 18 — DIVERSION #1 (ground game): Write the Brief, Not the Prompt
- **Register:** short, operational, one thing to do this week. Under 1,000 words on purpose.
- **Thesis:** The underrated skill surfacing in the hiring data is not prompt engineering as a
  job title. It is **specification precision** — writing a brief clear enough that an agent
  executes it without handholding. That is a management skill wearing a technical hat, and most
  readers already have the raw version of it.
- **The body:** what a brief actually contains — goal, constraints, definition of done, what to do
  when blocked, what not to touch. One worked example. Then the 20-minute rep.
- **Insider "we" is free here:** his own pipeline *is* a specification artifact. The editor panel,
  the morning brief config, the week plan — these are briefs an agent executes without him
  hovering. Show one. That is the piece nobody else can write.
- **Thread:** Shape of Work-to-Come · Practitioner.
- **Why it is the right ground game:** it is the smallest working unit of the whole
  architecture-of-work thesis, it is teachable in 800 words, and the reader can do it Tuesday night.
- **Hooks Saturday:** *you just wrote one brief; Saturday is the map for where that skill sits.*

## Wed Aug 19 — Open Weights From the House That Closed Them
- **Thesis:** OpenAI shipping Apache 2.0 reasoning models is the biggest structural shift in the
  local model market this year, and for regulated buyers it kills the last procurement objection:
  *we can't get a name-brand model on-prem.* Now you can.
- **Material:** gpt-oss-20b and gpt-oss-120b, 128K context, running on Ollama, vLLM, llama.cpp,
  LM Studio.
- **Print both readings, because both are defensible:** either they judge closed inference revenue
  safe from cannibalisation, or they are pulling the rug on Mistral and Meta. Do not pick one and
  pretend it is settled.
- **Thread:** AI Sovereignty (Model Sovereignty) · Ad Hoc Regulatory Regime.
- **Callbacks:** *Control You Can Locate* (5 Aug) and the Sat 8 Aug on-ramp ladder — **the ladder
  just got a new rung with a brand on it**, which is precisely what a procurement committee needs
  and a hobbyist does not. Also the *open weights ≠ open source* honesty caveat, already established.
- ⚠️ **Verify before draft:** licence text, parameter counts, context window, and any
  capability-parity claims. Do not repeat benchmark assertions as settled.

## Thu Aug 20 — The Roles Aren't Going. The Job Is.
- **Thesis:** "Impact and transformation, not elimination" is true — and it is only true *for the
  people who get to redefine the job.* Every field now has an opening for whoever figures out what
  the new version looks like. The honest question is who gets to be that person and who gets
  redefined at.
- **Material:** the Vantage sweep through finance, law, software and middle management.
- **The caution beat lands here:** Eliza Filby's trust-erosion argument (surveillance, shadow AI,
  "AI is really replacing human conversations," the generational split) is exactly what the
  optimistic transformation framing misses. Credit her by name. This is the piece she belongs in.
  ⚠️ verify the ~80% shadow-AI figure and pin her source before use.
- **Thread:** Shape of Work-to-Come + entry-ladder caveat.
- **Pattern:** same callback-and-correct move as Thu 6 Aug — the thread's own honesty beat, so the
  week is not four days of good news.

## Fri Aug 21 — The Governor and Who Can Reach It
- **Thesis:** Every lane shows the same gap. Article 50 requires labelling, not control. The OAIC
  sweep measures disclosure, not auditability. "Data in Frankfurt" is a disclosure claim, not a
  sovereignty guarantee. Open weights give you on-prem inference, not sovereign compute. The
  disclosure layer is fully built. The control layer is not. One procurement question closes the
  gap: **what is the governor, and who can reach it?**
- **Live hook (genuinely timely):** Article 50 landed 2 Aug. By the 21st there are roughly three
  weeks of *actual practice* to look at rather than an abstraction. That is the difference between
  this piece and every "here comes the AI Act" piece already written.
- **Thread:** Ad Hoc Regulatory Regime × AI Sovereignty. The bridge — hands Sunday its fight.
- **Callback:** sign / camera / governor (31 Jul). This is the governor argument turned on the
  regulators rather than the vendors.
- *(If Spine B wins, this becomes the Sunday capstone and Friday needs new material.)*

## Sat Aug 22 — DIVERSION #2 (long form): A Better Map, Not a Better Prediction
- **Register:** the weekend read. Long by design. Doom-relief through usefulness, not cheerleading.
- **Open:** both sides got the shape wrong. The catastrophists and the hype merchants were arguing
  about the same wrong axis, and a year of forecasts has been worth less than one accurate map.
- **Then give the map.** The archetype deck revisited with 2026 evidence underneath it: 1.3M new
  roles added, the wage premium for AI skills, up to 60% of new roles degree-free by 2030,
  FDE +729% YoY as the Orchestrator arriving on a job board. Organised as *here is where your job
  actually sits, and here is what the next version of it looks like.*
- **Close on the turn:** the useful move was never predicting. It is positioning. The window for
  "I should figure this out" is closing; the window for "I figured it out and now I help others"
  is opening.
- **Thread:** Shape of Work-to-Come · Diversions.
- **Pairs with Tuesday:** Tuesday was one rep. Saturday is the training plan. Reference it directly.
- ⚠️ **Numbers discipline:** today's brief carries a **28–56% wage premium**, which conflicts with
  the standing Aug 6 instruction to use **PwC 2026's 62%** as primary. Pin one figure and one
  source across Tue/Thu/Sat, or the week contradicts itself in public.

## Sun Aug 23 — Capstone: The Window Just Changed Shape
- Pulls Mon (the machine outpaced the humans triaging it), Wed (the tools arrived with a brand on
  them), Thu (the job is being redefined, by someone), Fri (nobody can point at the governor),
  and Tue + Sat (what you personally do about it).
- **Synthesis:** every lane this week shows capability arriving ahead of position. The gap is not
  technical any more. It is positional. What you do is take a position — the governor in your org,
  the brief in your team, the map for your function.
- **Why it earns the ending:** it is the direct answer to the question Lars is actually being
  asked, which makes it the least abstract capstone of the run so far.

---

## Accuracy watchlist
- NVD 46,872 CVE count + "nearing 2025 full-year total" — primary before Monday.
- Chrome per-release bug counts and the 349-found-by-AI figure — Google release notes, not secondary.
- gpt-oss licence / params / context / any parity claim — primary before Wednesday.
- Wage premium: **28–56% vs PwC 62%** — pin one, week-wide.
- Filby ~80% shadow-AI figure — verify and pin her source before Thursday.
- FDE +729% YoY — name the tracker, same discipline as the layoffs numbers.
- Article 50 practice as of 21 Aug — this is live news; draft late or carry an explicit "as of" line.

## Open items
1. **Aug 10–16 map is not on disk.** Needed to settle the capstone fork (A vs B) and to check
   whether the sovereignty thread is already spent going into the 19th.
2. Confirm the Tue/Sat pairing (rep → map) versus running them as two independent light pieces.
3. Confirm the Shape-of-Work overweight (3 of 7 slots) is intentional for this week only.
4. Decide whether Tuesday's diversion becomes standing structure or stays a one-week experiment
   — the answer probably depends on how Tue 4 Aug and Sat 8 Aug land.
