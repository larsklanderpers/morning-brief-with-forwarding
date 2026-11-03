# Research Note — Wednesday "Control You Can Locate" (four items)
For: draft Wed 5 Aug "Control You Can Locate" (Tributary 1, answer half) · Depth: deep · Date: 2026-08-01

## Bottom line
Both blocking items are now solid and primary-sourced, and one of them changes the piece. The France
84% is real and precise: the Autorité de la concurrence's **Avis 26-A-05 (17 July 2026)** found
**OpenAI, Google and Anthropic together hold more than 84% of the AI *agents* market** -- note the
scope, it's the agents layer, not foundation models broadly, which is actually perfect for this week.
The Altman quote is real (Relentless podcast, ~27 Jul), **but the outline's read of it was wrong and
would have misfired**: Altman's "liberty" is NOT deregulation/fewer-fences -- it's "distribute AI,
don't let a few control it," and he explicitly warns that "a small number of companies or countries"
controlling AI is "a new authoritarianism." The devastating, *honest* foil is the contradiction: he
names the exact disease the French regulator just measured (concentration), while OpenAI is one of
the three firms holding the 84% and keeps its models closed. He diagnoses the concentration and sells
you the symptom. "Control you can locate" (open/local) is the liberty he only talks about. OpenWorker
and the open-weights/open-source distinction are both solid.

## What's solid

- **France 84% -- PRIMARY, pinned.** Autorité de la concurrence, **Avis 26-A-05, 17 July 2026**,
  "relatif au fonctionnement concurrentiel du secteur des agents d'intelligence artificielle." The
  authority's own English release states: **"OpenAI, Google and Anthropic together holding more than
  84% of the market"** -- the **AI agents** market segment specifically. Other primary findings worth
  having: AI agents could redirect **20-25% of e-commerce traffic by 2030** (disintermediation); named
  concerns = self-preferencing, lock-in, capture of technical standards, reduced consumer choice.
  [autoritedelaconcurrence.fr EN press release + the full Avis_26a05 PDF]. **Use the precise scope**
  ("84% of the AI *agents* market," three named firms) -- a sharp reader will call "84% of AI."
- **Altman quote -- PRIMARY (podcast), pinned.** On the **Relentless** podcast (coverage 27-28 Jul
  2026): **"I think the fight of the current moment is: Are we going to head to a world of AI
  authoritarianism or liberty?"** His gloss on "liberty": **"We're going to empower them... let
  society express its ideas and use this technology in the way they want,"** and **"Every time that
  humanity has traded off its liberty for safety, it's been a long-term net loss."** He warns against
  **"a small number of companies or countries"** controlling AI -- "weird power concentration and kind
  of a new authoritarianism." [digit.in, AOL, Türkiye Today, RealClearPolitics -- multiple outlets,
  consistent wording]
