# L&D Project Management — Templates, Tools & Workflows

Load this file when the user needs project management support for learning projects: project
charters, RACI matrices, design documents, style guides, review/approval workflows, scope
management, or stakeholder communication. Covers both waterfall/ADDIE and Agile/hybrid contexts.

---

## Table of Contents
1. The L&D Project Lifecycle — Overview
2. Project Charter Template
3. RACI Matrix — L&D Standard Roles
4. Scope Management & Change Control
5. Design Document (Blueprint) — Template & Standards
6. Storyboard Standards & Review Workflow
7. Style Guide — What It Must Contain
8. Review & Approval Workflow
9. QA Checklist — Pre-Launch
10. Stakeholder Communication Templates
11. Project Risk Register
12. Waterfall vs. Agile — Choosing the Right Approach
13. Cross-References

---

## 1. The L&D Project Lifecycle — Overview

Regardless of methodology (ADDIE, SAM, Agile), every learning project moves through the same fundamental phases. What differs is how linearly and how rigidly:

```
INITIATE          ANALYZE           DESIGN            DEVELOP           IMPLEMENT         EVALUATE
─────────         ────────          ──────            ───────           ──────────        ────────
Project           Needs             Learning          Content &         Deploy &          Measure
charter           assessment        blueprint         media build       launch            impact
Stakeholder       Task              Storyboard        eLearning /       Facilitator       L1–L4
alignment         analysis          Style guide       ILT materials     training          data
Scope &           Audience          Prototype         QA & review       LMS config        Iterate
timeline          analysis          sign-off          cycles            Pilot             Improve
```

**Key principle**: Decisions made late cost more to fix than decisions made early. The highest ROI activities are front-end analysis and design — not build. Invest time before the keyboard.

---

## 2. Project Charter Template

The project charter is the foundational agreement between the ID/L&D team and the sponsoring stakeholder. Get it signed before any design work begins.

---

**PROJECT CHARTER**
*[Organization Name] — Learning & Development*

**Project Title**: _______________________________________________
**Date**: _____________ **Version**: _______
**Project Sponsor**: _________________________ **Project Lead (ID)**: _________________________

---

### 1. Business Problem & Performance Gap
*What is happening (or not happening) that prompted this project? Be specific — observable behaviors and measurable outcomes, not "we need training on X."*

____________________________________________________________

### 2. Target Audience
| Field | Detail |
|---|---|
| Role(s) | |
| Approximate population size | |
| Geographic locations | |
| Language requirements | |
| Technology access | |
| Prior knowledge of topic | |

### 3. Learning Goals (High Level)
*After this learning experience, participants will be able to:*
1.
2.
3.

### 4. Proposed Solution & Modality
- [ ] eLearning (self-paced)
- [ ] ILT (instructor-led, in-person)
- [ ] VILT (virtual instructor-led)
- [ ] Blended (specify: _______________)
- [ ] Performance support / job aid
- [ ] Other: _______________

**Estimated duration**: _______________
**Authoring tool**: _______________
**LMS/delivery platform**: _______________

### 5. Project Scope
**In scope**:

**Out of scope**:

**Assumptions**:

**Dependencies** (SME availability, legal review, translation, etc.):

### 6. Timeline
| Milestone | Target Date | Owner |
|---|---|---|
| Needs analysis complete | | |
| Design document approved | | |
| Prototype / Alpha review | | |
| Beta review | | |
| Final content approved | | |
| QA complete | | |
| Launch | | |
| Evaluation data collection begins | | |

### 7. Resources & Budget
| Resource | Estimated Hours/Cost | Notes |
|---|---|---|
| Instructional Designer | | |
| Graphic Designer | | |
| Developer/Programmer | | |
| SME time (review cycles) | | |
| Facilitator (if ILT) | | |
| Translation/localization | | |
| LMS configuration | | |
| Total estimated budget | | |

