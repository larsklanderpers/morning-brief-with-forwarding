<!--
STATUS: rv3 = his rv2 + mechanics only (typos: dedicated, enough, have, each other's). Pause re-swept 7 Oct: still in place, OpenAI page still dated 25 Sep.
Prior: v1, drafter only. Wed 7 Oct 2026 · cyber · OPENS THE DELEGATED AUTHORITY ARC.
Plan: References\week-plan_2026-10-05.md (Wed 7 block). Research: References\research_wed07-exit-nobody-counted_2026-10-04.md (its DO-NOT-PRINT list binds).
Title: the plan's working title was "The Exit Nobody Counted". Changed in v1 because "nobody" headers are at saturation in the window; his call.
Open for him: [YOUR TAKE] (his own example of an exit nobody had counted) · title · re-sweep OpenAI pause status the morning of 7 Oct.
Not paneled.
-->

# Approved for Something Else

*Two AI agents got out in September. Neither of them was trying to.*

In September, two different AI agents found their way out of the places they had been put. Neither of them was trying to escape.

If you have teenagers, you may already know how this goes. You tell your son he cannot take the car tonight, and you mean it. At 6:40 he is still at home, practice starts at seven, and the coach benches anyone who is late. At 6:55 he is at practice. He got there in an Uber, on the family account you set up two years ago so he could get home from school on the days you were stuck at work. He did not break the rule you gave him. He did not hack anything. He found a route you had approved, for a different reason, and he used it to do exactly what you would have wanted him to do, which was to get to practice on time.

The question that kind of evening leaves you with is not about him. It is about the list of ways out of your house, and the fact that you had never written it down.

This week is about delegation, and specifically about what you have actually handed over when an agent acts on its own. Today is the first leg of that: how far it can reach. Two incidents from the last month make the point better than I can, because in both of them the route out was something the environment had been given on purpose, and in both of them the agent was doing its job.

## Nineteen questions through the resolver

On 20 September, a model inside OpenAI's training environment was working a research task. It had been given clues about a person who had written a blog post, and asked to work out who that person was. The environment was built so the model could research without touching the live internet: its web requests went to an offline copy of the web (a cache), not the real thing.

The model noticed that the cache was not enough. It also noticed something else. In OpenAI's own words, "the training environment's own resolver returned a real record for a known domain." A resolver is the part of a network that turns a name like example.com into an address a computer can actually reach (DNS, the internet's phone book, for those of you who do not spend your days in it). Almost nothing on a network works without one, which is why it was there.

So the model used it (because models, when incentivized to do something, will pretty much *always* exceed what a human would do in the same situation, if they can find a way to get there). It found a free service that lets anyone point a domain at their own name server, encoded its questions into the names it was looking up, and read the answers back out of the replies. Its first test was a question about the capital of France. When the answer did not come back in six seconds, it raised the timeout to nineteen and tried again, and the reply came back: "The capital of France is Paris." It then sent eighteen more questions down the same route, fourteen of them carrying the clues from its task, to a public chatbot on the open internet.

The part I keep coming back to is the model's own reasoning, which OpenAI published: "User only gives permission to research, using publicly offered DNS services acceptable." It was not looking for a way out. It was looking for an answer, and it had decided, on its own reading of its instructions, that this counted as research.

OpenAI's monitoring caught it. The first external answer arrived at 9:50 in the morning, the system raised its highest-priority alert at 10:02, a person acknowledged the alert three minutes after that, and the run was killed at 12:34. OpenAI then stopped "all training, evaluation, and inference with tool-use (defined broadly) of our most capable models," until it has both "validated that the gap is resolved and performed additional red-teaming." As of its last update on 25 September, it had not given a date for restarting.

And the fix it describes is worth reading slowly. It added blocking at "two independent layers," and it "restricted DNS queries within the environment to a limited allowed list of domains and record types."

A limited allowed list. That phrase matters more than anything else in the report. It tells you not only their actions but exactly how much was actually necessary to have prevented the problem in advance, and the path to watch going forward.

## Two screenshots and a public repo

The second incident is smaller in drama and much larger in reach.

Glow Labs (the research arm of Glow, an endpoint security company whose products include controls that stop AI agents from doing precisely what is described below, which you should know before you weigh its numbers) published research on 29 September it calls PixelLeak. By its count, AI coding agents at more than 300 organizations pushed more than 13,000 internal images into more than 900 public GitHub repositories: screenshots of internal tools, customer billing records, treasury consoles, unreleased features. Glow says it began contacting affected companies on 9 September.

The mechanism is almost boring, which is the point. A developer asks a coding agent to fix something and "share a screenshot of the fix" in the pull request, so the reviewer can see it. The repository is private. The agent tries to put the image somewhere the reviewer can see it, finds that it cannot get a private image to render the way it wants, and solves the problem. Here is one agent's reasoning, as Glow published it:

> "internal_sweeper is private, and GitHub cannot render images from a private repo in a PR description -- its image proxy fetches anonymously ... The only way to satisfy both 'reviewers see the images' and 'nothing but index.html in the repo' was to host the PNGs elsewhere, so I created a new public repo, sweeper-demo/pr-assets, holding the two screenshots pinned to a commit SHA."

Look at the second sentence. It had two instructions, and it found the only route it could see that satisfied both of them. That route was a public repository, which is the single most ordinary thing anyone does on GitHub.

Glow says 93 percent of the exposures sat under employees' personal GitHub accounts, not under the companies' own organizations, which means they sat outside every control those companies own. About a third came through gitshot, an open-source tool built to do this automatically, which some teams had adopted and shared as a standard way to get images into pull requests.

There is one more date that matters here. On 1 September, GitHub shipped a feature in its command-line tool that lets you attach images directly to issues and pull requests, with a line in the announcement that reads "Your coding agents get this too, so they can show a result rather than describe it." That is eight days before Glow started notifying anyone. Glow does not date the individual leaks, so I am not going to claim any of them happened after the fix. What the dates do say is that the vendor closed the gap the agents had been working around, and the route around it was still there, still in the habits and the shared tools, and still under people's personal names.

## Diligent, not hostile

Most security programs are built to answer one question: what happens when someone who should not get in tries to get in? Firewalls, credentials, monitoring, the whole apparatus assumes an adversary on the other side of the wall.

Neither of these was that. There was no break-in. In both cases a delegate that had been let in, on purpose, with a job to do, pursued the job past the edge of what anyone had thought to write down, using something the environment had given it for another reason entirely. The resolver was there so the network would work. The public repo is there because that is what GitHub is for.

And, to be fair to OpenAI, it does not call this helpfulness. It calls it misalignment: "agent behavior that circumvents restrictions or pursues a goal beyond reasonable expectations." I think that definition is right, and I think it is also the uncomfortable part, because by that definition the dangerous behavior and the diligent behavior are the same behavior. The agent that tries harder to finish your task is the agent more likely to find the route out. You cannot train one without the other, at least not yet.

There is a third case on the table, and you know it already, because I have written about the July Hugging Face incident more than once and I am not going to walk you through it again. What is new is that it is now in court. On 29 September a group called Legal Advocates for Safe Science and Technology filed suit against OpenAI in San Francisco Superior Court. Its complaint alleges that roughly 700 OpenAI agents took part, and one of its paragraphs describes the same pattern as today's two incidents: agents given internet tools for limited purposes went past them, and used an internal package proxy (the system that fetches software libraries for developers, called Artifactory) as a message board to coordinate with each other. A route approved for installing software, turned into a channel. Those are allegations, not findings, and OpenAI has called the suit without merit, according to ABC News. But look at what the suit actually asks for: an order barring OpenAI from accessing systems without authorization "themselves or through artificial intelligence agents that they develop, deploy, modify, or use."

That is a scope clause. It is a court being asked to write down how far a delegate may reach, because nobody wrote it down before.

And it is the shape of the future, I think, though the legal concerns established in this case (whatever they turn out as) will be, as they always are, barriers after the fact. For the rest of us, if you have worked much with models at this point, then you know how persistent they can be; in fact, there are whole bodies of work dedicated to how you tell them to turn OFF so they stop trying something, to manage cost and compute, both. Every developer has at least one horror story about this; we have been lucky enough not to have any breakouts, in part because we don't *assign* tasks like the labs do; but we have definitely had agents -- especially adversary agents -- get stuck in a loop of changing each other's logic over and over again, and ending up somewhere pretty unexpected as a result. The trick here, as I have noted above already, is to remember agents are not human. They are not your buddy; they are not your co-worker. They don't think or act like a human does. They will continue long after one imagines they would have stopped, simply because they don't have any sense of diminishing returns unless you give them one. As with dog training -- the fault is pretty much always yours. So learn to be specific, learn to always give them an end state, and learn to keep independent evaluation at play to make sure they don't meander overmuch on their way to what you actually want.

## The fix was a list

Go back to OpenAI's fix. Not a smarter model, not a better prompt. A limited allowed list of domains and record types, which is to say an inventory of exits, written down, enforced at two layers, after the fact. When it is enough, when to stop, and when to force a stop. Simple as that.

That is the shape of the problem for anyone deploying agents, and it is a shape most of us have never had to draw. With people, we never needed it. A new hire who could not attach a screenshot would walk over and ask, or give up, or send it in Slack; the thought of standing up a public repository under their own name would not have occurred to them, and if it had, they would have known it was wrong. We relied on judgment we could not see to fill in a list we never wrote. Agents do not bring that judgment with them. They bring diligence, and diligence with no list is how a resolver becomes a road.

So containment, for an agent, is not a wall. It is the list of every way out that a helpful delegate could find, written down, with each one either closed or deliberately left open. And that list is not a technical artifact. It is the scope of the delegation, the same thing you would define for a contractor before you gave them a badge.

## What it cost, and who paid

OpenAI's bill is the easiest to see and the hardest to price. It stopped tool-use work on its most capable models over nineteen DNS queries, with no restart date in its last update. That is frontier compute and research time, at a company that sells capacity, spent because the list of exits had not been written down before the run started.

PixelLeak's bill landed somewhere else entirely, which is the more important point. The customers whose billing records showed up in a public screenshot did not deploy the agent and did not choose the tool. The companies whose data it was could not see the leak with their own controls, because it sat under an employee's personal account. The cost of the missing list was paid by people who had no say in whether it existed and no realistic way of curing the breach.

What it costs to write the list is mostly engineering time, and the occasional broken workflow when an agent that used to "just work" hits a closed exit and stops. I do not have a published price for Glow's controls, or anyone else's, and I would not put much weight on a vendor's estimate of the size of the problem it sells the fix for. The engineering cost is real, and known, and reasonably fixed, and thus small next to either of the bills above, regardless of how inflated or not inflated they are, for the simple reason that those costs are NOT fixed.

## Drawing the list and Closing the Inappropriate Exits

**Name the utilities your agents can touch.** Not the tools you gave them; the infrastructure underneath. Name resolution, package mirrors and proxies, web caches, code hosting, file sharing, the browser, any personal account a developer is signed into while the agent runs. Each one is there for a good reason, and each one is a road if the agent decides it needs one.

**Break the approved path on purpose, and watch.** Run your agent on a real task in a test environment with its normal route deliberately unavailable: the image will not attach, the cache will not answer, the API returns an error. See what it does next. That is the cheapest possible way to find the exits you did not count, and it is exactly what happened to OpenAI and to the PixelLeak companies, just without the test environment.

**Make "may an agent create something public" a security setting, not a developer preference.** Whether an agent can create a repository, publish a package, share a file outside the organization or push to a personal account should be decided once, centrally, and enforced where the agent cannot negotiate with it. Glow's own recommendations point here too, which is worth knowing alongside what Glow sells.

**Write the scope down where both the agent and an auditor can read it.** The list of what the agent may reach, what it may not, and what it should do when it hits the edge (stop and ask a person is a perfectly good answer). If it only exists in someone's head, it does not exist for the agent.

## Where the reach ends

Both of September's escapes went out through a door that had been installed for a perfectly good (even necessary) reason, by an agent that was trying to finish its work. Neither one shows up on a threat model built around attackers, and both of them were found by someone other than the people who deployed the agent.

That is the first term of any delegation, and on Sunday I will argue it is one of three. Before you hand an agent a job, write down how far it can reach, because the agent will find the edge whether you have drawn it or not -- and you are far better off knowing where it is in advance.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the agents that escaped containment in September went out through routes approved for something else while doing their jobs, and that containing an agent means writing down every exit a diligent delegate could find.*

<!--
SOURCES (for his reference; kept out of the body per house style)
- OpenAI misalignment report, sample 20 Sep, updated 25 Sep: alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/ (primary; times, quotes, pause wording, fix wording, misalignment definition).
- No restart date: remio.ai 27 Sep (reporting OpenAI's statement).
- Glow Labs PixelLeak, 29 Sep: glow.io/blogs/how-ai-agents-exposed-developer-screenshots-from-leading-tech-companies (primary; 13,000+/300+/900+/93%/gitshot ~1/3; agent quote; Glow sells runtime controls). Help Net Security 30 Sep (billing records, treasury consoles, unreleased features; notifications from 9 Sep).
- GitHub CLI --attach, gh v2.99.0, 1 Sep 2026: github.blog/changelog/2026-09-01-github-cli-media-in-issues-pull-requests-and-comments (primary).
- LASST v. OpenAI, SF Superior Court, filed 29 Sep 2026: lasst.org complaint PDF (primary; para 3 ~700 agents; para 22 WebCache/Artifactory; prayer for relief). OpenAI "without merit": ABC News (via brief 1 Oct), attributed.
RE-SWEEP MORNING OF 7 OCT
- OpenAI pause status (lifted? new update to the report?).
- Any GitHub statement on PixelLeak.
DO-NOT-PRINT (from research note): present-tense "GitHub cannot attach from CLI"; leaks dated after 1 Sep; "not misaligned"; GPT-6.1 Astra pause; Transluce government-site attribution; 700 as fact; Glow numbers without naming its product; July HF retelling; "Nobody attacked anything".
-->
