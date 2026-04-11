# Technical Improvement Roadmap — master-instructional-design
**Version target:** v3.1.0 and beyond
**Purpose:** Claude Code planning document — implement features in priority order
**Status:** Planning phase — do not implement multiple items simultaneously

---

## Implementation Rules for Claude Code

- Implement one item at a time — complete, test, and commit before starting the next
- Each item has its own branch: `claude/[item-name]-<id>`
- Each item requires an activation test before merging to main
- All taxonomy content is encoded in the reference files under master-instructional-design/references/ — specifically taxonomy-decision-engine.md, hard-new.md, hard-change.md, soft-change.md, soft-new.md, and mixed.md
- All new reference files go in `master-instructional-design/references/`
- All new workflow files go in `master-instructional-design/` root or designated subdirectory

---

## Priority 1 — Artifact Generation
**Branch:** `claude/artifact-generation-<id>`
**Complexity:** Low — pure prompt engineering, no external dependencies
**Impact:** Highest immediate visible value in every conversation

### What it does
At the completion of each workflow gate, the skill generates a ready-to-use, formatted document the designer can use immediately — not just coaching about what the document should contain.

### Artifacts to generate

| Trigger | Artifact | Format |
|---|---|---|
| Ecosystem audit complete | Audit exit criteria document | Markdown |
| Gate 1 approved | Learning Proposal | Markdown |
| Gate 2 approved | Project Charter with RACI | Markdown |
| Scope change identified | Stakeholder briefing package | Markdown |
| Pilot data collected | Diagnosis + recommendation document | Markdown |
| Estimation complete | Workload estimate with uncertainty buffer | Markdown table |
| Evaluation plan agreed | L1–L3 evaluation instruments | Markdown |

### How to build it
Add artifact generation trigger instructions to each reference file. Pattern:

```
## Artifact Output Trigger
When [condition] is confirmed, generate the following artifact:
- Title: [artifact name]
- Format: Markdown
- Required sections: [list]
- Populate with: [variables from the conversation]
- Tone: Stakeholder-ready, non-ID jargon
```

### Files to modify
- `references/hard-new.md` — ecosystem audit artifact, fidelity gate artifacts
- `references/stakeholder-communication.md` — scope change briefing artifact
- `references/workload-estimation.md` — estimation output artifact
- `references/evaluation-architecture.md` — evaluation plan artifacts
- `references/scope-creep-governance.md` — escalation briefing artifact

### Activation test
Prompt: *"I've just completed the ecosystem audit for a new QC system training project. No existing content found. Generate the exit criteria document."*
Expected: Formatted Markdown document, stakeholder-ready, all required sections populated from conversation context.

---

## Priority 2 — Memory Persistence Across Projects
**Branch:** `claude/memory-persistence-<id>`
**Complexity:** Low-medium — prompt engineering with memory system instructions
**Impact:** Eliminates the biggest friction point — re-establishing context every session
**Dependency:** None — can build independently of Priority 1

### What it does
The skill remembers who the user is, their experience level, active projects, and SME patterns across conversations. Context is established once and carried forward.

### What to persist

**Permanent (never expires):**
- User name, role, organization
- Years of experience and CPTD/credential status
- Preferred working style and communication register
- Tool stack — authoring tools, LMS, PM system

**Project-level (per active project):**
- Project name, classification result (e.g. Hard-New)
- Current gate status and last completed milestone
- SME names, roles, and behavioral notes (responsive, political, hesitant)
- Key decisions made and their rationale
- Scope changes logged with criticality level

**Calibration data (accumulates over time):**
- Estimated vs. actual hours per project type
- Estimation accuracy trend — used to narrow uncertainty buffer over time

### How to build it
Add memory instruction sections to `SKILL.md`:

```
## Memory Protocol

### On first conversation — capture and store:
- User name, role, organization, years of experience, credential status
- Tool stack and working environment

### On project intake — capture and store:
- Project name and classification
- SME ecosystem map
- Timeline and constraints

### On gate completion — update:
- Current gate status
- Key decisions and rationale

### On project close — store:
- Estimated vs. actual effort
- What caused variance
- SME reliability rating for future reference
```

### Files to modify
- `SKILL.md` — add Memory Protocol section after Level Sensing
- `references/sme-governance.md` — add SME memory capture instructions
- `references/workload-estimation.md` — add calibration data capture instructions

### Activation test
Session 1: Establish context — name, role, project details.
Session 2 (new conversation): Open with *"What project am I currently working on?"*
Expected: Skill recalls project name, classification, current gate, and SME details without being told again.

