# Ninety Percent Cheaper, and Still Metered

**Status: DRAFT rv1 -- Wednesday, 9 September 2026. Drafted 6 Sep from the Wed 9 block of `References\week-plan_2026-09-07.md` (v1.1) plus the 4 Sep addenda and the 6 Sep pre-draft re-check in `References\research_canva-inference-cost_2026-08-25.md`, against the landed seven-day window rather than the plan's summary of it. ~2,680 body words. Em-dash-free; zero contractions outside quoted speech; US spelling. NOT PANELLED. ONE [YOUR TAKE] OPEN. No open [VERIFY]. He pushes to Substack himself.**

**Series: Weekday feed (Wednesday) · Thread: Inference Sovereignty × Ad Hoc Regulatory · Register: the unit cost**

**rv1 CHANGES, 8 Sep 2026 -- perishability re-check against the window as it now stands, plus his Figma ruling. No panel run.**
**1. CLOSE REWRITTEN. v1's first close paragraph ("nothing about it was a governance decision, and it produced a governance outcome anyway") ran the same machinery as Mon 7's scheduled close ("the choice does not feel like a governance decision when it is made, because it reads as an administrative tidy-up") two days earlier. Zero shared vocabulary, which is why only a register sweep catches it. Mon 7 is signed off and cannot move. Wednesday now lands on the two documents that do not speak to each other rather than on the innocent-looking decision. The loyalty payoff paragraph is unchanged.**
**2. HEADER `## What Canva actually said` -> `## In their own words`. It was the fifth "actually" header in the seven-day window (Wed 2, Thu 3, Fri 4, and Tue 8's rv1 which landed 8 Sep, after this draft was written). Mon 7's panel renamed its own instance specifically because this one was running forward.**
**3. ACTION SECTION thinned against Tue 8. Action 1 no longer says "in writing" (Tue 8's action is a written look-up one day earlier). Action 3 was a write-down-and-inventory, one day after Tue 8's inventory-and-count; it is now a read-your-policy-against-them, which is a different act. Its closing prediction about which organizations will struggle was also cut as an unearned absolute about a population.**
**4. FIGMA NUMBERS CUT on his ruling, 8 Sep. The 27% -> 14% FCF margin and 48% -> 36% guide were aggregator-sourced and used unattributed, the softest footing in the piece. The shape is kept: Figma absorbed the cost and it showed. Nothing else depended on the figures.**
**Still open: ONE [YOUR TAKE] after the AI Pass section. Not panelled. Not emailed. He pushes to Substack himself.**

**Source: research_canva-inference-cost_2026-08-25.md (25 Aug note, 4 Sep addendum, 4 Sep AI Pass verification, 6 Sep re-check) · research_oaic-adm-guidance_2026-07-27.md · canva.com/pricing, canva.com/help/ai-pass, canva.com/help/ai-top-ups, canva.com/help/data-residency, all fetched 6 Sep 2026**

---

Canva cut the cost of serving a single AI task by roughly ninety percent in about three months. Its cost to serve each user went up over the same period anyway.

Both of those are the company's own numbers. Almost everything written about Canva in the last month printed the first one and left the second one out, and the pair is the entire story. A unit cost fell by an order of magnitude, the bill got worse regardless, and the company responded by holding back a product release -- not because the product was broken, because it was working -- and then putting a meter in front of it.

If you have ever run a points program, you already know this mechanic in your bones. A club prices its loyalty program on an assumption about how members behave: what fraction of points get earned, what fraction get burned, how many sit unredeemed on the books forever. The assumption is invisible while it holds. Then something changes the behavior, redemption climbs, and the liability that was a rounding error becomes a line item somebody has to explain. What you do next is instructive, because you do not usually apologize and you do not usually withdraw the program. You change the earn rate. You put an expiry on the points. You add a tier. The program continues, the members mostly do not notice the day it happened, and the economics quietly come back inside the fence.

That is what happened to Canva this year, at a scale most of us will never operate at, and the useful part is that they wrote a fair amount of it down.

## In their own words

In early August, Canva told shareholders it was cutting its 2026 revenue growth forecast from about thirty percent to about twenty percent. Not revenue. Revenue was US$921.9m, up 25.2% year over year, which is a good year by any standard anybody reading this would recognize. What fell was the growth guidance, by a third, and the valuation marks that had been priced against the old guidance came down behind it: Blackbird and AirTree remarked Canva from US$42bn to US$34.9bn on 14 August 2026, Canva's own independent valuer went to US$31bn, and the IPO slipped to 2027.

The reason given was that the average cost of serving an AI task was, in CEO Melanie Perkins' words, "too high." The diagnosis underneath it is the sentence worth carrying around, because it is unusually specific for a company explaining a downgrade:

> "We were relying too heavily on frontier models. Several of our first-party models were not yet ready for release, and our pricing, consumption model and usage controls had not caught up with the outsized demand we were seeing."

Three things were not ready, and only one of them is technology. The models. The price. The meter.

And then the decision, also verbatim:

> "Rather than broadly rolling out a product before the underlying economics were ready, we decided to slow the rollout while we rebuilt the architecture, reduced unit costs and strengthened the business model."

Canva AI 2.0 launched in April 2026. Demand "significantly exceeded" projections and users began creating three times the designs. Roughly three months of rebuilding followed, in-house models were substituted for frontier-vendor APIs, and cost per AI task came down about ninety percent. The next release is now gated on unit economics in writing: "We'll roll out Canva AI 2.1 thoughtfully, expanding access as we continue to monitor quality, engagement and unit economics." Cliff Obrecht, on stage at Stripe Tour Sydney on 19 August, put it more plainly. They had to slow the rollout "whilst we get those costs in check."

Read the sequence rather than the headline and the shape changes completely. This is not a company whose AI feature failed. It is a company whose AI feature succeeded past the point its pricing could absorb, and whose response was to treat *access* as the control variable.

## The half of the number that goes missing

The ninety percent is a per-task figure. It is a ratio against a base Canva has never published, measured by Canva, against unnamed "frontier alternatives," with no methodology and no third-party verification. That does not make it false. It makes it a company measurement, and the correct way to print it is "Canva says."

The number that matters more sits right next to it and travels almost nowhere. Per-task cost down ninety percent, designs created up three times, and cost to serve each user up. Those three facts are mutually consistent and they describe the single most important thing about running anything on inference: **the unit cost is not the bill.** You can win the unit cost decisively, by a factor most infrastructure teams would sell a kidney for, and lose the aggregate, because the thing you made cheaper is the thing your customers immediately did much more of.

There is no dollar figure anywhere for Canva's total inference spend. I went looking specifically for one. No annual figure, no quarterly figure, no percentage of cost of revenue, nothing. What was disclosed was a growth-rate consequence and a unit-cost improvement ratio, and what was withheld was every absolute number that would let you check either. If you see a total in circulation, somebody extrapolated it.

## The meter

Here is the part that closes the loop on Perkins' sentence, and I think it is the most useful thing in the whole story for anybody buying software.

Canva now sells AI Pass. It is an add-on to a Pro or Business plan, and it is "USD $100 globally per person, per month." It buys "40x more AI" than Pro and Teams, and "20x more" than Business. Standard, Premium and Ultra tools draw from one shared allowance and burn it at different rates. When you get close to the edge, "Canva will notify you as you approach your AI allowance limit so you can plan your work accordingly." After that you upgrade, or if you are on Business you buy a top-up -- a one-time purchase equal to a month's allowance, active for thirty days, which "expires and doesn't roll over" -- or you keep working with what the help page calls "short pauses."

Short pauses. That is throttling, written as a feature, in a help center. It is also, word for word, the mechanic of every points program that ever had to be brought back inside the fence: an earn rate, differential burn rates by product, a notification before the wall, a top-up that expires, and a tier above you that solves it for money.

The price deserves stating carefully, because it is easy to get wrong and easy to overstate. On Canva's own pricing page, on the day I am writing this, Canva Pro lists at US$180 per year for one person on annual billing. AI Pass lists at US$100 per person per month, which is US$1,200 a year. The AI add-on lists at roughly six and a half times the annual price of the seat it attaches to. Regional pricing and monthly billing move that ratio, so check both prices on the same day before you quote it to your CFO, but the order of magnitude is not in dispute.

Two details are worth more than the headline price. The first is that Enterprise is excluded from AI Pass, along with Free, Education, trials and app-store subscriptions. The tier that can negotiate is not on the meter. The second is the ratio problem again: "40x more AI" is measured against an allowance Canva does not publish for any paid tier. The pricing page does publish one absolute number, at the very bottom of the ladder -- Canva Free gets "up to 200 Standard AI uses or 20 Premium AI uses" -- and everything above it is expressed as a multiple of that. So a denominator exists for the tier nobody pays for, and for the tier you actually buy, you get a multiplier and a promise. I am not going to chain those ratios together and hand you a number, because the result would be my arithmetic across two pages rather than anything Canva disclosed.

<!-- [YOUR TAKE]: this is the beat where your side of the desk is the payload. You buy and resell seat-based licensing for a living, and this is the pattern arriving in a product almost every one of your customers already has deployed. What actually happens in a renewal conversation when a feature people budgeted as included turns into a per-person add-on at six times the seat price? Do your customers see it coming, and what does it do to the "AI is basically free with the suite" assumption that a lot of buying decisions in the last eighteen months quietly rested on? Your read here, in your words. -->

## Canva is representative, not exceptional

It would be easy to read all of this as one company that mispriced one product, and I do not think that survives contact with the comparison set.

Figma made the opposite choice against the same bill. It absorbed the inference cost and kept shipping, and both its margins and its growth guidance came down in the same quarter. Two companies, two strategies, one problem. Canva slowed access and repriced; Figma paid and let it show in the numbers. Neither of them found a third option, and Figma is public and audited, which means the shape sits in filings rather than in a leaked shareholder update.

Which is the other thing worth noticing about how any of this reached us. None of Canva's disclosure lives on its newsroom or its engineering blog. It lives in a shareholder update that leaked, an email to Fortune, and a conference stage in Sydney. The company confirmed it on the record when asked. It simply chose not to publish it.

## The question the documentation does not answer

Now the part that turns an economics story into a governance one, and it is a small thing that I have been unable to stop thinking about.

Canva is an Australian company. Its product-level data residency, per its own help center, is available for the United States and the European Union. That is the list. Australia is not a residency option that Canva offers Australian customers, and residency is confined to Enterprise, Campus and District plans in any case. Canva's own disclaimer on that page is admirably direct: "Data residency isn't a compliance solution. It can help support your internal data-hosting requirements, but you'll need to consult your legal or compliance team for guidance."

The residency guarantee covers designs and comments, media files, folders, audit logs and search indexes. Where your data rests. It says nothing at all about where your data is *inferred over*. There is no sentence on that page putting generative processing inside or outside the residency boundary, and there was not one a month ago either. That is not an accusation. It is a gap in documentation that a great many vendors share, and it happens to be the gap that a company under unit-cost pressure has every commercial reason not to close, because the answer to "where does the inference run" is now the same answer as "where is the compute cheapest this quarter."

Set that against the calendar. From 10 December 2026, new APP 1.7 to 1.9 require Australian privacy policies to disclose the kinds of personal information used in automated decision-making, the kinds of decisions made solely by a computer program, and the kinds of decisions where a program does something substantially and directly related to the decision. The OAIC has signaled a broad reading, which catches recommendation and human-in-the-loop systems rather than only fully automated ones, and licensed venues are already on its list of high-risk sectors whose privacy policies it is actively reviewing. The OAIC said it intended to publish final guidance by September 2026. I looked this week and could not find it published; the consultation page is still the consultation page.

So the obligation lands in three months, the guidance to interpret it is not out, and the vendor documentation you would need in order to answer it does not address the processing question at all.

## What to do about it before December

**Put the inference question to every AI vendor in your stack, and get the answer on the record.** Not "where is our data stored." Where is it processed, by whose models, in which country, and does that change when the vendor changes its cost base. A residency page is an answer to the storage question and vendors will hand you one gladly, because it is the question they have already documented. The processing question is usually unanswered, and an unanswered question in a supplier file is a materially better position in December than an assumption in your head.

**Re-read the AI line items in your renewals as usage-based, because they are becoming usage-based.** A per-seat AI allowance with a shared pool, differential burn rates, expiring top-ups and pauses at the limit is not a feature, it is a meter, and it prices like a utility no matter what the order form calls it. Work out what your organization's actual consumption looks like before somebody discovers it at the wall, because the wall arrives during the busy week rather than the quiet one. That is the same arithmetic you would run on any consumption line, and it belongs in the budget the same way.

**Read your current privacy policy against the decisions you already automate, and do it while the guidance is still missing.** Loyalty tiering, differential offers, patron risk scoring, exclusion decisions, anything where a model's output is a key factor in what a human then decides. Take them one at a time and go looking for the sentence in your own policy that would have to cover each one. Where there is no such sentence, that is a three-month problem rather than a December one, and it is a great deal easier to read the final guidance against a policy you have just been through than against one you have not opened since it was drafted.

## The economics chose your architecture

There is a version of this story where somebody made a bad call, and it is not this one. Canva watched a cost curve, rebuilt against it, and got back an order of magnitude. Every step of that was competent. The part worth sitting with is who was in the room. Which models process your customers' work, in which country, at what quality, got settled by an engineering and finance question that had its own clean answer, and there is no document anywhere in which that appears as a question about you. No obligation attaches to a unit cost. Your privacy policy has nothing to say about a compute contract and the compute contract has nothing to say about your privacy policy, and the actual answer to where your customers' work is being read sits in the space between them.

The loyalty analogy holds all the way to the end, and here is where it stops being an analogy for a lot of the people reading this. When a program's economics break, the fix is a change to the terms of participation rather than an admission that the price was wrong. Canva made the compute ninety percent cheaper and still had to change the earn rate, because the members came more often than the model assumed. Your vendors are running the same play right now on features you bought as included. The earn rate is the part they will change quietly, and it is the part you should be reading.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that Canva cut its cost per AI task by about ninety percent and watched its cost per user rise anyway, that the company's answer was to hold a working product and ship a per-person meter in front of it, and that the same cost pressure quietly decides where inference runs at a moment when Australian law is about to start asking.*
