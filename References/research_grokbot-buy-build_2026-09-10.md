# Research Note -- Grok Bot, and what the build side actually is
For: Sat 12 Sep (buy) and Sat 19 Sep (build), the two-parter · Depth: deep, three parallel digs · Date: 2026-09-10

**Commissioned by Lars 10 Sep. All fetched live 10 Sep 2026.**

---

## Bottom line

**The buy side is cheaper, more documented and more alarming than expected.** Grok Bot's entry price is
**$20/month**, not the $120/$200/$300 the secondary sources say. And the two facts that matter most to his
readers are both in xAI's own docs: **Grok Bot runs in Cursor's cloud on Cursor identity**, and **all of a
user's bots share one computer with no security boundary between them.**

**The build side needs its recommendation changed, and one candidate needs killing outright.** ⛔ **The X
account he follows, `@openbotx`, is promoting a Solana memecoin and its repo has been dead since 3 March
2026.** Do not point readers at it. CopilotKit's OpenBot is real and serious but **cannot start without a
commercial licence** despite the MIT badge. **The honest build-side answer is `elie222/rakazo`.**

**And the two threads he sent are one thread. TradBot is Claire Vo's.**

---

## §1 -- TradBot, and the terminology correction

**He is right that TradBot is a sub-element of Grok Bot. The word "plugin" is xAI's for something else,
and the piece has to use their words or it will read as wrong.**

There are **two** marketplaces:

1. **The Bot Marketplace** (`x.ai/bot/marketplace`) -- public catalog of **Bot templates**, i.e. saved
   agent configurations you import. **This is where TradBot is.** Header verbatim: *"69 Bots · 43 creators
   · 9 categories."*
2. **Plugins** -- connectors and MCP servers (Gmail, Slack, Notion, GitHub), inside the app under
   Settings → Plugins. Verbatim from `docs.x.ai/grok-bot/settings-and-notifications`: *"Use Marketplace to
   discover plugins and packaged skills."* xAI's own explainer video: *"Plugins still connect external
   services; Marketplace is for bots."*

### ★★ TradBot is by Claire Vo, and it is a household bot

`x.ai/bot/marketplace/bots/tradbot-2`, **"By Claire Vo"**. Not a trading bot. Verbatim:

> *"Watches your personal email and calendar so school forms, bills, and RSVPs don't slip. Drafts the
> reply, catches the pickup clash, and never sends without you."*

Its published configuration, verbatim: *"I watch your personal email and calendar so the household things
don't slip: school forms, family plans and RSVPs, bills and renewals, appointments, and who is doing
pickup. I'm not work email triage, a finance app, or a general chatbot."*

Setup collects: *"timezone, digest hour = 6:30am default, your name, spouse or partner, other caretakers,
kids (first name, age, grade), schools and teachers, activities with days, pickup owner and time by day,
city, recurring bills to never miss, providers."* Default connectors are Gmail and Google Calendar.

★★ **The paragraph writes itself, and every clause is a verbatim quote.** A one-click import of a
third-party config that xAI explicitly disclaims -- *"This AI bot was created by a third-party user, not by
SpaceXAI. It may act on your behalf"* -- onto a computer xAI's own docs say has no boundary between bots,
whose default ask is personal Gmail and Calendar, and whose setup form collects **your children's names,
ages, grades, schools, teachers and daily pickup schedule.**

**Marketplace cost:** no price appears on any of ~15 pages fetched, and import is one click. ⚠️ **xAI
publishes no explicit "free" statement, so phrase it as "no listing shows a price," not "they are free."**

**Other entries worth naming:** *Home robots* by Sawyer Merritt (Segway Navimow, Matic vacuum, Matter
robots -- physical actuators, one click from a marketplace). *The Morning Newspaper* by Karen X. Cheng.
*Nightly Audit Engineer* by Lingxi Li (unattended cleanup PRs at 4am). *Haggle Bot*, official, drafts
vendor counters off Ramp data. ★ A near-universal tic in the listing copy: *"never sends without you,"
"never posts on your behalf," "never buys unless asked."* Every creator reaching for the same reassurance.

