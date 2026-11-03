<!--
rv3 (29 Sep, Wed 30 day chat): his rulings on rv2 proposals applied -- (1) Dependabot callback NOT added, his call; (2) 'conversation' -> 'a live session'; (3) 'ordered a print of it'; (4) 'traditional code is deterministic' + 'Historically, the flow itself was the guardrail'; (5) 'components of art' -> 'components'; (6) lightbulb paragraph moved to the top of 'What the factory is built from', Dependabot paragraph moved after the TanStack/CrowdSec paragraph (its 'similar to the above' now points at the TanStack credential stealer). Two controlling images kept on his word: Tylenol for the US reader, the lightbulb for everyone.
-->
<!--
rv2 (29 Sep, Wed 30 day chat): rv1 = his edit pass. rv2 = MECHANICS ONLY on his text (its->it's x2, 'coding in'->'coding is', 'have have'->'that have', repitition, unbeknowst, intelltectual, reallized, extent->extant, 'We updates'->'We updated', 'things is'->'things that is'). No word, tone or contraction changes. Proposals are with him in chat, not applied.
-->
<!--
DRAFT v1 -- Wed 30 Sep 2026 [cyber]. Week plan: References\week-plan_2026-09-28.md (Wed 30 block).
Drafted 28 Sep 2026 in the Wed 30 day chat, after a re-sweep (addendum in References\research_wed30-their-script_2026-09-25.md).
NOT PANELLED. Not delivered. One [YOUR TAKE] open.
WORKING TITLE CHANGED: the plan's "Their Script, Your Storefront" leans on Ribon, which the record shows as a data pull, not a script on shoppers' screens. "The Name on the Bottle" is the drafter's proposal; title is his call.
CONTROLLING IMAGE: the 1982 Tylenol tampering (first death 29 Sep 1982, the day before publication). New to the corpus (grepped Published + Scheduled 28 Sep: zero hits).
WINDOW AVOIDED: Mon 28's press / proof / pallets / "the line"; Tue 29's logins and dashboard; the Fri 25 fountain; the keys-kept frame (Jul 8); open-question close; "for the price of"; "operator", "downstream", "on the hook", "black box", "sealed notice".
DO-NOT-PRINT honoured: no STARDUST CHOLLIMA; no "100,000 sites infected"; no Ribon skimmer; no "SRI/CSP would have stopped it"; no CrowdStrike 87%; no CrowdSec offboarding frame.
-->

# The Name on the Bottle

On 14 September, websites that had not changed a line of their own code started asking some of their visitors to run a command on their computers. The code that did it belonged to someone else, and the visitors had no way of knowing that.

Forty-four years ago yesterday, on 29 September 1982, a twelve-year-old girl in Elk Grove Village, outside Chicago, took an Extra-Strength Tylenol for a sore throat and died within hours. (For my Australian readers, Tylenol is roughly your Panadol: the same drug, sold under a different name.) Six more people in the Chicago area died over the next few days. The capsules had been laced with cyanide, and the police concluded fairly quickly that it had not happened at the factory. Someone had taken bottles off the shelves of ordinary stores (two Jewels, an Osco, a Walgreens, a Dominick's, a Frank's Finer Foods), poisoned them, and put them back. Johnson & Johnson had not touched those bottles after they left its building. It pulled more than 31 million of them anyway, spent more than $100 million doing it, and watched Tylenol's share of the painkiller market fall from about 35 percent to about 8.

The reason is simple and brutal. The customer never met the shelf. The customer met the name on the bottle. Whatever happened between the factory door and the medicine cabinet, it happened under Tylenol's name, and Tylenol carried it. The case has never been solved.

The web has the same shape, with one difference that matters a great deal. On a website, the name on the bottle is the one in the address bar, and that name is yours.

## Four and a half hours in September

Brevo (an email marketing platform, formerly Sendinblue, whose forms and chat widgets sit on a great many small and mid-sized business websites) published its own write-up of what happened on 14 September, and it is unusually candid, which deserves credit before anything else gets said about it. That said, the blast radius of the problem was substantial enough that the alternative was probably not any more palatable.

Here is the sequence, in UTC and in Brevo's own account. At 14:23 an attacker created a hostname on a Brevo-owned domain. By 15:01 a malicious Cloudflare Worker (a small program that runs at Cloudflare's network edge, rewriting web traffic in flight before it reaches the person asking for it) was live on brevo.com. At 16:07 it was routed to Brevo's forms domain and to three JavaScript files that customers embed in their own pages: the forms script, the Brevo Conversations chat widget, and the SDK loader. Brevo's security team opened an investigation at 19:33. The Worker came down at 20:30.

