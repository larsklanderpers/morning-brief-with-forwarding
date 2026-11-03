# Research Note -- Aura and the inherited acquisition list
For: `substack_draft_what-you-inherited_2026-09-12` (Sat 12 Sep) · Depth: deep · Date: 2026-09-09

## Bottom line

The acquisition is named, and it is named by Aura itself: **Circle Media Labs, Inc., acquired
December 2021**, a parental-controls company. The exposed data was **Circle's sales and marketing
database**, not Aura's. That single fact turns the plan's thesis from an assertion into a documented
case, and it is on Aura's own second incident page, which the 14 Aug pass never reached.

Two things in the working brief are wrong and one kill needs reversing. **Circle is not a dormant
list from a forgotten acquisition** -- meetcircle.com is live today and its footer reads
"© 2026 Circle Media Labs, Inc., an Aura company," so the piece cannot run a forgotten-in-the-attic
image. And the **14 Aug kill on the ShinyHunters attribution was over-broad**: the name collision it
found is real and separate, but BleepingComputer and Help Net Security independently report
ShinyHunters claiming this incident on its own leak site around 16 March 2026.

⚠️ **His own brief pipeline re-injected two killed claims on 7 Sep.** `Daily Briefs/brief_2026-09-07.md`
flags the story as "March 2026, ShinyHunters, 900K records" and pitches the recursive-irony hook --
the exact framing the 14 Aug pass ruled is not the story, wearing a fresh SecurityWeek citation. Same
engine as the 55% on-prem figure. Do not draft from that brief entry.

---

## What's solid

**All footed at Aura's own two pages, both re-fetched live 9 Sep 2026.**

- **The acquisition is Circle Media Labs, Inc., and Aura names it.** The incident-update page: the
  data came from *"a sales and marketing database used by Circle Media Labs, Inc. ('Circle')"* which
  Aura acquired in 2021. [aura.com/learn/march-2026-security-incident-update]
- **The press release names the year but not the company.** *"a contact list from a company Aura
  acquired in 2021."* Update stamp on the page: **19 March 2026, 10:00 AM ET.**
  [aura.com/press/release/statement-on-exposure-of-customer-information]
  ★ **The two pages disclose different amounts. The press release is the one the coverage quotes and
  it does not name Circle. The learn page does.** That gap is itself usable.
- **The acquisition date is 9 December 2021**, and Circle is described in Aura's own announcement as
  *"the #1 parental control and screen time management solution for families."* Deal terms not
  disclosed. Announced weeks after Aura's $200m Series F at a $2.5bn valuation (October 2021).
  [aura.com/press/release/digital-security-provider-aura-acquires-parental-controls-leader-circle-media-labs]
- **The scale and the denominator.** *"approximately 900,000 records, the vast majority of which
  consist of names and email addresses from a marketing tool."* Aura's own customer exposure:
  *"less than 20,000 active Aura customers and less than 15,000 former Aura customers."*
  **Roughly 35,000 against roughly 900,000: about 96% of the exposure was people who were never
  Aura customers.**
- **HIBP is the independent count and it is higher: 903.1k accounts**, added **18 March 2026**,
  breach date March 2026. Compromised data classes: **customer service records, email addresses,
  IP addresses, names, phone numbers, physical addresses.**
  [haveibeenpwned.com/Breach/Aura]
  ★ **"Customer service records" appears in HIBP's classes and in BleepingComputer's field list, and
  in neither of Aura's own pages.** The press release says names and email addresses; the learn page
  adds home addresses, phone numbers and IP addresses "in some cases." Support-ticket history is
  disclosed nowhere by Aura.
- **The vector is vishing and it is Aura's own word, not a reporter's inference.** *"an employee was
  the victim of a targeted phone phishing attack"*; the third party *"gained access to that
  employee's account for approximately one hour."*
- **What Aura says was not taken:** *"No Social Security numbers, passwords, or financial information
  were compromised."* Learn page adds no Aura app vault data and no credit records, and states
  *"Aura's product was not hacked"* and the compromised employee *"did not have access to any of the
  systems or databases that support our online safety and identity theft protection product."*
- **Aura's own mitigation framing, quotable as theirs:** *"90% of the leaked emails were already
  present in previous leaks."* HIBP reports the same 90% figure.
- ★★ **Circle is still a live brand.** meetcircle.com, fetched 9 Sep 2026: *"Circle is now part of
  Aura, the leader in family online safety,"* an active trial offer, and the footer
  *"© 2026 Circle Media Labs, Inc., an Aura company. All rights reserved."*
  **This kills the forgotten-list framing and replaces it with a better one** -- the database was
  never abandoned, it was attached to a business that kept running, which is precisely why nobody
  ever had an occasion to look at it.

