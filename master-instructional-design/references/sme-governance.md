# SME Governance — Ecosystem Mapping, Role Architecture, and Dispute Resolution

**Load when:** SME ecosystem mapping is needed, POC model or lead SME consolidation model is being set up, or dispute resolution authority needs to be assigned.

---

## The Governing Principle

> *SME management is a governance problem, not a relationship problem.*

Junior IDs default to relationship behaviors — stay friendly, send updates, be responsive. That is insufficient. The correct approach is structural: assign roles, decision rights, escalation paths, and consolidation responsibilities before the work starts.

**The critical principle:**
Maximize visibility to all roles as early as possible. Roles, rights, and escalation paths are assigned before the work begins — not managed reactively as conflicts emerge.

---

## SME Ecosystem Mapping

### When to Execute

First discovery meeting if possible. If not, establish the times and spaces needed to onboard the SME team immediately after.

### Where to Document

In the project management system (e.g., Confluence) at project initiation. Not in email. Not in personal notes.

### What to Document

| Element | Why It Matters |
|---|---|
| Who has subject matter knowledge | Identifies who can answer content questions |
| Who has approval authority | Identifies whose sign-off is required at each gate |
| Who has political veto power without a formal role | Identifies the informal authority that can stop or redirect the work |
| Who needs to be kept informed without being given approval authority | Prevents scope by committee while maintaining stakeholder visibility |
| Time and effort commitment per role | Creates accountability for SME availability before the sprint starts |
| Approval process and artifact walkthrough schedule | SMEs know when they will be asked for input and when they will not |

**The political veto question is not optional.**
Every organization has people whose informal authority exceeds their formal title. Failing to map them at intake means encountering them as blockers mid-project. Mapping them at intake means managing them as stakeholders.

---

## SME Role Architecture

### Simple Projects — Single SME POC Model

**When to use:** Single SME team, one domain, clear approval authority.

**Structure:**
One SME serves as point of contact AND operates as liaison to secure approvals requiring escalation.

**Advantages:**
- Clean accountability — one throat to call
- Minimal coordination overhead
- Faster feedback turnaround
- Clear escalation path

**Limitation:**
The POC model assumes the SME has both content knowledge and organizational access to approval authority. When these are separated — domain expert ≠ approval authority — the model requires adjustment.

---

### Complex Projects — Lead SME Consolidation Model

**When to use:** Multiple SME teams are involved — especially when teams may have conflicting or opposing standards (e.g., multiple QA teams from different business areas using the same platform with different evaluation criteria).

**Structure:**
Assign a **Lead SME** whose role includes:
- Internal consolidation of SME input before it reaches the learning team
- Final validation of content accuracy across all contributing SMEs
- Dispute resolution within the SME team

**Critical design requirement:**
The Lead SME role is assigned, not emergent. The person with the most informal authority does not automatically become the Lead SME — the role is defined by consolidation and dispute resolution capability, not by organizational rank.

**The consolidation principle:**
Without a Lead SME, conflicting input arrives at the learning team simultaneously. The designer is left making content decisions that are above their authority. The Lead SME absorbs internal conflict before it becomes a design problem.

---

## Dispute Resolution Authority

### When to Assign

Early and explicitly — at project initiation, in writing, in the project management system.

### What to Define

| Level | Decision Authority |
|---|---|
| Content accuracy dispute between contributing SMEs | Lead SME resolves |
| Dispute Lead SME cannot resolve | Named escalation authority — defined by title or role, not by availability |
| Design vs. content dispute (learning team vs. SME) | Learning leader + Lead SME — never designer alone |

**Critical principle:**
Dispute resolution authority is not negotiated mid-project when a conflict surfaces. It is documented at initiation so everyone knows the path before they need it.

---

## SME Onboarding as Preventive Governance

SMEs who understand the rhythm of work and why it is structured the way it is will:
- Self-filter before submitting off-schedule change requests
- Understand why approval cycles exist and don't resist them
- Participate in reviews with appropriate depth (not too shallow, not expanding scope)

**SME onboarding is not a courtesy.** It is a preventive governance mechanism. A SME who has been onboarded properly will pause before hitting send on a mid-sprint change request.

**Minimum onboarding elements:**
- How the learning team's sprint/production cycle works
- When SME input is required and when it is not
- What the review and approval artifacts look like at each gate
- How change requests are processed and classified
- Who to contact and when

For the full scope creep response protocol when SME change requests arrive: `references/scope-creep-governance.md`

---

## Verification Protocol — When Capability Claims Are Made

When a SME asserts that the learner population already has a specific capability (justifying a design shortcut):

**Step 1 — Intake query:**
- Clear definition of job description and role expectations
- Success metrics in this specific context
- Failure occurrence patterns: *"Are errors in judgment a recurrent issue, or does it tilt more toward system errors?"*

**Step 2 — Read the SME:**
- Confident, specific answer → provisionally accept; document the claim and confidence level
- Hesitation → probe deeper; ask explicitly: *"How confident are you about this?"*
- Document confidence level alongside the claim — the accuracy of SME confidence is itself a data point

**Step 3 — Seek independent corroboration:**
- Performance data
- Incident reports
- Quality metrics and error logs
- Job descriptions and role requirements

Never rely on SME confidence alone. The SME's certainty is not evidence.

For the full Level 4 verification protocol and what to do when verification fails: `references/taxonomy-decision-engine.md`

---

*© 2026 Norman Arosemena, CPTD. [CC BY-NC-ND 4.0](../../../LICENSE) — personal/educational use only; commercial use prohibited.*