For about four and a half hours, then, a merchant who had pasted Brevo's snippet into their site (which is exactly what Brevo's documentation tells you to do) was serving an attacker's page to some of their own visitors. The page was a fake "verify you are human" check styled to look like Cloudflare, and it used a technique called ClickFix: it told the visitor to press Win+R, then Ctrl+V, then Enter. That sequence opens the Windows Run box, pastes a command the page had quietly put on the clipboard, and runs it. The command downloaded malware. On WordPress sites where an administrator happened to be logged in, the code went further and tried to install a malicious plugin in the background.

It was selective. In Brevo's words, "The page was shown selectively, so most visitors and repeat visits saw nothing." That is good news for the visitors who were skipped and bad news for the merchants, because it means most site owners who went and checked their own pages that afternoon would have seen a perfectly normal site.

How far it could have reached is a different number from how far it did reach, and the two keep getting blended in the coverage. A PublicWWW scan cited by Cybernews found something over a hundred thousand pages referencing Brevo's infrastructure. That is the size of the shelf, not a count of poisoned bottles. I have not found a figure from anyone for how many visitors actually ran the command.

## The part that was never touched

The detail that makes this worth a whole Wednesday is where the change lived.

Brevo is clear that its source files were fine: "No Brevo systems were modified at their source, the content was altered in transit at our CDN edge." The JavaScript sitting on Brevo's own servers was exactly what it was supposed to be. What changed was the layer in between, the delivery network that carries those files from Brevo to your visitor's browser. The factory was clean. The shelf was not.

And the way onto the shelf was a credential. Brevo's write-up, again in its own words: "A long-lived Cloudflare API key with full account permissions was stored in application source code." It says that key was "first misused in late August 2026," which means somebody had it for a couple of weeks before they used it for this.

Four days before any of that, on 10 September, Brevo had a separate and in some ways purer version of the same problem. A flaw in how its single sign-on was scoped let an attacker create an account, invite legitimate users into it, and ride those users' access into every organization they could reach. By Brevo's count, 138 accounts were accessed, 43 had contacts exported, and six were used to send phishing. Malwarebytes named some of the senders. Trezor (a maker of hardware wallets for cryptocurrency) was one, and its subscribers received an urgent "security alert" about a chip flaw that asked them for their wallet backup. That email came from Trezor's real account, through Trezor's real marketing platform, under Trezor's real name. Brevo's summary of that one is a sentence I would put on the wall of any vendor: "Customers trust us with access to their audiences, and in this case we failed to protect it." I have, in fact, ordered a print of it for my own business, because I think it's one of those things that is too easy to lose sight of on a regular basis.

Brevo does not say the two incidents are connected, and I am not going to say it for them. What they share does not depend on who did it. In both, the customer met the attacker under a name the customer trusted, and the business behind that name had not changed anything at all.

## What the factory is built from

On Monday I wrote about how fast the work gets made now. Today is about what it gets made from, because a modern website, and a modern piece of software in general, is overwhelmingly assembled from parts that someone else wrote, someone else ships, and someone else can change.

It's important to understand, I think, that when we talk about "parts" and "tools", here, we are talking about the conceptual equivalent of lightbulbs and batteries. These are not super complex components (like a catalytic converter); rather, they are items that have value in their repetition and their easy use model. So put it into that context, as if you were in a bad spy movie: you installed a new lightbulb in your kitchen and unbeknownst to you, there was a recording device inside the lightbulb. No one checks the filament in the lightbulb to make sure that's not the case. We're talking about the same thing here.

