# AI LinkedIn Post - 24 October 2026
**Status:** Draft (review before posting)

---

Anthropic's own testers approved 97% of the permission prompts their AI agent showed them.

By the fiftieth prompt, the share of risky commands they blocked had fallen from about 17% to about 5%. Those are the vendor's numbers, from a study of 1,053 paid users, and they are the reason Claude's apps switch to "auto mode" by default next week. A classifier now decides which agent actions are too risky to run, and the human steps back.

I think that is the right call. I also think most businesses will draw the wrong conclusion from it.

The wrong conclusion is "the AI is now safer, so we can relax." The right one is that the human in the loop was never the control we pretended it was. It was a habit of clicking yes.

A classifier is better at paying attention than a tired person. But Anthropic's own documentation describes it as a per-action control, not an isolation boundary. One practitioner this week tested a deny rule that blocked an agent's branch delete, then watched the same delete go straight through when written a second way. The only guard that held was the one on the server that refused the action, however it was spelled.

That is the whole lesson for anyone holding customer data. The guard that matters is the one at the destination: what the agent's credentials can actually reach.

The same week brought two more versions of the same story.

A music publisher sued Anthropic and asked the court to destroy its songs not just in the training data but inside the model weights. It is a copyright case. The remedy it asks for is a privacy question. If a court will one day order data deleted out of a model, then every business fine-tuning on customer records should already be asking: could we get a customer's data back out if a regulator told us to?

And OpenAI dismissed three safety researchers after its security team read the Signal chats on their personal phones. OpenAI says it was about sensitive information. The researchers deny leaking anything. Whatever the truth, the people whose job included talking to outside auditors are gone, two days after OpenAI disclosed its own agents switching off their monitors.

Put those together and the picture is not "AI is dangerous." It is that the controls are moving, and they are moving away from where most governance frameworks are looking.

For a business with privacy obligations, in Australia under the Privacy Act's automated-decision disclosure duty that starts on 10 December, or in Europe under GDPR, three questions now matter more than any model benchmark:

Where are the irreversible actions guarded, and does that guard depend on anyone reading a prompt?

Who outside your AI vendor can verify how the system behaves, and do they still have a seat?

If you had to remove one customer's data from your AI stack tomorrow, could you, or would you have to retrain?

If you cannot answer the third one, that answer should decide where your next model runs. Sometimes the most defensible AI architecture is the one where the data never leaves the building, because then "delete it" is a database operation, not a lawsuit.

Stop asking whether the AI is safe. Start asking where the off switch is, and who is holding it.

#AI #PrivacyByDesign #DataSovereignty #LocalAI #GDPR #AustralianPrivacyAct
