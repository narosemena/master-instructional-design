# Changelog

All notable changes to this skill are documented here.  
Format: [Semantic Versioning](https://semver.org/) — `MAJOR.MINOR.PATCH`

---

## [2.2.0] — 2026-04-29

### Added
- **`references/document-templates.md`** — 8 lean structural scaffolds for core L&D artifacts: Audience Analysis Report, Facilitator Guide, Job Aid/Quick Reference Card, Learning Objective Alignment Matrix, SME Interview Protocol, Content Audit Template, Storyboard, Program Communication Plan; Bitter Lesson compliant — section headers and `[PLACEHOLDER]` fields only
- **Artifact & Document Output Protocol** in `SKILL.md` — 5-rule consultative generation system: diagnose before drafting (ask 1–3 questions unless context is sufficient), consult as you build (name gaps, don't silently placeholder), apply three design lenses during the build (performance, inclusive, emotional), format for use (headers, tables, markdown-ready), close with ≤3 bullets including the most important design risk; generation does not bypass the skill's coaching identity — documents emerge from the consulting process
- **Router pattern at position 2** in `reference-router.py` — high-priority document generation intent pattern; catches generate/draft/create/build verbs before topic-specific patterns; standalone artifact names (facilitator guide, storyboard template, etc.) matched without requiring verb to prevent false-positive routing of informational questions

### Changed
- **README**: count updated 30 → 31 reference files (both occurrences); `document-templates.md` row added to reference table; "What it does" updated with Document & Artifact Generation bullet; "What's inside" expanded with Artifact Protocol description; "Tested against" block updated with 12/13 router accuracy and 10/10 consultative stance results; "Recent Enhancements" section added with v2.2.0, v2.1.0, v3.0.0 entries
- **SKILL.md version**: `3.0.0` → `3.0.0` (version held; protocol added as minor enhancement atop v3.0.0 base)

### Validated
- **Consultative stance**: 10/10 test cases — minimal-context requests diagnose before drafting; sufficient-context requests proceed directly; compliance traps fire performance lens before scaffold is touched; emotional high-risk topics fire all three lenses; every case closes with a practitioner-level design risk (not a generic placeholder note)
- **Router accuracy**: 12/13 pass — 1 acceptable edge case: "how do I create a job aid" routes to `document-templates.md` rather than `facilitation-and-ilt.md` (correct behavior — the scaffold is the useful context for that request)

---

## [3.0.1] — 2026-04-11

### Added
- **Classification Confidence Protocol** in `taxonomy-decision-engine.md` — model self-assesses classification confidence (0–100%) after reviewing prompt signals; proceeds at ≥70%, asks up to 2 targeted clarifying questions at <70%; includes collaborative framing and one-question-at-a-time instruction
- **First Interaction Protocol** in `SKILL.md` — when opening message is vague, skill offers 3 entry paths (classify project / audit artifact / explore framework) before asking diagnostic questions
- **Classification error recovery** in `taxonomy-decision-engine.md` — explicit instruction for when user rejects a classification: ask which dimension is wrong (New vs. Change, or Hard vs. Soft) and reclassify from correction rather than restarting the full diagnostic
- **Progress signaling** in Classification Confidence Protocol — skill acknowledges partial information and signals intent before asking clarifying questions

### Improved
- **Router vocabulary coverage** — added natural-language patterns to 7 routes covering 8 stress-test scenarios; coverage improved from 1/9 → 9/9 on the full scenario suite
- **Router priority order** — governance routes (sme-governance, stakeholder-communication, workload-estimation, scope-creep-governance, evaluation-architecture) moved above taxonomy fallback; prevents "where do we begin" from intercepting domain-specific prompts
- **test_router.py** — test harness now imports routes dynamically from production `reference-router.py` at runtime; eliminates manual sync requirement

### Fixed (GitHub hygiene)
- **`.skill` binary untracked** — removed from git tracking; add to `.gitignore`; should be published via GitHub Releases
- **`TECHNICAL-ROADMAP.md` untracked** — internal planning document removed from public visibility
- **`testing-scripts.md` moved** — relocated to `evaluations/` alongside existing eval files
- **`.gitignore` expanded** — now covers `*.skill`, `test_router.py`, `TECHNICAL-ROADMAP.md`, `*.pyc`, `__pycache__/`
- **`CLAUDE.md` cleaned** — gstack skill table (local dev tooling) replaced with single-line note; reference count corrected (14 → 30)

---

## [3.0.0] — 2026-04-11

### Added
- **Taxonomy Decision Engine** (`references/taxonomy-decision-engine.md`) — two-tier classification engine (Hard/Soft × New/Change) with 6-cell taxonomy matrix; entry point for all Project Mode engagements; routes to all workflow reference files
- **11 new workflow and governance reference files** completing the v3.0.0 architecture:
  - `references/hard-new.md` — ecosystem audit, fidelity ladder, Gate 1–3 protocol, scenario selection, designer-developer negotiation
  - `references/hard-change.md` — WIIFM reframing, unlearning design, ADKAR ownership, pre-launch gap conversation
  - `references/soft-change.md` — identity threat distinction, andragogical foundation, opening protocol, mid-session resistance handling
  - `references/soft-new.md` — prior scaffolding diagnostic, transfer vs. acquisition, heterogeneous cohort design, cross-level pairing
  - `references/stakeholder-communication.md` — verbatim language frameworks for sponsor conversations, scope change, evaluation commitment, escalation
  - `references/workload-estimation.md` — two-owner estimation model, SME involvement curve, uncertainty buffer calibration, definition of ready
  - `references/scope-creep-governance.md` — criticality taxonomy (A/B/C/D), two-decision model, silent absorption problem, jidoka escalation protocol
  - `references/evaluation-architecture.md` — root cause of missing evaluation, role accountability, Kirkpatrick teaching sequence, Level 4 timing constraint, design-time checklist
  - `references/sme-governance.md` — ecosystem mapping, approver vs. knower gap, single POC vs. lead SME model, verification protocol
  - `references/designer-developer-handover.md` — co-authoring reframe, script standards, developer creative liberty, equivalent value negotiation, pre-build prototype
- **`TECHNICAL-ROADMAP.md`** at repo root — documents planned features for roadmap phases 1–4 (artifact generation, memory persistence, coaching arc, performance analytics)
- **11 new keyword routes** in `reference-router.py` covering all new reference files; taxonomy routes at high priority

### Changed
- **SKILL.md version**: `2.1.0` → `3.0.0`
- **SKILL.md "For More Depth"**: 18 → 29 reference pointers
- **`CLAUDE.md`** reference count updated: 14 → 29 files; directory listing updated
- **Reference file count**: 18 → 29 total reference files

### Architecture note
The v3.0.0 rebuild introduces a taxonomy-first classification system as the entry point for all project coaching. Every incoming project is classified into a cell (Hard-New, Hard-Change, Soft-New, Soft-Change, or Mixed) before any design guidance is offered. Each cell has a dedicated reference file with full workflow, diagnostic protocols, and design principles. The classification router connects intake to the correct workflow automatically.

---

## [2.1.0] — 2026-04-02

### Added
- **7 new reference files** extracted from SKILL.md and supporting modules:
  - `references/situational-leadership.md` — SLII framework, development levels D1–D4, leadership style matching
  - `references/corporate-communications.md` — executive communication, stakeholder messaging, brand voice
  - `references/marketing-for-ld.md` — program launch strategy, learner engagement campaigns, L&D brand
  - `references/change-management.md` — ADKAR, Prosci, Kotter, change readiness and resistance
  - `references/lxd-and-atd.md` — extended LXD and ATD capability model reference
  - `references/academic-courseware.md` — graduate program canon, CLO strategy, organizational learning
  - `references/project-management.md` — extended project governance templates and workflows
- **Additional keyword routes** in `reference-router.py` for new files

### Changed
- **SKILL.md version**: `1.1.0` → `2.1.0`
- Total reference files: 14 → 18

---

## [1.1.0] — 2026-04-02

### Added
- **3 new reference files** extracted from SKILL.md for better context efficiency:
  - `references/coaching-stance.md` — coaching response patterns, error recovery, scope boundaries
  - `references/modes-deep-dive.md` — full guidance for all 15 engagement modes including Needs Analysis 7-step workflow and Formative Assessment Architecture
  - `references/quick-reference.md` — glossary of ID terms, key frameworks table, Kirkpatrick/Phillips quick reference
- **Reference router hook** (`.claude/hooks/reference-router.py`) — zero-LLM keyword router that injects the most relevant reference file path as `additionalContext` on every `UserPromptSubmit` event; 14 routing patterns covering all reference files
- **Claude Code hook wiring** (`.claude/settings.json`) — `UserPromptSubmit` command hook; 5-second timeout
- **GitHub Actions CI** (`.github/workflows/validate.yml`) — 8-check pipeline: JSON/Python syntax, description length (≤ 1024 chars), license footers, frontmatter fields, README count, bundle staleness, router smoke test
- **`build.sh`** — validates source then rebuilds `.skill` ZIP; `--check` flag for CI staleness detection; prints full manifest on each build
- **`CLAUDE.md`** — repo map, key constraints, dev workflow, new-file checklist; auto-loaded by Claude Code
- **`evaluations/skill-eval.xml`** — 10 verifiable evaluation Q&A pairs following mcp-builder Phase 4 spec, covering all major modes
- **`evaluations/run_eval.sh`** — evaluation runner; dry-run mode, single-question mode, token-matching pass/fail scoring
- **`testing-scripts.md`** — 30+ manual test prompts across all 15 modes with 8-dimension evaluation rubric
- **`version:` and `license:` fields** added to SKILL.md frontmatter
- **CC BY-NC-ND 4.0 license footer** added to all 14 reference files
- **`.gitignore`** — excludes `.claude/hooks/__pycache__/`

### Changed
- **SKILL.md trimmed**: 537 → 275 lines (~800 tokens lighter per invocation); verbose sections moved to dedicated reference files
- **SKILL.md description optimized**: 1011 → 851 chars (173 chars headroom); persona paragraph removed from trigger field; 13 new high-value trigger terms added: `storyboard`, `learning objective`, `curriculum design`, `needs analysis`, `task analysis`, `learner journey`, `LMS`, `LXP`, `blended learning`, `performance support`, `Kirkpatrick`, `branching scenario`, `formative assessment`
- **Mode 6 (LXD) emoji**: changed from 🎨 (duplicate of Mode 10 Adobe) to 🗺️
- **README**: reference count updated 11 → 14; table expanded with 3 new files; Claude Code install instructions rewritten with hook setup steps
- **LICENSE**: updated to CC BY-NC-ND 4.0 with full terms and commercial inquiry contact

### Fixed
- `.skill` bundle rebuilt — was stale (old 38KB SKILL.md, missing 3 reference files); now 133KB with all 14 reference files and current SKILL.md (19KB)
- README reference count mismatch (said 11, was 14)
- Broken Claude Code install command (malformed URL in backtick-fenced block)

---

## [1.0.0] — 2026-03-01

### Added
- Initial release
- SKILL.md with 15 engagement modes and 9-dimension audit framework (A–I)
- 11 reference files: `academic-courseware.md`, `agile-and-design.md`, `authoring-tools.md`, `evaluation-planning.md`, `facilitation-and-ilt.md`, `foundational-texts.md`, `generative-ai-for-ld.md`, `inclusive-emotional-design.md`, `lms-evaluation.md`, `lxd-and-atd.md`, `project-management.md`
- `master-instructional-design.skill` ZIP bundle for Claude.ai Projects upload
- `CONTRIBUTING.md` with IP and attribution standards
- LICENSE (CC BY-NC-ND 4.0)
- README with install instructions and capability overview
- Baseline evaluation score: **314/320 (98.1%)** across 10 progressive complexity challenges
