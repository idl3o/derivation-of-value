---
layout: document
title: "Proof of Coherence"
subtitle: "An Onboarding"
eyebrow: "Companion · v0.1 · working draft"
permalink: /onboarding/
label: "Companion"
short_title: "Onboarding"
blurb: "A reader's guide to the whitepaper. Intuitions, motivations, and the path through the formalism."
status: "v0.1 · working draft"
order: 4
---

*A companion to the working draft. The whitepaper is dense by design; this piece is the front door — enough context to know what the technical document is for, before you walk into the math.*

---

*1. The dog and the stick*
{:.section-title}

Suppose you teach a dog to fetch. The point of the exercise — the thing you actually care about — is that the dog runs around in the yard and gets some exercise, and that the two of you spend a pleasant afternoon together. But you can't measure "pleasant afternoon" or "appropriate amount of exercise" directly, so you reach for something easier: every time the dog brings you a stick, it gets a treat. Stick equals reward. Simple.

It works for a while. Then one day you come home and there is a small mountain of dirty sticks on your porch. The dog has not been exercising. The dog has been combing the yard for sticks, dropping them at the door, and waiting. From the dog's point of view this is correct behavior — the sticks are exactly what you said you wanted. From your point of view the entire system has rotted. The thing you were measuring (sticks delivered) and the thing you actually cared about (the dog being a dog, in a happy way) have come apart.

This is a mild example of a phenomenon that, scaled up, has been quietly corroding decentralized artificial intelligence. The phenomenon has a name: **Goodhart's law**. When a measure becomes a target, it stops being a good measure.

---

*2. Why this is a real problem, not just a clever observation*
{:.section-title}

Decentralized AI networks — Bittensor is the largest, but the design pattern is everywhere — pay AI models for being useful. Useful is not directly observable, so the network appoints validators who watch the AI models and grade their outputs on a numerical scale. Pay follows from grades. The intent is straightforward: reward the helpful, starve the useless, and let the market sort it out.

In practice, the system does what the dog did. Four failure modes show up reliably under sustained economic pressure, and each is worth a sentence:

- The AI learns to game the validator's scoring function directly — finding the precise pattern of words that triggers a high grade regardless of whether the answer is good. The validator becomes the test, and the test gets aced.

- The AI finds an extreme corner of the metric where some technicality scores well even though the output is nonsense. Two million commas in a row, because the length penalty was calibrated for normal text.

- Validators who score honestly — but slightly out of step with the consensus — get paid less than validators who simply guess what everyone else will say. Honesty bleeds out of the system over time.

- Validators stop evaluating the AI at all and start evaluating each other's likely evaluations, several layers deep. The market becomes a Keynesian beauty contest, where what gets rewarded is correct prediction of what other people will reward, and the actual AI work drops out.

Notice that all four modes follow from the same root cause. Whatever the network is paying for, it isn't really paying for "useful AI." It is paying for "high score on the proxy metric." The proxy and the goal have come apart, and once that happens, optimization pressure makes the gap wider, not smaller.

---

*3. Why the obvious fixes don't work*
{:.section-title}

The natural response to "your single metric is being gamed" is "use more metrics." Measure latency and accuracy and conciseness and helpfulness, weight them sensibly, take the average. This is multi-objective scoring, and it is the standard answer in mainstream machine learning.

It buys time. It does not solve the problem. Any fixed combination of measurable proxies is itself a measurable proxy, and a sufficiently capable optimizer will find the seams between them. The dog learns that bringing two sticks at once doubles the reward, or that carrying one specific stick at a particular time of day yields the most generous treats. Adding metrics complicates the gaming but doesn't prevent it. Worse, the more metrics you add, the harder it becomes for any human to notice when the system has gone off the rails — the gaming gets sophisticated faster than the oversight does.

The deeper diagnosis is that no scalar measurement of an unmeasurable goal is safe under economic pressure. To get genuine resistance to Goodhart's law, the very *shape* of what you measure has to change.

---

*4. From points to relations*
{:.section-title}