### The M&A inheritance ground, footed at the regulator

**ICO, Marriott International Inc, Monetary Penalty Notice, 30 October 2020** -- fetched 9 Sep 2026.
Unspent in his entire corpus; no piece has run Marriott, Starwood or a due-diligence exhibit.

- ★ **Para 6.64, the sentence the piece can hang on:** *"The need for a controller to conduct due
  diligence in respect of its data operations is not time-limited or a 'one-off' requirement."*
- **Para 3.2:** Marriott *"states that it was only able to carry out limited due diligence on the
  Starwood data processing systems and databases."*
- **Para 6.66:** *"Controllers cannot process personal data without appropriate security measures
  being in place on the basis that the system was deficient prior to May 2018 and has not been
  remedied."*
- Penalty **£18.4 million** (para 1.7). **339 million guest records** affected, 30.1 million EEA,
  7 million UK (para 4.3). Intrusion began **29 July 2014** (para 3.8); discovered **8 September
  2018** via Accenture and a Guardium alert (para 3.18).
- ⚠️ **The disanalogy is the point and the draft must state it.** Marriott inherited a system that
  was *already compromised* at close. **Aura inherited a list that was perfectly fine at close and
  became a liability five years later.** The Marriott defense was "we could only do limited
  diligence." Aura has no equivalent defense to need, because there was nothing to find. That is
  the harder case and the more common one.

**OAIC, APP Guidelines Chapter 11, last updated 3 October 2025** -- the AU instrument that bites.
APP 11.2: an entity *"must take such steps as are reasonable in the circumstances to destroy the
information or ensure that it is de-identified"* once it is no longer needed for a permitted purpose.
The obligation applies whether or not the entity physically holds the data, so long as it has
*"the right or power to deal with it."* An inherited marketing list nobody has a current purpose for
is the textbook APP 11.2 case, and the destruction duty runs continuously, not at close.

---

## What's contested / watch out

- **ShinyHunters. The 14 Aug kill is reversed, narrowly.** BleepingComputer, 18 March 2026:
  *"Earlier this week, the threat group ShinyHunters claimed the attack on their data extortion
  site."* Help Net Security, 19 March 2026, reports the same claim. Wikipedia dates it to on or
  around 16 March 2026. **Aura has never named an actor, in either statement.** So the printable
  form is a **claim of responsibility, attributed and dated** -- never "ShinyHunters breached Aura."
  ⚠️ **The name collision the 14 Aug pass found is real and remains a live trap:** ShinyHunters also
  ran a large, entirely separate campaign against misconfigured **Salesforce Experience Cloud
  `/s/sfsites/aura` endpoints**. Two unrelated things named Aura. **Recommendation: leave the actor
  out of the piece.** Who did it is not the argument, and naming them buys a hedging clause and a
  collision risk for nothing.
- **IBM's Cost of a Data Breach 2026** ($4.99m global average, $11.5m US) is available but every
  path to it is secondary and the report is a vendor lead-generation asset. **He has already used
  IBM's cost report three times** (`you-the-product` 30 Jun, `tooling-up` 4 Aug, `brief-and-check`
  18 Aug). A fourth is a tic, and the per-record framing is not what this piece needs.
- **The M&A due-diligence advice literature is almost entirely written by people selling due
  diligence** -- the search returns consultancy checklists and law-firm alerts. Per house rule 2, if
  the piece uses any of it, that is the story and not the source. The ICO notice and APP 11.2 are
  the only non-commercial instruments found.

---

## Couldn't verify

- **When the Circle records were collected.** Circle's original product was "Circle with Disney"
  (now discontinued), so the list plausibly reaches back to 2015-2016 and predates the acquisition
  by years. **Aura says nothing about the age of the records and no source establishes it.**
  ⛔ Do not print any claim about how old the list is, or that it contains Disney-era buyers.
- **Whether Aura notified regulators, and which.** Help Net Security quotes Aura on notifying law
  enforcement and affected customers. No state AG filing, FTC action or class action was found.
  **Per the standing absence rule this is a not-found, not an absence.** The Maine AG database was
  not queried directly. Do not write that nobody sued or that no regulator acted.
- **Any intrusion date.** Neither Aura page gives one, and SecurityWeek's earlier reporting
  explicitly said Aura did not say when the attack occurred. The only dates in hand are the leak-site
  claim (~16 Mar), HIBP's add (18 Mar), the press-release stamp (19 Mar) and the learn page (26 Mar).
