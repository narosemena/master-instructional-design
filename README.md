---                                                                                                    
  # master-instructional-design                                                                                                                                                                                   
  A Claude skill that embodies a 30-year veteran instructional design practitioner — coaching, auditing, 
  and elevating every dimension of your L&D practice across 15 engagement modes and 30 on-demand       
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

  # 3. Copy the hook and settings to your project (or global) Claude config
  #    Run this from inside any project where you want the reference router active:
  mkdir -p .claude/hooks
  cp .claude/hooks/reference-router.py .claude/hooks/
  cp .claude/settings.json .claude/settings.json  # merge manually if you have an existing one
  ```

  The reference router hook (`reference-router.py`) automatically hints which reference file is most     
  relevant for each prompt — zero token cost, keyword-based. Runs on `UserPromptSubmit`.

  > **Already have a `.claude/settings.json`?** Manually merge the `hooks.UserPromptSubmit` block from   
  this repo's `.claude/settings.json` into yours rather than overwriting it.

  ---

  ## What's inside

  **SKILL.md** — the core skill file with 15 engagement modes, a 9-dimension audit framework, coaching   
  response patterns, diagnostic questions, and evaluation planning framework.

  **30 reference files** loaded on demand — never all at once, preserving context efficiency:

  | Reference file | Covers |
  | :--- | :--- |
  | `foundational-texts.md` | Adult learning theory, ID texts, cognitive science, immersive learning,    
  organizational learning |
  | `facilitation-and-ilt.md` | Workshop design, facilitation guides, VILT, needs analysis methods, job  
  aids, microlearning |
  | `authoring-tools.md` | Storyline, Rise, Captivate, Lectora, Camtasia + JavaScript/CSS/HTML coding    
  patterns |
  | `lxd-and-atd.md` | LXD frameworks, learner journey, ATD Capability Model, CPTD exam prep |
  | `agile-and-design.md` | Agile/Scrum for L&D, visual design, UX/UI, Adobe Creative Suite |
  | `generative-ai-for-ld.md` | Prompt engineering, AI tools, agentic workflows, responsible AI |        
  | `academic-courseware.md` | Graduate program canon, textbook tiers, ID theory frameworks, CLO strategy
   |
  | `lms-evaluation.md` | LMS/LXP selection, RFP process, platform comparison, learning data strategy |  
  | `project-management.md` | Project charters, RACI, design documents, style guides, QA checklists |    
  | `evaluation-planning.md` | Kirkpatrick L1–5, ROI methodology, survey templates, L3 observation tools 
  |
  | `inclusive-emotional-design.md` | DEI design, psychological safety, stereotype threat, emotional arc,
   trauma-informed design |
  | `coaching-stance.md` | Coaching response patterns, error recovery, feedback calibration, scope       
  boundaries |
  | `modes-deep-dive.md` | Full guidance for all 15 engagement modes including Needs Analysis workflow   
  and Formative Assessment Architecture |
  | `quick-reference.md` | Glossary of ID terms, key frameworks table, Kirkpatrick/Phillips quick        
  reference |
  | `situational-leadership.md` | SLII development levels (D1–D4), leadership style matching, L&D team   
  coaching, SLII failure modes |
  | `corporate-communications.md` | Executive communication (Pyramid Principle/BLUF), stakeholder message
   mapping, L&D brand voice, CLO presentation structure |
  | `marketing-for-ld.md` | 3-phase program launch framework, learner persona segmentation, L&D campaign 
  design, enrollment metrics |
  | `change-management.md` | ADKAR mapped to L&D interventions, change resistance types, change champion 
  network design, cannot vs. will-not diagnostic |
  | `taxonomy-decision-engine.md` | Two-tier classification engine (Hard/Soft × New/Change); 6-cell      
  taxonomy matrix; entry point for all project mode engagements |
  | `hard-new.md` | Ecosystem audit, fidelity ladder, Gate 1–3 protocol, scenario selection, SME
  governance for brand-new hard skills |
  | `hard-change.md` | WIIFM reframing, unlearning design, ADKAR ownership model, pre-launch gap
  conversation |
  | `soft-change.md` | Identity threat distinction, andragogical foundation, opening protocol,
  mid-session resistance handling |
  | `soft-new.md` | Prior scaffolding diagnostic, transfer vs. acquisition, heterogeneous cohort design, 
  cross-level pairing |
  | `mixed.md` | Keep-together vs. separate decision rule, judgment/system sequencing, verification      
  failure → separation rule |
  | `stakeholder-communication.md` | Verbatim language for sponsor conversations, scope change,
  evaluation commitment, escalation |
  | `workload-estimation.md` | Two-owner estimation model, SME involvement curve, uncertainty buffer     
  calibration, definition of ready |
  | `scope-creep-governance.md` | Criticality taxonomy (A/B/C/D), silent absorption problem, jidoka      
  escalation protocol |
  | `evaluation-architecture.md` | Root cause of missing evaluation, role accountability, Kirkpatrick    
  teaching sequence, Level 4 timing |
  | `sme-governance.md` | Ecosystem mapping, approver vs. knower gap, lead SME model, verification       
  protocol |
  | `designer-developer-handover.md` | Co-authoring reframe, script standards, developer creative        
  liberty, equivalent value negotiation |

  ---

  ## Tested against

  10 progressive complexity challenges — from writing a single learning objective (L1) to building a     
  3-year L&D capability strategy for a 5,000-person organization (L10).

  **Result: 314/320 (98.1%)** across alignment, learner-centeredness, cognitive load, practice/transfer, 
  feedback quality, engagement, visual design, DEI & inclusion, emotional design, theory grounding, and  
  consulting posture dimensions.

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
