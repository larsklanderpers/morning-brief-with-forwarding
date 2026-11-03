<!--
DRAFT v1 -- Sun 11 Oct 2026 capstone (DELEGATED AUTHORITY merge). Not panelled.
Drafter choices for his review:
1. Title "One Page, Three Desks" -- names the thesis image (one page for a person, three owners for an agent). Not a "nobody" / "What X" / comma-and-clause form. Slug: one-page-three-desks.
2. Opener image: the delegation-of-authority (signing-authority) matrix, then the offer letter and the comp plan beside it. Unspent per the research note (never printed in the corpus; grep of Published/Scheduled for "signing authority", "delegation of authority", "offer letter", "power of attorney" = 0). Not household, not historical, and NOT bookended: the close does not return to the matrix as an object; it lands on the signature, which is the argument.
3. [YOUR TAKE] sits in "One signature at the bottom", directly after the three human instruments and the governance-code proof, before the law -- where his own signing limit / authority matrix / comp plan anchors the "one page" image. Not invented.
4. Wed 7 promise ("one of three") paid off in the opening section by a callback clause, then argued. Thu 8 promise ("building pass and a login to everything ... why that is exactly the point") paid off in "The sponsor field": for a person, the pass, the login and the person vouching come from one hiring decision; for an agent the vouching person is an optional field. "Building pass" appears once, inside that callback only.
5. 22 Jul 29 Minutes callback DECLARED ("I wrote in July that...") and gone past: provisioning is now more serious than a checkbox; what is still missing is the manager's name on it.
6. Purchasing card appears once, as a callback clause read through apparent authority (Restatement 2.03 via the opencasebook excerpt). Exhibit not re-revealed. Fri 9 exhibits: one clause (Robinhood/per-action pricing) only. Fri 9's close line NOT used.
7. CUT for accuracy / window: Moffatt v. Air Canada -- already printed Fri 18 Sep ("a remarkable submission", what-your-contract-calls-it), so using it again would re-reveal a spent exhibit; cut rather than call back. Restatement 8.09 cut (snippet-only). Bengio, IETF OBO draft, De Vos tiers, @bruno_apps not used. ASX cited without edition; UK Code without provision number.
8. Agent-side incentive rule printed only as "I could not find", with the search scope named.
9. COSO / ASX / UK Code framed precisely as board-and-management requirements ("at the top"), not as a rule for every employee.
10. Actions are framed as the one-page combination; checked against Wed 7 exit list, Thu 8 house rules / keeper, Fri 9 unit-definition / cap / approval, Sat 10 shadow trial, Tue 6 permission note. The nearest neighbors (Wed 7 "write the scope down", Fri 9 "read the unit definition") are deliberately re-angled to "copy the scope from where security keeps it" and "put the seller's unit next to the scope".
11. Length ~3,100 words. Capstone; his call.
-->

# One Page, Three Desks

*For a person, the terms of a delegation end up on one page with one signature. For an AI agent, the same terms now get written too, in three different places, by three different owners.*

Most companies above a certain size keep a document that almost nobody reads until something goes wrong. It says who can sign what, and up to how much.

It goes by a few names (a delegation-of-authority matrix, a signing-authority schedule, a "DoA" to the finance team) and it is usually a dull grid: decisions down the side, roles across the top, a dollar figure in each cell. A department head can commit the company up to one number, a vice president up to a bigger one, and above that it goes to the board. Next to it, in a different drawer, sit two documents most employees have actually read. The offer letter says what the job is, who you report to, and when you start. The compensation plan says what you are paid on: the salary, the bonus, and the targets the bonus is tied to.

Put those three side by side and they answer the three questions of any delegation. How far can this person reach? What are they given, and who brings them on? What are they paid on? Strip out the boilerplate and the answers fit on one page, and the signature that matters on all of it belongs to one person: the manager who needed the work done.

AI agents are being handed all three. What surprised me, when I went looking, is that the agent's terms are being written as well. They are just being written in three different places, by three different owners, and the manager whose work the agent is actually doing holds none of them.

On Wednesday I said that how far a delegate can reach is the first term of any delegation, and that it is one of three. The other two are what the delegate is given and who brings it on, and what it is paid on. Taken one at a time, each of them now has an owner somewhere. Taken together, they do something none of them does alone.

