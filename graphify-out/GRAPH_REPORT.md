# Graph Report - C:/Users/norma/master-instructional-design  (2026-04-11)

## Corpus Check
- 39 files · ~78,656 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 265 nodes · 269 edges · 54 communities detected
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 21 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `SKILL.md â€” Core Skill File v3.0.0` - 28 edges
2. `README â€” Master Instructional Design Skill Overview` - 14 edges
3. `ILT, VILT & Facilitation Design Reference` - 14 edges
4. `Authoring Tools â€” Expert Technical Reference` - 13 edges
5. `Academic Courseware & Graduate Program Canon` - 10 edges
6. `Evaluation Planning â€” Templates, Instruments & Methodology` - 10 edges
7. `Agile/Scrum for L&D, Visual Design, Adobe Creative Suite` - 9 edges
8. `Evaluation Architecture â€” Root Cause & Role Accountability` - 8 edges
9. `Coaching Stance â€” Response Patterns & Error Recovery` - 7 edges
10. `Designer-Developer Handover Framework` - 7 edges

## Surprising Connections (you probably didn't know these)
- `GEMINI.md â€” Repo Context for Gemini` --references--> `SKILL.md â€” Core Skill File v3.0.0`  [EXTRACTED]
  GEMINI.md → master-instructional-design/SKILL.md
- `CLAUDE.md â€” Repo Context for Claude Code` --references--> `Authoring Tools â€” Expert Technical Reference`  [EXTRACTED]
  CLAUDE.md → master-instructional-design/references/authoring-tools.md
- `GEMINI.md â€” Repo Context for Gemini` --references--> `Authoring Tools â€” Expert Technical Reference`  [EXTRACTED]
  GEMINI.md → master-instructional-design/references/authoring-tools.md
- `README â€” Master Instructional Design Skill Overview` --references--> `SKILL.md â€” Core Skill File v3.0.0`  [EXTRACTED]
  README.md → master-instructional-design/SKILL.md
- `README â€” Master Instructional Design Skill Overview` --references--> `Academic Courseware & Graduate Program Canon`  [EXTRACTED]
  README.md → master-instructional-design/references/academic-courseware.md

## Hyperedges (group relationships)
- **Evaluation Design Lifecycle â€” Architecture, Planning & Accountability** — ref_evaluation_architecture, ref_evaluation_planning, ref_eval_arch_level4_timing, ref_eval_arch_root_cause, concept_kirkpatrick_model [INFERRED 0.88]
- **Taxonomy Classification Workflow â€” Decision Engine, Hard-New, Hard-Change** — ref_hard_new, ref_hard_change, skill_proactive_risk_flags, skill_first_interaction_protocol [EXTRACTED 0.90]
- **Designer-Developer Fidelity System â€” Gates, Prototyping, Equivalent Value** — ref_handover_fidelity_ladder, ref_handover_equivalent_value, ref_handover_scenario_selection, rationale_prebuild_prototype [EXTRACTED 0.92]
- **SME Governance, Workload Estimation, and Scope Creep Governance form an integrated project risk management system** — sme_governance_involvement_curve, workload_estimation_sme_destroyer, scope_creep_criticality_taxonomy, scope_creep_escalation_protocol [INFERRED 0.88]
- **Taxonomy Decision Engine routes to Soft-Change, Soft-New, and Mixed classification workflows forming the classification-to-design pipeline** — taxonomy_decision_engine_core_matrix, soft_change_design_pattern, soft_new_reclassification_decision_tree, mixed_keep_together_vs_separate [EXTRACTED 0.92]
- **Psychological Safety, Stereotype Threat Mitigation, and Identity-Affirming Design form the inclusive emotional design prerequisite cluster** — inclusive_emotional_design_psychological_safety, inclusive_emotional_design_stereotype_threat, inclusive_emotional_design_identity_affirming, inclusive_emotional_design_emotional_arc [EXTRACTED 0.90]

## Communities

### Community 0 - "Skill Architecture & Versioning"
Cohesion: 0.09
Nodes (25): Skill Versioning & Changelog, Version 1.0.0 â€” Initial Release, Version 1.1.0 â€” Reference Router & CI Pipeline, Version 2.1.0 â€” 7 New Reference Files, Version 3.0.0 â€” Taxonomy Engine Release, Version 3.0.1 â€” Classification Confidence Protocol, CLAUDE.md â€” Repo Context for Claude Code, Rationale: Zero-LLM Keyword Router for Context Efficiency (+17 more)