- **OpenWorker -- SOLID (already in Lars's corpus).** Andrew Ng + Rohit Prasad, **MIT-licensed,
  local-first desktop AI coworker** that **returns finished deliverables** (documents, analyses, code)
  instead of chat; **35 app connectors; Ollama for local model inference; data stays on the user's
  machine** and only leaves through an explicitly chosen LLM provider. Launched **23 Jul 2026**.
  [MarkTechPost 23 Jul; `ai_brief_2026-07-26.md` + `ai_brief_2026-07-29.md`]. His own brief's take:
  "the first mass-market product to position 'data stays on your machine' as the primary feature."
- **Open weights =/= open source -- SOLID, standard distinction.** Open weights = downloadable and
  runnable yourself (no vendor kill switch, data stays local) but NOT full transparency /
  training-data / reproducibility, so not "open source" in the OSI sense. Widely established by 2026
  (OSI Open Source AI Definition; multiple explainers; "openwashing" critiques). Corpus policy cite:
  **Lawfare, "Knives Are Out for Open-Weight AI Models," 24 Jul** (already used in the 30 Jul piece).
  If you want a verbatim "=/= open source" line specifically, pull it from an explainer or confirm the
  exact Lawfare wording; the distinction itself is safe to assert.

## What's contested / watch out — READ THIS, it changes the foil
- **Do NOT frame Altman as "liberty = fewer fences / deregulation."** The primary shows the opposite:
  his liberty is about *distributing* AI and *preventing* a few from controlling it. Framing him as
  anti-regulation is a misframe a sharp reader (or any Altman follower) would catch, and it's the weaker
  attack anyway. **The stronger, honest foil is the gap between his words and his company:** he says
  don't let a few control AI; the Autorité just measured that OpenAI + two others hold 84% of the
  agents market; and OpenAI keeps its weights closed. He named the disease and is selling the symptom.
  That turn is unimpeachable because it uses *his own words* plus *a regulator's number* -- no
  caricature required. (Several outlets already flag the same contradiction re: OpenAI's closed models,
  so you're on solid ground.)
- **France scope:** it's the **AI agents** market (84% by three firms), per the Autorité -- not
  foundation models writ large. Precise scope only.
- **Altman air date:** coverage published 27-28 Jul; the exact episode date isn't cleanly pinned. Say
  "on the Relentless podcast, late July" rather than asserting a specific day. Ideally confirm against
  the episode itself before publish if you quote it tightly.

## The economics (control-is-a-spectrum honesty, per the Kimi rule)
Open/local is a hedge, not a free lunch -- keep the honesty that served "Bring the Model Home." A
frontier open model is still a ~1.4TB download you have to serve (real hardware, real money); but the
*bottom of the ladder is genuinely cheap and real now* -- OpenWorker + Ollama put capable local agent
work on a normal machine, data staying home, for the cost of the hardware you already own plus
whatever you spend on an optional hosted model. The point isn't "run frontier on your laptop"; it's
"the enforcing layer and your data can live where you hold the key," and the cost of getting onto that
ladder has collapsed. (This dovetails with Saturday's on-ramp ladder; don't overclaim frontier-local.)

## Drop-in facts (verbatim, sourced)
- **"OpenAI, Google and Anthropic together holding more than 84% of the market"** for AI agents.
  [Autorité de la concurrence, Avis 26-A-05, 17 Jul 2026]
- AI agents could redirect **20-25% of e-commerce traffic by 2030.** [same]
- Altman: **"I think the fight of the current moment is: Are we going to head to a world of AI
  authoritarianism or liberty?"** [Relentless podcast, late Jul 2026]
- Altman: **"Every time that humanity has traded off its liberty for safety, it's been a long-term net
  loss."** [same]
- Altman fears **"a small number of companies or countries"** controlling AI -- "weird power
  concentration and kind of a new authoritarianism." [same]
- OpenWorker: **MIT-licensed, local-first desktop AI coworker** (Ng + Rohit Prasad) that returns
  finished deliverables and keeps data on the machine (Ollama for local inference). [MarkTechPost, 23
  Jul 2026]

## Angles this opens
- **The spine writes itself:** Altman warns of concentration -> the French regulator *measured* it (his
  company + two others = 84% of agents) -> "control you can locate" (open/local, a harness you own) is
  the fix he names but won't ship. France stat and Altman quote interlock; you don't need to caricature
  anyone.
- **AU parallel for the clubs/APRA audience (in your own corpus):** APRA's 30 Apr 2026 letter already
  told regulated entities that single-vendor / offshore AI *concentration risk* is unacceptable and
  enforceable. So a French competition regulator and an Australian prudential regulator are converging
  on the same finding from opposite directions -- that's a strong "this isn't fringe" beat, and it
  lands the sovereignty thread on your regulated audiences.
- **OpenWorker = the "you can do this today" proof** for the harness-you-own
  ([[research_five-agent-engineering-paradigms]]): a local-first agent that returns deliverables with
  data staying home is exactly "the enforcing wall, where you hold the key," productised.
