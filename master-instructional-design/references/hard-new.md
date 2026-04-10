# Hard-New (Cell ①) — Design Reference

**Load when:** Classification result is Hard-New. Covers ecosystem audit, fidelity ladder, pre-build approval gates, and designer-developer handover. SME governance covered in `references/sme-governance.md`. Workload estimation covered in `references/workload-estimation.md`.

---

## The Most Common Hard-New Design Mistake

**Jumping straight to design without auditing the existing ecosystem.**

This is the cardinal Hard-New error. Before a single design decision is made, the designer must verify that a solution does not already exist — internally or externally.

Two distinct failure modes produce this mistake:

| Failure Mode | Root Cause | Required Intervention |
|---|---|---|
| **Ignorance** | Junior ID genuinely doesn't know to look; design is what they were trained to do | Process — provide the audit protocol |
| **Creation bias** | Junior ID knows they should check but unconsciously favors building; building is visible, creative, and portfolio-worthy | Reframe — the designer's job is to close the performance gap by the most efficient means, not to produce artifacts |

---

### The Downstream Consequence

A full suite of learning solutions is designed and developed when that was not necessary — because:
- A vendor already provides training as part of an SLA
- Existing training already lives in the LMS or content library
- Learners are being hired, promoted, or relocated with the skill already in place

This is a complete waste event. In Lean/TPS terms: the highest category of educational waste.

---

## The Ecosystem Audit Protocol

**Trigger:** Before any design decision is made on a Hard-New classification.

**Sources to check (no fixed order):**
1. Verify the SLA for the tool, system, or solution — check for clauses covering training or performance provisioning of any type
2. Check internal resources — enterprise-wide repositories (LMS), department-specific training, current documentation (user manuals, help portals, in-tool help functions)
3. Check vendor content providers and externally licensed content libraries

**The parallel HR check:**
Ask the SME team directly: *"Are there any plans to cover this skill gap through hiring, promoting, or relocating staff who already have this skill?"*

This surfaces a parallel HR track that would make the intervention redundant before it starts. It cannot be detected through a content audit.

---

### Audit Exit Criteria

The audit is complete — and the designer may proceed — when all three of the following are confirmed **by the SME team**:

1. There are no provisions for performance support in any vendor agreement
2. There is no in-house training for this skill or system
3. Any content found in the LMS has been reviewed and confirmed by the SME team as not accurate, current, or relevant enough to satisfy the need

**Critical principle:** Exit criteria are SME-confirmed, not self-declared. A junior ID cannot exit the audit by deciding they've looked enough. They exit when a human with organizational knowledge has confirmed the negative.

---

## The Partial Match Decision (60/40 Scenario)

When existing content covers part of the need but not all of it:

**The anchor trap:** Junior IDs tend to anchor their design around the existing content rather than around the performance requirement. The existing content becomes the spine of the intervention and the developed portion gets bolted on. The result is a solution shaped by what existed rather than by what the learner needs to do.

**The correct sequence:**
1. Build learning objectives independently — before reviewing what the existing content contains
2. Hold the existing content against those objectives — not the reverse
3. Evaluate using the quality audit rubric below
4. Then decide: embed + develop, curate additional, or supplement

**The trade-off:**
Curating is the most time and cost efficient approach but trades customization and tailoring for convenience. The decision is driven by budget, timeline, and audience characteristics (co-location, technology access, language, prior knowledge, etc.)

---

## Existing Content Quality Audit Rubric

Applied when evaluating vendor-provided, externally sourced, or internally existing content for potential incorporation.

**Access requirement:** The learning team must explicitly request access to the content to execute this audit. This must be scoped into the project timeline — it is not a free activity.

**Four evaluation dimensions — assess in this order. Each gate must pass before proceeding to the next:**

