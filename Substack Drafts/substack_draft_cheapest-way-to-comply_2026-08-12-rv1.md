# The Cheapest Way to Comply Is to Buy It Instead

**Status: DRAFT rv1 -- Wed 12 Aug 2026. Not panelled. Carries open [YOUR TAKE] markers.**
**Series: Weekday feed**
**Thread: Ad Hoc Regulatory Regime · AI Sovereignty · Supply Chain**
**Builds on: "Which Tasks, Exactly?" (Tue 11 Aug -- the list somebody signed); "Control You Can Locate" (Wed 5 Aug -- a harness you own); "A Policy Isn't a Control. An Execution Rule Is." (Fri 31 Jul -- sign / camera / governor); "The World's Biggest AI User Has No Framework" (Wed 29 Jul -- the ad hoc regime, federal edition).**
**Source: NSW AI Operational Policy 2026 (Circular DCS-2026-02) and NSW AI procurement essentials, both fetched as primaries; APRA CPS 230 primary text; APRA Letter to industry on Artificial Intelligence, 30 Apr 2026. Full dig: References/research_nsw-ai-operational-policy_2026-08-06.md**
**Note on slot: no 10-16 Aug week plan existed on disk; this is the Ad Hoc Regulatory Regime slot the 6 Aug research note and the 17-23 plan both reserved.**

---

New South Wales now requires every one of its agencies to register every AI system it uses, before it uses it. It is the most serious piece of AI governance any Australian government has actually shipped.

It also contains one sentence, about forty words long, that keeps a fast-growing category of government AI off that register permanently. Not by accident. The sentence is deliberate, it is defensible, and whoever drafted it can tell you exactly why it is there.

That sentence is what I want your Wednesday for, because it is not really a New South Wales story. Some version of it is sitting in the AI inventory your own organization is standing up right now, and almost nobody has read it closely.

Think about a construction site for a second. Everyone who works for you gets inducted. Signed in, briefed, name on the register, and the site manager can tell you at any moment who is on the ground. The subcontractor's crew is a different arrangement. They arrive through the head contract, carrying their own paperwork, their own insurances, their own inductions done somewhere else, and the whole thing is managed by whoever signed the contract rather than by whoever keeps the register. That is not sloppiness. It is how the industry works, the paperwork is real, and it is mostly fine.

Then something goes wrong at two in the afternoon and somebody asks the only question that matters, which is who was actually on site. The register answers honestly. It also answers incompletely. Nobody lied to anyone, and you still cannot get a straight answer for another six hours.

Yesterday I argued that the only control I have ever really trusted looks like a list somebody signed. I stand by that. Today is the part I owe you, which is that a list is exactly as good as the sentence defining what goes on it, and that sentence is usually written by someone who is not thinking about controls at all.

## What New South Wales actually built

Give them the credit first, because they have earned more of it than they are going to get.

The NSW AI Operational Policy was approved in June and published in July, issued under Circular DCS-2026-02, and it binds every agency in the NSW Government sector along with statutory authorities and their employees. State Owned Corporations and advisory entities are recommended rather than mandated. Four hard obligations sit at the center of it. Nominate an Accountable Official within three months. Register every AI use case before it goes into use, and existing use as soon as practicable. Run the AI Assessment Framework where registration tells you to, and refer anything that comes back high or critical to the AI Review Committee within five business days. File an annual attestation, endorsed by the Accountable Official and approved by the Agency Head, by the thirty-first of October each year, with the first one due in 2027.

The assessment instrument is sixteen mandatory questions that produce a risk level and, depending on that level, pull in a Privacy Impact Assessment, a Human Rights Impact Assessment and a cybersecurity review. The review committee has twelve members and is chaired by Professor Ed Santow, who was Australia's Human Rights Commissioner and has been arguing about automated decision-making since well before it was fashionable to.

And then there are three clauses in that document that I did not expect to see a state government write down.

The first: agencies must ensure AI systems maintain continuity of government services, including the ability to operate or transition if an AI solution, model or service becomes unavailable or materially changes, and AI dependencies supporting critical services need tested business continuity plans. That is a government refusing, in writing, to become dependent on a vendor it cannot replace.

The second: records of AI-informed decisions affecting people's rights, interests or access to services must be captured and retained as State records under the *State Records Act 1998*. You cannot rent that audit trail. It cannot live only inside the provider's platform, and if it goes missing that is a reportable event.

The third is the one I would print out and pin up. *Treat all inputs to and outputs of AI systems as potentially shared with the provider.* Stated flat, as policy, by a government. Everything I have been writing about inference sovereignty for two months, arriving not as infrastructure spend or as a data center subsidy but as an acceptable-use clause that costs nothing and bites the week it is written.

This is not a box-ticking document. Somebody thought hard about it.

## The forty words

Here is the sentence, verbatim.

*"The requirement to register AI use cases does not apply to third-party suppliers providing services to the NSW Government where they use AI as part of those services. These arrangements are managed through procurement, contracting, and supplier assurance processes."*

