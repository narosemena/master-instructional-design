# master-instructional-design — Claude Code Context

This repo is a Claude skill for expert-level instructional design coaching. It ships a skill harness (SKILL.md + 14 reference files) and a Claude Code hook that routes prompts to the right reference file automatically.

---

## Repo structure

```
master-instructional-design.skill   ← distributable ZIP bundle (regenerate with ./build.sh)
build.sh                            ← rebuilds the .skill bundle from source
CONTRIBUTING.md                     ← contribution and IP standards
LICENSE                             ← CC BY-NC-ND 4.0

master-instructional-design/
  SKILL.md                          ← core skill: frontmatter, 15 modes, audit framework
  references/                       ← 14 on-demand reference files (loaded per conversation, not all at once)
    academic-courseware.md
    agile-and-design.md
    authoring-tools.md
    coaching-stance.md
    evaluation-planning.md
    facilitation-and-ilt.md
    foundational-texts.md
    generative-ai-for-ld.md
    inclusive-emotional-design.md
    lms-evaluation.md
    lxd-and-atd.md
    modes-deep-dive.md
    project-management.md
    quick-reference.md

.claude/
  settings.json                     ← UserPromptSubmit hook wiring
  hooks/
    reference-router.py             ← keyword router; routes each prompt to most relevant reference file

.github/
  workflows/
    validate.yml                    ← CI: description length, syntax checks, bundle staleness, router smoke test

testing-scripts.md                  ← manual test prompts across all 15 modes
```

---

## Key constraints

- **SKILL.md `description:` field must stay ≤ 1024 characters** — the skill upload validator enforces this hard limit. Run `./build.sh` before committing; it will fail if the limit is exceeded. Current: 851/1024 chars.
- **All reference files need the CC BY-NC-ND 4.0 license footer** — the CI check enforces this.
- **`.skill` bundle must stay current** — run `./build.sh` after any change to SKILL.md or any reference file. The CI `--check` step will fail on stale bundles in PRs.

---

## Development workflow

```bash
# Make changes to SKILL.md or any reference file
# Then:
./build.sh          # validate + rebuild bundle
git add -p          # stage what you changed
git commit          # commit message describes what changed and why
git push -u origin <branch>
```

Branch naming convention: `claude/<short-description>-<id>` (matches existing pattern).

---

## Adding a new reference file

1. Create `master-instructional-design/references/<name>.md`
2. Add a `Load when:` entry in the `For More Depth` section of SKILL.md
3. Add a route pattern in `.claude/hooks/reference-router.py`
4. Update the README table and count
5. Run `./build.sh` to rebuild and validate

---

## CI checks (`.github/workflows/validate.yml`)

| Check | What it validates |
|-------|-------------------|
| settings.json syntax | Valid JSON |
| reference-router.py syntax | Valid Python |
| SKILL.md description length | ≤ 1024 chars |
| License footers | All reference files contain CC BY-NC-ND notice |
| SKILL.md frontmatter fields | `name`, `version`, `license`, `description` all present |
| README count | Matches actual file count in references/ |
| .skill bundle staleness | Bundle matches current source |
| Router smoke test | Storyline prompt → authoring-tools.md |

---

## License

CC BY-NC-ND 4.0 — © 2026 Norman Arosemena, CPTD. See LICENSE.  
Commercial use prohibited without a license. Contact via [LinkedIn](https://www.linkedin.com/in/normanarosemena/).
