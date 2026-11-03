# Which Agents Are Actually Running?

**Status: DRAFT rv1 -- Wed 12 Aug 2026. Not panelled. Two open [YOUR TAKE] markers, one open [VERIFY].**
**Series: Weekday feed**
**Thread: Machine Identity × Ad Hoc Regulatory Regime (landing on clubs / AUSTRAC)**
**Builds on: "The Contractor Who Finished the Job and Kept the Keys" (Tue 8 Jul -- the census; Machine Identity's last beat); "Your AML Desk Already Knows How to Govern a Machine" (Thu 23 Jul -- put your agents in the register); "Every Gate Said Yes" (Mon 10 Aug -- the control answered the question it was scoped to ask); "Which Tasks, Exactly?" (Tue 11 Aug -- the list is the control).**
**Source: Ömer Kirca, LinkedIn, c. 1 Aug 2026 (four questions) -- [VERIFY] his exact title before publish; the brief has only "KnowBe4 / IT Security". NSW AI Operational Policy 2026 (Circular DCS-2026-02) and NSW AI procurement essentials, both primaries. Full dig: References/research_nsw-ai-operational-policy_2026-08-06.md**
**Fold note: this absorbs the back third of the banked NSW/CPS 230 draft (substack_draft_cheapest-way-to-comply_2026-08-12-rv1.md). CPS 230 deliberately NOT used here -- AUSTRAC's designated-service register makes the same mechanism point on Lars's own turf, and the technology-agnostic-beats-AI-specific payload is banked whole for a later Ad Hoc Regulatory slot.**
**Length: ~2,900w, deliberately under Mon (3,330) and Tue (3,911) -- first step in the back-half correction the week plan calls for by Thursday.**

---

Four questions went around LinkedIn a couple of weeks ago and they have been sitting in my head since. Which AI agents are operating across your business. What permissions have they been granted. What data can they reach. How is their behavior monitored.

They were posted by Ömer Kirca, who works in security at KnowBe4, and I want to be clear that there is nothing clever about them. That is the point. They are the four questions any auditor has asked about any system for thirty years, pointed at the newest thing in the building.

I have put versions of those four questions into real rooms this year. Almost nobody says "sure, let me pull it up."

Think about a regulated gaming floor for a minute, because it is the cleanest version of the opposite. Every machine out there is individually identified. It has an approved configuration, a serial number, an owner of record, and a regulator who can walk in unannounced and ask about any one of them. Nobody in that industry argues about whether the floor should be inventoried. Nobody treats the register as bureaucracy. It is simply understood that if a machine is taking money from a member, somebody had better be able to say what it is and who is answerable for it, and that understanding is so settled that the argument stopped being had decades ago.

Now go and ask the same building how many AI agents are running against its member data.

<!-- [YOUR TAKE]: You know this floor better than anyone reading. The detail I cannot supply and you can: what happens with vendor-operated equipment on a floor -- participation deals, revenue-share machines, kit the venue does not own. My understanding is that it is still on the register, still individually identified, still inspectable, because the regulator scoped the rule to what is on the floor rather than to who owns it. If that is right, say it in your own words here, because it is the entire argument of this piece delivered from inside your own industry, and it lands harder from you than from any policy document. If I have it wrong, that matters more -- tell me and I will restructure. -->

## I have told you to build this register twice, and both times I left something out

In July I wrote that you cannot govern what you cannot see, and that the first move is an honest census of every agent, integration and non-human identity holding access to something sensitive, plus who owns each one. Two weeks later I told the clubs audience that an AI agent is a designated service that needs to go in a register, described the same way you describe everything else: what it touches, what it can do, who owns it, who can switch it off.

I stand behind both. Both are incomplete, and I want to fix that today, because a register is not a neutral object. A register is a scoping decision wearing a filing system, and the scoping decision is made once, early, usually by somebody solving a different problem, and after that it silently determines everything the register will ever be able to tell you.

Monday's argument was that a control answers the question it was scoped to ask, and answers it correctly, and that the correctness is what fools you. Yesterday's was that the announcement is not the declaration, and the list is. Today is where those two meet: the list has a scope, and you did not read it.

## Why the four questions are hard, and it is not incompetence

Start with why nobody can answer Kirca cold, because the reason is structural and worth being fair about.

Agents do not arrive through one door. Some are built by your own developers and are, at least in principle, discoverable. Some arrive as a feature inside software you already licensed, switched on by a vendor release note you did not read, running under an existing service credential. Some are spun up per task by a platform your team adopted through a self-service signup that never touched procurement. And a growing number are not yours at all: they are running inside a supplier's service, doing work you pay for, on data you handed over, and their existence is a detail of how that supplier chose to deliver.

Every one of those is an actor with credentials, and only the first category reliably shows up in anything you would call an inventory.

The identity problem underneath this is the one I wrote about in July and it has not improved. Joiner-mover-leaver was built around humans, who have employment records, managers and a last day. An agent has none of those. The project ends and nothing fires. The credential lives on, the grant stays valid, and six months later there is a live privileged identity connected to something sensitive that nobody currently employed remembers creating.

So the honest position is not that people are careless. It is that the machinery for answering these four questions was designed for a population that behaved completely differently, and the new population is arriving faster than the machinery can be rebuilt.

Which is exactly the moment where you find out what your register was scoped to.

## New South Wales built the register. Properly. Watch what happened to it.

Here is why I am not writing this as an exhortation to go build an inventory, which you already know.

New South Wales has just made this mandatory across its entire government. The NSW AI Operational Policy, approved in June and published in July under Circular DCS-2026-02, binds every agency in the NSW Government sector. Nominate an Accountable Official within three months. Register every AI use case *before* it goes into use. Run the assessment framework where registration says to, and refer anything coming back high or critical to an AI Review Committee within five business days. File a signed annual attestation, endorsed by the Accountable Official and approved by the Agency Head, by the thirty-first of October each year.

That is the census, made compulsory, with a name against it and a date on it. It is more than the Commonwealth has built, and there are clauses in it I did not expect a state government to write down. Agencies have to be able to keep operating if an AI service becomes unavailable or materially changes, with tested continuity plans for AI dependencies on critical services -- a government refusing, in writing, to become dependent on a vendor it cannot replace. Records of AI-informed decisions affecting people's rights or access to services have to be retained as State records, so the audit trail cannot live only inside the provider's platform. And one line I would pin above a desk: *treat all inputs to and outputs of AI systems as potentially shared with the provider.* Stated flat, as policy.

Somebody thought hard about this document. Then the scope got written.

*"The requirement to register AI use cases does not apply to third-party suppliers providing services to the NSW Government where they use AI as part of those services. These arrangements are managed through procurement, contracting, and supplier assurance processes."*

Forty words. The register covers AI the agency runs. It does not cover AI the agency buys the output of. And the register is not a filing cabinet -- it is the artifact the Office for AI reports against and the annual attestation certifies. So an agency can be fully, provably compliant with the strongest AI governance instrument in the country while having no idea what its major suppliers are running inside the services it depends on.

Now the correction I owe you before somebody hands it to me, because the obvious version of this argument is wrong. Supplier AI in New South Wales is **not unregulated. It is unregistered.** The state's AI procurement guidance names outcome-based AI procurement as a primary procurement type, expects a triage at planning and a self-assessment at sourcing, and sits under a framework carrying statutory force under the *Public Works and Procurement Act 1912*. Vendor AI gets looked at. It gets looked at once, at purchase, by a different track, and then it never enters the central inventory or the attestation. The claim I will defend is about visibility and the reporting line built on it, not about coverage, and I want to be held to the narrower one because the narrower one is true.

There is a better fact underneath anyway. That procurement guidance was last updated in May, two months before the policy was published, and it still describes the older self-assessment world rather than the register world the policy just created. Two mandatory tracks inside one government, four months apart, not yet reconciled with each other.

## The template that got the scoping right is already in your building

Which brings it back to the floor, and to the thing I keep saying about AML because it keeps being true.

The AUSTRAC obligation does not attach to a technology. It attaches to a *designated service*. If you provide the service, the obligation follows, and it does not matter what you built it out of, who owns the equipment, or whether the thing performing it was invented after the rules were written. Scope by what is being done and who relies on it, and the net catches things nobody had thought of when the net was made. Scope by what you yourself operate, and the net catches what you operate.

That is the whole mechanism, and New South Wales made the newer, more targeted, more thoughtful choice and got the smaller net.

So when I said put your agents in the register, the sentence I should have added is: and go read the definition at the top of the register, because that sentence is the control. An agent register scoped to "systems we deploy" will never contain the agent your core platform vendor switched on in a point release, running against your member data, under a credential your team issued three years ago for something else.

## Compliance follows the cheaper path, and somebody chose it

Now the part I actually want you to take away, because the scoping choice would be a technicality if it were free.

Being inside the register costs money and keeps costing money. In the NSW case, a high or critical rating pulls a Privacy Impact Assessment, a Human Rights Impact Assessment, a cybersecurity review and a committee referral, per use case. Above five million dollars there is another layer of central oversight. Then the standing obligations start and never stop: tested continuity plans, State Records retention, and a maintained human channel anywhere the AI faces the public -- which quietly caps how much of the savings case anyone can ever book, because you are now running both channels forever.

Being outside the register costs a triage and a self-assessment, once, at purchase.

So the instrument prices AI you run above AI you buy, and the gap is not small. Put yourself in the chair. You have a use case that is going to come back high, a delivery date, and a finance partner who has already asked twice what the assessment work will cost. You do not have to be cynical to buy the outcome instead of running the model. You only have to be busy.

That is a control whose own price signal pushes work out of the register the control just built. And the same arithmetic is running in your shop right now, wearing different clothes. Every organization standing up an agent inventory this year is deciding, usually in a working group, usually in one line nobody escalates, whether the inventory is scoped to what we run or to what we rely on. The second is the right answer and it is more expensive, so the first one wins by default, and it wins quietly.

Which is the sentence I would like to leave you with. Compliance arriving through what your vendors infer on your behalf is an expense line. It is a decision somebody made about where the cost of governance should sit, and it can be defended -- there are good arguments for putting the burden on procurement and the contract rather than on a central register. What it is not is a thing that happened to you. Nobody was forced into that scope by circumstance. Somebody chose it, and it was cheaper, and in most buildings nobody wrote down that a choice had been made at all.

<!-- [YOUR TAKE]: The insider beat, and it is the one nobody else writing about this can do -- you are the supplier on the other side of that exclusion. When a client's AI obligations land on the contract rather than on their register, what actually happens on your end? Do you get asked what you run, by whom, and how specifically -- and does the question look different coming from procurement than from the risk function? The honest version of "an agency can be compliant and not know what its vendors run" is presumably that some vendors would answer in real detail if anybody asked, and mostly nobody asks. If there is a time you volunteered something a client had not thought to ask for, that is the paragraph. -->

## What I would actually do this week

**Read the definition, not the register.** Find the sentence in your own AI or agent inventory that says what goes in it. Not the tool, not the dashboard, not the count. The definition. It is usually one line and it is usually in a document nobody has opened since it was approved.

**Then ask the question the definition cannot answer.** Take your single most critical supplier -- the one whose outage would put you on the phone at two in the morning -- and ask what AI is operating inside the service they provide you, what it touches, and how you would find out if that changed. Not whether they *have* an AI policy. What is running, on your data, today. The answer, or the shape of the non-answer, tells you exactly how wide your register really is.

**And put the date on it.** If the definition was written before agents started arriving inside other people's products, it was scoped for a world that no longer exists, and it is doing exactly what it was built to do while telling you almost nothing.

## The fifth question

Kirca's four are the right four, and they are the ones every board is going to be asked in the next eighteen months. Which agents are operating. What permissions. What data. What monitoring.

But there is a fifth one sitting underneath them, and it is the one that decides whether the other four ever get an honest answer. It is not "which agents are running." It is which agents your register was built to be capable of seeing -- and whether anyone in the building can tell you when that was decided, by whom, and what it saved.

---

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that an agent register is a scoping decision rather than a filing system, that scoping to what you operate rather than to what you rely on is the cheaper choice and therefore usually the default one, and that the governance you get through your vendors is an expense line somebody selected, not a circumstance anybody was handed.*
