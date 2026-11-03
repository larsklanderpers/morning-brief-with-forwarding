# Research: the 119th Congress's law count against the executive-order count

**Commissioned by:** Lars, Heinlein inbox, 22 Sep 2026, on an Instagram reel screenshot. His note
was "Facts to research and confirm" (a research instruction, not a draft commission).
**Raw item:** `Research Notes/intake/intake_2026-09-22_congress-laws-vs-executive-orders.md`
**Status:** research only. Nothing is drafted and no slot is claimed.

---

## Headline

**The reel is right about the shape and loose about the numbers.** Every figure it prints is either
correct, or stale low by a few units, in the direction that flatters its argument. Two of its six
claims do not survive as stated:

- ⛔ **"The Trump presidency holds the record for the most executive orders since FDR" is false
  unless you say "per year".** Truman signed 907 and Eisenhower 484.
- ⛔ **"Fewest enacted laws since Thomas Jefferson" is not established and currently runs the wrong
  way.** The 119th has already enacted more public laws than the Congress of 1807-1809 did in its
  full two years.

The defensible version of the whole thing is narrower and still striking, and it is in
*What can be printed* at the end.

---

## Claim by claim

### 1. "With the House closed until midterms" - CONFIRMED for the House, WRONG for Congress

The House closed **Wednesday 16 September 2026** for a seven-week recess, returning after the
**3 November** election. Speaker Johnson cancelled the Thursday votes, cutting the week short.
Members had been back only about **seven working days** since the 31 August return. Rep. Ralph
Norman, quoted in the Daily Signal piece, says the House has cancelled **at least 63 scheduled
voting days this Congress**, nine of them in September alone. Left undone on the way out: an AI
regulation package and an impeachment vote against Secretary of War Hegseth.

⚠️ **But the Senate is not closed, and several headlines say "Congress" when they mean the House.**
The Senate held a pro forma session on **18 September** and **reconvened at 3pm on Tuesday 22
September 2026**. Both chambers are out for nearly all of October and the first week of November.
**Do not print "Congress adjourned until the midterms".**

⚠️ CNBC 403'd the fetcher. This rests on the Daily Signal, AllSides and voz.us summaries, which
agree with each other. Re-read one at source before quoting Norman's 63-days figure.

### 2. "They've passed 108 laws so far" - STALE, and the wrong verb

The **119th Congress has enacted 111 public laws and 2 private laws**, the most recent being
**PL 119-111, the Lindsey O. Graham Sanctioning Russia and Iran Act of 2026, 18 September 2026**.
108 would have been right a few days before the reel was posted.

Two qualifications that matter more than the three-unit gap:

- **"They've passed" reads as the House.** 111 is *public laws enacted*, which means both chambers
  plus a signature. The House passes far more bills than that and they die in the Senate.
- ⚠️ **congress.gov 403'd the fetcher**, so 111 comes from Wikipedia's transcription of the acts
  list (updated 22 Sep 2026). **Re-check at congress.gov before any number ships.**

For the year on its own: **34 public bills through 31 August 2026**, which No Labels puts as the
lowest of any midterm year back to 1990 by a wide margin (1990: 142, 2018: 136, 2022: 93, 2014: 91).

### 3. "In 1948, Truman called them the Do Nothing Congress with 906 passed laws" - CONFIRMED

The 80th Congress (1947-49) passed **906 public bills**. Truman campaigned against it as the
"Do Nothing Congress" in 1948. It passed the Truman Doctrine, the Marshall Plan and Taft-Hartley,
the last over his veto; what it *did not* pass was his Fair Deal programme.

★ **The reel's best point is one it makes by accident.** Truman's label was about **priorities, not
output**. A Congress that passed 906 laws got called do-nothing for refusing one president's agenda.
That is the honest frame for the whole metric, and it cuts against the reel as much as for it.

### 4. "Go back to 1807 ... only 17 states" - the state count is right, the comparison is not

**17 states in 1807: CONFIRMED.** Ohio was the 17th, admitted 1803; Louisiana was the 18th, 1812.

⛔ **The law comparison breaks.** The **10th Congress (March 1807 to March 1809) passed roughly 104
public acts** across its two sessions: 67 public chapters plus 1 public resolution in the first
session, 37 in the second, per the Wikisource transcription of *Statutes at Large* volume 2. The
**119th is already at 111 with three and a half months left to run.**

