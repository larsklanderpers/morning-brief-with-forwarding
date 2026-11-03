<!--
STATUS: rv1 (30 Sep: re-foot of the four flagged sources, his request; facts only, no voice changes) of v1 DRAFT -- Thu 1 Oct 2026 (AI growth spine, factory-floor arc day 4). Drafted 28 Sep by the Thu 1 day chat. NOT panelled. NOT delivered.
Basis: References\research_thu01-model-onto-desk_2026-09-25.md + re-sweep 28 Sep (Microsoft Learn Phi Silica page re-read: Aion schedule unchanged, page dated 15 Jul 2026; 7 Oct event still secondaries only -- Windows Latest 16 Sep, Windows Central, Windows Report).
Plan rulings honored: "ordinary MODERN machine, not a legacy computer" (his word 25 Sep) -- legacy hardware named plainly as excluded.
DO-NOT-PRINT honored (research note list): no "Qwen on Surface", no 24 November, MXC never a security boundary, ODR never a governance register, Zenith specs not used, arXiv figure not presented as a laptop number, no StatCounter share.
Window avoided: Mon 28 press/line/COGS; Tue 29 dashboard/logins; Sun 27 used car/hood/"as is"; Aug 8 kitchen/stove/ladder; Sep 9 "the meter" image; Jul 24 "open is not local"; Jul 10 sovereignty. No open-question close.
Controlling image: GPS arriving in the phone (iPhone 3G, 2008). Chosen over Trumpet Winsock / Windows 95, which is held for Fri 2 (it IS the platform-absorbs-the-wrapper story).
Held for Wed 30's call, NOT used here: OpenAI DNS sandbox escape (Fortune 26 Sep).
Open: 2 x [YOUR TAKE]. 0 x [VERIFY].
-->

# The Model Moves Onto the Desk

In November, Windows starts shipping with a language model already inside it. You will not download it, subscribe to it or sign up for it; it arrives with the operating system, on the machine you already bought.

That sounds like a feature announcement. It is closer to what happened to the phone in 2008.

The first iPhone, in 2007, did not have a GPS chip. Its Maps app could make a rough guess at where you were, which was fine for finding the nearest coffee shop and useless for anything that needed to follow you down a street. The iPhone 3G, a year later, put "built-in GPS for expanded location based mobile services" in the box, in Apple's own words, and the App Store opened alongside it. Within a couple of years a company called UberCab was building an entire business on the assumption that the phone in a stranger's pocket knew where it was, continuously, and that asking it cost nothing. (For those of you who are not from the United States: GPS is paid for out of general US tax revenue, run by the Department of Defense, and by US law and policy the civil signal is provided "free of direct user fees" to anyone with a receiver, anywhere. It is a detail most people never think about, and it quietly made the whole economy of "where are you right now" possible.)

The interesting part of that story is not the chip. The chip was a commodity; standalone GPS units had been on dashboards for years. The interesting part is what changed once a developer could *assume* it. Before, location was something you had to ask the user to go and buy. After, it was something you could just call. The apps that came out of that shift were not better maps. They were things that had not been worth building while location was an accessory.

That is the shift Microsoft is making with Windows over the next two months, and it is worth taking seriously, because it moves the AI growth story off the frontier labs' servers and onto the machine that is already sitting on the desk.

## What actually ships, and when

First, the honest part: most of what gets written up as "Windows is building an AI stack" is not new this month, and a good part of it is not new this year.

Windows ML (the layer that lets an app run a model on whatever chip the machine has, whether that is the processor, the graphics card or the neural processing unit) went generally available on 23 September 2025. The On-Device Agent Registry, which is essentially a list of the local tools an AI agent is allowed to plug into (Microsoft calls them "agent connectors, which are just MCP servers"), went to public preview at Ignite in November 2025. MXC, an open-source execution layer that runs agents inside a policy you set, was announced in early preview at Build in June 2026. The Pragmatic Engineer did a good long walk-through of all of it on 22 September, and that is where most people first saw the pieces side by side, but it is a synthesis of things that shipped over the previous year.

The new thing has a date on it.

Microsoft's own developer documentation says that Aion Instruct, a small on-device language model that replaces the older Phi Silica model behind the Windows AI APIs, "begins rolling out to Windows Insider Preview devices in October 2026 and to retail devices in November 2026, at which point Phi Silica will be removed." A standalone package for developers to test against lands in early October. And one line on that page matters more to a developer than it looks: "Unlike Phi Silica, LAF tokens are no longer needed with Aion Instruct." LAF is a Limited Access Feature, which in plain English is a permission slip you had to get from Microsoft before your app was allowed to use the model. That slip goes away.

