# Research note -- Sat 26 Sep 2026 -- "Ten, Then Five, Then Stop" (attention layer, layer one)

Written 24 Sep 2026 by the Sat 26 day chat. All primaries fetched 24 Sep 2026 unless stated.
Input material (his): Codex transcript "Prototype Teams catch-up app" (24 Aug 20:47 PT to 27 Aug 18:43 PT; UTC 25-28 Aug), PR bodies "android-controlled-actions" and "android-release-readiness", the Slack radar-hub paste (16 Aug).

## Footed

| Claim in draft | Verdict | Primary |
|---|---|---|
| Graph `markChatReadForUser`, delegated Chat.ReadWrite, no application permission, 204 on success | VERIFIED | learn.microsoft.com/en-us/graph/api/chat-markchatreadforuser?view=graph-rest-1.0 |
| Unread = compare last message preview `createdDateTime` with `viewpoint.lastMessageReadDateTime`, and Microsoft says so | VERIFIED ("allows the caller to determine whether the user has read all messages in a chat", chat-list Example 4) | learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0 |
| Channels: no per-user read marker, no mark-read | VERIFIED by absence in the v1.0 channel and chatMessage resource pages (beta not checked). An absence finding, so the draft words it as "no way to mark one read from outside", not "never" | learn.microsoft.com/en-us/graph/api/resources/channel?view=graph-rest-1.0 |
| Work/school only, personal MSA not supported | VERIFIED ("Delegated (personal Microsoft account) Not supported") | same two pages |
| Chat.ReadWrite does not need admin consent | **PARTLY. Draft carries it with the caveat.** Permissions reference: AdminConsentRequired = No. But MC1163922 (Microsoft-managed default consent policy, from late Oct 2025) means third-party apps reaching Teams chat content typically need admin approval. Footed only via a Microsoft Q&A answer: learn.microsoft.com/en-us/answers/questions/5572742/clarification-on-mc1163922 -- **[VERIFY] in draft until re-read at a Microsoft Learn / message-center primary** |
| Google Play internal testing, up to 100 testers | VERIFIED | support.google.com/googleplay/android-developer/answer/9845334 |
| Google Play registration US$25 one-time | VERIFIED | support.google.com/googleplay/android-developer/answer/6112435 |
| Apple Developer Program US$99/yr | VERIFIED | developer.apple.com/support/enrollment/ |
| Azure Static Web Apps has a Free plan for personal projects | VERIFIED (Free plan, 100 GB bandwidth, "hobbies/personal projects") | azure.microsoft.com/en-us/pricing/details/app-service/static/ |
| Glance widgets can be interactive (so read-only was a choice) | VERIFIED (Action classes, actionRunCallback etc.) | developer.android.com/develop/ui/compose/glance/user-interaction |
| Teams has recaps for meetings but no unread-chat catch-up | PARTLY: intelligent recap is meetings-only and on mobile; no official unread-chat catch-up found. Draft says "for the ordinary pile of unread chats there is no catch-up view" -- an absence claim from a search, so keep it at that strength | learn.microsoft.com/en-us/microsoftteams/intelligent-recap-calls-meetings |
| Slack Catch Up widget exists on iPhone | VERIFIED as existing (iOS release notes mention "our Catch Up widget"); what it shows is NOT footed at Slack, but Sat 19 already printed his own screenshots, which is his first-hand account | slack.com/release-notes/ios ; slack.com/help/articles/226410907 |
| Codex = OpenAI's coding agent | Common knowledge; his own tool. Fine as gloss |

## From his own material (his first-hand, not footed externally)

- Timeline: first message Mon 24 Aug evening PT; Play internal release installed and "all looks good" Thu 27 Aug evening PT. "Three evenings" is fair; twelve PRs ("a dozen saved checkpoints").
- His rules, his words: 10 then "Load 5 more", 15 max; refresh "every couple of hours"; 30/45 days proposed by him then cut to 15 by him; fireworks and "Caught up!" his ask; "If I'm going to do it, I'd rather sit down on Teams and do it."
- Empty-list bug (paged all history when zero unread): found by him; fixed with a three-page (~150 chat) ceiling. Not printed as a number.
- "Anything older belongs in Teams search, not in a pop-up" is the ASSISTANT's line in the transcript, used in the draft in his narration. Flag at his edit pass; he may want it attributed or reworded.
- Mark-read safety: confirmation, exact-204 advancement, no double tap, reconcile on uncertain lifecycle (Fold posture), refresh-before-mark race (raised by the assistant on day one), widget holds no token and no write control. All from the PR body and transcript.
- Live acceptance: one Lars-picked non-critical chat, eight checks passed ("it does all work properly for these 8 items").
- Tester list: Play defaulted to an existing 13-user list; assistant stopped and asked; a one-person list was made.
- Summaries: generated locally in the web POC and in the Android live-read plan. **[VERIFY] in draft**: confirm the shipped Android build still summarizes on-device.
- Slack radar hub (16 Aug): hub fell back to another radar because the 19-entry config was published into a path IIS was not serving (incomplete security-gate cutover); the assistant declined to republish into the old anonymous share because it would bypass the gate. Written generically, no names.

## DO NOT PRINT

- Employer name (never named in any published piece), the Entra app name, the package name, the logo description beyond "black and gold".
- Any chat title or customer/venue name from the transcript (the test chat names a customer site and a WAN).
- Tenant, client, user IDs; signature hash; device-code strings.
- Internal hostnames, share names and paths from the radar paste; the Azure Static Web Apps URL; the Play internal-test link; any email address, including the Play account.
- PR numbers and commit hashes (a count is fine).
- The 13-person tester list's name.

## Window check (Sat 19 to Fri 25)

- Spent and avoided: concierge / front desk / hotel (Sat 19); "Read ... again" (Wed 23, Thu 24); "Here is how you build yours" and "Take the shape" (Sat 19 headers/phrasing, renamed here); "nobody" headers; "load-bearing".
- Deliberate callbacks to Sat 19: the Slack widget and the 45; "fatigue ... field of view" (quoted as last week's line in the close).
- Controlling image here: the bouncer (door, list, limit, closing time). Not used in the window as far as checked by grep of Published/Scheduled 19-25 Sep: re-run before panel.