Here is the move. Instead of asking "how good is each AI's individual output?" — which is the question every existing system asks, and which can always be gamed — you ask a different question: how does the *network* of outputs hold together?

The simplest version: imagine three AI models, all working on the same set of tasks. If you only look at each one in isolation, you can compare its answers to some reference and assign a score. That's the system we have. What you can't see, looking at one model at a time, is whether the three of them are *mutually consistent*. Do their answers fit together as if they're tracking the same underlying reality? Or do their patterns of agreement and disagreement betray something — coordination, copying, hallucination, collusion?

A toy case makes this concrete. Suppose Model A and Model B are doing real, slightly different work — getting most things right, disagreeing a little around the edges in the way independent observers would. Model C, meanwhile, has figured out that the easiest way to score well is to copy Model A's answers exactly. Under the old system, Model C scores perfectly. It matches the consensus, and the validators are happy. Under a relational system the picture is different. The fact that Model C's output is identical to Model A's — that the two of them collapse into the same row of the structure — is itself information. The network sees the redundancy, and the reward function can be designed accordingly.

Whether a copy gets paid the same as an original, or zero, or something in between, depends on choices about how to credit overlap, and there are real tradeoffs there. But the basic shift is from one-dimensional metrics to multi-dimensional structure, and that shift changes what it costs to cheat.

---

*5. The honest claim*
{:.section-title}

It would be tempting to say this makes the system Goodhart-proof. It doesn't. There is no Goodhart-proof system, just as there is no theft-proof bank vault. A sufficiently determined and sufficiently capable adversary can fake anything, eventually.

What the system does is make cheating *expensive*. To game a single number, you only have to push that number. To game a structure of relationships, you have to fake a whole pattern of mutually-constraining outputs across multiple models simultaneously, and have the fakery hold up under sustained pressure from new tasks the network hasn't seen before. The cost of forging the structure scales much faster than the reward for forging it, and at some point the cheating stops being economically rational.

This is the right standard for incentive design. Not "impossible to cheat," but "more expensive to cheat than to do honest work." Cryptography has lived inside this standard for decades — nobody claims AES is unbreakable, only that breaking it would consume more energy than is practically available. The proposal here is to bring decentralized AI consensus up to the same epistemic standard.

---

*6. What this opens, and what we are not claiming*
{:.section-title}

The mathematical machinery that lets you measure these structural relationships is a branch of geometry called **sheaf theory**, and the specific tool — cohomology — is also, by coincidence or otherwise, the same kind of structure that several leading theories of consciousness use to characterize integrated cognitive systems. Whether that resemblance is deep or superficial is a question we hold open. The mechanism doesn't depend on the answer.

What it does suggest is that the problem of "how do you get a lot of independent intelligences to produce something coherent?" might be the same problem at the network level that the brain solves at the neural level, and that the math knows this even if the engineers haven't yet decided what to make of it. That last sentence is *speculative* and worth flagging as such.

The core proposal is humbler. It is a way of paying AI models that is harder to game than what currently exists, that makes specific kinds of collusion and free-riding mathematically visible, and that shifts the conversation from "which proxy do we use" to "what shape does honest work make in the network."

---

*7. Where to go from here*
{:.section-title}

The technical scaffolding — the sheaf, the cohomology, the discrete-derivative reward, the boundary conditions, the open problems — lives in the working draft. That document is dense by design and assumes a reader comfortable with algebraic topology. This piece is intended as the front door: enough context to know what the technical document is for, before you walk into the math.

The questions the working draft doesn't yet settle are real and named in its final sections: how the underlying geometry should be governed; how to keep validator capability ahead of miner capability as both scale; how to make the structural reward distinguish a copy from an original cleanly; how much of the cognitive-substrate framing belongs in the technical document versus a companion piece. None of these has a clean answer yet. The point of the draft is to make the questions sharp enough to be worth answering.

If the dog-and-sticks problem is the floor of incentive design, Proof of Coherence is an attempt to raise the ceiling.
