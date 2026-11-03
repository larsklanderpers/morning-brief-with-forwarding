# Research note -- Sat 24 Oct 2026 -- Duet, Grok Bot, Projects: a personal agent stack  [Saturday, personal]

Written 23 Oct 2026. Three parallel research passes, primaries read live 23 Oct. His brief (23 Oct): *"take it as a personal agent story -- duet for the personal, small business agent and Projects as agentic support for the developer. Let's also in between them check in on Grok Bot and how it fits into the stack."*

## SATURDAY GATE (run 23 Oct): PASS, with two watches
- **Human feature, one line:** a three-agent personal stack you can have this month -- Duet for the house and the small business, Grok Bot for the standing staff in the background, Projects for the code -- with what each costs and what each will not do.
- **Action is build/install/try:** join the Duet waitlist and hand it one chore; set one Grok routine; brief one Project. Not an audit.
- **Watch 1 -- survey drift.** Three products can turn into a review roundup heavier than the weekdays. Keep it HIS stack and how they hand work to each other; one section each, no spec tables.
- **Watch 2 -- incident as subject.** Straiker's CyberCartel report is weekday material. One line at most, or out.
- Arc: none needed (Saturday). Pays part of Sat 10's printed promise ("child bots versus bots you talk to directly ... a coming Saturday") if the Grok section uses his Artemis structure.

