#!/usr/bin/env python3
"""
Reference router for master-instructional-design skill.
Reads a UserPromptSubmit event from stdin, keyword-matches the user's message,
and outputs additionalContext pointing to the most relevant reference file.
No LLM call — pure keyword matching, zero token cost.
"""
import json
import re
import sys

data = json.load(sys.stdin)
prompt = (data.get("message") or data.get("prompt") or "").lower()

base = "master-instructional-design/references/"

# Priority-ordered routes: first match wins
routes = [
    # --- Taxonomy and workflow-specific routes (high priority) ---
    ("taxonomy-decision-engine.md",
     r"taxonomy|classify.*project|project.*classif|\bhard.new\b|\bhard.change\b"
     r"|\bsoft.new\b|\bsoft.change\b|mixed.*project|project.*type|decision engine"
     r"|what (type|kind) of.*project|diagnos.*project|project.*cell"),

    ("hard-new.md",
     r"brand.new.*skill|never.*done.*before|ecosystem audit|fidelity ladder"
     r"|new.*procedure.*learn|new.*process.*learn|anchor trap|partial match"
     r"|hard new.*workflow|hard.new.*design"),

    ("hard-change.md",
     r"process.*change.*train|procedure.*change.*train|policy.*change.*train"
     r"|unlearn.*hard|wiifm.*change|hard.change.*workflow|hard.change.*design"
     r"|change.*resistance.*procedure"),

    ("soft-change.md",
     r"soft.change.*workflow|soft.change.*design|identity.*threat.*train"
     r"|reptilian.*react|andragog|opening protocol.*facilit"
     r"|mid.session.*resistance|behavior.*change.*identity"),

    ("soft-new.md",
     r"soft.new.*workflow|soft.new.*design|prior.*scaffolding"
     r"|heterogeneous.*cohort|transfer.*acquisition.*design|persona card"
     r"|expert augmenter|cross.level.*pair"),

    # --- Governance and project management (specific before general) ---
    ("stakeholder-communication.md",
     r"scope change.*conversation|sponsor.*conversation|pre.launch.*gap"
     r"|holding response.*sme|escalation.*briefing.*leader"
     r"|decision.maker.*not.*room|backlog.*urgency.*project"),

    ("workload-estimation.md",
     r"workload.*estimat|estimat.*workload|story.*point.*id|\bunderestimat\b"
     r"|uncertainty.*buffer|estimation.*destroy|two.owner.*estimat"
     r"|definition.*ready.*id"),

    ("scope-creep-governance.md",
     r"scope creep|criticality.*taxonomy|andon cord|jidoka.*ld"
     r"|silent absorption|change.*request.*sprint|level [abcd].*change.*request"
     r"|escalat.*designer.*leader"),

    ("evaluation-architecture.md",
     r"evaluation.*architecture|evaluation.*plan.*missing|level 4.*timing"
     r"|measurement.*infrastructure|uninformed.*yes.*eval"
     r"|evaluation.*baked.*design|approver.*knower.*eval"),

    ("sme-governance.md",
     r"\bsme\b.*governance|\bsme\b.*onboard|approver.*knower"
     r"|lead sme|sme.*ecosystem|sme.*verification|sme.*dispute"
     r"|sme.*involvement|subject matter expert.*govern"),

    ("designer-developer-handover.md",
     r"handover|designer.*developer|developer.*handover|script.*standard.*build"
     r"|equivalent value|pre.build.*prototype|developer layer"
     r"|negotiation.*stack.*build|co.author.*build"),

    # --- Original routes ---
    ("authoring-tools.md",
     r"storyline|rise 360|captivate|lectora|camtasia|ispring|authoring tool"
     r"|\bscorm\b.*build|\bxapi\b.*build|\bjavascript\b|\bcss\b|\bhtml\b"
     r"|interaction logic|publish.*course|trigger.*variable|variable.*trigger"),

    ("facilitation-and-ilt.md",
     r"\bilt\b|\bvilt\b|instructor.led|train.the.trainer|needs analysis"
     r"|task analysis|job aid|microlearning|live session|facilitat|debrief"
     r"|\bworkshop\b|\bblended\b"),

    ("generative-ai-for-ld.md",
     r"generative ai|agentic ai|prompt engineer|multi.agent|ai.*workflow"
     r"|responsible ai|ai tool.*learn|chatgpt|claude.*l.d"),

    ("evaluation-planning.md",
     r"kirkpatrick|\bl1\b|\bl2\b|\bl3\b|\bl4\b|\bl5\b|\broi\b|phillips"
     r"|evaluation strategy|learning analytics|measurement|smile sheet"
     r"|level.*evaluat"),

    ("inclusive-emotional-design.md",
     r"\bdei\b|psychological safety|stereotype threat|emotional design"
     r"|\bbelonging\b|trauma.informed|\budl\b|inclusive design"
     r"|learner resistance|emotional arc|identity.*learn"),

    ("lms-evaluation.md",
     r"\blms\b|\blxp\b|platform select|vendor.*rfp|learning management system"
     r"|learning record|\blrs\b|technology stack|\bscorm\b.*track"
     r"|\bxapi\b.*track"),

    ("corporate-communications.md",
     r"corporate communicat|executive communicat|stakeholder message"
     r"|communication plan|communicat.*strateg.*learn|brand voice.*learn"
     r"|messaging.*ld|internal comm.*ld"),

    ("project-management.md",
     r"project charter|\braci\b|design document|storyboard standard"
     r"|style guide|scope creep|approval workflow|qa checklist"
     r"|stakeholder.*communic"),

    ("academic-courseware.md",
     r"dick.*carey|van merr|reigeluth|gagne|bloom.*taxon|graduate.*id"
     r"|doctoral|\bclo\b.*strateg|academic.*model|smith.*ragan"
     r"|merrill.*principle"),

    ("situational-leadership.md",
     r"situational leader|\bslii\b|hersey.*blanchard|blanchard.*hersey"
     r"|development level.*d[1-4]|d[1-4].*development level"
     r"|directing.*coaching.*support|leader.*readiness"),

    ("agile-and-design.md",
     r"\bscrum\b|\bsprint\b|backlog|visual design|typography|color theory"
     r"|\blayout\b|\badobe\b|photoshop|illustrator|\bux\b.*design"
     r"|\bui\b.*design"),

    ("change-management.md",
     r"change management|\badkar\b|\bprosci\b|\bkotter\b|lewin.*change"
     r"|change readiness|change resistance|change champion"
     r"|organizational change|transformation.*learn|change impact"),

    ("lxd-and-atd.md",
     r"learner journey|\blxd\b|atd capability|\bcptd\b|empathy map"
     r"|human.centered design|experience design|journey map"),

    ("marketing-for-ld.md",
     r"marketing.*learn|learn.*marketing|marketing.*course|marketing.*program"
     r"|\bl.?d brand\b|learner engagement campaign"
     r"|program launch|launch.*course|launch.*program|learning campaign"
     r"|enrollment.*strateg|learn.*awareness|course.*promotion"),

    ("foundational-texts.md",
     r"book recommend|foundational text|research backing|adult learning theory"
     r"|evidence.based|learning science|seminal"),

    ("coaching-stance.md",
     r"how.*respond|feedback.*style|resistant.*learner|beginner.*user"
     r"|expert.*user|error recovery|scope.*boundary"),

    ("modes-deep-dive.md",
     r"audit mode|process coach|co.creation mode|authoring.*mode|lxd mode"
     r"|atd mode|agile mode|facilitation mode|clo mode|which mode"),

    ("quick-reference.md",
     r"glossary|what.*mean|framework.*list|compare.*framework"
     r"|kirkpatrick.*level|bloom.*level"),
]

match = next((base + f for f, p in routes if re.search(p, prompt)), None)

if match:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": f"Relevant reference file for this query: {match}"
        }
    }))