---

## §2 -- The buy side, at the primary

### Price: $20, and every secondary number is a price for something else

**There is no standalone Grok Bot subscription.** `cursor.com/help/grok-bot/plans`, verbatim:

> *"Do I need a separate Grok Bot subscription? No. Access is included with Cursor Pro, Cursor Pro+,
> Cursor Ultra, or a Cursor Teams seat, or through an individual SuperGrok, SuperGrok Plus, SuperGrok
> Heavy, or X Premium+ account link."*

From `x.ai/bot` itself: **Cursor Pro $20/month · SuperGrok $30/month · Cursor Teams Standard $40/seat/month.**
`cursor.com/pricing` lists "✓ Grok Bot access" on the **$20 Pro** tier.

**Resolving the three conflicting numbers:** $120 is a Cursor Teams **Premium** seat and is **not required**
-- verbatim: *"Team admins do not need to assign a Premium seat, and members do not need to request
access."* $200 is Cursor **Ultra**, the top individual tier. $300 is almost certainly SuperGrok Heavy.
⛔ **Do not print $300 as a Grok Bot price.**

**Free trial** is a usage credit, not a time window: *"The Grok Bot free trial is a usage credit rather
than a set number of days, though a 7-day window also applies."*

⚠️ **xAI's own FAQ is stale on eligibility** -- it omits Cursor Pro and plain SuperGrok. Quote `x.ai/bot`
and `cursor.com/pricing`, not the FAQ.

### ★★ It runs on Cursor. This is the buried lede for his audience.

`docs.x.ai/grok-bot/teams-and-enterprises`, verbatim:

> *"Grok Bot is a computer-use agent that operates applications, browsers, and development environments.
> **It runs in Cursor's cloud**, and each user's work executes on a dedicated cloud computer."*

Sign-in is *"Sign In with Cursor."* Admin settings live at `cursor.com/dashboard/bot`. The certifications
are **Anysphere's**: *"Anysphere holds ISO/IEC 27001 and ISO/IEC 42001 certifications, issued by
Schellman, and Grok Bot is included in the current ISO scope."* **The vendor you are diligencing is not
only xAI.**

### ★★ One computer, no boundary between bots

`docs.x.ai/grok-bot/overview`, verbatim:

> *"**Bots share one computer.** All of your Bots use the same persistent cloud computer. They share files,
> browser sessions, and app logins... Each Bot gets its own screen on that computer, so several Bots can
> use browser and desktop tools in parallel **without getting separate security boundaries.**"*

`computer-and-apps`: *"Browser cookies and signed-in sessions are shared · Files are visible to every Bot ·
**Command-line credentials are shared**"* and *"The screens are separate work surfaces, **not separate
security boundaries.**"*

`faq`: *"**Do not use separate Bots as a security boundary.**"*
`security-faq`: *"Each user gets a dedicated Firecracker microVM... **When a workload needs its own
computer and credential set, give it its own Cursor user.**"*
`approvals-security-and-privacy`: *"Deleting a Bot does not remove shared-computer files or browser
sessions."*

### Credential handling is genuinely good, with one hole

`docs.x.ai/grok-bot/security`: *"A Bot has no identity or credentials of its own... **A Bot can never hold
more access than the person it belongs to**"* and *"Connector tokens stay on Cursor's backend. Bots invoke
tools without receiving OAuth tokens, and **tokens are never stored on the computer.**"*
**The hole:** command-line credentials and anything left in `/workspace` are shared across every bot.

### Admin control: most of it is Enterprise-only

`teams-and-enterprises`, verbatim: *"Enterprise only on the Grok Bot dashboard: the organization-wide
enable switch, Network Controls, Team Setup, Action Recording, and computer management... Audit logs,
OpenTelemetry Export, the MCP allowlist, and SCIM are also Enterprise only. **Self-serve Teams do not see
those settings.**"*