## SOLID -- Claude Duet (launched 21 Oct)
Primaries: https://claude.com/resources/articles/claude-duet (21 Oct) · https://claude.com/product/claude-duet · https://support.claude.com/en/articles/17631495-get-started-with-claude-duet · https://claude.com/resources/articles/claude-duet-safety-privacy-and-security (23 Oct)
- "a new app where Claude works as a proactive agent" ... "We built Claude Duet for professionals and small business owners with more on their plates than they can track." iOS, Android, claude.ai.
- Research preview, "Pro and Max plans in the US, through a waitlist"; "isn't available on Team or Enterprise plans yet"; "Access opens in waves."
- "included with the Pro and Max plans at no extra cost" during preview; uses plan limits; background work "also counts, so you may reach your limits sooner." New users get "one full limit reset ... until November 30, 2026."
- Runs on "a virtual machine with its own browser, so it doesn't require your laptop or phone to be on."
- Morning brief each day; "checks your connected accounts every few hours, because checking nonstop would use up your plan's limits much faster." Carries over "your memory, skills, and connected apps from your Claude account."
- Connectors: "Gmail, Google Calendar, Google Drive, Slack, QuickBooks, HubSpot, Docusign, and Calendly"; Stripe / Link / Shop Pay purchases on "a one-time card that only works for that purchase." "Microsoft 365 isn't available yet."
- Asks first: "before it sends a message, makes a payment, signs a document, or deletes anything, it shows you exactly what it's about to do and waits for your approval."
- **Never list:** "Some actions are off-limits even with your approval, such as trading securities, moving money between accounts, or accessing someone else's account." Never shares "sign-in credentials, full card and bank account numbers, and government ID numbers ... even if you ask."
- Limits: "You can't choose a model." "You can't watch Claude Duet work in its browser or take over the browser." No calls or texts to others. "can't see all of your projects or the files on your computer." Personal errands "aren't quite as strong."
- Small-business examples (Anthropic's): unpaid invoices in QuickBooks/Stripe + draft reminders; "Prepare and run payroll in Gusto"; Docusign; HubSpot follow-ups. Testers: Pro Homes (real estate), Shahs of Kabob ("about 110 employees").
- Starter asks (help article): "Clear out anything in my inbox that I don't need to read." / "Check Stripe for unpaid invoices and draft reminder emails for me to approve." / "Pull together a brief on this company before my 2 pm meeting."
- 1Password sign-in is **"coming soon"** (Anthropic and 1Password both). Not live.

## SOLID -- Grok Bot (now SpaceXSI)
Primaries: https://x.ai/bot · https://x.ai/pricing · https://x.ai/news/x-subscription (12 Oct) · https://x.ai/news/introducing-grok-bot (11 Aug) · https://x.ai/news/designing-grok-bot (3 Sep) · https://x.ai/news/team-bots (28 Sep) · https://1password.com/blog/1password-for-ai-agents (22 Oct)
- x.ai pages now carry **SpaceXSI** (xAI joined SpaceX 2 Feb 2026). Built on Cursor infrastructure.
- "your team of always-on agents. They have their own computer"; "Every Grok Bot shares one persistent cloud computer ... Isolation is per user, not per Grok Bot."
- **PRICE CHANGED -- Sat 12 Sep's "twenty dollars a month" is now stale.** 12 Oct "The X Subscription": Free $0 / Plus $8 / **Premium $30** / Super $100 / Ultra $200. Grok Bot "is included with Premium, Super, Ultra, Teams, and Enterprise" -- so **$30 is the floor for new subscribers.** "Nothing changes for existing SuperGrok, Cursor, or X Premium subscribers." Pool now shared: "covers Chat, Imagine, Voice, and Bot." Weekly reset; top-ups at token cost.
- Child bots / chief of staff: "A chief of staff sits on top, with a specialist for each lane." Bots message each other; "practical limits of roughly 50 Bots per account and six per group chat." (His 30+ fits.)
- Routines: "a standing responsibility that runs on a schedule or in response to an event."
- Connectors mostly by signing in through its own browser, "including platforms with no clean API or MCP."
- 1Password: "integrations rolling out over the coming days."

## SOLID -- Claude Projects (the new, agentic version)
Primaries: https://claude.com/resources/articles/projects-redesigned (17 Sep) · https://code.claude.com/docs/en/claude-projects · https://support.claude.com/en/articles/9517075-what-are-projects
- **⚠️ Two products share the name.** The NEW Projects (beta) is agentic and lives in **Claude Code** (claude.ai/code, desktop, mobile; "not in the terminal CLI, the VS Code extension, or the JetBrains plugin"). The CLASSIC chat Project is still a folder of instructions and files. "Projects are designed for long-running or agentic workflows" applies to the new one only. **Say which in the sentence.**
- "A project is one ongoing conversation where Claude coordinates a stream of related work ... it starts a thread for each task." Brief it "the way you'd brief a chief of staff" (Anthropic's phrase -- note the overlap with his Artemis).
- "Cloud threads keep going after you close your laptop." Watches PRs with auto-fix: "pushes fixes when CI fails, addresses review comments." Scheduled tasks run as threads. Local threads via Remote Control (v2.1.280+). Defaults to Opus at high effort.
- Holds: repos + files + instructions ("up to 16,000 characters") + `MEMORY.md`; each repo's `CLAUDE.md` (not its skills or settings). GitHub.com only. "200 new threads per day."
- Pro and Max, public beta, rolling out; not Team/Enterprise; "chat, Cowork, Team, and Enterprise will follow." "A project belongs to one user. You can't share a project."
- Usage counts against plan limits; "on a Pro plan in particular you should expect to reach your limit sooner." Pro $20 monthly ($17 annual); Max from $100.
- Anthropic's examples: cut checkout p75 latency with parallel threads and PRs; retire a v1 endpoint across API/web/mobile repos ("a thread per repo"); "Build what `docs/spec.md` describes". Admitted weakness: overlapping threads resolve "as a merge conflict just like any other PR."

## THE STACK, in their own words (for the shape of the piece)
- All three now sell the same shape: an always-on agent on its own cloud machine, a chief of staff over specialists, and a usage pool that background work drains. **The economics line he will want:** Duet = $0 extra on Pro $20 / Max; Grok Bot = $30 floor for new subscribers; Projects = $0 extra on Pro / Max. Background work burns the same limits in all three.
- The differences that matter to a reader: Duet has a hard never-list and cannot be watched; Grok bots share one computer and are built around child bots; Projects is the only one aimed at code and the only one that cannot be shared.

## CONTESTED / SINGLE-SOURCE
- Duet + M365: product page logo strip shows Microsoft/Office 365; help article says "isn't available yet." Use the help article.
- Thurrott says Duet is "supported at launch" on 1Password; both primaries say coming soon. Use the primaries.
- AI Chat Daily: Pro subscribers get Duet "when it reaches general availability" -- not on any primary. Do not print.
- Linas: never-list is "its real pitch to small businesses" -- opinion, paywalled; same issue leads on Ramp (in Duet's logo strip). Attribute if used.
- Straiker / CyberCartel (21 Oct, https://www.straiker.ai/blog/inside-carliy0s-how-cybercartel-used-multiple-ai-models-to-attack-latin-american-banks): Claude models in decision roles, Grok as credential "miners"; Grok MODEL use, not shown to be Grok Bot; "400+" headline only; xAI statement only via Straiker. Straiker sells agent runtime security. **Gate: one line or out.**

## COULDN'T VERIFY
- Duet price after preview; exact check-in interval; contents of the "small business plugin".
- Grok Bot absolute usage per tier (only "3.5x" / "12x" Premium); whether legacy SuperGrok keeps separate Bot usage; personal-bot connector list.
- Date the new Projects reaches chat/Cowork.

## DO-NOT-PRINT
- "twenty dollars a month" for Grok Bot as current (Sat 12 Sep printed it; correct forward in this piece, in public: it is now $30 for new subscribers on the X Subscription, unchanged for existing ones).
- "Projects" as agentic without saying it is the Claude Code version.
- Duet on 1Password as live; Duet on M365; Duet GA pricing.
- Straiker's model names ("Opus 4.7", "Fable 5" etc.) -- Straiker's only.

## OWED FROM HIM (the piece is his stack; none of this is fabricated)
1. Does he have Duet access yet (waitlist), and what did he hand it first? If not, the Duet section is "what I am going to hand it", which is weaker.
2. Where Duet overlaps Artemis: does anything move off Grok, or does Duet sit beside it? Is he an existing SuperGrok/Cursor subscriber (price unchanged) or on the new $30 Premium?
3. Projects: has he run the new Claude Code Projects on a real repo (his public Jev/bot repo?), and what did a thread do while his laptop was closed?
4. The small-business leg: his own business (Player Elite) or a reader's? Customer names only with his word.
5. Sat 10's child-bot promise: pay it here, or keep it for its own Saturday?
