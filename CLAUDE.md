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
  references/                       ← 29 on-demand reference files (loaded per conversation, not all at once)
    academic-courseware.md
    agile-and-design.md
    authoring-tools.md
    change-management.md
    coaching-stance.md
    corporate-communications.md
    designer-developer-handover.md
    evaluation-architecture.md
    evaluation-planning.md
    facilitation-and-ilt.md
    foundational-texts.md
    generative-ai-for-ld.md
    hard-change.md
    hard-new.md
    inclusive-emotional-design.md
    lms-evaluation.md
    lxd-and-atd.md
    marketing-for-ld.md
    modes-deep-dive.md
    project-management.md
    quick-reference.md
    scope-creep-governance.md
    situational-leadership.md
    sme-governance.md
    soft-change.md
    soft-new.md
    stakeholder-communication.md
    taxonomy-decision-engine.md
    workload-estimation.md

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

---

## gstack

gstack is installed at `.claude/skills/gstack` and provides a full AI-powered development toolkit via slash commands.

### Web browsing

**Always use `/browse` from gstack for all web browsing tasks.** Never use `mcp__claude-in-chrome__*` tools — use gstack's `/browse` instead.

### Available skills

| Skill | Purpose |
|-------|---------|
| `/office-hours` | Product strategy & idea reframing |
| `/plan-ceo-review` | CEO-level scope and priority review |
| `/plan-eng-review` | Engineering architecture review |
| `/plan-design-review` | Design review and critique |
| `/design-consultation` | Build and refine design systems |
| `/design-shotgun` | Generate visual design variants |
| `/design-html` | Generate production-ready HTML |
| `/design-review` | Review designs against standards |
| `/review` | Code review — find production bugs |
| `/ship` | Release engineering and publishing |
| `/land-and-deploy` | Production deployment verification |
| `/canary` | Canary release monitoring |
| `/benchmark` | Performance benchmarking |
| `/browse` | Headless browser — navigate, interact, screenshot, verify |
| `/connect-chrome` | Connect to Chrome DevTools |
| `/qa` | Browser-based QA testing |
| `/qa-only` | QA without code changes |
| `/setup-browser-cookies` | Configure browser authentication |
| `/setup-deploy` | Configure deployment pipeline |
| `/retro` | Team retrospective facilitation |
| `/investigate` | Debugging and root cause analysis |
| `/document-release` | Update documentation on release |
| `/codex` | Cross-model code review |
| `/cso` | Security auditing |
| `/autoplan` | Automated planning |
| `/careful` | Enable careful/conservative mode |
| `/freeze` | Freeze codebase changes |
| `/guard` | Guard against unintended changes |
| `/unfreeze` | Unfreeze codebase |
| `/learn` | Memory management and knowledge capture |
| `/gstack-upgrade` | Upgrade gstack to latest version |

### Troubleshooting

If gstack skills aren't working, rebuild the binary and re-register:

```bash
cd .claude/skills/gstack && ./setup
```