So the order of events is: the plumbing has been going in for a year, the model that sits on top of it is now scheduled, and the gate in front of it is coming down. Microsoft is also reported to be holding a Windows and Surface event in San Francisco on 7 October on "how local AI will shape the next chapter of the PC," with Satya Nadella and NVIDIA's Jensen Huang attending; that one I have only from the trade press (Windows Latest, Windows Central and others), not from Microsoft itself, so treat the agenda as reported rather than announced.

Microsoft states a month, not a day. Some coverage has a specific date in November. I have not seen Microsoft say it, so I am not repeating it.

## A modern machine, which is not the same as every machine

Here is the honest limit, and it is a real one.

The in-box model runs best on the neural processing unit (the NPU, a chip designed specifically for this kind of maths) in what Microsoft has been calling Copilot+ PCs. There is a second route through the graphics card, on an NVIDIA RTX 30-series or AMD Radeon RX 9060-series card or newer with at least 6 GB of video memory, but today that route needs developer mode, an experimental Insider build and beta drivers, and Microsoft has not said when it reaches ordinary retail machines. On a plain processor with neither, the Windows AI APIs cover speech recognition and video upscaling, not the language model.

So this is a modern-machine story. A laptop bought in the last year or two with the right chip gets a model in November. A five-year-old desktop in accounts payable does not, and nothing in Microsoft's documentation suggests it will.

