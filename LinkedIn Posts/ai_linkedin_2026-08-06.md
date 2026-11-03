# AI LinkedIn Post — 6 August 2026
**Status:** Draft (review before posting)

---

Four people who together built MapReduce, Google File System, Bigtable, Spanner, and the seq2seq architecture that underlies every model you've used in the last decade walked out of Google yesterday.

Their startup, Discovery Loop, has one goal: automate the experimental loop itself.

And Sam Altman, on the same day, told a room full of founders that what used to take three months to build "now takes seven minutes."

I've been sitting with both of those data points this morning. Here's what they mean together.

---

**The speed is real. The accountability isn't keeping up.**

When Jeff Dean and three co-founders can raise a seed round from Radical, Khosla, Lightspeed, and Kleiner Perkins to automate the scientific method, we're not talking about AI that writes your emails faster. We're talking about AI that replaces the human in the loop of discovery itself — drug trials, materials research, engineering validation.

Meanwhile, on August 2 — four days ago — the EU AI Act's core enforcement obligations went live. High-risk AI systems across biometrics, employment, financial services, critical infrastructure, and law enforcement are now subject to Articles 9 through 17. Risk management. Data governance. Logging. Human oversight. Cybersecurity resilience. Post-market monitoring.

Not in 2027. Now.

---

**The PII problem just got harder.**

Here's the tension that should be keeping compliance teams up at night.

Agentic AI systems — the systems now deploying in wealth management, insurance underwriting, and customer onboarding — don't operate as the classified system you reviewed last quarter. By the time an agentic workflow produces a decision affecting your customer, it has typically assembled tools, delegated to sub-agents, retrieved new context, and adapted its plan. The execution chain that produced the outcome may never have been reviewed as a whole.

A practitioner in the AI governance community named this "compliance identity drift" this week on LinkedIn, and it's exactly right.

Meanwhile: Verizon's 2025 DBIR found that credential abuse — a threat that becomes dramatically worse when agents hold standing API keys in their environment — was the most common breach initiator at 22% of cases.

Your compliance documentation describes a static system. Your production AI is not a static system.

---

**The organisations that get this right are building it in, not bolting it on.**

There are now genuinely capable open-weight models you can run inside your own jurisdiction. OpenAI's gpt-oss-20b runs on 16GB of RAM under Apache 2.0. Kimi K3 is the open-weight benchmark leader. Qwen3's family runs from 1.7B to 235B with no commercial restrictions. On Apple Silicon, Ollama's MLX backend is stable.

A Smart Prompts for AI newsletter published this morning described a financial advisory firm that nearly lost a major retainer when a junior analyst pasted an unredacted tax return — SSNs, bank routing numbers, the works — into a public chatbot to beat a deadline. They caught it. Not every firm will.

The lesson isn't "write better policies." Policies don't survive deadline pressure and tired analysts. The lesson is architectural: if the tool connects to the internet, you are one bad day away from an incident.

For businesses with real PII obligations — financial services, health, government — the question has shifted. It's no longer "can we afford capable local AI?" The entry point for a private LLM server is $8,000 to $12,000. Cost parity with cloud APIs arrives around 50,000 queries a month. For most organisations running meaningful AI workloads, that's a capital expenditure conversation, not a capability conversation.

---

**The window to build it right is narrowing.**

Australia's Privacy Act automated decision-making transparency deadline hits December 10. The EU AI Act is enforcing now. Australia's National Cabinet is considering AI standards this month. The White House is running a secret vetting process for frontier model releases that most companies aren't invited to observe.

The governance framework is being written in real time. The organisations that have clean answers — what personal information feeds our automated decisions, where does inference run, who controls the audit trail, what happens when the agent acts outside its mandate — are the ones that won't have to pause and retrofit when the examiner comes calling.

Jeff Dean's Discovery Loop will automate the experimental loop. Sam Altman says seven minutes is the new three months. Both of those things can be true. The question is whether your organisation is building compliance into its AI stack at seven-minute speed, or whether you're going to spend three months explaining to a regulator why you weren't.

---

*What's your organisation's current answer to "which personal information feeds your automated decisions"? I'm genuinely curious where regulated-industry teams are on this.*

#AI #DataSovereignty #PrivacyByDesign #LocalAI #EUAIAct #AustralianPrivacyAct #AIGovernance #RegulatedIndustries #GDPR #ArtificialIntelligence
