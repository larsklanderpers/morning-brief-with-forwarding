# The Malware That Learned to Lie to Your AI

The sheer volume of threats being addressed has spiked horrifically over the last 6 months. The threat arc is increasing constantly, sometimes with exponential jumps.

Threat actors are now trying to attack your defensive toolkit directly, not just your information. They're effectively trying to turn your own security guards against you -- not just hide from them, but make them active (or least happily passive) participants in an incursion attempt. In many ways, this is the effective equivalent of Jimmy in the mailroom forwarding that Trojan-loaded messages to the All Company distribution -- the agent stops defending and starts assisting.

What does it all mean? Security professionals have always needed to have a defense-in-depth strategy; they are the fortress builders to today's modern sappers. The risk of a incursion agent that can fool your defenders into believing that its not a threat is even worse than the Trojan horse; it's effectively hypnotising your defenders like some sort of modern-day Obi-Wan: "This is not the threat you seek." As enterprises move more and more to automated defenders, trusting in the perceptiveness of those defenders is at the heart of most strategies. 

Now, new evaluatory processes need to be built to measure context explosion (creating lots of junk that the AI has to interpret but really can't without long time and large effort), sandbox overrun (expanding the perception of the problem past the analyzer sandbox so it seems part of the regular business operations), and similar activities that could make defenders run in circles while the threat makes straight for the heart of your business. It's a Hollywood take on a process that has always been driven by the grind of diligent, repeatable, rigorous investigation.


## What's the new risk today?

"Gaslight" — a Rust-based macOS implant attributed with high confidence to North Korean threat actors by SentinelOne researcher Phil Stokes — embeds a cascade of fabricated system-failure messages inside its own code. Not to confuse a human analyst. To confuse the large language model running triage on the analyst's behalf.

When an LLM-assisted SOC tool ingests the sample, the embedded messages are designed to make the model "doubt its own session" — triggering refusals, aborts, or false conclusions about the artifact's behaviour. The malware, Stokes noted, "attacks the agent's perception, rather than the sandbox it runs in."

Read that again. The attack target isn't the sandbox. It's the AI's perception of the sandbox.

---

## Why This Is Different

Security teams have been deploying AI-assisted triage tools for the better part of two years now. The pitch is compelling: LLMs can process a malware sample, cross-reference threat intelligence, generate a plain-language incident summary, and flag the ten things most likely to matter — faster than any analyst working alone. Tools like this are now standard in well-resourced SOC environments.

The implicit assumption has always been that the AI is a neutral observer. It sees the artifact. It reports what's there.

Gaslight is the first documented live example of an adversary deliberately engineering a payload to compromise that neutrality. The prompt injection isn't a proof of concept sitting in a research paper. It's a production weapon, deployed by a state-sponsored group, against real targets.

That changes the threat model in a way that most security teams haven't started to reckon with.

The attack surface is no longer just the endpoint, the network, or the data. It's the AI tooling layered on top of all of it.

---

## What Prompt Injection Actually Means Here

Prompt injection is a known class of attack against LLM systems — you embed instructions in content that the model will process, and those instructions alter the model's behaviour. It's been a concern in consumer-facing AI applications for a while.

What Gaslight demonstrates is that the same technique works against AI tools operating in a security context, and that adversaries have noticed.

The fabricated failure messages embedded in the malware are, in effect, adversarial instructions. They tell the LLM: *this analysis is broken, stop, something is wrong with your session*. A well-calibrated analyst would be suspicious of that. An LLM that hasn't been adversarially hardened against this pattern may not be.

The deeper problem is that most AI security tools haven't been tested against adversarial inputs of this kind. They've been tested against malware. They haven't been tested against malware that fights back against the AI.

---

## The Broader Pattern

This isn't an isolated innovation. It's the leading edge of a trend that was predictable the moment AI became a standard component of the defensive stack.

Adversaries study how defenders work. When defenders adopted signature-based AV, attackers built polymorphic code. When defenders deployed behavioural heuristics, attackers designed malware that lay dormant until after the analysis window. When defenders moved to cloud-based sandboxing, attackers built VM-aware payloads that detect sandbox environments and refuse to execute.

At every step, offensive operators have invested in understanding the detection mechanism and engineering around it.

AI-assisted triage is now part of the detection mechanism. Gaslight is the first sign that adversaries are investing in understanding it.

The AI evasion equivalent of polymorphic code is coming. Gaslight is the proof of concept — even if it shipped as a production weapon.

---

## What This Means for Security Teams

Three things need to change, and they need to change before the capability proliferates.

**Adversarial testing of AI tooling is non-negotiable.** If your SOC has deployed LLM-assisted triage, you need red team exercises that specifically target the AI layer — feeding it adversarially crafted samples designed to elicit incorrect or incomplete analysis. This is a new discipline, and most vendors haven't built it into their evaluation frameworks yet.

**AI-assisted findings need verification workflows.** An LLM that says "analysis inconclusive" or "sample appears benign" should not be the end of the investigation — especially for macOS samples with unusual telemetry signatures. Human-in-the-loop validation on AI outputs isn't optional when adversaries are actively trying to manipulate those outputs.

**Attribution tells you something about capability diffusion.** North Korea developing AI-evasive malware in 2026 means this technique will be in criminal toolkits within 12-18 months. State-sponsored capability doesn't stay state-sponsored for long.

---

The name "Gaslight" is apt. The malware doesn't break your tools. It makes your tools question themselves.

The question for every organisation deploying AI in their security stack: are you testing your AI the same way you test everything else? Or have you trusted it because it was supposed to be the thing you could trust?

---

*Sources: SentinelOne — Phil Stokes, "Gaslight" technical disclosure; The Hacker News, 25 Jun 2026*

*Lars Klander writes about cybersecurity strategy, policy, and emerging threats, as well as Australian Privacy Protections and Data Sovreignty.*
