# Final-Review Skill — Pangram Feasibility & Integration Plan
**Researched:** 20 July 2026 | **For:** Writing Flow (proposed stage 4, between editor-panel and sign-off)

---

## TL;DR

A Pangram "final-review" pass is feasible and cheap, and it slots cleanly into the flow. Two things you should know before we build it:

1. **The only real obstacle is network.** Pangram has a clean API and a working Python SDK — I installed it and it runs. But every `pangram.com` domain is blocked at this cloud session's egress gateway (tested: GitHub and PyPI reach out fine; all Pangram hosts get reset). So a script running *here* can't call Pangram today. There are two ways around that (below).
2. **Pangram measures the wrong thing for your stated goal — and that's fine if we frame it right.** You want "consistent with my voice." Pangram doesn't measure voice; it measures *AI provenance* — "was a machine involved in producing this." Your drafts are Claude-assisted by design, so a faithfully-in-your-voice piece will often register as AI or AI-Assisted regardless of how much it sounds like you. That doesn't make the tool useless — it makes it a **third-party AI-slop detector**, an external number for the AI-Slop Allergist seat you already run. Used as a diagnostic (which paragraphs spike, did our edits move it) it's genuinely valuable. Used as a pass/fail gate it would punish your own honest writing.

Recommendation: build it as a **non-blocking diagnostic** that feeds the AI-Slop Allergist, and run it through **Claude-in-Chrome against pangram.com** (works today, no egress dependency, ~free at your volume). Keep the API path documented as the upgrade if you ever want it fully headless.

---

## 1. What Pangram actually offers

**API + SDK (confirmed working):**
- Python SDK: `pip install pangram-sdk` → `from pangram import Pangram`. Installed cleanly here (v0.3.1); exposes `Pangram` and `PangramText`.
- Auth: `x-api-key` header. Key is self-serve from your account's **API tab** after signup.
- Endpoints (SDK wrappers):
  - `predict(text)` — analyzes ~first 400 words, 1 credit. Good for a spot check.
  - `predict_sliding_window(text)` — splits a long doc into windows, 1 credit per 1,000 words. **This is the one for a full 1,400–2,400w piece** — it returns per-paragraph scores so we can see *where* the AI fingerprint lives.
  - `batch_predict([...])` — array in, array out.
  - `predict_with_dashboard_link(text)` — adds a shareable dashboard URL.
- Response fields: `ai_likelihood` (0–1, 1 = highly likely AI), `short_prediction` ("Human" / "Mixed" / "AI"), `prediction` (human-readable), `fraction_ai_content` (0–1), plus per-window objects with an `ai_assistance_score`, a `confidence` ("High/Medium/Low"), and character offsets so a flagged span can be located in the text. Pangram 3.0 adds an explicit **"AI-Assisted"** class.

**Cost — negligible at your volume:**
- Developer credits are pay-as-you-go, self-serve, **no subscription required**: starts at $25 for 500 credits; **$0.05 per 1,000 words** realtime ($0.04 bulk).
- One of your pieces ≈ 1,400–2,400 words ≈ **2–3 credits ≈ $0.10–$0.15 per final-review**. A year of daily pieces is a few dollars.
- Note the subscription tiers (Free 4 credits/day, Individual $20/mo, Professional $65/mo) **do not include API access** — only the pay-as-you-go Developer credits and Enterprise do. The Free tier *does* give 4 web checks/day, which matters for the Chrome path below.

## 2. The blocker: network egress (tested)

| Endpoint | Result from this cloud session |
|---|---|
| `api.github.com` (control) | HTTP 200 ✓ |
| `pypi.org` (control) | reachable ✓ (SDK installed) |
| `text.external-api.pangram.com` (API) | **HTTP 000 — reset at gateway** ✗ |
| `www.pangram.com`, `docs.pangram.com` | **HTTP 000 — reset at gateway** ✗ |

The TLS handshake terminates at Anthropic's `sandbox-egress-gateway`, which allows connections only to allowlisted domains and resets the rest. Pangram isn't on the allowlist. Two consequences:
- A Python/API skill **running in this cloud container cannot reach Pangram** until the domain is allowlisted.
- `device_bash` (your local machine) is **also** no help here — that environment has no outbound network at all (installs/fetches are explicitly pushed to the cloud container).

So the API path requires getting `*.external-api.pangram.com` (and `pangram.com`) added to the org's egress allowlist. Network access is an **org Owner** setting (Admin → Capabilities) on Team/Enterprise; on an individual account it may not be exposable at all. That's the gating question for the API route — worth checking your plan before committing to it.

The way around the whole problem: don't call the API from the sandbox. Use your **browser**, which has normal network.

## 3. Two build paths

### Path A — Claude-in-Chrome drives pangram.com (recommended, works today)
At the final-review step, Claude-in-Chrome opens `pangram.com` in your own Chrome, pastes the near-final draft, reads back the score and the per-section highlights, and writes them into a review note. 

