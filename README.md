---                                                                                                    
  # master-instructional-design                                                                                                                                                                                   
  A Claude skill that embodies a 30-year veteran instructional design practitioner — coaching, auditing, 
  and elevating every dimension of your L&D practice across 15 engagement modes and 31 on-demand       
  reference files.

  ---

  ## ⚖️ Proprietary Framework & Terms of Use

  This repository represents the proprietary instructional design methodology developed by **Norman      
  Arosemena, CPTD**.

  * **For Individuals/Learners:** You are welcome to use this skill for personal research, study, and    
  non-commercial professional development.
  * **For Organizations/Consultancies:** Commercial use, redistribution, or "white-labeling" of this     
  framework or its underlying logic is strictly prohibited without a commercial license. For enterprise  
  licensing or consulting inquiries, please contact me directly.

  ---

  ## What it does

  Activates expert-level guidance across the full L&D spectrum:

  * **Instructional Design** — objectives, storyboards, assessments, scenario design, needs analysis,    
  task analysis
  * **eLearning Authoring** — Storyline, Rise, Captivate, Lectora, Camtasia, iSpring; advanced
  JavaScript/CSS
  * **Facilitation & Live Learning** — ILT/VILT workshop design, facilitation guides, train-the-trainer, 
  VILT platforms
  * **Learner Experience Design (LXD)** — learner journey mapping, empathy mapping, experience ecosystems
  * **Inclusive & Emotional Design** — psychological safety, stereotype threat, DEI content design,      
  emotional arc
  * **Agile/Scrum for L&D** — sprint-based ID, backlog writing, SAM + Scrum integration
  * **Visual Design, UX & UI** — visual hierarchy, typography, color, usability heuristics for eLearning 
  * **Adobe Creative Suite** — Photoshop, Illustrator, InDesign, After Effects, Premiere, XD workflows   
  for L&D
  * **Generative AI for L&D** — prompt engineering, AI-assisted ID workflows, agentic pipelines,
  responsible AI
  * **CLO & Learning Leadership** — organizational learning strategy, talent analytics, skills taxonomy, 
  3-year L&D strategy
  * **Academic ID Theory** — graduate program canon, major textbooks (Dick & Carey, Gagne, Smith & Ragan,
   Reigeluth, van Merrienboer, Bloom, Merrill)
  * **LMS/LXP Strategy** — platform selection, RFP process, learning data architecture, xAPI
  * **Project Management** — project charters, RACI matrices, design documents, QA checklists,
  stakeholder communications
  * **Evaluation Planning** — Kirkpatrick L1–5, ROI calculation, L3 manager observation, learning        
  analytics
  * **Document & Artifact Generation** — on-demand production of complete, populated L&D documents: facilitator guides, job aids, storyboards, audience analysis reports, alignment matrices, SME interview protocols, content audits, and communication plans; generation is consultative — the skill diagnoses before drafting and challenges assumptions during the build

  ---

  ## Who it's for

  * Instructional designers at all levels — from new practitioners to senior IDs
  * L&D managers and program designers building or auditing learning products
  * Graduate students in ID, LDT, EdTech, or related programs
  * CLOs and learning leaders shaping organizational learning strategy
  * Anyone who designs, builds, facilitates, or leads learning experiences

  ---

  ## Install

  ### Claude.ai (Projects)

  1.  Download `master-instructional-design.skill` from the
  [Releases](https://github.com/narosemena/master-instructional-design/releases) page
  2.  Open your Claude Project → Skills → Upload skill
  3.  The skill activates automatically when relevant topics are mentioned

  ### Claude Code

  ```bash
  # 1. Clone the repo
  git clone https://github.com/narosemena/master-instructional-design
  cd master-instructional-design

  # 2. Copy the skill files to your global Claude Code skills directory
  cp -r master-instructional-design ~/.claude/skills/

  # 3. Copy hooks and settings to your project (or global) Claude config
  #    Run this from inside any project where you want the skill harness active:
  mkdir -p .claude/hooks
  cp .claude/hooks/reference-router.py .claude/hooks/
  cp .claude/hooks/guard-writes.py .claude/hooks/
  cp .claude/hooks/session-end.py .claude/hooks/
  cp -r .claude/agents .claude/agents
  cp .claude/settings.json .claude/settings.json  # merge manually if you have an existing one
  ```

  The reference router hook (`reference-router.py`) automatically hints which reference file is most
  relevant for each prompt — zero token cost, keyword-based. Runs on `UserPromptSubmit`. The guardrail
  hook (`guard-writes.py`) protects `SKILL.md` and all reference files from accidental overwrites via
  `PreToolUse`.

  > **Already have a `.claude/settings.json`?** Manually merge the `hooks` block from this repo's
  `.claude/settings.json` into yours rather than overwriting it.

  **Optional: MCP integrations** — each user provides their own credentials. Copy the template and rename it, then set your environment variables:

  ```bash
  cp .mcp.json.example .mcp.json   # gitignored — stays local to your machine
  ```

  | Server | Env var(s) | How to get credentials |
  | :--- | :--- | :--- |
  | Perplexity | `PERPLEXITY_API_KEY` | Sign up at [perplexity.ai](https://www.perplexity.ai/) — free tier 2,000 calls/month |
  | Google Drive | `GDRIVE_CLIENT_ID`, `GDRIVE_CLIENT_SECRET` | Google Cloud Console → APIs & Services → OAuth 2.0 Client ID (free) |
  | Notion | `NOTION_API_KEY` | notion.so/my-integrations → New integration → copy Internal Integration Token (free) |

  Users who don't need MCP integrations can skip this step entirely — the skill and routing hook work without it.

  ---

  ## What's inside

  **Specialist subagents** — isolated agents with focused expertise:

  | Subagent | Trigger | What it does |
  | :--- | :--- | :--- |
  | `needs-analyst` | "new project", "intake", "I've been assigned…", "where do I begin" | One-question-at-a-time intake: performance gap → root cause (taxonomy signal) → audience → constraints → success definition. Writes to `memory.json`. |
  | `eval-architect` | Kirkpatrick, ROI, Level 3/4 evaluation, measurement strategy | Designs L1–L5 evaluation architecture tied to the performance gap. Flags L3 infrastructure gaps and missing baselines. |

  **SKILL.md** — the core skill file with 15 engagement modes, a 9-dimension audit framework, coaching response patterns, diagnostic questions, evaluation planning framework, and the **Artifact & Document Output Protocol** — a consultative document generation system that diagnoses before drafting, applies the three design lenses during the build, and closes with the most important design risk the document reveals.

  **18 reference files** loaded on demand — never all at once, preserving context efficiency:

  | Reference file | Covers |
  | :--- | :--- |
  | `foundational-texts.md` | Adult learning theory, ID texts, cognitive science, immersive learning, organizational learning |
  | `facilitation-and-ilt.md` | Workshop design, facilitation guides, VILT, needs analysis methods, job aids, microlearning |
  | `authoring-tools.md` | Storyline, Rise, Captivate, Lectora, Camtasia + JavaScript/CSS/HTML coding patterns |
  | `lxd-and-atd.md` | LXD frameworks, learner journey, ATD Capability Model, CPTD exam prep |
  | `agile-and-design.md` | Agile/Scrum for L&D, visual design, UX/UI, Adobe Creative Suite |
  | `generative-ai-for-ld.md` | Prompt engineering, AI tools, agentic workflows, responsible AI |
  | `academic-courseware.md` | Graduate program canon, textbook tiers, ID theory frameworks, CLO strategy |
  | `lms-evaluation.md` | LMS/LXP selection, RFP process, platform comparison, learning data strategy |
  | `project-management.md` | Project charters, RACI, design documents, style guides, QA checklists |
  | `evaluation-planning.md` | Kirkpatrick L1–5, ROI methodology, survey templates, L3 observation tools |
  | `inclusive-emotional-design.md` | DEI design, psychological safety, stereotype threat, emotional arc, trauma-informed design |
  | `coaching-stance.md` | Coaching response patterns, error recovery, feedback calibration, scope boundaries |
  | `modes-deep-dive.md` | Full guidance for all 15 engagement modes including Needs Analysis workflow and Formative Assessment Architecture |
  | `quick-reference.md` | Glossary of ID terms, key frameworks table, Kirkpatrick/Phillips quick reference |
  | `situational-leadership.md` | SLII development levels (D1–D4), leadership style matching, L&D team coaching, SLII failure modes |
  | `corporate-communications.md` | Executive communication (Pyramid Principle/BLUF), stakeholder message mapping, L&D brand voice, CLO presentation structure |
  | `marketing-for-ld.md` | 3-phase program launch framework, learner persona segmentation, L&D campaign design, enrollment metrics |
  | `change-management.md` | ADKAR mapped to L&D interventions, change resistance types, change champion network design, cannot vs. will-not diagnostic |

  ---

  ## Tested against

  **Complexity challenges (L1–L10)** — from writing a single learning objective to building a 3-year L&D capability strategy for a 5,000-person organization.

  **Result: 314/320 (98.1%)** across alignment, learner-centeredness, cognitive load, practice/transfer, feedback quality, engagement, visual design, DEI & inclusion, emotional design, theory grounding, and consulting posture dimensions.

  **Router accuracy** — 19-pattern keyword router smoke-tested across all reference files.

  **Result: 12/13 pass** (1 acceptable edge case: "how do I create a job aid" routes to `document-templates.md` rather than `facilitation-and-ilt.md` — correct behavior since the scaffold is the useful context for that request).

  **Consultative stance validation** — 10 artifact generation scenarios tested to confirm the Artifact Protocol does not bypass the skill's coaching identity.

  **Result: 10/10 pass** across: minimal-context requests (diagnose before drafting), sufficient-context requests (proceed directly), compliance traps (performance lens fires before scaffold is touched), emotional high-risk topics (all three lenses fire before the document is started), specific constraints (addressed inline during the build), and scope-undefined requests (minimum load-bearing questions asked). Every test closed with a practitioner-level design risk, not a generic placeholder note.

  ---

  ## Recent Enhancements

  **v3.2.0 — Specialist Subagents + Session Continuity (Tier 2)**

  * **Needs Analyst subagent** (`.claude/agents/needs-analyst/`) — runs a structured one-question-at-a-time intake interview: performance gap, root cause (taxonomy signal), audience, constraints, success definition. Does not recommend solutions during intake. Ends by confirming the taxonomy cell and offering to save the project brief to `memory.json`.
  * **Evaluation Architect subagent** (`.claude/agents/eval-architect/`) — designs complete Kirkpatrick L1–L5 (Phillips ROI) evaluation architectures tied to a specific performance gap and business outcome. Flags the top evaluation risk (usually no L3 infrastructure or missing baseline data). Reads active project memory if available.
  * **Session log hook** (`session-end.py`) — appends session summaries to `session-log.md` (gitignored) on `Stop`. Silently no-ops when no summary is available.
  * **Notion MCP** — `.mcp.json` now includes the Notion server for syncing project briefs, design decisions, and risk logs to a shared workspace. Requires `NOTION_API_KEY` (free with Notion account).

  **v3.1.0 — Skill Harness Upgrades (Tier 1)**

  * **Cross-session project memory** — `memory.json` (gitignored) persists active project state across sessions. The `UserPromptSubmit` hook injects active projects (updated within 30 days) as pre-loaded context. A `## Memory Protocol` section in SKILL.md governs when to read, write, and merge. Never re-brief the audience or constraints again.
  * **PreToolUse guardrail hook** — `guard-writes.py` intercepts Write/Edit tool calls targeting `SKILL.md` or any file in `references/` and prompts for confirmation before proceeding. Protects the core skill harness from accidental overwrites.
  * **Dynamic mode hints** — the reference router now detects unambiguous classification signals (soft-new, soft-change, hard-new, hard-change, mixed) and injects a one-line design cell hint before routing. Primes the correct coaching stance without adding tokens.
  * **Perplexity MCP** — `.mcp.json` wires in the Perplexity Ask server for real-time research during sessions. Free tier: 2,000 calls/month. Set `PERPLEXITY_API_KEY` in your environment.
  * **Google Drive MCP** — `.mcp.json` also includes the Google Drive server for reading source documents (SME notes, existing decks, stakeholder briefs) directly from Drive. Requires `GDRIVE_CLIENT_ID` and `GDRIVE_CLIENT_SECRET` (free OAuth).

  **v2.2.0 — Artifact & Document Generation**
  * New `document-templates.md` — 8 structural scaffolds (facilitator guide, job aid, storyboard, audience analysis, alignment matrix, SME interview protocol, content audit, program communication plan)
  * New **Artifact & Document Output Protocol** in SKILL.md — consultative generation: diagnose before drafting, consult during the build, close with the key design risk
  * Router updated with generation-intent pattern (position 2 — high priority)
  * Protocol refined after 10-case consultative stance test: generation does not bypass coaching identity; documents emerge from the consulting process, not in place of it

  **v2.1.0 — Four New Domains + Efficiency Audit**
  * 4 new reference files: `situational-leadership.md`, `corporate-communications.md`, `marketing-for-ld.md`, `change-management.md`
  * Two-pass Bitter Lesson efficiency audit across 9 files — removed encyclopedic content the model already knows (Bloom's definitions, Kirkpatrick level descriptions, CRAP principles, Nielsen's heuristics, UDL principle descriptions, 70-20-10 breakdown, WCAG numbered criteria, 23 TD Capabilities prose); replaced with practitioner-specific decision trees, failure modes, and application tables
  * Bundle reduced ~2.3% compressed; router expanded to 18 patterns

  **v3.0.0 — Taxonomy Decision Engine (prior release)**
  * Two-tier project classification: Hard/Soft × New/Change — 4 cell-specific reference files plus a `mixed.md` for inseparable skills
  * 11 new governance and project management reference files (SME governance, scope creep, workload estimation, evaluation architecture, stakeholder communication, designer-developer handover)
  * Knowledge graph of all skill nodes via graphify

  ---

  ## How to use it

  Just mention what you're working on. The skill activates automatically based on context. Examples:     

    * *"Audit these 5 learning objectives for a new manager course"*
    * *"Design a blended onboarding program for software engineers"*
    * *"Our CSAT dropped 11 points — the sponsor thinks agents need product knowledge training. What do I
   do?"*
    * *"Help me write JavaScript to track variable states in Storyline"*
    * *"Build a 3-year L&D strategy for a 5,000-person financial services firm"*

  ---

  ### 🛠️ Work with Me

  If you are looking to elevate your organization's learning ecosystem or require a customized deployment
   of this AI framework, let's connect.

    * **Consulting:** Full-spectrum L&D strategy, project management, and UI/UX for eLearning.
    * **Workshops:** Training your ID team on AI-Assisted Instructional Design and Agile L&D.

  **[Contact me via LinkedIn](https://www.linkedin.com/in/normanarosemena/) or open a private inquiry via
   GitHub Issues.**

  ---

  ## Attribution & Disclaimer

  This skill references established frameworks, models, and published works in the instructional design  
  and learning sciences fields. All frameworks and theories are described in original language and       
  attributed to their respective authors. Tool and product names are trademarks of their respective      
  owners.

  **This project is a personal endeavor created by Norman Arosemena. It is not affiliated with, endorsed 
  by, or representative of any current or past employers.**

  ---

  ## License

  [CC BY-NC-ND 4.0](https://www.google.com/search?q=LICENSE) — This work is licensed under a Creative    
  Commons Attribution-NonCommercial-NoDerivs 4.0 International License.

  ---

  ## Feedback & Requests

  While this is a proprietary framework, I value community feedback. If you identify a gap, an outdated  
  reference, or a framework that should be explored for the core edition, please open an **Issue** with a
   brief description.

  ---
