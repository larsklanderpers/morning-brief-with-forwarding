# The Kill Switch You Didn't Know About

Your AI stack has a kill switch. It's in Washington. And nobody knows what triggers it.

On Friday June 12, engineers at Anthropic received a letter from the US Commerce Department's Bureau of Industry and Security. By the time Australian businesses started work on Monday morning, Fable 5 and Mythos 5 — Anthropic's most powerful models — were dark globally. Not just for foreign nationals. For everyone. Including Anthropic's own staff.

That's how a regulatory enforcement action works when the regulator has no published rules.

---

## You're Already Regulated. Nobody Told You the Rules.

The conventional wisdom in enterprise AI right now is that we're in a pre-regulatory moment — that governments are still figuring out how to govern frontier AI, and that formal rules are 12 to 18 months away. That's wrong in two ways: the rules are here now, not 18 months away; and the rules are not formal, and at the moment, the US government has indicated they have no intention of making them formal. 

Dean Ball, who briefly served as the Trump administration's White House AI advisor before becoming OpenAI's head of strategic futures, put it bluntly: *"AI is licensed now, but the requirements change constantly and are always a secret, even to the administration itself, which will discover the rules spontaneously in real time as it reacts to events."*

Read that again.

The rules are secret even to the people writing them. That's not a policy gap. That's a policy.

The Commerce Department didn't invoke a new AI law when it pulled Fable and Mythos. It used the Export Administration Regulations — rules written for physical goods, weapons, and semiconductors — and applied them to a software model. No formal statute. No notice period. No published threshold for what would trigger action. Just a letter threatening criminal and civil penalties, sent on a Friday.

The pulling of Fable and Mythos has been explored ad nauseum on the interwebs. I don't particularly have a strong opinion either way -- if they are risky, I think they should be made less risky, but less risky for *everyone*, not just the normies. I am not sure that even for advanced users, an extra month for everyone to determine the protections of the model is a big deal. The pragmatic arguments around this kind of move are very sound, and in fact are the kind of responsible government (if applied appropriately) that we wish we could expect from politicians all the time. I haven't really heard anyone -- aside from certain cybersecurity experts, for reasons that have to do with defender advantage calculation -- complain that pulling the models was a bad idea. In fact, for a couple of months prior to their release, many people outside the bubble of AI felt like releasing such advanced models so fast was actually a really *bad* idea. It's not the pull that's the problem: it's the methodology (or lack thereof) behind it. And that methodology is not just a problem for Americans -- it is a problem for every entity with exposure to US frontier models, in the *world*. Which is, needless to say, a lot of people and companies.

---

## Then It Happened Again

Three weeks later, OpenAI announced GPT-5.6 — three models named Sol, Terra, and Luna that represent their most capable release yet. Sol, the flagship, is their most powerful coding and cybersecurity model to date.

Access is restricted to approximately 20 companies. Those companies were approved by the US government. Everyone else waits.

Sam Altman said the current approach — approving customers one by one during a "preview period" — was *"not our preferred long term model."* OpenAI's statement says it was acting at the US government's request, driven by the same cyber-risk concerns that grounded Fable.

Jeremy Kahn at Fortune, writing shortly after the Fable ban, described what's actually happening: *"The export controls, the partner gates, the framework agreements, the daily talks between Anthropic and Commerce — these are now the standing regulatory regime for frontier AI in the United States."*

The US has a mandatory licensing regime for frontier AI. It just doesn't have one that anyone wrote down.

---

## Mythos Came Back. Read the Fine Print.

On June 26, Commerce Secretary Howard Lutnick sent Anthropic a second letter. Mythos 5 is back — for roughly 100 approved companies and federal agencies. He "determined that appropriate safeguards are in place to permit certain trusted partners to access the Claude Mythos 5 Model."

At first glance that looks like a resolution. It's the opposite.

Lutnick's letter explicitly reserves "the right to reevaluate and adjust the scope of license requirements on the Covered Models, should circumstances change." He can also change the list of approved entities "at any time." The criteria for becoming a "trusted partner" have not been published. Fable 5 remains suspended. And Anthropic must "work with the US government on protocols and standards and releases for the Covered Models" — ongoing compliance with a framework that, again, doesn't exist in any written form.

