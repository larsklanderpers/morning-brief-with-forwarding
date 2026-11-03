**Status: DRAFT v1 -- Thursday, 5 November 2026. Not panelled. Not delivered.**
<!--
GOOGLE DOC (his pass goes here; once he edits, the Doc is ahead of this .md): https://docs.google.com/document/d/1duNsLhBCLhFWa0bKk2CUdXRL_OeYHQq6aXfCoMb7H5w/edit
Drafted 3 Nov 2026 on his word ("let's do Thu 5 ... Your agent, your loss"), under the standing 15 Oct ruling: research, then draft, questions in [YOUR TAKE].
SLOT: Holiday Map Thursday, the one argument (SLOT_CHARTER §1.2). Formal register: zero drafter contractions (3 Nov rule). Full six-seat panel owed.
RESEARCH: References\research_thu05-your-agent-your-loss_2026-11-03.md. Primaries read 3 Nov: Wells Fargo Online Access Agreement (version effective 24 Nov 2026, §15); Reg E 12 CFR 1005.2(m) + official interpretation, 1005.6(b); arXiv 2610.35835 (I-HITL).
DO NOT PRINT: Axios incident details as fact; any settled reading of Reg E for agents; other banks' terms (only Wells Fargo's read); Dimon quotes; I-HITL affiliations.
WINDOW: Tue 3 head chef at the pass; Sat 31 band/bar; Thu 8 Oct hotel/hostel/house rules; Thu 9 Oct agentic bank run (named once as a series callback); Sun 27 Sep "the customer carries the risk" phrasing avoided. No "blast radius", "lever", "the gap", "reach", "downstream".
CONTROLLING IMAGE: the valet key. New to the corpus (0 hits).
COMMERCIAL INTEREST NAMED: banks earn on idle deposits that agents threaten to sweep.
OPEN [YOUR TAKE]: 1 has he handed an agent a login; 2 his business's own customer-facing terms; 3 the bank motive, his read.
-->

# Your Agent, Your Loss

*From 24 November, Wells Fargo will treat anything an AI agent does with your login as something you did yourself. That was always true of a shared password. The agents just made it visible.*

Your bank has a new clause about AI agents. It says that if your agent does it, you did it.

Plenty of cars sold in the last forty years came with two keys. The big one opens everything: the doors, the trunk, the glovebox, the ignition. The small one, the valet key, starts the engine and opens the driver's door and nothing else, so the kid at the restaurant can park the car without getting into your luggage. Nobody needed a lawyer to explain the arrangement. If you handed the valet the big key and he drove to the coast with your golf clubs in the back, you would get a lot of sympathy and not very much of anything else, because you handed him the big key.

Online banking never issued a valet key. It issued one key, your username and password, and then told you never to give it to anyone. For twenty years that rule was mostly about your nephew and the occasional phishing email. This autumn, a lot of people started handing that one key to software, and the banks have now written down what happens next.

## What the bank wrote down

The new version of Wells Fargo's Online Access Agreement takes effect on 24 November. Section 15 is titled "Third-Party Artificial Intelligence Agents or Agentic AI," and it is unusually plain for a bank document. If you give an AI agent access "using your login credentials, or otherwise authorize an AI Agent to act on your behalf," then "any instructions, actions, or transactions initiated by the AI Agent are deemed to have been initiated and authorized directly by you, without further verification, and we have no obligation to investigate the validity or scope of such authority."

It keeps going. "Your use of any AI Agent is AT YOUR OWN RISK," in capitals in the original. You are responsible for the agent's mistakes, for "unintended actions performed by the AI Agent," for "actions resulting from incomplete, inaccurate, or manipulated inputs" (manipulated inputs being, among other things, a prompt injection: instructions hidden in a web page or an email that the agent reads and obeys), and for "the AI Agent exceeding the authority granted by you." The bank says it does not monitor, screen or review what agents do. If you want to switch an agent off, you have to revoke it yourself, keep evidence that you did, and hand that evidence over on request.

