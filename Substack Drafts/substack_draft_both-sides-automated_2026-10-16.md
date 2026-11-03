**Status: DRAFT v1 -- Friday, 16 October 2026. Commercial spine, Friday leg of the week-of-12-Oct arc (plan label only, never a header). Feeds Sun 18 with point 3. Not panelled. Not delivered.**
<!--
v1 drafted 15 Oct 2026 from week-plan_2026-10-12.md (Fri 16 block) and References\research_fri16-both-sides-automated_2026-10-14.md (its DO-NOT-PRINT list binds every revision).
Drafted WITHOUT the planned interview, on his prompt 15 Oct ("have you still not drafted this piece yet?"). His loyalty and rewards seat is therefore a scaffolded section with [YOUR TAKE] slots; no program, operator or member is named. The plan expected that leg to be the lead; promote it once he fills it if it proves stronger.
Footing: every healthcare figure footed at primary (BCBSA PDF, AHA 5 Oct blog and 31 Jul fact sheet, ICD-10-CM FY2026 Sec. III, CMS WISeR page, npj Digital Medicine Dec 2025) or a named secondary with the interest stated (HCA CFO via Becker's; Premier via Becker's). No neutral figure exists for the two-sided overhead and the text says so.
Opener kind: online gaming / anti-cheat (spent in window: everyday object/service x5, office document, courtroom, heist film, TV episode). No referee or umpire word anywhere.
Collision guards: not Sun 27 (who carries the loss); not Fri 9 (meter, unit, "whoever writes the definition"); no "whoever" close; no "on Sunday I will" close; no open-question close; ICD-10-CM rule used once, lightly (Sunday owns the argument).
Window callbacks to Wed 14 and Thu 15 are to v1 drafts; re-check both against what lands.
[YOUR TAKE] markers: 3. Footer: written in full.
-->

# Both Sides Automated

*When one side of a deal points a model at the rules, the other side buys one too. The rules do not get any fairer. The deal just gets more expensive to run.*

Hospitals are using AI to read their own patients' charts for anything that pays. Insurers are using AI to read the same claims for anything they can knock back.

If you have ever played a competitive online shooter, you have already seen how this goes. For most of this century the cheaters and the game studios have been building against each other. Somebody writes an aimbot (software that aims for you, faster and steadier than any human hand), the studio writes software to catch it, the cheat writers hide deeper, and the studio follows them down. The big titles now ship anti-cheat that loads before almost anything else on your PC and watches everything that runs. Every round of that has cost both sides real money and real engineering, and the honest player has paid for it too: in the install, in the occasional false ban, in the ticket price that funds all that work. The game itself is no better for it. It is the same game, run at a much higher cost to everyone who touches it.

This week has been about what happens when the party on the other side of an exchange stops getting tired. On Wednesday it was the attacker. Yesterday it was you, and the fact that you can now afford to read everything the other side sends you. <!-- Wed 14 / Thu 15 callbacks: re-check against both as landed. --> Today is the awkward next step. The other side read Thursday's piece too. When both parties to a commercial exchange point a model at the rules between them, the exchange gets more expensive for both of them, and nobody in the middle of it gets better care, better service or a better deal for the money.

The clearest place to watch it happen right now is American healthcare billing, so that is where I will start, and then I will bring it home to the part of the economy most of my readers actually run.

## Anemia, by the lab value

On 24 September, the Blue Cross Blue Shield Association (the trade group for the independent Blue Cross and Blue Shield insurance companies; for my Australian friends, these are the health insurers, the payers, on the other side of nearly every American hospital bill) published a short white paper on what it calls coding intensity. Name the interest before anything else: BCBSA is the payers' own association, the paper is three pages, it was produced in-house, and it is not peer-reviewed.

Here is what it claims. Hospitals bill an inpatient stay in a category (a DRG, the bucket that sets the price), and the bucket gets more expensive when the claim lists extra conditions the patient had alongside the main one. BCBSA says the share of Blue claims billed in the more complex, higher-paying buckets rose from 37.5% at the start of 2023 to 39.8% at the end of 2025, and it estimates "the added cost to the Blue System at about $942 million over two years." Most of that, by its count, came from 55,158 extra cases billed as complex, at an average of $11,800 each.

The part I find genuinely interesting is *which* extra conditions are doing the work. The fastest-growing ones are things like acidosis, low sodium and acute anemia after blood loss, and the paper notes that "many of these diagnoses can be derived from single laboratory values," which makes them "particularly well-suited for detection by modern RCM technology" (revenue-cycle management, the software hospitals use to code and bill). In other words, the conditions that grew fastest are the ones a model can find by reading a lab result.