### Community 1 - "Change Management & Communications"
Cohesion: 0.11
Nodes (20): ADKAR Change Model (Prosci), Pyramid Principle / BLUF Communication Structure, Rationale: Cannot vs Will-Not Prevents Training-for-Desire Gap, README â€” Master Instructional Design Skill Overview, ADKAR Mapped to L&D Interventions, Cannot vs Will-Not Diagnostic, Change Champion Networks, Change Management for L&D â€” Coaching Scaffold (+12 more)

### Community 2 - "Evaluation & ROI Frameworks"
Cohesion: 0.12
Nodes (19): Kirkpatrick Four Levels of Training Evaluation, Phillips ROI Methodology (Level 5), SCORM / xAPI Learning Standards, Rationale: Designer Accountability for Evaluation at Intake, Rationale: Level 4 Is a Timing Constraint Not a Capability Constraint, SCORM / xAPI / LMS Integration Reference, Kirkpatrick Teaching Sequence Without Jargon, Level 4 Timing Constraint â€” Critical Decision Rule (+11 more)

### Community 3 - "Adult Learning Theory Foundations"
Cohesion: 0.12
Nodes (19): 4C/ID Model â€” van MerriÃ«nboer, Andragogy â€” Knowles Adult Learning Principles, Keller's ARCS Motivation Model, Bloom's Revised Taxonomy, Cognitive Load Theory (Sweller), Dick & Carey Systematic Design Model, GagnÃ©'s Conditions of Learning & Nine Events, Merrill's First Principles of Instruction (+11 more)

### Community 4 - "Behavioral Design & Resistance"
Cohesion: 0.11
Nodes (19): Edmondson Psychological Safety Research, Learner Resistance as Design Problem, Psychological Safety as Design Prerequisite, Mixed-Change Cell 5 Design Approach, Shared Governance Foundation for All Projects, Scope Creep Root Cause Distinction, SME Onboarding Rhythm of Work Conversation, Soft-Change Design Pattern Self-Discovery Principle (+11 more)

### Community 5 - "ID Methodology & Accessibility"
Cohesion: 0.13
Nodes (17): SAM â€” Successive Approximation Model, Universal Design for Learning (UDL), WCAG 2.1 AA Accessibility Standard, GEMINI.md â€” Repo Context for Gemini, Adobe Creative Suite L&D Master Reference, Agile/Scrum for L&D, Visual Design, Adobe Creative Suite, SAM + Scrum Integration, Agile & Scrum for Learning Product Development (+9 more)

### Community 6 - "Hard-New Skill Design"
Cohesion: 0.26
Nodes (12): ATD Talent Development Capability Model, Rationale: Creation Bias as Motivation Gap Not Process Gap, Hard-New Full Workflow, Creation Bias â€” Design Motivation Gap, Ecosystem Audit Protocol â€” Hard-New Trigger, Priority 1 â€” Artifact Generation, Priority 5 â€” Estimation Calibration Engine, Priority 3 â€” MCP Google Drive Integration (+4 more)

### Community 7 - "Facilitation & DEI Practice"
Cohesion: 0.17
Nodes (12): Gilbert's Behavior Engineering Model, Blended Learning Architecture â€” 70-20-10, DEI & Inclusive Facilitation Practice, Facilitation Guide Format & Standards, ILT, VILT & Facilitation Design Reference, Performance Support & Job Aid Design, Microlearning Design Standards, Needs Analysis â€” Methods & Tools (+4 more)

### Community 8 - "Scope Creep Governance"
Cohesion: 0.17
Nodes (12): Mixed-New Cell 6 Design Approach, Scope Management and Change Control, Scope Change Criticality Taxonomy A B C D, Scope Creep Escalation Protocol, Silent Absorption Problem in Scope Creep, Two-Decision Model for Scope Creep Governance, SME Involvement Curve Across Project Phases, Scope Creep Mid-Sprint Escalation Language (+4 more)

### Community 9 - "Mixed Classification & Stakeholder Language"
Cohesion: 0.25
Nodes (8): Mixed Classification Keep Together vs Separate Decision, Mixed Scope Change Stakeholder Conversation, Mixed Verification Failure Separation Rule, Mixed Prior Capability Verification Protocol, Stakeholder Communication Templates, SME Verification Protocol for Learner Capability Claims, Pre-Launch Gap Conversation Change Management, Scope Change Conversation Full Sequence

