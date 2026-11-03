# PerthSEC 2026 — submitted text
Submitted: 4 September 2026 (confirmed by Lars). Form: https://aisasecuritydays.com.au/perthsec-cfs

> ⚠️ **THIS FILE IS INCOMPLETE AND MUST BE FIXED.**
> The text below is the final drafted version plus the edits Lars stated he made.
> **It is not verified against what was actually pasted into the form.**
> Lars made at least one edit in-form (the regulator wording) and may have made others.
>
> **TO DO:** paste the actual submitted text over this, add the exact timestamp, and
> attach the confirmation screenshot to this folder. Until then this is a reconstruction,
> not a record — which is exactly the failure mode this folder exists to prevent.

---

**Session style:** Session (40-minute concurrent), individual speaker
**Stream:** 1 — Strategic Leadership: Leading Through Rapid Change (+ Stream 2 if multi-select was available)

## Title
The Control Was on the Register. It Was Not in the System.

*Alternate offered, not used: "Six Weeks of Controls, One Dependency, and Nothing on Fire."*

## Abstract (~410 words)

We spent six weeks building the controls that govern our AI coding agents. Deny rules, approval structures, the things you would put on a control register and describe to a board. Then we found that design decisions in the infrastructure underneath allowed all of them to be bypassed.

Nobody attacked us. There was no breach, no incident call, nothing to restore. That is the part worth sitting with. The controls stopped being controls quietly, because of a dependency we did not own and had not thought to examine, and every report saying they were in place stayed technically accurate the whole time.

This is a supply chain story wearing an AI costume. Your AI controls sit on infrastructure somebody else designed, and their validity is a function of decisions you did not make and will not be told about.

This failure mode is not yet in anybody's third-party review playbook, and the four tests at the end are what we built because we could not find an existing one that caught it.

It comes with a second failure that makes the continuity question concrete. One accidental line in a configuration file skewed everything our agents produced for over a week. Nothing alerted, because nothing had failed. I would ask any board reading this how long a silent degradation could run in their environment before somebody noticed -- and what, specifically, would do the noticing.

A week used to be a reasonable amount of time to notice something. It is not any more. The distance between a weakness existing and somebody using it has collapsed toward zero, and the sequence most security programmes are built on -- detect, triage, escalate, convene, decide -- no longer fits inside the window. That is what turns a decorative control from an audit finding into an exposure. When the clock was long, a control that existed only on paper was something you would get to. When the clock is short, it is the thing that was supposed to hold, and did not.

Aviation worked this out after a run of accidents that began not with mechanical failure but with a crew who were capable, and deliberating, when they needed to be executing. So the question I would put to a board is not how fast can we respond. It is what have we already decided, and can you point at the thing that will carry out the decision without us.

The session ends where a regulator would start. When you are asked to evidence that a control was operating effectively across a period, a policy document is not evidence and a log of approvals is barely better. I will set out the four questions we now ask before we will put anything on a register and call it a control.

## Key takeaways (~146 words)

1. The four questions to ask before accepting that an item on your AI control register is actually a control — applied live to an agent approval gate, a dependency automation pipeline, and a loyalty reconciliation, on a one-page test you keep.

2. Why a control you built and tested can be quietly invalidated by a third-party dependency you never assessed, and what that adds to your third-party review that isn't in it today.

3. What evidence of effective operation looks like for an AI control, drawn from twenty years of producing exactly that kind of evidence under a financial-crime/AML/organised-crime regulator — and why most current AI governance reporting would not survive the request.

4. The decisions worth making before an incident rather than during one, because the sequence most programmes rely on — detect, triage, escalate, convene, decide — no longer fits inside the window.

## Bio
See `../../Bios/bio-long-first-person.md` (long, first person, ~270 words).

## Run of show — 40 minutes

| Min | Beat |
|---|---|
| 0-3 | The register line, stated flat. We had the controls. They were on the register. They were not in the system. |
| 3-9 | What we built and why we believed it. Enough architecture to earn trust, not enough to lose the room. |
| 9-15 | The bypass, and the moment it stopped being an engineering problem: the dependency was not ours. |
| 15-21 | The supply chain argument. Your controls inherit somebody else's design decisions. What that means for third-party review. |
| 21-27 | The second failure. One config line, a week of drift, nothing alerted. The continuity question put to the room. |
| 27-34 | The four questions, run live against three real systems. Hand out the one-pager. |
| 34-38 | The evidence problem. What a regulator asks for, and what most AI governance reporting would produce. |
| 38-40 | Close. Two short paragraphs, resolved line first. |

## Constraints to carry into the deck
- Mandatory AISA PowerPoint template, provided after the speaker agreement is signed
- **No vendor or company logos on any slide** (Guideline 14) — Player Elite appears nowhere in the deck
- Vendor neutral; no product focus; no disparaging named competitors
- 40 minutes **including** Q&A
- No speaker substitution permitted after acceptance
- AISA does not fund travel or accommodation