### 8. Review & Approval Process
| Review Round | Reviewers | Turnaround Time |
|---|---|---|
| Design document | | |
| Alpha (prototype) | | |
| Beta (full draft) | | |
| Final / Gold | | |

### 9. Evaluation Plan (High Level)
| Level | What We'll Measure | Method | Timeline |
|---|---|---|---|
| L1 Reaction | | | |
| L2 Learning | | | |
| L3 Behavior | | | |
| L4 Results | | | |

### 10. Risks & Mitigation
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| SME unavailability | | | |
| Scope creep | | | |
| Content accuracy issues | | | |

---

**APPROVALS**

| Role | Name | Signature | Date |
|---|---|---|---|
| Project Sponsor | | | |
| L&D Project Lead | | | |
| SME Lead | | | |
| IT/LMS Admin (if applicable) | | | |

---

## 3. RACI Matrix — L&D Standard Roles

**R** = Responsible (does the work) | **A** = Accountable (approves/owns) | **C** = Consulted (input required) | **I** = Informed (kept updated)

| Task | ID/Designer | SME | L&D Manager | Sponsor | IT/LMS Admin | Legal/Compliance |
|---|---|---|---|---|---|---|
| Define business problem | C | C | A | A | I | I |
| Conduct needs analysis | R | C | A | I | I | I |
| Write design document | R | C | A | I | I | C |
| Approve design document | C | C | C | A | I | C |
| Develop storyboard | R | C | A | I | I | I |
| SME content review | C | R/A | I | I | I | C |
| Legal/compliance review | I | I | I | I | I | R/A |
| Build eLearning / materials | R | I | A | I | I | I |
| QA review | R | C | A | I | I | I |
| LMS configuration | I | I | C | I | R/A | I |
| Pilot / UAT | R | C | A | C | R | I |
| Final sign-off / launch approval | C | C | C | A | I | C |
| Post-launch evaluation | R | I | A | I | I | I |

**Customize this matrix** for your organization's actual roles. Common variants:
- Add a **Graphic Designer** row for visual asset tasks
- Add a **Facilitator** row for ILT/VILT projects
- Add a **Translation Vendor** row for multilingual projects
- Split **Legal** and **Compliance** if they are separate functions

---

## 4. Scope Management & Change Control

### The Scope Creep Problem in L&D
Scope creep is the #1 killer of L&D project timelines and budgets. It arrives in the form of:
- "Can we just add one more topic?" (after design document is approved)
- "The SME wants to change the examples" (during beta review, not alpha)
- "Legal needs to review this now" (two weeks before launch)
- "The sponsor wants a live session version too" (after eLearning is built)

### Change Control Process

**Step 1 — Log it**: Every change request goes into a change log, regardless of size.

**Step 2 — Assess impact**: ID estimates the impact on timeline, budget, and scope before responding.
- Small (< 2 hours): Absorb with note to sponsor
- Medium (2–8 hours): Formal change request with timeline adjustment
- Large (> 8 hours or affects architecture): Sponsor approval required; timeline reset

**Step 3 — Communicate and document**: Never make changes without written confirmation from the requestor. Email or project tool — not verbal.

**Step 4 — Update charter**: Significant scope changes require charter amendment and re-signature.

### Change Log Template
| Date | Requested By | Description | Impact Assessment | Hours | Decision | Approved By |
|---|---|---|---|---|---|---|
| | | | | | Accept / Reject / Defer | |

### Language for Managing Scope Conversations
- "That's a great addition — let me assess the impact on our timeline and come back to you."
- "This change would push our launch date by [X] days. Do you want to make that trade, or should we log it for version 2?"
- "We can include this if we remove [Y]. Which is the higher priority?"
- Never: "Sure, no problem" (before assessing the actual impact)

---

## 5. Design Document (Blueprint) — Template & Standards

The design document (also called a blueprint, design plan, or learning design document) is the bridge between analysis and development. It should be approved before any build work begins.

### Design Document — Required Sections

