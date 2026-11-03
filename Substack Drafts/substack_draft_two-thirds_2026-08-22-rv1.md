# The Two Thirds Nobody Counted

**Status: DRAFT v1 -- Sat 22 Aug 2026 (Diversion #2, long form -- second of the week's two diversions). Unpanelled. One [YOUR TAKE] marker open.**
**Series: Saturday Diversion. Lighter register by argument, not by length (Lars, 12 Aug: lightness is a state of being). No word-count gate.**
**Thread: Practitioner / Coding Ground Truth · Co-Existence / Judgment · Diversions. DELIBERATELY NOT Shape of Work -- Sat 15 was Shape of Work, two consecutive Saturdays on one thread is the collision the handoff caught.**
**Builds on: "You Already Know What Wrong Sounds Like" (Sat 15 -- DECLARED RETURN to the same paper) · "Write the Brief. Then Write the Check" (Tue 18 -- pays off its printed promise: "Saturday brings a number that puts a floor under all of this... a great deal less uncomfortable if you have spent the week writing checks").**
**Source: week-plan_2026-08-17.md (Sat 22) · References/research_saturday-verify-items_2026-08-12.md (all quotes verbatim from the primary).**

**★ THE DECLARED RETURN IS PRECISE, DO NOT LOOSE IT. Sat 15 ALREADY STATED the 26-30% number and called it "the honest floor under every 'the agents do the work now' conversation you will have this year." So the move is NOT "I walked past the number" (false -- he named it). The move is "I mentioned it and moved on, and it has been bothering me all week." Getting this wrong is a factual error about his own corpus.**

**DELIBERATE EXCLUSIONS -- all Sat 15, do NOT re-run:**
**- The ten-largest-occupations-within-seven-points finding.**
**- The expertise gradient / the three inferred signals / "senior engineer in unfamiliar Rust is a beginner."**
**- Taste as the controlling image; the "write down three things a new hire would miss" exercise (that was Sat 15's action section -- Tue 18 already picked it up, this must not a third time).**
**- AI FinOps, Qualcomm band, archetypes, Ramp x Revelio 12%.**

**METAPHOR/DEVICE BURN (7-day window Sun 16 -> Fri 21, both directions):**
**- see/hold/grip (Sun 16, used Wed 19) · chain of custody / belt-and-braces / rip-in-pants / logs-as-input (Thu 20) · documented-feature-wearing-a-reputation / stop-sign-speed-camera / ATM (Fri 21) · harness-as-image (Mon 17) · scope of works / builder (Tue 18) · "Sit with" (BANNED).**
**- The verified-success NUMBER itself is shared with Sat 15 by design (declared). Its INTERPRETATION here -- the missing two thirds as unmeasured rather than failed -- is new and is the whole piece.**

**SELF-CAUGHT BEFORE FIRST DELIVERY (panel will confirm): (1) "Read that twice" removed -- it is the near-variant of his rationed "Read that again" that the Sat 15 panel already cut once; installing it again would be the exact repeat that got cut. Now "That definition is doing all the work." (2) "Sit that number down" removed from the opener -- echoes the BANNED "Sit with" device (Fri 14/Mon 17/Wed 19). Now "Set that number down next to."**
**ACCURACY -- verbatim from the primary (Hitzig, Massenkoff, Lyubich, Zhang, Heller, McCrory, "How Claude Code is used in practice," 16 Jun 2026):**
**- verified success = judged success PLUS verifiable evidence (git commits, passing tests, explicit user confirmation). Quote the definition, it is the piece.**
**- ~26-30% overall; novice 15%; intermediate/expert 28-33%.**
**- Authors' limits carried in text: "We cannot measure real-world outcomes, like whether code written in a session is actually used or discarded thereafter" and "classifiers remain challenging to validate at scale."**
**- Selection caveat in text: measured INSIDE code-producing sessions, a population already self-selected into agentic tooling. Do NOT generalize to all knowledge work.**
**- "as of" freshness: the study window is Oct 2025-Apr 2026, published 16 Jun. Do NOT write "now" -- it is a measurement of a past window.**

---

Two out of every three times someone used the most instrumented AI coding tool on the planet, nobody could confirm anything worked.

Not that it failed. That nobody could confirm. Set that thought down next to every headline you have read this year about agents doing the work now, and the two of them cannot both be describing the same planet.

## Coming back to last Saturday, because I dropped this and walked on

Last Saturday I put that ratio in a paragraph, called it the honest floor under every "the agents do the work now" conversation, and then moved straight on to something else, because the something else was what the piece was about. It has now been sitting in the back of my head all week like a stone in a boot, aggravating me at the tail end of a long hike. So this is the Saturday where I stop and take the boot off.

Here is the study again, stated cleanly as our starting premise. In June, Anthropic published a look at roughly four hundred thousand of its own Claude Code sessions, from about two hundred and thirty-five thousand users, over the previous six months or so. It is the vendor measuring the vendor's product, which usually means the numbers arrive polished. These did not.

The number I want is what they call **verified success**, and the definition is the entire point, so I am going to quote it exactly:

> *judged success plus verifiable evidence -- git commits, passing tests, explicit user confirmation.*

That definition is doing all the work. Verified success is not "the agent produced something." It is not even "a classifier thought the user got what they asked for" -- that is the softer measure, which they call judged success and which runs higher. Verified success is that *plus* a receipt. Something outside the conversation that says yes, this worked: a commit that stuck, a test that passed, a human who said so.

By that measure, across everything, the number lands somewhere around twenty-six to thirty percent.

So call it seven in ten sessions where no receipt exists -- or was so ephemeral as to be non-existent. And I want to be careful and slow here, because the whole piece turns on what that seven-in-ten actually is.

## What the missing two thirds is not

It is not two thirds failure. That is the reading the number invites and it is wrong. We need to establish that first, because that's a great headline but completely inaccurate.

Some of it is failure, certainly -- the agent produced nonsense, or confidently wrong work, or a plausible thing that did not survive contact with reality. That bucket is real and you have all met it. But it cannot be the whole seventy percent, because the softer measure -- did the classifier think the person accomplished their goal -- runs meaningfully higher than the verified one. The gap between "looked like it worked" and "we can prove it worked" is enormous, and that gap is not failure.

That gap is the absence of a receipt.

Think about what has to be true for a session to count as verified. Somebody has to have committed the code, or written a test that runs, or stopped and said out loud that the thing was correct. Every one of those is a human doing a small deliberate act of confirmation. And what the number is quietly telling you is that most of the time, nobody does. The work comes back, it looks right, it gets used or pasted or shipped, and no receipt is ever generated -- not because the work was bad, but because nobody set up a way to check.

The missing two thirds is not mostly broken work. It is mostly **unconfirmed work.** And unconfirmed is a thing you can do something about, which is why this is a Saturday piece and not a funeral.

## The honest limits, because they are load-bearing

I am not going to hand you a number this heavy without the caveats the authors themselves put on it, because the caveats are half the value.

The first, in their words:

> *"We cannot measure real-world outcomes, like whether code written in a session is actually used or discarded thereafter."*

So the number cuts both ways. Some of the unverified sessions produced code that shipped fine and simply never got a receipt attached. And some of the verified ones produced a commit that got reverted on Monday. The study sees the receipt, not the reality behind it. It is measuring the paper trail, which is exactly the thing this whole week has been about.

The second, also theirs:

> *"classifiers remain challenging to validate at scale."*

They built machines to judge the output of machines, which -- and I said a version of this on Thursday -- is a hall of mirrors you should never fully trust. They know it. They wrote it down. I respect the study more for it, not less.

And the one they do not say loudly enough, so I will: this is measured *inside sessions that produced code*, among people who had already chosen to use an agentic coding tool. This is not a random slice of knowledge workers. It is the enthusiasts, the self-selected, the people leaning in. Which makes the twenty-six to thirty percent more sobering rather than less, because it is the number for the people trying hardest, not the number for everyone. 

## Why this is the most reassuring number of the week

Here is the turn, and I mean it as one.

For three weeks I have been describing controls that are not controls, instructions nobody reads, provenance nobody can establish. It is easy to come away from that thinking the machines are running ahead of us and we are jogging behind holding a clipboard nobody looks at.

This number says the opposite. It says that two thirds of the time, the machine did something and the thing that was missing was *a human closing the loop.* The scarce ingredient in the whole picture is not model capability. It is somebody caring enough to check, and having set up a way to. That is not a capability gap you wait on a lab to close. That is a habit, and you own it entirely.

Everything I asked you to do on Tuesday was, unknowingly, a way of manufacturing receipts. Decide in advance what would count as done. Set the metrics that provide the intermediate steps along the path to get to done. Don't write the check before you look; don't even just write the check at the end. Write the check at every meaningful step along the way (and keep the receipt of same) so that not only do you have the capacity to report your work later if needed (to governance, or regulatory, or your partner) but also so that you have the capacity to repeat the work, consistently, and even more importantly than *you*, the agents have the capacity to do the work within the limitations and qualifications that you have set. That repeatable infrastructure is where you go from a good idea to a solid process. And more material to the moment, that is not productivity advice. It is you personally converting an unverified session into a verified one, which is to say, moving work out of the seventy percent and into the thirty. You do not need permission, a platform, or a budget to do it. You need to decide that "it looks right" is not the same sentence as "it is right," which is a decision, not a skill.

Nearly forty years ago now I was working on a confidential document, for purposes of this example, let's call it an "intelligence brief." I was reviewing the work that had been done by a number of other people and I was getting ready to submit this brief myself. Now I was very young at the time. I was very new and quite confident in my own right but I was actually unsure about one of the things that someone else had cited that had made it into this brief. I went back through and started reading their sourcing on their piece of the brief. What they had was correct from the sourcing but it disagreed with what I had so that led me to then go back and source my own piece of this brief.  
  
As I worked back through my own sourcing, I realized that in one place, basically on a page turn, I had changed the meaning of something from the first page to the second page. Effectively inverted it just by sheer volume of what I was working on at the time. The brief was, I don't know, 40-some-odd pages long, which was a lot back then because we didn't have anything to generate the pages for us.  
  
In that situation the fact that I had my own receipts that I could use to foot out somebody else's receipts and ultimately find something that I had taken as a conclusion, eventually led to me rewriting about four or five pages of the brief to meet what the corrected intelligence said. It sort of very much proved to me that no matter how much I might think I have it right, the need to check my own work is always there. The only good way to check your own work, in my opinion, is to have the receipts, to have the evaluation, to know what qualifies as good, whether that's written down or you know it from experience, and to check what you've done against what you know is good.  
  
This is the exact same thing that you're doing with an AI, except the difference is that with the AI you're not necessarily doing all the grunt work. Even if something does twig in your mind without the receipts, you can't actually be sure whether what you've remembered is right or wrong.

## What I would do with this on a Saturday

**Pick one thing you shipped this week with an agent's help and go find its receipt.** Not the work -- the proof. The commit, the passing test, the moment you or somebody else confirmed it was right. If you can put your finger on it in under a minute, good. If you cannot, you have just found a session in the seventy percent that you thought was in the thirty, and that is worth knowing before something else does.

**Then pick the next thing before you start it, and decide the receipt in advance.** One sentence. "This is done when the test I am about to write passes." "This is done when the numbers tie to last month's." Written down before you see the output, for the reason I laboured on Tuesday: afterwards, the good-looking work has already recruited your judgment, and your judgment is exactly what you are trying to keep independent.

**And notice which of your work genuinely does not need a receipt, and leave it alone.** Not everything does. A first draft you are going to rewrite, a throwaway script, a summary you will read critically anyway -- forcing a ceremony onto those is how good advice turns into bureaucracy that everybody quietly ignores. The whole skill is telling the two apart: the work where "looks right" is fine, and the work where "looks right" is how the excessive transfer goes out the door. Most people have never sorted their week into those two piles even once.

## The number, one more time, pointed the useful way

Twenty-six to thirty percent is the floor. It is the vendor's honest measurement of its own product, on its most engaged users, and it is not going to leap to ninety because a better model ships -- because the thing keeping it low is not the model. It is the receipt, and the receipt is a human decision. If anything, knowing humans, I would expect this number to go lower in the future, not higher; but the *importance* of it in that environment will just grow.

Which means the number is not a verdict on the tools. It is a measurement of how few of us are closing the loop, and that is the most fixable finding I have run into in awhile. Tomorrow I want to pull the whole month together, because there is a single question underneath all of it and I think this number is the quiet answer to a piece of it. For today, the small version does the job.

Go find one receipt. Then go make one. Then do it again until the muscle is sharpened and its becoming a habit. You will be better for it and so will your outputs.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the vendor's own study shows verified success in only about a quarter to a third of sessions, that the missing two thirds is mostly unconfirmed work rather than failed work, and that the scarce ingredient is not model capability but a human deciding in advance what would count as proof.*
