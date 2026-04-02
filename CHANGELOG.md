# Changelog

All notable changes to this skill are documented here.  
Format: [Semantic Versioning](https://semver.org/) — `MAJOR.MINOR.PATCH`

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
