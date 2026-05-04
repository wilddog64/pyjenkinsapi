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
- Renamed repo-local helper entrypoints to `ai-bootstrap`, `ai-lint`, `ai-review`, and `ai-upload`, and updated docs/workflows/tests to match.
- Added a plan to let `ai-review` accept piped stdin as review context alongside `--prompt` and `--prompt-file`.
- Implemented stdin review-context support in `ai-review` and added BATS coverage plus direct smoke validation.
- Added a bug doc for the missing stdin help text in `ai-review` so the wrapper’s piped-input behavior is discoverable.
- Added a bug doc for the backend `--prompt-file` leak so `ai-review` can keep its internal temp file private and only pass supported flags to `rigor review`.
- Fixed `ai-review` help text and backend handoff so piped stdin is documented and the wrapper no longer forwards unsupported backend flags.
- Recorded Copilot review feedback for the `ai-review` wrapper contract in a bug note and tied it to the existing `bf47e67` fix.
- Added a plan for opt-in CI failure-on-findings behavior in `ai-review` so pipelines can gate on review findings without changing the default local exit status.
- Implemented the `ai-review` CI failure-on-findings mode with a result marker contract and BATS coverage.
- Added a bug note for the missing `pyjenkinsapi-review` compatibility alias after the helper rename.
- Restored `bin/pyjenkinsapi-review` as a thin compatibility alias to `bin/ai-review` and covered the legacy path in tests.
- Updated repo guidance and CI review context handling to match the renamed `ai-*` helpers and avoid oversized AI review prompts.

### Why
To provide persistent engineering context for future contributors/agents and reduce repeated repository discovery work.
