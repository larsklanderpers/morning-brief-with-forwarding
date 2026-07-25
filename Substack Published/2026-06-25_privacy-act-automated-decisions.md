# Your Algorithm Makes Decisions. Come December, Your Privacy Policy Has to Say So.

The delegation of decisions to algorithms has been one of the quietest shifts in Australian business over the last five years. Not a transformation program. Not a technology initiative. Just a slow, organisation-by-organisation handover of choices — about who gets a loan, who makes the shortlist, who pays what premium, whose claim gets prioritised — to systems that neither sleep nor second-guess themselves. While this hasn't come knocking for clubs in particular yet, it certainly has for every member or customer you service — and in most cases, the implied algorithm impacts whether they even walk through the door.

For clubs, most operators are constantly trying to do more with the same staff or less, and continue to deliver an experience that excites and amazes for members — and particularly members whose loyalty most affects the club's financial health and well-being. Letting the algorithm make the decision has become the underlying de facto status quo, whether we recognise it or not.

For enterprise of all shapes and sizes, this generally wasn't done deliberately. They chose to be more efficient. At the same time, they chose to be more impactful. The algorithm was the means, not the end. And so the decision-making quietly moved, and nobody updated the documentation, and nobody told the customers, and the humans who nominally reviewed the recommendations found themselves approving 40 in an hour — which is effectively the same as approving none at all; or reviewing hundreds of compliance documents or interaction reports a week, which is the same outcome made large for operations with less than 1 million customers.

On 10 December 2026, Australia's Privacy Act calls out companies for allowing this and not telling anyone it's happened. We have all been given six months to clean up our act — or at least get radically more transparent about what we are doing behind the scenes — or pay the price. The first criteria (APP 1.7) describes pretty much every modern business, even cafes. The third (APP 1.9) is the one with the most impact for the way we operate — it's in many ways even tougher than 10.1.(i) from a compliance perspective.

---

## What the Law Actually Says

The Privacy and Other Legislation Amendment Act 2024 inserts three new obligations into APP 1 — the transparency principle — and they all take effect at once.

**APP 1.7** is the trigger. If your organisation uses a computer program on personal information to make — or directly support — a decision that could reasonably be expected to significantly affect an individual's rights or interests, you're in scope.

**APP 1.8** is the obligation. You must update your privacy policy to disclose: what kinds of personal information go into the system, what decisions are made solely by automated means, and what decisions are substantially automated — even where a human technically has final sign-off.

**APP 1.9** defines "significantly affects" to include decisions that grant or refuse benefits, affect contractual rights, or affect access to significant services. Both adverse *and* beneficial decisions count.

The most consequential word in the framework is "substantially." A human clicking approve on an algorithm's output is still, under this law, a substantially automated decision. The obligation was written precisely to capture that scenario.

Read that again. Your approval step doesn't get you out of scope. It gets you into the harder conversation about what your approval step actually means.

---

## The Appearance of Oversight

Here's the pattern this law was designed to address.

An organisation deploys an AI model — for loan assessment, CV filtering, insurance pricing, fraud scoring, customer segmentation. The model produces a recommendation. A human reviews it. The organisation tells itself it has human oversight. It tells its board it has human oversight. It may even believe it.

What actually happened: a person confirmed a machine's judgement in a window too short to interrogate it, on data they didn't independently gather, using logic they can't explain. That is not oversight. That is what oversight looks like when you're trying to move 40 decisions an hour. And this is exactly the kind of thing that you both need to do to comply with FINRA/AUSTRAC and the kind of thing that will burn you under this act if you don't ensure you have the right human-in-the-loop for all those decisions, as well as substantially documented evaluatory statements about each decision. In other words, the paperwork you need to comply with the new regulation is the same as the paperwork that will be used to audit you to make sure you comply with the older, more established money laundering regulations. It's no longer a case of "damned if you do, damned if you don't" — it's now a case of "damned if you do without the right documentation, and double-damned in any other situation." For clubs, in particular, the OAIC is the ruleset, and while there will be particularly broader enforcement of this, in the immediate term window, AUSTRAC is the hammer — not only because it has current expectations, but also because failure to meet the current expectations will be used to trigger an audit on historic performance.

The OAIC has been explicit: substantially automated decisions include those where there is no meaningful human involvement in the decision process for each individual case. The emphasis is on *meaningful* and *individual*. Batch approvals, threshold queues, and score-based workflows all count.

It's the old IT security audit dynamic — "yes, we have a change management process" — while everyone waves everything through at 4pm on Friday. The process existed. The control did not.

---

## The Broader Pattern

Businesses have always wanted the benefits of efficiency without the friction of accountability. That's not cynical — it's rational. Automation exists precisely because human attention is finite and expensive.

