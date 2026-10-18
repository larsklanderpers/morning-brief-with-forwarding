# AI LinkedIn Post - 18 October 2026
**Status:** Draft (review before posting)

---

Anthropic just told us how many hours a week its engineers would need to read everything their AI agents write.

424.

That is not a typo, and it is not a competitor's smear. It is in Anthropic's own study of its own workforce, published this week. By August, the agents its staff direct were working six hours for every human hour. Even the non-technical teams would need more than half their week just to read the output.

Sit with that if you run a business that holds customer data.

Every piece of agent output nobody reads is a decision nobody reviewed. In most companies that is a productivity story. In a company with PII obligations, it is a compliance story. You cannot demonstrate a control over something no human looked at.

Now put a second story next to it.

This week Meta quietly folded new language into its commercial terms. Lawyers who read it said it could let Meta use content from any business account's website to train its products, with no opt-out, accepted simply by continuing to use the tools. After journalists flagged it, Meta removed the language and said it only ever meant ads products.

Notice how that one got caught. Someone read the terms.

Here is the uncomfortable symmetry. The risk is the same in both stories: things that matter, written somewhere, that nobody has time to read. Agent output on one side. Vendor terms on the other. Both are growing faster than human attention.

And the default context windows keep growing too. When a model takes half a million tokens by default, an entire customer file fits in one careless paste.

So what actually holds when nobody can read everything?

Not more reading. Architecture.

First, put the data where the model is, not the other way round. This week NVIDIA shipped a 74-billion-parameter-class open model designed to run on a single 24GB card, and Liquid AI released a model with about two billion active parameters built for on-device agents. On-premise AI used to be a capital request. It is becoming a line item. Check the licence file yourself before legal signs off.

Second, enforce data rules at the one place every agent call has to pass: the gateway. A policy in a PDF does not stop an agent. A gateway that holds the credentials and decides which destinations are allowed does.

Third, write the AI-training carve-out into your own contracts. Do not rely on the vendor's terms staying the way they were when you signed. They are allowed to change, and you are deemed to agree.

In Australia, the automated-decision transparency duties start on 10 December. If you score customers, patrons or applicants with software, your privacy policy will have to say so. That list will be much easier to write if you already know which systems make decisions, where they run, and where their data goes.

The question for decision-makers this week is simple. Not "how many agents are we running?" but "what are they producing that no one is reading, and where is the data going while we are not looking?"

If you cannot answer that, the next step is not another pilot. It is a map.

#AI #PrivacyByDesign #DataSovereignty #LocalAI #AustralianPrivacyAct #AIGovernance