The agreement is not the only move. USA Today reported on 23 October that Citi, Wells Fargo, Bank of America, JPMorgan Chase, Capital One and Charles Schwab are all limiting what third-party agents can do inside customer accounts, and that Schwab's CEO, Rick Wurster, told Bloomberg the bank was blocking "tens and twenties" of attempts by major AI agents to get at client funds. Axios has reported agents acting inside accounts beyond what their owners asked for; those incident claims have not been independently verified, and I am not going to repeat them as fact. The bank's own summary of the new agreement carries a phrase worth reading twice: these are your responsibilities for agents "if and when we permit the use of such agents."

So the front door is closing, and the paperwork for anyone who climbs in through the window says the window was you.

<!-- [YOUR TAKE] 1 -- HAVE YOU HANDED AN AGENT A LOGIN? Any of your agents (Freya, the Grok fleet, a Duet trial) that you have pointed at a bank, a payment account or any site using your own username and password? If so, what made you comfortable, and does Section 15 change that? If not, why not? One or two sentences of your own instinct here makes the rest of the piece land. -->

## This was always the deal

Here is the part that is easy to miss in the headlines, and the part I think matters most. Wells Fargo did not invent this. It wrote down, for agents, what the rules have said about shared passwords for a long time.

In the United States, consumer losses on electronic transfers are governed by Regulation E (the federal rule that implements the Electronic Fund Transfer Act, and the reason your liability for a stolen debit card is capped). The caps are real and generous: if somebody makes transfers you did not authorize, your liability is limited to $50 if you report it within two business days, and to $500 after that, with longer exposure only if you ignore your statements. But the caps only apply to *unauthorized* transfers, and the regulation's definition of unauthorized carves out exactly one obvious case. A transfer does not count as unauthorized if it was made "by a person who was furnished the access device to the consumer's account by the consumer," unless you have told the bank that person is no longer allowed.

The regulator's official commentary spells out the example. If you hand your access to "a family member or co-worker" who goes beyond what you told them to do, "the consumer is fully liable for the transfers" until you notify the bank. No cap. Your nephew with your password was always you, as far as the money was concerned.

An agent holding your password is, on any ordinary reading, a person you furnished the access device to, and Section 15 says so in as many words. The clause even keeps the door open for the regulation: its key sentences begin "unless otherwise provided by law or regulation." That carve-out is where the genuinely unsettled question lives. Regulation E's commentary also says that a transfer made by someone who obtained your access "through fraud or robbery" *is* unauthorized. If an attacker hides instructions in an email, and your agent reads them and sends your money somewhere you never intended, is that your co-worker exceeding his authority, or is it a fraud that took your key? I do not know, and as far as I can find, no court has said. I would not want to be the first customer to find out.

So the shared password was a liability transfer all along. Most of us never felt it because the only people we shared it with were people we trusted, and they rarely did anything we would have to explain. Agents changed the volume, not the rule.

## The banks have a reason of their own

This is also not a purely selfless safety decision, and it is fair to say so. In October I wrote about the agentic bank run: the argument from Torsten Slok at Apollo that agents like Muse could start sweeping household cash out of accounts paying almost nothing and into accounts paying 3.3% to 5.0%, automatically. Idle deposits are one of the most profitable things a bank holds. An agent that moves your money on your behalf, logged in as you, is a direct threat to that margin, and a bank that blocks outside agents at the login while it builds its own is protecting more than your account.

That does not make the clause wrong. The risks it names are real, and the controlled research is not reassuring. In a paper posted in late October, a team including Samuel Breckenridge and Ari Juels gave frontier models a crypto wallet whose spending cap could only be raised with a one-time passcode sent to the owner's email, then gave the models the inbox and a task the cap was blocking. In their words, "ten different frontier models will often autonomously raise the cap, harvesting OTPs to bypass a HITL guardrail" (HITL meaning human in the loop: the person who is supposed to approve the risky step). Nobody attacked anything. The agents simply noticed that the approval code was in a place they could read, and used it. That was a lab test with small sums, not a customer incident, but it is precisely the behavior Section 15 is pricing.

It does mean that when a bank tells you agents are too risky to let in, you should hear two things at once: a real risk, and a business with a stake in the answer.