BCBSA's evidence is what it calls clinical discordance: a diagnosis on the bill without the treatment you would expect to go with it. At the hospitals with the fastest coding growth, anemia was diagnosed 38% more often than at their peers (13.7% against 9.9%), and yet the patients diagnosed with it were transfused *less* often (16.9% against 19.3%). One of the paper's authors put it simply to Reuters: "If patients are truly sicker, we'd expect to see more treatment."

Now, be careful with what that does and does not show. BCBSA never observed a hospital using AI. It inferred it. The paper says the rise "coincides with hospitals adopting new AI-assisted billing software," and its own conclusion is that AI tools "may be linked to over $650 million" of the total, not the whole $942 million.

The hospitals' side of this has an interest too, and a point. The American Hospital Association (the hospitals' lobby) answered on 5 October that BCBSA's analysis "insinuates conclusions about AI-enabled coding without reviewing the underlying medical records," and that "the appropriate test for whether a patient has been correctly coded is not whether reimbursement increased." By the AHA's own arithmetic, coding intensity added about 0.3 of a percentage point to commercial spending growth. That is a fair hit. Documenting a condition that was always there, and was simply missed before, would produce exactly the numbers BCBSA is pointing at.

Both of them are arguing over the same paragraph, as it happens. The official coding guidelines (which the AHA itself helps approve) say abnormal lab findings "are not coded and reported unless the provider indicates their clinical significance." That rule was written for a human coder with a stack of charts and a finite day. It reads very differently when the coder never gets to the bottom of the stack because there is no bottom anymore.

<!-- [YOUR TAKE]: optional -- where you land between BCBSA and the AHA. The research supports either a "both have a point" read or a sharper verdict on one side; the logic test is that BCBSA inferred AI use and the AHA did not show the diagnoses were supported. -->

## Meanwhile, in the claims shop

None of this is happening to a passive insurer. The payers automated first, and at scale.

Long before anyone was talking about agents, insurers were reviewing claims with rules engines. In 2023, ProPublica reported that Cigna's medical directors had denied more than 300,000 claims over two months in 2022 using a system called PxDx, an average of 1.2 seconds of review per claim. Cigna "categorically disagree[s]" with that characterization, and to be clear, PxDx was an algorithm, not AI. But it shows how long the payer side has been doing this by machine.

The current round is more sophisticated. Since October 2025, Cigna has been automatically reducing many higher-level office-visit claims by one level unless the documentation clearly supports the higher one (downcoding, in the trade). The AHA's own fact sheet complains that "some insurers are using automated tools to partially deny claims, forcing providers to engage in burdensome and costly appeals." And the government is now a customer for the payer-side model as well. Under a Medicare pilot called WISeR, running in six states from January 2026, technology companies use "AI and machine learning" to review requests for a list of services before they are approved, and they are paid a percentage of the spending they avert. CMS says every recommendation to deny is "determined by appropriately licensed clinicians," which is good, but look at the incentive. The vendor's model is paid out of the other side's loss.

The hospitals, by their own account, are behind. Mike Marks, the CFO of HCA (one of the largest hospital operators in the US), told an investor conference in September that the insurers have "been working really hard on their version of AI in their claims shop." Then he said the part that matters most for this piece: "The administrative cost that they have and that we have to administer all of these claims is enormous."

## Paying twice for the same argument

That sentence is the whole economics of an automated standoff, and it comes from someone with every reason to blame the other side.

Follow the money around the loop. The hospital buys software to find every codeable condition in the chart. The insurer buys software to find every claim it can push back on. The hospital pays people (and increasingly more software) to appeal. The insurer pays people to review the appeals. Premier (a firm that sells revenue-cycle and denial-management services, so weigh it accordingly) estimated in 2024 that hospitals were spending $19.7 billion a year fighting denied claims, at about $44 a denial, and that more than half of the private-payer denials they appealed were eventually paid anyway. That is one side of the ledger, counted by someone who sells the remedy. I could not find a neutral figure for both sides added together, and I am not going to invent one. What I can tell you is that nobody inside the fight seems to think it is small.

A policy brief in *npj Digital Medicine* last December, by researchers at Johns Hopkins and Mass General, called this "the coding arms race," and its description of where it ends is the most useful paragraph I read all week. AI documentation tools "can increase billing and risk-adjustment coding intensity, prompting payer responses such as downcoding and risk-score recalibration." The early adopters get a temporary bump. Then the payers reset their rates, and "late adopters may end up missing the temporary upside yet practicing under a lower baseline set after everyone else's gains have been priced in." Meanwhile, in the commercial market, "employers and workers bear higher premiums until plans lower fees or downcode." Their summary of the end state: "an arms race that ends with higher administrative friction, payer pushback, and little improvement at the bedside."

Now read that as a business owner rather than as a patient. Both sides spend more. The advantage each side buys lasts only until the other side catches up. The new baseline is worse for whoever was slowest. And the bill for the whole thing lands on a third party, the employer and the employee paying the premium, who never got a vote.

