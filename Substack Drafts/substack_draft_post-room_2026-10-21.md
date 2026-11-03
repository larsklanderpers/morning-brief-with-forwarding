**Status: DRAFT v1 -- Wednesday, 21 October 2026. Drafted 21 Oct evening, Wed 21 day chat, on his word ("research, then draft"). Not panelled. Not scheduled.**
<!--
DRAFT v1. Cyber spine, OPENS the week-of-19-Oct arc (THE AFTERLIFE OF A HANDOVER -- plan label only, never a header). Feeds Sun 25 with point 2 (rotate everything it ever stored or injected).
RESEARCH: References\research_wed21-post-room_2026-10-21.md. Every fact below is footed at a primary read 21 Oct (US Courts AO notice; S.D. Ill. GO 26-4; E.D.N.Y. update; E.D. Mich. AO 26-18 signed 21 Oct; CISA 16 Oct alert; BeyondTrust BT26-05; Mandiant/GTIG ARMORY CASTLE post).
OPEN [YOUR TAKE]: 2 (a vendor running something you are obliged to do; a key you found still live long after the job).
CONTROLLING IMAGE: the house-sitter (a job and a key). Domestic, not film/TV, not occupation-as-opener. Wed 14's vault and crew avoided; Mandiant's "vault extraction" phrasing deliberately not quoted.
FOR HIS RULING: (1) title -- working title moved off "The Post Room" because "room" is on the carried spent list (Thu 8) and the image changed; "post room" survives once in the body. (2) "twelve days" is true as of 21 Oct; add one if it publishes 22 Oct.
-->
# The House-Sitter's Keys

*A federal court system lost its post for twelve days, and a remote-support tool turned out to be holding the keys to everything it ever fixed. Both bills arrived long after the handover was signed.*

When you go away, the house-sitter gets two things from you. One is a job, and the other is a key.

The job is the part you think about. Bring in the post, feed the cat, water the tomatoes, put the bins out on Tuesday. The key is the part you stop thinking about the moment it leaves your hand, because a key does not do anything on its own; it just sits on somebody's ring, opening your front door whenever anyone holding it decides it should. And here is the thing about both of them. If the house-sitter comes down with the flu, the tomatoes still die and the electricity bill in the letterbox is still yours to pay. And if the house-sitter's keyring gets stolen out of their car, it is not only your door that is open now. It is every door on that ring.

Organizations hand out both, all the time, and mostly for very good reasons. We give a contractor a function to run and the access to run it, and then we go back to our own work, which is exactly what the handover was supposed to buy us. This week is about what those handovers still do after we have stopped thinking of them as ours. Two weeks ago I wrote about how far an agent can get at the moment you give it permission; this is the other end of the timeline, long after the permission was given and forgotten.

Two stories from the last fortnight make the case, and they are the two halves of the house-sitter: the job and the key.

<!-- [YOUR TAKE]: optional, here or after section 1 -- a time a vendor running something you were legally or contractually obliged to do went dark, and what it was like to discover the obligation had never actually left your desk. Gaming floor, a reporting obligation, payroll, anything. Leave blank if nothing fits; do not invent. -->

## Twelve days without the post

If you have never been through a bankruptcy (and I hope you have not), the part nobody tells you about is how much of it runs on mail. A bankruptcy case is a long conversation between a debtor and everyone they owe, and the law is very particular that every one of those creditors gets told, in writing and on time, when the case opens, when the meeting of creditors is, when the deadlines fall and when it ends. Federal bankruptcy courts do not do that mailing themselves. They send it to the Bankruptcy Noticing Center, the BNC, which, in the words of the Administrative Office of the US Courts, "produces and transmits bankruptcy notices for all federal bankruptcy courts around the country." And "BAE Systems operates BNC systems and websites on behalf of the Federal Judiciary."

On 15 October, the Administrative Office said that BAE's systems supporting the BNC had "been impacted by a cybersecurity incident," that all access to the BNC systems and websites was "unavailable at this time," and that the incident "has also halted the BNC's production and distribution of bankruptcy notices for bankruptcy courts." BAE, it said, "is actively investigating this incident and working to restore operations." That notice has not been updated since.

