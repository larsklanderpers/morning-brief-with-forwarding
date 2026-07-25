# AI LinkedIn Post — Wednesday, 15 July 2026
**Status:** Draft (review before posting)

---

Microsoft's CEO just made the case against his own industry's business model. Nobody blinked.

In a post this week, Satya Nadella wrote that when you use cloud AI, you "pay for intelligence twice — once with money and again with your proprietary knowledge." Every prompt, every tool call, every correction your team makes when the model gets it wrong leaks institutional know-how "trace by trace" back to the model provider.

That's not a privacy activist talking. That's the man selling you the cloud.

He said it in the same 48 hours that two governments moved on the same underlying question — who controls AI, and on whose terms.

In Canberra, the Prime Minister announced Australia's new Office of AI: unified standards, streamlined approvals, a coordinated national posture. No standalone AI Act — Australia is betting on existing law plus coordination. But the binding constraint hasn't moved: from 10 December, the Privacy Act's automated decision-making rules apply, with penalties up to AUD 50 million or 30% of turnover.

In the US, Demis Hassabis published a manifesto calling for a government-backed body with the power to screen frontier models before they reach the market. Read the buried sentence carefully: frontier models "would be required to pass it to be deployed in the US market." That's not a framework. That's a licensing regime.

Put the three together and a pattern emerges.

Your AI capability is rented. Your access to it is a policy variable — June's export-control freeze that switched off frontier models for millions of users proved that in the most direct way possible. And your usage of it is quietly training someone else's asset.

For most businesses, that's an abstract worry. If you hold customer PII — in financial services, health, government — it's not abstract at all. It's three concrete questions:

Where does inference actually happen? (APRA-regulated entities: "stored in Australia" is not "processed in Australia." Ask in writing.)

What does your usage teach your vendor? (If your team's corrections encode how you assess risk, price policies, or triage patients, that knowledge is compounding on someone else's balance sheet.)

What's your fallback when policy shifts? (The organisations that handled June's model freeze best were the ones already running multi-model, with open weights they controlled.)

Here's the uncomfortable part: the answer to all three is architecture, not procurement. You can't contract your way out of a learning loop you don't own. You can't disclose automated decisions — as Australian law will require in five months — made by systems you can't inventory.

The good news is the toolkit has never been better. Open-weight models now trail the frontier by single digits on most working tasks. Local inference runs on hardware you already own. Sovereign options in Europe and Australia are multiplying by the quarter.

Capability is table stakes. Control is the strategy.

If you're a decision-maker in a regulated industry, don't start with "which model is best." Start with an inventory of every decision your systems now make about a customer without a human in the loop. December is closer than it looks — and you can't govern what you can't list.

#AI #DataSovereignty #PrivacyByDesign #LocalAI #AustralianPrivacyAct #AIGovernance
