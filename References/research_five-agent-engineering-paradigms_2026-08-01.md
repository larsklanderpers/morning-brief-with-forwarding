# Research Note — The Five Agent-Engineering Paradigms (Prompt / Context / Harness / Loop / Graph)
For: Tuesday "Tooling People Up" (loop/graph aside) + reusable corpus context · Depth: deep-ish · Date: 2026-08-01

## Bottom line
All five terms are real and individually well-sourced -- each is an established or fast-crystallizing
discipline with its own ecosystem, and "loop engineering" / "graph engineering" in particular are
legitimate 2026 terms (the skeptic seat's earlier doubt was stale). What is NOT yet a settled,
canonical named taxonomy is the neat "five paradigms in five years" *packaging*: that clean
progression is largely the framing of the one article Lars found (todayforai, 25 Jul 2026), even
though the individual terms and the rough arc are broadly recognized. So: present each term as real;
present "the five paradigms" as the useful way people are now framing it, not as settled industry
canon. The standout for Lars is **Harness engineering** -- it is, almost word for word, Monday's
"a sign is not an execution rule" argument in the field's own vocabulary: the harness is the wall
that actually *enforces*, and Monday's `--yolo` disaster is what a disabled harness looks like.

## What's solid — the five, with dates, definitions, confidence
- **Prompt engineering (2022)** -- crafting/tuning instructions within a single turn (few-shot,
  chain-of-thought) to steer model reasoning. Baseline layer. **SOLID / universal.** [todayforai]
- **Context engineering (2025)** -- managing everything the model perceives *beyond* the prompt:
  RAG retrieval, short- and long-term memory, dynamic tool definitions, session history, all inside
  a token budget (sliding-window compression, context pruning). **SOLID** (widely used by 2025-26).
  [todayforai; broad usage]
- **Harness engineering (Feb-Mar 2026)** -- the "**Agent = Model + Harness**" layer: the runtime
  *around* the model that sets tool access, permissions, sandboxes, approvals, retries, logging,
  and evals, and enforces deterministic evaluation + authorization *before* an agent action
  executes. **SOLID** -- multiple independent sources: todayforai; Louis-Francois Bouchard
  ("Harness Engineering: The Missing Layer," 25 Mar 2026); NxCode; Augment Code; the
  `ai-boost/awesome-harness-engineering` GitHub list; balancedsec. This is the security-boundary
  layer.
- **Loop engineering (June 2026)** -- designing autonomous iterative cycles: **Plan -> Execute ->
  Verify -> Evaluate/Repair**, with maximum-retry and budget limits to prevent infinite loops.
  **SOLID (fast-moving)** -- explainx.ai, IBM (think/topics/loop-engineering), LangChain ("The Art
  of Loop Engineering"), GitHub cobusgreyling/loop-engineering, claude.com.
- **Graph engineering (July 2026)** -- organizing multiple single-responsibility agent loops into
  **directed-graph topologies** (nodes = agents/tools/human checkpoints/evaluators; edges = control
  flow + dependencies; shared-state "blackboard"), to decouple complexity and add parallelism.
  Frameworks: **LangGraph, AutoGen GraphFlow, Google ADK 2.0**. **SOLID (newest, crystallizing)** --
  aibuilderclub, truefoundry, Analytics Vidhya (Jul 2026), smartscope.

**The stack, verbatim (this is the line Lars is paraphrasing -- it's the article's own):**
> "Prompt provides instruction baselines, Context delivers data support, Harness establishes
> security boundaries, Loop enables autonomous iteration, and Graph accomplishes complex system
> decoupling." [todayforai, 25 Jul 2026]

## What's contested / watch out
- **"Five paradigms in five years" as a canonical taxonomy = one article's synthesis.** The arc
  (prompt -> context -> harness -> loop -> graph) is a clean narrative from todayforai; it is a
  *good* framing and each rung is real, but do not assert "the five paradigms" as an
  industry-standard named canon. Safer: "the way the field is now stacking it," or "five layers
  people have started naming." Lars adopting the framing is fine; presenting it as settled is a
  reach a sharp reader could poke.
- **The month-by-month dates** ("harness Feb 2026, loop June, graph July") are the article's
  periodization. Fine as narrative color; don't state them as hard historical fact.
- **Loop/graph are weeks-old as *named* disciplines** and moving fast -- re-check before leaning
  hard on any specific framework claim in a later piece.

## The human's role — Lars's overlay, and it's a real gap he fills
Neither todayforai nor Bouchard frames these around human oversight; the whole taxonomy is
engineering-first (constraints, determinism, topology). That is exactly the lens Lars adds. Across
the stack the human moves OFF the per-turn keystroke and UP into: writing the prompt/spec, curating
the context, **setting the harness's permission boundaries**, defining the loop's goal + verification,
and sitting as the human-checkpoint node in the graph. So Tuesday's "stay in the loop" double meaning
is well-founded: you are not in the loop typing each prompt -- you are the one who decides where the
loop points and what "done" means. The article's silence on the human is the seam Lars writes into.

## The Harness angle (highest value — ties straight to Monday)
Harness engineering is Monday's thesis in the field's own words. Two independent sources say the
quiet part:
- todayforai: **"Prompt-level restrictions are soft constraints that models may violate during
  multi-step reasoning or under adversarial inputs. Even with well-crafted prompts, lacking
  architectural isolation cannot prevent agents from executing unauthorized, high-risk system
  operations."**
- Bouchard: reliable systems need **"environments that expose failures, enforce boundaries, preserve
  progress"**; "better prompts can help, but" the constraint has to be architectural.
That is precisely "a sign is not a governor; a policy is not an execution rule" (Fri 31 Jul) and the
`--yolo` beat (Mon 3 Aug): the approval prompt was a soft constraint; the *harness* is the enforced
boundary, and turning off `--yolo` is disabling the harness. **A future cyber piece basically writes
itself: "The Harness Is the Wall That Holds" -- the constructive answer to Monday's "Nothing Held."**

## Drop-in facts (verbatim, sourced)
- "**Agent = Model + Harness**": the harness is everything around the model -- "the tools it can use.
  The permissions it has. The state it carries forward. The tests it has to pass... The retries,
  checkpoints, guardrails, reviews, and evals." [Bouchard, 25 Mar 2026]
- Harness engineering is "the work around an AI agent that makes its behavior inspectable, testable,
  and constrained." [Bouchard]
- "Prompt-level restrictions are soft constraints that models may violate... lacking architectural
  isolation cannot prevent agents from executing unauthorized, high-risk system operations."
  [todayforai, 25 Jul 2026]
- Loop = Plan -> Execute -> Verify -> Evaluate/Repair, bounded by retry + budget limits. [todayforai;
  corroborated IBM, LangChain]
- Graph = single-responsibility loops wired as nodes/edges over a shared-state blackboard; frameworks
  LangGraph, AutoGen GraphFlow, Google ADK 2.0. [todayforai; aibuilderclub]

## The economics / complexity discipline (light, but on-brand)
The article's own practical guidance is a cost-control rule Lars will like: **don't over-engineer.**
"Simple structured extraction and Q&A only require optimizing Context and Prompts; complex automation
involving file writes and code modifications demands Harness isolation and Loop verification first."
i.e. match the paradigm to the job; a graph you don't need is gold-plating. [todayforai]

## Angles this opens
- **Harness = the constructive sequel to Monday.** Monday said nothing held; the harness is the
  layer that *does* hold. Strong future Cyber / Trust Boundaries piece, and it folds the Friday
  execution-rule piece and Monday's `--yolo` into one named concept the field already uses.
- **The five-layer stack as a "Shape of Work" backbone:** the human's job moves up the stack as the
  machinery matures -- prompt-writer -> context-curator -> boundary-setter -> goal/verifier ->
  orchestrator. That is the Tuesday thesis ("management is the superpower") mapped onto the
  engineering ladder.