---

## Priority 3 — MCP Integration — Google Drive
**Branch:** `claude/mcp-google-drive-<id>`
**Complexity:** Medium — requires MCP server configuration
**Impact:** Skill stops being a conversation tool and becomes a workflow tool
**Dependency:** Priority 2 (memory) should be complete first
**Prerequisite:** Google Drive MCP server must be connected in Claude settings

### What it does
The skill can read and write actual project documents from the user's Google Drive — storyboards, proposals, design documents, SME feedback — without the user copying and pasting content into the conversation.

### Capabilities to enable

| Action | Trigger | Output |
|---|---|---|
| Read storyboard | "Audit my storyboard" | Pulls document from Drive, runs full audit framework |
| Write proposal | Gate 1 approved | Creates formatted Learning Proposal in Drive |
| Read SME feedback | "Here's the feedback doc" | Pulls comments, categorizes by criticality level |
| Write estimation | Estimation complete | Creates populated estimation sheet in Drive |
| Log scope change | Level B/A change identified | Appends change log entry to project document in Drive |

### How to build it
Use the `mcp-builder` skill to scaffold the Google Drive integration. Then add Drive action triggers to relevant reference files.

MCP server URL for Google Drive: `https://drive.mcp.claude.com/mcp`

### Files to modify
- `SKILL.md` — add Google Drive MCP server reference and action map
- `references/hard-new.md` — add Drive read trigger for ecosystem audit
- `references/designer-developer-handover.md` — add Drive write trigger for script/handover doc
- `references/scope-creep-governance.md` — add Drive write trigger for change log

### Activation test
Prompt: *"Pull my Learning Proposal draft from Drive and tell me what's missing."*
Expected: Skill accesses Drive, reads document, runs Gate 1 completeness check, returns itemized gap list.

---

## Priority 4 — Pre-Build Prototype Generator
**Branch:** `claude/prototype-generator-<id>`
**Complexity:** Medium — Claude artifact generation from structured input
**Impact:** Highest wow moment for designers and developers
**Dependency:** Priority 1 (artifact generation) should be complete first

### What it does
After Gate 2 is approved, the skill generates a working HTML prototype of the course architecture — a clickable skeleton the designer hands to the developer instead of a static document.

### Prototype contents
- Module and lesson structure as navigable HTML screens
- Placeholder interactions with correct interaction type labeled per screen
- Estimated screen count per module
- Developer layer annotations visible as tooltips or sidebar notes
- Color-coded complexity indicators per interaction type

### Input required from user
- Approved mind map structure (can be pasted as text or pulled from Drive if MCP connected)
- Modality confirmed (eLearning, ILT, blended)
- Authoring tool target (Storyline, Rise, Captivate)

### Output format
Single-file HTML artifact — self-contained, no external dependencies, opens in any browser. Designer downloads and shares with developer directly.

### How to build it
Add prototype generation instructions to `references/hard-new.md` Gate 2 section:

```
## Prototype Generation Trigger
When Gate 2 is approved and mind map is confirmed, offer:
"Would you like me to generate a clickable HTML prototype 
from this mind map for your developer handover?"

If yes — generate single-file HTML using this structure:
[prototype template instructions]
```

### Files to modify
- `references/hard-new.md` — add prototype generation trigger at Gate 2 completion
- `references/designer-developer-handover.md` — add prototype as optional handover artifact

### Activation test
Prompt: *"Gate 2 is approved. Here's the mind map: [paste mind map text]. Generate the developer prototype."*
Expected: Working HTML file with navigable module structure, labeled interactions, screen count estimates, and developer annotations.

---

## Priority 5 — Estimation Calibration Engine
**Branch:** `claude/estimation-calibration-<id>`
**Complexity:** Medium — requires memory persistence foundation
**Impact:** Turns estimation from principled guessing into personalized prediction
**Dependency:** Priority 2 (memory persistence) must be complete first

### What it does
After enough completed projects, the skill produces calibrated estimates based on the user's actual delivery history — not just a principled range but a personalized range that narrows over time.

### How calibration works

**Data collected per project at close:**
- Original estimate (hours/points)
- Actual hours/points delivered
- Uncertainty buffer applied
- Variables present: SME responsiveness, documentation quality, scope changes, team splits
- Final accuracy: over/under and by how much

