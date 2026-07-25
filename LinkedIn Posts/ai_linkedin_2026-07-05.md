# AI LinkedIn Post — July 5, 2026
**Status:** Draft (review before posting)

---

Last week a US export decision turned two frontier AI models back on for the rest of the world.

Not a product launch. Not a price change. A memo. Anthropic's Fable 5 and Mythos 5 became globally available again because a government lifted a restriction it had earlier imposed.

Sit with that for a second, because it reframes a question most boards think they've already answered.

We've spent two years asking "which model is best?" That was always the wrong question for anyone holding regulated customer data. The right question is quieter and far more uncomfortable: *who decides whether you can use it, and where does your data go when you do?*

Three things happened in the last few days that all point at the same answer.

Anthropic's models were switched on globally by policy, not by the market — proof that model availability in your jurisdiction is now a government variable. OpenAI, preparing an IPO, is reportedly floating a US government equity stake. And Mistral, in France, is closing on a €20 billion valuation largely because "your data stays in the EU by default" has become something European buyers will pay a premium for.

Read together, they say one thing: the geography of AI — where the model lives, where it thinks, who governs it — has become part of the product. And regulators noticed before most executives did.

Here's the part that should be on a calendar, not a slide.

In Australia, from December 10 this year, organisations must disclose which personal information feeds their automated decisions and where those decisions are made largely by machine. The OAIC has already run its first compliance sweep. Maximum penalty: the greater of AUD 50 million, three times the benefit, or 30% of turnover. In April, APRA sent every regulated entity a letter naming four AI governance failures — a polite way of saying *we are watching, and we have a list.*

None of this required a standalone AI Act. The existing regulators simply scoped AI into the rules they already enforce. "There's no AI law yet" was never the reassurance people treated it as.

For years, the honest excuse for sending customer PII to a cloud model was capability: the good models lived in someone else's data centre, so that's where the data had to go. That excuse quietly died this year. Open-weight models now beat proprietary flagships on agentic benchmarks. A 27-billion-parameter model runs on a single GPU that costs less than a business-class flight. "We had to send the data offshore to get a capable model" is no longer true — and in about five months, an Australian regulator may ask you, in writing, to prove exactly which data left the building and where it went.

So the strategic move for anyone accountable for PII isn't to pick a better vendor. It's to treat *where inference happens* as a first-class architecture decision — the same way you already treat where data is stored.

Two clarifications worth internalising before December:

Data residency is a storage claim. Data sovereignty is a processing claim. The moment a prompt containing personal information hits a model, your data is being processed wherever that model runs — regardless of which region your database sits in. Vendors will keep selling the first as if it were the second.

If you do one thing this quarter, do this: map every automated decision that touches customer data, and trace the inference path — not the storage map — for each one. If any of those paths cross a border you can't defend, you've just found your December problem while you still have time to fix it.

Capability stopped being the constraint. Custody is the constraint now. Build like it.

#AI #DataSovereignty #PrivacyByDesign #LocalAI #GDPR #AustralianPrivacyAct
