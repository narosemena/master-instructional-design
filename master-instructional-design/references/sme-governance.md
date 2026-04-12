<!-- sme-governance.md -->

# SME Governance Model

---

## Core Principle

SME management is a **governance problem, not a relationship problem.**

Junior IDs default to relationship behaviors — stay friendly, send
updates, be responsive. That is insufficient. The correct approach is
structural: assign roles, decision rights, escalation paths, and
consolidation responsibilities before the work starts.

---

## The SME Involvement Curve

SME involvement is not constant across a project. It spikes at
predictable points and must be planned for — not reacted to.

| Phase | SME Involvement Level | Driver |
|---|---|---|
| Project kickoff | Low | Awareness only |
| Discovery | High spike | Designer needs SME time to surface, validate, and map all subject matter |
| Internal production | Low trough | Learning team working independently |
| Review cycles | High spike(s) | Multiple review gates from proposal through full build |
| Final approval | Medium | Sign-off and closure |

**Why elapsed time does not equal active work time:**
SME-driven elapsed time is the gap between them. A designer working
at full capacity still waits — for SME availability, feedback
turnaround, and alignment meetings. None of this appears as active
work hours but all of it appears on the calendar.

**Estimation implication:** SME availability is the single most
reliable estimation destroyer. Account for it explicitly — not as
a single line item but as a variable at each project phase.

---

## SME Ecosystem Mapping

**When:** First discovery meeting if possible. If not, establish the
times and spaces needed to onboard the SME team immediately after.

**Where:** Documented in the project management system at project
initiation.

**What to document:**
- Who has subject matter knowledge
- Who has approval authority
- Who has political veto power without a formal role
- Who needs to be kept informed without being given approval authority
- Time and effort commitment per role
- Approval process and artifact walkthrough schedule

---

## The Approver vs. Knower Gap

The person who attends the Gate 1 proposal review is often not the
same person whose knowledge the content depends on. A manager approves
the architecture. The frontline SME who actually knows whether the
interaction represents the work accurately is downstream — sometimes
not consulted until Gate 3 or later.

By the time that frontline SME sees the content, you're at storyboard
or prototype fidelity. Changes at that point are expensive,
scope-expanding, and relationship-damaging.

**The fix:** Map approvers and knowers separately at project initiation.
Never assume they are the same person.

---

## SME Role Architecture

### Simple Projects — Single SME POC Model

One SME serves as point of contact AND operates as liaison to secure
approvals requiring escalation.

**When to use:** One SME, clear authority, no competing standards.

**Benefits:**
- Clean accountability
- Minimal coordination overhead
- Single source of truth for content decisions

---

### Complex Projects — Lead SME Consolidation Model

Used when multiple SME teams are involved — especially when teams may
have conflicting or opposing standards.

*Example: Multiple QA teams from different business areas using the
same platform with different evaluation criteria.*

**Lead SME responsibilities:**
- Internal consolidation of SME input before it reaches the learning
  team
- Final validation of content accuracy across all contributing SMEs
- Dispute resolution within the SME team

**When to use:**
- Multiple SMEs from different departments
- Competing or conflicting standards across teams
- Subject matter that spans more than one organizational unit
- High political complexity in the SME ecosystem

---

## Dispute Resolution Authority

**Assign early and explicitly.** Who has decision power, and who has
ultimate authority to break disputes?

Document at project initiation — not negotiated mid-project when a
conflict surfaces.

**The failure mode:** When dispute resolution authority is undefined,
every SME conflict escalates to the designer, who has neither the
organizational authority nor the positional power to resolve it.
The project stalls. The designer is blamed for a governance failure
that predates their involvement.

---

## SME Onboarding — The Rhythm of Work Conversation

SMEs who understand the rhythm of work and why it is structured the
way it is will self-filter before submitting off-schedule changes.

**Onboarding agenda for SME kickoff:**
1. Why the process is staged — what each gate does and why the sequence
   matters
2. What we need from you and when — specific time commitments per phase
3. What happens when changes come in outside of review cycles —
   the criticality taxonomy and how we handle it
4. How decisions get made — approval authority, escalation path,
   dispute resolution
5. What the learning team owns vs. what the SME owns — explicit
   boundary setting

**The boundary statement:**
> *"You are the expert on what the work requires. We are the experts
> on how to build a learning experience that produces it. Our job is
> to translate your expertise into something a learner can acquire.
> We will always bring you back to validate the content — but the
> design decisions are ours to make."*

---

## SME Verification Protocol

When a SME makes a claim about the learner population — prior
knowledge, existing capability, performance baseline — do not accept
it at face value.

**Three lines of inquiry before accepting a SME claim:**
1. **Job description clarity** — What does the role actually require?
   Is the claimed capability in the formal requirements?
2. **Success metrics** — How is performance measured in this role?
   Does the metric require the claimed capability?
3. **Failure occurrence patterns** — *"Are errors in judgment a
   recurrent issue, or does it tilt more toward system errors?"*

**Reading the SME:**
- Confident, specific answer → provisionally accept, document the claim
- Hesitation → probe deeper using the three lines above
- Ask explicitly: *"How confident are you about this?"*
- Document the confidence level alongside the claim

**Independent evidence sources:**
Do not rely on SME confidence alone. Seek corroborating evidence:
- Performance data
- Incident reports
- Job descriptions and role requirements
- Quality metrics and error logs

**The proxy approval failure mode:**
A confident SME who is wrong about what their learner population
knows is the most dangerous intake condition. Confidence is not
accuracy. Documentation of the claim protects the designer. It does
not improve the design decision made on bad data.

---

## Minimum Viable Verification — Evidence-Desert Environments

When no historical data exists (new role, new organization, greenfield):

**Preferred:** On-the-job observation
- Discreet — preserves learner dignity
- Behavioral — yields observable data without triggering defensiveness
- Does not require learner awareness

**Observation sampling problem:**
Routine performance may appear competent while edge case judgment
remains untested. Structure the observation window where possible
to include exposure to ambiguous or non-routine situations.

**If observation is not possible:**
Encode the assumption formally in job description or role goals as a
documented departure point. Flag as unverified assumption in design
documentation.

---

## Critical Governance Principle

> *Maximize visibility to all roles as early as possible. SME
> management is a structural discipline — roles, rights, and
> escalation paths are assigned before the work begins, not managed
> reactively as conflicts emerge.*

---

## SME Behavior Patterns and Design Responses

| SME Behavior | What It Signals | Design Response |
|---|---|---|
| Submits changes outside review cycles | Not onboarded to rhythm of work | Revisit onboarding; apply criticality taxonomy to the change |
| Hesitates when asked about learner capability | Uncertainty about the population | Probe with three lines of inquiry; seek independent evidence |
| Wants to drive design decisions | Doesn't understand the boundary | Restate the boundary explicitly and collegially |
| Escalates every decision to executive | Lacks approval authority | Identify and engage the actual decision-maker directly |
| Goes silent during review cycles | Overloaded or disengaged | Escalate to learning leader; do not absorb the delay silently |
| Submits conflicting standards with other SMEs | Lead SME consolidation needed | Assign or escalate to Lead SME; do not mediate between SMEs directly |

---

*© 2026 Norman Arosemena, CPTD. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Commercial use prohibited without a license.*
