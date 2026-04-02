# Generative AI & Agentic AI for Learning & Development

Load this file when the user wants to leverage AI in their L&D work — prompt engineering,
AI-assisted content creation, workflow automation, multi-agent design, or responsible AI guidance.

---

## Table of Contents
1. The L&D AI Landscape — Strategic Overview
2. Where AI Genuinely Accelerates L&D Work
3. Where AI Falls Short (and What to Do About It)
4. Prompt Engineering Fundamentals
5. Prompting for L&D — Patterns and Templates
6. Advanced Prompting Techniques
7. AI Tools Purpose-Built for L&D
8. General-Purpose AI Tools Applied to L&D
9. Agentic AI — Foundations
10. Multi-Agent Workflows for L&D
11. Building AI-Assisted L&D Pipelines
12. Responsible AI in L&D
13. AI and the Future of the ID Profession

---

## 1. The L&D AI Landscape — Strategic Overview

Generative AI is not a replacement for instructional design expertise — it is a force multiplier for practitioners who know how to use it. The practitioner's value has shifted: from being the person who can write, to being the person who can direct, evaluate, and elevate AI-generated content with deep expertise.

**Three tiers of AI application in L&D:**

| Tier | What it is | Examples |
|---|---|---|
| **Tier 1: AI-Assisted** | Human-led work, AI accelerates specific tasks | Using ChatGPT to draft a first-pass storyboard |
| **Tier 2: AI-Augmented** | AI and human collaborate at each stage | AI generates scenarios, ID refines and validates each one |
| **Tier 3: Agentic AI** | AI systems work autonomously through multi-step workflows | Agent research topic → outline → draft → QA → format → deliver |

Most L&D practitioners are at Tier 1-2 today. Tier 3 (agentic) is rapidly maturing and represents the frontier.

**The irreplaceable human elements**: Learner empathy, performance consulting judgment, ethical oversight, stakeholder navigation, context sensitivity, creative vision. AI cannot replace these — it depends on them.

---

## 2. Where AI Genuinely Accelerates L&D Work

### High-Value AI Applications

**Content first drafts**: AI can produce a solid first-draft storyboard, script, or module outline in minutes. The ID's job shifts to editorial direction and quality elevation — faster and often better than starting from scratch.

**Scenario and case study generation**: Describe the job role, decision context, and learning objective — AI generates realistic branching scenarios, character dialogue, and consequence paths at volume.

**Learning objective writing**: Feed AI your topic, Bloom's level, and audience — it drafts behavioral objectives. Review and refine for precision. Dramatically faster than blank-page drafting.

**Assessment item generation**: Generate multiple-choice, scenario-based, and application questions mapped to objectives. AI is especially strong at generating distractor options (plausible wrong answers).

**Content localization prep**: AI can translate and culturally adapt content as a starting point (always require human review for cultural nuance).

**Research and synthesis**: AI can rapidly synthesize background research on a topic, identify key concepts, and surface relevant frameworks — compressing the SME-information-gathering phase.

**Accessibility remediation**: AI tools (including Adobe Acrobat AI) can auto-generate alt text, summarize content for captions, and flag accessibility issues at scale.

**Personalization at scale**: AI can adapt content pathways, vocabulary complexity, and examples based on learner profile data — difficult to do manually at scale.

---

## 3. Where AI Falls Short

**Accuracy and hallucination**: AI confidently generates false information. Never publish AI-generated content without SME verification, especially for technical, legal, medical, or compliance content.

**Deep learner empathy**: AI cannot feel what a stressed nurse, a frustrated new employee, or a resistant manager experiences. Human empathy-driven design remains irreplaceable.

**Organizational context**: AI doesn't know your company culture, your stakeholders, your political landscape, or your learners' history with training. You do.

**Judgment calls**: When to challenge a stakeholder's solution, when training isn't the answer, when a scenario crosses a cultural line — these require human judgment.

**Novel creative vision**: AI recombines existing patterns. Genuinely original design thinking — a breakthrough interaction metaphor, a new learning experience architecture — still comes from humans.

**Mitigation strategies**: Build verification checkpoints into every AI-assisted workflow. Never let AI output go directly to learners without human review. Treat AI output as a first draft, not a final product.

---

## 4. Prompt Engineering Fundamentals

### The Anatomy of a High-Quality Prompt

**Role**: Tell the AI who it is. "You are an expert instructional designer with 20 years of experience in corporate compliance training."

**Context**: What's the situation? Audience, constraints, purpose. The more specific, the better.

