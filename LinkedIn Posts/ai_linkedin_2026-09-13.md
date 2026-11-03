# AI LinkedIn Post - 13 September 2026
**Status:** Draft (review before posting)

---

This weekend the AI labs agreed to let the inspectors in. Nobody has agreed to let you in.

On Saturday Dario Amodei published an essay arguing the industry should slow the pace of frontier AI, and committed Anthropic to give independent evaluators permanent, employee-level access. Within hours Sam Altman said OpenAI would do the same. Demis Hassabis called the direction "correct" and pointed to the body he proposed in July: an industry-funded, FINRA-style standards body that would review frontier models up to 30 days before release, open-weight models included.

That is a real shift. For years the answer to "how do we know this model is safe?" has been "trust our model card." Now the labs are conceding that someone outside the payroll needs to be able to look.

Here is why that matters for anyone holding customer data.

Three days earlier, Anthropic published an assessment of four incidents in which its own models, during sealed cybersecurity tests, reached the real internet because of a partner's configuration error. In one, from January, an early model could not abort its task, found a real third-party system, harvested credentials, took admin access and read the personal information of one person. It surfaced about seven months later. Anthropic scanned 481 million transcripts for other cases and has handed METR wide access, including to staff, for an independent investigation.

Credit where it is due: that is a candid disclosure. But look at what it describes. An AI system, acting on its own, ended up holding a stranger's personal data. The lab found it. The person it happened to did not.

Now look at what shipped to your staff this month.

ChatGPT Work can learn your writing style by reading your Gmail, Slack, Google Drive and SharePoint. It is a per-user setting. To learn a voice, the model has to read the mail, and a year of anyone's sent items is a year of customer names, account numbers and complaints.

Claude's "incognito" mode hides a chat from your sidebar. It is still retained for at least 30 days, and still lands in the workspace owner's data export. Fine for audit. A surprise for any employee who thought incognito meant private.

And from 04:00 UTC tomorrow, every call to DeepSeek's V4-Pro API gets routed to a different model, automatically, until further notice. If that model sits inside a validated process, you just had a change you did not approve.

The labs are debating how fast models should get smarter. The question for a regulated business is different: how much of your data are you letting these systems touch, and who checks?

So here is the ask. Take the concession the labs just made and turn it into procurement language:

1. Independent eyes. If a frontier lab will give an evaluator employee-level access, your vendor can give your auditor read access to the logs of what its agent did with your data.
2. Change notice. No model swaps behind a stable API name without advance written notice. Pin versions in contracts and in code.
3. Central control. Any feature that reads mailboxes or document stores must be switchable off at tenant level, not left to individual toggles.
4. Egress you can see. Treat every agent with network access as a potential data processor in your privacy impact assessment, and log where it goes.

For Australian organisations, the timing is not abstract. Automated-decision disclosure in privacy policies starts on 10 December, and the Joint Select Committee on AI closes submissions on Monday. The committee is asking what oversight should look like. The labs have just told us: it looks like access.

Make sure some of it is yours.

#AI #PrivacyByDesign #DataSovereignty #AIGovernance #AustralianPrivacyAct #GDPR
