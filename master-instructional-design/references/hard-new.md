<!-- hard-new.md -->

# Hard-New — Full Workflow

Brand new performance expectation. Hard skill. Learner has no prior baseline
in this specific context. This is the most common enterprise design scenario.

---

## The Most Common Design Mistake

**Jumping straight to design without auditing the existing ecosystem.**

Two distinct failure modes produce this mistake:

- **Ignorance:** The junior ID genuinely doesn't know to look. Design is what
  they were trained to do, so they design.
- **Creation bias:** The junior ID knows they should check but unconsciously
  favors building. Building is more visible, more creative, and more
  portfolio-worthy than curating. This is a motivation gap dressed as a
  process gap.

These require different interventions. Ignorance needs a protocol. Creation
bias needs a reframe — the designer's job is to close the performance gap by
the most efficient means, not to produce artifacts.

**The downstream consequence of skipping the audit:**
A full suite of learning solutions is designed and developed when that was
not necessary. This is a complete waste event — the highest category of
educational waste in Lean/TPS terms.

---

## The Ecosystem Audit Protocol

**Trigger:** Before any design decision is made on a Hard-New classification.

**Sources to check (no fixed order):**
1. Verify the SLA for the tool, system, or solution — check for clauses
   covering training or performance provisioning of any type
2. Check internal resources — enterprise-wide repositories (LMS),
   department-specific training, current documentation (user manuals,
   help portals, in-tool help functions)
3. Check vendor content providers and externally licensed content libraries

**The parallel HR check:**
Ask the SME team directly: *"Are there any plans to cover this skill gap
through hiring, promoting, or relocating staff who already have this skill?"*
This surfaces a parallel HR track that would make the intervention redundant
before it starts. It cannot be detected through a content audit.

---

## Audit Exit Criteria

The audit is complete — and the designer may proceed — when all three of the
following are confirmed by the SME team:

1. There are no provisions for performance support in any vendor agreement
2. There is no in-house training for this skill or system
3. Any content found in the LMS has been reviewed and confirmed by the SME
   team as not accurate, current, or relevant enough to satisfy the need

**Critical principle:** Exit criteria are SME-confirmed, not self-declared.
A junior ID cannot exit the audit by deciding they've looked enough. They
exit when a human with organizational knowledge has confirmed the negative.

---

## The Partial Match Decision (60/40 Scenario)

When existing content covers part of the need but not all of it:

**The anchor trap:** Junior IDs tend to anchor their design around the
existing content rather than around the performance requirement. The existing
content becomes the spine of the intervention and the developed portion gets
bolted on. The result is a solution shaped by what existed rather than by
what the learner needs to do.

**The correct sequence:**
1. Build learning objectives independently — before reviewing what the
   existing content contains
2. Hold the existing content against those objectives — not the reverse
3. Evaluate using the quality audit rubric below
4. Then decide: embed + develop, curate additional, or supplement

**The trade-off:**
Curating is the most time and cost efficient approach but trades
customization and tailoring for convenience. The decision is driven by
budget, timeline, and audience characteristics (co-location, technology
access, language, prior knowledge, etc.)

---

## Existing Content Quality Audit Rubric

Applied when evaluating vendor-provided, externally sourced, or internally
existing content for potential incorporation.

**Access requirement:** The learning team must explicitly request access to
the content to execute this audit. This must be scoped into the project
timeline — it is not a free activity.

**Four evaluation dimensions (assess in this order):**

| # | Dimension | What to Evaluate |
|---|---|---|
| 1 | **Overall content architecture** | How is the content structured? Does the structure serve the learning need or create friction? |
| 2 | **Content modality/ies** | Do the modalities offered match the performance requirement and learner context? |
| 3 | **Instructional design standards** | Are objectives, goals, knowledge checks, and other ID artifacts present and at required standards? |
| 4 | **Subject matter integrity** | Is all needed content present — concepts, processes, tasks, sub-tasks, exceptions, error paths, correct terminology? |

**The disqualifying condition:**
There is no single universal disqualifier — any dimension can be a deal
breaker depending on the specific need. Criticality is contextual.

*Example of an absolute disqualifier:* Content available only in a language
the learner population does not speak. No other evaluation is needed.

**The ID goggles test:**
The designer reviews existing content as a learner would experience it,
while simultaneously evaluating it as a designer. This dual lens is what
distinguishes a genuine quality audit from a checkbox review.

