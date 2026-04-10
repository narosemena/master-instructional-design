# Taxonomy Decision Engine — Classification Sequence and Decision Logic

**Load when:** User needs the full classification sequence and decision logic for any learning project.

---

## Foundational Design Principle

> *Accuracy of judgment outranks system fluency. The harder skill to acquire takes sequencing priority.*

This principle governs every split decision where two skill types must be addressed in a single intervention.

---

## The Two-Tier Decision Engine

### Level 1 — First Classification Cut

**The first question asked of any content handed to a designer:**

> "Is this a **change in current performance** or a **brand new performance expectation**?"

| Branch | Definition |
|---|---|
| **Change** | Learner already performs this. Something about the performance must shift — behavior, system, standard, or context. |
| **New** | Learner has never performed this. No prior baseline exists in this specific context. |

**Critical nuance inside Change:**
Change is not uniform. These are meaningfully different design problems:
- Replacing a wrong behavior with a correct one
- Adding a step to an existing process
- Performing the same task in a new system or tool
- Unlearning a deeply habitual behavior *(hardest design problem in the field)*

**Critical nuance inside New:**
New is not uniform either:
- No prior context whatsoever
- Prior knowledge exists in a transferable adjacent domain
- Learner believes they already know it but doesn't *(dangerous — combines New with Change dynamics)*

---

### Level 2 — Content Nature Classification

Applied to both Change and New branches equally.

| Type | Definition |
|---|---|
| **Hard** | System operation, process execution, technical procedure, tool use, compliance behavior — observable, measurable, right/wrong verifiable |
| **Soft** | Judgment, communication, leadership, relationship, decision-making under ambiguity — contextual, harder to observe, harder to measure |
| **Mixed** | Intervention requires both hard and soft skill development; the two are operationally inseparable in the moment of performance |

**The 2×3 taxonomy matrix — the core output of classification:**

| | Hard | Soft | Mixed |
|---|---|---|---|
| **Change** | ② | ③ | ⑤ |
| **New** | ① | ④ | ⑥ |

---

## MVP Priority Ranking (by real-world frequency)

| Priority | Cell | Frequency Rationale |
|---|---|---|
| 1 | **Hard-New** ① | Most common enterprise trigger: system implementations, new processes, compliance |
| 2 | **Hard-Change** ② | Second most common: system upgrades, process redesigns, policy shifts |
| 3 | **Soft-Change** ③ | Frequent: behavior shift initiatives, leadership development, culture change |
| 4 | **Soft-New** ④ | Less common: organizations rarely hire for zero soft skill baseline |
| 5 | **Mixed-Change** ⑤ | Complex: role evolution requiring simultaneous hard and soft redesign |
| 6 | **Mixed-New** ⑥ | Rarest: new role creation, major organizational transformation |

**MVP scope:** Full depth on cells 1, 2, 3, 4. Structural guidance + complexity flag on cells 5, 6.

---

## Level 3 — The Keep-Together vs. Separate Decision (Mixed Only)

When content is classified as Mixed (cells ⑤ or ⑥), the designer must decide whether to treat hard and soft skills within a single intervention or as separate sequential interventions.

### Decision Rule

| Condition | Recommendation |
|---|---|
| **Judgment/soft skill already present** in learner (from experience, industry standards, education, or combination) | Keep together. Prioritize hard skill. Pepper in exceptions to standards as they apply to the specific environment. |
| **Judgment/soft skill NOT yet present** | Separate into two distinct interventions. Assess most logical sequence to shorten time to proficiency. |

### Sequencing Principle
The harder-to-acquire skill takes sequencing priority. Judgment accuracy outranks system fluency because:
- Judgment is harder to develop
- Judgment errors have higher downstream consequence
- System navigation can be supported with job aids; poor judgment cannot

### Sequence Dependency
The soft/judgment skill generally precedes the hard/system skill — **unless** the learner already possesses the judgment capability, in which case the sequence can begin with the hard skill and use the system context to surface judgment application.

→ Full Mixed excavation: `references/mixed.md`

---

## Level 4 — Verifying Prior Capability Claims

### The Core Problem
Self-reported prior knowledge ≠ transferable capability. A learner can have extensive experience in an adjacent domain where judgment criteria partially overlap but differ meaningfully enough to cause systematic errors.

### Verification Protocol

**Step 1 — SME Intake Query**
Ask the SME directly. Use these three lines of inquiry:
1. Clear definition of job description and role expectations
2. Success metrics in this specific context
3. Failure occurrence patterns — *"Are errors in judgment a recurrent issue, or does it tilt more toward system errors?"*

**Step 2 — Read the SME**
- Confident, specific answer → provisionally accept, document the claim
- Hesitation → probe deeper using the three lines above
- Ask explicitly: *"How confident are you about this?"*
- Document the confidence level alongside the claim

**Step 3 — Independent Evidence Sources**
Do not rely on SME confidence alone. Seek corroborating evidence:
- Performance data
- Incident reports
- Job descriptions and role requirements
- Quality metrics and error logs

**Step 4 — Minimum Viable Verification (evidence-desert environments)**
When no historical data exists (new role, new organization, greenfield):
- **Preferred:** On-the-job observation *(discreet, preserves learner dignity, yields behavioral data without triggering defensiveness)*
- Encode the assumption formally in job description or role goals as a documented departure point
- Flag as unverified assumption in design documentation

### Observation Protocol Note
Observation has a sampling problem: routine performance may appear competent while edge case judgment remains untested. Structure the observation window where possible to include exposure to ambiguous or non-routine situations.

---

## Level 5 — When Verification Fails (Pilot Reveals Wrong Assumption)

When pilot data contradicts the SME's intake claim about prior capability:

### Design Response
1. Create a new vertical to treat the missing skill specifically
2. Do not collapse it into the existing intervention
3. Document the distinction explicitly with rationale
4. Articulate why separation is recommended and how the two verticals connect at the moment of performance

### Required Skill Outputs at This Decision Point

| Artifact | Purpose |
|---|---|
| **Diagnosis statement** | Plain language explanation of what the data revealed and why it changes the design classification |
| **Recommendation document** | New vertical proposal with sequencing rationale in non-ID stakeholder language |
| **Conversation guide** | How to deliver the finding without making the SME lose face |

---

## Reference File Cascade

| Classification Result | Primary Reference | Supporting References |
|---|---|---|
| Hard-New ① | `references/hard-new.md` | `references/workload-estimation.md`, `references/sme-governance.md` |
| Hard-Change ② | `references/hard-change.md` | `references/stakeholder-communication.md` |
| Soft-Change ③ | `references/soft-change.md` | `references/inclusive-emotional-design.md` |
| Soft-New ④ | `references/soft-new.md` | `references/soft-change.md` |
| Mixed-Change ⑤ | `references/mixed.md` | `references/hard-change.md`, `references/soft-change.md` |
| Mixed-New ⑥ | `references/mixed.md` | `references/hard-new.md`, `references/soft-new.md` |

**Always load alongside any classification:**
- `references/scope-creep-governance.md` — when project is in active sprint
- `references/evaluation-architecture.md` — when evaluation has not been discussed
- `references/designer-developer-handover.md` — when design-development transition is approaching

---

*© 2026 Norman Arosemena, CPTD. [CC BY-NC-ND 4.0](../../../LICENSE) — personal/educational use only; commercial use prohibited.*
