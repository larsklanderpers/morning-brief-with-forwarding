# The Party of Record

**STATUS: DRAFT v1 -- for Monday, 21 September 2026. Written 20 Sep. NOT PANELLED. HE PUSHES TO SUBSTACK HIMSELF.**

**Series: Monday · Thread: who carries it when the label is wrong (opens the 21 Sep arc) · Slot: shape of work**

**Research:** `References\research_party-of-record_2026-09-21.md` (deep dig, 20 Sep). The plan's test, "somebody is repricing this now," PASSES, and the repricer is the insurance market. Every factual claim below is footed there; its DO-NOT-PRINT list binds every later revision.

**Open for him:**
1. `[YOUR TAKE]` at the emotional core. He has a case and said he will add it in his edit ("leave it i will add it in my edit", 20 Sep). Not fabricated.
2. **Bessent line is secondary** (FedScoop/Gizmodo; hearing confirmed at the committee page, quote not in his written statement). Printed as reported. One sentence only, to stay off Thursday's ground.
3. **Controlling image is new:** the owner-builder permit. Checked against the window's spent images (concierge, staffing agency/temp, ECG, scrutineering, distribution list, dictionary, comment window, property notice and back of the form, truck scale, gate, glass, meter, room). The close does NOT return to it, because Sun 20 spent the bookend.
4. **Window checks done by the drafter:** no vendor contract text (Fri 18 owns it and already printed the Anthropic disclaimer and the twelve-month cap); no Moffatt; no four tests; no EULA-at-scale line; no "load-bearing"; no excluded-party close; no insurance-odds close (Tue 15's last line); no renewal close (Fri 18's last line); no "Read that again" (Wed 16 and Thu 17 used it). Headers avoid the comma-and-clause, "Where X" and spelled-number forms. Actions avoid write-down, ask-what-happens, ask-for-the-facts, use-the-route, price-the-model-change, swap-the-trigger, file-a-comment, hold-X-against-Y.

---

Every organization putting a model in front of its customers is now the party of record for what that model does. The insurance industry worked that out before most of the buyers did, and it has spent this year quietly rewriting its policies to match.

If you have ever renovated a house, you probably know the owner-builder permit. It lets you pull the building permit in your own name instead of paying a licensed contractor to do it, and it is cheaper, and it is faster, and it feels like nothing more than paperwork. What it actually does is make you the party of record. The electrician you hired still wires the kitchen, and the electrician still knows far more about what is behind the drywall than you ever will. But when the inspector finds something wrong, the finding has your name on it, and when the wiring starts a fire three years later, the question of whose job it was to know gets answered by the name on the permit. You did not do the work. You cannot see the work. You own it anyway. You are *responsible* and often more materially, *liable* for it anyway.

Deploying a model is pulling that permit. You did not train it, you cannot inspect its weights, and you have no view of what changed in it last Tuesday. But you put it in front of your customers, under your brand, inside your workflow, and the law, the regulators and now the insurers are converging on the same answer about whose name is on the job.

Last week was about who decides what a label says. This week is about where the cost lands when the label, or the model behind it, turns out to be wrong. And the clearest place to watch that happen is not a courtroom or a statute. It is the fine print of your next insurance renewal.

## The exclusions arrived in January

In January, Verisk, the company whose ISO forms sit underneath a very large share of the commercial insurance written in the United States, made three new generative AI exclusions available for general liability policies. One of them, CG 40 47, removes generative AI claims from both the bodily injury and property damage coverage and the personal and advertising injury coverage in a standard policy. Verisk's definition of what is being excluded is, I imagine, broad on purpose: *"a machine-based learning system or model trained on data with the ability to create content or responses, including text, images, audio, video or code."* According to the trade press, the forms were approved by state regulators before they took effect.

General liability is the dull, foundational policy almost every business carries. It is not where most people would go looking for an AI decision. That is rather the point.

The management liability side moved earlier and harder. W. R. Berkley filed what the market has started calling an "absolute" AI exclusion for its directors and officers, errors and omissions and fiduciary lines, and the operative language bars coverage for any claim *"based upon, arising out of, or attributable to... any actual or alleged use, deployment, or development of Artificial Intelligence by any person or entity."* Read the last four words carefully. It does not matter who built the system, or whose model it was. If the claim arises from AI being used, by anybody, the policy steps back. And the definition of artificial intelligence underneath it covers any machine-based system that infers outputs, which is a great deal more than chatbots.

The reasoning behind this showed up in the Financial Times last November, when AIG, Great American and W. R. Berkley were reported to be seeking regulators' permission to exclude AI liabilities. One underwriter described model outputs as *"too much of a black box."* Aon put the problem in the terms an actuary actually worries about: the market can absorb a single $400 million loss, but not an *"agentic AI mishap that triggers 10,000 losses at once."* That is the whole shape of it. A fire burns one building. A bad model update ships to every customer running it, on the same afternoon.