So the register covers AI the agency runs. It does not cover AI the agency buys the output of. An agency can be fully, provably, auditably compliant with the strongest AI policy in the country and have no idea what its major suppliers are running inside the services it depends on.

And the register is not a filing cabinet. It is the artifact the whole regime is built on. It is what the Office for AI reports against and what the annual attestation certifies. Draw the scope of the register and you have drawn the scope of everything downstream of it.

## Now the correction I owe you, before somebody hands it to me

The obvious version of this argument is wrong, and I would rather say so than have a procurement officer take the piece apart in the comments, which they would be entitled to do.

Supplier AI is not unregulated in New South Wales. It is unregistered. Those are different words and the difference matters.

The state's AI procurement essentials guidance names, as a primary procurement type, *"platform, service or outcome-based procurement involving AI: contracting a supplier to deliver a specific outcome or deliverable, where the supplier utilises generative AI technologies as part of service provision."* It expects an assessment triage at the planning stage and a self-assessment at sourcing. It sits under the Procurement Policy Framework, which carries statutory force under the *Public Works and Procurement Act 1912*, and NSW buyers must comply with its mandatory requirements in every procurement activity. That is not a gentle suggestion.

So vendor AI gets looked at. It gets looked at once, at the moment of purchase, by the procurement track, and then it never enters the central inventory or the annual attestation. The defensible claim is about visibility and the reporting line built on it, not about coverage, and I want to be held to the narrower claim because the narrower claim is the true one.

There is a better fact underneath, anyway. The procurement guidance was last updated in May, two months before the policy was published, and it still describes the older self-assessment world rather than the register world the policy just created. Two tracks inside one government, both mandatory, neither yet reconciled with the other. That is the ad hoc regulatory regime I have been writing about all year, except this time it is not federal against state or industry against statute. It is one government, two instruments, four months apart.

## The rule that never says "AI"

Now put it next to something that works differently, and stay honest about the fact that these are not the same kind of instrument.

APRA's CPS 230 is a prudential standard binding banks, insurers and superannuation funds. It has applied since July of last year, with an amended version commencing this July. Its register is a material service provider register, not an AI register. It is not a public-sector policy and it was never trying to be.

It also contains no mention of artificial intelligence. None. Not AI, not inference, not models, not data residency. I got this wrong myself earlier in the year and ran a correction on it, and the correction turned out to be more interesting than the error, because here is what the standard actually does. Materiality is functional. A material arrangement is one the entity relies on to undertake a critical operation, or that exposes it to material operational risk. That is the whole test, and it does not care what technology is inside the box.

Which means vendor AI is caught. Not because a regulator named it, but because if you rely on it to run a critical operation, it is in scope by definition, wherever it sits and whoever owns it. And there is a sharper edge: a material offshoring arrangement is defined as a material arrangement where the service is performed outside Australia, explicitly including cases where the provider is incorporated here but the work happens elsewhere. You have to notify APRA *before* you enter one. Given that every major cloud and model provider documents, in their own materials, that inference can route outside the nominated geography by default, that is a live duty and not a theoretical one.

APRA did write to industry about AI, at the end of April, alongside a parallel letter from ASIC. Boards should maintain sufficient understanding and literacy. Map the full AI supply chain including material, third-party and fourth-party dependencies. Contract for audit rights, model updates, incident notification. Plan for concentration risk with credible substitution and exit arrangements. Sensible, all of it. And the letter never mentions CPS 230, data location, offshoring, sovereignty or inference services once, which tells you the expectations are not arriving as new AI powers. They are arriving through machinery that already existed.

So here is the payload, and it is not "the states and the Commonwealth disagree." That is the setup.

**The technology-agnostic instrument catches AI. The AI-specific instrument does not.** A register keyed to function and reliance nets everything you depend on, including things nobody had invented when it was drafted. A register keyed to the technology you yourself operate nets only what you operate. New South Wales made the newer, more targeted, more thoughtful choice, and got the smaller net.

I do not think that inverts the whole AI policy debate on its own. But it should give pause to anybody whose position is that AI needs bespoke rules because the general ones cannot reach it. Sometimes the general ones reach further, precisely because they never had to guess what they were reaching for.

## Follow the money, because the money is the argument

The scoping choice would be an interesting technicality if it were free. It is not free, and once you price it the whole thing tilts.

**Being inside the register is expensive and it keeps being expensive.** A high or critical rating pulls a Privacy Impact Assessment, a Human Rights Impact Assessment, a cybersecurity review and a committee referral within five business days, per use case. Above five million dollars the Digital Assurance Framework adds central oversight on top. Then the standing obligations start: tested business continuity plans for AI dependencies on critical services, State Records retention of AI-informed decisions, and a maintained human or non-AI channel anywhere the AI faces the public. That last one is a single sentence in the policy and it quietly caps how much of the savings case an agency can ever book, because you are running both channels forever.

**Being outside it costs a triage and a self-assessment at sourcing.** One time. At purchase. No register entry, no attestation line, no committee referral, no continuity obligation of its own.

