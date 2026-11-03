**Status: rv2 -- MECHANICS ONLY on his rv1 (Google Doc pass). 15 Oct 2026. Not panelled. Word/tone proposals held for his ruling, not applied.**

# Cheap Enough to Read Everything

*Most of what lands on your desk from the other side of a deal was written on the safe bet that you would not read all of it. That bet just got a lot worse.*

Most of what a counterparty sends you was written on the assumption that you would skim it. As of last week, reading every word of it costs about half a cent.

In 2011, South Park built an entire episode around a single click. Kyle accepts an update to the iTunes terms and conditions without reading them, and the joke the whole episode hangs on is everyone around him reacting as though he is the only person alive who does not read the terms (he is not, of course, and that is the point). Nobody reads them. The people who write them know nobody reads them. A great deal of commercial life is built on that quiet, mutual understanding: one side writes forty pages, the other side signs page forty, and both of them treat the thirty-nine in between as a formality right up until the day one of those pages matters.

This week's thread has been about what happens when the other side of an exchange stops getting tired. Yesterday was the uncomfortable half of that, the attacker's side. Today is the half that works for you, because the same collapse in the price of attention that lets one person do a crew's work against you also lets you do something you have never been able to afford before. 

You can read everything. Completely, comprehensively, and with no lack of focus on page 27 because it's Wednesday and your kid has soccer tonight.

## Ninety percent off the sticker

On 7 October, Anthropic released Claude Haiku 5.5, the smallest and cheapest model in its current family. Anthropic describes it as built for *"high-volume, cost-sensitive tasks"* (summaries, classification, database queries, the work you would hand to a model a few thousand times a day rather than once). The price is the headline. For any request under 100,000 tokens (a token being the unit these models count and bill in, roughly three-quarters of a word), Haiku 5.5 costs $0.10 per million tokens going in and $0.50 per million coming out. Its predecessor, Haiku 4.5, cost $1.00 and $5.00.

That is a tenth of the price. It is also not quite what you will pay, and Anthropic is unusually upfront about why.

The new model uses a newer tokenizer (the piece of the model that chops text into those billable units), and in Anthropic's own migration guide, *"the same input text produces approximately 30% more tokens on Claude Haiku 5.5 than on Claude Haiku 4.5."* Same contract, more tokens. There is also a cliff: a request over 100,000 tokens pays five times the rate, $0.50 in and $2.50 out, and Anthropic's pricing page is explicit that the whole request pays the higher price once it crosses the line. Net all of that off and Anthropic's own footnote puts the average saving at *"around 75% less to run."* (Anthropic sells the model, so that is the seller's number. It is also the seller marking its own headline down by fifteen points, which is not something any of us see every week.)

So: ninety percent off the sticker, roughly seventy-five percent off the bill. Hold onto that gap, because it comes back in a minute. That said, the cost of this is a bit of diligence on your part: keep the context low, keep the costs low. Stop paying attention, or allow a service agent to process a document instead of component pages, and then process the response in the same context, and the cost goes up exponentially.

Here is what it looks like in a unit you actually deal with. Take a contract of forty-odd pages, call it 40,000 tokens on the new model's count, and ask for a two-page summary of what it commits you to. By my arithmetic from the published rates, that is about $0.004 going in and $0.001 coming out. Half a cent. The same job on last year's small model, at the old token count, runs about four cents. Eight times cheaper, not ten, which is exactly the sticker-versus-bill gap showing up in practice. Put a 130,000-token master agreement with all its schedules through in one go and you cross the cliff: about six and a half cents in. Still trivial in dollars, but five times the per-token rate for the same words, and avoidable by splitting the document in two. And if the reading can wait a few hours, Anthropic's batch pricing halves all of it again.

Six and a half cents is not a budget line.

If you've been in business for any length of time ever, you've always known that this contract risk was out there. You've always known that there was a good chance that somebody was going to slip something in if you didn't watch it really closely. It's part of the reason why everybody paid for really expensive lawyers if the contract was worth enough. Not so much because the lawyers were really necessary for the wording itself, but to make sure that the other side didn't slip something in that was going to end up costing you an amendment to a contract or a reputational problem.

For us, there have been multiple occasions where contracts have been executed with terms that are very favorable to a customer and that were actually not what our own guys intended. That ended up that way because the reviewer had a phone call come in the middle and got distracted, or had to run out and talk to a customer about something else, or otherwise got pulled into another conversation. They didn't really close out the fact that they were working on that item, nor come back to it properly later.

This is not a big deal, it’s why we and most organizations have standardized on two reviewers before final signature, but across a couple hundred contracts, it becomes a big deal. It's part of the reason why the company pays the expensive lawyer, and things are often held for longer than they need to be because of this worry.

I suppose the other part of this is not just that 6.5 cents is not a budget line, but that 6.5 cents compared to a few thousand dollars for what's effectively the same review changes the economics of an entire industry. It certainly changes the economics of how you, as an owner or operator or individual, can reach the same point in terms of reliability and coverage without the same level of spend. It's a meaningful difference. 