| # | Dimension | What to Evaluate |
|---|---|---|
| 1 | **Overall content architecture** | How is the content structured? Modules, lessons, capsules, paths? Does the structure serve the learning need or create friction? |
| 2 | **Content modality/ies** | Do the modalities offered (video, text, simulation, etc.) match the performance requirement and learner context? |
| 3 | **Instructional design standards** | Are objectives, goals, knowledge checks, and other ID artifacts present and at required standards? Is the content instructionally sound? |
| 4 | **Subject matter integrity** | Is all needed content present — concepts, processes, tasks and sub-tasks, exceptions, error paths, correct terminology and language? |

**The disqualifying condition:**
There is no single universal disqualifier — any dimension can be a deal breaker depending on the specific need. Criticality is contextual. However, some conditions are absolute regardless of other dimensions.

*Example of an absolute disqualifier:* Content available only in a language the learner population does not speak. No other evaluation is needed — stop at dimension 1.

**The ID goggles test:**
The designer reviews existing content as a learner would experience it, while simultaneously evaluating it as a designer. This dual lens — experiencing and assessing simultaneously — is what distinguishes a genuine quality audit from a checkbox review.

---

## The Two Pre-Build Approval Gates

**The second most common Hard-New mistake:** Running to the keyboard without a plan. No pre-build alignment with SMEs before development begins.

The correct discipline: **two sequential approval gates before touching a single slide.** Each gate earns the right to the next level of investment. This is a staggered fidelity model — resolution increases incrementally so SMEs are never asked to approve something they cannot visualize, and the designer never builds at high fidelity on unvalidated content.

---

### Gate 1 — The Learning Proposal

**Fidelity level: Conceptual**
**Purpose:** Align on architecture, scope, and direction before any design decisions are locked.

**Required elements:**
- Results of needs analysis (conducted by ID or inherited from a trusted source)
- Learning objectives
- Business objectives being addressed
- KPIs, OKRs, or metrics the solution is expected to move
- Content domains included — concepts, ideas, processes
- Proposed modality — eLearning, ILT, hybrid, blended
- Content chunking logic — modules, lessons, chapters
- Logical flow of content

**Critical constraint:** The proposal presents the problem and the architecture — it does not go into solution-level detail. SMEs approve direction, not design.

**Format:** Document usable as a presentation. Built for a non-ID audience.

---

### Gate 2 — The Mind Map

**Fidelity level: Structural**
**Purpose:** Add a layer of resolution that shows the SME how the learner will actually move through the content and what each section and interaction will look like — without building it yet.

**Structure:** Hierarchical branching from approved proposal topics to slide/screen level specificity.

*Example:*
- Mother branch → Module 1: QC System Basics
- Child branch 1 → Access Requirements
- Grandchild branch 1.1 → Card flip activity: Learners flip cards with icons to learn about criteria for system access [Role, Job level, Training requisites, Manager approval]
- Child branch 2 → Installing the Application

**Why two gates are necessary:**
SMEs consistently struggle to visualize learner experience from text-based proposal elements alone. The mind map bridges the gap between conceptual approval and experiential fidelity. It catches misalignment at structural level before high-fidelity assets are built — when changes are still low-cost.

**What Gate 2 catches that Gate 1 doesn't:**
- Interaction types that don't match the content
- Sequencing that makes sense on paper but breaks down at the screen level
- Content the SME approved in principle but rejects when they see it mapped to a specific learner moment
- Missing sub-topics that weren't visible at the proposal level

---

## The Fidelity Ladder (Complete Picture)

| Gate | Artifact | Fidelity | SME Question Being Answered |
|---|---|---|---|
| **Gate 1** | Learning Proposal | Conceptual | Is this the right problem, direction, and scope? |
| **Gate 2** | Mind Map | Structural | Is this the right flow, chunking, and interaction approach? |
| **Gate 3** | Storyboard/Prototype | Experiential | Does this feel right as a learner experience? |

Each gate earns the next. No gate is skipped regardless of timeline pressure.

→ Gate 3 (Script and Pre-Build) and handover detail: `references/designer-developer-handover.md`

---

*© 2026 Norman Arosemena, CPTD. [CC BY-NC-ND 4.0](../../../LICENSE) — personal/educational use only; commercial use prohibited.*
