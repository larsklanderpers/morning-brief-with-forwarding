# AI LinkedIn Post - 21 October 2026
**Status:** Draft (review before posting)

---

Your AI register is a list of things people remembered to tell you.

That line is not mine. It comes from a governance lead in an Australian regulated entity who found a live AI agent that was not on the register she maintains. Nobody hid it. The team that built it called it "a script". The register asked about agents, so nobody thought it meant them.

I keep coming back to it, because three stories this week all turn on the same question: who actually holds the record?

Start with the vendor side. Reporting on Anthropic's newer draft IPO filing says revenue went from $1.1 billion to $16.3 billion in a year, compute commitments are above $600 billion, and the company's own cloud partners have started refusing it extra capacity. Set the valuation drama aside. The operational fact is that one of the most widely used models in enterprise sits at the end of somebody else's capacity queue.

Then look at what the platforms shipped. ChatGPT now lets users lock individual chats behind a PIN or a fingerprint. Per the reporting, nothing is newly encrypted, the provider keeps its standard logs, and forgetting the PIN permanently deletes the lot. The same week, OpenAI added a 12-hour prompt cache that holds your context on its side for half a day in exchange for a cheaper bill.

Both are sensible features. Both will be read by staff as "private" and by finance as "savings". Neither changes who holds the copy.

Now look at what regulators are asking for. New York City has proposed a rule that businesses must disclose chatbots and give customers an easy path to a human, with fines per violation. In Australia, the OAIC's automated-decision transparency duties start on 10 December, and law firms are reading the guidance as reaching decisions where a human signs off on an AI-generated summary.

Put those together and the direction is clear. The business owns what its automation does. "A human was in the loop" is no longer a shelter if the human was reading a machine's summary. And the evidence you will be asked for is evidence about your own systems, not your vendor's promises.

So here is the practical shift I would make, especially if you hold customer PII under the Privacy Act, GDPR or APRA's prudential standards.

Govern the credential, not the spreadsheet. Every agent needs a key, a service account or a mailbox, and every one of those comes from a system with a log. Make issuing a key the moment something gets registered. Then the register fills itself.

Keep the source behind the summary. If a summary informs a decision about a customer, keep the material it summarised and know who checked it. From 10 December, that may be a disclosure obligation, not just good practice.

Treat vendor-side features as vendor-side. Locked chats, long caches and memory are conveniences that live on someone else's infrastructure. Write in your AI use policy what may and may not go into them.

Design for the second model now. A vendor that is rationed by its own clouds can change your rate limits and your price list. Moving inference later is an architecture project. Planning for it now is a design choice.

The organisations that come through the next year well will not be the ones with the best model. They will be the ones that can show, from their own logs, what ran, on whose data, and who decided.

Who in your organisation finds out first when an AI tool goes live? If the honest answer is "nobody, until something breaks", that is the place to start this week.

#AI #AIGovernance #PrivacyByDesign #DataSovereignty #AustralianPrivacyAct #LocalAI