**Task**: What exactly do you want? Be precise. "Write" is weaker than "Write a 5-question scenario-based knowledge check."

**Format**: How should the output be structured? "Format as a table with columns: Question | A | B | C | D | Correct Answer | Rationale"

**Constraints**: What should the AI avoid, limit, or include? "Do not use jargon. Keep each question under 40 words."

**Examples**: One or two examples of what good output looks like dramatically improve output quality. (Few-shot prompting)

**Evaluation criteria**: Tell the AI how you'll judge success. "The scenarios should feel realistic to a mid-career HR professional, not a textbook exercise."

### Prompt Quality Levels

| Level | Example |
|---|---|
| Weak | "Write a quiz about customer service" |
| Moderate | "Write 5 multiple choice questions about handling difficult customer complaints for retail employees" |
| Strong | "You are an expert ID. Write 5 scenario-based multiple choice questions for retail store associates (2-5 years experience) on de-escalating difficult customer complaints. Each question presents a realistic scenario, 4 options, correct answer identified, and 1-sentence rationale. Avoid textbook language. Use realistic retail settings." |

---

## 5. Prompting for L&D — Patterns and Templates

### Learning Objective Writing Prompt
```
You are an expert instructional designer skilled in Bloom's Revised Taxonomy.

Write 5 learning objectives for a module on [TOPIC] targeting [AUDIENCE DESCRIPTION].
- Objectives should be at the [BLOOM'S LEVEL: Remember/Understand/Apply/Analyze/Evaluate/Create] level
- Use precise action verbs appropriate to that Bloom's level
- Each objective should be measurable and observable
- Format: bulleted list, "Learners will be able to [verb] [specific content/task]"
```

### Scenario-Based Question Prompt
```
You are an expert instructional designer specializing in scenario-based learning.

Create 3 branching scenarios for [AUDIENCE] on [TOPIC/SKILL].
For each scenario:
- Setting: Realistic workplace context familiar to [AUDIENCE]
- Situation: A specific decision moment (not a theoretical question)
- 3 choices: one clearly correct, one plausible-but-wrong, one clearly incorrect
- Consequence for each choice: immediate realistic outcome + coaching feedback
- Tone: [formal/conversational/direct — match to audience]
- Avoid: jargon, obvious wrong answers, trick questions
```

### Storyboard First Draft Prompt
```
You are a senior instructional designer creating an eLearning storyboard.

Create a storyboard outline for a [X-minute] eLearning module on [TOPIC].
Audience: [DESCRIPTION]
Learning objectives: [LIST OBJECTIVES]
Delivery: [Articulate Storyline / Rise / other]

For each slide, provide:
- Slide number and title
- On-screen text (concise — no more than 50 words)
- Visual description (what the learner sees)
- Audio narration script
- Interaction type (click-to-reveal, quiz, video, text + graphic, etc.)
- Notes for the developer

Structure: Introduction → [Key concepts] → Practice scenario → Summary → Knowledge check
```

### SME Interview Question Generator
```
I am preparing to interview a subject matter expert on [TOPIC] to gather content for a training course.
Audience: [DESCRIPTION]
Performance goal: After training, learners should be able to [GOAL]

Generate 15 interview questions that will help me:
1. Identify what top performers do differently
2. Uncover common mistakes and misconceptions
3. Gather realistic examples and stories I can use in scenarios
4. Clarify the decision-making process involved
5. Identify what learners find most confusing

Format: numbered list, grouped by category
```

### Assessment Item Generation Prompt
```
You are an expert in assessment design for corporate learning.

Generate 10 multiple-choice questions on [TOPIC] for [AUDIENCE].
Bloom's level: [Apply / Analyze]
Format for each question:
- Stem (scenario-based, under 60 words)
- Option A (correct answer)
- Option B (plausible distractor — common misconception)
- Option C (plausible distractor — partially correct)
- Option D (plausible distractor — related but irrelevant)
- Rationale: 1-2 sentences explaining why A is correct
- Objective alignment: which learning objective this measures

Avoid: trick questions, "all of the above", double negatives, obvious wrong answers
```

### Feedback/Coaching Text for Scenarios
```
I have a scenario-based question with the following:
- Correct choice: [DESCRIPTION]
- Incorrect choice 1: [DESCRIPTION]
- Incorrect choice 2: [DESCRIPTION]

Write feedback text for each choice:
- Correct: Affirm + explain why it works (30-40 words)
- Incorrect 1: Name the error + redirect to correct thinking + why it matters (40-50 words)
- Incorrect 2: Name the error + redirect to correct thinking + why it matters (40-50 words)
Tone: [coaching/direct/supportive] — avoid "Wrong!" or "Correct!" as opening words
```