**Section 1: Project Overview**
- Project title, audience, business problem, learning goals (from charter)
- Any updates since charter was approved

**Section 2: Audience Analysis Summary**
- Who they are: role, experience level, prior knowledge
- What they care about: motivation, what's in it for them
- What they find difficult: common errors, misconceptions, resistance points
- Context: where/how they'll use this learning; what tools are available on the job

**Section 3: Learning Objectives — Full List**
Formatted as: *"After completing [module/course], learners will be able to [Bloom's verb] [specific content] [in context/conditions if applicable]."*

Every objective must have:
- A Bloom's level designation (Remember → Create)
- A corresponding assessment method listed

**Section 4: Content Outline & Sequencing**
- Module/section structure with estimated time for each
- Rationale for sequencing decisions
- Prerequisites and dependencies between modules

**Section 5: Instructional Strategy**
For each module/section:
- Instructional approach (scenario-based, worked example, simulation, lecture + activity, etc.)
- Practice activity type and frequency
- Assessment approach (formative/summative)
- Feedback strategy

**Section 6: Media & Interaction Plan**
- Media types used: text, audio, video, animation, interactive, graphic
- Interaction types: click-to-reveal, branching, drag-and-drop, assessment, simulation
- Accessibility requirements and accommodations

**Section 7: Evaluation Plan**
- L1: what survey, when, tool
- L2: pre/post assessment design, passing threshold
- L3: follow-up plan, manager involvement
- L4: business metric and data source

**Section 8: Technical Specifications**
- Authoring tool and version
- Output format: SCORM 1.2 / SCORM 2004 / xAPI
- LMS destination and configuration requirements
- Screen resolution and device requirements
- Accessibility standard: WCAG 2.1 AA

**Section 9: Style & Brand**
- Link to or summary of style guide (see §7 below)
- Tone of voice: formal/conversational/coaching
- Visual style: existing brand standards or new direction

**Section 10: Open Questions & Risks**
- Unresolved content questions requiring SME input
- Content areas pending legal/compliance review
- Known risks to timeline

---

## 6. Storyboard Standards & Review Workflow

### What a Storyboard Must Contain
A production-ready storyboard is the complete specification for what will be built. Developers should be able to build from it without asking questions.

**Per-slide/screen minimum requirements:**
| Field | Content |
|---|---|
| Slide/screen number | Sequential; use decimal for sub-screens (3.1, 3.2) |
| Slide type | Title, content, activity, knowledge check, scenario, summary, etc. |
| Learning objective reference | Which objective(s) does this slide serve? |
| On-screen text | Exact text, formatted as it will appear |
| Narration script | Word-for-word audio script (even if audio TBD) |
| Visual description | What the learner sees — layout, images, animations, interactions |
| Developer notes | Build instructions, interaction specs, trigger logic, variables |
| Slide notes | Context for SME reviewers; not visible to learners |

### Storyboard Review Protocol
**Alpha review** (prototype — 1–3 representative slides per section):
- Reviewers: ID lead, one SME, sponsor
- Focus: Are we on the right track? Does the approach work? Are examples realistic?
- NOT a copyedit — don't review grammar at prototype stage

**Beta review** (full draft — all slides, rough visuals):
- Reviewers: Full SME panel, legal/compliance if needed
- Focus: Content accuracy, completeness, scenario realism
- ID resolves content issues; visual polish comes later

**Final/Gold review** (complete, polished):
- Reviewers: Sponsor, one SME, QA reviewer
- Focus: Final accuracy check, no new content changes
- Any change at this stage requires change control (§4)

**Review turnaround SLA** (establish in charter):
- Standard: 5 business days per review cycle
- Complex/legal: 10 business days
- Escalation: if review is not returned by deadline, ID escalates to sponsor

---

## 7. Style Guide — What It Must Contain

A learning style guide ensures consistency across a program or across an entire L&D portfolio. Every multi-module project should have one.