- **Pros:** No egress/allowlist dependency. No API key to manage. Uses your logged-in account or the Free tier (4/day is plenty for one piece's final pass). Zero marginal setup.
- **Cons:** UI automation is more brittle than an API (a site redesign can break it). Slightly slower. The free web tier truncates very long inputs, so a 2,400-word piece may need to be checked in two halves.
- **Best when:** final-review happens while you're at the desk about to sign off — which is exactly when it happens.

### Path B — Headless API skill (cleanest, needs one unblock)
A Python script in the skill installs `pangram-sdk`, reads the draft `.md`, strips markdown to plain prose, calls `predict_sliding_window`, and writes a structured report. Requires either:
- (b1) `pangram.com` API domain **allowlisted** for this session's egress, **and**
- (b2) a `PANGRAM_API_KEY` available to the session (env var or a git-ignored key file — never committed, never written to memory).

- **Pros:** Fully headless, deterministic JSON, per-window scores with offsets, trivially loops on re-runs to show a delta. Best long-term ergonomics.
- **Cons:** Blocked until the domain is allowlisted (may not be possible on an individual plan); adds secret-handling; ~$0.10/piece.

*(Hybrid option: build the skill logic once against the SDK, and have it fall back to the Chrome path when the API domain isn't reachable. More work up front; most robust.)*

## 4. Where it slots in the flow

New **stage 4: final-review (detectability pass)** — after the editor panel clears the Voice bar (9.0) and slop is clean, before your sign-off. It does **not** gate publication and never overwrites; it produces a note and surfaces it to you.

```
… → 3. EDITOR PANEL (voice ≥ 9.0, slop clean, no open [VERIFY])
              │
              ▼
     4. FINAL-REVIEW (Pangram detectability pass)   ← NEW, non-blocking
        • overall ai_likelihood + short_prediction
        • top 3–5 highest-AI windows quoted w/ location
        • delta vs previous -rvN if re-run
        • hands findings to the AI-Slop Allergist lens
              │
              ▼
     LARS'S SIGN-OFF (final gate — always)
```

**How to read the output (the important part):**
- Treat it as an **AI-fingerprint diagnostic, not a verdict on voice.** A high overall score on a piece you're happy with is expected (it's Claude-assisted) — the *actionable* signal is the **per-window spikes**: the two or three paragraphs that score far above the rest are usually the ones with the tells (over-balanced "not just X but Y" cadence, tidy tricolons, hedged transitions) — exactly what the AI-Slop Allergist hunts. We revise *those*, toward your voice, not toward the detector.
- **Track movement, not the absolute.** The useful metric across a revise loop is "did the humanizing pass lower it, and did the spiky windows come down." Chasing a fixed "X% human" target would optimize for beating a detector rather than sounding like you — and would routinely flag your genuinely-human passages (see caveats).
- **Never a hard gate.** Your sign-off stays the only gate. Pangram is one more input to it.

## 5. Reliability caveats (so we use the number honestly)

- **Pangram is genuinely top-tier.** Self-reported 99.98% accuracy / 0.01% false-positive; an independent aggregator (DetectArena) ranks it at the top (Elo ~1555), strongest on academic and technical prose. It's about the best detector to pick.
- **But the accuracy is largely self-reported**, and independent blind data on *edited/hybrid* human-AI text — which is exactly what your pieces are — is thin.
- **Detectors systematically flag polished human writing as AI** (well-documented "built-in paradox," 2026 studies). Your voice is deliberately crafted; expect false alarms on passages you wrote yourself.
- **It answers provenance, not fidelity.** "Was a machine involved" ≠ "does this sound like Lars." Only the editor panel's Voice Score speaks to the second. Keep them in separate columns.

## 6. What it would take to build (either path)

**Path A (Chrome):** a `04_final-review.SKILL.md` in `Writing Flow\` + one project-memory reference note; the skill orchestrates Claude-in-Chrome (open pangram.com → paste → read result → write `Writing Flow\final-review_<slug>_<date>.md`), then hands the spikes to the AI-Slop Allergist. ~half a day of build + a test run on an existing draft (e.g. `bring-it-home`). No credentials, no cost.

**Path B (API):** same skill file + a small Python module (`pangram_check.py`) using `pangram-sdk`; requires the egress allowlisting and a stored `PANGRAM_API_KEY`. Add a reachability preflight so it fails gracefully to Path A if the domain is blocked.

**Common to both:** update `00_WRITING_FLOW.md` to add stage 4 to the chain diagram and the "stage skills" list; add a memory note so it auto-triggers ("run the final review", "check this for AI", "run pangram on <draft>"); wire the output into the editor-panel's AI-Slop Allergist seat so a re-run after edits shows the delta.

## 7. Decision for you

The one fork that changes what I build: **which path.** Path A (Chrome) works today and is free; Path B (API) is cleaner but needs the Pangram domain allowlisted for the session — possibly an org-plan limitation. My recommendation is to build **Path A now**, structured so we can drop in the API later if/when egress allows.

*Everything above is tested from this session except the accuracy figures (vendor/DetectArena self-reported) and the egress-allowlist admin path (depends on your plan).*
