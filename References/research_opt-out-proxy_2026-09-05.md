# Research Note -- Somebody Else Holds Your Opt-Out
For: Tue 8 Sep, `substack_draft_opt-out-proxy_2026-09-08` (unwritten) · Depth: deep · Date: 2026-09-05

## Bottom line

Both halves verified at their primaries today. The spine moved substantially since the 11 Aug
record, and it moved in the piece's favor -- except for one framing the plan carries that is now
flatly wrong on mechanism and would have shipped wrong. **The Compliance API does not reach the
laptop.** It records the API traffic the client was already sending. Anthropic says so in writing,
and a technical reader will catch the other version. The four-week-old Twitch geo `[VERIFY]` is
settled as a documented absence, verified across four independent paths, and no longer blocks
Scheduled. Twitch has also expanded its own text since 14 Aug, which retires the weakest-sourced
line in the plan and replaces it with a primary that is better.

---

## ★★ THE CORRECTION -- the plan's framing is wrong on mechanism

The 24 Aug block reads *"Anthropic's Compliance API reaches the laptop"* and *"reaching onto
personal hardware."* The current documentation states the opposite mechanism explicitly:

> "For local sessions, Anthropic records each conversation server-side as its requests reach the
> Claude API; nothing is installed on the device, and nothing is collected beyond the requests the
> client already sends to the Claude API."
> -- [Retrieve session transcripts](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)

Nothing reaches onto the hardware. There is no agent, no endpoint install, no device inspection.
The FAQ repeats it independently: *"Local sessions are captured as their requests reach the Claude
API, so nothing is installed on the device, and on-device activity that never reaches the API is
not captured."*

**The honest framing, and it is still sharp:** the sessions that run on your own machine are
captured, but by recording what left the machine. "Local" names where the session runs, not where
the capture happens. The piece is stronger for the precision -- the reader who thinks the danger is
an agent on the endpoint is looking at the wrong thing, and the actual mechanism is quieter.

The honest-limit quote is **confirmed verbatim** and belongs in the piece as the counterweight:

> "Local session transcripts show what Claude was asked to do and what it returned, not what
> happened on the device."

---

## ★★ THE BEST NEW FACT -- and it is the thesis in one sentence

**You can delete the session that ran in the cloud. You cannot delete the one that ran on your own
machine.**

- Remote (cloud) sessions: *"retained for 6 years, unless a user deletes the session sooner. The
  remote session endpoints no longer return a session once a user deletes it, and its transcript is
  not recoverable through the Compliance API."*
- Local sessions (your machine): *"The session endpoints are read-only; local and remote sessions
  cannot be deleted through the Compliance API."* And there is no user-side path either. For Claude
  for Microsoft 365 specifically: *"deleting a conversation in the add-in happens only on the
  client, so it is not reflected in the API: local sessions have no `deleted_at` field, and the
  session stays listed until retention removes it."*

Deleting it on your own screen deletes the thing you can see. The record is somebody else's. That
is the proxy, in the reader's own hands, and it is a better spine fact than the six-year tail.

---

## What is solid