### Style Guide Minimum Contents

**Voice & Tone**
- Formal/informal register (examples of each)
- Second person ("you") vs. third person ("the employee")
- Active vs. passive voice (active preferred; specify exceptions)
- Contractions: allowed or not?
- Reading level target (use Flesch-Kincaid; specify grade level)

**Terminology**
- Approved vocabulary list for key terms (especially regulated/technical content)
- Forbidden terms (jargon to avoid, deprecated product names, etc.)
- Capitalization rules for company-specific terms
- Abbreviations and acronyms: always spell out on first use; approved abbreviation list

**Learning Objective Language**
- Approved Bloom's action verbs list by level
- Objective format template
- Forbidden verbs: "understand," "know," "appreciate," "be aware of"

**Screen Layout Standards**
- Standard slide/screen template (reference file or tool template)
- Title placement and character limits
- Body text zone dimensions
- Navigation button placement and labeling
- Progress indicator style

**Typography**
- Primary font (headings): name, size, weight
- Secondary font (body): name, size, weight, line height
- Caption/label: name, size, color
- Minimum body text size (16px minimum)
- Heading hierarchy: H1, H2, H3 specifications

**Color System**
- Primary brand color + hex code
- Secondary color + hex code
- Semantic colors: success (green), error (red), warning (yellow), info (blue) + hex codes
- Neutral scale: 5–7 grays + hex codes
- Minimum contrast ratios: confirm all text combinations meet WCAG AA

**Imagery & Illustration**
- Approved image sources (stock library, custom illustration, brand library)
- Photography style: candid/posed, color graded/natural, industry context
- Illustration style: flat/isometric/hand-drawn/photorealistic
- Character representation standards (diversity requirements)
- Forbidden image types (cheesy stock, clip art, overly staged)

**Icons**
- Icon library/set (specify name and version for consistency)
- Standard icon sizes: 24px, 32px, 48px
- Color usage: monochrome vs. color icons; when each applies

**Audio & Video**
- Narration voice specifications: tone, pace, accent considerations
- Music guidelines: background music allowed/not; genre/energy
- Video style: screen capture, talking head, animation, documentary
- Caption standard: 32-character line limit, 2-line max, 1–7 seconds on screen

**Interaction Patterns**
- Standard interaction types used in this program (with screenshots/examples)
- Button labels: standard text for Continue, Back, Submit, Try Again, Replay
- Feedback text format: correct feedback template, incorrect feedback template
- Scenario/branching conventions

---

## 8. Review & Approval Workflow

### The Three-Gate Model
Most L&D projects benefit from three formal approval gates. Each gate has defined reviewers, criteria, and a turnaround commitment.

```
GATE 1: DESIGN          GATE 2: BETA             GATE 3: LAUNCH
────────────────         ──────────────────        ──────────────────
Design document          Full draft storyboard     Final built course
approved                 + rough visuals            QA complete
                         reviewed                   Pilot complete
Reviewers:               Reviewers:                Reviewers:
Sponsor + SME lead       SME panel + legal         Sponsor + QA lead
L&D manager              (if needed)               LMS admin

Output:                  Output:                   Output:
Approved blueprint       Tracked-changes           Launch approval
                         storyboard                sign-off
```

### Reviewer Responsibilities — Setting Expectations Early
Brief reviewers before they review, not during. Establish:
- What they are reviewing for (content accuracy — not design preferences)
- What format feedback should take (comments in doc, email, review tool)
- What "approved" means (no changes, or only minor copyedits?)
- What happens if no feedback is received by deadline (assumed approved, or escalated?)

### SME Review — Common Problems & Solutions

| Problem | Solution |
|---|---|
| SME rewrites rather than reviews | Brief SME explicitly: "Your role is accuracy, not writing. Mark factual errors and flag anything missing." |
| SME adds scope mid-review | Route additions through change control; don't absorb silently |
| SME is unavailable | Establish backup SME in charter; build SME availability into timeline |
| Conflicting feedback from multiple SMEs | Identify a single SME decision-maker before the project starts |
| SME approves content with errors | Final accuracy check by ID + independent QA before launch |

