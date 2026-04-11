<!-- designer-developer-handover.md -->

# Designer-Developer Handover Framework

---

## The Core Reframe

The handover meeting is the kickoff of a co-authoring and
co-development process — not a transfer event after which the
designer exits.

**The failure mode:** Designer delivers the script, considers their
job complete, and disengages. Developer encounters ambiguity, makes
judgment calls the designer would not have made, and the learner
experience degrades without either party knowing why.

**The correct model:** Designer remains on call throughout the build.
Their role changes shape — from creator to clarifier — but does not
end at handover.

---

## The Fidelity Ladder — Full Sequence

Each gate earns the next. No gate is skipped regardless of timeline
pressure.

| Stage | Artifact | Fidelity | Owner | SME Question |
|---|---|---|---|---|
| **Gate 1** | Learning Proposal | Conceptual | ID | Is this the right problem, direction, and scope? |
| **Gate 2** | Mind Map | Structural | ID | Is this the right flow, chunking, and interaction approach? |
| **Gate 3** | Script | Instructional | ID | Is the content accurate, complete, and correctly sequenced? |
| **Pre-build** | Placeholder prototype | Experiential-partial | Developer | Does this feel right as a learner experience before full build? |
| **Full build** | Complete course | Experiential-full | Developer | Final QA and approval |

---

## Gate 3 — The Script

**Fidelity level: Instructional**

**Format:** Built directly in the authoring tool (e.g., Articulate 360).

**Required elements per slide/screen:**
- Scenes and slides organized to serve the build sequence
- Voice over text for all characters — narrator, avatars, scene
  dialogue
- A Developer Layer with explicit instructions: number of needed
  layers, interaction details, feedback text, on-screen text vs.
  VO-only decisions, callout specifications
- Blank canvas — populated by the designer at specified fidelity,
  handed to the developer as the build foundation

**Critical principle:** The script contains both explicit direction
AND surrounding context — notes, callouts, critically flagged
elements — so the developer can walk out of the handover session
confident enough to begin work independently.

---

## The Pre-Build Layer

**Owner:** Developer
**Purpose:** Provide reviewers and SMEs with experiential fidelity
before full build investment.

**Method:** Build a representative subset of the full interaction at
full fidelity. Leave the remainder at script level for content
validation.

*Example:* An interaction with 8 flip cards → developer builds 2 at
full fidelity. SMEs validate all 8 cards content in the script AND
experience the learner view through the 2 built cards.

**Why this works:** SMEs can validate content accuracy at script level
and interaction feel at prototype level simultaneously — without the
developer building assets that may require rebuilding after feedback.

---

## The Handover Session — What to Transfer

**Explicit content — in the script:**
- Interaction specifications
- Layer counts and structure
- VO text and character assignments
- Feedback text
- On-screen text vs. VO-only decisions
- Developer layer annotations

**Implicit content — transferred verbally:**
- Judgment calls made during design and why
- Interactions that were considered and rejected
- SME sensitivities around specific content
- Decisions made for learner experience reasons not obvious from
  the artifact
- Non-negotiables vs. areas of creative latitude

**Format principle:** The session is a conversation, not a
presentation. The designer talks the developer through the script
section by section. The developer asks questions. Both parties leave
with shared understanding — not just shared documentation.

---

## Developer Creative Liberty

Developers have creative liberty to challenge anything:
- Interaction design
- Course architecture
- Branding and graphic style
- VO style and character choices
- Build approach and technical implementation

This is a collegial model, not a hierarchical one. The developer's
technical expertise is as valid as the designer's instructional
expertise. Neither overrules the other — they negotiate.

**The designer holds firm only when** a proposed change threatens:
- Learner experience quality
- Achievement of the stated learning objectives
- The product goals the customer approved

**The defensible argument:** Not "I designed it this way." Not "it's
more realistic." The specific cognitive and behavioral outcomes the
learner achieves through the original design — stated precisely —
is the only defensible argument for holding firm.

---

## The Equivalent Value Principle

