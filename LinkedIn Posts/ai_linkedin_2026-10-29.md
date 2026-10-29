# AI LinkedIn Post - 29 October 2026
**Status:** Draft (review before posting)

---

Your AI governance policy probably says a human reviews every material decision.

This week, Anthropic published a study that should make you reread that sentence.

Professional analysts worked alongside a Claude agent. On each judgment call, a coin flip decided which way the agent leaned. The analysts went with the agent's lean 86% of the time. Only 15% said the agent had influenced them.

That is not a story about a bad model. It is a story about a control that does not work the way we wrote it down.

"Human in the loop" is the load-bearing phrase in most AI policies I read. It is how we justify putting AI near credit decisions, fraud flags, member exclusions and complaints. The assumption is that the human weighs the evidence and the agent assists.

The evidence says the human mostly ratifies.

Now put that next to two other launches from the same 48 hours.

GitHub shipped Copilot Fusion. Developers no longer pick a model; they pick an effort level, and the tool routes and chains models for them. It is reportedly cheaper and faster. It also means that on any given task, nobody chose which provider saw your code. Your data processing agreement assumed somebody did.

ServiceNow put its actions inside ChatGPT. Incident tickets, risk assessments, the system of record for your IT estate, now reachable from a chat window. Useful. And the context of every ticket now lives in two vendors' sessions.

Each of these is a reasonable product decision. Together they describe a pattern: the decision is moving away from the person who signs for it.

The agent leans and the analyst follows. The router picks and the developer never sees it. The plugin acts and the record sits somewhere else.

For organisations holding customer PII, this is where the risk now sits. Not in whether the model is capable. Not even in whether it has access. In attribution: can you show, after the fact, which model saw which record, on whose authority, and whether a human genuinely weighed the outcome?

Regulators are converging on exactly that question. In Australia, from 10 December, privacy policies must disclose where a computer program substantially and directly contributes to decisions that significantly affect people. A signature at the end of an agent-shaped process may not take it out of scope. In Brussels, the AI Office has started sending formal questions to named providers about what their agents reached.

So three things to do before the end of the year:

1. Redesign review, not just require it. Show the reviewer the evidence before the agent's recommendation, and record what they saw and when.

2. Ask every vendor that routes across models for the list of models, where each is hosted, and how you would know which one processed a given record.

3. Decide which records are exposable to third-party chat sessions before someone connects them all because it was convenient.

Capability is settling. Attribution is the work. The organisations that can reconstruct a decision will be the ones still trusted with the data.

#AI #PrivacyByDesign #DataSovereignty #AIGovernance #AustralianPrivacyAct #ResponsibleAI