---

## 9. QA Checklist — Pre-Launch

Run this checklist on every eLearning course before publishing to the LMS.

### Functional QA
- [ ] All slides/screens load correctly
- [ ] All navigation (Next, Back, Menu) functions as intended
- [ ] All interactive elements (click-to-reveal, drag-and-drop, tabs, accordion) function correctly
- [ ] All branching paths lead to correct destinations
- [ ] Variables reset correctly on course restart (if applicable)
- [ ] All audio plays without delay or distortion
- [ ] All video plays, buffering is acceptable
- [ ] Course completes and sends completion/score to LMS (test in actual LMS, not preview)
- [ ] SCORM/xAPI tracking verified: completion status, score, suspend data

### Content QA
- [ ] All on-screen text matches approved storyboard
- [ ] All narration matches approved script
- [ ] No spelling or grammar errors (run spell-check AND human review)
- [ ] All names, titles, and terminology match style guide
- [ ] All images match visual descriptions in storyboard
- [ ] All feedback text is present and accurate
- [ ] No placeholder text ("Lorem ipsum," "TBD," "[INSERT IMAGE]") remaining

### Accessibility QA
- [ ] Tab order is logical on every slide
- [ ] All images have meaningful alt text
- [ ] All audio/video has accurate captions
- [ ] All interactive elements are keyboard accessible
- [ ] Color contrast meets WCAG AA (4.5:1 text; 3:1 UI)
- [ ] No information conveyed by color alone
- [ ] Tested with screen reader (NVDA or JAWS minimum)

### Visual QA
- [ ] All images are high resolution (no pixelation)
- [ ] Typography consistent with style guide throughout
- [ ] Color palette consistent with style guide
- [ ] Layout alignment consistent (no floating elements)
- [ ] Progress indicator accurate
- [ ] All custom fonts render correctly (not substituted)

### Cross-Browser & Device QA
- [ ] Chrome (primary test browser)
- [ ] Firefox
- [ ] Edge
- [ ] Safari (if Mac/iOS users in audience)
- [ ] Mobile browser (if mobile audience)
- [ ] Tablet (if applicable)

---

## 10. Stakeholder Communication Templates

### Project Kickoff Email
```
Subject: [Project Name] — Kickoff & Next Steps

Hi [Sponsor name],

I'm excited to kick off [Project Name] with you. Here's what to expect:

WHAT WE'RE BUILDING: [1-sentence description]
WHO WE'RE SERVING: [Audience summary]
LAUNCH TARGET: [Date]

YOUR NEXT STEP: Please review the attached project charter by [date] and 
reply with your approval or any questions. This is our formal agreement on 
scope, timeline, and resources.

SME INVOLVEMENT: I'll need [Name(s)] available for:
- [X-hour] content review session during week of [date]
- [Y-day] storyboard review starting [date]
- [Z-day] final review before launch [date]

Questions? Reply here or book 30 min at [calendar link].

[Your name]
```

### Status Update (Weekly/Biweekly)
```
Subject: [Project Name] — Status Update [Week of Date]

STATUS: 🟢 On Track / 🟡 At Risk / 🔴 Off Track

THIS WEEK:
✅ [Completed milestone]
✅ [Completed milestone]

NEXT WEEK:
▶ [Planned milestone]
▶ [Planned milestone]

NEEDS FROM YOU:
⚠ [Action item — owner — deadline]

RISKS/ISSUES:
[Any blockers or emerging risks]
```

