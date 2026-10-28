# AI LinkedIn Post - 28 October 2026
**Status:** Draft (review before posting)

---

The most dangerous AI installer this week was signed by the real vendor.

Check Point Research published a campaign it calls Yoba on 27 October. Fake GitHub projects posing as ChatGPT and Claude desktop apps ranked near the top of Google. Each download was a ZIP containing a genuine, signed OpenAI or Anthropic installer, plus one extra file: a malicious DLL that Windows loads from the same folder. The signature checked out. The payload was a crypto miner, and the loader could have delivered anything.

Nobody at OpenAI or Anthropic was compromised. The model was never the problem. The wrapper was.

Hold that thought, because it describes most of what moved in AI this week.

Apple announced that Pages, Keynote and Numbers are getting AI assistants built on a mix of Apple and OpenAI models, and that those apps will support the Model Context Protocol so outside agents can read and edit documents. That is useful. It is also two new data paths arriving on managed Macs in November: an assistant whose requests may go to a third-party model, and a door any local agent can use. The coverage so far does not say which requests go where.

Meanwhile, the European Central Bank's deadline lands this Saturday. The 110 banks it directly supervises must submit plans against AI-enabled cyberattacks, and the priorities include internet-facing systems and tighter oversight of third-party providers. Not "what model are you using?" but "who and what surrounds it?"

And at the other end of the market, Liquid AI released LFM3, a family of small open-weight models, including a text model that reportedly fits in about 1 GB and is built for agent work on a laptop. The model in the middle keeps getting cheaper and more capable. That is the good news.

Here is the uncomfortable part for any business that holds customer PII.

Your privacy posture is no longer decided by the model you chose. It is decided by everything around it:

- Where did the client software come from, and who was allowed to install it?
- Which model does the assistant inside your document tool actually call, and under whose terms?
- What can an agent on that machine reach, and is outbound traffic denied by default?
- Could you show a regulator a register of every third party that touches the data on its way to and from a model?

Most AI governance programmes I see are built around model selection: a list of approved models and a policy that says what staff may paste into them. That was the right starting point in 2024. It is the wrong centre of gravity in 2026, because the model is becoming the most trustworthy component in the chain.

So my call to decision-makers is simple. Move your AI governance effort from the model to the perimeter.

Approve AI clients through your own software portal, not search results. Set your MDM policy for embedded assistants before they ship, not after. Treat every MCP endpoint and agent runtime as an integration that needs an owner and a review date. And if you are in financial services, write the ECB-style plan now, while nobody is asking for it yet.

The capability question is settling. The perimeter question is the one to staff.

#AI #PrivacyByDesign #DataSovereignty #LocalAI #AustralianPrivacyAct #AIGovernance