The individual courts are more specific about the timeline. The Southern District of Illinois and the Eastern District of New York both date the disruption to 9 October, which means the post had stopped for six days before the national notice went up. As I write this, on 21 October, that is twelve days, and no court I have read has a restoration date. The Eastern District of New York put it plainly on 16 October: "we do not have an estimated date or time for restoration of services."

A good deal is still not known. Nobody has said how BAE was hit, whether any data was taken, or whether anything other than the BNC was touched. There is no ransomware claim that I can find, and I am not going to give you one. What is on the record is the effect, and the effect is the interesting part.

The court did not get hacked. Its outsourced post room did, and the court still could not send its notices.

So the courts did what you do when the house-sitter is in bed with a fever: they went back to doing the job themselves, or more precisely, they handed it to whoever was standing closest. Southern Illinois told parties on 15 October that they "should not rely on the BNC to transmit notices" and "should themselves provide notification of important or time-sensitive bankruptcy events." Today, the Eastern District of Michigan went further, in a six-page order signed by its chief judge. Debtors must now serve the official notice of their own case and meeting of creditors on everyone entitled to it "within 3 business days of the petition filing." Trustees serve notice of their own final reports. Anyone asking the court for something serves every notice that goes with it, and files a certificate saying they did. Nobody is to assume that a document sent to the BNC was ever delivered, and "no adverse action should be premised on a failure to respond to a notice whose legally sufficient delivery cannot be established." The postage and copying can be charged against the estate.

Two lines in that order are worth reading slowly. The first is that a debtor doing the mailing "does not relieve the Clerk of any nondelegable duty." The court has asked other people to carry the job, and in the same breath reminded everyone that the obligation never left the court. The second is about who actually feels it. Lawyers, trustees and registered filers still get their electronic notices through the court's own filing system, which is fine. The people who normally get their notices on paper (the debtor without a lawyer, the unrepresented creditor) are the ones whose post stopped, and they are the least likely to notice that it had.

That is point one, and it is not new, but it is rarely this visible: **you can hand someone the job, but the obligation stays with you.** Whatever it costs to keep the job running when they go dark is a cost you never priced, because you priced the contract on the days it worked.

## A keyring, not a key

The second story is the key, and it is worse.

Remote-support software is the tool your help desk uses to take over a user's screen, or log into a server, to fix something from wherever they happen to be sitting. To do that job well, it has to be able to get into a great many machines, so it keeps the credentials to get into them, and hands them out on the technician's behalf when a session starts. That is what it is for. It is a key you hand to a stranger on purpose, because the stranger is there to help, and it is not one key. It is the house-sitter's whole ring.

On 15 October BeyondTrust disclosed CVE-2026-102764, an authentication bypass in its Remote Support product (formerly called Bomgar, if that is the name you remember), rated 9.3 out of 10. (This is a different BeyondTrust bug from the one I used last Wednesday to show how fast attackers line up behind a disclosure; that piece was about the order you patch in, and this one is about what the box was holding.) Mandiant and Google Threat Intelligence Group, writing the same day, say a suspected China-linked espionage group they call ARMORY CASTLE was exploiting it as a zero-day "in late August 2026," roughly seven weeks before anyone was told. Mandiant found it during an incident response engagement, which is worth knowing, because incident response is what Mandiant (which is Google) sells, and BeyondTrust's own explainer is published by the company that sells the product. Both are interested parties. Both are also, as far as I can tell, accurate.