I want to be precise about how far this has gone, because it is easy to overstate. AIG said afterwards it had no plans to implement its filed exclusions. Marsh told Business Insurance in April that the market *"has been restrained in taking any drastic actions,"* and Gallagher described the ISO forms as being picked up by *"a few carriers."* Verisk itself told the Insurance Journal in July that it does not know *"how many insurers are adopting them yet."* So this is not a market that has shut the door. It is a market that has built the door, had it approved, and left it on the shelf beside the renewal paperwork. Which, if you are the one renewing, is not a great deal more comforting.

## The law is walking the same way

If the insurers were out on their own here, you could call it caution and move on. They are not.

Since the first of January, California law has said that a defendant who *"developed, modified, or used"* an AI system cannot argue that the AI *"autonomously caused the harm"* (Civil Code section 1714.46, which started life as AB 316). That sentence is short, and it closes the one exit a deployer might have reached for. The system did it is no longer a defense in the state where most of these systems are built -- any more than "the dog ate my homework" used to be when we were kids. The word *used* is in there on purpose and it strongly identifies the operator as responsible regardless of the level, quality, or accuracy of the underlying inference.

Colorado got there from the other direction. Its first AI act never took effect, and the replacement signed in May, which applies from next year, splits fault by relative responsibility and, in Holland & Knight's summary of it, shields developers *"from liability for off-label deployer uses."* That is a reasonable rule on its face; nobody should be liable for a use they never contemplated. But run it forward. The deployer decides the use, the developer is shielded from the uses it did not sanction, and the space between the two is, in practice, yours.

The enforcement that exists points the same way. When Pennsylvania's Attorney General went after an auto insurance cancellation in May, the party that signed up to the fix was GEICO, the insurer that *"utilized a tool with artificial intelligence features,"* and the tool's maker was not named at all. When Massachusetts settled with the student lender Earnest for $2.5 million last year over its underwriting models, the party paying was the lender using them -- not a hallucinating AI, not a bad set of guardrails, not "a training run that escaped the sandbox"; the bank that owned the model that underlay its underwriting that odds are high there was no risk manager who really understood what it was doing, was the one with the purse strings and the liability.

The loudest counterexample in Washington is instructive precisely because of how it turned out. OpenAI backed an Illinois bill this year, SB 3444, that would have spared frontier developers liability for catastrophic harms (mass casualties, a billion dollars or more in damage) unless they acted intentionally or recklessly, provided they published a safety framework. It died in committee in May. Illinois passed a different AI safety law in July with no shield in it at all. And last Monday, Treasury Secretary Bessent told the House Financial Services Committee, as FedScoop reported it, that *"the best way to guarantee safety is that the creators are liable for what they build and generate."* That is the rhetoric. That is the *politics*, which we will talk more about tomorrow. The statutes that have actually been signed and that are responsible for enforcing the actualities keep landing on the word *used* and keep directing the liability *away*.

## Two cases that cut the other way

This argument has soft spots (as they all seem to, in an economy and environment that seems to have little or no nuance on the face of it but that is actually incredibly nuanced under the covers), and you should see them before you take it to anybody.

**The vendor does get sued, sometimes.** In 2024 the Texas Attorney General settled with Pieces Technologies, the maker of a clinical AI tool, over claims about how rarely it hallucinated. The four hospitals using it were not the target; the company that marketed the accuracy figure was. And in *Mobley v. Workday*, a federal court in California let discrimination claims proceed against the vendor itself, on the theory that an AI screening tool acting for an employer can be that employer's agent. So the developer is not untouchable, and anyone who tells you the vendor always walks is overselling it. What neither case does is get the deployer out of the chair. In *Mobley* the employer is still the employer. The question being argued is whether the vendor sits in the chair beside you, not whether you are able to get up and leave the room.

**Nobody has been denied a claim yet, as far as anyone has published.** I looked for a documented insurance claim, paid or refused, on the grounds of AI model error, and could not find one, and neither could the coverage lawyers writing about this. Policies without an explicit exclusion may still carry what the industry calls silent coverage, meaning they pay because nobody wrote the risk out. So the honest version of this piece is not that your policy has already failed you. It is that the language to make it fail has been written, approved and put on the shelf, and the first denials will be how most people find out which shelf their carrier took it from.

## Somebody is selling it back

Here is where it stops being a legal abstraction and becomes a line item.

