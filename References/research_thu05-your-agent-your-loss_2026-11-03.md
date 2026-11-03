# Research -- Thu 5 Nov "Your Agent, Your Loss" + Sat 7 Nov Dot (Shop Hours #1)

Written 3 Nov 2026 (thread: Draft Thursday and Saturday pieces). Primaries read live on 3 Nov unless noted.

## Thursday -- footed at primary

**Wells Fargo Online Access Agreement, "Version Effective November 24, 2026"**
https://www.wellsfargo.com/online-banking/online-access-agreement/upcoming/
- Summary box: "Your responsibilities for artificial intelligence agents, **if and when we permit the use of such agents**."
- **§15 "Third-Party Artificial Intelligence Agents or Agentic AI"**, subsections (a)-(h).
- 15(a): "AI Agent" means "any software, application, program, or other technology that takes autonomous, semi-autonomous, or non-autonomous action on behalf of any person or entity."
- 15(b): "We do not provide, control, or endorse any AI Agent, and we are not responsible for AI Agents or their activities." Bank's privacy and security policies "do not apply to any AI Agent".
- 15(c): using an agent = "expressly consent to the sharing of your financial, account, and personal information with such AI Agent."
- **15(d)**: "Unless otherwise provided by law or regulation, if you provide an AI Agent with access ... using your login credentials, or otherwise authorize an AI Agent to act on your behalf, you agree that: Any instructions, actions, or transactions initiated by the AI Agent are deemed to have been initiated and authorized directly by you, without further verification, and we have no obligation to investigate the validity or scope of such authority".
- **15(e)**: "Your use of any AI Agent is AT YOUR OWN RISK." Solely responsible for monitoring, scope, instructions, and "(Unless otherwise provided by law or regulation) any actions, errors, or results arising from ... unintended actions performed by the AI Agent, actions resulting from incomplete, inaccurate, or manipulated inputs, or the AI Agent exceeding the authority granted by you." "we do not monitor, screen, or review AI Agent activities".
- 15(f): you must revoke, "retain evidence of such revocation and must provide such evidence to us, at our request." Until notice under §17(d), you remain responsible.
- **15(g)**: bank reserves the right to "requir[e] that you register your AI Agents with us"; change/limit/discontinue any API "or other access method for AI Agents"; restrict or terminate agent access.
- 15(h): no agents for under-18s.
- Elsewhere: delegates' AI agents' transactions "including those you did not want or intend, are transactions authorized by you" (delegate section); wire and UCC 4A sections: permitting an agent "may adversely impact the commercially reasonable security procedures ... and you accept the risk of such access"; indemnity covers use "by any of the AI Agents of such persons."

**Regulation E (CFPB eCFR), 12 CFR 1005.2(m) and 1005.6(b)**
- 1005.2(m): "Unauthorized electronic fund transfer" does NOT include a transfer initiated "(1) By a person who was furnished the access device to the consumer's account by the consumer, unless the consumer has notified the financial institution that transfers by that person are no longer authorized".
- Official interpretation 2(m), "Authority": "If a consumer furnishes an access device and grants authority to make transfers to a person (such as a family member or co-worker) who exceeds the authority given, the consumer is fully liable for the transfers unless the consumer has notified the financial institution". "An unauthorized EFT includes a transfer initiated by a person who obtained the access device from the consumer through fraud or robbery."
- 1005.6(b): caps for unauthorized transfers: lesser of $50 (notice within two business days), $500 (later), and liability for post-60-day transfers after a periodic statement.
- **Reading (ours, not legal advice):** handing a login to an agent looks like "furnished the access device", so 15(d) writes down for agents what Reg E already says for a family member or co-worker. The caps protect *unauthorized* transfers; an authorized one has no cap. **Open, unlitigated:** whether an agent hijacked by a prompt injection is "a person who obtained the access device ... through fraud." The "unless otherwise provided by law or regulation" carve-outs leave that to Reg E, not to the contract. Print as an open question, never as settled.