When a developer proposes simplifying or changing a designed
interaction, the negotiation target is equivalent value — a different
path to the same learning outcome.

**Equivalent value is only operable if the designer can name:**
1. What specific cognitive operations the original design required
   the learner to perform
2. Why those operations are necessary for the performance outcome
3. Whether the proposed alternative produces the same operations

*Example — multi-path QC appeals simulation:*

The simulation's learning value is not realism. It is
**decision-making under realistic conditional complexity.**

The learner must develop five sequential cognitive operations:
1. Read color-coded evaluation status correctly before acting
2. Navigate a non-obvious UI to access filtering (3 clicks from
   base screen)
3. Recognize appeal eligibility based on evaluation status
4. Identify interaction type from the base screen
5. Select the correct appeal template based on that identification

Trimming to one path and one template trains a linear procedure.
The real job requires conditional judgment across multiple variables.
A learner trained on a single path will predictably fail on first
encounter with a non-matching scenario.

**That is the non-negotiable argument.** The trimmed version trains
a skill that does not match the job.

---

## The Negotiation Solution Stack

When full-fidelity build is justified but not achievable within
current constraints:

| Priority | Option | Trade-off |
|---|---|---|
| **1** | Bring additional developer capacity for this interaction only | Adds cost, preserves scope and quality |
| **2** | Decompose into representative scenario subset | Preserves cognitive complexity through principled selection; reduces build scope |
| **3** | Outsource the interaction to a specialized vendor | Maintains quality; adds coordination overhead and budget |
| **4** | Return to customer with transparent scope conversation | Resets expectations at highest level; customer becomes part of the decision |

**On Option 4:** Junior IDs are most afraid of this conversation.
Shipping a compromised product to avoid a difficult conversation is
the greater failure. The skill must normalize Option 4 as professional
integrity, not defeat.

---

## Scenario Selection Protocol — Option 2 Decomposition

When decomposing a complex interaction into a representative subset,
the designer arrives at the SME conversation with a proposed selection
— not a blank slate. Asking the SME to select scenarios is outsourcing
a design decision. The designer proposes; the SME validates.

**Selection criteria hierarchy:**

| Priority | Criterion | Operational Definition |
|---|---|---|
| **1** | **Frequency (Pareto)** | Which 20% of case types account for 80% of real job occurrences? Pull from operational records before touching the SME. |
| **2** | **Failure pattern** | Which errors appear most frequently in internal audit records? Data question with a findable answer. |
| **3** | **Transferability** | Which scenarios, once mastered, give the learner reasoning tools to handle unpracticed variants? Requires SME expertise — not determinable from data alone. |

**Four-step selection process:**
1. Pull operational frequency data and audit failure records
   independently before any SME contact
2. Present data-derived findings to SME — ask them to confirm,
   correct, or add — not to select from scratch
3. Ask SME: *"If a learner masters these scenarios, which other
   situations do you believe they would handle without explicit
   training?"*
4. Designer synthesizes all inputs into a final scenario set with
   documented rationale — returns to SME for validation only

**Accountability:** The designer owns the selection logic and the
proposal. The SME owns the operational validation. These are distinct
responsibilities and must not be conflated.

---

## Post-Handover — Designer Responsibilities

The handover session is not the end of the designer's involvement.
It is the transition from lead to support.

**Designer responsibilities post-handover:**
- Remain available for questions throughout the build
- Respond to developer clarification requests promptly — delays
  here compound into timeline problems
- Review pre-build output before SME review — catch misalignments
  before the SME sees them
- Attend or debrief after SME pre-build review — own the feedback
  triage alongside the developer
- Maintain the non-negotiables list — if scope pressure builds,
  the designer knows which elements cannot flex

**The critical boundary:**
Post-handover, the developer leads the build. The designer does not
re-enter the authoring tool without the developer's knowledge and
agreement. Parallel editing produces version conflicts and erodes
the collaborative trust the handover was designed to build.

---

*© 2026 Norman Arosemena, CPTD. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Commercial use prohibited without a license.*