For a self-serve Teams customer: no egress control (*"Teams without a policy default to allow-all"*), no
audit log, no org-wide off switch, **no spend cap** (*"A separate Grok Bot spend cap is not available
today"*), cannot push or block connectors per member, cannot lock Auto Review on.

And: *"**Blocking a plugin does not block that service's website**... Closing the website path takes
Network Controls, which is Enterprise only."*

### Local execution -- the paragraph a CISO stops on

`docs.x.ai/grok-bot/security`: *"Bots can act on a member's own machine through the desktop app: **run
commands, read files, and move files between the cloud computer and the local machine.**"* Default is
per-command approval; *"**Recommend Never**"* is xAI's own guidance; and *"a team-level ceiling is enforced
through settings; **a dashboard control for the ceiling is not available today.**"*

### Other primary-source facts worth carrying

- *"Grok Bot computers run in the United States today."*
- *"On-premises deployment... and bring-your-own-image deployment are not supported today."*
- *"Cursor manages model selection. There is no customer-facing model picker."* Team model allowlist is
  Enterprise-only and *"enforcement is not guaranteed."*
- Prompt injection, xAI's own words: *"These controls reduce, but do not eliminate, risk from malicious
  content."*
- Egress: *"shared static egress IP addresses... treat the ranges as identifying Grok Bot traffic rather
  than your team alone."*
- Auto Review *"is model-based and should complement, not replace, least privilege."*

### ★ Two primary-source contradictions, both usable

1. **Billing.** Launch post `x.ai/news/introducing-grok-bot`: *"Grok Bot comes with its own usage,
   separate from your Grok and Cursor plans."* Help doc `cursor.com/help/grok-bot/plans`: *"Grok Bot usage
   is metered on your Cursor account, not on Grok or X."* Cursor's own forum carries a thread titled
   *"Grok Bot: weekly usage hits 100% after bot-to-bot reviews."* **Read the meter, not the launch post.**
2. **Group chat.** xAI advertises *"Put them in a group chat so they pass work between themselves."*
   Claire Vo, after weeks of daily use: *"you can't put a Grok Bot in the group chat. And I want a Grok Bot
   in the group chat."* (video/ASR -- paraphrase rather than quote). **Vendor copy versus lived experience.**

### ⚠️ His own 2 Sep finding survives, narrowed -- correct-forward material

The FAQ still reads *"Backend retention follows the applicable Cursor terms"* and *"Training opt-out
follows the applicable Cursor account and privacy settings"* -- still pointers, page unchanged since
2 Sep. **But the doc set has grown around it.** `security` now states *"with Privacy Mode enabled, customer
data is not used for training"* and gives a 90-day retention for Action Recording. **Admin control is now
largely documented, and the answer is that most of it is Enterprise-only.**

★ **The specific gap he printed is still open, narrowed to Teach-a-task.** Verbatim, unchanged:
*"Teaching records visible computer interaction for up to ten minutes. It does not record microphone
audio. Avoid exposing secrets during the demonstration."* **No retention period, no training statement, no
admin control for teach-by-demonstration recordings.** The 90-day retention belongs to Action Recording,
which is a different mechanism. **That is a precise, defensible restatement and a clean correct-forward.**

### Surfaces, and the CarPlay point

Full platform list, `docs.x.ai/grok-bot/faq`: macOS, Windows, Linux, **iOS 18+, Android 9+**; *"iPad is not
supported at initial launch."* **CarPlay appears nowhere in any Grok Bot page.** The list is explicit
enough (it names iPad) that the silence is meaningful.

⚠️ **The distinction that prevents a correction: Grok the chat assistant DOES support CarPlay; Grok Bot
does not.** xAI's own words, `docs.x.ai/grok/faq`: Grok Bot *"is not the same as Grok on grok.com or the
Grok mobile apps."*

✅ **So his iMessage-as-control-surface idea for next week is sound and now has supporting evidence:** a
community-built skill connects Grok Bot to **iMessage on macOS** via local execution. Not an xAI
integration and not in the marketplace catalog -- which makes it a *more* interesting hook, not less.

---

## §3 ⛔ -- THE BUILD SIDE: kill one candidate tonight

### `@openbotx` is not CopilotKit's OpenBot, and it should not be recommended

They are **two entirely different projects**. `@openbotx` maps to `github.com/openbotx/openbotx` -- a solo
Python project by Paulo Coutinho. **93 stars, 1 contributor, 41 commits, last release `v0.0.10` on
3 March 2026. Seven months dead.**

⛔ **And the account is promoting a Solana memecoin.** Verbatim posts, fetched 10 Sep:

> *"Can someone make a DEX BOOST to me? Don't have money? Only press to share/repost. **$OPENBOTX BOOST
> 🚀** DEX: https://dexscreener.com/solana/7kedu6..."* -- 2 March 2026

> *"🚨 Wow. Project going to moon. 75 starts, 15 forks. Can you help sharing?"* -- 3 March 2026

**Do not point readers at it.** ★ **But it is a better paragraph than a recommendation:** "OpenBot" is a
crowded, unowned name -- there is also `next-open-ai/openbot`, a Chinese-language desktop platform under a
self-described "Restrictive MIT" licence. **Name collisions are exactly how readers get phished**, and this
one has a token attached.

### CopilotKit/OpenBot: the MIT badge conceals a required commercial licence

Real and serious: **4.6k stars, 29 contributors, 292 commits, latest commit the hour it was fetched.**
Genuinely good governance architecture -- gateway evaluates policy, writes the audit row **before**
execution, CEL deny-by-default, secrets recorded as character counts.

⛔ **But CopilotKit's own FAQ, verbatim:** *"The application code is MIT-licensed... **Running it requires
CopilotKit Intelligence, the commercial platform underneath.**"* The server refuses to start without the
Intelligence keys, and Intelligence holds threads and memory.

**Pricing:** Developer tier free but **3-day thread retention**, 200 threads, one developer. Pro $39/mo.
Team $100/seat/mo. ★ **A free tier that forgets everything after three days is a demo, not a free tier, for
something billed as a personal control plane.**

**Setup, honestly counted: 12 steps, two toolchains (Docker + Bun), two vendor signups, a 5.3 GB image
pull.** The repo ships a `prompt.txt` you paste into an AI assistant to do the setup, which is a tacit
admission the config surface is large.

**What breaks:** single replica only (in-process snapshot cache); `OPENBOT_SINGLE_USER=true` ships **on by
default**, admitting every request as an administrator with no sign-in; Docker's DNAT bypasses `ufw`
default-deny. Live issues: restarting the desktop app re-mints the encryption key so stored credentials
become unreadable; an errored tool renders as though it succeeded. ★ Best issue for the piece, `#397`:
*"What now? The example package is three coworkers and a blank page."*

⚠️ **"Bring your own model" is true; "runs entirely on your machine" is not.** Ollama, vLLM and LM Studio
are **never mentioned** in the README. And even with a fully local model, **threads and memory still go to
CopilotKit Intelligence.**

### ★ The build-side answer is Rakazo

`elie222/rakazo` -- self-describes as *"an open source Grok Bot alternative,"* which is the exact head-to-head
this two-parter is built on. **2.2k stars, 68 contributors, 819 commits, `v0.1.6` three days ago, latest
commit the hour it was fetched. Apache-2.0. Beta, not alpha.**

`rakazo.com`, verbatim: *"No pricing page. Just the repo. Rakazo is Apache-2.0 licensed and runs on your
own machine with your own model keys. **Nothing is gated, nothing phones home.**"*

**Setup: three steps** -- install Docker, run one curl-and-bash line, open `127.0.0.1:5173`. ★★ **And there
is a fourth path that matters more than anything else here: the Electron desktop app asks on first run
whether to run Rakazo on this computer, and if you say yes it installs and starts the whole Docker stack
itself.** That is the only genuinely non-developer path found in the entire category.

**Real BYO:** *"Point a bot at Claude, GPT, Grok, or a local model. Swap per bot: the cheap one triages,
the smart one writes."* Runtime is `pi` (`earendil-works/pi`), whose docs give first-class Ollama, vLLM and
LM Studio config. Apache-2.0 also carries an express patent grant that MIT does not -- a real point for
this audience.

**Caveats to state plainly:** still beta; will not run on a 1 GB VPS; optional integrations (Composio,
Pipedream, Treg) have their own terms and Treg is usage-metered, though all three are genuinely optional.

### ⚠️ The absence that should be in the piece

**No independent practitioner report exists for either project.** Searched r/LocalLLaMA, r/selfhosted,
r/AI_Agents, HN. CopilotKit's Show HN scored **14 points** against a 4.6k-star repo -- the stars came from
Trendshift and social, not from people who ran it. The only hands-on write-up is by **SSD Nodes, which
sells VPS hosting and concludes "run this on a VPS."** ★ **This whole category is running on stars and
launch posts rather than on people who have lived with it.** Say so.

---

## §4 ★★ -- Claire Vo, and there is a written source

**The episode:** *"7 Grok Bot agents I use every day"* (YouTube, 36:20, 2 Sep 2026, ~287k views).
Podcast-feed title: *"Grok Bot vs. OpenClaw: How I replaced my entire agent stack."* Solo screen-share,
no guest.

★★ **There is a full written companion post at `chatprd.ai/how-i-ai/grok-bot-agent-templates-and-workflows`
(3 Sep 2026), plus three workflow pages and a public X thread with shareable templates. So almost nothing
needs to come from the auto-transcript.**

**Who she is:** founder of ChatPRD, host of *How I AI*, 3x CPTO (LaunchDarkly, Color Health, Optimizely).
Technical -- she mentions Tailscale and SSH'ing into a Mac mini to maintain her old agents.

### The nine bots, and the corporate/personal blend is the point

**Chief** (chief of staff): hourly sweeps 6am-9pm, seven days, across **six inboxes**, multiple Slacks and
calendars. Deliberately does **not** run overnight -- *"I don't want people to get used to me responding to
them overnight."* Voice-trained with the prompt *"Go through my emails and really pull out my voice"*;
it extracted that she **never uses an em dash**, opens with "hey," signs off "-c".

**TradBot** (family): the kitchen-table newspaper, printed on a physical HP printer each morning. 2:30pm
routine confirming **who is doing pickup and what gear is needed**. Friday weekend-sports logistics across
three kids. ★ Her husband's trick: **email the PDF to a Kindle send-to-Kindle address** so it lands on
e-ink, not a screen.

**Lockdown** (SOC 2): ★ **uses the bot's own browser to log into their SOC 2 control dashboard** (Oneleet,
per her X thread). Daily control checks; on a new vulnerability it **triages, opens a PR with a fix, and
assigns it to her.** Her framing: it doesn't do the compliance work for her, it *"put me to work more
effectively."*