At the same time as the exclusions went on the shelf, a separate market opened to sell the same risk back to you. Armilla, writing on Lloyd's capacity through Chaucer, offers up to $25 million per organization for model error, output liability and agent failures, and in February the two launched a standalone AI tower designed to sit beside cyber and technology errors and omissions cover, rather than inside it. Chaucer's own explanation was that AI exposure *"starts to distort coverage lines it was never priced for."* Munich Re's aiSure product, which also offers cover to companies deploying AI rather than only to the vendors building it, says it sets premiums by *"the quality of the model and its performance stability."*

Now look at that from the buyer's side. The insurer is underwriting a model. The model belongs to somebody else, who will not show you how it was built, what changed in the last update, or how it performs on your data. The premium is set on the model's quality. And the premium is paid by you.

The underwriters have noticed the gap, too. A Westfield Specialty executive described the questions his underwriters now put to insureds as *"What models are you utilizing? How were decisions made? What checks exist?"* Those are perfectly reasonable questions. For a great many deployers, the honest answer to the first is a vendor name, to the second is that the vendor has not said, and to the third is a human who reads some of the outputs some of the time.

Gallagher's survey of its own insurance professionals in February found that one in five had a client with an AI-related loss or claim in the past year, *"with just over half covered fully by insurance."* Just over half. The rest was paid by the party of record.

As much as I wish (and don't wish) I had a direct example for you on this, what I do have is a friend's experience. They embedded an inference component into the fraud determination policy for a financial services customer. They (effectively) missed a configuration in their training and their guardrail creation which would have resulted in the fraud model working differently than it ultimately did on first go-live. The model let a few too many bad transactions go by, and blocked a few too many good transactions, to the point that customers noticed, got involved, and filed suit. Regardless of the fact that the suit was ultimately settled before going to court, a solution which was meant to eliminate mistakes and improve the bottom line ultimately cost its adopter several million dollars in legal fees alone, without counting the settlement, but nowhere in the mix was the model provider whose inference hallucinated outcomes because it hadn't properly been curtailed from those outcomes. Lots of mistakes to trace out in this example, the point is the liability still ended up on the adopter, because the business case *wasn't clearly delineated* so my friend's company (the deployer) was not responsible for the fact it was missing. 

## What to do before the renewal does it for you

First and foremost, know what is yours on the liability ledger *now*, even before things change, and make sure you share that insight with your risk managers and financial professionals. The suggestions below are only so useful if that first step is not done.

**Pull the endorsements before the broker sends them.** At your next renewal of general liability, directors and officers, and errors and omissions, get the full endorsement schedule, not the summary, and search it for the words *artificial intelligence*, *generative*, and the form numbers CG 40 47, CG 40 48 and CG 35 08 (if you are feeling particularly meta that day, have your AI assistant search for those words or anything comparable). If your broker cannot tell you whether any of them are attached, that is your answer about how closely anybody has been looking. And if one is attached, the next conversation is about what it costs to take it off, not whether it applies.

**Forward the underwriter's questions to the vendor.** Take Westfield's three questions, or whatever your own carrier asks, and send them to every AI vendor whose output reaches a customer, a filing or a decision about a person. Which model, which version, what changed recently, what testing exists that you can show an underwriter. Some vendors will answer properly, and that is useful information about who to keep. The ones that cannot answer have just told you what your insurer is going to price in.

**Put a number on the uncovered half.** Pick the two or three places where a model already makes, or drafts, something your customers rely on. For each one, estimate what a bad week costs, if every affected customer got the same wrong answer on the same afternoon, because that is the scenario the carriers are pricing. Then compare it with the price of the affirmative cover that now exists. Sometimes the premium will be obviously worth paying. Sometimes the cheaper answer will be keeping a person in the loop for another year. Either one is a real decision. Not knowing the number is the only one that is not.

## The name on the job

None of this happened because anyone was careless. The insurers are doing what insurers do with a correlated risk they cannot see into. The legislators who wrote *used* into their statutes were trying to make sure somebody answers for the harm. The vendors are pricing their products for a market where the risk sits downstream. Every piece of it is rational on its own.

Put together, though, it means the most expensive fact about the model you bought is not in the vendor's paper at all. It is in yours, and in your carrier's, and it was settled this year while most of us were still arguing about who should be accountable. The market has already answered that, in writing. Most buyers are going to read the answer for the first time in a letter explaining why a claim is not covered.

---

*Thanks for reading. I know these run long and land dense, and I appreciate you taking the time with them.*

*Lars Klander writes about cybersecurity strategy, AI governance, and technology risk. Today's argument is that the cost of a model being wrong is landing on the organization that deployed it, that the insurance market has already written the exclusions and started selling the cover back, and that California, Colorado and the state attorneys general are pointing at the same party: the one that used it.*