### Community 10 - "Designer-Developer Handover"
Cohesion: 0.33
Nodes (7): Rationale: Handover as Co-Authoring Not Transfer Event, Rationale: Pre-Build Prototype for Experiential Fidelity Before Full Build, Designer-Developer Handover Framework, Co-Authoring Reframe â€” Designer-Developer Model, Equivalent Value Principle â€” Negotiation Protocol, Fidelity Ladder â€” Gate 1-3 Protocol, Scenario Selection Protocol â€” Option 2 Decomposition

### Community 11 - "Emotional & Inclusive Design"
Cohesion: 0.29
Nodes (7): Affective Filter (Krashen), DEI Content Design Specific Guidance, Immordino-Yang Emotion and Learning Research, Neuroscience Foundation of Emotion and Learning, Steele Stereotype Threat Research, Stereotype Threat Recognition and Mitigation, Designing for Emotion Identity and Belonging

### Community 12 - "Project Management & QA"
Cohesion: 0.33
Nodes (6): LMS Implementation and Change Management, Project Charter Template, Design Document Blueprint Template and Standards, L&D Project Lifecycle Overview, QA Checklist Pre-Launch, Waterfall vs Agile Choosing the Right Approach

### Community 13 - "Learner Experience Design"
Cohesion: 0.4
Nodes (5): Emotional Arc Design for Adult Learning, Three-Lens Framework (Performance, Inclusion, Emotion), Learner Experience Design (LXD) Definition, LXD vs Traditional Instructional Design, Learner Experience Design Mode

### Community 14 - "Situational Leadership & Soft Change"
Cohesion: 0.4
Nodes (5): When Situational Leadership Breaks Down, Situational Leadership Common L&D Manager Mistakes, Situational Leadership Development Level Cues in L&D, Situational Leadership Style Matching to Development Level, Soft-Change Andragogical Foundation Self-Discovery

### Community 15 - "ATD Capability Model"
Cohesion: 0.5
Nodes (4): 23 TD Capabilities Quick Reference, ATD Talent Development Capability Model, CPTD Credential Exam Prep and Recertification, ATD Capability Model Mode

### Community 16 - "L&D Marketing & Launch"
Cohesion: 0.5
Nodes (4): 3-Phase Launch Framework for L&D Programs, One-Page Campaign Plan Structure, L&D Marketing Effectiveness Metrics, Four Learner Persona Types for Campaign Segmentation

### Community 17 - "Engagement Modes Framework"
Cohesion: 0.5
Nodes (4): Audit Mode Design Dimension Framework, ILT VILT and Facilitation Design Mode, Inclusive and Emotional Design Universal Lens, Process Coach Mode Needs Analysis Workflow

### Community 18 - "SME Governance"
Cohesion: 0.5
Nodes (4): SME Governance Core Principle Structural not Relational, SME Dispute Resolution Authority, SME Ecosystem Mapping Approvers vs Knowers, SME Role Architecture Single vs Lead Consolidation

### Community 19 - "Router & CI Testing"
Cohesion: 0.67
Nodes (1): Router smoke test — exercises reference-router.py routes against stress-test sce

### Community 20 - "Learning Platform Strategy"
Cohesion: 0.67
Nodes (3): LMS vs LXP vs LRS Comparison, Learning Technology Ecosystem Map, Learning Data Strategy xAPI LRS and Analytics

### Community 21 - "LMS Selection & RFP"
Cohesion: 0.67
Nodes (3): LMS RFP Process Step-by-Step, LMS Evaluation Criteria Master Scorecard, LMS Selection Decision Framework

### Community 22 - "Quick Reference & Glossary"
Cohesion: 0.67
Nodes (3): Evaluation Planning Quick Framework Kirkpatrick, Key Frameworks Quick Reference, Glossary of Key ID Terms

### Community 23 - "Evaluation Stakeholder Conversations"
Cohesion: 0.67
Nodes (3): Evaluation Conversation with Stakeholders, Kirkpatrick Teaching Sequence for Stakeholders, Level 4 Evaluation Timing Constraint

### Community 24 - "Taxonomy Confidence Protocol"
Cohesion: 0.67
Nodes (3): Taxonomy Classification Confidence Protocol, Taxonomy Classification Confirmation Protocol, Taxonomy Classification Diagnostic Questions