### Review Request Email
```
Subject: [Project Name] — [Alpha/Beta/Final] Review Request

Hi [Reviewer name],

The [Alpha/Beta/Final] version of [Project Name] is ready for your review.

WHAT TO REVIEW: [Storyboard / eLearning prototype / Full course — link]
REVIEW BY: [Date — X business days]
WHAT TO FOCUS ON: [Content accuracy / scenario realism / final check]
HOW TO GIVE FEEDBACK: [Comments in doc / email / review tool]

Please avoid: redesigning, rewriting for style, or adding new scope.
If you find a factual error or missing content, flag it with a comment.

If I don't hear from you by [date], I'll assume the content is approved 
and move forward.

[Your name]
```

### Scope Change Notification
```
Subject: [Project Name] — Scope Change Request: [Brief Description]

Hi [Sponsor name],

I've received a request to [description of change]. Before proceeding, 
I want to make sure you're aware of the impact:

CHANGE REQUESTED: [Description]
IMPACT ON TIMELINE: +[X] business days (new target: [Date])
IMPACT ON BUDGET: +[X] hours / $[Y]
RECOMMENDED ACTION: [Proceed / Defer to v2 / Decline]

Please confirm how you'd like to proceed by [date].

[Your name]
```

---

## 11. Project Risk Register

Maintain this throughout the project. Review at every status meeting.

| # | Risk | Category | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation Strategy | Owner | Status |
|---|---|---|---|---|---|---|---|
| 1 | SME unavailable for review cycles | Resource | H | H | Identify backup SME; build review buffers into timeline | ID Lead | Open |
| 2 | Scope expansion mid-project | Scope | H | H | Change control process; charter sign-off | Sponsor | Open |
| 3 | Content accuracy issues discovered at beta | Content | M | H | Alpha review by SME before full build | SME Lead | Open |
| 4 | LMS configuration delays | Technical | M | H | Engage LMS admin at project kickoff; test environment ready by beta | LMS Admin | Open |
| 5 | Legal/compliance review takes longer than planned | Legal | M | H | Engage legal at design document stage, not beta | Legal Lead | Open |
| 6 | Key team member unavailable | Resource | M | H | Cross-train; document work in progress; version control all files | ID Lead | Open |
| 7 | Translation/localization delays (if applicable) | Resource | H | M | Engage vendor at design document approval; freeze content before translation begins | Project Lead | Open |

---

## 12. Waterfall vs. Agile — Choosing the Right Approach

Most L&D projects benefit from a hybrid approach rather than a pure waterfall or pure Scrum model. Here's how to choose:

| Factor | Suggests Waterfall/ADDIE | Suggests Agile/SAM |
|---|---|---|
| Requirements stability | Stable, well-defined | Evolving, uncertain |
| Stakeholder availability | Limited, formal review cycles | Engaged, available for frequent input |
| Team experience | Sequential process familiar | Iterative process familiar |
| Project complexity | Moderate — well-understood domain | High — novel domain or new approach |
| Timeline | Fixed milestones, regulatory deadlines | Flexible, value delivery over schedule |
| Content volatility | Stable content unlikely to change | Content in active development |

### The Hybrid Model (Most Common)
- **Phase 1 (Analysis/Design)**: Waterfall gates — charter approval, design document sign-off
- **Phase 2 (Development)**: Agile sprints — build in 2-week increments, frequent stakeholder review
- **Phase 3 (QA/Launch)**: Waterfall gate — final sign-off before publish

For full Agile/Scrum methodology for L&D → `references/agile-and-design.md` §1–5

---

## 13. Cross-References to Other Skill Files

- For **Agile sprint planning and backlog management** for L&D projects → `references/agile-and-design.md` §1–5
- For **evaluation plan templates and measurement instruments** → `references/evaluation-planning.md`
- For **facilitation guide format standards** → `references/facilitation-and-ilt.md` §3
- For **style guide visual design standards** (typography, color, imagery) → `references/agile-and-design.md` §6–10
- For **LMS configuration and QA in the LMS** → `references/lms-evaluation.md` §9
- For **AI-assisted project documentation** (using AI to draft charters, status updates, review emails) → `references/generative-ai-for-ld.md` §5