So the Congress the reel tells you to go back to actually passed **fewer** laws than this one has.
The claim is a reasonable ballpark presented as a floor, and the floor is not there.

⚠️ The Wikisource page is **marked incomplete** and excludes private acts (held in volume 6). Treat
104 as approximate. If this is ever printed, the count has to come off the Library of Congress
scan (`tile.loc.gov/storage-services/service/ll/llsl/llsl-c10/llsl-c10.pdf`), not off Wikisource.

### 5. "Jefferson issued 4 executive orders" - CONFIRMED as catalogued, and the catalogue is the problem

The American Presidency Project lists **Thomas Jefferson: 4 executive orders, 0.50 per year**. The
number is correctly quoted.

⛔ **It is not the same unit as Trump's 284, and this is the weakest link in the reel.** Executive
order numbering **began in 1907**, when the State Department numbered the orders in its files back
to **1862**. Everything before Lincoln is a retrospective reconstruction from surviving papers and
is certainly an undercount. Jefferson governed by proclamation, instruction to cabinet officers and
private letter, none of which the modern series captures. **Setting 4 beside 284 compares a modern
census to an archaeological estimate.** Any piece that runs this pairing carries that sentence, or
it does not run the pairing.

### 6. "Trump has issued 281 so far, more than Obama's two terms combined" - CONFIRMED on the comparison, STALE on the count

- **Obama: 276 executive orders across eight years.** So "more than Obama's two terms combined" is
  **true**, and was true at 281 as well.
- **The current count is 284 or 285, not 281.** The Federal Register API, queried 22 Sep 2026,
  returns **284 executive orders signed on or after 20 January 2025**, the newest being **EO 14430,
  signed 17 September 2026**. The American Presidency Project's table says **285** for the second
  term. The one-document gap is a counting convention (corrections and numbering), not a dispute.
  281 corresponds to EO 14427 and was right a week or two ago.
- ⚠️ **federalregister.gov HTML 302'd to an unblock page.** The **JSON API answered**. Use
  `federalregister.gov/api/v1/documents.json` with `conditions[president]=donald-trump` and
  `conditions[presidential_document_type]=executive_order`.

### 7. "The record for the most executive orders since FDR" - FALSE as stated, TRUE per year

American Presidency Project totals and annual averages:

| President | Total EOs | Per year |
|---|---|---|
| F. D. Roosevelt | 3,726 | 307 |
| Truman | 907 | 117 |
| Eisenhower | 484 | 61 |
| Obama | 276 | 35 |
| Trump I | 220 | 55 |
| Biden | 162 | 41 |
| **Trump II** | **285** | **171** |

- **On totals the claim fails.** Truman's 907 and Eisenhower's 484 both beat Trump's second-term
  285. Even both Trump terms combined (505) sit below Truman.
- **On rate the claim holds, and comfortably.** At **171 a year**, Trump II is the **highest annual
  rate of any president since FDR**, running at about half of FDR's wartime pace and roughly
  **five times Obama's**.

⛔ **Print it as a rate or do not print it.** "Most since FDR" unqualified is refuted by Truman.

### 8. "Fewest enacted laws since Thomas Jefferson" - NOT ESTABLISHED

Follows from claim 4. 111 already exceeds the 10th Congress's roughly 104. The defensible claim is
the **modern** one: the 118th Congress's full-term **274 public laws** was already a modern low, and
the 119th is tracking well below it with the House gone until November.

### 9. "A congress that has handed over their power to president" - opinion, not a fact

Recorded as the reel's thesis. Not checked, and not checkable.

---

## ⛔ The objection that binds any use of this

**Counting laws is a contested productivity measure and the objection is not a partisan one.** AEI
argues directly that we mismeasure Congress by counting laws. The Library of Congress's own
Statutes at Large material makes the structural point: since the Second World War, Congress has
enacted roughly **4 to 6 million words of new law per two-year Congress**, and the falling bill
count reflects **consolidation into omnibus vehicles**, not less legislating. Newsweek's own
fact-check of the "least productive" framing carries experts making the same caveat while still
confirming the underlying count.

Note also that Speaker Johnson has claimed this is the **most productive Congress in 80 years**, a
claim Snopes and Yahoo both checked and found wanting on bills passed by the House. **Both sides of
this argument are reaching for the metric that suits them.** That is the most Heinlein-shaped
observation available here and it is standing accuracy rule 5 in its natural habitat.

