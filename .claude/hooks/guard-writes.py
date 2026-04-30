#!/usr/bin/env python3
"""
PreToolUse hook — protects SKILL.md and reference files from accidental overwrites.
Intercepts Write and Edit tool calls targeting protected paths and asks for confirmation.
"""
import json
import sys

data = json.load(sys.stdin)
tool = data.get("tool_name", "")
inp = data.get("tool_input", {})

PROTECTED = [
    "SKILL.md",
    "references/",
    "master-instructional-design/SKILL.md",
    "master-instructional-design/references/",
]

if tool in ("Write", "Edit"):
    path = inp.get("file_path", "")
    if any(p in path for p in PROTECTED):
        print(json.dumps({
            "decision": "ask",
            "reason": (
                f"Protected path: {path}\n"
                "This file is part of the core skill harness. "
                "Confirm you intend to modify it before proceeding."
            )
        }))
        sys.exit(0)
