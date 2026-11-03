**Status: rv3 -- Fri 2 Oct 2026. rv2 = his edit pass (Word "v2", 2 Oct 06:24), saved verbatim as `-rv2.md`. rv3 = rv2 + mechanics only. Not panelled.**

**Mechanics applied (his text otherwise untouched; every contraction he wrote kept):** "Open AI" -> OpenAI; "SAAS" -> SaaS + missing closing quote; "I am tech entrepreneur" -> "I am a tech entrepreneur"; "can really done about" -> "can really be done about it"; "its all" -> "it's all"; "Craftmanship" -> "Craftsmanship"; "craftsman do" -> "craftsmen do"; "$5 trillion dollars" -> "$5 trillion"; missing ")" in the final How-I-Would-Decide paragraph; Word's en dashes back to `--`.

**Open for his ruling:** see the chat report (Mollick quote not yet footed; craftsmanship piece needs its author; Isenberg's $5T now attributed to him; Sun 4 craftsmanship overlap; footer argument line).

---

# Shareware Season

More people are earning a million dollars a year on their own than at any point we have data for. The typical one of them is earning less than last year.

Both of those are true at the same time, and the gap between them is most of the commercial story of the one- and two-person AI business right now. Before getting to the numbers, though, a story from Tasmania.

In the early 1990s, if you had a Windows 3.1 machine and a modem and you wanted to get onto the internet, Windows could not do it on its own. It had no built-in way to speak TCP/IP (the language every machine on the internet uses to talk to every other machine). Something had to sit underneath your browser and your email client and translate. For a great many people, that something was Trumpet Winsock, a shareware program written by Peter Tattam and sold out of Hobart by his company, Trumpet Software. (For my American friends: Hobart is the capital of Tasmania, the island state off the bottom of Australia, and a very long way from Redmond.) Shareware meant you could download it, use it for an evaluation period, typically thirty days, and then you were supposed to pay a registration fee. A lot of people did not.

Then the platform filled the hole. Microsoft released a free TCP/IP add-on for Windows for Workgroups 3.11 in early 1994, and Windows 95, in August 1995, shipped with TCP/IP as one of its built-in networking components. The thing Trumpet sold was now a checkbox in the operating system. By most accounts Tattam saw very little money from a program that had been installed on an enormous number of machines.

I do not tell that story because Microsoft was cruel or Tattam was naive. I tell it because the thing he built was a missing piece of the platform, and platforms, if they survive long enough, fill their missing pieces, like water flowing into cracks. That was true in 1995 and it is the operating condition of every AI wrapper business being spun up this year. The commercial question for a very small shop is not whether to build on someone else’s model (you will; almost everyone does, you kinda need to). It is what you are building that the next release cannot ship, and how you protect that build for longer -- even a year longer than you would otherwise.

## More at the top, less in the middle

Start with the headline number, because it has been everywhere.

In June, Stripe’s economics team published a piece called “The Age of the Solopreneur,” which said: “More than twice as many solopreneurs earned over $1 million in 2025 than in 2023, and close to three times as many crossed $5 million and $10 million.” It is a real finding, from people who see an enormous amount of real payment data. It is also a *proxy* index, about 115 platforms aimed at solo businesses plus every solo company formed through Stripe Atlas (Stripe’s company-formation service), and Stripe publishes relative change only, not a count. Stripe says itself that the index “almost certainly understates” the population and may include some businesses that are not strictly solo. So when you see “one-person million-dollar companies have doubled,” what you are actually seeing is Stripe’s lens on Stripe’s customers. Which is fine, as long as everyone remembers that is what it is. I don’t think everyone does, because I have seen this number cited without many caveats over and over in the last few months.

The US government’s own count arrived on Tuesday. The Census Bureau published its 2024 Nonemployer Statistics on 29 September, and nonemployer establishments (businesses with no paid employees, which is the closest thing the government has to a count of one-person shops) with $1 million or more in receipts went from 117,060 in 2023 to 126,356 in 2024. That is up about 8%, after a year in which the same number barely moved (116,803 in 2022). So the official data backs Stripe on the *direction* and not on the *size*. A real rise, in the first year that series has moved since 2022, but nothing like a doubling. (Worth knowing: “nonemployer” is not quite the same as “one person.” It includes partnerships and businesses that lean on contractors. It is shorthand in both datasets. Any claim about solopreneur millionaires, solopreneur billionaires [which have started to enter the chat] or any other story about solopreneurs that says anything beyond “its really hard work no matter how many agents you use”, should be taken with a grain of salt.)

Now the part that gets left out of the headline. In May, a separate Stripe post on solo founders reported that “median initial six-month revenue in 2025 was down 23% year over year, while revenue at the top decile was up 19%.” The top tenth of new solo founders now earn about 61 times what the median one does in their first six months, up from about 34 times four years earlier. Carta, which sees startups through their cap tables rather than their payments, found the same shape from a different angle: solo-founded companies went from 23.7% of new startups in 2019 to 36.3% in the first half of 2025, and in 2024 they were 30% of new startups but got 14.7% of the money raised in priced rounds.

So the ceiling moved, and the floor did not. More solo businesses are reaching seven figures, faster, and the middle of the distribution is doing worse. That is what a power law looks like, and it means nearly every one-person success story you have read this year (and there have been a lot of them) was chosen from the top of it. The survivorship bias is not a flaw in the reporting. It is built into what makes a story worth reporting.

From a personal perspective, I think there are a couple of assumptions that are being assaulted here, but probably the biggest piece of historical wisdom is that entrepreneurs always have to have guys to work together with to fill what they don’t know -- I am a tech entrepreneur, and always had to have a sales guy, because I am not the best at selling. My partner is a good marketing guy, but we need a decent finance guy to make sure we cover all the operational items. So for us, three founders makes sense. For a lot of these solo companies, they are using agents to fill in the missing skills. And there is an even more subtle element here: if you are one of those super-smart people who has come up with something truly novel, and you genuinely believe the sky is the limit, being a solo founder and filling your weaknesses out with a bot farm means that when VC money comes calling, you end up being the sole recipient of the largess. That’s a very attractive way to start a company if you are in that universe.

## What the platform takes back

When people talk about a lab “killing” a wrapper, they usually mean one thing: the lab ships your feature. That happens, and it happens fast. When ChatGPT added PDF upload and analysis for paying users at the end of October 2023, Stripe’s Sahar Mor wrote that OpenAI had “just executed a move that will wipe out dozens of AI companies,” and the chat-with-your-PDF products were the obvious casualties. Jasper, one of the early generative AI writing successes, cut its internal valuation by about 20% in 2023 as ChatGPT turned into what The Information called “a formidable low-cost competitor practically overnight.”

And it is not only startups. In early February this year Anthropic released a legal plugin for Claude Cowork (contract review, NDA triage, compliance checks) and RELX, which owns LexisNexis, fell 14.6% that day, with Thomson Reuters and Wolters Kluwer down more than 11% at the open. A hundred-year-old information business can be the wrapper too, if what it sells is a layer the platform decides to provide.

But the feature is only one of the things a platform can take. There are at least three more, and a small shop needs to price all of them.

**It can take your supply.** In June 2025, Windsurf’s CEO posted that “with less than five days of notice, Anthropic decided to cut off nearly all of our first-party capacity to all Claude 3.x models.” Windsurf was, at the time, reportedly in acquisition talks with OpenAI, which tells you something about why. The point for a small shop is not who was right. It is that your product can be fine on Monday and rate-limited on Friday because of a negotiation you are not party to.

**It can take your margin.** The fastest-growing AI apps run on thin gross margins; Bessemer, a venture firm that invests in exactly these companies, put its hypergrowth cohort at “~25% (often negative)” in its 2025 report, and ICONIQ’s survey of about 300 software companies put AI product margins at 45% last year. Traditional software has run a long way above that. Every token you resell, you bought first, and the supplier sets the price.

**It can take its own product away.** OpenAI’s Agent Builder launched in October 2025 and was widely written up as the thing that would kill Zapier and n8n. On 3 June this year OpenAI told developers it was being deprecated, with shutdown at the end of November. n8n, meanwhile, raised at a $2.5 billion valuation days after the launch that was supposed to end it. If you built on Agent Builder, the platform did not absorb your feature; it absorbed your foundation.

I have never been in any of these particular shoes -- but I have spent 25 years playing a massive game of chicken as the David with the biggest operators in gaming. And the only time we ever came close to the bigger player being able to take us out of the market is when one of them decided to try and take away our supply. It’s an absolute killer, and if it wasn’t for loyal customers, we would have been cut by a third in a month from start to finish. I am not sure how much can really be done about it -- the problem is that it's all asymmetrical. If you are SpaceXAI (one of the most well-capitalized businesses in the world, despite its debt) or Anthropic or OpenAI (with their incredible private war chests), then the loss of a small competitor is peanuts; even loss of a group of customers is peanuts unless you happen to be massive consumers of tokens; the economic impact to them is minor compared to the business-ending event for the small operator. I know exactly how much angst this causes and so your only option is to penetrate as deeply as you can (like a tick) and hope it helps you keep on.

## Wrappers that stopped being wrappers

Here is the more useful evidence, and it cuts against the “wrappers are doomed” story as much as it supports it (just like the real things we see with “SaaS is dead” versus “SaaS is still an important control surface”).

Base44 is the cleanest case I know of. It was a vibe-coding tool (you describe the app you want, it builds it) started by a solo founder, Maor Shlomo, with a small team; Calcalist reported fewer than ten people at the sale. Wix bought it in June 2025 for about $80 million up front plus earn-outs running through 2029. It was, at the start, a wrapper in the purest sense: a very good interface on top of other people’s models. And on Wix’s own earnings call in August, management said Base44’s gross margin had gone “from roughly 0% when we started the year to approximately 60% in the second half of the year.” Note that the 60% is a target, not a reported result. What changed was that Base44 shipped its own model, Base1. Zero margin is what reselling someone else’s tokens looks like at scale. Sixty is what owning the expensive layer looks like.

Cursor followed the same path at a much larger scale. It started as an editor wrapped around frontier models, built its own coding model (Composer 2, on top of Moonshot’s open-weights Kimi; Cursor’s Lee Robinson said “only ~1/4 of the compute spent on the final model came from the base, the rest is from our training”), and SpaceX closed its $60 billion purchase of it in August.

And in the same category, you can get opposite outcomes. Gamma and Tome both built AI presentation tools. Gamma says it passed $100 million in annual recurring revenue with about 50 people and has been profitable for more than two years. Tome, with something north of twenty million users, plateaued at around $3 million in annual revenue according to Forbes and its founders walked away from presentations entirely to build a CRM. Same models, same moment, same idea. The difference was distribution, pricing and discipline, not the model underneath.

So I think “what is worth wrapping” is the wrong question, or at least an incomplete one. The wrapper is a way in. It gets you customers, usage data and a reason for people to come back, while the margin is borrowed. What the wrapper is *for* is buying the time to own something the next release cannot ship: the data your users generate, the distribution you built, the workflow your customers have rebuilt their week around, eventually maybe the model itself, or a niche small enough that no lab will ever bother to come for it.

Ethan Mollick actually commented about this same thing in the last few days, and I think his insight is pretty bang on -- “Every one of the apps from the AI Labs have weird edges and are under-documented and break sometimes and update without any sort of notice or changelog and change UIs on a dime... but even a broken early version of whatever product they are shipping is still better then a well-built traditional product a lot of the time because LLMs are just unreasonably effective tools at doing a vast array of stuff. And, from what I have seen, people and companies are learning to just roll with it as a result.”

I will cross that against a piece that has been circling around the traps in the industry for some months, called “Software Craftsmanship Is Dead.” And I think this is very evidentiary of the problem -- craftsmen do beautiful work that takes a long time, costs a lot more, and lasts for a hundred years. Manufacturing of an item is directed in the opposite way -- volume, acceptable quality, and it lasts how long it lasts. No matter how much we might mourn that loss of a whole category of woodworker from the economics of our economy, *it doesn’t change the fact that people will go where the economics drive them*. And that is not something that any of us are in a position to change.

I think the lesson here is one for all of us, especially those of us who are traditional engineers -- and it might come down to, “if you can’t beat ‘em, join ‘em”. I feel as if part of what we need to look at as software providers is to deliver faster, iterate faster, and know that functions and access trump perfectly deployed code all the time now, and if you are trying to adjust ahead of the platform, its nearly your only choice at a certain size and complexity. The models will keep getting better, the platforms will keep getting broader. The only truly viable business model is to stay ahead, or have a moat that is uneconomical to try and cross. That leads to the other option.

## Or buy the shop instead

There is a second route that has been getting a lot of attention this week, and it runs in the opposite direction.

Greg Isenberg (a startup investor and podcaster with a very large following on X) published a long post on 26 September pitching what he calls AI roll-ups: instead of building a new product on top of a model, buy an existing small service business, the accounting practice or the property manager whose founder wants to retire, and run it with agents. He estimates the market opportunity as $5 trillion (he is an investor but also a talking head, so that’s probably an outside number, but do your diligence regardless).

That said, the underlying figure he leans on is real, and it comes from McKinsey. In February, McKinsey’s Institute for Economic Mobility reported that “by 2035, six million small businesses will be on the market as their owners retire. More than one million of them are viable candidates for transfer, representing $5 trillion in enterprise value.” The same report has the number I find more striking: in 2022 alone, 510,000 small businesses exited the market, and 92% of them closed. Five percent sold. Three percent were transferred.

The money is already moving. Thrive Holdings, a company set up by Thrive Capital to buy and build services businesses, with an ownership stake from OpenAI as of last December, is reported by Forbes to be committing $1 billion to buying accounting practices. One of them is Larson Gross, a 200-person firm founded in Bellingham, Washington, in 1949, in which Thrive’s accounting platform, Current, took a stake last year. Forbes reports its OpenAI-built tax system processed 7,000 returns directly this tax season, with 31% time savings for the accountants. (The interests here are worth naming: Thrive Capital is a major OpenAI investor, and OpenAI owns part of the company doing the buying. That does not make the numbers wrong. It does mean the people telling the success story are the people selling the model.)

What makes this interesting for a small shop is that it flips the risk in everything above. If you sell a wrapper, the platform’s next release is a competitor. If you own a practice with clients, licenses and a reputation built over seventy-five years, the platform’s next release is a *cost reduction*. You rent the model; you own the relationship. When the lab ships the feature, your margin goes up instead of your business going away.

That is not free, of course. Buying a business takes capital that writing a wrapper does not, and the 92% closure rate cuts both ways: plenty of those businesses closed because there was not much there to buy. And running an accounting firm is running an accounting firm, with all the regulation and staff and liability that comes with it; agents do not make that part go away. But as a way to think about what you are actually building, it is a useful mirror. The question is the same either way. Which part of this do I own, and which part am I renting from someone whose roadmap I cannot see?

## How I Would Decide

You heard me talk about it above: our biggest moat in our business is our loyal customers. We have great products, great features, great penetration: but our customers are loyal to us for the exact same reasons as Larson Gross’ customers. The best way to protect yourself is to protect those around you. Deliver the product, deliver the service, deliver the deep industry knowledge, and maintain the advantage. Whether you get acquired by an investor or you run that business yourself for a decade, as I have argued in Cybersecurity conversation after cybersecurity conversation, a “defense in depth” strategy is also your best attack.

If *I was starting a new business today, that would be my focus: how can I deliver a value proposition in software that exceeds what they can get from the model, and provide my expertise to leverage it (back to the above, that’s part of why solopreneurs are both more common and often more successful).*

## Before you wrap it

**Write down the kill rule before you launch.** Decide, in advance and in writing, what the platform would have to ship for this business to stop being worth running. If you cannot describe that release, you have not looked hard enough at the roadmap you are building on. If you can, you know what to watch for every time a lab posts a changelog.

**Price inference as cost of goods.** Every model call is something you bought and are reselling. Put it on the same line as the hosting bill, track it per customer, and know your gross margin the way a restaurant knows its food cost. Base44’s journey from zero to a 60% target started with someone admitting the first number was zero.

**Keep a second supplier wired in.** Not as a theory: as a configuration you have actually switched to at least once, with the prompts and the evaluations to prove the product still works when you do. Windsurf had less than five days. Plan for fewer.

**Collect what cannot be downloaded.** Usage data, customer relationships, a workflow people have rebuilt their week around, a community, a trust position in a regulated niche. None of those come with the next model release, and all of them are what a buyer (or a lab) would actually pay for.

**Look at buying before building.** If what you are good at is running a business rather than inventing a product, there are a very large number of businesses whose owners want out and whose only alternative is closing. That route has its own costs, but the platform is on your side of it.

## Shareware season

Peter Tattam’s stack did not lose because it was bad. It lost because it was a piece the platform was always going to need to own, and he was selling into the gap until the platform got there. That gap was real money for a while, and for some people it still is.

This is shareware season again: a lot of very good small tools, built quickly by very few people, sitting in the spaces the platforms have not filled yet. Some of those people will be in the top decile that Stripe is counting. The ones who stay there will have spent the gap building something the next release cannot ship.

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today’s argument is that a one- or two-person AI business is now a real option at the top of a very steep curve, that the platform it runs on can take its features, its supply, its margin and even its foundation, and that the shops that last treat the wrapper as a way in while they build, or buy, something the next release cannot ship.*

## Sources and checks (not for print)

    SOURCES (for his reference; kept out of the body per house style)
    - Stripe Economics, "The Age of the Solopreneur", Tedeschi/Rama/Cruickshank, 22 Jun 2026 (PRIMARY): https://www.stripeeconomics.com/p/the-age-of-the-solopreneur -- "More than twice as many..."; proxy index ~115 platforms + solo Atlas; "almost certainly understates". Re-checked live 1 Oct.
    - Stripe blog, 28 May 2026 (PRIMARY): https://stripe.com/blog/top-solo-founder-traits -- median -23%, top decile +19%; 61x vs ~34x. Re-checked live 1 Oct.
    - Census 2024 Nonemployer Statistics, released 29 Sep 2026 (PRIMARY): https://www.census.gov/newsroom/press-releases/2026/2024-nonemployer-statistics.html ; table NS00NONEMP via data.census.gov: >=$1M establishments 116,803 (2022), 117,060 (2023), 126,356 (2024). Unit = establishment.
    - Carta Solo Founders Report 2025, 9 Dec 2025 (PRIMARY): https://carta.com/data/solo-founders-report/
    - Trumpet Software v OzEmail [1996] FCA 560 (PRIMARY): Tattam MD; Hobart; shareware evaluation "typically 30 days".
    - Microsoft TechNet, "Windows 95 Networking: The Basics" (PRIMARY): built-in TCP/IP. WfW 3.11 free TCP/IP: PC Week 21 Feb 1994 (contemporaneous secondary).
    - Tattam earnings: ANECDOTAL (Wikipedia over Tedium/Vice 2016 and HN 2011) -- printed only as "by most accounts".
    - ChatGPT PDF upload / Sahar Mor quote: Business Insider via Yahoo, 31 Oct 2023 (secondary).
    - Jasper valuation cut: The Information via Maginative, Sep 2023 (paywalled primary, secondary summary).
    - RELX -14.6% / TR, WK >11% at open, early Feb 2026: Investing.com; ABC News (secondary).
    - Windsurf quote: https://x.com/_mohansolo/status/1930034960385356174 (PRIMARY); OpenAI talks: TechCrunch 3 Jun 2025 (secondary, printed as "reportedly").
    - Bessemer State of AI 2025 (PRIMARY); ICONIQ State of AI 2026 (PRIMARY).
    - OpenAI Agent Builder deprecation (PRIMARY): https://developers.openai.com/api/docs/deprecations ; n8n $2.5B: Bloomberg 9 Oct 2025.
    - Base44: Wix release 18 Jun 2025 (PRIMARY); Wix Q2 2026 call transcript, Motley Fool (PRIMARY transcript) -- 0% to ~60% TARGET; Calcalist (team size, fewer than ten).
    - Cursor: Composer 2 / Lee Robinson quote, TechCrunch 22 Mar 2026 (secondary); SpaceX $60B closed 14 Aug 2026, Bloomberg/TNW.
    - Gamma: BusinessWire 10 Nov 2025 (self-reported). Tome: VentureBeat 20 Nov 2025; Forbes 20 Jul 2026 ($3M plateau). User count printed as "north of twenty million" to sit under both figures.
    - McKinsey Institute for Economic Mobility, "The Great Ownership Transfer", 26 Feb 2026 (PRIMARY) -- six million / one million viable / $5T enterprise value; 2022: 510,000 exits, 92/5/3.
    - Thrive Holdings: OpenAI 1 Dec 2025 (PRIMARY). Larson Gross: Forbes, Anna Tong, 2 Jun 2026 (secondary) -- stake via Current in 2025, 1949, 200 employees, 7,000 returns, 31%, $1B; Current partner page (PRIMARY).
    - Isenberg "$5T opportunity: AI Roll Ups", X, 26 Sep 2026: UNREACHED at source (x.com robots; firecrawl schema error). Described, not quoted.
    
    CHECK BEFORE SCHEDULING
    - "OpenAI ownership stake" in Thrive Holdings: OpenAI's 1 Dec 2025 post is the primary; re-read for exact wording before print.
    - Tome founders "walked away from presentations ... to build a CRM" (Lightfield): VentureBeat. Fine as written; re-read if challenged.
    - Isenberg glossed as "startup investor and podcaster" from general knowledge; confirm the gloss at his own bio (affiliation-at-primary rule).
