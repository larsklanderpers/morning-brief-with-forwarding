# AI LinkedIn Post - 1 November 2026
**Status:** Draft (review before posting)

---

The strongest AI data terms I have read this year were not written by a bank, a regulator or a Fortune 500 procurement team. A teachers' union negotiated them.

Today, Microsoft's AI safety and privacy standard for US schools takes effect. Any district can add it to an existing contract. Student and educator data cannot train models, with a narrow safety exception. It cannot be sold or used for advertising. There are third-party audits and a 72-hour breach reporting duty. Microsoft says the bans on training and data sales are permanent, and that deletion and breach duties continue after the contract ends.

Read that last part again. The obligations outlive the relationship.

Now hold that next to the other AI security story of the weekend.

Cisco Talos has documented an infostealer called VOLTA. It takes a victim's passwords, cookies, saved cards and tokens, compiles them into a report, and posts that report to a commercial AI model through an API. The model is asked to appraise the person: what are they worth, and how good is their security? If the model refuses, the malware tries the next one. Talos expects that kind of refusal resilience to become a standard design requirement.

Then consider a third item. Anthropic researchers had Claude write fine-tuning data designed to make a small model misaligned while passing a monitor similar to those used in production. Every run found data that did both. Each row looked harmless. The harm lived in the whole. The authors are careful to say this is a red-team game with the odds tilted, and not a finding about deployed models. I take them at their word. The lesson still travels.

I think these three stories belong together, because they sort AI safeguards into two piles.

The first pile is controls that ask. A model's refusal. A row-level content filter. A sandbox. A press line saying a provider will not train on your data. All of these are useful, and all of them are behaviours. Behaviours can be routed around, updated in a release, or changed when the company is sold.

The second pile is controls that bind. A contract clause with an audit right. A breach deadline. A ban that survives termination. These are dull, and they are slow to negotiate. They are also the only things on the list that you can enforce when the vendor has a bad quarter.

That matters more this month than it did last month. S&P has just moved Meta's outlook to negative over AI spending. OpenAI has cut the size of its round. The companies under your AI stack are being asked to show returns, and a company under that pressure looks hard at every asset it holds. Your data may be one of them.

For any business holding customer PII, whether under the Australian Privacy Act, GDPR or a sector regulator, most AI assurance I see rests on the first pile. That is no one's fault. The first pile is what vendors offer by default.

So here is what I would do this quarter.

Open your AI register and mark each safeguard as a behaviour or an obligation. If it is a behaviour, ask what enforces it and what happens when it fails.

Then take Microsoft's clause list into your next renewal, and see which ones your vendor strikes out. The strikeouts will tell you more than the security questionnaire did.

And where the data is sensitive enough that no clause would comfort you, keep it on infrastructure you control. A contract gets you damages after the event. Sovereignty means the event never had a route to you.

If a teachers' union can get these terms, what is your excuse?

#AI #PrivacyByDesign #DataSovereignty #LocalAI #GDPR #AustralianPrivacyAct