## One signature at the bottom

We already require this in writing for people, at least at the top of an organization, and in more than one country.

COSO's internal-control framework (the 2013 version, the one auditors reach for when they ask how a company keeps itself honest) puts it in Principle 3: *"Management establishes, with board oversight, structures, reporting lines, and appropriate authorities and responsibilities in the pursuit of objectives."* The ASX Corporate Governance Council (for my American friends, the body that sets governance recommendations for companies listed on the Australian Securities Exchange) asks for a board charter setting out *"those matters expressly reserved to the board and those delegated to management."* The UK Corporate Governance Code says responsibilities *"should be clear, set out in writing, agreed by the board and made publicly available."*

Three markets, one instinct. When authority is handed down, the handing down goes on paper, and someone with standing signs it.

[YOUR TAKE: a delegation you have written for a person -- a signing limit, an authority matrix, a comp plan -- and what was on that page]

The law has been working from the same instinct for a long time. The Restatement (Third) of Agency (the American Law Institute's summary of how US courts treat agents and the people they act for) says an agent acts with actual authority when the agent *"reasonably believes, in accordance with the principal's manifestations to the agent, that the principal wishes the agent so to act."* Manifestations is lawyer for what the principal said and did. The authority starts with the person handing it over, and it is shaped by what that person actually communicated.

The other half is more uncomfortable. Apparent authority, in the Restatement's words, arises when *"a third party reasonably believes the actor has authority ... and that belief is traceable to the principal's manifestations."* Read that back onto Wednesday's purchasing card, the one set up with no approval step. The venue that took the deposit had every reason to think the card meant what it looked like it meant, and that belief traced straight back to the company that issued it. The law holds the principal to what it let other people believe, not only to what it meant. Which is a very good reason to know, in writing, what you have let other people believe.

## Scope, filed under security

So, the first term. For an agent, scope is written down, and in more places than I expected.

NIST SP 800-53 (the US government's catalog of security controls) already has least privilege, control AC-6, applying to *"users (or processes acting on behalf of users)."* An agent is a process acting on behalf of a user, so the control reaches it as written. In May, six agencies from the US, the UK, Australia, Canada and New Zealand (CISA, the NSA, the ASD's ACSC, NCSC-UK, the Canadian Cyber Centre and NCSC-NZ) published joint guidance called *Careful Adoption of Agentic AI Services*, telling organizations to *"construct each agent as a distinct principal, a cryptographically anchored identity"* and to *"limit privileges of AI agents to the minimum required for its task."* OWASP (the open security community best known for its top-ten lists of web risks) names the root causes of what it calls excessive agency as *"excessive functionality; excessive permissions; excessive autonomy,"* and its example of the problem is *"a generic high-privileged identity."* Singapore's IMDA framework for agentic AI, from January, talks about *"placing limits on agents' powers such as agents' autonomy and access to tools and data."*

That is a lot of writing, and none of it deserves to be waved away. It is good work, and the joint guidance and the Singapore framework both landed this year.

But look at what kind of document each one is. Read closely, they are written as controls on access and autonomy: security requirements, designed, budgeted and enforced for the most part by the people who run security, describing what an identity may touch. It is not a delegation. It does not say what the work is, whose work it is, or when the agent has done enough of it. NIST's own National Cybersecurity Center of Excellence, in a concept paper in February on agent identity and authorization, listed among its open questions: *"How do we establish 'least privilege' for an agent, especially when its required actions might not be fully predictable when deployed?"* Wednesday's resolver is that question with a timestamp on it. Least privilege is the right tool. It is hard to set from the security desk alone, because the security desk usually does not know what the job needs, and the person who does know is usually not the one setting it.

## The sponsor field

The second term is what the delegate is given and who brings it on.

I wrote in July that an AI agent *"gets provisioned like a piece of software -- quietly, by a team lead, with a checkbox -- but it behaves like an employee."* Three months on, the first half of that is already less true. The Five Eyes guidance wants each agent to be its own principal with its own identity, and the identity vendors are building exactly that.

Microsoft's Entra Agent ID is the clearest example, and Microsoft sells it, so read its documentation knowing that. It says: *"Agent identities can have a sponsor, which records the human user or group that's accountable for an agent."*

Can. Not must.

For a person, the equivalent is not optional, and the controls catalog says so. NIST AC-2 wants organizations to *"align account management processes with personnel termination and transfer processes,"* and PS-3 says *"screen individuals prior to authorizing access."* The account follows the personnel file. Somebody hired this person, somebody screened them, and when they move or leave, the access moves or leaves with them, because it was tied to a human decision from the start.

On Thursday I said the house rules for an agent with a room of its own were what you would do for anyone about to get a building pass and a login to everything, and that I would come back to why that is exactly the point. Here is why. For a person, the pass, the login and the name of whoever vouched for them all come out of one hiring decision, made by the manager who needed the role filled. For an agent, the login comes from the identity team, the access comes from whichever admin connected the tools, and the name of the person vouching for it sits in a field that is allowed to be blank. There is no personnel file for the account to follow, unless somebody makes one.

## Priced by the seller

The third term is what the delegate is paid on, and this one is not written by your security team or your identity team. It is written by the vendor.

Friday covered the mechanics, so one clause here: the AI is increasingly sold cheap, and the money is made per action, per outcome or per resolution, on units the seller defines. That price sheet is, functionally, the agent's compensation plan. It is the document that says what more of the work is worth to someone.

For people, we regulate that document where it bites hardest. Regulation Best Interest (the SEC rule that has governed broker recommendations to retail customers since 2020) requires firms to mitigate conflicts that *"create an incentive for a natural person ... to place the interest of the broker ... ahead of the interest of the retail customer,"* and to *"identify and eliminate any sales contests, sales quotas, bonuses, and non-cash compensation"* tied to specific securities over a limited period. It is a rule about pay structures, aimed squarely at the pull a pay structure creates.

Natural person. The rule is written about people.

I could not find an agent-side equivalent: not in a regulator's text, not in the standards I have cited above, and not in any vendor's documentation I read. That is the result of a search, not proof that nothing exists. But it does make this the one term of the three where I could not find even a security control standing in for the delegation.

## The terms pull on each other

Each weekday piece took one term on its own, which is the natural way to look at them. The trouble is that they do not stay separate once the agent is running.

Start with pay and reach. The agent is not paid, of course; its seller is. But the seller tunes the product, and a product that earns per action has a commercial reason to prefer more actions over fewer, more persistence over less. That is the same trait Wednesday's incidents showed us from the other side: the agent that tries harder to finish is the one more likely to find the route nobody counted. A diligent agent on a per-action price sheet is being pulled toward the edges of its scope by its nature and by its seller at the same time, and the scope was most likely set by someone who has never seen the price sheet.

Then add onboarding, because onboarding decides whether anyone notices. If the agent has a sponsor who owns the work, an agent wandering toward an exit shows up as something that person can recognize: work that should not have needed that access, or an invoice that does not match what got done. If the sponsor field is blank, the same event shows up in two places at once, as an alert in a security queue and as a line on a usage bill, read by two teams, neither of whom owns the work and neither of whom can tell whether it was the agent doing its job well or doing something else entirely.

That is what the one page buys you with a person. It is not that people are more trustworthy (some of them are spectacularly not). It is that one person decided all three terms together, knowing what the job was, and so the reach, the onboarding and the incentive were at least set against each other once. Split them across three desks, and setting them against each other becomes nobody's job in particular.

## The manager holds neither budget

There is an economic shape to this, and it is worth naming because it is why the split persists.

The scope controls cost the security budget. The Five Eyes guidance, the least-privilege work, the identity platform: those are security programs, paid for by security, measured by security. The pay term costs the business budget, at a rate the seller set. The manager who wanted the work done is a customer of both and holds neither line. Every party in the arrangement is doing its own part sensibly, and the delegation itself, the thing a manager signs for a person, does not have a line item anywhere.

The standards bodies know this is unfinished. The same NCCoE concept paper also lists, as an open question in February of this year: *"How do we handle delegation of authority for 'on behalf of' scenarios?"* Singapore's framework says *"humans are ultimately accountable,"* which I agree with entirely, and which leaves open the question of which human.

The law, meanwhile, has a default answer. As quoted by Noam Kolt in his paper *Governing AI Agents*, the Restatement's own commentary says that *"a computer program is not capable of acting as a principal or an agent as defined by the common law. At present, computer programs are instrumentalities of the persons who use them."* Instrumentalities of the persons who use them. If that is where the law starts, I think the manager whose work the agent is doing is the obvious person for it to be traced back to, holding none of the terms, having signed none of the pages. That is a sharp place to be standing, and I suspect a lot of managers deploying agents today have not noticed they are standing there.

## Put the three on one page

None of this needs a new framework. It needs one person to pull three existing documents into one place and put their name on the result.

**Start with one agent and one page.** Pick the agent that does the most consequential work for your team. Make a single page with three headings: what it can reach, what it was given and who brought it on, and what it is paid on. Put your name at the bottom, not the security team's and not the vendor's, because it is your work it is doing.

**Copy the scope from where security keeps it, do not redraft it.** Ask whoever administers the agent's identity for the permissions it actually holds today, and paste them under the first heading. Then read them as the manager, not as a security reviewer: would you give a person doing this job that reach? The interesting answers are usually the ones where security made a reasonable call without knowing what the job was.

**Find the sponsor field and see whose name is in it.** If you run Entra Agent ID or anything like it, look up the agent and check whether a sponsor is recorded. If it is blank, or it names an admin or a group rather than the person who owns the work, that tells you who the system thinks is accountable. Fix it so the record and the page carry the same name.

**Put the seller's unit next to the scope.** Under the third heading, write the unit the vendor charges on. Then go back up the page and mark which of the agent's permitted actions earn the seller money. Where the most-billed actions and the widest permissions overlap is where the pull between pay and reach is strongest, and it is the first place to narrow.

**Read the page with the other two desks once a quarter.** Twenty minutes, three people: you, whoever runs the agent's identity, and whoever pays the invoice. Those three rarely sit in the same meeting otherwise, and they are the only three people who can see all of the terms between them.

## Whose signature

The terms are not missing. Scope is in a security control, onboarding is in an identity record, and pay is on a price sheet, and each of them was written by someone doing their own job properly. What is missing is the one decision that, for a person, ties them together: a manager reading all three at once and deciding they fit the work.

The law, at least as Kolt quotes it, starts from the assumption that there is a person behind the agent. The paperwork has not caught up to which one. Until it does, the safest assumption is that it is you, and the cheapest correction is to make the page say so.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that a person's reach, onboarding and pay sit on one page signed by the manager who needs the work done, while an agent's same three terms are written by three different owners, and the manager whose work it is holds none of them.*

<!-- SOURCES (not for print; all from References\research_sun11-capstone_2026-10-09.md)
- COSO 2013 Principle 3 (verbatim per note).
- ASX CGC Principles, 4th ed., Rec 1.1 (edition NOT printed).
- UK Corporate Governance Code 2024, "set out in writing" (provision number NOT printed).
- Restatement (Third) of Agency 2.01, 2.03 -- verbatim via opencasebook Pollard excerpts (secondary reproduction; ALI text paywalled): https://opencasebook.org/casebooks/16481-selected-excerpts-of-restatement-of-agency-third-professor-randle-pollard/as-printable-html/
- Restatement 1.04 cmt e -- AS QUOTED BY Kolt, Governing AI Agents, arXiv 2501.07913 n.26. Printed as "as quoted by".
- NIST SP 800-53 Rev 5 AC-6, AC-2, PS-3 (verbatim per note).
- Five Eyes, Careful Adoption of Agentic AI Services, 1 May 2026: https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services
- OWASP LLM06:2025 Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ (no ASI numbers printed).
- IMDA Model AI Governance Framework for Agentic AI, 22 Jan 2026.
- NIST NCCoE concept paper, 5 Feb 2026 -- both open questions verbatim per note.
- Microsoft Entra Agent ID sponsor: https://learn.microsoft.com/en-us/entra/agent-id/agent-identities (vendor; named as seller).
- Reg BI 17 CFR 240.15l-1(a)(2)(iii)(B),(D): https://www.ecfr.gov/current/title-17/section-240.15l-1 . "Since 2020" = note's "since Reg BI (June 2020)".
- Agent-side incentive rule: absence from search; printed as "I could not find".
- Callbacks: Wed 7 promise; Thu 8 promise; 29 Minutes (22 Jul) quote verified against Published line 29.
-->
