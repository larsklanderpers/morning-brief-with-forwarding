# Research note: Instinct (invite-only personal agent over iMessage)

Date: 25 Sep 2026. Status: background "hmm?" item, not blocking any piece.
Scope: who makes it, how it works, access and price, privacy/terms, dates, and how it stacks up against Meta Muse and xAI Grok Bot.

## Headline

Instinct is a text-or-call personal agent from Spear Street Technology, Inc. d/b/a Instinct (San Francisco), founded by Noah Shinn (23, ex-Sierra research scientist). Invite-only beta, free, no published price. Series B of $250M at $2.5B (Index, Benchmark) in late Aug 2026; reports of talks at $10B since. Users praise it for doing things (bookings, cancellations, calls, bill haggling) with almost no setup and without stopping to ask. The same trait is the main criticism: it acts without confirmation, it retained Gmail copies after disconnect, it is prompt-injectable via email, and its terms put all liability for its actions on the user.

Flag for Lars: every source reached says Instinct is currently free. If Lars is paying for something, check what the charge is (the Terms reserve the right to charge fees but list no plans or amounts).

## 1. Who makes it

- Legal entity: Spear Street Technology, Inc. d/b/a Instinct. Source: Instinct Terms and Privacy Policy, both "last revised on August 26, 2026" (https://instinct.com/terms, https://instinct.com/privacy-policy). instinct.co 302-redirects to instinct.com.
- Founder/CEO: Noah Shinn. Founder intro post on X, 26 Aug 2026 (quoted in thread under https://x.com/pranavreddy/status/2092710913329770808): "I'm Noah, the founder of Instinct... building for the past few months... You can text or call it. It's trained to use a phone and a computer in the same way that humans do... invite-only beta program while we're actively bringing up more compute."
- Background: ex-Sierra (Bret Taylor's company) per Forbes and SiliconANGLE; Northeastern undergrad per investor Pranav Reddy (Conviction). Reflexion and tau-bench research attributions appear only in a KuCoin news flash (not reached; secondary).
- Funding (see CONTESTED for discrepancies):
  - TechCrunch, 26 Aug 2026: $250M Series B co-led by Index Ventures and Benchmark, $2.5B valuation, $350M total raised. https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/
  - Forbes (Iain Martin), 26 Aug 2026: seed at ~$50M valuation led by Pranav Reddy (Conviction), Neil Mehta (Greenoaks) also in; Series A early Aug, $75M at $500M+ led by Mamoon Hamid (Kleiner Perkins); Series B "in talks" $200M+ at $2.5B+. Company registered April 2026. https://www.forbes.com/sites/iainmartin/2026/08/26/vcs-are-so-obsessed-with-this-ai-assistant-that-its-valuation-jumped-fivefold-in-weeks/
  - SiliconANGLE, 27 Aug 2026 (citing WSJ): $250M at $2.5B; previous round $100M from Conviction and a Greenoaks consortium. https://siliconangle.com/2026/08/27/consumer-focused-ai-assistant-startup-instinct-reportedly-raising-250m/
  - PYMNTS, 16 Sep 2026 (citing The Information, 15 Sep): in talks to raise $1B at $10B post; says prior round was $250M at $2.25B; 100,000+ beta users; CEO has "no current plans to charge users"; ads floated as possible revenue. https://www.pymnts.com/startups/2026/instinct-ai-assistant-targets-10-billion-dollar-valuation/

## 2. What it does and how

- Interface: no app required to talk to it. You text it (iMessage, WhatsApp) or call it; it can also call and text you proactively. Web dashboard at app.instinct.com for settings, connectors, Vault, data deletion. Sources: instinct.com homepage; Claire Vo thread ("i set up imessage -- delightful experience"); Aakash Gupta review (iMessage and WhatsApp, onboarding under a minute).
- Connects to (homepage): "email, messaging, screen, audio, and location." Users report Gmail/Google Calendar, WhatsApp, 1Password, Slack, Granola, Substack, card-on-file via its "Vault," and a dedicated agent email alias (firstlast@mail.instinct.com per fabian @fabianstelzer).
- Actions (first-hand, Sheel Mohnot, 20 Aug, 677 messages in five days; https://x.com/pitdesi/status/2090579987778937159): found in-network podiatrist and filled paperwork; got Comcast from $100 to $60/mo (hit a wall, gave him a call script); negotiated with merch vendors on WhatsApp overnight; booked spa activities, emailing the hotel from his account; DMV appointment; canceled Amazon Subscribe & Save; activated card offers; linked United itineraries via airline chat; paid toll notices from a photo.
- Other first-hand: award-seat monitoring and booking, Cloudflare billing monitoring with a read-only token, PR tracking, reads OTPs from email to complete checkout (Anirban Chowdhury, 11 Sep, https://x.com/VoyageBliss/status/2098368354646167724).
- Architecture: persistent cloud computer with browser and cached credentials (per Vellum and investor Anish Acharya quoted by usecarly; secondary). Claire Vo's export showed every email converted to .md on a filesystem.
- Memory: one long-running thread stored server-side; users say memory carries across tasks (Aakash Gupta; Scott Belsky: "reasoning, judgment, and memory is just better"). The data deletion tool added 22 Aug deletes synced data but keeps conversation history and generated memory (Claire Vo).
- Payments: Stripe Link payments for Instinct and "users who buy things through it spend over $1,300 a month" (Matt Van Horn roundup; UNVERIFIED, no primary found).
- Model: undisclosed.

## 3. Access model and price

- Invite-only beta; waitlist at instinct.com; existing users get invite links (Sheel gave out 100+ in two minutes; invite URLs posted publicly as app.instinct.com/invite?t=...).
- Price: free, no published pricing (Forbes, PYMNTS, Aakash Gupta, AI Interview Agents). Terms: "You may be required to pay us fees to access or use certain features" and "all payments are non-refundable," but no plan names or amounts.
- Age: 18+ (Terms).

## 4. Privacy and data handling (from its own docs)

Privacy Policy and Terms, both revised 26 Aug 2026 (the same day as the funding news):
- Collects message and email content, audio/voice, precise geolocation (if shared), payment credentials, third-party passwords, health info, and clickstream "(keystrokes, clicks, cursor positions)."
- Training: default on. Opt-out at app.instinct.com/settings, but "we may still use your information for AI model training when that information is flagged for safety review." Google Workspace data and Vault materials are excluded from training. No equivalent carve-out found for WhatsApp, iMessage, audio or location.
- Sharing: with "third-party AI model providers who help support the Services" and vendors. "We do not sell your information or disclose your information to registered data brokers." No explicit retention period.
- Agency: "You hereby appoint the Services as your agent to enter into agreements, commitments or transactions on your behalf." For purchases, "you, not us, are making such purchase." User is responsible for "all consequences... arising from any Action."
- Liability cap: greater of $100 or what you paid in the past six months. Binding individual arbitration, 30-day opt-out, class-action waiver. Company may delete accounts "for any or no reason."
- The current Terms do NOT contain "perpetual" or "irrevocable." The earlier version reportedly did ("perpetual and irrevocable" license incl. training; Forbes, TechCrunch Muse piece, usecarly). Many posts still quote the old language as current.
- Neither document mentions iMessage or WhatsApp by name.

## 5. Dates

- Company registered April 2026 (Forbes). Private beta start: Feb 2026 per SiliconANGLE; "past few months" per founder on 26 Aug; Reddy says he has spent "ten months" of Fridays at the office. See CONTESTED.
- Viral moment: Sheel Mohnot post 20 Aug 2026. Claire Vo retention thread 21 Aug. Deletion tool shipped overnight 21-22 Aug. Founder public intro and Series B news 26 Aug. Terms rewrite 26 Aug. $10B talks reported 15 Sep.
- No general-availability date announced.

## 6. Vs Meta Muse and xAI Grok Bot

Baseline facts:
- Muse: launched 8 Sep 2026; web (muse.ai), iOS, Android, WhatsApp; free tier plus Power $20/mo and Maximum $100/mo; U.S. at launch; runs in a "Muse Secure VM" without visibility into passwords or payment methods; Meta says conversations are not shared with ads systems; Stripe Link checkout; 1Password and Shop Pay "coming soon." TechCrunch, https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/
- Grok Bot: launched 11 Aug 2026 (beta); desktop and iOS apps plus X; each bot has its own cloud computer, signs into tools, works across apps without APIs; available to SuperGrok, SuperGrok Plus, SuperGrok Heavy and certain Cursor plans, usage billed separately. xAI, https://x.ai/news/introducing-grok-bot

| | Instinct | Meta Muse | xAI Grok Bot |
|---|---|---|---|
| Interface | iMessage/WhatsApp text, phone calls; web dashboard | Own app, web, WhatsApp | Desktop + iOS app, X; team of bots |
| Access | Invite-only beta, waitlist | Open (U.S. at launch) | Beta for paid SuperGrok/Cursor tiers |
| Price | Free, none published | Free / $20 / $100 per month | Tied to SuperGrok tiers; per-bot cost CONTESTED |
| Autonomy | Acts first, rarely asks | More cautious, less aggressive | Stops at passwords, 2FA, CAPTCHAs, payments |
| Memory | One long thread, server-side | Learns from conversations, suggests unprompted | Isolated context per bot |
| Security posture | Retention-after-disconnect (fixed with tool), email prompt injection shown, liability on user | "Well documented security architecture," secure VM | Hand-back at sensitive steps |
| Model | Undisclosed | Meta | Grok 4.5/4.6 (per Van Horn) |

What users/reviewers say Instinct does BETTER:
- vs both: zero-setup, no new app, "OpenClaw for normal people" (Sheel Mohnot); finishes chores without stopping for confirmation, which "kills the vibe" in others (Sheel); proactive (checks you in to flights, flags forgotten reservations; Kenan Saleh via Van Horn).
- vs Grok Bot: simpler than managing a team of bots; Christian Pean MD (Substack, 23 Sep, self-disclosed conflict: building clinical AI tools) called Instinct the "clear winner" and said managing Grok Bot's bots "became overwhelming." https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes
- vs Muse: Pean found Muse "less aggressive" at executing tasks than Instinct.
- Judgment and memory: Scott Belsky, "something about its reasoning, judgment, and memory is just better."

What users/reviewers say Instinct does WORSE:
- Safety and control vs Grok Bot: "Grok Bot stops for a human decision at the precise moments Instinct did not" (Van Horn summarizing Shashi Bellamkonda). Sent an email without approval (reported, primary not reached).
- Security architecture vs Muse: Adam MacBeth, 8 Sep: "Muse is really good. Seriously fast and a well documented security architecture. I've already forgotten about Instinct, Poke, etc." https://x.com/adamac/status/2097420929383141720
- Transparency vs Muse: Business Insider's Henry Chandonnet preferred Muse for trip planning (maps, ticket tracking); on Instinct, "you can't see exactly what it's doing," and he was unsure how personalization worked. Read via a syndicated copy only (see Unreached).
- Prompt injection: Alex Cohen's test email to his own inbox succeeded, then he deleted his account (via Van Horn/usecarly); fabian (@fabianstelzer, 10 Sep) says Instinct tries to trust only the primary messenger but email is "very convenient and breakable." Anirban Chowdhury: no independent security assessment of its Vault or injection defenses.
- Data retention: Claire Vo found it kept copies of her Gmail after disconnect and could be "one-shot" into emailing that package to arbitrary addresses (21 Aug). Instinct shipped a deletion tool within about 15 hours.
- Access: Muse is open to anyone in the U.S. with a free tier; Instinct needs an invite.
- Costly mistakes: "$200 no-show fees on flights their agent booked wrong" (reported by Aakash Gupta, secondhand).
- Grok Bot better for "leverage over a portfolio of work" if you pay top-tier (Van Horn).

## SOLID (primary or multiple independent)

- Company is Spear Street Technology, Inc. d/b/a Instinct; founder/CEO Noah Shinn. (Terms, Privacy Policy, founder post.)
- Text-or-call interface, invite-only beta, compute-constrained rollout. (Founder post, homepage.)
- Free today, no published pricing. (Forbes, PYMNTS, multiple users; Terms list no amounts.)
- $250M Series B at $2.5B co-led by Index and Benchmark, late Aug 2026. (TechCrunch, SiliconANGLE/WSJ, Forbes as "in talks.")
- Terms and Privacy Policy revised 26 Aug 2026; training on by default with opt-out, safety-review exception, Google Workspace and Vault excluded; agent appointment; $100 liability cap; arbitration.
- Claire Vo retention-after-disconnect incident and next-day deletion tool. (Her own thread.)
- Muse launched 8 Sep 2026 with free/$20/$100 tiers; Grok Bot launched 11 Aug 2026 as beta for SuperGrok/Cursor subscribers. (TechCrunch; xAI.)

## CONTESTED

- Total raised and prior rounds: TechCrunch $350M total; Forbes seed plus $75M Series A (Kleiner) plus Series B; SiliconANGLE prior $100M from Conviction and Greenoaks. Series B valuation $2.5B (most) vs $2.25B (PYMNTS).
- Beta start: Feb 2026 (SiliconANGLE) vs company registered Apr 2026 (Forbes) vs "past few months" (founder, 26 Aug).
- "Perpetual, irrevocable" license: in the pre-26-Aug terms per multiple reports; not in current Terms. Many 2026 posts cite it as current.
- Grok Bot cost: $120/seat/month (Pean) vs "$200 to $300 a month" and SuperGrok Heavy $300 (Van Horn); xAI page lists tiers but no dollar amounts in the excerpt reached.
- Muse availability: U.S. only (TechCrunch) vs U.S. and Canada (AI Interview Agents, secondary).
- Head-to-head verdicts split: Pean picks Instinct; Business Insider and MacBeth prefer Muse; Van Horn says "not competitors yet."

## UNVERIFIED

- $1B raise at $10B post and 100,000+ beta users (The Information via PYMNTS; The Information not reached).
- Users who buy through it spend over $1,300/month; Stripe shipped Link for it (Van Horn roundup, no primary).
- Katie Jacobs Stanton unauthorized email; Katie Chiou ticket-queue crashes (only via usecarly, a competitor; primaries not reached).
- "$200 no-show fees" on wrongly booked flights (secondhand in Aakash Gupta).
- Shinn's Reflexion / tau-bench authorship (KuCoin flash, not reached).
- Instinct model identity (undisclosed; SiliconANGLE speculates).
- Muse human contractors making calls without disclosure, later paused (Pean only).

## DO-NOT-PRINT (unfooted)

- Any Instinct price or subscription tier. None exists publicly.
- "$10B valuation" as fact (it is reported talks).
- "100,000 users" as fact.
- "Perpetual and irrevocable" as the CURRENT terms.
- "$1,300/month user spend" and "Stripe built Link for Instinct."
- Stanton, Chiou and "$200 no-show fee" anecdotes as fact.
- Grok Bot "$120/seat" or any single Grok Bot price.
- Any claim that Instinct uses a specific model.
- Vellum's list of "known issues" as independent reporting.

## Sources and commercial interest

Primary:
- Instinct homepage https://instinct.com/ ; Terms https://instinct.com/terms ; Privacy https://instinct.com/privacy-policy
- Noah Shinn founder post, 26 Aug (quoted within Pranav Reddy thread) https://x.com/pranavreddy/status/2092710913329770808 (Reddy is an investor, Conviction)
- xAI, Introducing Grok Bot https://x.ai/news/introducing-grok-bot

First-hand users (X, via firecrawl):
- Sheel Mohnot https://x.com/pitdesi/status/2090579987778937159 (VC; replies from Simon Taylor, Scott Belsky)
- Claire Vo https://x.com/clairevo/status/2090929592853037078 and https://x.com/clairevo/status/2090970541557698755
- Anirban Chowdhury https://x.com/VoyageBliss/status/2098368354646167724
- fabian https://x.com/fabianstelzer/status/2097928966535320044 (builds a competing "creative super agent," glif)
- Adam MacBeth https://x.com/adamac/status/2097420929383141720
- Matt Van Horn roundup https://x.com/mvanhorn/status/2095007828742397982 (aggregator output of his own last30days tool; quotes others)
- Shashi Bellamkonda https://x.com/shashib/status/2093299149848424654 (commentary, not a user report)

Reviews:
- Aakash Gupta, 18 Sep https://www.aibyaakash.com/p/instinct (newsletter; hands-on)
- Christian Pean MD, 23 Sep https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes (self-disclosed: building clinical AI tools)

News:
- TechCrunch (Instinct) https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/
- TechCrunch (Muse) https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/
- Forbes https://www.forbes.com/sites/iainmartin/2026/08/26/vcs-are-so-obsessed-with-this-ai-assistant-that-its-valuation-jumped-fivefold-in-weeks/
- SiliconANGLE https://siliconangle.com/2026/08/27/consumer-focused-ai-assistant-startup-instinct-reportedly-raising-250m/
- PYMNTS https://www.pymnts.com/startups/2026/instinct-ai-assistant-targets-10-billion-dollar-valuation/

Secondary, vendor-adjacent (commercial interest named):
- Vellum https://www.vellum.ai/blog/official-instinct-breakdown -- sells a competing personal AI assistant ($30 to $200/mo, open-source self-host).
- usecarly https://www.usecarly.com/blog/what-is-instinct-ai/ -- sells a competing email/scheduling agent (from $35/mo), pitches "no screen monitoring."
- profitablefounder.xyz https://www.profitablefounder.xyz/blog/instinct-ai -- founder of Distribb; sells podcast sponsorships and a paid founder club.
- AI Interview Agents https://www.aiinterviewagents.com/blog/meta-muse-vs-instinct -- sells hiring/interview software; SEO content.
- Jingletree syndicated copy of Business Insider (Henry Chandonnet) https://jingletree.com/i-used-muse-instinct-and-grok-bot-to-plan-my-european-vacation-meta-s-ai-agent-was-my-favorite-275268.html -- aggregator; original not reached.
- Seen in search but not read: cellcog, spinnable, alphamatch, agent37, the-ai-corner, refix.ai, porteden, faraday.email, codemypixel, mindstudio, mem0, layer3labs (most sell competing agents or tooling).

## Unreached

- Business Insider original (MSN copy blocked by robots.txt; not routed around). Read only via Jingletree syndication.
- The Information (15 Sep) and WSJ (27 Aug) originals: paywalled, not reached.
- Katie Jacobs Stanton, Alex Cohen, Katie Chiou primary posts.
- Instinct help docs or FAQ: none found on instinct.com; app.instinct.com is login-gated.
- Grok Bot pricing page; Muse terms/privacy docs.
- YouTube comparisons (F7LVJbM78S4, _LPFQU1abWY): not watched.