So: if you weren't already on the list of 100 approved companies when Lutnick signed that letter, you don't have Mythos. If Commerce changes its mind about the criteria tomorrow, anyone on the list could be off it. Fable — which was actually the more widely deployed model — is still dark with no published path to reinstatement.

The kill switch didn't get removed. It got put on a dimmer. Commerce is holding the dial.

Bruno Retailleau, a French presidential candidate who was previously interior minister, put it plainly when the original ban landed: *"A nation that depends on others for its technology is a nation that can be unplugged overnight."* The reinstatement doesn't change that. It proves it.

---

## Why This Is an Australian Problem

You might be thinking: this is an American political fight. Australia will sort out its own approach through the Privacy Act review, the OAIC, maybe a sector-specific framework for regulated entities. That's true. But it doesn't protect you from the kill switch.

If you're running frontier AI workloads — Fable, Mythos, GPT-5.6, or any of the other US-headquartered frontier models — your business continuity depends on a regulatory conversation happening between Silicon Valley and Washington that you have no seat at. You're not a "trusted partner" in Lutnick's letter. You're not in the room when Commerce decides who gets access and who doesn't.

This is precisely the risk APRA flagged in April. Its letter to regulated entities explicitly named "offshore frontier AI concentration risk" as an observed governance failure. CPS 230 went live on 1 July. The Fable ban is the closest thing to a live case study APRA could have asked for: a single Friday-night enforcement action that removed global access to an enterprise AI tool without warning — and two weeks later, a partial reinstatement with terms that can be revoked at any time.

**The operational question isn't philosophical.** If your AI-assisted compliance workflow, your fraud detection stack, or your customer service tooling runs on a US frontier model, what's your continuity plan if it goes dark this weekend?

Neither my company nor any of our customers run any workloads on Fable. There are a lot of reasons for that, most of which have to do with data sovereignty and inference sovereignty and the upcoming legal regime in Australia; but we wouldn't have done it for any of our customers, any where, because the institutional risk outweighed any conceivable benefit at this point. There are a host of reasons to keep your company away from frontier models -- and you should listen to them. Carefully. And if your people are telling you that the pending regulatory changes already signed into law won't affect you, you should be pushing back on that claim very heavily.

---

## The Real Problem Isn't the Ban. It's the Opacity.

Charlie Bullock, at the UK Institute for Law and AI, framed this better than anyone when the Fable ban broke: *"This ad hoc last-minute licensing regime is bad for companies, the administration, and the public — we desperately need to replace it with actual legislation."*

Jonathan Iwry at the Wharton Accountable AI Lab describes what's happened as "the government repurposing existing legal authorities into what is effectively a backdoor licensing regime."

The problem isn't that the US government is regulating AI. A credible argument exists that it should. Dario Amodei himself — whose company explicitly called for an FDA-like approval process for AI models — is on record saying he wants *"a statutory process that is transparent, fair, clear, and grounded in technical facts."*

He wants the thing the current approach is the opposite of.

Amodei published a blog post on June 10 calling for "mandatory testing by a qualified third party" of model risks. Two days later his company received a Commerce letter pulling his models. The administration used Anthropic's own risk framing as justification for its enforcement action — then ran the process in exactly the way Amodei said it shouldn't be run.

Take it out of the AI space for a minute. Consider if a gaming inspector could get together with everyone around the office and suddenly decide that EGMs more than 1.5m tall were no longer allowed. And they made the decision on a Friday afternoon at 5:25 pm and decided enforcement was immediate. Your entire floor, feasibly, could be shut down indefinitely without recourse or standing. This is the risk of the ad hoc regime -- no matter how much we might chafe at the rules that regulators impose on us as vendors and operators, *we still know what they are*. We still know how to comply. There is a path, no matter how twisted or rocky, that we can navigate, to ensure we stay on the right side of the regulations. I don't think I need to express what that would mean in our day to day.

---

## What You Should Do Right Now

This isn't a "wait and see" situation. It's a "your board already needs to know about this" situation.

**Map your frontier AI dependencies.** Which of your business-critical workflows touch US-headquartered frontier models? What would happen if acces