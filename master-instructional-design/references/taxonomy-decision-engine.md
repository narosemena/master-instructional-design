<!-- taxonomy-decision-engine.md -->

# Taxonomy Decision Engine

This file contains the classification logic that routes every project to the correct
workflow. It is the entry point for all Project Mode engagements. Load this file first.
Do not skip the classification sequence — every design decision downstream depends on
the correct classification result.

---

## Foundational Design Principle

> *Accuracy of judgment outranks system fluency. The harder skill to acquire takes
> sequencing priority.*

This principle governs every split decision where two skill types must be addressed
in a single intervention.

---

## The Two-Tier Decision Engine

This skill operates on two levels simultaneously:

**Macro level:** Treatment selection for the full intervention — modality, architecture,
sequencing, blended approach.

**Micro level:** Treatment selection for each individual content block — which interaction
type, which practice method, which feedback approach serves this specific piece of content.

The taxonomy drives the macro level. The micro-level engine is a separate reference file.
Both must be active for complete design intelligence.

---

## Level 1 — First Classification Cut

**The first question asked of any project:**

> "Is this a **change in current performance** or a **brand new performance expectation**?"

| Branch | Definition |
|---|---|
| **Change** | Learner already performs this. Something about the performance must shift — behavior, system, standard, or context. |
| **New** | Learner has never performed this. No prior baseline exists in this specific context. |

### Critical nuances inside Change

These are meaningfully different design problems — do not treat them as equivalent:

- Replacing a wrong behavior with a correct one
- Adding a step to an existing process
- Performing the same task in a new system or tool
- Unlearning a deeply habitual behavior *(hardest design problem in the field)*

### Critical nuances inside New

New is not uniform either:

- No prior context whatsoever
- Prior knowledge exists in a transferable adjacent domain
- Learner believes they already know it but doesn't *(dangerous — combines New with
  Change dynamics)*

---

## Level 2 — Content Nature Classification

Applied to both Change and New branches equally at this level.

| Type | Definition |
|---|---|
| **Hard** | System operation, process execution, technical procedure, tool use, compliance behavior — observable, measurable, right/wrong verifiable |
| **Soft** | Judgment, communication, leadership, relationship, decision-making under ambiguity — contextual, harder to observe, harder to measure |
| **Mixed** | Intervention requires both hard and soft skill development; the two are operationally inseparable in the moment of performance |

---

## The Core Taxonomy Matrix

| | Hard | Soft | Mixed |
|---|---|---|---|
| **New Performance** | ① Hard-New | ④ Soft-New | ⑥ Mixed-New |
| **Change in Performance** | ② Hard-Change | ③ Soft-Change | ⑤ Mixed-Change |

---

## MVP Priority Ranking

| Priority | Cell | Frequency Rationale |
|---|---|---|
| 1 | **Hard-New** | Most common enterprise trigger: system implementations, new processes, compliance |
| 2 | **Hard-Change** | Second most common: system upgrades, process redesigns, policy shifts |
| 3 | **Soft-Change** | Frequent: behavior shift initiatives, leadership development, culture change |
| 4 | **Soft-New** | Less common: organizations rarely hire for zero soft skill baseline |
| 5 | **Mixed-Change** | Complex: role evolution requiring simultaneous hard and soft redesign |
| 6 | **Mixed-New** | Rarest: new role creation, major organizational transformation |

**Full depth coaching:** Cells 1, 2, 3, 4
**Structural guidance + complexity flag:** Cells 5, 6

---

## Classification Routing

Once classification is confirmed, load the corresponding reference file:

| Classification | Primary Reference | Supporting References |
|---|---|---|
| Hard-New | `hard-new.md` | `workload-estimation.md`, `sme-governance.md` |
| Hard-Change | `hard-change.md` | `stakeholder-communication.md` |
| Soft-Change | `soft-change.md` | `inclusive-emotional-design.md` |
| Soft-New | `soft-new.md` | `soft-change.md` |
| Mixed-Change | `mixed.md` | `hard-change.md`, `soft-change.md` |
| Mixed-New | `mixed.md` | `hard-new.md`, `soft-new.md` |

**Always load alongside any classification:**
- `scope-creep-governance.md` — when project is in active sprint
- `evaluation-architecture.md` — when evaluation has not been discussed
- `designer-developer-handover.md` — when design-development transition is approaching

---

## Classification Diagnostic Questions

Ask these before confirming classification. Do not proceed to routing until all
answers are known or documented as assumptions.

1. Is the learner population currently performing any version of this task?
2. If yes — what specifically needs to change about how they perform it?
3. If no — does any transferable prior knowledge exist in an adjacent domain?
4. Is the performance primarily procedural (hard), judgment-based (soft), or both (mixed)?
5. If mixed — does the learner already possess the judgment component, or is that also new?
6. What does the SME say about prior learner capability — and how confident are they?
7. Is there independent evidence (performance data, incident reports, job descriptions)
   that corroborates or contradicts the SME's claim?

---

## The Hidden Reclassification Trigger — Soft-New

**Critical warning:** Soft-New projects almost always contain a hidden Change component.

A learner with strong general interpersonal competence is often harder to develop in
a specific soft skill than a learner with no competence at all — because existing
patterns interfere with new acquisition even when they are not formally wrong.

**Before committing to a Soft-New acquisition design, always run the prior scaffolding
diagnostic:**

Ask the SME: *"What other types of work demand a similar performance from this
population?"*

If relevant prior scaffolding exists — reclassify as Soft-Change or Transfer before
designing. The design changes completely.

**Reclassification outcomes:**

| Outcome | Condition | Design Path |
|---|---|---|
| **Pure Soft-New** | No relevant prior scaffolding | True acquisition — build mental models from ground up |
| **Hidden Soft-Change** | Existing scaffolding conflicts with new skill | Unlearning required first — apply Soft-Change protocol |
| **Transfer opportunity** | Relevant scaffolding in adjacent domain | Adapt existing models — do not rebuild from scratch |
| **Mixed foundation** | Heterogeneous cohort | Separate populations or use expert augmenter model |

---

## Classification Confirmation Protocol

Before routing to a cell reference file, confirm classification explicitly:

> *"Based on what you've shared, I'm classifying this as [Cell Name]. This means
> [one-sentence description of what that classification implies for design].
> Does that match your understanding of the project?"*

Do not proceed without explicit confirmation. A misclassification at this stage
produces wrong design recommendations at every subsequent stage.

---

*© 2026 Norman Arosemena, CPTD. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Commercial use prohibited without a license.*
