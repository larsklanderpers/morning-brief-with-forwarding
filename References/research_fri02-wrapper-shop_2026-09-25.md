# Research Note -- The Wrapper Shop: what one or two people can build now, and what the platform eats next

For: Fri 2 Oct The Wrapper Shop · Depth: deep · Date: 2026-09-25

## Bottom line

The thesis survives, but it needs two corrections before it goes to a skeptical CTO audience. First, the "one-person million-dollar companies more than doubled since 2023" claim is real but it is Stripe's own proxy index (about 115 solopreneur platforms plus solo Atlas companies, relative counts only, no absolute numbers), and the same Stripe research shows the median solo founder's first six months of revenue fell 23% in 2025 while the top decile rose 19%: the ceiling moved, the floor did not. Second, the best 2026 evidence on "what the platform absorbs" is not that labs kill wrappers (they do, see the October 2023 PDF-chat episode and Jasper), it is that the wrappers that won stopped being wrappers: Base44 took gross margin from roughly 0% to a targeted ~60% by shipping its own model, and Cursor trained its own coding model before SpaceX bought it for $60 billion. The commercial question is therefore sharper than "what is worth wrapping": it is "what can you own before the margin or the feature gets taken", and the Census publishes its 2024 nonemployer count on 29 Sep 2026, three days before the piece runs.

## What's solid

