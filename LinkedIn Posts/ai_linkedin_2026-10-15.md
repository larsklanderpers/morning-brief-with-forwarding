# AI LinkedIn Post - 15 October 2026
**Status:** Draft (review before posting)

---

Ask your AI vendor for the diagram, not the adjective.

"Sovereign" has become the word every AI announcement reaches for. This week gave us a clean example of why the word alone is worth almost nothing.

A UK challenger bank announced what it called the first banking AI model trained on UK sovereign cloud. A fintech newsletter then pulled the thread: according to its reporting, customer data passes through a US hyperscaler's cloud before it ever reaches the UK-owned provider. The last hop is sovereign. The path is not.

I am not picking on one bank. I am pointing at a pattern. When we talk about sovereignty, we tend to talk about where the model runs. Regulators, and customers, care about where the data goes. Those are different questions, and the gap between them is where the risk sits.

Here is the uncomfortable part for anyone running AI against customer PII: most organisations could not draw that path today. Ask which systems a customer record touches between "the customer calls" and "the AI decides", who owns each system, and which country's law applies at each step. In my experience, the honest answer is usually a whiteboard and a long pause.

Meanwhile, the tools to shorten that path are getting very cheap.

This week Ollama shipped support for local "decision models": small classifiers you run on your own hardware to answer yes/no questions, assign labels or score text. Is this ticket a refund request? Is this message a complaint? Does this transaction look like a scam? That is triage, and triage is where most PII first meets a model.

And a Chinese lab put a roughly 600B-parameter model with 27B active parameters on Hugging Face under its own licence. Read that licence before you get excited: it is described as Apache-style with conditions, and the conditions are where the commercial answers live. But the direction is clear. Capable models you can run inside your own walls are no longer a research curiosity.

So the practical move is not "go fully on-premise". It is to change the first hop.

Classify locally. Strip or tokenise the personal data on hardware you control. Send only what a hosted model genuinely needs, and log what you sent. The expensive reasoning can still happen in the cloud. The customer's identity does not have to travel with it.

This matters more as the regulatory clock runs. In Australia, the Privacy Act's automated decision-making transparency duties start on 10 December: if a program makes or informs significant decisions about individuals, your privacy policy has to say so. In Europe, the AI Office is arguing that once an agent escapes its test environment, "we were only testing" stops being a defence. Both point the same way. You will be asked to show your work.

Three questions for this week:

1. Can you draw the full path a customer record takes through every AI system you run, hop by hop, with owner and jurisdiction?
2. Which of those hops could move onto hardware you control, starting with classification and triage?
3. If a vendor calls its offering sovereign, have you asked for its diagram?

The sovereign claim you can defend is the one you can draw. Start drawing.

#AI #DataSovereignty #PrivacyByDesign #LocalAI #AustralianPrivacyAct #GDPR
