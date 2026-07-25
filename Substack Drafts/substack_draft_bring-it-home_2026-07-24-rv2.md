# Bring the Model Home: The Same Answer in Two Jurisdictions

**Status: Draft rv2 -- CPS 230 claim corrected against primary source + correction paragraph added, awaiting Lars's read. Was: Scheduled (rv1) -- Friday, 24 July 2026**
**Series: Weekday feed**
**Thread: AI Sovereignty / "Where It Thinks" (closes the thread opened Monday). Short tie-ins folded in: price-war economics, WAICO geopolitics.**
**Builds on: Monday's "The Compliance Tool Nobody Ordered Just Shipped as a Model" and "Not Where It Lives. Where It Thinks." (10 Jul); Thursday's AML-desk sector landing. Sets up Sunday's capstone.**
**Source spark: Kimi K3 open weights 27 Jul; the AI price war ($4-6/M tokens) and $1T semiconductor repricing against rising capex; CPS 230 in force; Privacy Act ADM 10 Dec; Albanese's National AI Standards + Office of AI; WAICO vs Pax Silica; Native-American data sovereignty (CARE/OCAP).**

---

You can rent the smartest kitchen in the world. Top of the line, better than anything you could build, available tonight, cheap. But if the landlord can padlock the door by memo, on his schedule, for his reasons, and you find out on a Monday morning with a dining room full of bookings, you do not have a restaurant. You have a hostage.

That is the shape of most organizations' AI strategy in 2026, and this week two very different rulebooks, an ocean apart, quietly agreed that it has to change. Yesterday I argued that the gaming sector already owns the governance muscle for this, on both sides of the Pacific. Today I want to close the loop I opened Monday, because the two jurisdictions we live under are pointing at the exact same architecture -- and, for the first time, the architecture is affordable to build.

## The instruction both rulebooks give

