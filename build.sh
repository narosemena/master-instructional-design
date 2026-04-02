#!/usr/bin/env bash
# build.sh — Regenerate master-instructional-design.skill bundle
#
# The .skill file is a ZIP archive containing SKILL.md and all reference files.
# Run this script from the repo root whenever source files change.
#
# Usage:
#   ./build.sh           # build to default output path
#   ./build.sh --check   # verify bundle is current (exit 1 if stale)

set -euo pipefail

SKILL_DIR="master-instructional-design"
OUTPUT="master-instructional-design.skill"
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
BUILD_TMP=$(mktemp -d)

cleanup() { rm -rf "$BUILD_TMP"; }
trap cleanup EXIT

# ── Validate source before building ──────────────────────────────────────────

echo "Validating source files..."

# Description length check
python3 - <<'EOF'
import re, sys
content = open("master-instructional-design/SKILL.md").read()
m = re.search(r'description: >\n(.*?)^---', content, re.MULTILINE | re.DOTALL)
if not m:
    print("ERROR: Cannot parse description from SKILL.md frontmatter")
    sys.exit(1)
desc = ' '.join(line.strip() for line in m.group(1).strip().splitlines())
count = len(desc)
if count > 1024:
    print(f"ERROR: Description is {count} chars — exceeds 1024-char limit by {count - 1024}")
    sys.exit(1)
print(f"  ✓ Description: {count}/1024 chars")
EOF

# JSON/Python syntax checks
python3 -m json.tool .claude/settings.json > /dev/null && echo "  ✓ settings.json valid"
python3 -m py_compile .claude/hooks/reference-router.py && echo "  ✓ reference-router.py valid"

# ── Build bundle ──────────────────────────────────────────────────────────────

if [[ "${1:-}" == "--check" ]]; then
    # Compare current source against existing bundle
    if [[ ! -f "$OUTPUT" ]]; then
        echo "ERROR: $OUTPUT does not exist — run ./build.sh to create it"
        exit 1
    fi

    # Build a fresh bundle in temp and compare checksums
    FRESH="$BUILD_TMP/fresh.zip"
    (cd "$SKILL_DIR" && zip -qr "$FRESH" SKILL.md references/)

    existing_sum=$(python3 -c "
import zipfile, hashlib
z = zipfile.ZipFile('$OUTPUT')
h = hashlib.sha256()
for name in sorted(z.namelist()):
    h.update(name.encode())
    h.update(z.read(name))
print(h.hexdigest())
")
    fresh_sum=$(python3 -c "
import zipfile, hashlib, sys
z = zipfile.ZipFile('$FRESH')
h = hashlib.sha256()
for name in sorted(z.namelist()):
    h.update(name.encode())
    h.update(z.read(name))
print(h.hexdigest())
")

    if [[ "$existing_sum" != "$fresh_sum" ]]; then
        echo "ERROR: Bundle is stale — run ./build.sh to rebuild"
        exit 1
    fi
    echo "✓ Bundle is current"
    exit 0
fi

# ── Build ─────────────────────────────────────────────────────────────────────

echo "Building $OUTPUT..."

PREV_SIZE=""
if [[ -f "$OUTPUT" ]]; then
    PREV_SIZE=$(wc -c < "$OUTPUT" | tr -d ' ')
fi

(cd "$SKILL_DIR" && zip -qr "$BUILD_TMP/bundle.zip" SKILL.md references/)
mv "$BUILD_TMP/bundle.zip" "$OUTPUT"

NEW_SIZE=$(wc -c < "$OUTPUT" | tr -d ' ')
REF_COUNT=$(ls "$SKILL_DIR/references/"*.md | wc -l | tr -d ' ')

echo ""
echo "  Built: $OUTPUT"
echo "  Size:  ${NEW_SIZE} bytes${PREV_SIZE:+ (was ${PREV_SIZE})}"
echo "  Contains: SKILL.md + ${REF_COUNT} reference files"
echo ""

# List contents
python3 - <<EOF
import zipfile
z = zipfile.ZipFile("$OUTPUT")
total = sum(i.file_size for i in z.infolist())
print(f"  {'File':<55} {'Size':>8}")
print(f"  {'-'*55} {'-'*8}")
for info in sorted(z.infolist(), key=lambda x: x.filename):
    print(f"  {info.filename:<55} {info.file_size:>8,}")
print(f"  {'-'*55} {'-'*8}")
print(f"  {'TOTAL (uncompressed)':<55} {total:>8,}")
EOF

echo ""
echo "Done. Commit $OUTPUT to keep the bundle current."
