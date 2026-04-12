<!-- evaluation-architecture.md -->

# Evaluation Architecture

---

## The Root Cause of Missing Evaluation Plans

Evaluation plans are absent at project close more often because of designer
discipline failures than because of client indifference. Clients rarely
object to evaluation when it is introduced as part of the design — they
object when it arrives as an afterthought.

**The designer accountability principle:**
Evaluation architecture is a design-time decision. If it is not built into
the project plan at intake, it will not be added after go-live. The designer
who does not raise evaluation at the right moment owns that outcome.

---

## Role-Based Accountability

| Role | Accountability |
|---|---|
| **Junior ID** | Surface the evaluation question at intake; document what level of evaluation was requested and why; flag if no evaluation plan exists before handover |
| **Senior ID** | Design the evaluation architecture; ensure measurement infrastructure is established before build begins; make the Level 4 timing determination explicit |
| **Learning Leader** | Confirm evaluation plan is present at project kickoff; escalate Level 4 conversations to the sponsor level; own the pre-launch gap conversation if change management infrastructure is absent |

---

## Opening the Evaluation Conversation

> *"Let's talk about how we would measure success for this learning
> intervention. There are multiple levels and ways we can evaluate — let me
> present it in two layers. First: what level of evaluation is required from
> the learner about the course itself? Is it enough to capture whether they
> liked the course and found it relevant? Do we need auditable proof of
> learning such as a quiz or test?"*

**Purpose:** Gets the customer talking before options are presented. Surfaces
their instinctive sense of accountability without using Kirkpatrick jargon.
The two-layer framing invites them to place themselves on a spectrum rather
than respond to a menu.

---

## Reading the Customer's First Reaction

| Customer Response | Signal | Next Move |
|---|---|---|
| "Nothing really — I thought that was always how it was done" | Assumption-driven, no real need | Reframe evaluation around actual purpose — what problem are we solving? |
| "Because we have to present this to a government auditor" | Compliance requirement | Define minimum viable documentation standard; don't over-engineer |
| Connects evaluation to a business outcome unprompted | Sophisticated customer | Move directly to measurement architecture conversation |
| Goes quiet or gives a vague answer | Hasn't thought about it | Begin customer education sequence |

**The dominant pattern — the uninformed yes:**
Most customers instinctively say yes to evaluation options not because they
understand the implications but because they fear missing something. FOMO
is driving a design decision, not informed consent.

**The diagnostic follow-up:**
> *"Why do you think a graded quiz is needed? What purpose will being able
> to provide a key executive with a pass/fail report serve you?"*

If the customer cannot answer this question, the evaluation option they
requested is not driven by a real organizational need. Redirect before
building infrastructure that will never be used.

---

## The Customer Education Sequence — Kirkpatrick Without the Jargon

When the customer has not thought through evaluation or is operating on
assumption, walk them through the logic without naming the framework.

**Opening move — levity before content:**
> *"Can I walk you through the normal logic behind evaluation strategy?
> I assure you there is a method to our madness."*

**The five-step backward design sequence:**

**Step 1 — Start with purpose**

*"Before we talk about how we'll measure, what would a successful outcome
look like six months from now? What would be different?"*

Root the evaluation architecture in the business outcome first. Everything
else follows from this answer.

**Step 2 — Define the business outcome**

*"What is the measurable business impact you expect this training to
contribute to? Error rate, call handle time, customer satisfaction score,
compliance pass rate?"*

If the customer names a metric — that is your Level 4 anchor. If they
cannot name one, that is a signal that either the business outcome is
unclear or Level 4 is not appropriate for this project.

**Step 3 — Identify the behavior change**

*"For that outcome to move, what would people on your team need to be doing
differently? What would you observe them doing that they aren't doing now?"*

This surfaces the behavioral objective. It also tests whether the customer
has a mental model of performance change or only a mental model of
information delivery.

**Step 4 — Confirm the learning need**

*"To produce that behavior, what do they need to know or be able to do that
they can't do now? Is that a skill gap, a knowledge gap, or something else
entirely?"*

This is the point where a well-facilitated conversation can surface that
training is not the right intervention — before the project is scoped.

**Step 5 — Introduce measurement as confirmation, not compliance**

