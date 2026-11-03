## Summary

- add a full-width **Open in Teams** action using only opaque Graph-provided chat or message URLs
- add confirmation-protected **Mark read** with exact-204 advancement, duplicate-tap protection, and failure preservation
- carry the MSAL tenant and signed-in Graph user identity into the write request without storing tokens or raw messages
- retain the pending/uncertain write coordinator across Fold posture and configuration recreation without retaining an Activity
- key first-write confirmation to the authenticated account and reset it on every session exit
- keep the Glance widget read-only and document the controlled Fold acceptance procedure

## Integration

PR #9 is merged. This PR now targets `main` and contains only the controlled Android navigation, write-safety, lifecycle, testing, documentation, and acceptance changes that followed the live-read foundation.

## Safety boundary

- automated Graph transport tests use MockWebServer only
- no live Teams write is automated or has been performed for this PR
- Lars selects and confirms one non-critical chat on the Fold for final acceptance
- only `204 No Content` advances the review session; any other status preserves the card
- a blank tenant ID refuses the write without calling Graph
- pending writes cannot be cancelled or overtaken by Refresh, Later, Load more, or Sign out
- uncertain lifecycle outcomes require reconciliation before retry or navigation
- the widget contains no token, Graph client, or write control

## Verification

- `npm run build` — passed
- `npm test` — 25 passed
- `npm run test:e2e` — 4 passed
- `:shared:testAndroidHostTest` — passed
- `:androidApp:testDebugUnitTest` — passed
- `:androidApp:compileDebugAndroidTestKotlin` — passed
- `:androidApp:assembleDebug` — passed
- independent code review — approved after lifecycle, cancellation, post-204, confirmation, and launcher findings were fixed
- connected Fold Compose suite — passed on Samsung SM-F946U; reviewed APK reinstalled successfully afterward
- non-mutating **Open in Teams** navigation — passed; returning preserved the current card
- one Lars-selected non-critical live **Mark read** — passed through confirmation, pending state, success-only advancement, refresh reconciliation, Teams read state, and read-only widget regeneration

## Acceptance

Completed on 2026-08-27 using the Samsung SM-F946U. The live product checks continued successfully over the phone's network after USB was disconnected. No chat title, URL, message content, token, or response body was captured.