---

## ✅ What can be printed

Three sentences that survive everything above:

1. The 119th Congress has enacted **111 public laws** as of 18 September 2026, and **34 of them in
   2026**, which is the lowest total of any midterm year since at least 1990. The House left on
   **16 September** and is gone until after the 3 November election.
2. Over the same period the second Trump administration has signed **284 executive orders**, more
   than Obama signed in eight years, at **about 171 a year, the highest annual rate since FDR**.
3. Whether that is a Congress ceding power or a Congress legislating in bigger vehicles is the
   argument, and **the bill count alone cannot settle it**.

## ⛔ Do not print

1. **"Most executive orders since FDR"** without "per year". Truman: 907.
2. **"Fewest laws since Jefferson"** or **"you have to go back to 1807"**. The 10th Congress passed
   about 104 and the 119th is past that.
3. **"281 executive orders"** or **"108 laws"**. Both are stale low. Use 284 and 111, re-checked.
4. **"Congress adjourned until the midterms."** The House did. The Senate sat on 22 September.
5. **Jefferson's 4 beside Trump's 284** without the 1862/1907 numbering caveat in the same sentence.
6. **The 104 figure for the 10th Congress off Wikisource.** Incomplete page. Go to the LoC scan.
7. **Norman's "63 cancelled voting days"** without re-reading it at a source that opens.
8. **Anything sourced to the reel itself.** The account was not checked and the video was not
   fetched. It is the prompt for this note, not a citation in it.

## Sources

- [List of acts of the 119th United States Congress](https://en.wikipedia.org/wiki/List_of_acts_of_the_119th_United_States_Congress) (111 public laws, updated 22 Sep 2026; congress.gov 403'd)
- [Federal Register API, Trump executive orders since 20 Jan 2025](https://www.federalregister.gov/api/v1/documents.json) (284; newest EO 14430, 17 Sep 2026)
- [Executive Orders - The American Presidency Project](https://www.presidency.ucsb.edu/statistics/data/executive-orders) (totals and per-year averages; Jefferson 4)
- [80th United States Congress](https://en.wikipedia.org/wiki/80th_United_States_Congress) (906 public bills; Do Nothing Congress)
- [United States Statutes at Large, Volume 2, 10th Congress](https://en.wikisource.org/wiki/United_States_Statutes_at_Large/Volume_2/10th_Congress) (roughly 104 public acts; page marked incomplete)
- [Acts of the Tenth Congress, Library of Congress scan](https://tile.loc.gov/storage-services/service/ll/llsl/llsl-c10/llsl-c10.pdf) (the primary, not yet read)
- [How Much Has Congress Actually Worked in 2026? - No Labels](https://nolabels.org/the-latest/how-much-has-congress-actually-worked-in-2026/) (34 public bills through 31 Aug 2026; midterm-year table)
- [House Closes Up Shop a Day Before Scheduled 7-Week Recess - Daily Signal](https://www.dailysignal.com/2026/09/16/house-closes-for-recess/) (16 Sep close, seven-week recess, Norman quote)
- [Congress goes home after just 7 workdays - AllSides](https://www.allsides.com/news/2026-09-16-0700/politics-congress-goes-home-after-just-7-workdays-summer-break-ended-and-wont-be-back-until-after-midterms) (seven working days)
- [House heads home to campaign amid calls for urgent AI action - CNBC](https://www.cnbc.com/2026/09/17/ai-crisis-congress-regulation.html) (403'd; summary only)
- [Senate Schedule - Senate Democratic Caucus](https://www.democrats.senate.gov/floor/senate-schedule) (pro forma 18 Sep, reconvened 3pm 22 Sep)
- [Has the 119th Congress Been One of the Least Productive Ever? - Newsweek](https://www.newsweek.com/donald-trump-least-productive-congress-laws-2102819) (the caveat, from experts)
- [We Mismeasure the Productivity of Congress by Counting Laws - AEI](https://www.aei.org/commentary/we-mismeasure-the-productivity-of-congress-by-counting-laws/)
- [Is current Congress most productive in 80 years, as Mike Johnson claimed? - Snopes](https://www.snopes.com/fact-check/mike-johnson-productive-congress/)