---

## 6. Advanced Prompting Techniques

### Chain-of-Thought Prompting
Ask the AI to reason step by step before giving the final answer. Use for complex analysis or multi-part ID problems.

"Before writing the learning objectives, first analyze the performance problem I've described, identify the root causes, determine whether training is the right solution, and then write objectives only for the components that are training-addressable. Show your reasoning."

### Few-Shot Prompting
Provide 1-3 examples of the output format you want before asking for new output. Dramatically improves formatting and style consistency.

"Here are two examples of scenario-based questions in our house style: [examples]. Now write 5 more in the same format for [topic]."

### Iterative Refinement
Don't try to get perfect output in one prompt. Layer:
1. Generate a first draft
2. "Revise this to make the scenario more realistic for [audience context]"
3. "Now tighten the word count by 20% without losing meaning"
4. "Rewrite the incorrect answer feedback to be more coaching-oriented, less critical"

### Persona Prompting
Give AI a specific expert persona to draw from — this narrows output style and expertise level dramatically.

"You are a performance consultant with 15 years of experience in financial services, trained in Cathy Moore's Action Mapping approach. Review this training outline from that perspective and identify where it is content-driven rather than performance-driven."

### Constraint-Stacking
Layer multiple constraints to get precise output:
"Write a scenario that is: under 80 words / set in a retail environment / involves a customer complaint about a product return / requires the employee to apply the company's 30-day return policy / has no obvious correct answer / avoids racial or gender stereotyping"

---

## 7. AI Tools Purpose-Built for L&D

### Course/Content Generation
| Tool | Best For |
|---|---|
| **Synthesia** | AI avatar video — rapid video production, 120+ languages, no filming required |
| **Articulate AI** (in Rise/Storyline) | Course outline generation, content drafting, image generation within Rise |
| **Lectora AI** | In-tool content drafting and assessment generation |
| **iSpring AI** | Scenario builder, quiz generation within iSpring Suite |
| **Coursebox AI** | Full course generation from documents/URLs; LMS-ready output |
| **Elucidat AI** | Content generation, localization at scale within the Elucidat platform |

### AI Writing & Scripting Assistants
| Tool | Best For |
|---|---|
| **Claude (Anthropic)** | Complex reasoning, long-form content, nuanced coaching, ethical analysis, agentic workflows |
| **ChatGPT (OpenAI)** | General content drafting, brainstorming, broad L&D tasks |
| **Gemini (Google)** | Google Workspace integration, research synthesis, multimodal input |
| **Jasper** | Marketing-flavored content; good for learning campaign copy |

### AI Image Generation for L&D
| Tool | Best For |
|---|---|
| **Midjourney** | Highest quality photorealistic and illustrative images; ideal for custom scenario characters |
| **Adobe Firefly** | Native in Creative Suite; commercially safe (trained on licensed content); great for extending photos, generating backgrounds |
| **DALL-E 3** (via ChatGPT) | Quick image generation inside ChatGPT workflow |
| **Stable Diffusion** | Open-source, locally runnable, highly customizable; for teams with technical capacity |

### AI Audio/Video
| Tool | Best For |
|---|---|
| **ElevenLabs** | Highest quality AI voice narration; voice cloning for brand consistency |
| **Descript** | Transcript-based video editing; remove filler words by editing text |
| **HeyGen** | AI avatar video + voice translation/lip-sync |
| **Adobe Podcast AI** | Narration cleanup, noise removal, voice enhancement (free, in-browser) |

### AI for Personalization and Adaptive Learning
| Tool | Best For |
|---|---|
| **Area9 Rhapsode** | Adaptive learning platform; AI adjusts content difficulty per learner |
| **Docebo AI** | LMS with AI-powered content recommendations and skill mapping |
| **Cornerstone AI** | Enterprise talent + learning AI for skill inference and pathway personalization |

---

## 8. General-Purpose AI Tools Applied to L&D

### Claude (Anthropic) — Deep Capabilities for L&D
- Best for: Complex instructional analysis, scenario writing with nuance, ethical edge cases, long document synthesis, agentic task chains, coaching conversations, code generation (JS for Storyline)
- Unique strength: Constitutional AI design makes it well-suited for sensitive topics in compliance, DEI, and mental health training
- Agentic capability: Claude can operate tools, browse the web, write and run code — powerful for multi-step L&D workflows

