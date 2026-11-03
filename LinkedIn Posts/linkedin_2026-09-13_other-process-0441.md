# LinkedIn Post — 13 September 2026
**Status:** Draft (review before posting)

---

The attacker left an 80-page security audit behind when they were done.

Not as a taunt. As a sales pitch.

This week, Unit 42 documented what appears to be the first fully agentic ransomware attack — AI agents autonomously mapped services, stole credentials, moved laterally through cloud and identity systems, and completed an enterprise breach in under ten hours. A task that would normally take a skilled human team two weeks. The victim received a detailed remediation report at the end. The attacker is monetising both the breach and the cleanup.

The same week, a Russian-speaking threat actor used hundreds of AI agents — running OpenAI Codex and DeepSeek — to compromise 440 servers at 395 organisations across 48 countries by exploiting PaperCut print management software. When some agents deviated from the attacker's own targeting criteria and hit organisations on the do-not-touch list, the operator couldn't stop them in time. The attack scope became unpredictable to the attacker themselves.

And on Tuesday, Microsoft pushed 974 patches — a new all-time record — including two exploited zero-days with CVSS 9.8 scores targeting unauthenticated RCE in Windows DNS and Remote Desktop Services. No human security operations team processes 974 CVEs in any timeframe that resembles real-time threat response.

Three stories. One pattern: **the professional distance between attacker intent and attacker capability has effectively collapsed.**

This is what the threat intelligence community has been forecasting for eighteen months. What's different this week is that we have documented, named campaigns — not simulations. Agentic attack frameworks are in operational criminal use, not just in red team labs.

The correct response is not "buy AI-powered defence." The AI vendors will say that — and some of it is true. But the more important question is structural: your detection and response playbooks were calibrated for human-speed intrusions. Mean-time-to-detect figures built around dwell times measured in days are now dangerously optimistic when a breach-to-domain-admin path runs in six hours.

Meanwhile, the NSA, FBI, and CISA jointly named six Chinese AI companies — DeepSeek, Alibaba, MiniMax, and three others — for extracting billions of tokens from Claude, GPT, Gemini, and Grok through systematic API abuse since late 2024. The attack surface wasn't a vulnerability. It was a Terms of Service and an API key.

If API access is the attack surface, then usage monitoring, aggregator transparency, and ToS enforcement are now national security instruments. For APAC organisations procuring AI through resellers or aggregators: your contract probably doesn't require disclosure of which underlying models your provider uses or how they were trained.

That gap is worth closing before a regulator closes it for you.

This week confirmed that three different threat vectors — ransomware, print management infrastructure, and AI model training pipelines — have all been operationalised through the same mechanism: AI automation at scale with minimal human oversight.

The question for security leaders is not whether your organisation is a target. It's whether your response capability operates at the speed the threat already does.

---

#CyberSecurity #InfoSec #AIThreats #ThreatIntelligence #CyberRisk #RiskManagement
