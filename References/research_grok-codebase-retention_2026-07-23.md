# Research Note — The xAI / Grok Codebase-Retention Incident (July 2026)
For: Monday "Fifty Agents" rv3 Grok anecdote · Depth: verification (named-vendor allegation) · Date: 2026-07-23

## Bottom line (4 sentences)
The story is **real and well-documented** -- Lars can keep the beat -- but rv3's version fuses two different xAI stories and overstates on three specifics, and a CISO reader would catch each. What actually happened: xAI's OWN coding CLI (**Grok Build**, not Cursor) uploaded users' **entire git repositories** -- full history, unopened files, and unredacted `.env` secrets -- to an xAI cloud bucket, and it kept doing so even when the "improve the model" toggle was OFF. The proven victims were **default/individual CLI users**; enterprise zero-data-retention (ZDR) accounts were explicitly carved out and unaffected. Musk posted that all previously uploaded data would be "completely and utterly deleted," and xAI killed the upload, flipped retention off, and open-sourced the tool within a day or two.

## Verdict: CONFIRMED-BUT-OVERSTATED
Three corrections rv3 needs before it can ship:
1. **It was Grok Build (xAI's own CLI), NOT Cursor.** Cursor is a *separate, conflated* thread (see below).
2. **The proven victims were individual/default CLI users, NOT enterprise customers.** Enterprise ZDR was the one group explicitly said to be safe -- so "adopted enterprise wide → got siphoned" inverts the actual risk population unless Lars knows his friends ran the default (non-ZDR) CLI.
3. **"Kept copies for any reason at all" is half-right.** What's *proven* is that retention was decoupled from the training toggle (turning off "improve the model" didn't stop uploads). The non-training *purpose* (session traces/debugging/analytics) was never established -- so don't assert "for any reason at all" as fact.

## What actually happened (primary sources)
- **~14 Jul 2026:** a security researcher publishing as **cereblab** posted a wire-level analysis + a reproducible mitmproxy harness showing **Grok Build CLI v0.2.93** uploaded a git bundle of the *entire repository* -- commit history, files the model never opened, and unredacted `.env` secrets (API keys, DB passwords) -- to a Google Cloud Storage bucket named `grok-code-session-traces`, via `POST /v1/storage`.
  - Repro repo: https://github.com/cereblab/grok-build-exfil-repro · wire gist: https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