- **Origin of the "more than doubled since 2023" claim.** It traces to Stripe Economics, "The Age of the Solopreneur," 22 Jun 2026, by Ernie Tedeschi, Marisa Rama, Chris Cruickshank. Verbatim: "More than twice as many solopreneurs earned over $1 million in 2025 than in 2023, and close to three times as many crossed $5 million and $10 million." -- Stripe Economics, primary -- https://www.stripeeconomics.com/p/the-age-of-the-solopreneur . Promoted by Patrick Collison (https://x.com/patrickc/status/2070210504388133155), picked up by WSJ ("The Rise of Million-Dollar Companies With Just One Employee"), then by the AI Daily Brief 6 Jul 2026 (https://aidailybrief.ai/e/2026-07-06). Verdict: VERIFIED as a Stripe claim; not a census count (see Contested).
- **What the Stripe index actually measures.** "Approximately 115 solopreneur-focused platforms and all solo Stripe Atlas businesses." Stripe itself says it "almost certainly understates" the population and "might [include] nonsolo businesses." -- same primary.
- **Business-level (not solo) speed to $1M.** "The share of businesses (not just solopreneurs) reaching $1 million in cumulative revenue within a year after going live on Stripe was roughly 30% higher for the 2025 cohort as it was for the 2023 cohort, and ... roughly 3x higher ... than the 2019 cohort." -- same primary. Note: the podcast presented the 3x as a solo figure; it is not.
- **Solo founders are now a majority of Atlas C corps.** "63% of C corps formed so far in the second quarter of 2026 -- an all-time high." -- Stripe blog, 28 May 2026, primary -- https://stripe.com/blog/top-solo-founder-traits
- **The winner-take-most split among solo founders.** Top-decile solo founders earned 61x the median in their first six months in 2025, up from about 34x four years earlier; "Median initial six-month revenue in 2025 was down 23% year over year, while revenue at the top decile was up 19%." -- Stripe blog, primary, same URL. Also on Stripe's X account: https://x.com/stripe/status/2060050284051620336
- **Carta's independent solo-founder series.** Solo-founded share of new startups rose from 23.7% (2019) to 36.3% (H1 2025); solo founders were 30% of 2024 startups but got 14.7% of priced-round cash. Report dated 9 Dec 2025. -- Carta Solo Founders Report 2025, primary -- https://carta.com/data/solo-founders-report/ . Carta (cap-table data) and Stripe (payments data) point the same way from different populations, which is the closest thing to corroboration here.
- **Stripe annual letter (24 Feb 2026).** "The number of companies reaching $10 million ARR within 3 months of launch was double the 2024 count"; Atlas saw "a 41% increase in company formations"; 20% of Atlas startups charged a first customer within 30 days, up from 8% in 2020. -- Stripe 2025 annual letter PDF, primary -- https://assets.stripeassets.com/fzn2n1nzq965/3LlGw839Q6kUwxZlLZDtH6/165febe69e83add86fcf2f24a54b83f9/Stripe-annual-letter-2025-desktop.pdf
- **Base44 deal terms.** Wix announced 18 Jun 2025: about $80M initial consideration plus earn-outs through 2029 tied to performance metrics; about $25M in retention bonuses to Base44 employees in 2025. -- Wix press release via GlobeNewswire, primary -- https://www.globenewswire.com/news-release/2025/06/18/3101508/0/en/Wix-Further-Expands-into-Vibe-Coding-with-Acquisition-of-Base44-a-Hyper-Growth-Startup-that-Simplifies-Web-and-App-Creation-with-AI.html
- **Base44 after the deal.** Shlomo payouts have passed $150M including a $41M payment (Calcalist, 4 Aug 2026, https://www.calcalistech.com/ctechnews/article/apa3i9eyt); ARR $100M (Mar 2026), $150M (May 2026), $200M (announced 20 Aug 2026, Shlomo: "We just blew past $200M ARR at Base44. 5 months after hitting $100M. We've released Base 1 in between.") -- Calcalist, https://www.calcalistech.com/ctechnews/article/syw900pvdzg . The $200M is founder self-reported; the $100M+ was also stated by Wix management on earnings calls.
- **Base44 gross margin went from ~0% to a ~60% target by owning the model.** Wix Q2 2026 call (early Aug 2026): Base44 gross margin "from roughly 0% when we started the year to approximately 60% in the second half of the year," driven by its own model, Base1. -- Wix earnings call transcript (Motley Fool), primary transcript -- https://www.fool.com/earnings/call-transcripts/2026/08/11/wix-wix-q2-2026-earnings-call-transcript/ ; corroborated by Calcalist (above). Note: 60% is a management target for H2 2026, not a reported result.
- **Cursor, the "wrapper" that became a $60B acquisition.** ARR past $500M (Jun 2025, TechCrunch), past $1B (Nov 2025), $3B (Bloomberg, 21 May 2026); SpaceX exercised a right to buy for $60B in stock, closed 14 Aug 2026 (SEC 8-K per Wikipedia; Bloomberg https://www.bloomberg.com/news/articles/2026-08-14/spacex-completes-its-60-billion-cursor-acquisition ; TNW https://thenextweb.com/news/spacex-cursor-acquisition-completed-gpu-fleet). Solid on the deal; ARR figures are company-sourced via press.
- **Cursor's own model.** Composer 2 (Mar 2026) was built on Moonshot's open-weights Kimi; Cursor's Lee Robinson: "Only ~1/4 of the compute spent on the final model came from the base, the rest is from our training." -- TechCrunch 22 Mar 2026 (via Wikipedia citation). Treat as one strong secondary plus company quote.
- **Platform absorbs a category, case 1 (Oct 2023).** ChatGPT added PDF upload and analysis for paying users on ~31 Oct 2023. Stripe's Sahar Mor at the time: "OpenAI just executed a move that will wipe out dozens of AI companies." Named exposed products: PDF.ai, Sider's ChatPDF feature, ChatOCR (its creator's poll: 72.4% of 210 users expected "less usage"). -- Business Insider via Yahoo, 31 Oct and 3 Nov 2023 -- https://tech.yahoo.com/science/articles/minor-chatgpt-warning-founders-big-123540379.html and https://tech.yahoo.com/ai/articles/bracing-impact-founders-built-chatgpt-140248452.html
- **Platform absorbs a category, case 2 (Jasper).** Sep 2023: internal valuation cut about 20% from $1.5B to ~$1.2B, 2023 ARR projection cut by at least 30%, CEO replaced; "OpenAI's launch of ChatGPT ... created a formidable low-cost competitor practically overnight." -- The Information (paywalled, reached via Maginative summary) -- https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/ and https://www.theinformation.com/articles/jasper-an-early-generative-ai-winner-cuts-internal-valuation-as-growth-slows
- **Platform absorbs incumbents too, case 3 (Feb 2026).** Anthropic released a legal plugin for Claude Cowork (contract review, NDA triage, compliance). On 3 Feb 2026 RELX fell 14.6%, Wolters Kluwer more than 11%, Thomson Reuters more than 11% at the open (later more than 15% per ABC), Pearson 6.2%. -- Investing.com (https://www.investing.com/news/stock-market-news/wolters-kluwer-relx-shares-slip-after-anthropic-unveils-aienhanced-legal-tool-4481124) and ABC News (https://abcnews.com/Business/new-ai-tool-hammered-software-stocks-week/story?id=129845251). CNN fetch blocked (robots), recorded as unreached.
- **The platform also absorbs its own products.** OpenAI Agent Builder (launched at DevDay Oct 2025, widely billed as "killing Zapier and n8n") was deprecated: "On June 3, 2026, we notified developers using Agent Builder that the product is being deprecated. ChatKit remains available." Shutdown 30 Nov 2026. -- OpenAI deprecations page, primary -- https://developers.openai.com/api/docs/deprecations . Meanwhile n8n raised at $2.5B days after DevDay (Bloomberg, 9 Oct 2025, https://www.bloomberg.com/news/articles/2025-10-09/ai-agent-startup-n8n-nets-2-5-billion-valuation-with-backing-from-nvidia).
- **Supplier risk, not just feature risk.** Windsurf CEO Varun Mohan, Jun 2025: "With less than five days of notice, Anthropic decided to cut off nearly all of our first-party capacity to all Claude 3.x models." -- primary, X -- https://x.com/_mohansolo/status/1930034960385356174 ; TechCrunch coverage https://techcrunch.com/2025/06/03/windsurf-says-anthropic-is-limiting-its-direct-access-to-claude-ai-models
- **Same category, opposite outcomes.** Gamma (AI presentations): over $100M ARR, "profitable for more than two years," about 50 employees, $2.1B valuation, 10 Nov 2025 -- company press release, self-reported -- https://www.businesswire.com/news/home/20251110805751/en/Gamma-Surpasses-$100M-ARR-Raises-at-$2.1B-Valuation-as-It-Replaces-PowerPoint-for-the-AI-Era . Tome (AI presentations, 20M+ users) abandoned presentations for an AI CRM (Lightfield) -- VentureBeat 20 Nov 2025 (https://venturebeat.com/technology/tomes-founders-ditch-viral-presentation-app-with-20m-users-to-build-ai) and Forbes 20 Jul 2026 (revenue "plateaued at $3 million annually").
- **Altman's "one-person billion-dollar company."** "In my little group chat with my tech CEO friends there's this betting pool for the first year that there is a one-person billion-dollar company. Which would have been unimaginable without AI and now will happen." Said in conversation with Alexis Ohanian, reported as September 2023 (widely circulated Feb 2024). -- Fortune 4 Feb 2024 (https://fortune.com/2024/02/04/sam-altman-one-person-unicorn-silicon-valley-founder-myth/) and TechCrunch 1 Feb 2025. Two secondaries agree; original video not reached.

## What's contested / watch out

- **"More than doubled" is Stripe's lens, and the public census does not (yet) show it.** Census Nonemployer Statistics (reported by Elaine Pofeldt, Forbes) put $1M+ nonemployer businesses at 57,822 in 2021 (a March 2025 Forbes piece says 57,222; one is a typo), 116,803 in 2022, and 117,060 in 2023. So the big census jump was 2021 to 2022 (pre-ChatGPT tax year) and 2022 to 2023 was flat (+257). Forbes attributes the 2022 jump partly to generative AI, which is implausible for 2022 receipts. -- https://www.forbes.com/sites/elainepofeldt/2025/08/10/number-of-million-dollar-one-person-businesses-keeps-growing/ and https://www.forbes.com/sites/elainepofeldt/2025/03/23/number-of-million-dollar-one-person-businesses-doubles-in-one-year/ . Census numbers here are via one secondary; I did not reach the underlying data.census.gov table.
- **Census 2024 release lands 29 Sep 2026.** Census tip sheet, 18 Sep 2026: 2024 Nonemployer Statistics "Scheduled for release Sept. 29." -- https://www.census.gov/newsroom/tip-sheets/2026/tp26-19.html . Pull the $1M+ size-class count before Friday; it either corroborates Stripe or undercuts it.
- **Nonemployer does not mean one person.** Census nonemployer firms have no payroll but can be partnerships and can use contractors; Stripe's proxy may include non-solo businesses by its own admission. "One-person" is shorthand in both datasets.
- **The podcast garbled details.** AI Daily Brief said the 3x cohort figure was about solopreneurs (it is all businesses) and said "Delaware LLC incorporations up 40%" (Stripe says "Delaware incorporations have grown approximately 40% year over year since early 2025," no LLC split). Do not quote the podcast; quote Stripe.
- **Base44 team size.** Calcalist reported six employees at sale; others say eight; Forbes (Sandy Carter, Apr 2026) calls it one person. Wix did not disclose. Say "fewer than ten" and attribute to Calcalist. The $189K single-month profit is Shlomo's own public post (self-reported).
- **Base44 was a "solo" company with retention bonuses of ~$25M.** The one-person framing and the employee-bonus line in Wix's release sit awkwardly together. Use "solo founder, small team."
- **Cursor margins.** Newcomer (10 Aug 2025) reported Cursor "has negative gross margins" on individual plans, paying heavily to Anthropic, ~150 employees -- https://www.newcomer.co/p/cursors-popularity-has-come-at-a . One secondary with anonymous sourcing; not independently confirmed. Do not state as fact.
- **Tome numbers disagree.** VentureBeat: 20M users, $43M raised. Forbes: 25M users, $80M raised, $3M revenue plateau. Pick one and attribute.
- **Claude Cowork plugin date.** ABC says the plugins were unveiled on a Friday; Investing.com dates the legal-plugin selloff to 3 Feb 2026 (a Tuesday). Say "early February 2026."
- **"Wrapper killed" narratives are mostly punditry.** Blog posts titled "OpenAI just killed Zapier/n8n" were wrong on the evidence: n8n raised at $2.5B, and OpenAI later deprecated Agent Builder itself.

## Couldn't verify

- **Absolute count of $1M+ solopreneurs in Stripe's index.** Stripe publishes only relative change. Unverifiable as a number.
- **Pieter Levels revenue.** Widely repeated "~$3M/year, zero employees" traces to his own X posts and public dashboards; photoai.com/open returned 404 (unreached). Self-reported only.
- **Midjourney.** The Information: revenue "significantly surpassed" $200M in 2023, profitable per David Holz. Current headcount (often cited as ~40 to 100+) and later figures ($300M to $500M) are aggregator estimates. Treat 2023 figure as one strong secondary.
- **Altman primary video.** Not located; two secondaries agree on wording.
- **OpenClaw / Peter Steinberger "acquired by OpenAI."** Forbes (Apr 2026) says acquired; I did not confirm whether it was an acquisition or a hire. Do not print as an acquisition.
- **Census 2021 to 2023 $1M+ counts at source.** Only via Forbes.
- **Claude Cowork CNN piece.** Blocked (robots), unreached.
- **Survival rate of solo AI businesses beyond year 2.** No primary dataset found. Stripe's cohort work covers the first two years only.

## The economics

- **Model API list prices today (per million tokens, input / output).** Anthropic: Claude Opus 5.5 $4 / $20, Sonnet 5 $2 / $10, Haiku 4.5 $1 / $5; batch halves these; cache hits on Opus 5.5 are $0.20 -- https://platform.claude.com/docs/en/about-claude/pricing . OpenAI: GPT-5.6 Sol $5 / $30, Terra $2 / $12, Luna $0.20 / $1.20; batch 50% off -- https://openai.com/api/pricing/ . Primary, checked 25 Sep 2026.
- **Price per capability falls fast; bills do not.** a16z (Guido Appenzeller, 12 Nov 2024): "For an LLM of equivalent performance, the cost is decreasing by 10x every year" (GPT-3-level MMLU 42 from $60 to $0.06 per million tokens in three years) -- https://a16z.com/llmflation-llm-inference-cost/ . Caveat: agentic products consume far more tokens per task, which is why the margins below are thin.
- **Fixed tooling for a one-to-two-person shop is small.** Claude Pro $20/mo, Max from $100/mo (https://claude.com/pricing); Cursor Pro $20/mo (https://cursor.com/pricing); Stripe 2.9% + 30 cents per domestic card charge plus 0.7% for Billing (https://stripe.com/pricing). The real cost line is variable inference, not seats.
- **Gross margins of AI apps (named investor sources).** Bessemer "State of AI 2025" (13 Aug 2025): hypergrowth "Supernovas" run "~25% (often negative)" gross margin, ARR per FTE $1.13M; steadier "Shooting Stars" ~60%, ~$164K ARR per FTE; Bessemer notes some are "so close to the functionality of core foundation models that 'thin wrapper' labels could be thrown" -- https://www.bvp.com/atlas/the-state-of-ai-2025 . ICONIQ "2026 State of AI" (Jul 2026, ~300 execs): AI product gross margins 45% in 2025, projected 53% in 2026 and 59% in 2027 -- https://www.iconiq.com/growth/reports/state-of-ai-2026 . Classic SaaS runs 70-80%.
- **Margin repair route = own the model.** Base44 ~0% to ~60% target via Base1 (Wix, Aug 2026). Cursor Composer on Kimi base. This is the economic tell for "what the platform will not let you keep": the inference margin.
- **Revenue per employee is the new vanity metric.** Lovable: $400M ARR with 146 employees (Feb 2026), company-confirmed to TechCrunch -- https://techcrunch.com/2026/03/11/lovable-says-it-added-100m-in-revenue-last-month-alone-with-just-146-employees/ . Gamma ~$100M ARR with ~50 people, self-reported.

## Drop-in facts

- "More than twice as many solopreneurs earned over $1 million in 2025 than in 2023." -- Stripe Economics, 22 Jun 2026 (Stripe's proxy index, not a census).
- Solo founders formed 63% of Stripe Atlas C corps in Q2 2026, an all-time high. -- Stripe, 28 May 2026.
- Median solo-founder revenue in the first six months fell 23% in 2025; the top decile rose 19%; the top decile now earns 61x the median, up from 34x. -- Stripe, 28 May 2026.
- Solo-founded share of new US startups: 23.7% in 2019, 36.3% in H1 2025; solos got 14.7% of priced-round cash. -- Carta, Dec 2025.
- Census counted 116,803 nonemployer businesses with $1M+ receipts in 2022 and 117,060 in 2023. -- Census via Forbes/Pofeldt, Aug 2025. 2024 data out 29 Sep 2026.
- Wix bought Base44 for ~$80M plus earn-outs through 2029 on 18 Jun 2025; founder payouts have since passed $150M. -- Wix release; Calcalist, Aug 2026.
- Base44 gross margin: "roughly 0%" at the start of 2026, targeted "approximately 60%" in H2 after shipping its own model. -- Wix Q2 2026 call.
- SpaceX closed its $60B purchase of Cursor on 14 Aug 2026. -- Bloomberg; TNW.
- Fastest-growing AI apps run ~25% gross margins, "often negative." -- Bessemer, Aug 2025.
- AI product gross margins averaged 45% in 2025 across ~300 software companies. -- ICONIQ, Jul 2026.
- AI subscription apps: annual retention 21.1% vs 30.7% for non-AI; refund rate 4.2% vs 3.5%; but trial-to-paid 8.5% vs 5.6%. -- RevenueCat State of Subscription Apps 2026 via TechCrunch, 10 Mar 2026 (https://techcrunch.com/2026/03/10/ai-powered-apps-struggle-with-long-term-retention-new-report-shows ; report https://www.revenuecat.com/state-of-subscription-apps).
- OpenAI deprecated its own Agent Builder on 3 Jun 2026, eight months after launch; shutdown 30 Nov 2026. -- OpenAI deprecations page.
- When ChatGPT added PDF upload (Oct 2023), a Stripe product lead wrote it "will wipe out dozens of AI companies." -- Business Insider, 31 Oct 2023.
- RELX fell 14.6% the day Anthropic's Claude legal plugin hit the market (3 Feb 2026). -- Investing.com.
- Stripe Atlas: 20% of startups charged a first customer within 30 days of incorporation, up from 8% in 2020. -- Stripe annual letter, Feb 2026.

## DO-NOT-PRINT

- "One-person million-dollar companies more than doubled" without saying "on Stripe's own proxy index." It is not a count of US businesses.
- The "3x vs 2019" figure as a solopreneur stat (it is all businesses on Stripe).
- "Base44 was a one-person company" (it had a small team; Wix booked ~$25M in retention bonuses for employees).
- "Cursor has negative gross margins" as fact (single anonymous-sourced secondary, 2025).
- "OpenAI acquired OpenClaw" (unconfirmed acquisition vs hire).
- Any Pieter Levels, Marc Lou, or Daymaker revenue figure without "self-reported."
- Midjourney 2025/2026 revenue or headcount from aggregators (Latka, "statistics" sites).
- "OpenAI killed Zapier/n8n" (contradicted by n8n's $2.5B round and Agent Builder's deprecation).
- The AI Daily Brief's "Delaware LLC" line.
- Forbes's suggestion that ChatGPT drove the 2022 census jump.

## Angles this opens

1. **The ceiling moved, the floor did not.** Stripe's own data is the strongest skeptic's weapon: top decile up 19%, median down 23%. The million-dollar solo shop is a power law, and the survivorship bias is baked into every example anyone names.
2. **Wrappers that win stop being wrappers.** Base44 (Base1) and Cursor (Composer) both bought back their margin by owning a model. The wrapper is a customer-acquisition phase, not a business model. What is worth wrapping is whatever gives you the usage data and distribution to later own the expensive layer.
3. **The platform eats three things, not one.** Features (PDF chat, Oct 2023), supply (Windsurf cutoff, Jun 2025), and margin (inference bills, 25% Supernova margins). And it also eats its own products (Agent Builder). A wrapper's risk register needs all four.
4. **Same category, opposite fates.** Gamma vs Tome in AI presentations: the difference was not the model, it was distribution, pricing, and profitability discipline. Useful counter to "the category is dead."
5. **The incumbents are the wrapper now.** The Feb 2026 legal-plugin selloff hit Thomson Reuters and RELX, not startups: at platform volume, a 100-year information business can be the thing that gets absorbed.
6. **Timely hook:** Census 2024 nonemployer data drops 29 Sep 2026. If the $1M+ count jumps, it is the first independent corroboration of Stripe; if it is flat, that is the story.

Interview questions for Lars:

- [YOUR TAKE] When you spin up a wrapper business for a new opportunity, what is your written rule for when to kill it, and has a platform release ever triggered that rule for you? Give the date and the feature.
- [YOUR TAKE] What share of your wrapper's revenue goes to model inference today, and at what margin would you decide to fine-tune or host your own model, the way Base44 did with Base1?
- [YOUR TAKE] Which of your wrappers survived a platform release, and was it distribution, proprietary data, workflow lock-in, or a niche the lab will not bother with?
- [YOUR TAKE] Have you ever been on the Windsurf side of this: a supplier cutting capacity, repricing, or rate-limiting you? What is in your contracts or architecture now because of it?

---

## ADDENDUM -- 1 Oct 2026 (Fri 2 day chat: Census re-sweep, roll-up section, Winsock)

**Census 2024 Nonemployer Statistics -- RELEASED 29 Sep 2026 (PRIMARY).** Press release: https://www.census.gov/newsroom/press-releases/2026/2024-nonemployer-statistics.html . Counts from data.census.gov table NS00NONEMP (`data.census.gov/api/access/data/table?id=NONEMP{year}.NS00NONEMP`, US, all sectors, all legal forms; size classes sum to the published totals). Unit = ESTABLISHMENT, not firm. Nonemployer = "no paid employees, subject to federal income tax, receipts of $1,000 or more."

| Year | $1M-2.49M | $2.5M-4.99M | $5M+ | Total >=$1M | All nonemployer |
|---|---|---|---|---|---|
| 2024 | 112,661 | 12,644 | 1,051 | 126,356 | 31,985,874 |
| 2023 | 104,643 | 11,512 | 905 | 117,060 | 30,427,808 |
| 2022 | 104,524 | 11,314 | 965 | 116,803 | 29,811,495 |

- **Read:** >=$1M up ~7.9% 2023->2024 after ~+0.2% 2022->2023; all nonemployers up ~5.1%; $5M+ up ~16%. Census backs Stripe's DIRECTION and not its SIZE: a measured rise of about 8% in the first full post-ChatGPT tax year, not a doubling. Forbes's 2022/2023 figures match exactly.
- Receipts units unconfirmed (likely $1,000s): do not print a receipts total.

**Roll-ups (one section, his ruling 28 Sep).**
- Isenberg "$5T opportunity: AI Roll Ups" (X, 26 Sep): UNREACHED at source (x.com robots; firecrawl failing on a schema error). Secondary reproduction only (startup.whatfinger.com, 28 Sep). "3x EBITDA" NOT in the reproduction.
- McKinsey Institute for Economic Mobility, "The Great Ownership Transfer", 26 Feb 2026 (PRIMARY): "By 2035, six million small businesses will be on the market as their owners retire. More than one million of them are viable candidates for transfer, representing $5 trillion in enterprise value that could remain productive." Also: in 2022, 510,000 SMBs exited; 92% closed, 5% sold, 3% transferred.
- Thrive Holdings: OpenAI primary 1 Dec 2025 (https://openai.com/index/thrive-holdings/): "invests in, acquires, and builds businesses that benefit from long-term, technology-driven transformation"; initial focus accounting and IT services.
- Larson Gross: Forbes (Anna Tong, 2 Jun 2026): stake acquired in 2025 by Current (renamed Crete Professionals Alliance), owned by Thrive Holdings; founded 1949, five offices, 200 employees; Tax AI "processed 7,000 tax returns directly through the AI", "31% time savings"; Thrive "committing $1 billion" to buying accounting practices. Current's site (PRIMARY) lists Larson Gross: 200+ employees, 18 partners, five WA offices.
- Current firm count conflicts: "almost 30" (CFOtech, Jun 2026) / 48 (PYMNTS, Jul 2026) / "nearly 50" (Forbes). Do not print a single count.

**Trumpet Winsock (held for Fri 2 by the Thu 1 chat).**
- Federal Court of Australia, Trumpet Software v OzEmail [1996] FCA 560 (PRIMARY): Peter Tattam, MD of Trumpet; ten years at the University of Tasmania psychology department before Sep 1994; shareware with a registration fee after an evaluation period "typically 30 days". Heard in Hobart.
- Microsoft TechNet "Windows 95 Networking: The Basics" (PRIMARY): built-in support for "TCP/IP and IPX/SPX"; remote access over PPP.
- WfW 3.11 free TCP/IP: PC Week, 21 Feb 1994 (contemporaneous secondary).
- "Received very little" = Wikipedia wording over Tedium/Vice (2016) and a Hacker News comment (2011). ANECDOTAL: attribute as "by most accounts", never as fact.

**DO-NOT-PRINT (adds to the list above):** "3x EBITDA" as Isenberg's; any Isenberg quote as read at source; "$5 trillion of businesses changing hands" (it is enterprise value of ~1M viable candidates); "a million businesses set to sell"; "tax agents built on Codex" (say Tax AI built with OpenAI); "Thrive bought Larson Gross" (a stake, via Current); a single Current firm count; "nonemployer firms" (establishments); ">=$1M nonemployers = solo founders"; a receipts total; any Trumpet user or registration count; Tattam's earnings as fact.

## ADDENDUM 2 -- 2 Oct 2026 (panel night, firecrawl working again)
- Isenberg X post READ AT SOURCE (firecrawl, 1 Oct): "I'll make the case why you should buy a business and use AI agents to 3x EBITDA." -> the "3x EBITDA" kill is LIFTED. He credits the $5T to McKinsey ("~$5 trillion worth of American businesses will change hands by 2035, according to McKinsey"). He says Thrive "bought a stake" in Larson Gross; he claims Larson Gross's "tax agents run on OpenAI's Codex" (still do not print as fact). He caveats that roll-up results are self-reported and untested by a downturn. Self-description: Startup Ideas podcast; Late Checkout (holding company; "design firm LCA" in the post).
- 7,000 returns: OpenAI's own 27 May post puts them across the Crete/Current pilot firms, not Larson Gross alone. Print as the pilot's figure.
- Larson Gross founded 1949 ("75-year history" on Current's page is approximate): print "since 1949".
