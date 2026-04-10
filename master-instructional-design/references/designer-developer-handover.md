# Designer-Developer Handover — Script, Pre-Build, and Negotiation Framework

**Load when:** Design-development transition is approaching, script handover is being prepared, pre-build scope is being defined, or a designer-developer negotiation is underway.

---

## Gate 3 — The Script and the Pre-Build

**Fidelity level: Instructional → Experiential-partial**

Gate 3 is the third step in the fidelity ladder and the last approval gate before full build investment. It is composed of two artifacts: the script (designer-owned) and the pre-build (developer-owned).

For the full fidelity ladder context: `references/hard-new.md`

---

### The Script (Gate 3 — Designer Artifact)

When design and development are split roles, a third gate artifact is required before development begins — the script.

**Format:** Built directly in the authoring tool (e.g., Articulate 360).

**Required elements per slide/screen:**
- Scenes and slides organized to serve the build sequence
- Voice over text for all characters — narrator, avatars, scene dialogue
- A Developer Layer with explicit instructions:
  - Number of needed layers
  - Interaction details
  - Feedback text
  - On-screen text vs. VO-only decisions
  - Callout specifications
- Blank canvas — populated by the designer at specified fidelity, handed to the developer as the build foundation

**Critical principle:** The script contains both explicit direction AND surrounding context — notes, callouts, critically flagged elements — so the developer can walk out of the handover session confident enough to begin work independently.

**What makes a script precise vs. vague:**
A precise script tells the developer not just what to build but what design intent is non-negotiable vs. where creative latitude exists. Flagging critical elements explicitly removes ambiguity at the point where ambiguity is most expensive — in the build.

---

### The Handover — A Co-Authoring Kickoff, Not a Transfer Event

The handover meeting is the kickoff of a co-authoring and co-development process — not a handoff after which the designer exits.

**Designer responsibilities post-handover:**
- Remain on call for clarification and questions throughout the build
- Flag critical elements explicitly in the script so the developer knows where design intent is non-negotiable vs. where creative latitude exists

**Developer creative liberty:**
Developers have creative liberty to challenge anything — interaction design, architecture, branding, graphic style, VO style. This is a collegial model, not a hierarchical one.

The designer holds firm only when a proposed change threatens learner experience quality or product goals — and must articulate specifically why. "I prefer it this way" is not a defensible argument. The specific cognitive and behavioral outcomes the learner achieves through the original design — stated precisely — is the only defensible argument.

---

### The Pre-Build Layer (Developer Artifact)

**Owner:** Developer
**Purpose:** Provide reviewers and SMEs with experiential fidelity before full build investment.

**Method:** Build a representative subset of the full interaction at full fidelity. Leave the remainder at script level for content validation.

*Example: An interaction with 8 flip cards → developer builds 2 at full fidelity. SMEs validate all 8 cards content in the script AND experience the learner view through the 2 built cards.*

**Why this works:**
SMEs can validate content accuracy at script level and interaction feel at prototype level simultaneously — without the developer building assets that may require rebuilding after feedback. This catches two failure modes in one review cycle:
- Content that is accurate but won't land the way the SME imagined
- Interactions that look right in the script but break at experiential fidelity

---

## Designer-Developer Negotiation Framework

### The North Star

Design for the best possible learner experience within the tech stack. When development constraints push back, negotiate toward **equivalent value** — a different path to the same learning outcome. Never compromise the learning outcome itself.

---

### Equivalent Value — The Core Concept

Equivalent value is only operable if the designer can articulate precisely what learning value the original design was delivering. "It's more realistic" is not a defensible argument.

The specific cognitive and behavioral outcomes the learner achieves through the original design — stated precisely — is the only defensible argument.

**Example — Multi-path QC Appeals Simulation:**

The simulation's learning value is not realism. It is **decision-making under realistic conditional complexity.** The learner must develop five sequential cognitive operations:
1. Read color-coded evaluation status correctly before acting
2. Navigate a non-obvious UI to access filtering (3 clicks from base screen)
3. Recognize appeal eligibility based on evaluation status
4. Identify interaction type from the base screen
5. Select the correct appeal template based on that identification

Trimming to one path and one template trains a linear procedure. The real job requires conditional judgment across multiple variables. A learner trained on a single path will predictably fail on first encounter with a non-matching scenario.

**The non-negotiable argument:** The trimmed version trains a skill that does not match the job. That is the argument — not aesthetics, not realism, not scope preference.

---

### The Negotiation Solution Stack

When full-fidelity build is justified but not achievable within current constraints, present options in this order:

| Priority | Option | Trade-off |
|---|---|---|
| **1** | Bring additional developer capacity for this interaction only | Adds cost, preserves scope and quality |
| **2** | Decompose into representative scenario subset | Preserves cognitive complexity through principled selection; reduces build scope |
| **3** | Outsource the interaction to a specialized vendor | Maintains quality; adds coordination overhead and budget |
| **4** | Return to customer with transparent scope conversation | Resets expectations at highest level; customer becomes part of the decision |

**On Option 4:** Junior IDs are most afraid of this conversation. The skill must normalize it as professional integrity — shipping a compromised product to avoid a difficult conversation is the greater failure.

---

### Scenario Selection Protocol (for Option 2 Decomposition)

When decomposing a complex interaction into a representative subset, the designer arrives at the SME conversation with a proposed selection — not a blank slate.

**Asking the SME to select scenarios is outsourcing a design decision.** The designer proposes; the SME validates.

**Selection criteria hierarchy:**

| Priority | Criterion | Operational Definition |
|---|---|---|
| **1** | **Frequency (Pareto)** | Which 20% of case types account for 80% of real job occurrences? Pull from operational records before touching the SME. |
| **2** | **Failure pattern** | Which errors appear most frequently in internal audit records? Data question with a findable answer. |
| **3** | **Transferability** | Which scenarios, once mastered, give the learner reasoning tools to handle unpracticed variants? Requires SME expertise — not determinable from data alone. |

**Four-step selection process:**

1. **Data first:** Pull operational frequency data and audit failure records independently. Derive frequency and failure pattern candidates before any SME contact.
2. **SME validation:** Present data-derived findings. Ask SME to confirm, correct, or add — not to select from scratch.
3. **SME expertise for transferability:** Ask: *"If a learner masters these scenarios, which other situations do you believe they would handle without explicit training?"* This surfaces transferability through expert knowledge.
4. **Designer synthesizes and proposes:** Combines all inputs into a final scenario set with documented rationale. Returns to SME for validation only — not further ideation.

**Accountability:** The designer owns the selection logic and the proposal. The SME owns the operational validation. These are distinct responsibilities and must not be conflated.

---

*© 2026 Norman Arosemena, CPTD. [CC BY-NC-ND 4.0](../../../LICENSE) — personal/educational use only; commercial use prohibited.*