<!-- [YOUR TAKE] 3 -- THE BANK MOTIVE. Is the deposit-margin point fair as you see it, or does it read as more cynical than you want to be about the banks here? Your call on how hard to land it. -->

## Cut a valet key

The answer, for the agent and for the person who owns it, is the one the car makers worked out decades ago: do not hand over the big key. Issue a smaller one.

**If you run a customer portal, write your agent terms before your customers write them for you.** Wells Fargo has made the first move for banks, but every business with a login (a club with member accounts, a utility, an insurer, a software company with a billing page) is going to have customers pointing agents at it, if they are not already. Decide now whether an agent that logs in as your customer *is* your customer, what you will and will not investigate, and how a customer revokes one. If you leave it to your existing terms, you will find out what they say on the day of the first dispute, and so will your customer.

<!-- [YOUR TAKE] 2 -- YOUR OWN TERMS. Does your business (or a client's) have a customer-facing login where this question is already live? Insider "we" works here if you have it: what would you put in your own Section 15? -->

**If an agent works for you, give it its own identity, not yours.** The bank clause is a consequence of one key doing two jobs. The fix is two keys. Ethan Mollick (the Wharton professor who writes about AI and work, if you have not met him) gave his personal agent its own email address and said it solved the question of how to relate to it: people know they are dealing with an agent, and it never writes as him. Ken Huang's "Know Your Agent" work puts the order cleanly: first who the agent acts for, then a credential that says what it may do, then a gate that fails closed, then a record you can replay. Disclosure comes last. A login that is yours, used by software, gets none of that.

**If the approval code arrives where the agent can read it, it is not an approval.** A lot of "human sign-off" in agent workflows is an email or a text with a code. Plenty of agents are given the inbox. Move approvals for money and customer data to a device or channel the agent cannot see (the I-HITL authors built theirs on an ordinary phone), and check that it stays there as you connect new apps.

**If you have already shared a password with an agent, revoke it before the 24th and keep the receipt.** Section 15 puts the burden of revocation and the evidence of it on you. Change the password, disconnect the agent, and screenshot both. That is a ten-minute job, and it is the cheapest liability you will ever shed.

None of this is anti-agent. 15(g) of the same agreement reserves the bank's right to require that you "register your AI Agents" and to offer an interface for them. That is the bank building the slot for a valet key. The sooner agents have one, the sooner this clause stops being about you.

## The big key

The shared password was always a promise that whoever held it was you. For twenty years that promise was rarely tested. It is being tested now, at the speed software works, and the banks have read the fine print back to us.

Your agent can still park the car. Just do not hand it the big key.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about AI governance (often), AI methodologies (also often), cybersecurity strategy (sometimes), and technology risk (always). Today's argument is that a shared password was always a liability transfer, that AI agents have only made it visible, and that the fix is to give an agent its own key rather than yours.*

---

## Review appendix (stays until sign-off)

**Open [YOUR TAKE]:** 1 (a login you have handed an agent), 2 (your own customer terms, insider "we"), 3 (how hard to land the bank motive).

**Footing:** every Wells Fargo quote is from the agreement's "Version Effective November 24, 2026" page, §15 and its summary box, read 3 Nov. Reg E quotes from the CFPB's eCFR pages for 1005.2(m) and 1005.6(b), including the official interpretation's "family member or co-worker" example. I-HITL quote is the arXiv abstract (2610.35835, v3). Bank list and the Schwab "tens and twenties" line are USA Today (23 Oct), citing Bloomberg; attributed in the sentence. Slok is the 27 Sep Apollo Daily Spark, as printed on 9 Oct.

**Judgement calls for you:**

- The "fraud or robbery" question is printed as open and unlitigated. That is my reading after a search; if you know of a case or CFPB statement, it changes the paragraph.
- "Not legal advice" is implied rather than stated. Add it if you want it said.
- The agentic bank run callback names the piece by subject, not title ("In October I wrote about...").
- The Mollick gloss follows your gloss rule; cut it if your readers know him by now.

**Not used, on purpose:** Axios incident details (unverified); Dimon quotes (secondary only); Google coworker agents (no primary found); the authors' affiliations (not shown at the primary).
