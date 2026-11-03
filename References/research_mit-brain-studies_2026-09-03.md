# Research Note — the two MIT Media Lab follow-ons to Danry
For: Shape of Work-to-Come (no slot yet; candidate follow-on to Sat 5 Sep) · Depth: quick check ×2 · Date: 2026-09-03

## Bottom line

**One is real, footed, and comes with a do-not-print list written by its own authors. The other could
not be found anywhere except the AI summary that named it.** *Your Brain on ChatGPT* (Kosmyna et al.,
MIT Media Lab, arXiv, June 2025) is a 54-person EEG preprint with an 18-person fourth session that IS the
"second number" experiment -- the tool taken away -- and the authors have published the most explicit
plea against over-reading I have seen on any paper. *Socrates Went Nuclear* (2026) has a title and a
media.mit.edu URL and nothing I can reach: the page redirect-loops, it is not on the Fluid Interfaces
publications list, and no search surfaces an abstract. **Treat it as unverified until somebody has the
PDF.** The first is usable with the authors' own caveats carried verbatim. The second is not usable.

## What's solid

- **Kosmyna et al., "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant
  for Essay Writing Task." arXiv 2506.08872, posted 10 June 2025. PREPRINT** -- the authors' own FAQ:
  *"Peer review process has been already started, but we are in the very beginning of this process,
  and it will probably take months."* No funding: *"No, no funding to report for this study or the
  next one."*
  - **Design:** *"54 participants took part in Sessions 1-3, with 18 completing session 4."* Three
    groups -- LLM, Search Engine, Brain-only -- essay writing, three sessions each. **Session 4 swapped
    groups:** LLM-to-Brain and Brain-to-LLM.
  - **★ THE SECOND-NUMBER FINDING (session 4, n=18), verbatim:** *"LLM-to-Brain participants showed
    reduced alpha and beta connectivity, indicating under-engagement. Brain-to-LLM users exhibited
    higher memory recall and activation of occipito-parietal and prefrontal areas."*
  - **Connectivity across the three groups:** *"Brain-only participants exhibited the strongest, most
    distributed networks; Search Engine users showed moderate engagement; and LLM users displayed the
    weakest connectivity."*
  - **Recall of own work:** *"LLM users also struggled to accurately quote their own work"* and
    reported the lowest sense of essay ownership.
  - **The frame the authors want used:** *"Accumulation of Cognitive Debt"* -- their term, and the
    only one they endorse.
  [arXiv](https://arxiv.org/abs/2506.08872) · [authors' FAQ](https://www.brainonllm.com/faq)

- **★★ THE AUTHORS' OWN DO-NOT-PRINT LIST, verbatim from brainonllm.com/faq:**
  > *"Please do not use the words like 'stupid', 'dumb', 'brain rot', 'harm', 'damage', 'passivity',
  > 'trimming' and so on."*
  They also ask readers to avoid *"brain scans," "LLMs make you stop thinking," "impact negatively,"
  "brain damage,"* and *"terrifying findings."* And: *"the study has a list of limitations we list very
  clearly both in the paper and on the webpage"* -- *"one of the first protocols."*
  **This is a source writing its own accuracy sheet. It goes into the pipeline's do-not-print list as
  is.** Any draft that uses the study and any of those words fails the standing rules on the source's
  own terms.

## What's contested / watch out

- **n=18 in the session that matters.** The connectivity, memory and ownership findings across
  sessions 1-3 rest on 54; the tool-taken-away finding rests on **18 people, one session**. It is a
  real signal and it is a small one. Write "eighteen people" in the sentence, not "the study found."
- **EEG connectivity is not skill.** Reduced alpha/beta connectivity is a measure of neural
  engagement during the task, not of essay quality or later ability. The paper's own framing is
  "cognitive debt," which is a hypothesis about accumulation, not a measured decline in competence.
  Budzyń measured a competence outcome; Kosmyna measured an engagement proxy. Do not weld them.
- **It is the most over-read paper of 2025.** The FAQ exists because coverage ran "ChatGPT makes you
  dumber." A piece that cites it inherits that baggage and should say, in the sentence, that the
  authors themselves reject that reading. That is not a hedge; it is the story -- a preprint whose
  authors had to publish a plea against their own press.
- **Preprint, single institution, essay task.** Same population class as Danry and V&M: not
  professionals, not professional stakes.

## Couldn't verify

- Nothing outstanding. Socrates Went Nuclear was unverified at the first pass and is now footed at the
  PDF (below). The default-to-fabricated assumption was correct procedure and wrong in fact; the
  paper is real and was posted two days before Lars supplied it.

## ★★ UPDATE 3 Sep, later — SOCRATES WENT NUCLEAR, FOOTED AT THE PDF. Lars supplied arXiv 2609.00584v1.

**Clin Deffarges (ETH Zürich), Kosmyna & Maes (MIT Media Lab). arXiv 2609.00584v1, posted 1 SEPTEMBER
2026. Accepted to HAI '26, Osaka, 16-19 Nov 2026. PREPRINT. doi 10.1145/3841580.3841620.**
- **Design:** 50 participants (Full/unrestricted 17, Socratic 17, Adaptive 16), MIT campus, aged
  18-40, heavy AI users (30/50 daily). Domain: nuclear safety protocols, chosen as zero-prior.
  Ten-minute IAEA video → pre-test → 30-min AI-assisted training → immediate post-test. Muse 2 EEG
  throughout. Backend and grader: GPT-5.2. Three modes: (1) unrestricted ChatGPT-like bot;
  (2) Socratic bot that NEVER gives the answer; (3) no chatbot, EEG-adaptive sub-questions.
- **★ THE HEADLINE, verbatim (abstract):** *"The unrestricted chatbot produced higher learning gains
  (delta) than both constrained modes (p < .03, d > 0.80)."* Full Δ = 20.12, Socratic 10.52,
  Adaptive 11.20. Full vs Socratic t = 2.345, p = .025, d = 0.80. **Hypothesis H1 -- that the
  Socratic method leads to better learning -- was REJECTED.**
- **★★ THE AUTHORS' OWN INTERPRETATION, verbatim (§6.1):** *"the data and analysis of the bot
  discussions suggests that the success of the unrestricted AI is not evidence of deeper learning,
  but rather a result of the immediate post-test evaluation after the training phase."* And:
  *"Immediate testing favors retention of answers over understanding... The post-test followed the
  assessment session with no delay, so the experiment measures short-term recall rather than deep
  conceptual understanding or long-term retention."* And in the limitations: *"long-term retention
  was not measured."* Future work: *"a delayed post-test (one to two weeks after the learning
  session)."*
  **This is the two-outcomes argument stated by the authors of the study that produced it.**
- **Answer retrieval, measured:** *"52.9% of all exercise interactions in Mode 1 were classified as
  copy-paste question"* -- participants pasted the exercise into the chatbot and transcribed the
  answer. *"25.3% of Mode-1 final training answers were nearly identical to the chatbot text,
  against 0% in Mode 2."* Participant quote (P031): *"A bit like cheating, copy/pasting context,
  questions and answers."*
- **★ The Socratic mode failed for a specific reason and it is not "asking does not work":** people
  quit. *"most of the participants did not complete this process and 'gave up'."* Socratic EEG
  engagement fell to 0.297 by Q10, *"well below the 0.5 baseline."* **58% of Socratic exercises never
  reached the 80% mastery threshold.** Chatbot helpfulness: Full 8.62/10, Socratic 5.67/10
  (d = 1.75). Quotes: *"It felt annoying and frustrating"* (P035), *"Feeling almost crazy"* (P029),
  *"I just gave up"* (P014). Authors: *"this pedagogical path can only be beneficial if learners
  persist through the discomfort, which many did not."*
- **★ Null result on perceived learning (§5.6.1):** Full-mode participants, with nearly double the
  objective gain, *"did not perceive themselves as having learned more"* (p = .845). The people who
  did best did not feel they had learned -- and they were right, by the authors' own reading.
- **Adaptive mode (EEG-driven):** highest engagement (p = .018 vs Full) but learning gain no better
  than Socratic. Engagement and learning DISSOCIATED: *"mode 1 participants achieved high deltas
  with low engagement by transcribing AI answers."*
- **⚠️ LIMITATIONS, the authors' own, all of which travel:** GPT-5.2 graded with no inter-rater
  reliability recorded (*"grading validity comes first"*); single domain, factual knowledge; 30-min
  session may penalise Socratic; 16-17 per arm, no subgroup power; interest in the topic not
  measured; Hawthorne. And it is a **preprint posted 1 Sep 2026** -- two days before this note.
- **The relation to Everett:** same shape, independent domain. Everett: answer-first 85 > attempt-first
  82 on immediate diagnostic accuracy, physicians. This: answer-available 20.1 > Socratic 10.5 on
  immediate recall, students. **Two studies, two populations, two domains, one direction on the
  immediate measure -- and only one of them (this) says in text that the immediate measure is the
  reason.** That is not a coincidence to explain away. It is the second number, unmeasured, twice.

**What this does to Sat 5 Sep:** it goes IN. Not as a reach -- it is the thesis, footed, posted this
week, with the authors making the argument themselves. One paragraph block after Everett in "The
number everybody measures," carrying: the 20-vs-10, the authors' immediate-post-test line, the
copy-paste rate, and the gave-up finding as the reason "just use a Socratic tool" is not the answer.
Preprint and n stated in text. Kosmyna (EEG, n=18 in the session that matters) stays OUT -- it is an
engagement proxy and the piece has enough.

## The economics

None directly. The cost framing that fits: Kosmyna's session-4 swap is the only experiment in this
whole set that priced the second number by design -- it made people do the task without the tool
after doing it with -- and it cost them an 18-person session to get one reading. Everett, with 70
physicians and an RCT, did not price it at all. The expensive measurement is the one nobody funds.

## Drop-in facts (each with a source)

- 54 participants, three groups (LLM / search / brain-only), three essay sessions; 18 completed a
  fourth session with the groups swapped. -- Kosmyna et al., arXiv 2506.08872, 10 Jun 2025, preprint.
- *"LLM-to-Brain participants showed reduced alpha and beta connectivity, indicating
  under-engagement."* (n=18) -- same.
- *"LLM users also struggled to accurately quote their own work."* -- same.
- The authors' own request: *"Please do not use the words like 'stupid', 'dumb', 'brain rot',
  'harm', 'damage', 'passivity', 'trimming' and so on."* -- brainonllm.com/faq.
- Unrestricted chatbot Δ 20.12 vs Socratic 10.52 vs EEG-adaptive 11.20 (n=50, MIT, nuclear safety, immediate post-test); authors: the unrestricted result is "not evidence of deeper learning, but rather a result of the immediate post-test"; 52.9% of unrestricted interactions were copy-paste; 58% of Socratic exercises never reached mastery -- "I just gave up." -- Clin Deffarges, Kosmyna & Maes, arXiv 2609.00584, 1 Sep 2026, preprint, accepted HAI '26.

## Angles this opens

- **A follow-on to Sat 5 Sep, not an addition to it.** "The second number" now has three studies at
  three altitudes: Budzyń (competence, specialists, months), Kosmyna (neural engagement, students,
  one session), Danry (discernment, lay adults, one session). A later Shape of Work piece could run
  them as a ladder of what "skill without the tool" even means -- and the honest finding is that the
  only competence-level measurement is the one from Poland.
- **The authors'-own-do-not-print is a reusable beat for the Sat 29 register.** A source publishing a
  list of words it does not want used about itself, because the press used all of them anyway, is the
  primary-is-quieter-than-the-secondary pattern with the primary shouting back. Bank it.
- **Danry → Kosmyna is the same lab, three years apart, same question** (does being told switch off
  the search?), moving from a behavioural proxy (perceived information insufficiency) to a neural one
  (connectivity). If Socrates Went Nuclear is real, it is the third rung. Confirm before building on it.