## The effort the other side was counting on

It is worth being precise about what the cheap part actually changes, because "AI can summarize a contract" is not news. It has been possible for a couple of years. What changed last week is not that *capacity* but rather the question you ask before doing it.

At $1.00 per million tokens, reading something carefully was a decision. You chose the big contract, the risky renewal, the document legal flagged, and you let everything else through on trust, the way everybody always has. At $0.10, the question flips. It is no longer "is this one worth reading?" or more properly, “is this one worth having the AI take a read?” Rather, it is now "why would I not read this one and candidly every one?" And once you are asking that, the list of things you have been waving through starts to look different: the terms-of-service update that arrives by email from every software vendor you use, the revised rate card, the "minor changes to our data processing addendum," the invoice whose line items nobody has checked against the contract since the second year, the forty-page policy wording behind an insurance renewal.

Every one of those was written by someone who could reasonably assume you would not read the whole thing. Not out of malice, in most cases; that is simply how the exchange has always been priced. The writer has a team, an incentive and time. The reader has a stack of other documents and a meeting in ten minutes. The assumption that the reader will get tired has been quietly holding a lot of commercial terms in place, and it has been doing it for decades.

Now, the reader does not get tired. Not because the person got better at reading, but because the person no longer has to do the first pass. A model that costs half a cent per contract will read the thirty-nine pages in the middle with exactly the same attention it gives page one, and it will do it every time, for every document, without anyone deciding it was worth it. What this means for the future of commercial arrangements is likely anyone’s guess; but if used properly, it should encourage a lot of contractual flow and cleanliness.

That is the up side of this week's argument. The cheapness that arms someone pointing a model at you arms you right back, at the same price, on the same day.

## A detector, open to anyone, for most things

The second half of reading everything is knowing what you are reading. If a counterparty can generate a convincing document, a voice note or a photo of a damaged shipment for fractions of a cent, then "who made this, and how?" becomes a question you need to be able to ask cheaply too. I actually have a couple of close friends in this fraud-detection and prevention space, and everyone who has used social media in the last few years has seen the impact of very realistic ideas and views delivered for little or no cost. They don’t work for Google, but I don’t think their work is directly competitive; however, for sure, when Google releases something similar, it means there is a real market and a real concern.

Here the news is real, and narrower than the headlines make it sound.

Also on 7 October, Google opened its SynthID Detector to everyone. SynthID is Google DeepMind's invisible watermark (a signal embedded in the content itself rather than attached to it, so it survives cropping, filters and compression better than a label would), and Google says it has marked more than 180 billion images and videos with it so far. In Google's words, *"anyone can easily check if an image, video, or audio file was made with AI from Google or our partners, including OpenAI, NVIDIA, Kakao, and soon, Apple."* It is free, global, and available in English. OpenAI runs its own verification page that looks for the same SynthID watermark plus C2PA Content Credentials (an open standard for attaching provenance information to a file, closer to a label than a watermark, and, as OpenAI notes, easier to strip).

For anyone receiving photos, video or audio from the other side of an exchange (a damage claim, a recorded instruction to change bank details, a screenshot "proving" a delivery) that new capability is a genuinely useful free check that did not exist for ordinary people a month ago. Google is not a neutral party here; it would very much like SynthID to become the standard everyone else adopts (so it can have a profit model later). That does not make the tool less useful today and for the foreseeable future.

Now the limits, because there are two, and both matter.

First, a detector only sees its own family's marks. OpenAI's page is blunt about what "no signal" means: the content *"could still have been generated by OpenAI if its metadata was stripped or tampered with, its watermark was degraded,"* or it *"could also still be AI-generated by another company's model, which the tool currently does not detect."* A clean result tells you which vendors probably did not make it. It does not tell, without qualification, that a human did, and that is really important to keep in mind.