Start with ours. I have written about inference sovereignty before, but the regulatory picture hardened this month, so here it is in one breath. CPS 230 (APRA's operational-risk standard) is now in force. It does not name AI anywhere in its text -- and that turns out to be the interesting part. What it does is define a *material offshoring arrangement* as one "where the service provided is undertaken outside Australia," and require you to notify APRA **before** you enter one. A model reasoning over your member's file is a service being performed. If it is performed offshore, you are in an offshoring arrangement, and the obligation is prior notification, not paperwork after the fact. The Privacy Act's automated-decision rules land on 10 December, requiring you to disclose which AI systems make decisions that significantly affect a person. And the Prime Minister has now announced a national set of AI standards and an Office of AI inside his own department. The through-line across all three is not "where is your data." It is *where does the consequential reasoning happen, and can a regulator you answer to reach it.*

Now the other rulebook, the one I raised yesterday. Native-American gaming corporations operate under a doctrine of data sovereignty that says the same thing in older and blunter language: the data about a people belongs, in a meaningful sense, to that people, and the authority over it -- the power to say no -- cannot be quietly exported. Different history, different legal machinery, identical instruction. Keep the sensitive thinking, and the authority over it, somewhere the sovereign can actually reach.

Two jurisdictions that share no legal DNA arrived at the same sentence. When that happens, you are not looking at a local rule you can wait out. You are looking at the shape of the thing.

### A correction, and why it makes the case harder

On Monday I wrote that APRA "had drawn the line" -- that CPS 230 treats your AI vendor as a
material service provider, and that inference on member data has to happen somewhere a
regulator can reach. I should not have written it that way, and the reason is worth more than
the correction.

CPS 230 classifies no vendor category at all. Materiality is functional: a material service
provider is one "on which the entity relies to undertake a critical operation or that expose
it to material operational risk." Your voice AI vendor might be one. Your model host might be
one. The standard declines to tell you, because that determination is yours to make and
defend.

Where did my version come from? I traced it back through my own reading. Every source saying
CPS 230 classifies AI vendors was a company selling sovereign AI deployment or voice AI
compliance -- and not one of them was quoting APRA. I had absorbed a vendor's framing as a
regulator's rule, which is the exact failure mode I spend most weeks warning other people
about. If you are building a compliance position this quarter, check whether the rule you are
citing has a regulator's name on it or a supplier's.

The corrected version is worse news, not better. "Register your vendor" is a form. "Notify
APRA before the reasoning leaves the country" is a decision you have to make in advance, in
writing, with someone's name on it. The vendors undersold it.

## Why "sovereign" is not the same as "hosted"

Here is the trap, and Australia is walking straight toward the comfortable version of it. The national strategy is essentially "host the frontier": bring the big American models onto Australian data-center soil and call it sovereignty. It is pragmatic, and it is not nothing. But it answers the wrong half of the question.

Hosting is about where the data sits. Sovereignty is about who controls the thinking, and who can switch it off. As sharp voices in our own AU governance circles have been putting it this month, infrastructure sovereignty is not model sovereignty -- and real sovereignty is the power to leave. If your compliant, onshore, beautifully-hosted AI capability still depends on a model whose weights and continued availability are controlled by a foreign company under a foreign government's export law, you have rented the smart kitchen. You have not built one.

And this is not a hypothetical worry. We watched it happen. Frontier models were fenced off from the rest of the world by one government's memo, then released by another, with no warning and no vote either time. This month a 29-nation bloc stood up to write a rival rulebook for the whole field, while the incumbent side keeps a hand on the export switch. The lesson the sharpest people in the room keep repeating is that export control follows the silicon wherever the data center sits. Your access to the reasoning your business runs on is, today, a foreign policy decision. It can be granted and revoked, and you will not get a vote.

## The part that changed this month

For two years, the honest response to all of the above was a shrug, because the only models good enough to run your business lived in someone else's cloud, and bringing them home meant accepting a visibly worse tool. That is the trade that just broke.

I walked through the specifics Monday, so I will keep this to the headline: near-frontier capability is now something you can run inside your own walls. Kimi K3's weights go fully public on 27 July -- a 2.8-trillion-parameter open-weight model that already beats our frontier systems on real coding work. Cleaner-lineage Western open-weight options exist alongside it for those who need a provenance story they can defend. And the economics stopped fighting you: a price war has pulled near-frontier reasoning from the $25-to-$50 range down to $4-to-$6 per million tokens in a matter of weeks, and even a trillion-dollar wobble in chip stocks has not slowed the build-out that keeps making inference cheaper. Capability came home and the price came down, in the same few weeks. The kitchen is now something you can actually own, not just rent.

## One architecture, two regimes

Here is the good news underneath all of it. You do not need two compliance architectures for these two jurisdictions. You need one, and you have already started it.

It is the categorization exercise from Monday and Tuesday. Sort your workloads by consequence. The genuinely low-stakes, reversible work -- the delegate bucket -- can live on a frontier cloud API, because nothing that touches a person's rights or a sovereign's data is riding on it. The consequential work -- the refuse-or-verify bucket, the decisions that significantly affect a member, the reasoning over sovereign data -- goes on a stack you control, in a jurisdiction you can reach. That single sort satisfies an APRA auditor and a tribal data-governance board at the same time, because they were asking the same question. Hybrid is not a hedge here. It is the answer.

**Inventory which workloads must stay home.** Not "which AI tools do we use" but "which of our AI use cases reason over data that a regulator or a sovereign has a claim on." That list is your December homework and your migration shortlist, and you have to write it either way.

**Choose a hybrid architecture on purpose.** Sensitive reasoning on a model you control; frontier tokens for the reversible remainder. Decide the split deliberately rather than discovering it in an incident.

**Evaluate the open-weight options with clear eyes.** 27 July is a date to assess K3, Inkling, and the permissive alternatives -- capability, yes, and provenance, honestly. Open weights solve foreign gating and hand you a supply-chain question in return; both are real, and both are manageable if you look.

**Contract for inference location, not just data location.** "The vendor has an Australian region" is not an answer if the reasoning routes offshore. Put the model layer in the register, and get the location in writing.

**Never single-source the frontier.** The organizations most exposed to the next memo are the ones with exactly one model dependency. Spread your supply on purpose -- a single model, from a single vendor, under a single export regime, is just the padlock waiting for a reason.

Sunday I will try to make the week add up, because Monday's model, Tuesday's decision, Wednesday's clock, and Thursday's desk are not four topics. They are one argument, and the sovereignty piece is where it gets its spine.

For today, the close is simple. The memo that grants or revokes your access to the reasoning your business runs on does not get your signature, and it never will. The only vote you actually hold is the one you cast now, in daylight, when you decide where the thinking happens.

So cast it. Does the fact that you can finally bring it home -- this month, at this price -- actually change your calculus? Or is it just one more headline to file away, buried in a news cycle that never seems to pause, let alone stop? The landlord can still change the locks. The only question that matters is whether you are still standing in his kitchen when he does.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that two jurisdictions with nothing in common gave the same instruction -- keep the thinking where you can reach it -- and this is the month it stopped being expensive to obey.*
