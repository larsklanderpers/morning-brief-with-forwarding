# You Are the Product: How AI Followed the Playbook Everyone Swore It Wouldn't

There is a phrase so old it has become background noise: *if you're not paying for the product, you are the product.* Everyone who was paying attention said it about Google. Then, everyone said it about Facebook. Then Instagram. Then TikTok. We tattooed it on the forehead of every free web service that turned data into dollars. And then, when a new wave of AI assistants arrived — extraordinary, almost magical things — we paid for them, and we told ourselves that changed everything. 

It didn't.

The architecture of extraction has simply upgraded itself. It is smarter now, more intimate, and infinitely more dangerous — because the data it harvests isn't your browsing history or your ad clicks. It is your thinking. Your strategy. Your company's secrets. And in some cases, very soon, your voice, captured in real time, while the system is talking back to you. And if you believe for one minute that it won't be used to sell to you as the system learns more and more about your tells, your inclinations, and what hits for you and what doesn't, you are burying your head in the sand.

---

## The Ads Were Always Coming

On February 9, 2026, OpenAI flipped the switch. Ads appeared in ChatGPT. The Ads Manager opened to all U.S. businesses by May. OpenAI is projecting $2.5 billion in ad revenue by year's end, $25 billion by 2028, $100 billion by 2030.

The company insists that responses won't be influenced by advertising, that "Sponsored" labels will be clear, that they will "never" sell user data to advertisers. These are the same assurances Google made in 2003 and Facebook made in 2009. The ad model has its own logic, and that logic is not neutral. The moment a platform's survival depends on advertiser revenue, the optimization pressure — however subtle, however slow — bends toward the interests of buyers, not users. History is unambiguous on this point.

For now, only free-tier users see ads. But the free tier is how you scale. It is how you acquire the hundreds of millions of users whose aggregated behavior trains the model, whose preferences teach the system what to anticipate, whose queries form the dataset that makes the paid product worth buying. The free user has always been the raw material. The ad announcement simply makes the transaction visible.

Gemini is already further down this road. Google's privacy audit gives it a D — 42 out of 100. Conversations with Gemini can feed Google's ad targeting. Gmail, Search, YouTube, Maps, and now your AI conversations merge into a single unified profile. For Gemini users on the free tier, human reviewers can access your prompts. The personalization isn't a feature. It is the business model wearing a feature's clothes.

---

## The Ear That Never Closes: GPT-Bidi-1

The most significant unreleased development is one most people haven't heard of: GPT-Bidi-1, OpenAI's bidirectional audio model currently in limited testing.

Unlike existing voice modes — which listen, process, then respond in sequence — Bidi-1 is full-duplex. It listens and speaks simultaneously. It can absorb interruptions mid-sentence, acknowledge you in real time, maintain conversational context across an extended session. Three intelligence tiers. Real-time translation. A genuinely continuous audio pipeline.

The technology is impressive. The privacy implications are arresting.

For Bidi-1 to function, it must maintain a persistent audio stream — either processed locally or, more likely, routed through OpenAI's cloud infrastructure with near-zero latency. This means an always-open microphone, a live feed to external servers, processing ambient conversation as a baseline condition of operation. What is captured in that ambient stream? What counts as the conversation and what counts as noise? Who decides? On platforms like Windows, where microphone permissions are already granted broadly for Cortana and dictation, the attack surface expands considerably. In a trusted environment that we have all been taught by experience to believe is secure.

There is no official launch date. There is no official statement. What exists is a trail of code references, limited sightings on mobile clients, and a set of privacy tradeoffs that the company has not yet been asked to explain publicly. The question isn't whether those tradeoffs will arise. It's whether anyone will be paying attention when they do.

---

## Copilot and the Illusion of the Trusted Assistant

Microsoft's Copilot was sold to enterprises as the AI that stays inside the walls. Deeply integrated into Microsoft 365, trained on your org's own data, subject to your own governance. The promise was containment and control.

The reality has been more complicated.

In January 2025, researchers discovered EchoLeak — CVE-2025-32711, CVSS score 9.3 out of 10 — a zero-click vulnerability that allowed exfiltration of sensitive data from Microsoft 365 Copilot's context without any user interaction. No clicks. No suspicious links. No social engineering. The data simply left.

That same month, Copilot was found accessing confidential emails in Sent Items and Drafts despite active DLP policies and confidentiality labels. Microsoft issued an emergency patch. In September 2025, researchers demonstrated that manipulated Office documents could trick Copilot into embedding email content in interactive Mermaid diagram links — another exfiltration vector, plugged only after Microsoft disabled interactive links in Mermaid entirely.