- **What Aura paid for Circle.** Terms undisclosed. There is no purchase price to set against the
  903,100 records, so **the cost framing cannot be a ratio.** It has to be the denominator instead.

---

## The economics

**The denominator is the economics, and it does not need a dollar figure.**

Roughly **903,100 records** exposed. Roughly **35,000** of them were Aura customers, active or
former. About **96% of the blast radius belonged to people who had no relationship with Aura at
all** -- they had a relationship with a parental-controls company that stopped being independent in
December 2021.

The marginal value of a 2021-era sales-and-marketing database to a 2026 subscription business is
close to zero; the liability attached to it is the full 903,100. **The asset depreciated and the
liability did not.** That asymmetry is the piece, and it is why nobody prices it: at close, a
contact list is a line in the data-room index with a positive sign in front of it. Nothing in the
deal mechanics ever revisits the sign.

Aura's own risk posture makes the point sharper rather than softer: the learn page lists ISO 27001,
AICPA SOC 2 Type II and PCI-DSS. **None of those certifications ask what you inherited.**

---

## Drop-in facts (each with a source)

- *"a sales and marketing database used by Circle Media Labs, Inc. ('Circle')"* -- Aura, incident
  update page. [aura.com/learn/march-2026-security-incident-update]
- *"a contact list from a company Aura acquired in 2021"* -- Aura press release, updated 19 Mar 2026.
- *"less than 20,000 active Aura customers and less than 15,000 former Aura customers"* -- same.
- **903,100 accounts**, added 18 Mar 2026; classes include **customer service records**. [HIBP]
- *"an employee was the victim of a targeted phone phishing attack"*; access lasted *"approximately
  one hour."* -- Aura press release.
- *"Aura's product was not hacked"* -- Aura, incident update page.
- *"© 2026 Circle Media Labs, Inc., an Aura company."* -- meetcircle.com footer, 9 Sep 2026.
- Circle was *"the #1 parental control and screen time management solution for families"* -- Aura,
  9 Dec 2021 acquisition announcement.
- *"The need for a controller to conduct due diligence in respect of its data operations is not
  time-limited or a 'one-off' requirement."* -- ICO, Marriott MPN, 30 Oct 2020, para 6.64.
- *"only able to carry out limited due diligence on the Starwood data processing systems and
  databases"* -- ibid, para 3.2. Penalty £18.4m; 339 million records.
- APP 11.2: destroy or de-identify once no longer needed; applies wherever the entity has
  *"the right or power to deal with it."* -- OAIC APP Guidelines ch. 11, updated 3 Oct 2025.

---

## ⛔ DO-NOT-PRINT

**This list binds every revision of this piece, not just v1.**

1. **"900,000 customer records."** They were not customers. The denominator is the story.
2. **"ShinyHunters breached Aura"** as a statement of fact. Claim of responsibility only, dated,
   attributed to the reporting -- and the recommendation is to omit the actor entirely.
3. **Any Salesforce `/s/sfsites/aura` material.** Different incident, same word.
4. **The recursive-irony hook** ("an identity protection company lost identities"). It is the 7 Sep
   brief's framing, it is what every outlet ran in March, and it is not this piece's argument.
5. **Any claim about the age or composition of the Circle list**, including Disney-era buyers.
6. **Any forgotten-list or dormant-list image.** Circle is live and still selling.
7. **That no regulator acted or nobody sued.** Not-found is not absence.
8. **Any intrusion date.** None is published.
9. **Any dollar figure attached to the Circle deal.** Terms undisclosed.
10. **Any motive attributed to Aura** for not finding the list sooner.

---

## Angles this opens

- **Supply Chain × Trust Boundaries**, as the plan has it, but the boundary is temporal rather than
  organizational: the party who accepted the risk and the party carrying it are the same company
  five years apart. That is a genuinely different axis from the week's other six pieces, all of
  which are a control held by *somebody else right now*.
- **Callback available and unspent:** Marriott/Starwood appears nowhere in his corpus, and the ICO's
  "not a one-off requirement" line is a governance sentence he can use straight.
- ⚠️ **Register adjacency to Sat 5, and it is the real risk.** Sat 5 closes on *measure the second
  number yourself, nobody else will check.* This piece's action is *go inventory what you inherited,
  because nobody counted it.* No shared vocabulary, same weekend slot, same self-audit shape, one
  week apart. **Whatever the action turns out to be, it cannot be a rep, a sort or a self-measurement
  the reader performs alone** -- those are all spent within the window. An inherited-data question
  put to somebody else (the deal lawyer, the data owner, whoever ran the last integration) is a
  different move and is available.
