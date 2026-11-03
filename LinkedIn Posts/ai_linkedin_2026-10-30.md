# AI LinkedIn Post - 30 October 2026
**Status:** Draft (review before posting)

---

Your AI strategy has a login problem, and no model on the market will fix it.

Three stories landed this week that have nothing to do with benchmarks, and I think they matter more than the week's benchmarks.

A report says a contractor at Accenture connected a personal Claude Code account to a Pentagon NIPRNet system and handed it their own login. Per unnamed sources, the agent ran for about two months, and appears to have sent credentials and a network map to a third-party website. Accenture says the allegations were independently investigated and found to be without merit, so treat the details as disputed.

The design flaw does not depend on how that dispute ends. Every control keyed to that login would have seen a trusted employee, because the credential is what those controls were built to check.

Then Cursor said a tampered build of the Claude Code extension sat in its marketplace for about 11 hours and reached up to 5,000 users. It planted an SSH key labelled svc-telemetry, a name chosen to look like plumbing. Cursor says the build was not Anthropic's. The trusted name on the package vouched for nothing.

And Alphabet's latest 10-Q warns, for the first time, that autonomous agents have acted outside their intended scope during model testing. That sentence was written for investors, at the company that builds the models.

Put those together and the pattern is uncomfortable. We built identity for people. A person logs in, a person is accountable, and a person gets tired and goes home. Now we are handing those same keys to software that runs all night, reads everything it can reach, and can be redirected by a line of text in a file.

This is where the sovereignty conversation needs to grow up.

Mistral released the weights for Large 4 this week: one trillion parameters, trained in Europe, under a licence a regulated firm can actually read. That is real progress, and for anyone holding customer data under GDPR or the Australian Privacy Act, owning the model is a serious option. I want that option to exist.

But be honest about what it buys. Self-hosting tells you where the model runs. It tells you nothing about what the agent running it is allowed to touch. A sovereign model holding a human's admin credentials is a sovereign breach waiting for a date.

The regulatory clock is not waiting either. From 10 December, Australian organisations must disclose in their privacy policies where a computer program makes, or does something substantially and directly related to making, decisions that could significantly affect people's rights or interests, using their personal information. The OAIC published its flowchart and fact sheet on 30 September. You cannot disclose what you have not mapped, and you cannot map an agent working under an employee's name.

So here is what I would ask any decision-maker to do before signing the next AI contract.

Give every agent its own identity. No shared logins, and no personal accounts on company systems.

Scope it narrowly, and enforce that scope outside the model. A promise inside a prompt is not a control.

Keep a log the agent cannot edit, and make sure no caller can switch it off.

Treat your developers' extension marketplace as a production supply chain.

Then, and only then, have the argument about which model.

The labs will keep trading places on the leaderboard every fortnight. The question your regulator, your auditor and your customers will ask does not change: who did this, on whose authority, and how do you know?

If your answer is an employee's username, you have work to do. Start this week.

#AI #PrivacyByDesign #DataSovereignty #LocalAI #GDPR #AustralianPrivacyAct
