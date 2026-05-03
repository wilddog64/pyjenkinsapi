# Memory Bank Change Log

## 2026-05-03

### Added
- Root `.clinerules` with project-specific coding, compatibility, and validation guidance.
- `memory-bank/README.md` explaining purpose and update triggers.
- `memory-bank/activeContext.md` for current work focus and next steps.
- `memory-bank/progress.md` for status, milestones, and known issues.
- `memory-bank/project-overview.md` with domain, entrypoints, dependencies, and compatibility surface.
- `memory-bank/architecture-notes.md` with module responsibilities and CLI flow.
- `memory-bank/development-playbook.md` with safe-edit workflow and lightweight validation.

### Updated
- Imported `rigor-cli` as a vendored subtree under `tools/rigor-cli/` on branch `pyjenkinsapi-v0.1.0`.
- Added Azure planning docs for lint/review pipeline structure, secret rotation helper, and Copilot review instructions/prompt behavior.
- Added repo-local `bin/pyjenkinsapi-bootstrap`, `bin/pyjenkinsapi-lint`, `bin/pyjenkinsapi-review`, and `.github/copilot-instructions.md` as the first implementation slice for Azure review/lint automation.
- Added `azure-pipelines.yml` wiring the dependency/bootstrap, lint, and review wrappers together.
- Added Azure PR branch-policy helper planning docs for automating Azure Repos PR validation from `bin/`.
- Added Azure CI helper test planning docs for the repo-local wrappers, Azure pipeline YAML, and Azure-specific helper scripts.

### Why
To provide persistent engineering context for future contributors/agents and reduce repeated repository discovery work.
