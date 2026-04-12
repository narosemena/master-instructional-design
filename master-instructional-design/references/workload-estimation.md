<!-- workload-estimation.md -->

# Workload Estimation Framework

---

## The Core Problem

Junior IDs almost universally underestimate. The directional bias is
consistent and produced by three compounding root causes:

| Root Cause | Description | Intervention Type |
|---|---|---|
| **Visibility failure** | Cannot see the full scope of what the work actually requires | Process — build the estimation model |
| **Impression management** | Wants to appear capable and fast; aims to overdeliver | Behavioral — reframe what professionalism means |
| **Fear of being the bottleneck** | Social pressure compresses the estimate downward; mistaken for realism | Behavioral — name the pattern explicitly |

**Critical principle:** Chronic underestimation is worse than occasional
overestimation. An overestimate produces a conversation. An underestimate
produces a missed deadline, compressed build, quality compromise, and
damaged relationship — all arriving too late to correct.

---

## The Two-Owner Estimation Model

Estimation is not one problem. It is two distinct problems with different
owners, different variables, and different failure modes — split at the
designer/developer role boundary.

**Owner 1 — The Designer estimates:**
- Discovery and needs analysis work
- Proposal drafting (heaviest lift — includes discovery, meeting
  planning/execution, and core brain work)
- Mind map drafting
- Script drafting
- Handover session planning and execution

**Owner 2 — The Developer estimates:**
- Pre-build scope and effort
- Full build scope and effort

These are sequential but not independent. The quality of the designer's
output directly determines the accuracy of the developer's estimate.
A vague script produces a wide, unreliable estimate. A precise,
complexity-flagged script produces a tighter, more defensible one.

**Developer's four estimation questions:**
1. Do I have everything I need to start my work? *(definition of ready)*
2. Can I see enough design complexity, challenges, and scope to accurately
   estimate pre-build and full build effort?
3. How and when do I know to push back?
4. How do I translate this into the effort unit this project uses —
   hours, weeks, story points, dollars?

---

## The Primary Estimation Destroyer — SME Involvement

SME availability, responsiveness, and engagement quality is the single
most reliable source of estimation error — and it almost never appears
as an explicit variable in a junior ID's estimation model.

**The SME involvement curve across a project:**

| Phase | SME Involvement Level | Driver |
|---|---|---|
| Project kickoff | Low | Awareness only |
| Discovery | High spike | Designer needs SME time to surface, validate, and map all subject matter |
| Internal production | Low trough | Learning team working independently |
| Review cycles | High spike(s) | Multiple review gates from proposal through full build |
| Final approval | Medium | Sign-off and closure |

**Why elapsed time does not equal active work time:**
SME-driven elapsed time is the gap between them. A designer or developer
working at full capacity still waits — for SME availability, feedback
turnaround, alignment meetings, and escalation resolution. None of this
appears as active work hours but all of it appears on the calendar.

---

## The Structural Truth About L&D Projects

Learning projects are organizational convergence points. The learning team
is frequently the first to look at a job holistically — across roles,
teams, and documented and undocumented knowledge simultaneously.

This means learning projects reliably surface organizational dysfunction
the working team has normalized:
- Missing standards and undocumented procedures
- Conflicting processes across teams
- Knowledge that exists only in one person's head
- Procedures never written down because everyone who needed them was
  present when they were invented

When dysfunction surfaces mid-project it creates scope uncertainty —
the designer may not know whether they are training the current broken
process or waiting for the organization to fix it first. This is an
estimation variable with no line item in any standard project management
template.

---

## The Uncertainty Buffer

**Mechanism:** Add a percentage buffer to the base estimate as a function
of assessed project uncertainty.

**Range:** 10–50% added to base estimate

*Example: A 6-point story becomes a 7–9 point story depending on
uncertainty level.*

**Critical principle:** This is not a mathematical formula. The edges are
intentionally blurry and must be calibrated case by case. Junior IDs want
a formula. There is not one. What exists is a principled range applied
with judgment.

---

## Uncertainty Calibration — Three Diagnostic Levels

Assessed at intake and early discovery. Each level contributes to
buffer sizing.

### Level 1 — Nature of the Request

| Signal | Uncertainty Level |
|---|---|
| Clear operational need — new tool, new team, identifiable skill gap | Low |
| Knee-jerk executive reaction — emotional token attached to request | High — more discovery needed before estimation is possible |

**Key indicator:** Is there an emotional token attached to the request?
Requests driven by frustration, pressure, or reactive thinking require
more discovery before they can be scoped.

### Level 2 — Support System Maturity

Examine the organizational scaffolding around the work:
- Are policies and procedures documented and current?
- Are there clear definitions of success and failure?
- Are consequences for failure defined and enforced?
- Are other performance support systems in place?

| Condition | Uncertainty Level |
|---|---|
| Most support systems present and documented | Low |
| Most support systems missing or undocumented | High |

### Level 3 — Current State of the Work

| Condition | Uncertainty Level |
|---|---|
| Work currently being performed successfully by this team | Low |
| Work performed successfully elsewhere — gap is specific to this team | Medium |
| Work is brand new to this organization but established in the industry | Medium-High |
| Work is brand new to the industry — no external benchmark exists | High |

---

## Definition of Ready — The Upstream Gate

The learning leader's responsibility: ensure work assigned to designers
and developers meets a minimum threshold before entering the sprint.
The uncertainty buffer handles residual uncertainty that passes through
this gate — not catastrophic uncertainty that should have blocked the
work entirely.

**Hard pass/fail criterion:**
> Can this problem be solved by a learning intervention? If no — do not
> assign. Hold in backlog until root cause is confirmed as a learning
> and performance gap.

**Judgment-dependent criteria (non-binary):**
- Is the subject matter sufficiently documented to begin design?
- Is SME access confirmed and committed?
- Is executive sponsorship established?
- Is the performance gap defined with enough specificity to write
  objectives?
- Is there an identified measure of success?

**Threshold reality:** The definition of ready is not a perfect checklist.
Experienced learning leaders make judgment calls on projects that partially
meet the criteria. The judgment question is: *"Is enough known to begin
design without creating rework work risk that exceeds the cost of waiting?"*

*Example of a borderline case:* Work is being performed successfully
externally but no documented process or standards exist internally. This
may pass the threshold depending on the learning leader's judgment about
discovery capacity and SME availability — it is not an automatic hold
or an automatic pass.

---

## Estimation Calibration — Accumulating Over Time

As projects complete, the skill tracks estimation accuracy to produce
personalized buffer recommendations.

**Data captured at project close:**
- Original estimate (hours/story points)
- Actual hours/points delivered
- Uncertainty buffer applied
- Variables present: SME responsiveness, documentation quality,
  scope changes, team configuration
- Variance: over/under and by how much
- Root cause of variance

**After 5+ projects:**
- Systematic bias becomes visible — almost everyone underestimates a
  specific variable consistently
- Buffer recommendations become personalized rather than generic
- Current project is compared against similar past projects with named
  variance patterns

**Calibration prompt at project close:**
> *"Before we close this project — what was your original estimate,
> what did it actually take, and what caused the variance? I'll store
> this to improve your next estimate."*

---

*© 2026 Norman Arosemena, CPTD. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Commercial use prohibited without a license.*