The Brevo snippet is one kind of part: a script you embed that fetches whatever the vendor currently serves. A software package is another. In May, 84 malicious versions of 42 packages in TanStack (a widely used family of open-source JavaScript libraries) were published to npm, the main public registry for JavaScript packages, in a window of about six minutes. The attacker got there through a misconfigured build workflow that let code from an outside contribution reach the project's publishing credentials. The poisoned versions carried a credential stealer aimed at cloud keys, npm tokens, GitHub tokens and SSH keys. An outside researcher spotted it in about 26 minutes, which is genuinely fast, and TanStack's own postmortem is honest about why it took an outsider: "No internal monitoring existed." One of the companies that later traced a breach back to that malware, CrowdSec, says a token stolen through it was used to copy about 170 of its private code repositories, which then surfaced on a forum in September.

We use tools heavily in our business -- most development companies do. The net effect is that you have more energy to spend on the things that fall into your intellectual property stack because you spend less energy on replicable items commonly available. For us, we use rendering components in displays. We also use a GitHub structure called "Dependabot" (now) which is responsible for making sure that components like these are fully up-to-date in our code. This is primarily a security methodology for us, but it does play out elsewhere in the system. And I say "now" because we realized that a component we were using was actually an active security risk and left us open to hacking as a result. A known hack, already extant in the wild. And the exploit was similar to the above -- credentials lifted from a live session. We updated it as soon as we found it, but we still weren't sure for a long time that the cows weren't already out of the paddock.

A third kind of part is the app you install into a platform you rent. In mid-September BigCommerce (now branding itself as Commerce) told merchants that credentials belonging to a third-party developer's apps, Ribon and Ribon 1.5, had been compromised through a breach at that developer's parent company. The one merchant on the public record, the UK spirits retailer Master of Malt, says the attacker used the app's key to download customer information page by page: names, emails, phone numbers and shipping addresses, but no card numbers or passwords. BigCommerce's public notice is careful to say this "was not a breach of Commerce systems or the BigCommerce platform," and it also contains the most honest sentence in this entire story: "Commerce has limited visibility into whether the actions taken by the application are valid or the result of the malicious actor."

Read that one twice, because it is true of almost every part in almost every stack. The platform can see that the app did something. It cannot see whether the app should have. And this is not particularly bad *design*, at least in a historic manner; traditional code is deterministic. Historically, the flow itself was the guardrail. The issue with that problem in the modern era is that governance on the flow itself no longer services the need of the system; mostly because the aggressors move towards penetration so much faster than they ever used to be able to, and the cost of penetration attempts has gotten so *de minimis*, that this historically sound design methodology is no longer sufficient.

## A credential, not a component

There is an easy version of this argument, and it is slightly off.

The easy version says "third-party code is dangerous, so use less of it." That is not quite what happened. At Brevo the code was fine; the key that let someone rewrite its delivery was sitting in source code. At TanStack the libraries were fine until a build credential was pulled out of the pipeline. At Ribon the app did what apps do; someone else was holding its key. In each case the part that failed was not the component itself but the credential that allowed the component to be changed, or to act, on someone else's behalf.

That matters because the parts you rely on are no longer static things you picked once. They are live relationships. Every snippet that loads from a vendor's URL, every package that updates on a version range, every app with an API key into your store is a standing arrangement in which somebody else can change what runs under your name, today, without asking you. That is the entire point of those arrangements (it is how the vendor fixes bugs for you without a phone call), and it is also exactly the property an attacker uses.

