---
type: intake
date: 2026-09-12
source_url: https://www.helpnetsecurity.com/2026/09/11/idscan-net-data-breach-153-million-drivers-licenses/
slack_permalink: none passed by the bot; #heinlein-briefs (C0BUVJE9A9M) thread 1789256028.291379, item reply 1789256074.185469
lars_note: "(none; the event text is item 5 of the 12 Sep cyber brief, echoed back by the bot, see Provenance)"
reactions: []
verdict: backgrounder
filed_to: Research Notes/intake/ only (no Signal, no thread line, no draft)
---

# IDScan.net confirms breach; seller claims 153 million scanned driver's licences

## Provenance

This did not come from Lars. The 12 Sep cyber brief posts its items as threaded replies through
Lars's own Slack connector ("Sent using Claude"), so the bot saw a reply from `lars_user_id` in
#heinlein-briefs and queued it as a Lars follow-up (dedupe key `C0BUVJE9A9M:followup:1789256028.291379`,
queued five times between 16:33:57 and 16:34:34). The headless prompt also arrived with the event
block missing (the claude.CMD newline cut). Both bugs are already recorded in the build memory
`heinlein-slack-control-plane`. The item text below was read from the bot's own queue file
`heinlein/bot/queue/C0BUVJE9A9M_followup_1789256028.291379.json`, not from Slack. No reaction from Lars
on it, so under the vault's flagged-items-only policy nothing was promoted.

## Extracted

Fetch FAILED: WebFetch was denied in this headless session and no Firecrawl tool was loaded. Nothing
below has been read at source. What follows is the brief's own summary (`Daily Briefs/brief_2026-09-12.md`
line 32):

- Help Net Security, 11 Sep 2026. Louisiana ID-verification firm IDScan.net says an unauthorised third
  party "may have accessed and/or copied" names and licence or government ID numbers from its cloud
  platform around 1 Sep.
- The 153 million figure is the dark-web seller's claim, not the company's. The seller also claims
  10 million ID cards, 3 million travel documents and 579,000 medical cards, US and Canada.
- Brief's take: venues that scan a licence at the door build a private copy of the state identity
  register and hand it to a vendor; the 2024 Outabox leak exposed licence sign-in data from patrons of
  "at least 17 NSW and ACT venues" [VERIFY: not checked against a primary]; retention and deletion
  belong in the contract.

## What changed since the 5 Sep test

`References/research_story-candidates_2026-09-05.md` section 4.1 tested this story and found:
"The company has issued no breach statement, ever", with the chain resting on Krebs (1 Sep), FBI
New Orleans confirming an investigation (2 Sep) and Louisiana lawsuits (4 Sep). **If the Help Net
Security wording holds at source, that line is now stale: the company has said access "may" have
occurred.** That is a hedged company statement, not a confirmation of scale. Read the 11 Sep article
before any draft relies on either version.

Still standing from that note, and the 12 Sep brief item respects both:
- Row 15: the 153 million is the seller's advertisement (separately advertised as 170 million, which
  contradicts it). No company figure.
- Row 14, REFUTED: "trusted to verify identity for millions of businesses". Not repeated here.

## Match

- Week plan 7-13 Sep: no IDScan, ID-scanning or KYC spine.
- Substack Scheduled / Published: nothing on IDScan. Nothing to contradict.
- Drafts (14 days), killed-claims files, corrections queue: no hit.
- Nearest thread hubs if Lars pins it: `Clubs - AML` (the venue scan-at-the-door and Outabox angle is
  that audience exactly) and `Trust Boundaries` (the vendor holds the scans; the victims never heard
  of the vendor).

## Lars's note

None. See Provenance.