The people in it know this. Aetna's chief medical officer has publicly urged the industry not to let this become "an agentic bot war." The chief revenue officer of NYC Health + Hospitals called it a "rock 'em, sock 'em robot" fight in which "nobody's going to win." When both sides of an exchange describe it that way, it is worth believing them.

## Points, tiers and the member who reads everything

Healthcare is just where this is most visible, because the numbers are big and both sides publish. The same shape is coming to every exchange where one side writes rules and the other side has a reason to find the edges of them: loyalty and rewards programs, promotions, warranty claims, chargebacks, rebates.

Think about how a loyalty program is built. The operator writes earn rules, tier thresholds, promotional terms and redemption conditions, and every one of them is priced on an assumption about how members will behave. Most members will not stack every promotion. Most will not notice the tier qualifying window resets on a particular day. Most will not work out which combination of activity earns the most for the least. A small number of enthusiasts always have, and the program could absorb them because there were not many of them and they had to do the work by hand.

A member with an agent does not have to do the work by hand.

<!-- [YOUR TAKE]: THE LEAD EXHIBIT (your seat, confirmed 9 Oct: "a loyalty and rewards angle around the automated back-and-forth between two things"). What the automated back-and-forth actually looks like from your side of the counter: which rule got read for its edges, what the member side (or a third party acting for members) automated, what the operator side built in answer, and what the round trip costs each side. No program, operator or member names unless you say so. If this proves stronger than the healthcare section, it moves up front and BCBSA becomes the outside number. -->

And then the operator does what the insurer did. It buys a model to spot the members whose behavior looks automated, tightens the terms, adds a review step, and starts declining things that would have sailed through a year ago. Some of that is fair. Some of it catches ordinary members who were simply paying attention. All of it costs money that used to go into the rewards themselves.

<!-- [YOUR TAKE]: optional -- the cost of the counter-model on your side: licences, review staff, member complaints, the goodwill line. Even a rough sense of scale ("more than the promotion itself", "a person's time a week") is worth more here than any figure I could source. -->

## The rule was the cheap part

Underneath both stories is the same thing. A great many commercial rules worked because the other side would not bother to read them closely. The coding guideline assumed a coder who would not get to every lab value. The promotion assumed a member who would not stack it. The rule was never really enforced by its wording; it was enforced by the effort it took to push on it, and that effort was free to the person who wrote the rule.

That effort is now priced in tokens, on both sides, and the answer most organizations are reaching for is a bigger model of their own. I will come back to what the better answer looks like on Sunday, because it belongs to the whole week. For Friday, the practical question is narrower: what do you do before you are in the middle of one of these?

## Before you buy the counter-model

**Read your own rules the way their model will.** Take the terms you publish (your promotions, your claim conditions, your credit and refund policies, your partner rebate schedule) and point a cheap model at them with one instruction: find every way to get more out of this than we intended, without breaking any rule as written. You are not looking for fraud. You are looking for the edges you only ever got away with because nobody pushed. Those are the ones that will be found first, and you would rather find them yourself.

**Count what the fight would cost you before you start it.** Before you match the other side's automation, put a number on the round trip: the reviews, the appeals or disputes, the rework, the staff time, the licences, and the customers you lose because they got caught in the net. I could not find a neutral version of it even for healthcare, where both sides publish, which is exactly why you need your own. If the counter-model costs more than the leakage it stops, you have bought yourself an arms race, not a control.

**Fix the rule, not just the enforcement.** Where an edge is genuinely unintended, change the rule so the edge is gone, rather than leaving it in place and building a model to police it forever. A rule that needs a machine to defend it every day is a rule that is costing you twice.

**Agree on the evidence before the dispute, not during it.** The most hopeful line in all of the healthcare reporting came from Marks, right after the cost complaint: "we do have the opportunity to help each other here." In most exchanges, the expensive part is not the rule itself; it is the arguing over whether a given case met it. Where you have a counterparty you deal with at volume, a partner, a supplier, a large customer, agree up front what evidence settles a claim. Two models checking the same agreed evidence is a much cheaper conversation than two models arguing about what the rule meant.

## Same game, higher bill

The anti-cheat war did not make anyone a better player, and the coding war, by the account of the people fighting it, is not making anyone healthier. Both sides got faster, both sides got more expensive, and the party paying for it was someone who was not at the table.

The model on the other side of your rules is coming whether you buy one or not. What you can still choose is whether you meet it with rules that hold up to a careful reader, or with a second model and a bigger bill.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that when both sides of a commercial exchange point models at the rules between them, the exchange costs more for both and improves for neither, so the cheaper move is to fix the rules a careful reader would exploit before you buy a model to defend them.*