What the attackers got is the part to sit with. Mandiant says the foothold "gave them access to every credential the appliance stored or brokered" (brokered meaning handed out to other systems on a technician's behalf), and it watched them try to dump the appliance's own password store using BeyondTrust's own administrative command-line tool. They did not need to break into each server the help desk supports. The help desk's tool already had the keys, and they took the ring.

There is a small irony in the timeline, and it cuts against the easy version of this argument. BeyondTrust says that "as of Oct 9, 2026," the fix had already been applied to every customer on its hosted service. The customers who had handed the whole thing to the vendor were patched six days before the advisory went out. The ones running it themselves had to wait for disclosure and patch by hand, unless they had automatic updates turned on. So this is not a story where handing things to a vendor is simply the mistake; in this case, on this one axis, it was the safer choice.

But patching is not where CISA stops, and that is the point. Its alert of 16 October tells self-hosted customers to patch and then do network and memory forensics, and, if they suspect a compromise, to isolate the appliance, preserve the evidence, hunt through the logs, "Rebuild from a known-good state and apply the BT26-05-RS patch. Then rotate every credential the appliance stored or injected, revoke all active support sessions, and review new multifactor authentication registrations on privileged accounts."

Read the order of that again. The patch is not the last step. Rotation comes after it, because the patch changes the lock on the appliance, and it does nothing at all about the doors the stolen keys open. If ARMORY CASTLE copied the ring in September, the ring still works in October, on whatever those credentials open, until somebody changes each of those locks one at a time.

That is point two: **when the thing you handed over holds keys, fixing the thing does not take the keys back.** And the economics are lopsided in exactly the wrong direction. The patch is an afternoon. The rotation takes as long as it takes to find every system those credentials were ever used on, change each one without breaking whatever depends on it, and convince yourself you did not miss one, and that is a project with a budget, not a change ticket.

<!-- [YOUR TAKE]: optional -- a time you found a credential, a vendor account or a support connection still live years after the job it was created for had ended. How it was found, and how long the clean-up took. Leave blank if nothing fits; do not invent. -->

## What it still opens

Put the two stories side by side and they have the same shape.

In both of them the handover was made a long time ago, by someone who was probably right to make it. Running a national mail operation for every bankruptcy court is not a thing a court clerk should be doing, and a help desk that cannot get into the machines it supports is not much of a help desk. Nobody in either story did something foolish at the moment of the handover. The cost did not arrive then. It arrived at the far end, when the contractor went dark, or when somebody else got hold of what the contractor was carrying, and at that point it turned out the handover had never really finished. The court still owned the duty. The appliance's keys still opened the doors.

I think that is the right way to measure a handover, and it is not how most of us measure them. We price them at the start: what it costs, what the service level says, what the vendor promises about security in the questionnaire. We almost never ask the question that matters at the end, which is: if this one went dark tomorrow, or was quietly compromised two months ago, what would it still be holding open, and how long would it take us to close it?

That is point three: **the exposure is what each handover still opens today, not when it was granted.** Thursday is the other side of that coin, because for some of this work the handover is no longer forced.

## Changing the locks

None of these needs a new tool. What they need is someone deciding, in advance, what happens at the end.

**When does the lock change?** For every tool or contractor that holds credentials on your behalf, decide now what event makes you rotate them: the contract ending, the person leaving, the vendor announcing an incident, the vendor going quiet. Then make rotation the default response to that event rather than a judgement call made in the middle of it. CISA's sequence for BeyondTrust is a good template for the bad day: preserve, hunt, rebuild, patch, and only then rotate, and rotate everything it ever stored or injected, not just the accounts you think were touched.

**Who runs the post if they cannot?** For every obligation you have outsourced (the notices, the filings, the payroll, the regulator's monthly report), know who does it by hand if the contractor is dark for two weeks, what it costs to do it that way, and who pays the postage. The bankruptcy courts had to invent their answer by order, six days and more into the outage. A fallback you have run once, on a quiet day, is worth far more than one written up in a continuity plan nobody has opened since the audit.

**Does it need to stay open?** A remote-support connection that is always available is convenient for the help desk and for anyone else who gets into the appliance. Put an expiry on standing access wherever the job allows it, so that access has to be granted again for each piece of work, and so a stolen key has a shelf life. CISA's other recommendation, to limit what the appliance exposes to the internet and keep its admin interface on trusted networks, is the same idea from the outside.

## After the job is done

A handover buys you time and attention, and it is usually worth buying. It also leaves something behind, a duty that never really left or a key that is still on someone's ring, and that part does not expire on its own just because the job did.

Somewhere, somebody is holding a key you gave them for a job that finished years ago. Do you know who?

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about AI governance (often), AI methodologies (also often), cybersecurity strategy (sometimes), and technology risk (always). Today's argument is that a function or a key you hand to someone else keeps its obligations and its access long after you stop thinking of it as yours, so the cost of a handover arrives at its end, and the only way to price it is to ask what it still opens today.*
