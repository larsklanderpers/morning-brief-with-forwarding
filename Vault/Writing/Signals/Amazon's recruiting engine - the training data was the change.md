---
date_first_seen: 2026-08-16
date_updated: 2026-08-16
source: Dastin, J., Reuters, 11 Oct 2018
url: https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G/
brief: research
threads: ["Adoption and Change"]
beat: cautionary case
status: signal
used_in:
---

# Amazon's recruiting engine — the training data was the change

**What happened.** Reuters, original reporting, five anonymous sources. An Edinburgh team of ~12
built from 2014: **500 models**, one per job function and location, trained to recognise **~50,000
terms** from ten years of submitted résumés, producing a **1–5 star rating** explicitly modelled on
Amazon product reviews. One source: *"they literally wanted it to be an engine where I'm going to
give you 100 resumes, it will spit out the top five, and we'll hire those."*

The training corpus was overwhelmingly male. The system taught itself male candidates were
preferable: it **penalised the word "women's"** (as in "women's chess club captain"), downgraded
graduates of two all-women's colleges, and favoured verbs more common on male engineers' résumés —
"executed," "captured." Identified by 2015; Amazon neutralised those specific terms but could not
guarantee the system would not find other proxies; team disbanded by early 2017.

**Why it matters.** The usual reading is bias. The more useful reading for adoption is that the
organisation's own history was the input, and nobody treated it as a design decision. There was no
step in the process at which someone asked what ten years of résumés encoded — because "use our
data" felt like the safe, conservative choice.

**Three caveats that must travel with it.** (1) Amazon says on the record the tool **was never used
by recruiters to evaluate candidates**, and no candidate is known to have been rejected by it —
"Amazon's AI rejected women" is not what the article supports; Reuters does state Amazon did not
dispute that recruiters looked at the recommendations. (2) It failed **as much for returning
near-random results** — data problems meant unqualified candidates were recommended "almost at
random" — as for bias. The bias-only telling is a simplification. (3) It is eight years old and
describes 2014–2016 pre-LLM ML.

On-record voice worth keeping: John Jersin, then LinkedIn Talent Solutions VP — *"I certainly would
not trust any AI system today to make a hiring decision on its own."*

## Observations

- **2026-08-16** — first seen. Canonical URL now redirects; archive a copy before citing.

## Feeds

- [[Adoption and Change]]