### ChatGPT (OpenAI)
- GPT-4o: Multimodal (text, image, voice); strong for rapid content drafting
- Custom GPTs: Build a dedicated "ID Assistant" GPT with your style guide, taxonomy, and examples baked in
- Code Interpreter: Analyze learner data, create charts, process spreadsheets inside the conversation

### Gemini (Google)
- Deep Google Workspace integration — summarize Drive documents, draft in Docs, analyze Sheets
- Gemini in Google Slides: Generate slide outlines and content from a prompt
- Strong for organizations in the Google ecosystem

### Perplexity AI
- Research assistant with real-time web search and citation
- Use for: rapid topic research, sourcing statistics and studies, finding recent L&D research

---

## 9. Agentic AI — Foundations

### What is Agentic AI?
Agentic AI refers to AI systems that can take sequences of actions autonomously to accomplish a goal — using tools, browsing the web, writing and running code, calling APIs, and making decisions along the way without a human approving each step.

**Key capabilities that make AI "agentic":**
- **Tool use**: AI can call external tools (search, code execution, file creation, API calls)
- **Planning**: AI breaks a goal into sub-tasks and sequences them
- **Memory**: AI retains context across steps (short-term) or across sessions (long-term via vector stores or external memory)
- **Self-correction**: AI evaluates its own output and retries or adjusts
- **Multi-agent coordination**: Multiple AI agents with different specializations work together

### Single Agent vs. Multi-Agent

| Type | How it works | L&D Example |
|---|---|---|
| **Single agent** | One AI with multiple tools completes a task autonomously | One Claude agent: research topic → draft objectives → write storyboard → format as template |
| **Multi-agent** | Specialized agents each handle one function; an orchestrator coordinates | Research agent + Writing agent + QA agent + Formatting agent — each expert at one thing |

Multi-agent systems produce higher quality than single-agent for complex tasks — specialization beats generalization at scale.

---

## 10. Multi-Agent Workflows for L&D

### Example: AI-Assisted Course Development Pipeline

**Orchestrator**: Master agent managing the workflow

**Agent 1 — Research Agent**
- Input: Topic, audience description, performance goal
- Tools: Web search, document analysis, academic database queries
- Output: Research brief (key concepts, common misconceptions, expert frameworks, statistics)

**Agent 2 — Needs Analysis Agent**
- Input: Research brief + existing performance data (if provided)
- Task: Determine training-addressable gaps, propose solution approach
- Output: Needs analysis summary, recommended learning objectives

**Agent 3 — Design Agent (ID Expert)**
- Input: Needs analysis, learning objectives, constraints (modality, time, tools)
- Task: Design the learning architecture — module structure, activity types, assessment approach
- Output: Design document / learning blueprint

**Agent 4 — Content Agent**
- Input: Design document, storyboard template, style guide
- Task: Write all on-screen text, narration scripts, scenario content, feedback text
- Output: Draft storyboard document

**Agent 5 — QA Agent**
- Input: Draft storyboard
- Checks: Bloom's alignment, reading level, scenario realism, accessibility language, style guide compliance
- Output: QA report with flagged items and suggested fixes

**Agent 6 — Formatting Agent**
- Input: Approved storyboard
- Task: Format to final template (Word/PowerPoint/Google Doc)
- Output: Production-ready storyboard deliverable

### Simpler Agentic Patterns for Individual IDs

**The "Stress Test" pattern**: After drafting your design, prompt Claude: "Act as a skeptical SME, a resistant learner, and a budget-focused sponsor. From each perspective, identify the weakest parts of this design and ask the hardest questions." Use responses to strengthen your design before stakeholder review.

**The "Persona Review" pattern**: "Review this scenario from the perspective of [specific audience persona]. What would feel unrealistic, irrelevant, or confusing to them? What would land well?"

**The "Critique and Rewrite" loop**: Submit a draft → get critique → ask AI to implement the top 3 fixes → review → repeat until satisfied. Typically 3-4 loops produces excellent output.

---

## 11. Building AI-Assisted L&D Pipelines

### Prompt Libraries — Build Yours
Maintain a personal/team library of proven prompts organized by task:
- Needs analysis prompts
- Objective writing prompts
- Scenario generation prompts
- Assessment prompts
- Feedback text prompts
- SME interview prep prompts
- Storyboard drafting prompts
- Evaluation planning prompts

