# Handoff — add Firecrawl as a custom MCP server

**Created:** 2026-07-21 · **Owner:** Lars · **Status:** Not started

## Why

Discovery is not the bottleneck — native web search found the Forbes FINRA piece, the APRA
standard and the PwC release without trouble on 20 July. **Extraction** is the bottleneck. Two
fetches that day returned 62,294 and 81,195 characters of navigation chrome, blew the context
limit, and forced a fall back to grepping saved files instead of reading them. Firecrawl
returns clean markdown and renders JavaScript, which also fixes the client-rendered AI Daily
Brief page the AI brief task fails on most mornings.

Tavily was considered and **deferred**: it is a search-and-summarise API, and it would
duplicate a capability that already works. Revisit only if discovery starts failing.

## Cost expectation

- Hobby: **$16/mo, 3,000 credits**; core scrape/crawl/map = 1 credit per page.
- At ~20 primary-source fetches/day across the three briefs plus research passes, that is
  roughly 600/mo — comfortable headroom on Hobby.
- **Watch:** Cloudflare-protected sites need stealth mode at **5 credits/page**, a 5x jump.
  Credits do not roll over. The `/extract` endpoint bills separately on a token track — avoid
  it unless there is a reason.
- Sources: [Firecrawl pricing](https://www.firecrawl.dev/blog/best-web-scraping-api),
  [eesel breakdown](https://www.eesel.ai/blog/firecrawl-pricing)

## Steps for Lars

Firecrawl is **not** in the Claude connector registry (checked 21 Jul), so this is a custom MCP
server, not a one-click connector.

1. Create a Firecrawl account and generate an API key. **Lars does this — I don't create
   accounts or handle keys.**
2. Add the MCP server in Cowork: Settings → Connectors → add custom MCP server. Firecrawl
   publishes an official MCP server; use their documented command/URL and paste the key into
   the credential field.
3. Approve the connection when prompted.
4. Tell me it's live. I'll run a test fetch against a page that failed before — the AIDB
   episode page is the honest test, since it is client-rendered and currently unreadable.

## Then: wire it into the research flow

Once connected, `Writing Flow/02_research-assistant.SKILL.md` needs a rule change. Proposed
wording, to apply after the connection is confirmed:

> **Fetch order.** Use native web search for discovery. For every primary source you intend to
> quote or cite, use the Firecrawl MCP scrape tool rather than the built-in fetch — it returns
> clean markdown, renders JavaScript, and avoids the context blowouts that force partial reads.
> Fall back to the built-in fetch only if Firecrawl errors. Never route around a blocked
> domain with either tool.

The same rule belongs in the `ai-morning-brief` task for the AIDB episode check, replacing the
current "try web_fetch, then Chrome" ladder with "try Firecrawl, then Chrome."

## Note

Per `CLAUDE.md`, buying credits is a RED item — I won't purchase a plan. The free tier (1,000
credits/mo) is enough to prove the value before you commit $16.
