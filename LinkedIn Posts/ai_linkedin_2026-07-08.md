# AI LinkedIn Post — July 8, 2026
**Status:** Draft (review before posting)

---

For eighteen days last month, a frontier AI model simply disappeared.

Not a bug. Not an outage. A government export-control order pulled Claude Fable 5 offline on June 12, and it didn't come back until July 1. Anyone who had built a workflow on top of it spent nearly three weeks discovering that the model behind their business wasn't theirs to keep.

I keep coming back to that blackout, because it's the cleanest illustration of a question most organisations still haven't asked themselves: whose jurisdiction is your AI actually running in?

We've spent two years arguing about which model is smartest. Gemini 3.5 versus GPT-5.6 versus Fable 5. It's the wrong argument. For anyone who holds customer PII, the benchmark that matters isn't reasoning score — it's control. And on that measure, the picture in 2026 is sharpening fast.

Look at what landed this month.

APRA's CPS 230 took effect on July 1, and it now sweeps AI vendors into "material service provider" scope for every bank, insurer, and super fund in Australia. The quiet detail regulators keep hammering: data residency is not data sovereignty. "Our data sits in an Australian data centre" sounds reassuring right up until an auditor asks where the *inference* runs — and you discover your Copilot queries may route offshore depending on load and configuration. Storage location and processing location are different questions, and only one of them satisfies a regulator.

Meanwhile Australia's automated-decision-making transparency rules go live on December 10. Five months out. They'll force every APP entity to disclose the personal information feeding its automated decisions — which means actually mapping where PII flows into every model you run. Most organisations have never done that map. The ones who start in December will be the ones explaining themselves to the OAIC in January.

And across the world, Mistral just opened early access to a new open-weight model family and committed €4 billion to data centres in France and Sweden. Their entire pitch is one word: autonomy. Run the model, inspect it, modify it — free from any foreign government's terms of service. A month ago that sounded like European marketing. After the Fable 5 blackout, it sounds like a risk-management strategy.

Here's the thread connecting all of it. The most important AI decision you'll make this year isn't *which* model. It's *whose infrastructure, under whose laws.*

And the good news is that the honest answer is finally available. The open-weight tier — Mistral, Qwen, gpt-oss, Nemotron — has matured to the point where self-hosting is a genuine compliance posture, not a downgrade. A capable team can stand up private inference in an afternoon. When the model runs on your own tin, customer PII never leaves your jurisdiction, there's no DPIA on a foreign processor, and no export-control order can switch it off. "Which model" and "whose jurisdiction" get answered by the same decision.

So the call to action for anyone sitting on regulated data is uncomfortable but simple: stop treating data sovereignty as a compliance line item and start treating it as an architecture decision. Ask your vendors one question and make them answer it in writing — *where, exactly, is our inference processed?* If they can't tell you, you don't control your sovereignty posture. You're renting it, and the lease can be revoked.

The organisations that come out ahead won't be the ones running the smartest model. They'll be the ones who can prove where their customers' data lives — and who can't have it taken away.

#DataSovereignty #PrivacyByDesign #LocalAI #AIGovernance #AustralianPrivacyAct #GDPR
