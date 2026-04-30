# Changelog

All notable changes to this skill are documented here.  
Format: [Semantic Versioning](https://semver.org/) — `MAJOR.MINOR.PATCH`

---

## [3.1.0] — 2026-04-30

### Added — Skill Harness (Tier 1)
- **Cross-session project memory** (`memory.json`) — persists active project state across sessions. The `UserPromptSubmit` hook injects projects updated within 30 days as pre-loaded context. `## Memory Protocol` section in SKILL.md governs when to read, write, and merge. Users never re-brief audience or constraints again.
- **PreToolUse guardrail** (`guard-writes.py`) — intercepts Write/Edit tool calls targeting `SKILL.md` or any file in `references/` and prompts for confirmation. Protects the core skill harness from accidental overwrites.
- **Dynamic mode hints in router** — `reference-router.py` now detects unambiguous classification signals (soft-new, soft-change, hard-new, hard-change, mixed) and prepends a one-line design cell hint before the reference file route. Zero token overhead.
- **MCP integration template** (`.mcp.json.example`) — pre-configured template for Perplexity Ask (real-time research, free 2K calls/month), Google Drive (read source docs via OAuth), and Notion (sync project briefs and decisions). File is gitignored; each user provides their own credentials.

### Added — Specialist Subagents (Tier 2)
- **Needs Analyst subagent** (`.claude/agents/needs-analyst/`) — structured one-question-at-a-time intake covering five diagnostic areas: performance gap (behavioral, not topic), root cause (taxonomy signal), audience, constraints, success definition. Does not recommend solutions during intake. Confirms taxonomy cell and writes project brief to `memory.json`.
- **Evaluation Architect subagent** (`.claude/agents/eval-architect/`) — designs complete Kirkpatrick L1–L5 (Phillips ROI) evaluation architecture tied to a specific performance gap and business outcome. Requires confirmed gap before recommending instruments. Flags the top evaluation risk (typically no L3 infrastructure or missing baseline data). Reads active project memory to tailor the architecture.
- **Session log hook** (`session-end.py`) — appends session summaries to `session-log.md` (gitignored) on the `Stop` hook event. Silently no-ops when no summary is available.
- **Notion MCP** added to `.mcp.json.example` for syncing project briefs, design decisions, and risk logs to a shared Notion workspace.

### Changed
- `settings.json` — added `PreToolUse` (guard-writes.py) and `Stop` (session-end.py) hook registrations alongside existing `UserPromptSubmit`.
- `.gitignore` — added `memory.json`, `.mcp.json`, `session-log.md` to local-only gitignore entries.
- `README.md` — updated install instructions (all hooks + agents + MCP table), added subagent reference table, added v3.1.0 enhancements section.

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