**After 5+ projects:**
- Skill identifies the user's systematic bias (almost everyone underestimates a specific variable)
- Buffer recommendations become personalized — not 10-50% generic but "based on your history with fragmented SME teams, add 35-40%"
- Flags when current project resembles a previous one that ran over, and names the specific variable that caused it

### Calibration data structure
Store in memory as:

```
estimation_history:
  - project: [name]
    type: [Hard-New / Soft-Change / etc.]
    original_estimate: [hours]
    actual_hours: [hours]
    variance_pct: [%]
    variables_present: [list]
    notes: [what caused variance]
```

### Files to modify
- `references/workload-estimation.md` — add calibration data capture and retrieval instructions
- `SKILL.md` — add project close debrief prompt trigger

### Activation test
After 3+ projects logged: *"I'm estimating a new Hard-New project with a fragmented SME team. What buffer should I apply based on my history?"*
Expected: Personalized buffer recommendation with reference to specific past projects and their variance patterns.

---

## Priority 6 — Skills Gap Analyzer
**Branch:** `claude/skills-gap-analyzer-<id>`
**Complexity:** Medium-high — requires substantial conversation history
**Impact:** Turns the skill from a project tool into a career development tool
**Dependency:** Priorities 2 and 5 must be complete; requires 10+ conversations minimum
**Version target:** v4.0.0

### What it does
After enough conversations, the skill generates a personal development profile — a map of which ATD capability areas the user engages with confidently, which they consistently avoid or struggle with, and a recommended learning path based on actual project patterns.

### Capability dimensions tracked
Based on the ATD Talent Development Capability Model — 23 capabilities across three domains:
- Building Personal Capability
- Developing Professional Practice
- Impacting Organizational Capability

### What the analyzer produces

| Output | Description |
|---|---|
| Capability heat map | Which of the 23 ATD capabilities appear in conversations and at what confidence level |
| Avoidance patterns | Which capabilities the user consistently skips, delegates, or asks for help with |
| Strength confirmation | Which areas show consistent independent reasoning without coaching |
| Development priorities | Top 3 recommended capability areas based on pattern analysis |
| Learning path | Specific resources, frameworks, and practice opportunities per priority area |
| CPTD recertification relevance | Which recommended activities map to ATD recertification requirements |

### How to build it
Add periodic synthesis instruction to `SKILL.md`:

```
## Skills Gap Analysis Trigger
After every 10 conversations, if the user requests it:
Generate a capability profile by reviewing conversation patterns.
Identify: confident areas, coaching-dependent areas, avoided areas.
Map to ATD Talent Development Capability Model.
Produce development priority recommendations.
```

### Files to modify
- `SKILL.md` — add Skills Gap Analysis trigger and synthesis instructions
- `references/lxd-and-atd.md` — add ATD capability mapping reference for analyzer
- New file: `references/skills-gap-analyzer.md` — full analyzer framework and ATD capability map

### Activation test
After 10+ conversations: *"Generate my capability profile based on our work together."*
Expected: Structured profile with capability ratings, avoidance patterns, top 3 development priorities, and CPTD recertification mapping.

---

## Implementation Sequence Summary

| Priority | Feature | Branch | Complexity | Dependency |
|---|---|---|---|---|
| 1 | Artifact Generation | `claude/artifact-generation-<id>` | Low | None |
| 2 | Memory Persistence | `claude/memory-persistence-<id>` | Low-Med | None |
| 3 | MCP Google Drive | `claude/mcp-google-drive-<id>` | Medium | Priority 2 |
| 4 | Prototype Generator | `claude/prototype-generator-<id>` | Medium | Priority 1 |
| 5 | Estimation Calibration | `claude/estimation-calibration-<id>` | Medium | Priority 2 |
| 6 | Skills Gap Analyzer | `claude/skills-gap-analyzer-<id>` | Med-High | Priorities 2, 5 |

---

## Version Mapping

| Version | Features |
|---|---|
| v3.0.0 | Current — taxonomy engine, dual entry point, jidoka framework |
| v3.1.0 | Micro-level content block treatment engine (already scoped) |
| v3.2.0 | Artifact Generation (Priority 1) |
| v3.3.0 | Memory Persistence (Priority 2) |
| v3.4.0 | MCP Google Drive (Priority 3) |
| v3.5.0 | Prototype Generator (Priority 4) |
| v3.6.0 | Estimation Calibration (Priority 5) |
| v4.0.0 | Skills Gap Analyzer (Priority 6) |

---

*Last updated: April 2026 — master-instructional-design v3.0.0*
