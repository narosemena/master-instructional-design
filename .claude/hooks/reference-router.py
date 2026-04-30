#!/usr/bin/env python3
"""
Reference router for master-instructional-design skill.
Reads a UserPromptSubmit event from stdin, keyword-matches the user's message,
and outputs additionalContext pointing to the most relevant reference file.
Also injects active project memory from memory.json when present.
No LLM call — pure keyword matching, zero token cost.
"""
import json
import os
import re
import sys
from datetime import datetime, timedelta

data = json.load(sys.stdin)
prompt = (data.get("message") or data.get("prompt") or "").lower()

base = "master-instructional-design/references/"

# Priority-ordered routes: first match wins
# Architecture: specific cell routes first (when classification is determinable
# from the prompt), taxonomy as fallback (when it isn't), everything else below.
routes = [
    # --- Cell-specific routes (highest priority — direct classification) ---
    ("soft-change.md",
     r"soft.change.*workflow|soft.change.*design|identity.*threat.*train"
     r"|reptilian.*react|andragog|opening protocol.*facilit"
     r"|mid.session.*resistance|behavior.*change.*identity"
     r"|refus.*change|veteran.*resist|won.t adopt|pushback.*training"
     r"|gut feeling|gut instinct|trust.*instinct|trust.*gut|gut.*trust"
     r"|prefer.*gut|gut.*over.*protocol|resist.*adopt.*soft"
     r"|actively resist|openly resist"
     r"|muscle memory|professional identity|years.*habit"
     r"|intimidation.*tactic|aggressive.*empathetic|empathetic.*negotiation"),

    ("soft-new.md",
     r"soft.new.*workflow|soft.new.*design|prior.*scaffolding"
     r"|heterogeneous.*cohort|transfer.*acquisition.*design|persona card"
     r"|expert augmenter|cross.level.*pair"
     r"|newly promoted|first.time manager|never.*feedback"
     r"|never.*given.*feedback|constructive feedback.*fail"),

    ("hard-change.md",
     r"process.*change.*train|procedure.*change.*train|policy.*change.*train"
     r"|unlearn.*hard|wiifm.*change|hard.change.*workflow|hard.change.*design"
     r"|change.*resistance.*procedure"
     r"|transitioning.*to.*new|switching.*to.*new|replacing.*with.*new"
     r"|moving.*from.*to.*system|migrat.*new.*system"),

    ("hard-new.md",
     r"brand.new.*skill|never.*done.*before|ecosystem audit|fidelity ladder"
     r"|new.*procedure.*learn|new.*process.*learn|anchor trap|partial match"
     r"|hard new.*workflow|hard.new.*design"),

    ("mixed.md",
     r"\bmixed\b.*classif|classif.*\bmixed\b|judgment.*system.*skill"
     r"|keep together.*separate|separate.*keep together"
     r"|mixed.new|mixed.change|inseparable.*skill|system.*judgment.*design"
     r"|hard.*soft.*same.*intervention"
     r"|never used.*system|rolling out.*new.*system|new.*system.*experienc"
     r"|system.*never.*used|new.*platform.*experienc|experienc.*new.*system"
     r"|new.*tool.*experienc|experienc.*new.*tool"
     r"|waterfall.*agile|know.*system.*but.*resist|jira.*standup"
     r"|situational judgment|no single right answer"
     r"|ambiguous.*data.*decid|drone.*data.*decid"),

    # --- Governance and project management (before taxonomy — specific signals) ---
    ("sme-governance.md",
     r"\bsme\b.*governance|\bsme\b.*onboard|approver.*knower"
     r"|lead sme|sme.*ecosystem|sme.*verification|sme.*dispute"
     r"|sme.*involvement|subject matter expert.*govern"
     r"|sme.*retir|protective.*knowledge|tacit knowledge|resent.*l.d"),

    ("stakeholder-communication.md",
     r"scope change.*conversation|sponsor.*conversation|pre.launch.*gap"
     r"|holding response.*sme|escalation.*briefing.*leader"
     r"|decision.maker.*not.*room|backlog.*urgency.*project"
     r"|conflicting.*sponsor|competing.*stakeholder|caught.*between.*executive"
     r"|compliance.*culture.*conflict|legal.*hr.*conflict"),

    ("workload-estimation.md",
     r"workload.*estimat|estimat.*workload|story.*point.*id|\bunderestimat\b"
     r"|uncertainty.*buffer|estimation.*destroy|two.owner.*estimat"
     r"|definition.*ready.*id"
     r"|vr.*budget|escape room|budget.*fidelity"
     r"|budget.*timeline.*mismatch|gamif.*budget"),

    ("scope-creep-governance.md",
     r"scope creep|criticality.*taxonomy|andon cord|jidoka.*ld"
     r"|silent absorption|change.*request.*sprint|level [abcd].*change.*request"
     r"|escalat.*designer.*leader"
     r"|just add.*slides|add a few slides|sponsor.*demand"
     r"|onboarding.*module.*complex|simple.*module.*complex"),

    ("evaluation-architecture.md",
     r"evaluation.*architecture|evaluation.*plan.*missing|level 4.*timing"
     r"|measurement.*infrastructure|uninformed.*yes.*eval"
     r"|evaluation.*baked.*design|approver.*knower.*eval"),

    # --- Taxonomy fallback (when no specific route matches) ---
    ("taxonomy-decision-engine.md",
     r"taxonomy|classify.*project|project.*classif|\bhard.new\b|\bhard.change\b"
     r"|\bsoft.new\b|\bsoft.change\b|mixed.*project|project.*type|decision engine"
     r"|what (type|kind) of.*project|diagnos.*project|project.*cell"
     r"|where do i begin|where do we begin|just.*assigned.*project"
     r"|i.ve been assigned|i have.*been assigned"
     r"|new project.*where|how do i start.*project|just.*assigned.*course"),

    ("designer-developer-handover.md",
     r"handover|designer.*developer|developer.*handover|script.*standard.*build"
     r"|equivalent value|pre.build.*prototype|developer layer"
     r"|negotiation.*stack.*build|co.author.*build"),

    # --- Original routes ---
    ("authoring-tools.md",
     r"storyline|rise 360|captivate|lectora|camtasia|ispring|authoring tool"
     r"|\bscorm\b.*build|\bxapi\b.*build|\bjavascript\b|\bcss\b|\bhtml\b"
     r"|interaction logic|publish.*course|trigger.*variable|variable.*trigger"),

    ("document-templates.md",
     r"(?:generate|draft|create|build|write me a|give me a|produce)"
     r".*(?:facilitator guide|job aid|storyboard|audience analysis|alignment matrix"
     r"|sme interview|content audit|comm.*plan|program.*plan|design document|charter)"
     r"|storyboard template|audience analysis report|\balignment matrix\b"
     r"|sme interview protocol|content audit template|program communication plan"),

    ("facilitation-and-ilt.md",
     r"\bilt\b|\bvilt\b|instructor.led|train.the.trainer|needs analysis"
     r"|task analysis|job aid|microlearning|live session|facilitat|debrief"
     r"|\bworkshop\b|\bblended\b"),

    ("generative-ai-for-ld.md",
     r"generative ai|agentic ai|prompt engineer|multi.agent|ai.*workflow"
     r"|responsible ai|ai tool.*learn|chatgpt|claude.*l.d"
     r"|ai.driven|ai.powered|\bai\b.*crm|\bai\b.*tool.*adopt"
     r"|artificial intelligence.*learn|machine learning.*train"),

    ("evaluation-planning.md",
     r"kirkpatrick|\bl1\b|\bl2\b|\bl3\b|\bl4\b|\bl5\b|\broi\b|phillips"
     r"|evaluation strategy|learning analytics|measurement|smile sheet"
     r"|level [1-4].*evaluat|evaluat.*level [1-4]"
     r"|measure.*level [1-4]|level [1-4].*behav.*train"
     r"|level [1-4].*measure|behavior change.*after.*train"),

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
     r"|organizational change|transformation.*learn|change impact"
     r"|refusing.*use|won.t use|pushback.*tool|resist.*adopt"
     r"|transition.*adopt|won.t.*adopt"),

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

