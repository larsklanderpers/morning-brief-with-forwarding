**Status: DRAFT v1 -- Thursday, 22 October 2026. Not panelled. Not delivered.**
<!--
Drafted 21 Oct 2026 evening PT (Thu 22 day chat), on his word ("Research, then draft"), under the standing ruling of 15 Oct: research, then draft, questions in [YOUR TAKE].
SLOT: AI growth, Thursday leg of THE AFTERLIFE OF A HANDOVER (plan label only). The arc's up day and pivot. Feeds Sun 25 with point 3 (keeping it home trades one handover for a smaller one).
WED 21 landed on disk mid-session (substack_draft_post-room_2026-10-21.md, v1, "The House-Sitter's Keys", another chat's). Thu bookends it in one clause ("Yesterday was the house-sitter's keys") -- if Wed's title or image changes, fix that clause. De-collided from Wed: arc sentence, Wed's hand-off line (not echoed), Wed's question-form bold action leads (Thu uses conditional leads), "post" as a noun for Google's announcement.
RESEARCH: References\research_thu22-keep-it-in-the-building_2026-10-21.md. Primaries reached: Meta's post, the Muse Model License on Hugging Face, DeepMind/GovTech post, DHS FASCSA notice (Federal Register 2026-21447), MOFCOM/MOST Announcement No. 48.
HIS RULING 17 Oct: two maxed Mac Studios = $40,000 to $50,000 (his figure, attributed); NVIDIA $150,000 to $250,000 (his figure, attributed); "under $100,000 for a startup" (his). Apple's store did not list the 512GB configuration on 21 Oct; reported "late October".
DO NOT PRINT (note binds): Meta promising data stays local; Singapore tool live or named ScamShield; DHS order covering or exempting self-hosted DeepSeek weights; MOFCOM thresholds as MOFCOM text; any Apple price for 512GB; "the license cannot be revoked".
WINDOW AVOIDED: Thu 1 Copilot+/NPU/"modern machine"; Thu 8 room/hostel/hotel/house rules; Thu 15 price-drop argument, "half a cent" (Thu 15 is named once as a series callback, by its price, not its phrase); Tue 20 head chef at the pass; Sun 18 bowl/porch/levers; no film or TV opener; "blast radius", "for free", "unmetered", "tired", "lever", "the gap", "reach", "exit", "downstream".
CONTROLLING IMAGE: the drugstore photo counter (film handed to strangers; the print at home). New to the corpus.
OPEN [YOUR TAKE]: 1 what he keeps in his own building today, and why; 2 Mac Studio vs NVIDIA in his own shop; 3 the workload he would never send out.
-->

# Keep It in the Building

*For two years, using the best AI meant sending your work to somebody else's building. For a growing share of that work, that is now a choice.*

Every serious AI workload you have run so far has left the building. As of last week, the best open model in the United States fits on two computers that sit on a desk.

Most of us of a certain age remember dropping a roll of film at the drugstore counter. You handed thirty-six exposures to a stranger, the stranger's machine developed every one of them, somebody you would never meet looked at the prints as they came off the line, and a week later you collected an envelope and hoped the negatives inside were all of them. Nobody thought of this as a risk decision. It was simply how photographs worked, because the alternative was a darkroom in the basement, and almost nobody was going to build one of those to print a birthday party. The handover was the price of the picture.

Then the camera started developing its own pictures, the printer moved onto the kitchen counter, and the photos stopped leaving the house. Not because anyone wrote a privacy policy. Because the equipment to do it yourself finally got small enough and cheap enough to be the obvious choice.

That is the shape of what happened to AI in the last ten days. Yesterday was the house-sitter's keys: the job and the access you hand out, and what both still cost long after the handover was signed. Today is the cheerful half of the week. For more of your AI work than a month ago, sending it out has become optional, and a handover you never make has nothing to come back and bite you.

## Two desks and a terabyte

On 15 October, Meta released Muse Spark Open, which it calls *"the most capable US open-weight model to date."* Open weights means Meta publishes the model itself (the trained numbers that make it work, which they call weights), so anyone can download it and run it on their own hardware, rather than only renting access through Meta's servers. The model has 816 billion parameters (those trained numbers, and a rough proxy for how much a model can do), of which 42 billion are active for any given word, a design that keeps it far quicker than its size suggests. It reads a context of a million tokens, which is a few thousand pages at a time.

The interesting part is not the size. It is where Meta says you can run it. In Meta's own words, you can *"run on your desktop using two Apple M5 Ultra Mac Studios,"* each holding *"up to 512 GB"* of memory, *"so two machines can hold an entire model,"* and the pair *"behave like one supercomputer with a terabyte of unified memory."* Apple's CEO, John Ternus, congratulated Mark Zuckerberg in public on the result. So this is a joint launch from two companies with something to sell: Meta wants developers building on its models, and Apple wants to sell you the computers. Neither of those interests makes the claim less true. They do explain why it arrived with a press tour.

Now the price, because a capability with no price attached is half an argument. Two Mac Studios configured to run this model are not desk toys. By my estimate, two of them fully loaded come to somewhere around $40,000 to $50,000. Apple had not listed the 512GB configuration on its own store when I wrote this (it is reported to arrive in late October), so treat that as my number rather than Apple's; for reference, one reviewer's 256GB configuration was priced at $12,299. The comparable NVIDIA hardware to run a model of this class sits more in the range of $150,000 to $250,000, again by my reckoning.

That difference is the whole reason people are excited. A frontier-class model, the kind you could only rent from a handful of companies a year ago, can now run inside your own walls for under $100,000, which puts it on the table for a startup, a mid-sized firm or a single business unit with a real budget, not only a bank with a data center. Fifty thousand dollars is real money. It is also a rounding error against what a lot of organizations already pay every year to send their work out.

<!-- [YOUR TAKE] 1 -- WHAT STAYS IN YOUR BUILDING TODAY. Last Thursday you wrote "send your contracts to your own inference and process them locally." What do you actually run locally today, on what, and what pushed you to it (a customer clause, a regulator, a cost line, a gut feeling)? Customer names only with your word. -->

Just so the picture is honest: running it yourself is not the same as running it well. Meta's model card says the alternative to the Mac route is a GPU with *"at least 700GB of VRAM"* for the compressed version and 2TB for the full one, which is data-center hardware. And two desktops will answer more slowly than a cloud service with racks of the stuff behind it. For a lot of the work that actually matters (the contract, the member file, the HR case, the board pack), slower and yours beats faster and theirs.

<!-- [YOUR TAKE] 2 -- MAC STUDIO VS NVIDIA IN YOUR SHOP. Would you put a pair of these on a desk at your company, or does the NVIDIA route still win for you? What would a startup do with this that it could not do last month? -->

## Sending the model to the data

The second story is smaller, and I think it is the more important one, because it shows the pattern rather than the hardware.

On 14 October, Google DeepMind and GovTech (the Singapore government's technology agency) described a scam detector built to run on the phone itself. Scams are a serious problem there; Google's write-up says they account for more than half of Singapore's reported crimes, with more than S$4 billion lost since 2019. The obvious way to catch a scam in someone's chat is to send their messages to a server that knows what scams look like. They chose the opposite.

The design has two stages. A small, cheap classifier runs on the phone and screens incoming messages; anything that looks safe gets a pass and goes no further. Only the messages that look suspicious are handed to a larger model, a version of Google's lightweight Gemma trained on local scam conversations, which also runs on the phone and reads more of the conversation to confirm the threat or clear the false alarm. The stated reason is privacy. Because the model *"runs entirely on-device,"* neither the Singapore Government nor Google *"will be able to access users' conversations through its deployment."*

Two caveats, because the coverage has run ahead of the write-up. It is not live yet; Google says the rollout inside applications will be *"carefully phased,"* with the user's consent. And Google wrote the write-up about its own model, so it is not a neutral reviewer of the design. Neither caveat changes the lesson.

The lesson is the direction of travel. For the whole of the cloud era, the default has been data-to-the-model: you send your information to wherever the clever software lives. This is model-to-the-data: the clever software goes to where the information already is, and the information never moves. A government that wanted to read citizens' chats for safety reasons chose a design in which it cannot read them, and paid for that choice with a smaller model and a second stage. That is a sentence I did not expect to be writing this year.

It is also cheaper than it sounds. The small classifier does most of the work, and the larger model only wakes up for the slice of traffic that deserves it. Every organization with a stream of sensitive material (claims, tickets, applications, member messages) can copy that shape: a cheap first pass, at home, that decides which few items are worth a closer look, and a closer look that also stays at home.

## A smaller handover, not none

Now the part Sunday will need, because it would be easy to read the first half of this piece and conclude that keeping it in the building ends the problem. It does not. It swaps a big handover for a smaller one.

When you send a workload out, you hand over the work itself. When you run open weights at home, you keep the work and take on a dependency instead: somebody else's license, and somebody else's decision about whether there is a next version.

Start with the license. Muse Spark Open is not open in the way most people hear that word. It ships under the *Muse Model License*, which Meta describes as *"limited commercial terms."* Read on Hugging Face, those terms include three things worth knowing before you build. If you offer the model as a service and your revenue from it passes $20 million in any twelve months, you *"must notify Meta and enter into a separate written agreement"* before carrying on. Your product has to display *"Built with Muse Spark Open"* somewhere visible. And your use has to comply with a usage policy Meta wrote and attached. Meta also says it *"claims no ownership of outputs,"* which is the right answer and worth having in writing. None of this is unreasonable. All of it is a relationship, and a relationship is a handover of a kind.

Then there is the supply. On 16 October, China's Ministry of Commerce and Ministry of Science and Technology published a draft revision of the country's export-control catalogue that adds 23 AI technologies, including large models and agents. Anything already released as open source is excluded, so the weights you have downloaded are yours to keep. But exporters now have to register before sending listed technology abroad, and comments close on 15 November. A great deal of the on-premise AI strategy in regulated industries quietly assumes that the best Chinese open models will keep arriving on Hugging Face at no charge. That assumption now runs through a ministry in Beijing.

And the politics comes with the weights. On 20 October, the US Department of Homeland Security published an order under the Federal Acquisition Supply Chain Security Act (a 2018 law that lets the government strip risky suppliers out of federal systems) that removes DeepSeek's products from civilian agencies, along with *"third-party products and services developed using DeepSeek implementations."* The same week, DeepSeek released new open weights that, reportedly, anyone can run at home without sending a word to China. Whether a self-hosted copy counts under that order, the published notice does not say. What it does say is that what you build on carries its maker's passport, wherever the hardware sits.

So the honest version of today's good news is this. Keeping the model at home takes your data out of the handover. It does not take you out of every relationship. You trade a vendor who holds your work for a licensor who holds your options, and for most sensitive workloads that is a much better trade. It is still a trade, and you should know which one you are making.

<!-- [YOUR TAKE] 3 -- THE WORKLOAD YOU WOULD NEVER SEND OUT. Is there something in your business that you have refused to put through a cloud model, even with the enterprise terms? What would it take for you to run it on a pair of these instead? -->

## Deciding what stays home

None of this asks you to buy hardware this week. It asks you to stop treating the handover as the default and start treating it as a decision.

**If you would hesitate to hand it to a stranger, it goes first.** Pick one workload, not a program. The member file, the HR case notes, the contracts, the claims queue: whichever one you would least like to see read back to you by somebody else. That is the candidate for running at home first, because it is where the handover costs the most if it ever goes wrong.

**If a small model can sort the stream, the big one only sees the sensitive slice.** Copy the Singapore shape before you copy the hardware. A small model running on a machine you already own can sort a stream into "routine" and "worth a closer look," and the routine part can carry on exactly as it does today. Only the sensitive slice needs the expensive answer, and only the sensitive slice needs to stay in the building.

**If you build on an open model, its license is a supplier contract.** Before anyone builds on an open model, have someone read its license the way they would read a supplier contract: the revenue threshold, the attribution requirement, the usage policy, and who wrote it. Then ask the question the DHS order raises: if the model's maker became a problem for your customers or your regulator, how long would it take you to swap it out?

**If the machine is not on the store yet, neither is your budget line.** Do not buy on a launch announcement. The 512GB Mac Studio was not on Apple's store when I wrote this. Try the pattern first on a smaller open model and the hardware you have, find out whether the answers are good enough for the job, and price the big machine against what you spend sending that same work out today. If the numbers work, they will still work when the machine ships.

## Nothing left to close

For most of the last two years, the handover was the price of the picture. If you wanted the capability, your work went to somebody else's building, and whatever happened to it there afterwards was part of the deal. That stopped being true for a meaningful share of the work this month, at a price a mid-sized business can actually pay.

Every handover you have already made is still out there, still open, still somebody else's to look after. The one you decide not to make has nothing left to close.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about AI governance (often), AI methodologies (also often), cybersecurity strategy (sometimes), and technology risk (always). Today's argument is that for a growing share of AI work, sending it out is now a choice rather than the price of admission, and keeping it in the building trades a large handover of your data for a smaller handover of your options.*