The Wayback vulnerability affected 16,290 organizations — Microsoft, Google, Intel, Huawei, PayPal, IBM, Tencent — exposing over 300 private tokens, keys, and secrets to GitHub, Hugging Face, GCP, and OpenAI. The U.S. Congress banned its staff from using Copilot. Sixty-seven percent of enterprise security teams report concerns about AI tools exposing sensitive information. The average breach cost for organizations with high shadow AI usage reached $4.63 million.

This is not a story about a flawed product. Every product has bugs. This is a story about what happens when you build a tool whose core value proposition — reading everything, synthesizing everything, remembering everything — is structurally in tension with the concept of secrets.

---

## The @Tag Problem: Secrets Summoned by Name

Consider how enterprise AI is actually used. A developer types a query and uses an @tag to reference a repository, a document, a database. A manager pulls in a strategic planning document to help draft a summary. A salesperson tags customer records to personalize an outreach. The AI obliges because that is what it was designed to do.

The problem is not malice. It is architecture.

When a user @tags a sensitive resource into an AI context window, they are inviting a system that may log, transmit, and potentially train on that content. Enterprise controls help — Microsoft's Zero Data Retention mode, Google's Vertex AI guarantees, Anthropic's enterprise agreements — but these safeguards apply only when the right tier is purchased, correctly configured, and actively enforced. The 77% statistic is damning: 77% of employees pasting company data into AI tools are doing so via accounts and sessions invisible to enterprise identity management. Shadow AI is not the fringe case. It is the norm.

Samsung learned this in the starkest possible way: three separate incidents in a single month, source code and internal meeting notes and hardware data entered into ChatGPT by employees who were simply trying to do their jobs faster. Samsung responded by banning generative AI tools entirely. Most companies will not respond that way, which means most companies are currently running this experiment without knowing it.

The @tag is not a bug. It is a feature that converts human organizational intelligence — the hard-won, competitively differentiated knowledge that companies spend years accumulating — into training signal for systems they don't own.

---

## The Upgrade Cycle as Data Collection Strategy

There is a pattern in how these systems evolve that deserves to be named clearly.

Each new capability — persistent memory, real-time voice, bidirectional audio, ambient context — is announced as a user benefit. And it is a user benefit, genuinely. The product gets better. But each capability also deepens the data collection relationship. Memory means the system accumulates a longitudinal profile. Real-time voice means latency-sensitive audio streaming to external servers. Bidirectional audio means an always-on pipeline. Ambient context integration means the AI learns your organizational structure, your priorities, your language, your people.

The product improves and the extraction deepens simultaneously. These are not separate processes. They are the same process.

ChatGPT's new Dreaming V3 memory architecture, rolled out in June 2026, reads across years of past conversations and rewrites what the system remembers about you — automatically, in the background, without prompting. "You're going to Singapore in July" becomes "you went to Singapore in July 2026" after the fact. The model is building a model of you, revising it continuously, and the controls for managing that knowledge are not a single toggle.

---

## What Changes, and What Doesn't

None of this means AI tools aren't useful. They are extraordinarily useful — perhaps the most significant productivity technology in decades. The argument is not to reject them. The argument is to understand what is actually being exchanged in every interaction. And not just the attack surface - the privacy implications are staggering. The surveillance state we have been warned about for a century or more isn't around the corner - its already here and no one even noticed.

Google built the greatest advertising business in history by making search so indispensable that users couldn't consider the cost of using it. Facebook built the dominant social graph the same way. The value was real. The extraction was real. Both things were true simultaneously, and the second one took years to become visible.

AI assistants are at the beginning of that same arc — but accelerated, and with access to something far more valuable than what we gave Google and Facebook. We gave those platforms our attention and our social connections. We are giving AI our cognition, our business logic, our strategy, our voices.

The next time you @tag a confidential document into a chat, or describe a competitor's weakness to an assistant that logs and potentially trains on your input, or enable real-time voice in a meeting where proprietary matters are discussed — the question worth asking is simple:

Who else is in this room and what am I giving away for free?

---

*Research basis: OpenAI advertising launch (CNBC, Forbes, OpenAI.com, January–May 2026); GPT-Bidi-1 disclosures (Let's Data Science, Kie.ai, Windows News, Open the Magazine, 2026); Microsoft Copilot vulnerabilities (SecurityToday, Truesec, Hexnode, Dark Reading, Lasso Security, Cybernews, 2025–2026); Google Gemini privacy analysis (terms.law, Concentric.ai, Cape.co, 2026); Enterprise AI data leaks (eSecurity Planet, Harmonic Security, Cyberhaven, 2025–2026); ChatGPT Memory Dreaming update (TechTimes, June 2026).*

*Lars Klander writes about cybersecurity strategy, policy, and emerging threats, as well as Australian Privacy Protections and Data Sovreignty.*