**Anthropic Compliance API** -- all from [compliance-sessions](https://platform.claude.com/docs/en/manage-claude/compliance-sessions),
[compliance-faq](https://platform.claude.com/docs/en/manage-claude/compliance-faq),
[compliance-api](https://platform.claude.com/docs/en/manage-claude/compliance-api),
[compliance-integration-patterns](https://platform.claude.com/docs/en/manage-claude/compliance-integration-patterns).

- **Endpoints, confirmed.** `GET /v1/compliance/apps/sessions/local` (list),
  `/local/{session_id}` (metadata), `/local/{session_id}/messages` (transcript). Read-only. Admin
  API keys get 403; only a Compliance Access Key with `read:compliance_user_data` works.
- **★ SCOPE HAS EXPANDED WELL BEYOND THE 11 AUG RECORD.** Local session capture now covers Cowork
  in Claude Desktop, Claude Code (terminal, desktop, IDE extension), the Claude Science desktop
  app, **and Claude for Microsoft 365 -- the Claude add-ins for Excel, PowerPoint, Word and
  Outlook.** The Office suite is in scope. That is a materially bigger story than August's.
- **★ NO LONGER BETA, and the piece must not say so.** *"The local and remote session endpoints
  are stable for Cowork and Claude Code sessions; coverage of Claude Science and Claude for
  Microsoft 365 sessions is in beta."* Stable for the two that matter; beta only for the two newest.
- **Enablement condition, confirmed.** *"Capture of local sessions is tied to the Compliance API
  being enabled for your organization and applies while users are signed in with their Claude
  Enterprise account."* Enablement is by the primary owner and **cascades** from the parent
  organization to every linked organization.
- **Retention, and it is more interesting than "six years."** *"Captured local session content is
  stored for 6 years from capture by default"*, or the organization's custom conversation retention
  period when a finite one is set, *"whether it is shorter or longer than the default"*; where an
  organization has several configured, **the shortest applies**. And it ratchets one way:
  *"the endpoints stop returning activity older than the organization's current period as soon as
  the setting changes, whereas each captured message is stored for the period that was in effect
  when it was captured, so lengthening the period later does not restore content that has already
  expired."*
- **★ "Nothing masks URLs, credentials, or personal data in that content, so treat transcripts as
  sensitive."** Anthropic's own instruction to the reviewer. Drop-in.
- **Not captured, confirmed and slightly expanded.** Claude Code under a Console API key; Claude
  Code via Bedrock, Google Cloud or Microsoft Foundry; **Claude Code on the web** (new to the
  record); organizations with HIPAA readiness (no local session data at all); sessions under zero
  data retention (excluded from lists, 404 on retrieve).
- **Transcript omissions, confirmed and expanded.** Thinking blocks *"are never included."* The
  system prompt *"is never returned"*, replaced by a `[system prompt content not shown]` marker.
  Tool definitions and MCP server configuration are not in the transcript. Images, PDFs and other
  binary blocks appear as `[image content not shown]`. Citation metadata is omitted.
- **★ `CLAUDE.md` and skills are in the transcript.** *"Project instruction files such as
  `CLAUDE.md` appear as ordinary user-role content. Skill content appears when the client sends it
  as message content and is not distinguished from other user text."*
- **★ The most candid line in the doc set, on the `not_captured` reason:** *"It does not prove that
  no record was stored: content that Anthropic's data-handling policies withhold from the
  Compliance API is reported with the same reason."* An absence in the compliance record is not
  evidence of an absence in the store. Note the rhyme with the standing absence-verification rule.
- **Tool content is truncated by default** to 10,000 bytes per tool input and per tool-result text
  entry; raisable to about 1 MiB on request. The default record is a partial one unless someone
  asks for more.

**Twitch** -- from the [account settings help article](https://help.twitch.tv/s/article/twitch-account-settings?language=en_US),
the [Privacy Notice](https://legal.twitch.com/en/legal/privacy-notice/) and the
[Privacy Choices page](https://legal.twitch.com/legal/privacy-choices/), all read in the browser
today (WebFetch cannot render the help portal; do not trust a fetch of it).

- **★ THE DELEGATION SENTENCE, confirmed verbatim, unchanged:** *"If you chat on someone else's
  stream, their opt-out preferences govern if that chat can be used for training."*
- **Scope sentence, confirmed verbatim:** *"Your stream and the stream's chat, your VODs, your
  Clips, Highlights, and any text or images on your Channel may be used."*
- **★ THE SETTING TEXT HAS GROWN SINCE 14 AUG.** It now reads: *"Allow your channel content to
  train generative AI content models at Amazon. Turning this off does not opt you out of Twitch and
  Amazon using your channel content for other purposes described in the Twitch Privacy Notice,
  including using AI-supported Twitch features that benefit the community by facilitating streamer
  growth and monetization (such as real-time sponsorship campaign assistance), viewer discovery
  (such as recommendations), and community safety (such as AutoMod)."* Everything after the first
  sentence is new to the record, and Twitch has added a five-question FAQ alongside it.
- **Prospective only, confirmed, with better wording than the old note carried:** *"your streams,
  VODs, clips, stream chats, and pictures and text on your channel will not be used in future
  training of a model developed by Amazon whose purpose is to generate or synthesize text, audio,
  images, or video."*
- **★ THE DOCUMENTATION GAP HOLDS, AND IS NOW WORSE.** The Privacy Choices page -- the page the
  Privacy Notice points to for your privacy options -- still reads **"Last modified on
  05/17/2023"**, three years and four months stale. Verified programmatically against the fully
  rendered 12,571-character body: **zero occurrences of "generative", zero of "train", zero of
  "AI".** The most consequential new choice is still absent from the canonical choices document,
  sixteen months after the practice and three weeks after the toggle.
- **The Privacy Notice never names generative-AI training either.** Last modified 08/12/2026;
  29,392 characters; a programmatic search returns **no occurrence of "generative"** and exactly
  one weak "train" hit, inside the generic operations clause (*"operate, maintain, enhance,
  provide, create, and develop all of the features, functionality, and services"*). The permission
  the toggle governs is described in the Notice only in general terms.

---

## ✅ THE OPEN [VERIFY], SETTLED -- Twitch geo treatment

**Resolution: a documented absence. Twitch documents no geographic carve-out and no differing
default for the EU, the UK or Australia. The flag no longer blocks Scheduled.**

Four independent paths, because a single failed or truncated fetch is not evidence of absence:

1. **Help article, en_US.** Full text render, complete from Profile through the closing FAQ. No
   occurrence of any geographic term in connection with the setting.
2. **★ Help article, en_GB.** The locale-parameterized variant is the sharpest test available, and
   it serves **identical** setting text. A UK-locale reader is shown the same words.
3. **Privacy Notice, programmatic full-body search** of the rendered 29,392 characters. No
   "generative" anywhere; no EEA, no "European Economic Area", no "United Kingdom"; the single
   Australia hit is a **minimum-age** provision (16 in Australia), unrelated to training.
4. **The Notice's own "Additional Information for Certain Jurisdictions" section** -- where a
   carve-out would live if one existed. It contains only representative designations (Twitch UK
   Limited under UK GDPR; Twitch Interactive Germany GmbH for the EU), and pointers to the
   State-Specific and Japan disclosure pages. **No AI-training content of any kind.**

Legal bases are described generically and are never attached to the training use: *"Twitch will
rely on legal grounds to process your personal information to the extent permitted by applicable
law"*, including *"legitimate interests."*

⚠️ **THE HONEST LIMIT, AND IT MUST TRAVEL INTO THE DRAFT.** Absence of documentation is not proof
the product behaves identically in the EU. What is verified is that **Twitch does not document a
regional difference**, which is itself the finding and is arguably the better one. Write the
absence: *Twitch's own documentation describes no geographic exception.* Do **not** write that
EU/UK/AU users get the same default -- that would need the settings UI on an account in-region,
which is unreachable from here. **Unreached:** the Japan Privacy Disclosures and State-Specific
Privacy Disclosures sub-pages, and the in-product settings view for a non-US account.

---

## What is contested / watch out

- **"Began by default" is still the wrong tense, and his own brief carries the error.** The
  14 Aug AI brief entry reads *"Twitch began feeding user-generated content ... by default."* The
  toggle is new (~12--13 Aug 2026); the Privacy Notice permission predates it. **The change is the
  addition of a control, not the start of the practice.** Do not reuse the brief's framing.
- **"May be used" throughout.** Twitch nowhere states content **has been** used. Write "permits
  itself to," never "is training on."
- **★ RETIRE THE CPO QUOTE.** The plan flagged *"If it was opt in, nobody would opt in. That's
  honestly the answer"* as the weakest-sourced thing in the piece -- press reporting of a
  livestream, not a Twitch document. **It is no longer needed.** Twitch's own new FAQ makes the
  argument better, on the record, at a primary. See drop-in facts below.
- **Vendor interest, name it in the text.** Amazon owns Twitch and is the beneficiary of the
  training. Anthropic is the vendor whose compliance product the spine describes, and this pipeline
  runs on it. The self-reference clause is licensed once, briefly -- it ran Mon 17, so this is the
  second and a third would be a tic.

## Couldn't verify

- **Any user notification, consent, or opt-out for Compliance API capture.** Searched four fully
  rendered Anthropic doc pages (sessions, FAQ, API overview, integration patterns). **None contains
  any guidance about notifying, informing, or obtaining consent from the end users whose sessions
  are captured** -- while the same pages carry detailed guidance on SIEM correlation, legal hold and
  chain of custody. ⚠️ **Calibrate this honestly in the draft.** These are administrator-facing
  documents, so "the documentation describes no user notification, consent or opt-out path" is
  precisely true and is the sentence to write. "There is no consent" is not established: notice
  obligations fall on the employer under local law, and are outside Anthropic's docs by design.
  That distinction is the difference between a claim that holds and one a privacy lawyer writes in
  about.

## The economics

There is no price tag on either instrument, and that is the point worth making. The Compliance API
carries **no new key, no new scope, no new setting and no client update** -- *"no new key, scope,
setting, or client update is required."* The capability arrives inside a product the organization
has already bought, and is switched on by one person: the primary owner, cascading to every linked
organization. The marginal cost of extending six-year retention across Excel, Word, Outlook and
PowerPoint sessions is a toggle. On the Twitch side the asymmetry is the same shape: opting out
costs a viewer nothing and is unavailable to them, while the party who *can* exercise it -- the
channel owner -- carries the growth and monetization incentives Twitch names in the setting text
itself. **The control is free and it is held by the party with the least reason to use it.**

## Drop-in facts (each verified at a primary today)

- "If you chat on someone else's stream, their opt-out preferences govern if that chat can be used for training." [Twitch help](https://help.twitch.tv/s/article/twitch-account-settings?language=en_US)
- "Your stream and the stream's chat, your VODs, your Clips, Highlights, and any text or images on your Channel may be used." [Twitch help]
- ★ "Some of it runs the service itself, the same way our servers and our code do. Some of it keeps the service secure. And some of it, like AutoMod, protects the whole community. Turning those off for one person would weaken safety and security for everyone else on the platform, so they are not individual settings." [Twitch help, FAQ: "Why can't I opt-out of all AI uses at Twitch?"] -- **use this instead of the CPO quote. It is a primary, it is more honest, and it concedes more than the paraphrase did.**
- "Local session transcripts show what Claude was asked to do and what it returned, not what happened on the device." [Anthropic]
- "For local sessions, Anthropic records each conversation server-side as its requests reach the Claude API; nothing is installed on the device." [Anthropic]
- "The session endpoints are read-only; local and remote sessions cannot be deleted through the Compliance API." [Anthropic]
- "Remote session transcripts are retained for 6 years, unless a user deletes the session sooner." [Anthropic] -- the delete asymmetry
- "Captured local session content is stored for 6 years from capture by default." [Anthropic]
- "Nothing masks URLs, credentials, or personal data in that content, so treat transcripts as sensitive." [Anthropic]
- "It does not prove that no record was stored: content that Anthropic's data-handling policies withhold from the Compliance API is reported with the same reason." [Anthropic]
- "Last modified on 05/17/2023" -- the Twitch Privacy Choices page, today. [Twitch legal]

## Angles this opens

- **Chain of custody is un-burned** (Sun 30 never ran; Sun 6 used the tether instead) and Anthropic's own integration guidance hands it over: *"For chain of custody, store the exported records with provenance metadata: source endpoint, query parameters, run timestamp, and a content hash of each record."* A bench candidate, not a Tuesday beat -- Tuesday is short and operational.
- **The `not_captured` line rhymes with the 5 Sep absence-verification finding**: a negative in a record is not evidence of absence. Same shape, different domain. One clause at most; do not build on it, it belongs to the methodology memory rather than to this piece.