context_parts = []

# Dynamic mode hints — inject a one-line design cell hint when a classification
# signal is unambiguous. Helps prime the correct coaching stance before routing.
MODE_HINTS = [
    (r"\bsoft[- ]new\b|first.time manager|newly promoted|never.*given.*feedback"
     r"|awareness.*train|mindset.*shift.*train|never.*done.*before.*soft",
     "Hint: soft-new cell — favor pull-based acquisition; heterogeneous cohort risk is high."),
    (r"\bsoft[- ]change\b|resist.*adopt|won.t adopt|veteran.*resist|openly resist"
     r"|actively resist|pushback.*training|muscle memory|professional identity",
     "Hint: soft-change cell — address identity threat before content; WIIFM must land first."),
    (r"\bhard[- ]new\b|brand.new.*skill|never.*done.*before.*hard|ecosystem audit"
     r"|fidelity ladder|new.*procedure.*from scratch",
     "Hint: hard-new cell — ecosystem audit and fidelity ladder before scenario design."),
    (r"\bhard[- ]change\b|process.*change.*train|procedure.*change.*train"
     r"|unlearn|retraining|switching.*to.*new.*system|migrat.*new.*system",
     "Hint: hard-change cell — delta mapping first; WIIFM reframe before content rebuild."),
    (r"\bmixed\b.*classif|classif.*\bmixed\b|hard.*soft.*same.*intervention"
     r"|inseparable.*skill|keep together.*separate",
     "Hint: mixed cell — confirm keep-together vs. separate decision before sequencing."),
]
for pattern, hint in MODE_HINTS:
    if re.search(pattern, prompt, re.I):
        context_parts.append(hint)
        break

match = next((base + f for f, p in routes if re.search(p, prompt)), None)
if match:
    context_parts.append(f"Relevant reference file for this query: {match}")

# Project memory injection — reads memory.json from repo root; silently skips if
# missing or malformed so the hook never breaks routing.
try:
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    memory_path = os.path.join(repo_root, "memory.json")
    if os.path.exists(memory_path):
        with open(memory_path) as f:
            memory = json.load(f)
        cutoff = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        active = [p for p in memory.get("projects", []) if p.get("last_updated", "") >= cutoff]
        if active:
            lines = ["Active project memory:"]
            for p in active:
                lines.append(
                    f"• {p['name']} [{p.get('classification', '?')}]"
                    f" — updated {p.get('last_updated', '?')}"
                )
                for field, label in [("audience", "Audience"),
                                     ("performance_gap", "Gap"),
                                     ("constraints", "Constraints")]:
                    if p.get(field):
                        lines.append(f"  {label}: {p[field]}")
                for field, label in [("open_risks", "Risks"),
                                     ("design_decisions", "Decisions")]:
                    if p.get(field):
                        val = p[field]
                        lines.append(
                            f"  {label}: {'; '.join(val) if isinstance(val, list) else val}"
                        )
            context_parts.append("\n".join(lines))
except Exception:
    pass

if context_parts:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "\n\n".join(context_parts)
        }
    }))