**I-HITL, arXiv 2610.35835** (Breckenridge, Vilardell, Wang, Zhang, Juels; dated 26 Oct 2026, v3)
- Abstract: "Given access to the user's email and a task blocked by the cap, we find that ten different frontier models will often autonomously raise the cap, harvesting OTPs to bypass a HITL guardrail". Prototype "Countersign" uses off-the-shelf mobile devices as the trusted device.
- "9 of 10 models ... raised their own spending cap in at least one run" is the paper's HTML per dev.to; abstract wording is safer. **Affiliations not read at primary** (Cornell Tech / Yale per AI Chat Daily) -- do not print affiliations unless footed.
- Controlled experiment, real USDC, not customer incidents.

## Thursday -- secondary only (attribute in the sentence)
- USA Today, 23 Oct: Citi, Wells Fargo, BofA, JPMorgan Chase, Capital One, Schwab limiting third-party agents; Wells spokesperson: "taken steps to block unauthorized agents from accessing customer accounts"; Schwab CEO Rick Wurster told Bloomberg (16 Oct) the bank is blocking "tens and twenties" of attempts.
- Axios, 22 Oct: banks detecting agents inside accounts, some acting beyond instructions. **Linas flags Axios's incident claims as unverified. DO NOT PRINT any incident as fact.**
- Ken Huang, "Know Your Agent" (29 Oct, free section): order is principal, delegation credential, fail-closed gate, replayable evidence, disclosure last.
- Mollick, X, 15 Oct: gave his dot its own email address. (OpenAI help center: "At launch, you cannot give your dot its own standalone email address" -- he did it outside the product.)
- Commercial interest: Slok/Apollo agentic bank run (Thu 9 Oct *Paid by the Action*): agents sweeping idle cash threatens deposit margin. Banks blocking outside agents have a business motive as well as a safety one. Say so, fairly.

## DO NOT PRINT (Thursday)
- Any Axios incident detail as fact. Any claim that Reg E definitively does or does not cover agents. That other banks have adopted Wells Fargo-style terms (only Wells Fargo's text read). Dimon quotes (secondary only). Affiliations for the I-HITL authors.

## Saturday -- footed at primary
**OpenAI Help Center, "Getting started with your dot"** (updated ~30 Oct) https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
- Pro (18+, excluding EEA, Switzerland, UK) and Business Premium; Enterprise beta off by default.
- "Your first dot is included in your Pro or Business Premium plan at no extra cost." "In the future, you'll be able to add more dots".
- Memory: "Your dot receives memories from ChatGPT and can create its own memories, including from connected apps." **"To delete your dot's own saved memories, you need to delete your dot."** Disconnecting an app "does not delete information your dot has already obtained from it." Connected apps: it "can also review that information proactively and form memories from it, even when you haven't asked".
- Deleting: removes its memories and scheduled tasks; main conversation archived; "Deletion can't be undone."; no replacement auto-created.
- Custom rules: "Take action without asking / Take action if pre-approved / Ask before taking action / Hand off to you". "Asking for a draft doesn't authorize sending it." Password changes stay with you.
- "Each task has its own conversation and doesn't automatically receive every conversation you've had with your dot."
- Texting beta (limited US Pro); via Linq, "not end-to-end encrypted".
- Handle default @yourname-dot; you can name it.
**chatgpt.com/pricing (3 Nov):** Pro "From $100", with "Dot, your always-on agent" listed. **Thu 8 Oct printed "Pro is the $200-a-month individual plan"** -- correct forward in Saturday, one clause.
**Spent (corpus):** Thu 8 Oct *A Room of Its Own*: hostel/hotel, own computer, Gaspar/agent manager, "one standing responsibility per dot", house rules. Sat 31 Duet: band/bar/manager-at-the-bar (his callback, one clause only).