- **The proof, two ways:** (1) prompted "reply OK, do not open any files," Grok still shipped the whole repo -- on one test the storage channel moved ~5.1 GB while the model channel used ~192 KB (a ~27,800x gap), proving upload was decoupled from what the model read; (2) a planted canary file the agent was told not to open was recovered verbatim from the intercepted bundle.
- **The toggle failure:** disabling "Improve the model" did NOT stop uploads; the server still returned `trace_upload_enabled: true`. Retention operated independently of training consent. Only `.gitignore` entries kept files out.
- **What is NOT proven (cereblab is explicit):** "Upload/storage ≠ training. We did not prove xAI trains on this data." The proof is transmission + durable storage, not training use.
- Secondary write-ups: [The Hacker News](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html) · [Simon Willison](https://simonwillison.net/2026/Jul/15/grok-build/) · [cybernews](https://cybernews.com/ai-news/grok-build-git-repository-upload/) · [The Register (open-sourcing after the furore)](https://www.theregister.com/ai-and-ml/2026/07/16/spacex-open-sources-grok-build-after-data-retention-furore/).

## What Musk / xAI actually said
- **Musk on X, ~13 Jul 2026 (via outlet transcription):** *"True. As a precautionary measure, all user data that was uploaded to SpaceXAI before now will be completely and utterly deleted."* Cited by [Neowin](https://www.neowin.net/news/elon-musk-says-spacexai-will-delete-all-grok-build-user-data-following-privacy-concerns/); X link (verify live before print): https://x.com/elonmusk/status/2076739687658496209
- **xAI's actual remedy (not just a tweet):** disabled the codebase upload server-side, flipped the retention default OFF for all users, added a `/privacy` command, said all retained coding data was deleted, and open-sourced the Grok Build harness (Apache 2.0), ~15-16 Jul.
- **The carve-out:** "Enterprise teams on zero data retention never have code stored." xAI did not dispute cereblab's technical findings; it changed behavior within hours.
- **Name note:** Musk says "SpaceXAI" because SpaceX reportedly acquired xAI in Feb 2026; the combined entity ships Grok Build. Write "xAI (now SpaceXAI)" if readers won't know.

## The conflation to keep straight
Lars's rv3 fuses TWO July-2026 xAI code-data threads:
1. **The proven incident** -- Grok Build CLI uploading/retaining whole repos (above).
2. **A separate, unproven boast** -- ~28 Jun 2026, Musk claimed Grok 4.5 was trained on xAI's foundation "with Cursor data added in supplemental training" -- a vendor-stated flywheel claim, not a security finding ([context](https://www.digitalapplied.com/blog/grok-4-5-cursor-data-flywheel-spacex-private-beta-2026)). This is almost certainly where "Cursor" entered the anecdote. Keep the two apart -- the Cursor angle is the weak, unverified one; the Grok Build angle is the strong, reproducible one.
- Other adjacent episodes whose vocabulary could bleed in (none is this story): Grok chats indexed by search engines; xAI system-prompt leaks; the xAI API-key-on-GitHub leak; Grok safety/output blowups.

## Safe-to-print version (general framing, if Lars wants to cite the incident directly)
> "In mid-July 2026 a security researcher demonstrated, with a reproducible wire capture, that xAI's Grok Build coding CLI uploaded users' entire git repositories -- full history, files the agent never opened, even unredacted `.env` secrets -- to an xAI cloud bucket, and kept doing it even with the 'improve the model' setting switched off. The researcher was careful: he proved the code was uploaded and stored, not that xAI trained on it. xAI killed the upload within hours, turned retention off by default, and open-sourced the tool; Elon Musk posted that everything already uploaded would be 'completely and utterly deleted.' Enterprise customers on zero-data-retention were never affected."

**If Lars keeps the personal anecdote about his friends:** the anecdote is his to tell on what he directly knows, but for it to be defensible he should (a) drop "Cursor" as the culprit (name Grok Build, or just "their Grok coding agent"), (b) not imply enterprise ZDR customers were hit -- if his friends were exposed, it's because they ran the default CLI, which is the whole point (rolling it out "enterprise wide" on the default config is exactly the exposure), and (c) swap "kept copies... for any reason at all" for something like "kept copies on xAI's servers -- and kept doing it even with model-training turned off." That last change actually *sharpens* his wall metaphor: the siphon ran regardless of the setting everyone assumed protected them.

## What to cut / fix in rv3
- **Cut "Cursor"** as the retainer -- it was Grok Build (xAI's own CLI). (Cursor only appears in the separate, unproven training-boast thread.)
- **Don't imply enterprise ZDR customers were siphoned** -- they were the exempt group.
- **Cut "for any reason at all"** -> "even with model-training switched off" (provable, and stronger).
- **Attribute the delete quote to Musk's X post** and re-verify the live post before publish (day-level dates vary across outlets; reporting clusters 12-16 Jul).
- No hard affected-user count was published -- don't cite one.

## Angles this opens
- The incident is a *near-perfect* illustration of Monday's thesis and Tuesday's exhaust argument: the third party with access to the building kept copies regardless of the toggle the customer trusted -- "you can't point to the system that would have denied it" (Friday's runtime-control piece) and "the vendor learns your operating model whether you consented or not" (Tuesday). Worth a callback flag in the Tuesday/Friday drafts.
- Also a clean data point for the FDE / vendor-dependency thread: when the vendor's own tooling sits inside your repo, provenance and exit-planning stop being abstract.
