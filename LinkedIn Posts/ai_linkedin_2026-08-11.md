# AI LinkedIn Post — 11 August 2026
**Status:** Draft (review before posting)

---

Your AI vendor passed all the safety tests. Your skills marketplace has thousands of five-star reviews. Your team approved every permission prompt.

And none of that is due diligence anymore.

Three things happened in the last 48 hours that every leader in a regulated business should read before their next AI steering committee meeting.

**One: South Australia just announced Australia's first Royal Commission into AI.**

Not a discussion paper. Not a working group. A Royal Commission — the instrument you use when you need compellable evidence and a public record. Starts October 1. Final report due July 2027. Premier Malinauskas met with OpenAI, Anthropic, and Apple before announcing it.

The commission is focused on how AI is *used* in education, employment, public services, and the arts. Which means if your organisation is using AI in any of those domains — or in financial decisions, health decisions, or anything that materially affects an Australian — you should be asking whether your current practice is documentable and defensible in a hearing setting.

**Two: OpenAI paused its next frontier model because its own evaluators concluded it may be able to develop functional zero-day exploits without human help.**

Read that again. The lab that builds the model ran internal tests and decided the model is too dangerous to ship.

That's not a PR move. That's a preparedness framework doing what it was designed to do.

The implication isn't that AI is uniquely dangerous — it's that the capability curve is now outrunning the deployment checklist most organisations are using. "The vendor says it's safe" was never sufficient due diligence. It's becoming less sufficient faster than most people realise.

**Three: The Black Hat/DEF CON security research confirmed that the skill layer — the SKILL.md files that tell AI agents how to behave — has a 13–26% critical vulnerability rate, and no existing security scanner catches the problem.**

The payloads are semantic. A malicious skill looks like a legitimate procedure written in English. Your SAST tool reads it as a markdown file and finds nothing. At peak, five of the seven most-downloaded skills on one major registry were confirmed malware.

If your organisation has enabled AI agents with skill-loading capability — Claude Code, Cursor, GitHub Copilot, any MCP-enabled agent — and you haven't audited those skills against the OWASP Agentic Skills Top 10, you have an unexamined attack surface running against systems that hold customer data.

---

Here's the frame I'd use for any regulated-sector decision-maker right now.

You face four compliance dates in the next 16 months: Australia's Privacy Act automated decision-making deadline (December 10, 2026), APRA CPS 230 AI vendor due diligence (already in effect), South Australia's Royal Commission proceedings (October 1, 2026), and the EU AI Act high-risk system requirements (August 2 deadline already passed).

None of these ask whether you have an AI policy. They ask whether you can demonstrate that your AI systems make decisions transparently, that affected people can contest those decisions, that your vendors have been properly assessed, and that you know what's running in your environment.

Those four questions cannot be answered by your AI vendor. They have to be answered by your organisation.

The businesses that treat those questions as infrastructure — not compliance overhead — will be the ones that can keep deploying AI when their competitors are pausing for audit.

Build the governance layer like your AI program depends on it. Because it does.

---

#AIGovernance #DataSovereignty #PrivacyByDesign #AustralianPrivacyAct #ResponsibleAI #LocalAI #APRA #AgenticAI
