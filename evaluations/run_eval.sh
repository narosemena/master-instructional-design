#!/usr/bin/env bash
# run_eval.sh — Run the master-instructional-design skill evaluation suite
#
# Sends each question from skill-eval.xml to Claude via the CLI with the
# skill loaded, then checks whether the expected answer appears in the response.
#
# Requirements:
#   - claude CLI installed and authenticated (claude --version)
#   - python3 with xml.etree.ElementTree (stdlib — no install needed)
#   - The skill installed at ~/.claude/skills/master-instructional-design/
#
# Usage:
#   ./evaluations/run_eval.sh                 # run all questions
#   ./evaluations/run_eval.sh --id 3          # run a single question by id
#   ./evaluations/run_eval.sh --dry-run       # print questions without sending
#
# Output:
#   Prints PASS/FAIL per question, then a summary score.
#   Exit code 0 if all pass, 1 if any fail.

set -euo pipefail

EVAL_FILE="$(dirname "$0")/skill-eval.xml"
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DRY_RUN=false
FILTER_ID=""

# ── Arg parsing ───────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true; shift ;;
    --id) FILTER_ID="$2"; shift 2 ;;
    *) echo "Unknown argument: $1"; exit 1 ;;
  esac
done

# ── Dependency checks ─────────────────────────────────────────────────────────
if [[ "$DRY_RUN" == false ]]; then
  if ! command -v claude &>/dev/null; then
    echo "ERROR: claude CLI not found. Install with: npm install -g @anthropic-ai/claude-code"
    exit 1
  fi
fi

if ! command -v python3 &>/dev/null; then
  echo "ERROR: python3 not found"
  exit 1
fi

# ── Extract Q&A pairs from XML ────────────────────────────────────────────────
python3 - "$EVAL_FILE" "$FILTER_ID" "$DRY_RUN" "$SKILL_DIR" <<'PYEOF'
import sys, os, subprocess, textwrap, xml.etree.ElementTree as ET

eval_file  = sys.argv[1]
filter_id  = sys.argv[2]   # "" = all
dry_run    = sys.argv[3] == "true"
skill_dir  = sys.argv[4]

tree = ET.parse(eval_file)
root = tree.getroot()
pairs = root.findall("qa_pair")

if filter_id:
    pairs = [p for p in pairs if p.get("id") == filter_id]
    if not pairs:
        print(f"ERROR: No qa_pair with id={filter_id} found")
        sys.exit(1)

PASS = "✓ PASS"
FAIL = "✗ FAIL"
SKIP = "  SKIP"
results = []

print(f"\n{'─'*70}")
print(f"  Master Instructional Design — Skill Evaluation")
print(f"  {len(pairs)} question(s) | {'DRY RUN' if dry_run else 'LIVE'}")
print(f"{'─'*70}\n")

for pair in pairs:
    qid      = pair.get("id")
    mode     = pair.get("mode", "")
    question = textwrap.dedent(pair.findtext("question", "").strip())
    expected = pair.findtext("answer", "").strip()
    rationale= textwrap.dedent(pair.findtext("rationale", "").strip())

    print(f"Q{qid} [{mode}]")
    print(f"  {question[:120]}{'...' if len(question) > 120 else ''}")
    print(f"  Expected: {expected}")

    if dry_run:
        print(f"  {SKIP} (dry run)\n")
        results.append(("skip", qid, question, expected, ""))
        continue

    # Build a prompt that asks for a direct answer
    prompt = (
        f"{question}\n\n"
        f"Answer concisely and directly. Your response must include the specific "
        f"term, name, or phrase that answers the question."
    )

    try:
        result = subprocess.run(
            ["claude", "--print", "--no-stream", prompt],
            capture_output=True, text=True, timeout=60,
            cwd=skill_dir
        )
        response = result.stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"  {FAIL} — timeout after 60s\n")
        results.append(("fail", qid, question, expected, "TIMEOUT"))
        continue
    except Exception as e:
        print(f"  {FAIL} — {e}\n")
        results.append(("fail", qid, question, expected, str(e)))
        continue

    # Check: each token in expected answer appears in response (case-insensitive)
    expected_tokens = [t.strip("(),;/") for t in expected.lower().split() if len(t) > 2]
    response_lower  = response.lower()
    matched = [t for t in expected_tokens if t in response_lower]
    score   = len(matched) / len(expected_tokens) if expected_tokens else 0

    if score >= 0.7:
        status = "pass"
        print(f"  {PASS} (matched {len(matched)}/{len(expected_tokens)} key terms)")
    else:
        status = "fail"
        missed = [t for t in expected_tokens if t not in response_lower]
        print(f"  {FAIL} (matched {len(matched)}/{len(expected_tokens)} — missing: {missed})")
        print(f"  Response excerpt: {response[:200]}...")

    results.append((status, qid, question, expected, response))
    print()

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"{'─'*70}")
passed = sum(1 for r in results if r[0] == "pass")
failed = sum(1 for r in results if r[0] == "fail")
skipped= sum(1 for r in results if r[0] == "skip")
total  = len(results) - skipped

if total > 0:
    pct = int((passed / total) * 100)
    print(f"  Result: {passed}/{total} passed ({pct}%)")
    if failed:
        print(f"  Failed: Q{', Q'.join(r[1] for r in results if r[0] == 'fail')}")
else:
    print(f"  Dry run complete — {skipped} questions printed, none sent")

print(f"{'─'*70}\n")

if failed:
    sys.exit(1)
PYEOF