So the policy prices in-house AI above bought-in AI, and the gap is not small. Put yourself in the chair. You are a director with a use case that is going to come back high, a delivery date, and a finance partner who has already asked twice what the assessment work is going to cost. You do not need to be cynical to buy the outcome instead of running the model. You just need to be busy, and everyone in that building is busy.

Which gives you a control whose own price signal pushes work out of the register the control just built.

I have seen this exact shape once already this year from the other government. The federal plan courts foreign capital to build data centers in Australia and mandates that they be energy-neutral, which raises the unit cost of Australian compute, which means the cheapest inference stays offshore. A sovereignty policy whose price signal pushes inference out of the jurisdiction. Same country, same year, same failure mode: the instrument is well drafted, the incentive underneath it points the other way, and the incentive wins because incentives always win against paperwork.

<!-- [YOUR TAKE]: This is the spot for the insider view, and it is the thing nobody else writing about this policy can say. You sell technology into regulated environments on both sides of the Pacific -- you are the supplier on the other side of that exclusion. What actually happens on your side when a client's AI obligations land on the contract rather than the register? Do you get asked what you run, by whom, how specifically, and does the question change when it comes from procurement versus from the risk function? The honest version of "an agency can be compliant and still not know what its vendors run" is presumably that some vendors would answer in detail if anybody asked, and nobody asks. Worth a first-person beat here -- and if there is a moment where you volunteered something a client had not thought to ask for, that is the paragraph. -->

## Mandatory at the front, softer all the way back

One more thing before the objections, and I want to be careful with the tone, because this is not a gotcha.

The registration requirement is mandatory. Everything behind it is lighter than that. The annual attestation is self-signed; the Office for AI *strongly recommends* that agencies fold compliance into existing audit and assurance programs, which is a recommendation and not a requirement. The Review Committee's advice on critical-risk systems is, in the policy's own words, *"advisory, with agencies retaining full decision-making authority and accountability."* No penalties or enforcement provisions appear in the document at all. There is an extension pathway, in writing, with a remediation plan and milestones, which is a genuinely sensible piece of drafting.

And there are no numbers. Nothing published on how many use cases are registered, nothing on how many came back high or critical, no committee case counts, no outcomes, no annual report. I went looking properly. The absence is not a gap in my research; it is the current state of the record. The Auditor-General has an audit of AI governance across NSW agencies scheduled for this financial year and has not yet reported, and that is the moment this all gets tested by somebody with the standing to insist.

Which, by the way, is why I am writing this now rather than after. Anybody can say a regime had a hole in it once the audit says so.

## The swings I would take at this

**"You are comparing a prudential standard to a public-sector policy."** Yes, I am, and they are not like-for-like. Different legal instruments, different regulated populations, different registers doing different jobs. If you want to argue that the comparison is unfair as a comparison, you win that one and I concede it in three words. What I am arguing is narrower and survives the concession: the *scoping mechanism* is the variable, and you can see its effect precisely because everything else about these two instruments is different and they still land on opposite sides of the same question.

**"Procurement covers it, so there is no problem."** Covered at purchase, yes. My argument is about what happens in year two, when the model behind the service is swapped, the provider's subprocessor changes, or the inference moves region. The policy asks contracts to support mechanisms for suppliers to disclose AI use and notify material changes over time, which is the right instinct. The procurement guidance imposes no blanket disclosure duty of that kind; the nearest thing is that buyers should assess whether the system can notify *users* they are interacting with AI. Telling a citizen they are talking to a bot is not telling the agency what changed in the stack. Do not let the two blur, because they read similarly and do completely different work.

**"A register is not a control anyway."** Fair, and I have made that argument myself about policies that were only ever a sign by the road. A register is an instrument, and it is worth exactly what it can see. That is the point rather than the counterpoint.

## This is not a New South Wales story

Every organization standing up an AI inventory this year is making the same scoping choice, usually in a working group, usually in a single line that nobody escalates, and usually in the same direction. List the models we run. List the tools we licensed. Vendor AI arriving inside a service we bought goes to third-party risk, where it becomes a questionnaire at onboarding and then, functionally, nothing.

So there is one question worth asking on Wednesday, and it costs you one meeting. Not "do we have an AI inventory." Ask what the inventory is *scoped to*, in the actual words of the actual document, and then ask whether the AI your biggest supplier runs inside the service you depend on appears anywhere in it. If the answer is that it is handled through procurement, you now know exactly what that means and exactly when it was last looked at.

New South Wales did the hard thinking, wrote it all down, and then wrote forty more words that decided how much of the problem it would ever be able to see. Those forty words were the cheapest thing in the document to draft. They will turn out to be the most expensive thing in it to have drafted.

The question I cannot answer for you is whether the sentence in your own document was a decision somebody made, or just the way it came back from the working group. There is a real difference between those two, and only one of them is a control.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the scope of an AI register decides everything downstream of it, that the instrument which never mentions AI can reach further than the one written for it, and that a compliance regime whose price signal pushes work outside its own boundary will lose to that price signal every time.*