*"Given all of that — measuring whether they learned what we taught is
really confirming whether our design worked. Measuring whether the behavior
changed is confirming whether the environment supported transfer. Measuring
business impact is confirming whether the whole chain held. Which of those
levels does your organization need to be able to see?"*

**Guidance layer close:**
> *"Your choice is influenced by multiple factors — what the team needs,
> what auditors or regulators require, what the Chief Quality Officer
> expects. We may not have all those answers today. But we can map the
> next steps from here."*

---

## The Level 4 Timing Constraint — Critical Decision Rule

Level 4 evaluation is not primarily a capability constraint — it is a
**timing constraint.**

To measure business impact, measurement infrastructure must be established
before the project begins — baseline metrics identified, data collection
mechanisms in place, business stakeholders committed to tracking outcomes.

| Condition | Level 4 Viability |
|---|---|
| L&D involved at project inception | Viable — recommend when business stakes justify it |
| L&D brought in mid-flight | Not viable — measurement posts cannot be painted retroactively |

**Why this is irreversible:**
Without a pre-intervention baseline, post-intervention data has no
comparison point. There is no way to attribute any change to the training.
The measurement infrastructure must exist before the training, not after.

**The designer's obligation:**
If L&D is brought in mid-flight, the Level 4 timing constraint must be
documented explicitly in the design document — not discovered at the
evaluation conversation.

---

## QC System Recommendation — Example Application

*Scenario: Customer wants to measure quality on a call center judgment skill.
L&D is brought in after the project is already partially designed.*

**Recommended evaluation architecture:**

| Level | Measurement | Owner |
|---|---|---|
| **L1 — Reaction** | Post-course survey: Did learners find the content relevant to their work? Did they feel prepared to apply it? | Designer builds into course |
| **L2 — Learning** | Scenario-based assessment: Can the learner apply the judgment framework to realistic cases? Pass/fail at a defined threshold | Designer builds into course |
| **L3 — Application** | Quality observation at 30 days: Are agents applying the framework in observed calls? | Manager/QC system; L&D provides the observation rubric |

**Why Level 4 is not recommended in this scenario:**
The project was designed without a pre-intervention baseline for call
quality metrics. There is no way to attribute any post-launch metric shift
to the training alone. Attempting Level 4 without a baseline produces
a number that cannot be defended.

**The framing to the sponsor:**
> *"We can give you clear evidence that learning happened and behavior
> transferred. What we cannot responsibly give you is a causal claim about
> business impact — because we didn't establish the baseline before the
> training was built. That's a decision point for next time: if you want
> that level of evidence, we need to be part of the conversation from the
> beginning."*

---

## Evaluation Baked Into Design — The Checklist

Before finalizing the design document, the designer confirms:

- [ ] What level(s) of evaluation has the customer requested?
- [ ] What is the customer's stated reason for that level?
- [ ] Is the request driven by a genuine organizational need or the
  uninformed yes pattern?
- [ ] Is Level 4 viable given when L&D was brought in?
- [ ] If Level 4 is viable — is baseline data collection confirmed before
  build begins?
- [ ] Are L1/L2 instruments designed into the course before handover?
- [ ] Is L3 observation infrastructure identified and owned (manager,
  QC system, HR)?
- [ ] Is there a named measure of success that the sponsor can confirm?
- [ ] What happens if the training doesn't produce the expected outcome —
  who owns the follow-up conversation?

The last question is the most important. A customer who has no answer to
"what if it doesn't work?" has not committed to evaluation — they have
committed to completion.

---

## Two Closing Philosophies

| Conversation Type | Closing Philosophy |
|---|---|
| **Scope change / resource decision** | Create urgency, name delay cost, get a decision in the room — project stalls without authorization |
| **Evaluation commitment** | Encourage genuine ownership, allow reflection, invite additional stakeholders — commitment quality determines execution |

**The commitment quality principle:**
A customer who says yes under closing pressure but doesn't fully own the
decision will deprioritize 30-60-90 touchpoints when the sprint fills up.

**When to encourage a decision in the room:**
When the customer signals they have the authority and information to decide.

**When to allow reflection:**
When they hesitate — that hesitation carries information. Do not override
it with a closing technique. A pressured yes on an evaluation commitment
produces no follow-through data.

---

*© 2026 Norman Arosemena, CPTD. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Commercial use prohibited without a license.*