Enterprise technology adoption follows the same arc almost every time. A new capability arrives. Organisations adopt it for its efficiency gains. The governance frameworks trail behind — sometimes by years. At some point, a regulator, a court, or a breach forces the accountability conversation that should have happened at the start.

AI-assisted decision-making is following that arc exactly. The capability arrived. Organisations adopted it quietly. The governance is now arriving — starting with transparency, which is the least invasive version of accountability imaginable.

The OAIC isn't asking you to stop using AI to make decisions. It's asking you to say that you do.

If that disclosure feels uncomfortable, the discomfort is telling you something.

---

## What's Actually In Scope

The definition is deliberately technology-neutral — AI models, rule-based scoring tools, algorithmic pricing engines, and automated assessment systems are all captured. If a system makes a systematic distinction between individuals based on personal information, and that distinction materially affects those individuals, it's in scope.

Things that are clearly captured:

**CV or application screening** that filters, ranks, or scores candidates before a human sees the shortlist.

**Credit scoring or loan eligibility** determination — even where a broker nominally reviews the score.

**Insurance underwriting or premium pricing** built on individual risk modelling.

**Customer risk segmentation** or fraud flagging that determines service terms or access.

**Dynamic pricing** that produces materially different offers to different customers.

**Clinical decision support** that significantly shapes a treatment pathway or referral decision.

The common thread: a system made a distinction between people without a human deciding each individual case on its own merits. If that sentence describes any part of your operation, you are in scope.

---

## The OAIC Is Not Waiting

The December obligations are six months away. The OAIC's enforcement posture changed six months ago.

In January 2026, the regulator launched its first-ever proactive compliance sweep — targeting roughly 60 organisations across real estate, pharmacy, car rental, licensed venues, and automotive. Not responding to complaints. Going looking.

That sweep covers existing privacy policy obligations — not even the new ADM rules yet. Penalties at this stage reach $66,000 for transparency failures. When December's obligations take effect, that enforcement capability is already operational and already pointing at your sector.

The OAIC is expected to publish specific ADM guidance in September 2026. Organisations that wait for that guidance before starting will have three months to close a gap that should take six.

---

## What Needs to Happen Before December 10

Three things, in the order that matters.

**Start with operations, not legal.** Map every system in your organisation that processes personal information and produces a decision, score, ranking, or recommendation about a customer, employee, applicant, or counterparty. Don't begin with your legal team's view of what counts. Begin with your engineering and operations teams' list of what actually runs.

**Classify honestly.** For each system: does this significantly affect someone's rights or interests? Does a human make a genuine individual decision, or does the algorithm determine the outcome? Is the human review meaningful, or is it a throughput exercise?

**Update your privacy policy — specifically.** The law requires disclosure of the *kinds* of personal information used and the *kinds* of decisions made. It does not require you to expose your model architecture. "We use an automated credit scoring system that processes identity, income, and employment data to assess loan eligibility" is the kind of plain-language statement the obligation is designed to produce. If you can't write that sentence for each in-scope system, that's the gap.

---

The Privacy Act's automated decision-making reforms are, at their core, a transparency measure. They don't prohibit AI from making decisions. They require you to stop pretending it isn't.

For clubs, the calculation is starker than for most. You already operate under AUSTRAC's expectation that you know who your members are, what decisions you're making about them, and why. The December obligations don't add a new burden — they reveal that the burden was already there, and the documentation wasn't keeping pace.

The organisations that treat December 10 as an opportunity to close that gap — rather than a deadline to scramble past — will be the ones that sail through the AUSTRAC audit that follows. The ones that don't will find that one regulator's finding becomes another's trigger.

If your algorithm is making decisions, your privacy policy needs to say so.

And if you're not sure whether it is — that's your answer.

---

*Sources: [Privacy and Other Legislation Amendment Act 2024](https://www.legislation.gov.au/); [Landers & Rogers — Australian Privacy Law Update 2026](https://www.landers.com.au/legal-insights-news/australian-privacy-law-update-what-app-entities-need-to-know-in-2026); [vocarelaw.com.au](https://vocarelaw.com.au/not-for-profits-charity/privacy-act-automated-decision-making-amendments-2026/); [Liquid.Digital — December 2026 Privacy Deadlines](https://liquid.digital/the-december-2026-privacy-deadlines-a-practical-guide-for-australian-businesses/); [MinterEllison — OAIC Compliance Sweep](https://www.minterellison.com/articles/oaic-ramps-up-privacy-enforcement-are-you-ready); [OAIC — Consultation on ADM Guidance](https://www.oaic.gov.au/engage-with-us/consultations/consultation-on-guidance-for-transparency-in-automated-decision-making); [NSW Registered Clubs Act 1976](https://legislation.nsw.gov.au/view/html/inforce/current/sl-2015-0479)*

*Lars Klander writes about AI strategy, data privacy, and the governance of intelligent systems.*
