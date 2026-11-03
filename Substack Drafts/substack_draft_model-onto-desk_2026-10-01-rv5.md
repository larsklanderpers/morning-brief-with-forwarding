<!--
rv5 (30 Sep, late): rv4 + HIS RULINGS on all seven panel items (1 Win11 'nearly five' + XP 'nearly twenty-five'; 2 mail merge 'could ... on a machine that qualifies'; 3 GPO 'neither the security barrier nor the governance barrier', 'on the local machine', '(concerns notwithstanding)'; 4 'This part is actually a pretty material consideration.'; 5 GPS soft-spot bridge added + 'holds up, up to a point'; 6 'or your device management inventory', 'Linux or Mac' (most of his devs run Macs with a Linux/Unix desktop), 'dull carries a low risk'; 7 keynote line in the close RESTORED -- one of his favorites). Skeptic 8 -> 9 on 1-2; projected Voice Score ~9.05, clears. Not re-panelled. NOT scheduled; awaits his word.
STATUS: rv4 = rv3 + EDITOR PANEL Round 1 safe fixes (30 Sep, late evening PT). NOT delivered. NOT scheduled.
PANEL: Rd1 on rv3 = 8.3 (slop categorical fail: comma-and-clause header form at 4 in window, 2 of them drafter's here). Rd2 on rv4 = 8.95 (Voice 9.5, Slop 9.5, Line 8.5, Structure 8.5, Skeptic 8.0, Taste 8.5). Bar 9.0 NOT cleared; plateau -- the remaining gap is his rulings (Win 11 age, mail-merge modal, GPO sentence, "short" line, GPS bridge). Footer present in full. 0 [VERIFY]. 0 [YOUR TAKE].
PROVENANCE: v1 = drafter. rv2 = HIS edit pass (fleet/customers para; knowledge-worker para; macros/GPO para; appended clauses: "functional economics", "but still", "or the desktop ... again", ROI / "invoice stops being the signpost", "actually a pretty material consideration", fixed asset register, "low risk of misbehaving"). rv1 = drafter re-foot (GPS para, Snapdragon para, sources). rv3 = merge + mechanics + drafter moves. rv4 changes:
  HIS text, mechanics only: '"older model", rank' -> '"older model" rank'; "CEOs indicates" -> "indicate"; "takeup" -> "take-up".
  DRAFTER text, slop/precision: 4 headers renamed (What actually ships, and when -> The plumbing came first; A modern machine, which is not the same as every machine -> Modern machines only, for now; Who pays for the answer now -> From the invoice to the refresh budget; The one caution worth carrying in -> The caution is the agents); "First, the honest part" -> "First, the history"; "Here is the honest limit, and it is a real one." -> "There is a real limit here."; "Every capability claim deserves its economics..." -> "The economics here are unusually clean."; "worth taking seriously" -> "matters"; "worth noting" cut; "quietly" x1 cut; "at Build" -> "during Build week" (it was an X post); four not-X-it-is-Y frames rewritten (the chip; the cost moved; friction; the close's last line, which drops the keynote jab -- restore if he wants it).
  Proposals to HIS sentences: NOT applied (see panel report).
Basis: References\research_thu01-model-onto-desk_2026-09-25.md + re-sweep 28 Sep. DO-NOT-PRINT audited 30 Sep: clean.
Controlling image: GPS arriving in the iPhone 3G (2008). Trumpet Winsock held for Fri 2.
Held for next week, NOT used: OpenAI DNS sandbox escape.
Sun 4 plant (his wording): "Sunday comes back to what it means when the invoice stops being the signpost." Does not pre-state the recall math; it IS a printed promise Sun 4 must pick up.
Pre-publish re-sweep (not blocking, deferred by him to Friday's chat): Microsoft notice of the Aion Insider rollout / 7 Oct event.
-->

# The Model Moves Onto the Desk

In November, Windows starts shipping with a language model already inside it. You will not download it, subscribe to it or sign up for it; it arrives with the operating system, on the machine you already bought.

That sounds like a feature announcement. It is closer to what happened to the phone in 2008.

The first iPhone, in 2007, did not have a GPS chip. Its Maps app could make a rough guess at where you were, which was fine for finding the nearest coffee shop and useless for anything that needed to follow you down a street. The iPhone 3G, a year later, put "built-in GPS for expanded location based mobile services" in the box, in Apple's own words, and the App Store opened alongside it. Within a couple of years a company called UberCab was building an entire business on the assumption that the phone in a stranger's pocket knew where it was, continuously, and that asking it cost nothing. (For those of you who are not from the United States: GPS is paid for out of general US tax revenue, run by the Department of Defense, and by US law and policy the civil signal is provided "free of direct user fees" to anyone with a receiver, anywhere. It is a detail most people never think about, and it quietly made the whole economy of "where are you right now" possible.)

The chip itself was a commodity; standalone GPS units had been on dashboards for years. What mattered was what changed once a developer could *assume* it. Before, location was something you had to ask the user to go and buy. After, it was something you could just call. The apps that came out of that shift were not better maps. They were things that had not been worth building while location was an accessory, for which the *functional economics* changed on the day that location became a standard.

That is the shift Microsoft is making with Windows over the next two months, and it matters because it moves the AI growth story off the frontier labs' servers and onto the machine that is already sitting on the desk.

## The plumbing came first

First, the history: most of what gets written up as "Windows is building an AI stack" is not new this month, and a good part of it is not new this year.

Windows ML (the layer that lets an app run a model on whatever chip the machine has, whether that is the processor, the graphics card or the neural processing unit) went generally available on 23 September 2025. The On-Device Agent Registry, which is essentially a list of the local tools an AI agent is allowed to plug into (Microsoft calls them "agent connectors, which are just MCP servers"), went to public preview at Ignite in November 2025. MXC, an open-source execution layer that runs agents inside a policy you set, was announced in early preview at Build in June 2026. The Pragmatic Engineer did a good long walk-through of all of it on 22 September, and that is where most people first saw the pieces side by side, but it is a synthesis of things that shipped over the previous year.

The new thing has a date on it.

Microsoft's own developer documentation says that Aion Instruct, a small on-device language model that replaces the older Phi Silica model behind the Windows AI APIs, "begins rolling out to Windows Insider Preview devices in October 2026 and to retail devices in November 2026, at which point Phi Silica will be removed." A standalone package for developers to test against lands in early October. And one line on that page matters more to a developer than it looks: "Unlike Phi Silica, LAF tokens are no longer needed with Aion Instruct." LAF is a Limited Access Feature, which in plain English is a permission slip you had to get from Microsoft before your app was allowed to use the model. That slip goes away.

So the order of events is: the plumbing has been going in for a year, the model that sits on top of it is now scheduled, and the gate in front of it is coming down. Microsoft is also reported to be holding a Windows and Surface event in San Francisco on 7 October on "how local AI will shape the next chapter of the PC," with Satya Nadella and NVIDIA's Jensen Huang attending; that one I have only from the trade press (Windows Latest, Windows Central and others), not from Microsoft itself, so treat the agenda as reported rather than announced.

Microsoft states a month, not a day. Some coverage has a specific date in November. I have not seen Microsoft say it, so I am not repeating it.

## Modern machines only, for now

There is a real limit here.

The in-box model runs best on the neural processing unit (the NPU, a chip designed specifically for this kind of maths) in what Microsoft has been calling Copilot+ PCs. There is a second route through the graphics card, on an NVIDIA RTX 30-series or AMD Radeon RX 9060-series card or newer with at least 6 GB of video memory, but today that route needs developer mode, an experimental Insider build and beta drivers, and Microsoft has not said when it reaches ordinary retail machines. On a plain processor with neither, the Windows AI APIs cover speech recognition and video upscaling, not the language model.

So this is a modern-machine story. A laptop bought in the last year or two with the right chip gets a model in November. A five-year-old desktop in accounts payable does not, and nothing in Microsoft's documentation suggests it will.

How many modern machines is that? Fewer than the marketing implies, but still, more every quarter. IDC put Copilot+ PCs at 2.3% of Windows PCs shipped in the first quarter of 2025 (via PCWorld). Against that, Nadella told investors in January that there are "one billion Windows 11 users, up over 45% year-over-year," and the Windows 10 end of support last October pushed a lot of organizations into a hardware refresh they had been putting off. The label itself is on its way out, too: Surface's Brett Ostrum told Windows Central last week that this year's Surfaces "are not called Copilot+ PCs," even though they meet the requirements. The name is fading; the chip requirement is not.

This is where the GPS comparison holds up, up to a point. In 2008, "every phone has GPS" was false. It was true of the new ones, and the new ones were what people bought next. Developers did not wait for the last flip phone to retire before they started building. They built for the phones that could, and the rest of the market caught up underneath them. The comparison has one soft spot: phones in 2008 were mostly replaced every couple of years, and business PCs are kept a good deal longer, some of them, as you are about to read, far longer.

Even for a software company like us, the fleet of machines is mixed (though some of that is because a lot of our developers are running Linux or Mac and don't use Windows at all); that said, it's mostly developers that fall into this model set, or replacements. Existing staff members have machines that are running Windows 11, for sure (it is nearly five years old at this point), but running a newer PC with an NPU or an RTX? Not really. They haven't particularly had a need, and so this ends up feeling to us like a hardware upgrade play in addition to an operating system change play. And our customers? I was just talking to one yesterday telling me that they had only just upgraded a bunch of core PCs in their network from *Windows XP* last year (that's a now nearly *twenty-five* year old operating system), and even that only to Windows 10, and even then only some units, and they are hesitant about the others because of the expense against the standard usage. He might as well have said "well, we're not really sure the Windows thing is going to be around for long" when he and I talked. He might be a bit exceptional, but I would estimate that upwards of 80% of the fleet our customers maintain will fall into the "older model" rank, and my brief conversations with a couple of CEOs indicate they are pretty worried about what the impact of this change will be on their organization when maybe 40 out of 200 computers are going to be in the affected set and the rest will lag even further and then may have a forced replacement cycle. That's never a cheap endeavor; it's even less so at current technology prices (especially current memory prices).

## From the invoice to the refresh budget

The economics here are unusually clean.

Nadella's phrase during Build week was "Unmetered intelligence on every desk and in every home with Windows." Microsoft's Foundry Local, the developer-facing runtime that runs open models such as Qwen, DeepSeek, Mistral, Phi and OpenAI's gpt-oss on the machine itself, is generally available and says it carries "no per-token costs" and needs no Azure subscription. The in-box Aion model, once the permission slip goes away, costs the developer nothing per call at all.

Compare that with the cloud. OpenAI's cheapest listed text model today costs $0.20 per million tokens in and $1.20 per million tokens out. That is already very cheap, and it is still a number on an invoice that goes up with every call. On the device, the number on the invoice is zero.

The cost moved, of course. It now lives in the price of the laptop or the desktop (the NPU, the graphics card and, above all, again, the memory) and in a small addition to the power bill. A developer blog responding to Build put it neatly: "unmetered" describes the billing model, not the cost. The inference you used to rent by the call, you now own, in advance, in hardware. For anyone who manages a fleet, the AI line item stops being an API budget and becomes part of the refresh budget.

To give a sense of scale, a preprint from January (Knoop and Holtmann, not yet peer reviewed) put the electricity-only cost of running models on consumer graphics cards at somewhere between a tenth of a cent and four cents per million tokens. That was measured on desktop-class cards in a small-business server setting, not on a laptop's NPU, so take it as an order of magnitude rather than a laptop price. The order of magnitude is the point.

Now, the counterweight, and it is a serious one. The one input local AI needs most is memory, and memory is the one thing the PC market cannot get cheaply right now. IDC in June forecast 2026 PC shipments down 11.3%, driven by a shortage of DRAM and storage, and said "We're not seeing any relief to the memory shortage situation before the end of 2027." So the model moves onto the desk at exactly the moment the desk is getting more expensive to fill. That does not kill the story, but it does mean the organizations best placed for it are the ones that were already buying modern machines with room to spare, and it means "free per call" arrives with a hardware bill that finance will notice long before it notices the missing API invoice.

One more thing, while the numbers are in front of us: when a call costs nothing, nothing on an invoice tells you how many times it was made. That is mostly good news, though it does make measuring impact, take-up, and effectiveness and ROI slightly more difficult. Regardless, Sunday comes back to what it means when the invoice stops being the signpost.

## What gets built when you can assume it

Think about what a developer building a Windows application has had to do, until now, to put even a modest bit of language intelligence into it: summarize this document, rewrite this paragraph more politely, pull the action items out of this email, sort these support tickets. They needed an account with a model vendor, an API key, a billing arrangement, a network connection, a privacy review of where the text was going, and a plan for what the app does when the connection drops. Every one of those is friction, and every one is a reason a small feature never gets built.

An in-box model removes most of that list at once. No key, no per-call bill, no permission slip, no network round trip, and the text stays on the machine it was typed on. For the kind of small, useful, unglamorous task a compact model handles well (summarizing, classifying, rewriting, extracting), the developer can now just call it, the way an app developer in 2009 could just ask the phone where it was.

And the same move is happening in the other pocket. Qualcomm's new top-tier phone chip, the Snapdragon 8 Elite Extreme Gen 6, unveiled at its Snapdragon Summit last week, is reported to run mixture-of-experts models of 30 billion parameters and up entirely offline (the trick is that only a small slice of the model does the work for any given word, which is what lets it fit), with the first handsets reported for this quarter. The desk and the pocket are getting the same capability from opposite directions, on roughly the same calendar.

None of this is a frontier model, and none of it is pretending to be one. Microsoft's own framing is hybrid: local for the small and routine, the cloud for the hard and the large. A bigger on-device sibling, Aion 1.0 Plan, was announced at Build as a model aimed at agent planning, due "on capable Windows devices in coming months," with no date. I would not build a roadmap on that one until it has a month attached.

So think about this from the knowledge worker perspective -- or the in-house business analyst or app developer who was always helping build macros and scripts for Office back in the day, but has seen much of that go away to a billable exercise, repeated over and over, with Copilot in the cloud, because the friction is lower (or Claude in the Excel doc, or whatever comparison you want). This type of move plays to Microsoft's strengths -- it's likely to work far better with Office than it does with Google Docs -- and it helps lower the friction even further for those knowledge workers. Closing the month probably just got a lot easier and cheaper, both, for finance. Sending out the mail merge (which I am not even sure anyone really does any more, but there are lots of similar tasks) stops being a round-trip and token expense to scrub the list, figure out who is eligible, and tie the doc to the list to Outlook; all that could be done in place, with no additional charge, on a machine that qualifies. Even those things, though, all come with a darker side, believe it or not.

## The caution is the agents

This part is actually a pretty material consideration.

Microsoft is admirably direct about the risk on the agent side. Its experimental agentic features in Windows are off by default and can only be switched on by an administrator, and its own support page names the problem plainly: "malicious content embedded in UI elements or documents can override agent instructions, leading to unintended actions like data exfiltration or malware installation." And the MXC repository says, in so many words, that "no MXC profiles should be treated as security boundaries currently." That is an early-preview project being honest about being early, which I appreciate, and it is also a sentence to read before anybody in your organization describes it as a sandbox.

A small model summarizing a document is one thing. An agent on the same machine that can act on what it reads is another, and the second one is still being built (at least from the perspective of safety and security). And lest we forget, office tools have had this problem for decades -- malicious macros have been embedded in templates for pretty much as long as there have been templates. It's why Microsoft historically has disabled macros by default until a trust boundary is established. Presumably, as they get further down the track, group policies or other types of centralized security objects will let you control *some* of what the agents are doing on the local machine. But if we have all learned anything in the last few months (concerns notwithstanding), we have learned that a model without guardrails and a harness, no matter how limited it is in total functionality, remains a dangerous thing. A group policy object is a security barrier, for sure, but it is neither the security barrier nor the governance barrier agents need. It may prove to be better to keep them **all** disabled until you are properly confident all your protocols are in place and enforced.

## Getting ready for November

**Count the machines that qualify.** Find out how many of your Windows devices have an NPU of the right class or a recent enough graphics card. That one number tells you whether the in-box model is a pilot or a platform for you this year, and it is a much easier number to get now than after somebody asks for it in a meeting. You can probably get it easily off your fixed asset register or your device management inventory.

**Try it on one boring job in October.** The standalone package lands early in the month, and Foundry Local already runs today. Pick something dull that currently goes to a cloud API or does not get done at all (meeting-note cleanup, ticket triage, a first pass on document summaries) and run it locally. Dull is the right test, because dull is what a small model is good at, and dull carries a low risk of misbehaving.

**Put the refresh and the memory in the same conversation.** If local AI is part of the case for the next hardware refresh, spec the memory for it now, while you are still deciding, rather than discovering in eighteen months that the machines you bought can run the model and nothing else alongside it.

**Ask your software vendors a new question.** Will their Windows products use the in-box model when it arrives? If the answer is yes, some text that currently leaves your machines to be processed somewhere else stops leaving, and some per-seat AI add-on pricing starts to look harder to justify. Both are worth knowing before renewal.

**Read the agent settings before anyone turns them on.** The model is the easy part. Whoever enables the experimental agentic features is enabling them for every user on that machine, and Microsoft has told you in writing what the risk is.

## Along for the ride

I doubt many people bought an iPhone 3G for the GPS chip. They bought it because it was the new phone, and the chip came along for the ride, and a couple of years later half the apps on their home screen depended on it without anyone ever deciding that they should.

The model arriving in Windows this autumn is the same kind of thing. It is small, it is modest, it runs on modern machines rather than every machine, and it will be free to call. The people who get the most out of it will not be the ones who waited for a keynote to tell them what it was for. They will be the ones who had a boring job ready for it the week it showed up.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that when Windows starts shipping a language model in the box this autumn, the growth in AI moves from the frontier labs' servers to the modern machine already on the desk, the cost of each answer moves from a per-call bill into hardware that most fleets do not have yet, and the organizations that benefit most will be the ones that have a small, dull job ready for it and the agent settings switched off until they are ready for those too.*

<!--
SOURCES (for his reference; kept out of the body per house style)
- Aion Instruct schedule, LAF line: learn.microsoft.com/en-us/windows/ai/apis/phi-silica and /windows/ai/apis/ (PRIMARY; re-read 28 Sep, page "last updated 2026-07-15")
- Hardware floor (NPU; RTX 30+/RX 9060+, 6 GB VRAM, dev mode + Insider Experimental + beta drivers; CPU = speech + video only): same Learn pages (PRIMARY)
- Windows ML GA 23 Sep 2025: blogs.windows.com/windowsdeveloper/2025/09/23/... (PRIMARY)
- ODR public preview, "agent connectors, which are just MCP servers": blogs.windows.com/windowsdeveloper/2025/11/18/... (PRIMARY)
- MXC early preview, Build 2 Jun 2026: blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/ ; "no MXC profiles should be treated as security boundaries currently": github.com/microsoft/mxc (PRIMARY)
- Pragmatic Engineer synthesis, 22 Sep 2026 (secondary; free sections only)
- 7 Oct event: Windows Latest 16 Sep 2026; Windows Central; Windows Report (SECONDARY; Microsoft invite not reached; re-swept 28 Sep)
- Copilot+ 2.3% Q1 2025: IDC via PCWorld, 18 Jun 2025 (secondary; IDC primary not reached)
- "One billion Windows 11 users, up over 45% year-over-year": Microsoft FY26 Q2 earnings (PRIMARY)
- Ostrum "are not called Copilot+ PCs": Windows Central, Zac Bowden, 24 Sep 2026 (secondary)
- "Unmetered intelligence on every desk...": x.com/satyanadella/status/2061896505481658767 (PRIMARY)
- Foundry Local GA, model list, "no per-token costs": learn.microsoft.com/en-us/azure/foundry-local/what-is-foundry-local (PRIMARY)
- OpenAI cheapest text model $0.20 in / $1.20 out per M: openai.com/api/pricing (PRIMARY, read 25 Sep) -- model name deliberately not printed
- "'unmetered' describes the billing model, not the cost": Pickuma, 2 Jun 2026 (secondary commentary; paraphrased, not quoted)
- Knoop and Holtmann, arXiv 2601.09527 (preprint): $0.001-0.04 per M tokens electricity-only, consumer Blackwell GPUs, SME server context
- IDC memory shortage, -11.3%, "We're not seeing any relief...": idc.com blog, Ubrani/Bouchard, 2 Jun 2026 (PRIMARY)
- Aion 1.0 Plan "on capable Windows devices in coming months": blogs.windows.com/msedgedev/2026/06/02/... (PRIMARY); 14B figure NOT printed (secondary only)
- Snapdragon 8 Elite Extreme Gen 6, 30B+ MoE offline, Q4 handsets: SECONDARY ONLY, attributed as "reported" in the sentence. 9to5Google 22 Sep; Tech Times 23 Sep ("the first mobile chip to run 30-billion-parameter AI models on-device without cloud access"; Q4 2026 devices: Xiaomi 18 Pro Max, Motorola Signature 27, HONOR Magic9 Pro Max). Qualcomm primary checked 30 Sep: the press release (qualcomm.com/news/releases/2026/09/snapdragon-leads-the-agentic-ai-age...) renders by JavaScript only and was unreadable; the Extreme Gen 6 product brief PDF does NOT state a parameter count. Unreached, not absent.
- Agentic features off by default, admin-only, XPIA quote: support.microsoft.com/en-us/windows/ai/ai-features/experimental-agentic-features (PRIMARY)
- iPhone 3G "built-in GPS for expanded location based mobile services"; US availability 11 July 2008: apple.com/newsroom/2008/06/09Apple-Introduces-the-New-iPhone-3G/ (PRIMARY, read 30 Sep). Apple says "built-in GPS", not "assisted GPS" -- v1 wording corrected.
- Original iPhone without GPS; App Store + iPhone OS 2.0 with the 3G, July 2008: Wikipedia, iPhone (1st generation) (secondary). The v1 claim that it located users by cell towers and Wi-Fi was NOT footed (Macworld explainer 410, gone) and is cut.
- Uber: idea 2009 (Camp); beta May 2010 as UberCab; public SF launch 2011; renamed from UberCab 2011 -- Wikipedia, Uber (secondary). "Within a couple of years ... UberCab" holds.
- GPS: "All GPS program funding comes from general U.S. tax revenues"; DoD operates; "U.S. law and policy require the civil GPS service to be provided free of direct user fees" -- gps.gov/policy/funding (PRIMARY, read 30 Sep)

RE-FOOT BEFORE SCHEDULING
- DONE 30 Sep: 2008 GPS facts, UberCab, gps.gov, Snapdragon (see SOURCES). Firecrawl failed on every call (client-side schema error), so these went through web fetch.
- Sweep 1 Oct morning: any Microsoft notice of the Aion Insider rollout or the 7 Oct event.
- Drafter absolutes already repaired at v1 ("nobody" x4 removed, including a "nobody" header, which is at saturation in the window).
-->