---

## The Five-Stage Fidelity Ladder

No gate is skipped regardless of timeline pressure. Each gate earns the next.

| Stage | Artifact | Fidelity | Owner | SME Question |
|---|---|---|---|---|
| **Gate 1** | Learning Proposal | Conceptual | ID | Is this the right problem, direction, and scope? |
| **Gate 2** | Mind Map | Structural | ID | Is this the right flow, chunking, and interaction approach? |
| **Gate 3** | Script | Instructional | ID | Is the content accurate, complete, and correctly sequenced? |
| **Pre-build** | Placeholder prototype | Experiential-partial | Developer | Does this feel right as a learner experience before full build? |
| **Full build** | Complete course | Experiential-full | Developer | Final QA and approval |

---

## Gate 1 — The Learning Proposal

**Fidelity level: Conceptual**

**Required elements:**
- Results of needs analysis (conducted by ID or inherited from trusted source)
- Learning objectives
- Business objectives being addressed
- KPIs, OKRs, or metrics the solution is expected to move
- Content domains included — concepts, ideas, processes
- Proposed modality — eLearning, ILT, hybrid, blended
- Content chunking logic — modules, lessons, chapters
- Logical flow of content

**Critical constraint:** The proposal presents the problem and the
architecture — it does not go into solution-level detail. SMEs approve
direction, not design.

**Format:** Document usable as a presentation. Built for a non-ID audience.

---

## Gate 2 — The Mind Map

**Fidelity level: Structural**

**Structure:** Hierarchical branching from approved proposal topics to
slide/screen level specificity.

*Example:*
- Mother branch → Module 1: QC System Basics
- Child branch 1 → Access Requirements
- Grandchild branch 1.1 → Card flip activity: Learners flip cards with
  icons to learn about criteria for system access [Role, Job level,
  Training requisites, Manager approval]
- Child branch 2 → Installing the Application

**Why two gates are necessary:**
SMEs consistently struggle to visualize learner experience from text-based
proposal elements alone. The mind map bridges the gap between conceptual
approval and experiential fidelity. It catches misalignment at structural
level before high-fidelity assets are built.

**What Gate 2 catches that Gate 1 doesn't:**
- Interaction types that don't match the content
- Sequencing that makes sense on paper but breaks at screen level
- Content the SME approved in principle but rejects when mapped to a
  specific learner moment
- Missing sub-topics not visible at the proposal level

---

## Gate 3 — The Script

**Fidelity level: Instructional**

When design and development are split roles, a third gate artifact is
required before development begins.

**Format:** Built directly in the authoring tool (e.g., Articulate 360).

**Required elements per slide/screen:**
- Scenes and slides organized to serve the build sequence
- Voice over text for all characters — narrator, avatars, scene dialogue
- A Developer Layer with explicit instructions: number of needed layers,
  interaction details, feedback text, on-screen text vs. VO-only decisions,
  callout specifications
- Blank canvas — populated by the designer at specified fidelity

**Critical principle:** The script contains both explicit direction AND
surrounding context — notes, callouts, critically flagged elements — so
the developer can walk out of the handover session confident enough to
begin work independently.

---

## The Pre-Build Layer

**Owner:** Developer
**Purpose:** Provide reviewers and SMEs with experiential fidelity before
full build investment.

**Method:** Build a representative subset of the full interaction at full
fidelity. Leave the remainder at script level for content validation.

*Example:* An interaction with 8 flip cards → developer builds 2 at full
fidelity. SMEs validate all 8 cards content in the script AND experience
the learner view through the 2 built cards.

---

## The Handover — A Co-Authoring Kickoff

The handover meeting is the kickoff of a co-authoring and co-development
process — not a handoff after which the designer exits.

**Designer responsibilities post-handover:**
- Remain on call for clarification and questions throughout the build
- Flag critical elements explicitly in the script

**Developer creative liberty:**
Developers have creative liberty to challenge anything — interaction design,
architecture, branding, graphic style, VO style. The designer holds firm
only when a proposed change threatens learner experience quality or product
goals — and must articulate specifically why.

---

## Designer-Developer Negotiation Framework

**The north star:** Design for the best possible learner experience within
the tech stack. When development constraints push back, negotiate toward
**equivalent value** — a different path to the same learning outcome.

