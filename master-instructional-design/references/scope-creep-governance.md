# Scope Creep Governance — Prevention, Classification, and Escalation

**Load when:** Active sprint underway, change request received, governance structure needed, or SME submitting off-schedule changes.

---

## The Root Cause Distinction

Scope creep in L&D projects has two distinct origin points requiring different interventions:

| Origin | Description | Intervention Type |
|---|---|---|
| **Upstream process failure** | Poor intake, incomplete needs analysis, unconfirmed performance gap — the project was built on an unstable foundation | Diagnostic — fix the foundation before build begins |
| **Governance failure** | No role clarity, no review discipline, no change control, mid-project resource changes — stable foundation but no structural containment | Structural — build containment from project kickoff |

**Critical principle:** Content-level scope creep appearing during design and development is almost always a symptom of upstream failure — not the disease itself. Treating the symptom without diagnosing the upstream cause guarantees recurrence.

---

## The Shared Governance Foundation

All projects regardless of complexity share the same governance standards. Complexity changes the negotiation effort required to establish them — not the standards themselves.

**Universal governance elements:**
- Customer approvals at all critical milestones and tollgates
- Standard procedures and artifacts for all macro phases: Intake, Design, Development, Testing, Release Planning, Go Live, Maintenance
- SME time and effort commitment documented at project kickoff
- SME onboarding to the learning team's rhythm of work
- Communications cadence established and agreed before work begins
- Review cycle schedule defined — SMEs know when they will be asked for input and when they will not

**SME education as preventive governance:**
SMEs who understand the rhythm of work and why it is structured the way it is will self-filter before submitting off-schedule changes. Customer education is not a soft skill — it is a preventive governance mechanism. A SME who has been onboarded properly will pause before hitting send.

---

## The Criticality Taxonomy

Every incoming change request is assessed against impact on product quality — not change type, not who submitted it. Criticality is about what the change does to the work.

| Level | Name | Definition | Real-World Example |
|---|---|---|---|
| **A** | Process Stopper | Change so drastic it stops work completely or renders the product unusable | New executive hired who wants to review all training before any further development |
| **B** | Breakdown | Does not stop work but must be addressed before the next milestone; impacts direction or structure | Policy change that affects processes directly referenced in the course; SME wants to resequence approved modules mid-development |
| **C** | Content Adjustment | Addressable at course level; no structural impact | Script change, VO adjustment, screen grab update |
| **D** | Optional Improvement | No impact to product quality; can be deferred | Nice-to-have additions, stylistic preferences, future enhancements |

---

## The Two-Decision Model

Scope creep governance operates on two distinct decisions with different owners:

### Decision 1 — Criticality Assessment

**Owner:** Designer or developer

**Rationale:** They are closest to the work and best positioned to evaluate impact. This is their judgment call — jidoka in practice. They see the abnormality first.

### Decision 2 — Response Execution

**Owner:** Depends on criticality level

| Level | Response Execution Owner |
|---|---|
| **D** | Designer/developer handles independently — queue or absorb |
| **C** | Designer/developer handles within sprint |
| **B** | Designer/developer flags and briefs; learning leader executes response with SME |
| **A** | Designer/developer pulls andon cord immediately; learning leader owns the conversation |

### The Structural Fix for Silent Absorption

The most common scope creep governance failure is the designer or developer absorbing Level B or A changes silently — assessing criticality correctly but not escalating.

Root causes mirror the underestimation problem: fear of appearing incapable, fear of being the bottleneck, desire to protect the SME relationship.

**The fix is not cultural — it is structural.** Escalation is the defined path for Level B and A, not an optional one. The designer holds assessment authority. The learning leader holds execution authority for anything above Level C. That boundary removes the silent absorption decision from the designer's discretion.

---

## The Escalation Protocol

### Designer to Learning Leader — The Briefing

Escalation is not a memo. It is a written document plus a conversation.

**Four elements the designer brings to the escalation briefing:**
1. **Nature of the request** — what exactly is being asked and by whom
2. **Reason for the request** — what is driving it from the SME's perspective
3. **Workload impact** — specific effect on timeline, sprint capacity, and downstream deliverables
4. **Execution plan** — the designer's recommended path forward

**Format principle:** Written documentation enables recall. The conversation provides context that the document cannot fully capture. Both are required. Neither alone is sufficient.

---

### Designer to SME — The Holding Response

In the window between receiving the change request and the learning leader executing the formal response, the designer sends a holding response that:
- Acknowledges receipt explicitly
- Signals the change is being taken seriously
- Communicates next steps and why the request requires process
- Makes no commitment to executing the work
- Commits to treating the request with the respect it deserves

**Tone:** Transparency and partnership. The SME should feel heard and informed — not managed or deflected.

---

## The Agility Principle

Scope creep governance is not rigidity. Agility demands the ability to fail fast and pivot. The governance structure must be permissive enough to welcome legitimate changes and disciplined enough to know when to say no — or not now.

The criticality taxonomy serves agility by making that distinction explicit and consistent:
- A Level C change mid-sprint is absorbed
- A Level B change is processed
- A Level A change stops the line

The decision is principled, not political.

**The hardest governance moment:** When a SME with legitimate organizational authority over the subject matter submits a Level B or A change and expects immediate execution. The governance structure does not disappear because of organizational rank. The learning leader executes the response — not the designer — precisely because that conversation requires equivalent authority on the learning team's side.

---

## Relationship to Evaluation and Definition of Ready

Scope creep governance is downstream of two upstream disciplines:

| Upstream Discipline | How It Prevents Scope Creep |
|---|---|
| **Definition of ready** (see `references/workload-estimation.md`) | Ensures unstable projects don't enter sprints where they generate structural changes mid-build |
| **Evaluation architecture** (see `references/evaluation-architecture.md`) | Ensures success criteria are defined before build — a missing evaluation plan often surfaces mid-project as a scope change |

---

*© 2026 Norman Arosemena, CPTD. [CC BY-NC-ND 4.0](../../../LICENSE) — personal/educational use only; commercial use prohibited.*