### Community 25 - "Workload Estimation"
Cohesion: 0.67
Nodes (3): Estimation Calibration Accumulation Over Projects, Workload Estimation Core Problem Underestimation Bias, Workload Two-Owner Estimation Model Designer vs Developer

### Community 26 - "Trauma-Informed Design"
Cohesion: 1.0
Nodes (2): SAMHSA Trauma-Informed Framework for L&D, Trauma-Informed Learning Design

### Community 27 - "Growth Mindset & Identity Design"
Cohesion: 1.0
Nodes (2): Dweck Growth Mindset Research, Identity-Affirming Design

### Community 28 - "AI Learning Platforms"
Cohesion: 1.0
Nodes (2): AI-Powered Learning Platforms Emerging Category, LXP Selection Criteria

### Community 29 - "Build vs Buy Framework"
Cohesion: 1.0
Nodes (2): Build vs Buy vs Configure Decision Framework, Total Cost of Ownership TCO Model

### Community 30 - "LXD Journey Methods"
Cohesion: 1.0
Nodes (2): Human-Centered Design Methods for LXD, Learner Journey Framework Five Phases

### Community 31 - "Storyboard & Review Workflow"
Cohesion: 1.0
Nodes (2): Review and Approval Workflow Three-Gate Model, Storyboard Standards and Review Workflow

### Community 32 - "Soft-New Cohort Design"
Cohesion: 1.0
Nodes (2): Soft-New Cross-Level Pairs Activity Design, Soft-New Heterogeneous Cohort Expert Augmenter Model

### Community 33 - "Audit Mode Tests"
Cohesion: 1.0
Nodes (1): Audit Mode Tests

### Community 34 - "CLO Graduate Programs"
Cohesion: 1.0
Nodes (1): CLO & Learning Leadership Graduate Programs

### Community 35 - "Organizational Learning Theory"
Cohesion: 1.0
Nodes (1): Organizational Learning Theory Academic Canon

### Community 36 - "ID Research Methodology"
Cohesion: 1.0
Nodes (1): Research Methodology in ID

### Community 37 - "UDL Applied"
Cohesion: 1.0
Nodes (1): Universal Design for Learning (UDL) Applied

### Community 38 - "LMS Platform Guide"
Cohesion: 1.0
Nodes (1): Major LMS LXP Platform Reference Guide

### Community 39 - "LXD Tools & Artifacts"
Cohesion: 1.0
Nodes (1): LXD Tools and Artifacts

### Community 40 - "QC System Reference"
Cohesion: 1.0
Nodes (1): QC System Example Reference Case

### Community 41 - "Theory & Concepts Mode"
Cohesion: 1.0
Nodes (1): Theory and Concepts Mode

### Community 42 - "Co-Creation & Formative Assessment"
Cohesion: 1.0
Nodes (1): Co-Creation Mode Formative Assessment Architecture

### Community 43 - "Authoring Tool Expert Mode"
Cohesion: 1.0
Nodes (1): Authoring Tool Expert Mode

### Community 44 - "Agile & Scrum for L&D"
Cohesion: 1.0
Nodes (1): Agile and Scrum for L&D Mode

### Community 45 - "Graphic UX & UI Design Mode"
Cohesion: 1.0
Nodes (1): Graphic UX and UI Design Mode

### Community 46 - "Adobe Creative Suite Mode"
Cohesion: 1.0
Nodes (1): Adobe Creative Suite Mode

### Community 47 - "Generative AI & Agentic AI Mode"
Cohesion: 1.0
Nodes (1): Generative AI and Agentic AI Mode

### Community 48 - "Academic Courseware Mode"
Cohesion: 1.0
Nodes (1): Academic Courseware and Graduate Theory Mode

### Community 49 - "L&D Project Management Mode"
Cohesion: 1.0
Nodes (1): L&D Project Management Mode

### Community 50 - "CLO & Learning Leadership Mode"
Cohesion: 1.0
Nodes (1): CLO and Learning Leadership Mode

### Community 51 - "RACI Matrix L&D Roles"
Cohesion: 1.0
Nodes (1): RACI Matrix L&D Standard Roles

### Community 52 - "Style Guide Standards"
Cohesion: 1.0
Nodes (1): Style Guide What It Must Contain

### Community 53 - "Project Risk Register"
Cohesion: 1.0
Nodes (1): Project Risk Register

