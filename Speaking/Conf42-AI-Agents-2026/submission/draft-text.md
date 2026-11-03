# Conf42 AI Agents 2026 — submission draft
**Status: NOT SUBMITTED.** Closes **9 September 2026**. Event 23 September 2026, online.
Submit at: https://cfp.ninja/e/conf42-agents-2026 (sign in with GitHub or Google, free)

> Note: Conf42 DevSecOps 2026 closed 31 Aug and was missed. AI Agents is the better home for this
> material anyway — agent permission architecture is the whole event rather than a corner of it.

## Form settings
- **Format: Talk** (NOT Keynote — keynotes go to Diamond sponsors)
- **Duration: 30 minutes** (deliver ~24 min of video; that is the house norm)
- **Level: Intermediate**
- **LinkedIn: https://www.linkedin.com/in/lars-klander-aa393a6/** — regex-checked by the form; must be the full URL, and must be the current profile, not Tech Results

## Title
Deny Rules Are Not Controls: Six Weeks of Agent Guardrails and the Bypass Underneath Them

## Abstract

Two of us spent about six weeks building the permission layer for our coding agents. Deny rules, approval structures, execution rules, the lot. Then we found that design flaws in the infrastructure underneath allowed all of it to be bypassed.

This is the postmortem. What we built, why we believed it held, how we found out otherwise, and what we changed.

It comes with a second failure that was quieter and, in some ways, worse. One accidental line in an onboarding configuration silently skewed every piece of code our agents produced for over a week. Nothing alerted. Nothing failed. The system was behaving exactly as designed, against an instruction I did not know was there, and it took me days to work out why the output kept drifting from our standards. No request log in our stack would ever have shown it, because the requests were all fine.

Both failures share a shape, and it is the shape most agent deployments are currently in: the control was written down, the control was reviewed, and the control was not where we thought it was.

What I took away, and where this talk ends, is a set of four tests I now run before calling anything a control. A policy is a sign. A log is a camera. Only an execution rule is a governor. We had built a great many signs.

Takeaways: the specific failure modes to test for in an agent permission layer; why instruction-layer contamination is invisible to request logging; and the four questions that separate a real control from a documented feature that has acquired a control's reputation.

## Bio
Use `../../Bios/bio-med-third-person.md` (~125 words, third person).

## Speaker notes (private field — organisers only)

This is a first-hand postmortem from my own production environment, not a survey or a framework talk. Two specific incidents, both ours, both told against myself.

I'm a first-time conference speaker, so if there's anything in the recording spec or the process I should pay particular attention to, I'd rather be told early than get it wrong. Happy to deliver ahead of deadline.

No product content — the company is named in the bio as context for the regulated-environment angle and does not appear in the talk.

---

## Why the abstract is incident-first
Conf42 screens for "sales pitches, especially reused ones," and a founder/CTO is pre-suspected. A framework-first abstract reads as thought leadership; an incident-first one reads as a postmortem, which is what their CFP explicitly asks for. The four tests land harder at minute 26 as the thing the failure forced him to invent than in paragraph one as an assertion. **Lars has not yet ruled on this ordering — flag for his review.**

## If accepted — five questions to send on day one
Conf42 publishes no recording guidelines; the pack arrives after acceptance.
1. Exact video delivery deadline and upload destination
2. Required resolution, frame rate, codec, max file size
3. Preferred framing — slides full-frame with webcam PiP? Slide template mandatory?
4. Is there a review pass, and can a corrected cut be resubmitted?
5. **Will I receive the final edited master, and may I re-upload it to my own channel and site?**

Q5 matters: Conf42's public terms contain **no speaker content licence**, and clause 9.1 asserts they own event materials. Embedding their YouTube video is safe and intended; re-uploading a copy is not covered by anything published. Get the line in writing before recording.

## Expectations
Conf42 averages roughly 68 views per video. This is credential manufacturing, not audience building — it produces the recorded-talk artefact that no other CFP can currently be given. The audience is on Substack; drive traffic there.
