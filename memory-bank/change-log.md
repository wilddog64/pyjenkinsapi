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
- Added Azure repo upload helper planning docs and a repo-local upload helper to publish `pyjenkinsapi` into Azure DevOps Git from `bin/`.
- Added Azure CI helper test coverage notes for the repo upload helper's prompt-on-missing behavior.
- Added explicit `--auto-detect` planning notes for the Azure repo upload helper's detection-first org/project lookup and fail-fast behavior when values cannot be inferred.
- Rewrote `.github/copilot-instructions.md` to emphasize compatibility, repo boundaries, and CI review behavior.
- Added a plan for PR-style terminal review output so `bin/pyjenkinsapi-review` can combine prompt instruction and diff context.
- Implemented PR-style prompt composition in `bin/pyjenkinsapi-review` so `--prompt` and `--prompt-file` are combined instead of overriding each other.
- Added a plan to redact forbidden shell fragments from `bin/pyjenkinsapi-review` prompt-file input before invoking `rigor review`.
- Implemented prompt-file redaction in `bin/pyjenkinsapi-review` so forbidden shell fragments are sanitized before review and covered by a local BATS smoke suite.
- Added a top-level `README.md` in a k3d-manager-style layout tailored to pyjenkinsapi’s Jenkins CLI, vendored tooling, and helper scripts.
- Added `.github/workflows/ci.yml` and split it into lint and optional review jobs for pull requests to `main`.
- Addressed Copilot PR review feedback by pinning the Copilot CLI install version in the workflow and adding `apt-get update` before shellcheck installation in the vendored workflow.
- Added a naming plan to simplify repo-local helpers from `pyjenkinsapi-*` to `ai-*`, keeping `rotate-secret` unprefixed.

### Why
To provide persistent engineering context for future contributors/agents and reduce repeated repository discovery work.