**Equivalent value** is only operable if the designer can articulate
precisely what learning value the original design was delivering.
"It's more realistic" is not a defensible argument. The specific cognitive
and behavioral outcomes the learner achieves is the only defensible argument.

**The negotiation solution stack:**

| Priority | Option | Trade-off |
|---|---|---|
| **1** | Bring additional developer capacity for this interaction only | Adds cost, preserves scope and quality |
| **2** | Decompose into representative scenario subset | Preserves cognitive complexity through principled selection |
| **3** | Outsource the interaction to a specialized vendor | Maintains quality; adds coordination overhead |
| **4** | Return to customer with transparent scope conversation | Resets expectations; customer becomes part of the decision |

**On Option 4:** Junior IDs are most afraid of this conversation. Shipping
a compromised product to avoid a difficult conversation is the greater
failure.

---

## Scenario Selection Protocol

When decomposing a complex interaction into a representative subset:

**Selection criteria hierarchy:**

| Priority | Criterion | Operational Definition |
|---|---|---|
| **1** | **Frequency (Pareto)** | Which 20% of case types account for 80% of real job occurrences? Pull from operational records. |
| **2** | **Failure pattern** | Which errors appear most frequently in internal audit records? |
| **3** | **Transferability** | Which scenarios, once mastered, give the learner reasoning tools to handle unpracticed variants? Requires SME expertise. |

**Four-step selection process:**
1. Pull operational frequency data and audit failure records independently
2. Present data-derived findings to SME for confirmation — not selection
3. Ask SME: *"If a learner masters these scenarios, which other situations
   would they handle without explicit training?"*
4. Designer synthesizes and proposes final set with documented rationale

**Accountability:** The designer owns the selection logic and the proposal.
The SME owns the operational validation. These are distinct responsibilities.

---

## SME Governance Model

SME management is a **governance problem, not a relationship problem.**

**SME Ecosystem Mapping — document at first discovery meeting:**
- Who has subject matter knowledge
- Who has approval authority
- Who has political veto power without a formal role
- Who needs to be kept informed without approval authority
- Time and effort commitment per role
- Approval process and artifact walkthrough schedule

**Simple projects — Single SME POC model:**
One SME serves as point of contact AND liaison to secure escalation approvals.

**Complex projects — Lead SME consolidation model:**
Used when multiple SME teams have conflicting or opposing standards.
Lead SME responsibilities:
- Internal consolidation of SME input before it reaches the learning team
- Final validation of content accuracy across all contributing SMEs
- Dispute resolution within the SME team

**Dispute resolution authority:** Assign early and explicitly — who has
decision power, and who has ultimate authority to break disputes. Document
at project initiation, not mid-project when conflict surfaces.

---

## Workload Estimation — Hard-New Specific

**The two-owner estimation model:**

**Owner 1 — The Designer estimates:**
- Discovery and needs analysis work
- Proposal drafting (heaviest lift)
- Mind map drafting
- Script drafting
- Handover session planning and execution

**Owner 2 — The Developer estimates:**
- Pre-build scope and effort
- Full build scope and effort

The quality of the designer's output directly determines the accuracy of
the developer's estimate. A vague script produces a wide, unreliable
estimate.

**The primary estimation destroyer — SME involvement:**
SME availability, responsiveness, and engagement quality is the single
most reliable source of estimation error. It almost never appears as an
explicit variable in a junior ID's estimation model.

**The uncertainty buffer:**
Add 10–50% to base estimate based on assessed project uncertainty.
This is not a mathematical formula. It is a principled range applied
with judgment.

**Uncertainty calibration — three diagnostic levels:**

*Level 1 — Nature of the request:*
- Clear operational need → Low uncertainty
- Knee-jerk executive reaction with emotional token attached → High uncertainty

*Level 2 — Support system maturity:*
- Most support systems present and documented → Low uncertainty
- Most support systems missing or undocumented → High uncertainty

*Level 3 — Current state of the work:*
- Work currently performed successfully by this team → Low uncertainty
- Brand new to the industry with no benchmark → High uncertainty

**Definition of ready — hard pass/fail:**
> Can this problem be solved by a learning intervention? If no — do not
> assign. Hold in backlog until root cause is confirmed as a learning
> and performance gap.

---

*© 2026 Norman Arosemena, CPTD. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Commercial use prohibited without a license.*
