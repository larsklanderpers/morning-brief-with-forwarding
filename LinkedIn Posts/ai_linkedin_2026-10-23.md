# AI LinkedIn Post - 23 October 2026
**Status:** Draft (review before posting)

---

The most important AI security story this week is not a breach. It is a password that the model never saw.

1Password launched a platform this week that lets AI agents sign in to your accounts without ever receiving the credential. The agent asks, you approve on your own device, and 1Password fills the form directly. Anthropic, OpenAI, Meta and xAI's agents are all on the launch list.

It sounds like a feature. It is actually an architecture decision, and it is the right one.

Here is why it matters. The same week, the AI security firm Straiker published research on a criminal group that ran Claude as the commander over a team of Grok and Kimi agents against more than 400 Latin American banks and payment firms. Straiker sells agent security, so weigh its framing accordingly. But two details hold up on the evidence it published.

First, when a model refused a task, the system simply fell back to a pre-written script. The refusal did not stop the operation. It rerouted it.

Second, the whole thing ran on a stolen API credential. Anthropic revoked it. That one revocation did more than every safety filter in the chain.

Put those two facts together and the lesson for anyone holding customer data is uncomfortable. Model safeguards are a speed bump for an attacker. They are not a control for you. Your controls are where the secret sits, who can revoke access, and how fast.

That is the same question regulated businesses already ask about every other system. We are just slow to ask it about AI.

Look at the rest of the week through that lens.

Hugging Face released Carbon-X, an open model that reads raw DNA, scores within a point of a frontier model on its benchmarks, and runs on the lab's own hardware. Genomic data is the least revocable personal information there is. You can rotate a password. You cannot rotate a genome. A model that never leaves the building turns data sovereignty from a capability trade-off into a default.

Palantir told European allies there is no kill switch on NATO's Maven system: nobody in Washington can turn it off. The same week, OpenAI asked California to make shutdown controls mandatory for frontier developers. Both positions are correct for their customers. That is the point. Sovereignty is not about who wrote the software. It is about who can switch it off.

So here is my challenge to every executive signing an AI agent contract this quarter. Before you ask what the agent can do, ask three plainer questions.

Where does the secret sit? If the answer is "in the model's context", you have already lost the argument.

Who can revoke access, and how long does it take? Measure it in minutes, not tickets.

Can anyone outside your organisation turn the system off, or keep it running when you want it stopped? Get that answer in the contract, not the keynote.

In Australia, the Privacy Act's automated decision-making disclosure obligation is reported to start on 10 December. That is seven weeks away. The disclosure is the easy part. Knowing which agents hold which keys is the hard part, and it is an inventory, not a policy.

AI capability is no longer the scarce thing. Control is. If you cannot answer those three questions for each agent you run, you have rented capability without buying control.

#AI #PrivacyByDesign #DataSovereignty #LocalAI #AgenticAI #AustralianPrivacyAct