Second, and this is the bigger one for this piece (I know, “where is he going with this exactly”): *none of the public tools check text*. Google's detector covers images, video and audio. OpenAI's page says plainly that it *"does not currently support text verification,"* with text checks available only to organizations that apply. Anthropic does watermark Claude's text, including Haiku 5.5's, but its detector is in private preview for regulators, researchers, media and enterprises with compliance obligations, and Anthropic itself says a detected mark is a signal, not proof (OpenAI has in the last week or so released watermarking in their documents as well, mostly because of requirements in the European AI Act, but still indicates it's a warning about whether AI was used, not the veracity or applicability of the document itself). 

So the one kind of content that makes up most of what a counterparty sends you, the email, the letter, the terms, the claim narrative, is the one kind you cannot yet check for provenance from your desk. Or at least, not yet.

The law is ahead of the tools on this. The EU AI Act's Article 50(2), which has applied since 2 August (with a grace period to 2 December for systems already on the market), requires providers of systems generating *"synthetic audio, image, video or text content"* to mark it *"in a machine-readable format and detectable as artificially generated,"* and asks for technical solutions that are *"effective, interoperable, robust and reliable as far as this is technically feasible."* Text is in the list. Interoperable is in the list. What has shipped to the public so far is one vendor family's detector, for media.

We process a fair bit of transactions -- driver licenses and other identity images, payment details through secure connectors, customer history and redemption transactions -- and every single one of these things is at risk of falsification in the new world. As with CyberSec and almost every other type of dual-signed technical activity, we have spent a fair bit of time, energy, and money, on defense, because the risk is real and we have felt it multiple times already -- particularly falsified IDs, where we have had to build logic that exceeds even what many third-party ID providers do to really ensure accuracy and protection.

## Where the advantage actually is

Put the two halves together and you get a fairly specific picture of what the defender's side of this week looks like.

Reading is now nearly free. Provenance is free for pictures and sound, and not yet available to you for words. And the one cost that did not fall at all is the person who has to look at what the model flags and decide what to do about it.

That last part is where I think the real advantage sits, and it is why "read everything" is not the same as "summarize everything." A model reading forty supplier agreements will happily give you forty summaries, and forty summaries is just a new pile of documents nobody reads. The value is in pointing the reading at the specific edges the other side was counting on you to miss: the clause that changed since last year, the fee that does not match the contract, the auto-renewal date, the liability cap that quietly moved, the photo that came in without any of the marks you would expect. The model is cheap. Your attention is not. Spend the model's attention so that you only spend yours on the five things that matter.

I will take a few seconds to add to this concept that there is also a new push for so-called decision models to support LLMs -- to provide an evaluatory rubric (“does this contract put us at risk given our help desk model”, though with way more detail) and then the cost of that decision or confidence ranking (depending on how you pose the request) costs even a tenth or a hundredth or less of the lowest Haiku cost. For Jev (one of the reference models), the cost of a response is so cheap *that it’s not even metered*. Combine that with what you are already supporting above and you get inexpensive reading, review, risk analysis and measurement, and evaluation across a corpus. It is environmentally entirely different.

That is also what makes this the hopeful half of the week. The side that never gets tired is not only the one across the table. As of last week, it can be yours, too.

## Making the other side's assumption wrong

So, assuming we are talking about things that are potentially adversarial (because, let’s be honest, legal agreements ALWAYS have the potential to become adversarial), there are a handful of good tactics you can take to the table right away:

**Start with the documents that were written to be skimmed.** Terms updates, renewal notices, rate cards and policy wordings are the obvious first set, because they arrive constantly and almost nobody reads them end to end. Run them through a small model as they arrive, not in a quarterly catch-up.

**Ask for the change, not the summary.** Give the model the previous version and the new one and ask what moved. Humans as well as computers both generally do better with difference comparisons than they do with just an open document. A prompt as plain as this does most of the work:

> *Here are two versions of the same agreement. List every change in the second version that affects what we pay, what we are liable for, when it renews, or what the other party may do with our data. For each, quote the old and new wording side by side. **Do not summarize anything that did not change.***

The last sentence matters more than it looks. It is what stops the model handing you a new forty-page document.

**Stay under the line.** On Haiku 5.5, anything over 100,000 tokens pays five times the rate for the whole request. For long agreements, split by schedule or by section and run them separately. It is the single cheapest optimization on this list, and it is mechanical. And if you use that to build key oversight on each section, you can combine them at the end to do a document-wide analysis as well to close it out.

**If you aren’t working with text at the moment, shift gears first and start by checking the picture, and knowing what the check means.** When a photo, video or audio file is the evidence in a claim, a complaint or an instruction to change payment details, run it through Google's SynthID Detector and OpenAI's verification page before you act on it. Treat a detected mark as a strong signal. Treat "no signal" as "not made by those vendors, probably," never as "made by a person." For text, there is no equivalent check yet, so anything that matters still gets verified the old way: a call to a number you already had (And I'm pretty sure I've talked about this before, but as a business, our best check for banking items, collections items, payments items, anything that seems nonstandard, is our receivables clerk. She is older than I am and persistent in a way that I have never been. She will continue to call until somebody answers the phone and can validate that a statement that doesn't feel right to her is right or wrong. It's a skill set that is underappreciated in the modern era, and it's a critical check and balance on anything that you do with an automated structure.)

**Budget the reading, not the tokens.** The ***tokens*** will cost you less than the coffee you drink while they run (regardless of how cheap that coffee might be). The ***flags*** will cost you a person's time. Decide up front who looks at what the model raises, and how many flags a week is a sensible number, so the cheap part does not quietly create an expensive part nobody planned for.

## The reader that does not get tired

For years, a lot of terms held because reading them carefully cost more than most people were willing to spend. As of 7 October, that cost is about half a cent a document, and the arithmetic that kept you skimming has quietly stopped being the governor. The only reason to keep doing it solely the old way is habit. And at the risk of seeming combative, the other side is counting on that habit.

The other side wrote those pages expecting a tired reader. The cheapest thing you can do this quarter is take to the review one of them that is not.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the same price collapse that arms the other side of an exchange lets you read everything they send you, and the advantage is in pointing that cheap reading at the edges the other side assumed you would skim.*
