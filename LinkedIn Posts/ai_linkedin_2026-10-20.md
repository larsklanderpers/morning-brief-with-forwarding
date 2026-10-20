# AI LinkedIn Post - 20 October 2026
**Status:** Draft (review before posting)

---

The US government just banned a model it cannot stop you from downloading.

On Monday, DHS ordered federal civilian agencies to remove DeepSeek from their systems, and not only DeepSeek's own apps. The order reaches third-party products "developed using DeepSeek implementations". The stated reason is data security: who can see what agencies type into it.

The same weekend, DeepSeek put the weights for its latest Flash model on Hugging Face. It claims the model beats Claude Opus 5 on several agent benchmarks. Independent scores are lower, and the vendor numbers deserve the usual scepticism. The price is not in dispute: reported at about $0.15 per million input tokens against $5 for Opus 5.

Those two facts look contradictory. They are not.

They describe two different things that happen to share a name.

The hosted DeepSeek service sends your prompts to servers under Chinese jurisdiction, under a policy that reportedly allows training on inputs. That is what DHS is removing.

The open weights, running on hardware you own, send nothing anywhere. Same model. Completely different risk.

For anyone holding customer PII, this is the distinction that matters more than any benchmark: the model is not the risk. Where inference happens is the risk.

Two other stories from this week sharpen the point.

Microsoft told customers to treat AI agents as insiders and shipped permissions that start at zero, granted per task, revocable mid-task. The principle is that the control must sit outside the model. That is data minimisation for software that acts.

And a security researcher found one operator using a multi-agent platform to break into more than 100 company websites, including sites in Australia, at an estimated $50 per success. The old comfort that a mid-sized business is not worth an attacker's time is gone. It now costs less than lunch for the team.

Put those together and the procurement question changes.

Not "which model is best?" but three questions you can put to any vendor this week:

1. Where does inference physically run, and which country's law can compel the provider to hand over what it sees?
2. What can the agent touch by default, and who approves anything beyond that?
3. Which models sit inside the products you already use? If a US agency needs that list to comply, a regulator here will ask you for it eventually.

Most vendors cannot answer the third question today. That is the gap.

Self-hosted weights are a sovereignty asset. A hosted API in another jurisdiction is a dependency you have to justify, line by line, to the people whose data you hold.

If your AI roadmap does not yet say where each workload runs, write that column before you choose another model.

#AI #DataSovereignty #LocalAI #PrivacyByDesign #AustralianPrivacyAct #AIGovernance
