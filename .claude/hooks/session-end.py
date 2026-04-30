#!/usr/bin/env python3
"""
SessionEnd hook — appends a brief session summary to session-log.md.
Silently no-ops if the event carries no summary content.
"""
import json
import os
import sys
from datetime import date

data = json.load(sys.stdin)

summary = (
    data.get("session_summary")
    or data.get("summary")
    or data.get("transcript_summary")
    or ""
).strip()

if not summary:
    sys.exit(0)

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_path = os.path.join(repo_root, "session-log.md")

entry = f"\n## {date.today().isoformat()}\n\n{summary}\n"

with open(log_path, "a") as f:
    f.write(entry)
