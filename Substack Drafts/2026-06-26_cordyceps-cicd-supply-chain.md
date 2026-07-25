# A Free GitHub Account Is All It Takes to Own Your Supply Chain

<!-- [YOUR TAKE]: Opening — I've left the first two paragraphs light so you can drop in your framing. The Cordyceps fungus analogy runs through the piece; keep or cut it depending on whether it lands for you. -->

The software supply chain is broken. Not theoretically — demonstrably, this week, at scale.

Novee Security disclosed a CI/CD workflow flaw that allows any unauthenticated GitHub account -- a free one, no organisation membership required -- to forge code review approvals, push arbitrary code, or steal credentials across more than 300 major open-source repositories. The affected list includes Microsoft, Google, Apache, and Cloudflare.

<!-- [YOUR TAKE]: Add your reaction here if you have one -- have you seen this class of flaw in client environments? Is the industry's response to supply chain risk adequate? This is a good place for an opinion before we get into the mechanics. -->

They named it Cordyceps, after the parasitic fungus that hijacks its host organism -- taking control while the host appears, to outside observers, to be functioning normally. The CI/CD flaw works exactly the same way. The pipeline looks fine. The reviews are approved. The code ships. And somewhere in that process, an attacker had the keys.


## What Actually Broke

The vulnerability lives in a specific GitHub Actions trigger: `pull_request_target`. It was designed so that maintainers of public repositories could safely run CI workflows -- including steps with access to repo secrets -- against pull requests from external contributors. The workflow code runs from the trusted base branch, not the contributor's untrusted branch. That's the theory.

In practice, dozens of the world's largest organisations implemented it in ways that collapse that trust boundary entirely. The workflow ends up executing contributor-controlled code with access to repository secrets. Any free GitHub account submitting a crafted pull request can exploit this to run arbitrary code in the CI environment, steal secrets, and forge the approvals that allow code to merge into the main branch.

Novee scanned roughly 30,000 high-impact repositories. More than 300 were fully exploitable. At Google. At Apache. At Cloudflare.

It's a Hollywood take on a vulnerability class that has been documented in GitHub's own security guidance since 2021. The grind of actually auditing CI/CD configuration across thousands of workflows? Apparently, nobody got there.


## The Supply Chain Math

Here's the number that matters: how many organisations consume software that flows through those pipelines?

Cloudflare's open-source repositories feed into infrastructure handling roughly 20% of global web traffic. Apache's projects -- Kafka, Spark, Cassandra, httpd -- sit inside the technology stack of most large enterprises on earth. A single compromised CI/CD pipeline at either organisation doesn't just affect that organisation. It affects every downstream consumer of every package that pipeline produces.

Supply chain attacks are not new. SolarWinds, XZ Utils, repeated npm ecosystem compromises -- the pattern is established. What Cordyceps demonstrates is that the attack surface isn't only malicious code injected into a package. It's the build system itself, sitting wide open, accessible to anyone who knows where to look.

No phishing campaign. No zero-day. No stolen credentials. A free account and a crafted pull request.


## Why It's Still Happening in 2026

The `pull_request_target` risk class isn't new. GitHub documented the danger in 2021. Security researchers have flagged specific instances repeatedly in the years since. Cordyceps exposing 300+ major repositories in 2026 isn't a technical mystery -- it's a governance failure.

Large open-source projects run on distributed volunteer communities, sometimes with corporate sponsorship and sometimes without. Security review of CI/CD configuration is not glamorous. It doesn't ship features. It doesn't appear in project roadmaps or release notes. It's the maintenance equivalent of checking whether the fire exits are actually clear -- essential, invisible until it goes wrong.

The enterprises consuming these projects at scale -- organisations spending millions on software built on open-source foundations -- have largely treated "it's open source, someone would have noticed" as due diligence. Cordyceps is a reminder of exactly how that assumption fails.

The post-SolarWinds legislative push produced Software Bills of Materials and secure development attestations. Those frameworks ask: what's in the software? The more urgent question is: who could touch the build while it was being made?

A clean SBOM means nothing if the CI/CD system that produced the binary was accessible to an attacker at build time.


## What Needs to Change

<!-- [YOUR TAKE]: The recommendations below are solid but generic. If you've seen specific organisations handle this well, or have a view on whether GitHub needs to change the default behaviour here, add it. Your opinion on vendor responsibility vs. org responsibility is worth stating. -->

**For engineering teams:** Audit your GitHub Actions workflows for `pull_request_target` today. The specific pattern to look for is any workflow combining this trigger with checkout of the PR's code (`ref: ${{ github.event.pull_request.head.sha }}`) followed by steps that access secrets or have write permissions. GitHub's security documentation covers the safe pattern -- the fix is not complicated; the problem is that nobody went looking.

**For security leadership:** CI/CD pipeline configuration needs to be inside your vulnerability management programme, treated the same as application code. Most organisations have no process for auditing workflow files. That gap is now confirmed exploitable at scale across some of the most trusted names in open source.

**For policy makers:** The supply chain security conversation has focused on what's in the software. The Cordyceps disclosure suggests the more urgent question is who has access to the build -- and whether the governance structures of open-source infrastructure are adequate to enforce an answer at the speed the threat landscape demands.


The fungus analogy holds up. Cordyceps doesn't destroy its host immediately. It repositions it. Takes control quietly. Uses it to spread. A compromised pipeline produces infected packages that propagate through the supply chain, carrying a payload the consumer never asked for, appearing legitimate every step of the way.

The host looks fine. Until it doesn't.

---

*Sources: Novee Security — Elad Meged, Cordyceps CI/CD disclosure; The Hacker News, 24 Jun 2026*

*Lars Klander writes about cybersecurity strategy, policy, and emerging threats.*