How many modern machines is that? Fewer than the marketing implies, and more every quarter. IDC put Copilot+ PCs at 2.3% of Windows PCs shipped in the first quarter of 2025 (via PCWorld; I have not reached IDC's own release). Against that, Nadella told investors in January that there are "one billion Windows 11 users, up over 45% year-over-year," and the Windows 10 end of support last October pushed a lot of organizations into a hardware refresh they had been putting off. The label itself is on its way out, too: Surface's Brett Ostrum told Windows Central last week that this year's Surfaces "are not called Copilot+ PCs," even though they meet the requirements. The name is fading; the chip requirement is not.

This is exactly where the GPS comparison holds up best. In 2008, "every phone has GPS" was false. It was true of the new ones, and the new ones were what people bought next. Developers did not wait for the last flip phone to retire before they started building. They built for the phones that could, and the rest of the market caught up underneath them.

<!-- [YOUR TAKE]: what your own fleet looks like against this line -- how much of what you run (office, dev boxes, venue-side machines) is on the modern side, and whether the Windows 10 cutoff already forced the refresh for you. A first-person read on "how many of my machines get this in November" is the thing a reader will not get anywhere else. -->

## Who pays for the answer now

Every capability claim deserves its economics next to it, and this one has an unusually clean one.

Nadella's phrase at Build was "Unmetered intelligence on every desk and in every home with Windows." Microsoft's Foundry Local, the developer-facing runtime that runs open models such as Qwen, DeepSeek, Mistral, Phi and OpenAI's gpt-oss on the machine itself, is generally available and says it carries "no per-token costs" and needs no Azure subscription. The in-box Aion model, once the permission slip goes away, costs the developer nothing per call at all.

Compare that with the cloud. OpenAI's cheapest listed text model today costs $0.20 per million tokens in and $1.20 per million tokens out. That is already very cheap, and it is still a number on an invoice that goes up with every call. On the device, the number on the invoice is zero.

The cost has not disappeared, of course. It has moved. It now lives in the price of the laptop (the NPU, the graphics card and, above all, the memory) and in a small addition to the power bill. A developer blog responding to Build put it neatly: "unmetered" describes the billing model, not the cost. The inference you used to rent by the call, you now own, in advance, in hardware. For anyone who manages a fleet, the AI line item quietly stops being an API budget and becomes part of the refresh budget.

To give a sense of scale, a preprint from January (Knoop and Holtmann, not yet peer reviewed) put the electricity-only cost of running models on consumer graphics cards at somewhere between a tenth of a cent and four cents per million tokens. That was measured on desktop-class cards in a small-business server setting, not on a laptop's NPU, so take it as an order of magnitude rather than a laptop price. The order of magnitude is the point.

Now, the counterweight, and it is a serious one. The one input local AI needs most is memory, and memory is the one thing the PC market cannot get cheaply right now. IDC in June forecast 2026 PC shipments down 11.3%, driven by a shortage of DRAM and storage, and said "We're not seeing any relief to the memory shortage situation before the end of 2027." So the model moves onto the desk at exactly the moment the desk is getting more expensive to fill. That does not kill the story. It does mean the organizations that get the most out of it are the ones that were already buying modern machines with room to spare, and it means "free per call" arrives with a hardware bill that finance will notice long before it notices the missing API invoice.

One more thing worth noting while the numbers are in front of us: when a call costs nothing, nothing on an invoice tells you how many times it was made. That is mostly good news. Sunday comes back to the rest of it.

## What gets built when you can assume it

Think about what a developer building a Windows application has had to do, until now, to put even a modest bit of language intelligence into it: summarize this document, rewrite this paragraph more politely, pull the action items out of this email, sort these support tickets. They needed an account with a model vendor, an API key, a billing arrangement, a network connection, a privacy review of where the text was going, and a plan for what the app does when the connection drops. Every one of those is a reason a small feature never gets built. None of them is a technical reason. They are all friction.

An in-box model removes most of that list at once. No key, no per-call bill, no permission slip, no network round trip, and the text stays on the machine it was typed on. For the kind of small, useful, unglamorous task a compact model handles well (summarizing, classifying, rewriting, extracting), the developer can now just call it, the way an app developer in 2009 could just ask the phone where it was.

That is not a frontier model and it is not pretending to be one. Microsoft's own framing is hybrid: local for the small and routine, the cloud for the hard and the large. A bigger on-device sibling, Aion 1.0 Plan, was announced at Build as a model aimed at agent planning, due "on capable Windows devices in coming months," with no date. I would not build a roadmap on that one until it has a month attached.

And the same move is happening in the other pocket. Qualcomm's new top-tier phone chip, the Snapdragon 8 Elite Extreme Gen 6, unveiled at its Snapdragon Summit last week, is reported to run mixture-of-experts models of 30 billion parameters and up entirely offline (the trick is that only a small slice of the model does the work for any given word, which is what lets it fit), with the first handsets reported for this quarter. The desk and the pocket are getting the same capability from opposite directions, on roughly the same calendar.

<!-- [YOUR TAKE]: one concrete thing you would build, or have wanted to build, if you could assume a model on every modern machine you ship to -- the small feature that never cleared the "API key, billing, privacy review" bar. Your own example will carry this section better than a generic one. -->

## The one caution worth carrying in

This part is short, but it is not nothing.

Microsoft is admirably direct about the risk on the agent side. Its experimental agentic features in Windows are off by default and can only be switched on by an administrator, and its own support page names the problem plainly: "malicious content embedded in UI elements or documents can override agent instructions, leading to unintended actions like data exfiltration or malware installation." And the MXC repository says, in so many words, that "no MXC profiles should be treated as security boundaries currently." That is an early-preview project being honest about being early, which I appreciate, and it is also a sentence to read before anybody in your organization describes it as a sandbox.

A small model summarizing a document is one thing. An agent on the same machine that can act on what it reads is another, and the second one is still being built.

## Getting ready for November

**Count the machines that qualify.** Find out how many of your Windows devices have an NPU of the right class or a recent enough graphics card. That one number tells you whether the in-box model is a pilot or a platform for you this year, and it is a much easier number to get now than after somebody asks for it in a meeting.

**Try it on one boring job in October.** The standalone package lands early in the month, and Foundry Local already runs today. Pick something dull that currently goes to a cloud API or does not get done at all (meeting-note cleanup, ticket triage, a first pass on document summaries) and run it locally. Dull is the right test, because dull is what a small model is good at.

**Put the refresh and the memory in the same conversation.** If local AI is part of the case for the next hardware refresh, spec the memory for it now, while you are still deciding, rather than discovering in eighteen months that the machines you bought can run the model and nothing else alongside it.

**Ask your software vendors a new question.** Will their Windows products use the in-box model when it arrives? If the answer is yes, some text that currently leaves your machines to be processed somewhere else stops leaving, and some per-seat AI add-on pricing starts to look harder to justify. Both are worth knowing before renewal.

**Read the agent settings before anyone turns them on.** The model is the easy part. Whoever enables the experimental agentic features is enabling them for every user on that machine, and Microsoft has told you in writing what the risk is.

## Along for the ride

I doubt many people bought an iPhone 3G for the GPS chip. They bought it because it was the new phone, and the chip came along for the ride, and a couple of years later half the apps on their home screen depended on it without anyone ever deciding that they should.

The model arriving in Windows this autumn is the same kind of thing. It is small, it is modest, it runs on modern machines rather than every machine, and it will be free to call. The people who get the most out of it will not be the ones who waited for a keynote to tell them what it was for. They will be the ones who had a boring job ready for it the week it showed up.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that when Windows starts shipping a language model in the box this autumn, the growth in AI moves from the frontier labs' servers to the modern machine already on the desk, the cost of each answer moves from a per-call bill into the hardware you already bought, and the organizations that benefit most will be the ones that have a small, dull job ready for it.*

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
