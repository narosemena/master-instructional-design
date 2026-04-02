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

    ("project-management.md",
     r"project charter|\braci\b|design document|storyboard standard"
     r"|style guide|scope creep|approval workflow|qa checklist"
     r"|stakeholder.*communic"),

    ("academic-courseware.md",
     r"dick.*carey|van merr|reigeluth|gagne|bloom.*taxon|graduate.*id"
     r"|doctoral|\bclo\b.*strateg|academic.*model|smith.*ragan"
     r"|merrill.*principle"),

    ("agile-and-design.md",
     r"\bscrum\b|\bsprint\b|backlog|visual design|typography|color theory"
     r"|\blayout\b|\badobe\b|photoshop|illustrator|\bux\b.*design"
     r"|\bui\b.*design"),

    ("lxd-and-atd.md",
     r"learner journey|\blxd\b|atd capability|\bcptd\b|empathy map"
     r"|human.centered design|experience design|journey map"),

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