Regulators have been here before, and they did not accept "it was the vendor's part" as an answer. In 2018, attackers modified JavaScript on British Airways' site and sent card details from its payment pages to a look-alike domain for about fifteen days. The Information Commissioner's Office (the UK privacy regulator) fined BA £20 million, reduced from an initial £183 million, and among the failings it listed were hardcoded credentials and the absence of file integrity monitoring. Two years later the same regulator fined Ticketmaster UK £1.25 million over a third-party chatbot that sat on its payment page and was compromised; per the law-firm summaries of the decision (the ICO's own page is no longer online), the ICO described third-party JavaScript on pages handling personal data as a known security risk. In both cases the bill went to the name in the address bar.

## The seal that does not fit

After 1982, the fix for the Tylenol problem was packaging. Johnson & Johnson brought the capsules back that November in triple-seal packaging, the industry followed, the FDA moved to tamper-resistant packaging requirements, and in 1983 Congress made product tampering a federal crime. The seal works because the product is fixed at the factory. You know what went into the bottle; the seal tells you whether anyone opened it after.

The web has a seal, and on paper it is almost exactly the same idea. It is called Subresource Integrity (SRI for short): you put a cryptographic fingerprint of a script in your page, and the browser refuses to run the file if what arrives does not match. Had Brevo's customers been fingerprinting a fixed file, an edge rewrite of it would have been refused.

The trouble is that most of these scripts are not fixed files, by design. Brevo's own documentation gives you a snippet that loads `sdk-loader.js` from its CDN with no version in the address and no fingerprint, and that loader then fetches more code at runtime. A merchant who pinned a fingerprint to it would have broken their own widget the next time Brevo shipped an update, which is precisely why so few do. It is a tamper seal on a bottle whose contents the supplier refills every week. Brevo's remediation list now includes "integrity protection for versioned embedded assets where technically possible," and the phrase "where technically possible" is carrying a lot of weight in that sentence.

The other common control, a Content Security Policy (a header that tells the browser which domains a page is allowed to load code from), would most likely have waved this through, because the bad code arrived from Brevo's own addresses and a hostname on a Brevo-owned domain. An allowlist that says "Brevo is fine" is an allowlist that says the attacker holding Brevo's key is fine.

And the rulebook most merchants think of first draws its boundary in a specific place. PCI DSS, the card industry's security standard, has since 31 March 2025 required two things of payment pages: requirement 6.4.3, that every script running in the customer's browser on a payment page is authorized, integrity-checked and inventoried with a written justification; and 11.6.1, a mechanism that alerts on unauthorized changes to those scripts and the security headers as the browser receives them. Those are good requirements. They cover payment pages. Brevo's forms and chat live on contact pages, newsletter sign-ups and account pages, and ClickFix was not after card numbers; it was after the visitor's computer. (And merchants who fully outsource their payment page now largely self-attest that their site "is not susceptible to attacks from scripts," which is a sentence that aged fast.) The standard fenced off the till. The attacker walked into the rest of the shop.

## What it (maybe?) costs, and what it (probably) costs to look

The numbers around this are large and mostly general, so take them as the size of the room rather than a price tag. IBM's 2026 breach report puts the global average cost of a breach at $4.99 million, a record. Verizon's 2026 Data Breach Investigations Report says third-party involvement in breaches is up 60 percent. The regulator's version is more specific: £20 million for BA, £1.25 million for Ticketmaster, both for code on their pages that they did not write or did not watch.

What it costs to look is smaller than most people assume, and that is the uncomfortable part. Cloudflare, the same edge network the Brevo attacker used, offers basic monitoring of the scripts loading on your pages on every plan, including the free one; detecting malicious or changed scripts and alerting on them sits in a paid tier. SRI and CSP cost nothing to license. What they cost is engineering time, and breakage when a vendor ships an update you did not pin. Which is a real cost, and a known one, and it is a very different kind of number from the ones in the paragraph above.

For the merchants in this month's cases, none of the companies involved has said what it cost them. What is visible so far is the unglamorous part: customer notification letters, a report to the ICO from Master of Malt, WordPress cleanups for Brevo customers whose admins were logged in at the wrong moment, and at least one law firm soliciting Ribon plaintiffs.

## A few things worth doing this week

**Count what runs on the pages that matter.** Not only the payment page. The contact form, the sign-up, the account page, the chat bubble. For each script, write down who serves it, whether it loads a fixed file or "whatever is current," and why it is there. PCI asks for a written justification on payment pages; the same habit is cheap everywhere else, and it is the list you will want in your hand on the day a vendor's name turns up in the news.

**Ask each vendor for a version you can fingerprint.** Some already publish versioned files with published hashes; some, like Brevo now, say they are moving that way. The question costs you an email. Where the answer is yes, pin it. Where the answer is no, you have learned how much of your page you are trusting on faith, and that is worth knowing.

**Watch what the browser actually receives.** Your origin files being clean told you nothing on 14 September. A weekly check of the scripts and security headers as a visitor's browser receives them (the 11.6.1 bar, applied off the payment page) would have been looking at the right layer. A Content Security Policy in report-only mode will not stop anything, but it will tell you when the list of things loading on your pages changes.

**Scope what your installed apps can do.** An app that needs to read orders does not need to read every customer record, and an app nobody has used since last spring does not need a key at all. Go through the apps installed in your commerce platform, your CMS and your marketing stack, and cut each one back to what it actually uses.

## The name in the address bar

Johnson & Johnson did not put anything in those capsules, and it still pulled every bottle in the country, because the only name anyone in Chicago saw that week was Tylenol. The seal that fixed it only worked because the product in the bottle stopped changing once it left the factory.

Most of what runs on a website never stops changing, and that is by design, and it is not going to be undone. So the name in the address bar carries whatever arrives under it, from whichever vendor, at whatever hour, and the seal the rest of the world takes for granted mostly does not exist yet for the parts doing the arriving.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the scripts, packages and apps a business builds on can be changed by someone else at any moment, that what failed in this month's Brevo, TanStack and Ribon incidents was the credential behind the part rather than the part itself, and that whatever arrives on your page arrives under your name.*

<!--
SOURCES (for his reference; kept out of the body per house style)
- Tylenol: PBS NewsHour (first death 29 Sep 1982, 12-year-old; seven deaths; bottles taken off shelves and returned; >31M bottles, >$100M; unsolved). Wikipedia "Chicago Tylenol murders" (store list; market share 35% -> 8%; triple-seal package reintroduced November 1982). Pharmacy Times (Federal Anti-Tampering Act, 1983). FDA packaging rule: "within the year" per Wikipedia; 21 CFR 211.132 codified 1989 per Pharmacy Times -- printed as "moved to tamper-resistant packaging requirements", no date. RE-CHECK the Elk Grove Village location of the first victim at primary before scheduling.
- Brevo 14 Sep: status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up (primary; re-read live 28 Sep). WordPress plugin detail: Brevo write-up + BleepingComputer.
- Brevo 10 Sep: status.brevo.com/incidents/01M266V1CZKJQNGZRNEGFD5CQE/write-up (primary); Malwarebytes (Trezor lure).
- Reach: Cybernews citing PublicWWW (~117,000 pages). Reach, not victims.
- Brevo snippet: developers.brevo.com/docs/getting-started-with-js-implementation (primary).
- TanStack: tanstack.com/blog/npm-supply-chain-compromise-postmortem; NVD CVE-2026-45321; GHSA-g7cv-rxg3-hmpx (primary).
- CrowdSec: crowdsec.net/blog/tanstack-supply-chain-attack-analysis (primary, 18 Sep).
- BigCommerce/Ribon: security.bigcommerce.com (primary, 17 Sep); eSecurityPlanet 28 Sep ("page by page", via Master of Malt); BleepingComputer 21 Sep. Emery Reddy Ribon page (class-action solicitation).
- BA: ico.org.uk/media2/migrated/2618421/ba-penalty-20201016.pdf (primary). Ticketmaster: law-firm summaries (Hunton); ICO page 404.
- SRI: MDN (primary). PCI DSS 6.4.3 / 11.6.1 / SAQ A: PCI SSC blog 30 Jan 2025 and 10 Mar 2025 (primary); requirement wording via Adyen and Foregenix (standard PDF unreached).
- IBM Cost of a Data Breach 2026 ($4.99M, primary). Verizon 2026 DBIR release ("up 60%", primary).
- Cloudflare Page Shield / Client-Side Security docs (primary).
RE-SWEEP BEFORE SCHEDULING
- Any Fastr / Ribon / Be A Part Of statement; any merchant count.
- Sansec research page (still unreached 28 Sep) -- only if we want to credit discovery.
- Brevo write-ups re-read for revisions.
-->