**Holly Helpdesk** (support): ★★ **the best governance mechanic in the episode.** Hourly Intercom and
email sweep. *"She is empowered to request refunds, but not to issue them unilaterally."* Claire gets an
Approve button; clicking opens a **Stripe agent action granting permission for that single transaction.**
Live example: a $19 refund.

**LGTM** (PR closer): ~50 PRs cleared in one Friday; kicks off Cursor cloud agents to do the code work.
**Penny Pincher**: found a dead Apple Arcade subscription, then **moved from cancelling to negotiating** --
spotted home insurance renewing and proposed shopping market rates. **ShopZilla**: found a birth-year
Rolex, researched fair market price, **identified which listings were open to negotiation and started
negotiating.** **Sylvie Style**: prompt *"Go look on Reddit for personal stylists and how they approach
building people's wardrobes"* -- had the agent learn the domain method from practitioners first. Monday
8am wardrobe routine.

**The Lifeguard** (migration): she kept a rescue bot in OpenClaw whose only job was managing the others.
Export prompt: *"Hey, I want you to pull a secrets-free package of my entire agent setup, crons, agent
identities, rules, et cetera."* She calls it a **"brain transplant."** Decommissioning: *"Kill Sam."*
★ The **"secrets-free"** qualifier is the one place credential hygiene is explicitly designed in.

