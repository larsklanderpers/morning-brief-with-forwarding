# Research note -- Muse by Meta, for the Sat 19 intro aside

**Written 15 Sep 2026 (Sat 19 chat). Firecrawl served most pages from cache, fetched 13-15 Sep. No draft yet.**
**Use: a brief, load-bearing first-person aside in the Sat 19 intro, before "how I built my own". His experience is the payload; this note foots everything around it.**

## SOLID -- at a Meta primary

**Launch.** Newsroom, 8 Sep (https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/): "Muse is rolling out in the US on iOS, Android, and muse.ai, and coming soon to AI glasses. It's free for most of what people need, with subscription plans for people who want to do more." You talk to it "in the Muse app or directly in WhatsApp." "It doesn't just answer questions, it actually does the work." "For tasks that take more time, Muse keeps working after people close the app, and comes back when something changes or when it needs approval." It "remembers what matters to a person, so it can make suggestions unprompted and act on details that person only mentioned once."

**Model.** Muse Spark 1.3 (safety post, https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse, byline Tarek Sheasha): "Driving the web browser to achieve the user's goal is something the Muse Spark 1.3 model is particularly good at." Internal codename Hatch (footnote).

**Pricing** (Meta Help Center, https://www.meta.com/help/subscriptions/1021145227643680/): "Power plan ($20/month) - 500M Muse tokens per week"; "Maximum plan ($100/month) - 3B Muse tokens per week"; "Muse is available for free with a usage limit." Also: "Muse and Muse subscriptions are in limited testing and aren't available in all locations yet." Free-tier number only from Zuckerberg (https://x.com/finkd/status/2097402101332590646): "free to use for up to 100M tokens per week" -- attribute to him, not to Meta docs.
- ★ **Same $20 as the Grok Bot entry price quoted in Sat 12.** Different metering (Muse: weekly token allowance; Grok Bot: weekly reset plus on-demand). Usable as a one-clause rhyme, not an argument.

**Security architecture** (safety post):
- "Sentinel is a separate host-side agent from your Muse. It is the sole permission authority for approval to perform actions with connectors to third-party services and for all egress over the network. Muse proposes actions, but only Sentinel can grant permission to perform action."
- "The right mental model is two isolated security domains on one box, not an LLM powered agent with root."
- "The agent never sees real tokens."
- "Muse has support for obtaining one-time, session-scoped, task-scoped, time-bounded, or perpetual permission."
- Newsroom: "Muse shows people a complete audit trail of everything it has done and plans to do."
- "Muse isn't immune to attack. Prompt injection remains an open problem in the industry."
- Bug bounty "up to $300,000 for valid reports, including up to $130,000 for successful prompt injection attempts that affect one user."
- ★ **Direct contrast with Sat 12's central finding** (Grok Bot: "Your Bots share one computer", no boundary beyond good behavior). Muse's pitch is the opposite design: a per-person VM plus a separate permission authority. Sat 12 readers will feel that contrast without being told; one sentence at most.

**What Meta can access -- the commercial interest, name it in the text.** Safety post: "It restricts access to your data by Meta personnel through operational policies. It does not prevent Meta from accessing data when necessary to support, secure or operate the service." Confidential VM, "encrypted with a key only they hold, so not even Meta can access it", is "later this year" (newsroom) and with "a small group of trusted testers" (safety post). **Not shipped.**

**Data use.** Training is ON by default, opt-out: "We think this is a good default ... you can opt-out via a simple switch in Muse settings." Ads: "Muse doesn't share your conversations or the data in your Virtual Machine with Meta ad systems" -- then: "there are some legitimate scenarios where how you use Muse can influence the ads you see. When Muse browses the internet, it will appear as your activity."

**Meta's own cautions.** "Your Muse may be inaccurate or take unexpected actions. Monitor its actions carefully and intervene as needed." (https://www.meta.com/help/artificial-intelligence/1331373868832401/). "You're responsible for all transactions your Muse makes on your behalf." (https://www.meta.com/help/artificial-intelligence/1436362127544482/).

## CONTESTED
- **Availability.** Newsroom "rolling out in the US"; help centre "limited testing"; TestingCatalog "isn't available to everyone"; a reply to Volkov says wait-list / invite code. **Print "rolling out in the US", never "available".**
- **Age.** AP: "for people 18 and over". Meta's page states 18+ only for subscribers.
- **Staff testing failures** (exposed iCloud photos; logouts reported by Bosworth) -- Forbes citing Reuters; Reuters unread. Not printable as fact.

## SIGNAL (who, and their verdict)
- **Praise.** The Verge, Emma Roth, hands-on (https://www.theverge.com/tech/993391/meta-muse-ai-hands-on): "Muse delivered on its promise of handling life's more mundane tasks in the background"; deleted "thousands of promotional emails"; noticed other cart items before an Amazon order -- "The consideration pleasantly surprised me." Alex Volkov (bio: "Host of @thursdai_pod ... AI Evangelist with @wandb & @coreweave"), video review: "Verdict: genuinely impressed", but also a chapter "Turn this off on day one (training opt-out)". TestingCatalog: "WhatsApp connection is available from the start"; "Soul and Memory files are easily accessible and editable." HN commenter modeless: "It's hilarious that Meta made a good AI integration for Gmail before Google did."
- **Critique.** Same Verge piece is headlined as working and creeping her out: Muse listed her Instagram interests, saying "I read it through the account's API data, which surfaces more than the UI does"; Meta spokesperson Emil Vazquez: Muse can "pull and infer interests based on your IG activity." TechCrunch, Sarah Perez: "Meta has a history of proclaiming one thing and doing another" (2011 FTC settlement, 2019 $5B penalty); security claims "will require deeper investigation by security experts." TechRadar (metadata only): "remarkably capable at handling digital errands, but its usefulness depends on granting an unsettling amount of access."
- **Shape of the signal:** the reviewers who used it for household errands liked it; the critique is almost entirely about trusting Meta with the access, not about whether it works. **That split is exactly his aside:** outstanding for personal use, and the access question is the price.
- **Comparisons.** 9to5Mac: "Similar to Grok Bot in presentation"; "Unlike other systems, Muse is free upfront with weekly limitations." Nothing substantive vs OpenClaw or Hermes.

## DO NOT PRINT
- "Requires a card to start" (TechCrunch only; no Meta page says it).
- "End-to-end encrypted" / "Meta cannot see your data" -- that is the unshipped Confidential VM.
- "Never affects your ads" -- Meta says browsing can.
- "Training is opt-in" -- it is opt-out.
- "Available" / worldwide / EU -- US rollout, "limited testing".
- A community note on Zuckerberg's post -- none found.
- Simon Willison, Stratechery or Platformer "reviewed Muse" -- not found. (Meta's post quotes Willison's 2025 lethal-trifecta essay; that is not a review.)
- Staff-failure anecdotes as fact (Reuters via Forbes, unread).
- Free-tier token figure as a Meta-doc fact (Zuckerberg only).
- Any FTC/settlement dollar figure beyond TechCrunch's $5B 2019 penalty (Forbes and TechCrunch disagree on the 2026 settlement).
- "Negotiates successfully" -- Meta marketing claim; no reviewer tested it.
- Current titles for Sheasha, Singleton, Shah, Wang, Vazquez -- from press/metadata, not their own bios. Fetch the bio before printing any title.

## Gate note
Saturday gate still PASS: the subject is his build. **The aside must stay an aside** -- a vendor product as the subject is an automatic Saturday fail, so Muse gets one short beat that sets up why he built his own anyway, and does not grow a section.