Store in: Notion, Confluence, Google Doc, or a custom GPT system prompt.

### AI-Assisted Storyboard Workflow (Practical)
1. SME interview → record and transcribe with Otter.ai or Descript
2. Feed transcript to Claude: "Synthesize the key content from this SME interview relevant to [objective]. Identify the most important concepts, common mistakes, and realistic examples."
3. Use synthesis + objectives to prompt storyboard draft
4. Iterate storyboard through 2-3 AI refinement loops
5. Human ID reviews for accuracy, tone, learner empathy
6. SME review for accuracy (not design)
7. Build in authoring tool

### Version Control for AI-Generated Content
- Always save your prompt + the AI output together (prompts are documents — version control them)
- Track what was AI-generated vs. human-refined in your storyboard comments
- Maintain a "content decisions" log: why you kept, changed, or rejected AI suggestions

---

## 12. Responsible AI in L&D

### Accuracy and Hallucination Management
- **Never publish AI content without SME verification** — especially technical, legal, medical, financial content
- Build verification checkpoints into every AI-assisted workflow
- Use AI for structure and language, not as a source of truth on facts
- Cite sources independently of what AI suggests — verify each one

### Bias in AI-Generated Learning Content
- AI reflects patterns in its training data — which reflects historical biases
- Review all AI-generated scenarios for: demographic stereotyping, cultural assumptions, gender coding, ability assumptions
- Actively prompt for diversity: "Ensure the scenario characters reflect a diverse workforce. Vary gender, age, cultural background, and name diversity across scenarios."
- Have a DEI reviewer check AI-generated content before publication

### Learner Data Privacy
- Never input real learner PII (names, performance data, health information) into commercial AI tools without checking your organization's data governance policy
- Understand where AI tool providers store and train on your data (Claude, for instance, does not train on API inputs by default — verify for any tool)
- Anonymize all data before using it in AI prompts

### Transparency with Learners and Stakeholders
- Disclose when learning content was AI-assisted (organizational policy varies — know yours)
- Be prepared to explain what AI did and what humans validated
- Don't overclaim AI capabilities to stakeholders — set accurate expectations

### AI Ethics Framework for L&D Practitioners
Questions to ask before deploying AI in your L&D workflow:
1. Has AI-generated content been verified for accuracy by a qualified human?
2. Has it been reviewed for bias and cultural sensitivity?
3. Is learner data handled in compliance with privacy policies?
4. Is the AI application transparent to relevant stakeholders?
5. Does this AI use enhance or erode the quality of the learning experience?

---

## 13. AI and the Future of the ID Profession

### Skills That Become More Valuable With AI
- Performance consulting and needs analysis (AI can't replace the conversation)
- Learner empathy and audience insight
- Evaluation design and learning measurement
- Stakeholder influence and communication
- Creative vision and design judgment
- Ethical oversight of AI-generated content
- Prompt engineering and AI workflow architecture

### Skills That AI Is Automating (Partially)
- First-draft content writing
- Basic learning objective writing from topic lists
- Standard assessment item generation
- Template formatting and document production
- Translation and localization first passes

### The New L&D Practitioner Archetype
The most valuable L&D practitioners of the near future will be **AI-fluent design leaders** — people who can:
1. Diagnose a performance problem with rigor
2. Direct AI systems to produce high-quality draft content
3. Evaluate and elevate AI output with expert judgment
4. Architect multi-agent workflows for efficiency at scale
5. Maintain ethical and quality standards as the human in the loop
6. Communicate the value of learning design to business stakeholders

This is not a threat to the profession — it is an expansion of what one skilled practitioner can produce. The ceiling of impact has risen dramatically. The floor — for practitioners who don't adapt — is dropping.

---

## Cross-References to Other Skill Files

- For **Storyline JavaScript** that AI can generate and test → `references/authoring-tools.md` §9
- For **AI-assisted facilitation guide writing** → `references/facilitation-and-ilt.md` §3
- For **AI-powered needs analysis synthesis** (feeding SME interview transcripts to AI) → `references/facilitation-and-ilt.md` §9–11
- For **AI in CLO strategy** (learning analytics, skills inference, adaptive platform selection) → `references/lms-evaluation.md` §7
- For **academic research** on AI in learning (intelligent tutoring, adaptive learning systems) → `references/academic-courseware.md` §7


---
*© 2026 Norman Arosemena, CPTD. [CC BY-NC-ND 4.0](../../../LICENSE) — personal/educational use only; commercial use prohibited.*