## Knowledge Gaps
- **144 isolated node(s):** `Router smoke test — exercises reference-router.py routes against stress-test sce`, `Skill Versioning & Changelog`, `Version 1.0.0 â€” Initial Release`, `Audit Mode Tests`, `8-Dimension Evaluation Rubric` (+139 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Trauma-Informed Design`** (2 nodes): `SAMHSA Trauma-Informed Framework for L&D`, `Trauma-Informed Learning Design`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Growth Mindset & Identity Design`** (2 nodes): `Dweck Growth Mindset Research`, `Identity-Affirming Design`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `AI Learning Platforms`** (2 nodes): `AI-Powered Learning Platforms Emerging Category`, `LXP Selection Criteria`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Build vs Buy Framework`** (2 nodes): `Build vs Buy vs Configure Decision Framework`, `Total Cost of Ownership TCO Model`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `LXD Journey Methods`** (2 nodes): `Human-Centered Design Methods for LXD`, `Learner Journey Framework Five Phases`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Storyboard & Review Workflow`** (2 nodes): `Review and Approval Workflow Three-Gate Model`, `Storyboard Standards and Review Workflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Soft-New Cohort Design`** (2 nodes): `Soft-New Cross-Level Pairs Activity Design`, `Soft-New Heterogeneous Cohort Expert Augmenter Model`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Audit Mode Tests`** (1 nodes): `Audit Mode Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `CLO Graduate Programs`** (1 nodes): `CLO & Learning Leadership Graduate Programs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Organizational Learning Theory`** (1 nodes): `Organizational Learning Theory Academic Canon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `ID Research Methodology`** (1 nodes): `Research Methodology in ID`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `UDL Applied`** (1 nodes): `Universal Design for Learning (UDL) Applied`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `LMS Platform Guide`** (1 nodes): `Major LMS LXP Platform Reference Guide`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `LXD Tools & Artifacts`** (1 nodes): `LXD Tools and Artifacts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `QC System Reference`** (1 nodes): `QC System Example Reference Case`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Theory & Concepts Mode`** (1 nodes): `Theory and Concepts Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Co-Creation & Formative Assessment`** (1 nodes): `Co-Creation Mode Formative Assessment Architecture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Authoring Tool Expert Mode`** (1 nodes): `Authoring Tool Expert Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Agile & Scrum for L&D`** (1 nodes): `Agile and Scrum for L&D Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Graphic UX & UI Design Mode`** (1 nodes): `Graphic UX and UI Design Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Adobe Creative Suite Mode`** (1 nodes): `Adobe Creative Suite Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Generative AI & Agentic AI Mode`** (1 nodes): `Generative AI and Agentic AI Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Academic Courseware Mode`** (1 nodes): `Academic Courseware and Graduate Theory Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `L&D Project Management Mode`** (1 nodes): `L&D Project Management Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `CLO & Learning Leadership Mode`** (1 nodes): `CLO and Learning Leadership Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `RACI Matrix L&D Roles`** (1 nodes): `RACI Matrix L&D Standard Roles`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Style Guide Standards`** (1 nodes): `Style Guide What It Must Contain`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Project Risk Register`** (1 nodes): `Project Risk Register`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SKILL.md â€” Core Skill File v3.0.0` connect `Skill Architecture & Versioning` to `Change Management & Communications`, `Evaluation & ROI Frameworks`, `Adult Learning Theory Foundations`, `ID Methodology & Accessibility`, `Hard-New Skill Design`, `Facilitation & DEI Practice`, `Designer-Developer Handover`?**
  _High betweenness centrality (0.133) - this node is a cross-community bridge._
- **Why does `README â€” Master Instructional Design Skill Overview` connect `Change Management & Communications` to `Skill Architecture & Versioning`, `Evaluation & ROI Frameworks`, `Adult Learning Theory Foundations`, `ID Methodology & Accessibility`, `Hard-New Skill Design`, `Facilitation & DEI Practice`, `Designer-Developer Handover`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Why does `Academic Courseware & Graduate Program Canon` connect `Adult Learning Theory Foundations` to `Skill Architecture & Versioning`, `Change Management & Communications`, `ID Methodology & Accessibility`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **What connects `Router smoke test — exercises reference-router.py routes against stress-test sce`, `Skill Versioning & Changelog`, `Version 1.0.0 â€” Initial Release` to the rest of the system?**
  _144 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Skill Architecture & Versioning` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._
- **Should `Change Management & Communications` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._
- **Should `Evaluation & ROI Frameworks` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._