### ★★★ The sentence that could carry a Saturday

> *"My goal for a household agent is simple: it should get me **off** my computer and spending more time
> with my family."* (written source)

And it drives real design: the family digest is **printed on paper**, and the alternative she recommends is
**e-ink**. The output surface is deliberately non-digital. ★ **That is the same shape as his own item-cap
insight for Sat 19** -- the constraint is the feature -- and it means the two Saturdays rhyme on purpose.

### The tension for his audience, stated plainly

**The same control plane, same credentials, same pane runs her company's SOC 2 posture and who is picking
her kids up from jujitsu.** And: **enterprise access is waitlist-only**, so this entire stack -- corporate
Stripe, GitHub, Intercom and SOC 2 dashboard credentials -- is being adopted on a **$20-to-$300/month
personal plan, below the procurement line.**

### Her caveats, which are as useful as the wins

No group chat (her biggest complaint, and it contradicts xAI's own copy). Proactivity must be hand-managed
-- Grok Bot has no "heartbeat," so routines must be explicit. **The model is a bad writer**: *"I still
don't love it writing on my behalf, but for low stakes stuff, it definitely works"* -- she does not let it
write high-stakes email. No model picker, no config weeds. ★ **The two places she chose not to automate are
exactly money and production code.**

---

## §5 ⛔ DO-NOT-PRINT

1. **"TradBot is a plugin."** It is a Bot Marketplace **template**. Plugins are connectors in xAI's usage.
2. **$300, $200 or $120 as "the Grok Bot price."** Entry is $20 (Cursor Pro) or $30 (SuperGrok).
3. **Any recommendation of `@openbotx` / `openbotx/openbotx`.** Dead repo, memecoin promotion.
4. **CopilotKit/OpenBot as a thing readers should go run.** Describe its governance model on the merits;
   do not send a non-developer at it.
5. **"Marketplace templates are free."** No listing shows a price; xAI states nothing.
6. **"Grok Bot does not support CarPlay" without the Grok/Grok Bot distinction.** Grok the chat app does.
7. **Any harsh Claire Vo quote sourced to the auto-transcript** without saying it came from the video --
   her written post softens several of them materially.
8. **SuperGrok Heavy's price.** UNREACHED at primary (see below).
9. **Any claim that nobody has written a practitioner report.** It is a not-found across four venues, and
   it should be stated as that.

---

## §6 -- Unreached

- **SuperGrok Plus / Heavy dollar figures.** `grok.com/plans` renders prices as an animated CSS odometer
  with no plain-text value in the DOM; three escalations failed, and the screenshot path was blocked by the
  egress proxy. **Tool limit, not absence.**
- **The in-app Plugins marketplace catalog.** Behind auth inside the desktop app. ★ **Lars can see this in
  one click, and should -- a paid plugin would change the marketplace paragraph.**
- **The bot template pages themselves** (`x.ai/bot/uY_7s1...` etc.) need an authenticated session. ★ **If he
  wants the actual system prompts behind TradBot, LGTM, Holly and Lockdown, those five URLs are where they
  are, and he can reach them.** That is the richest available stage-2 material for the piece.
- **Self-hosted CopilotKit Intelligence licence terms and price.** Not published anywhere. ★ **The single
  load-bearing gap on the build side, and a fair question to put to CopilotKit directly before publishing.**
- The HN thread itself; OpenClaw and Hermes in depth; Grok Bot changelog specifics.
