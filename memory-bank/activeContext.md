# Active Context

## Current Status
- `pyjenkinsapi` PR #1 is merged into `main` on commit `9bf3ecd`.
- Local branch now moved to `pyjenkinsapi-v0.1.1` from the merged `main` tip.
- `rigor-cli` remains vendored under `tools/rigor-cli/` and is treated as read-only tooling.
- GitHub Actions CI and the review wrapper are now part of the shipped repo state.
- Azure helper scripts, plans, and review/docs work remain available for future follow-up.
- Helper naming cleanup is now implemented: repo-local helper scripts use `ai-*` names, and `rotate-secret` remains unprefixed.
- `ai-review` stdin input support is now implemented so piped review context can be combined with `--prompt` and `--prompt-file`.
- `ai-review` stdin help text is now fixed and documented in `--help`.
- `ai-review` backend handoff is now fixed so the wrapper keeps its temp handling internal and passes only supported arguments to the vendored backend.
- Copilot review feedback for the `ai-review` wrapper contract has been captured in a bug note and resolved in `bf47e67`.
- `ai-review` now has an opt-in CI failure mode so review findings can return non-zero without changing the default local review flow.
- `pyjenkinsapi-review` compatibility alias has been restored so older scripts and habits keep working after the `ai-*` rename.

## Current Focus
- Keep `main` protected again after the merge flow is complete.
- Keep the next branch lean and focused on the next queued task.
- Preserve compatibility for the legacy CLI and vendored tooling boundaries.
- Keep the helper naming cleanup aligned with the repo-local `bin/` surface and docs references.
- Keep the stdin-input support aligned with the existing `ai-review` prompt composition and redaction behavior.
- Keep the stdin-help and backend handoff fixes aligned with the wrapper help text, README guidance, and vendored `rigor review` CLI contract.
- Keep the recorded wrapper-contract review feedback aligned with the current `ai-review` stdin and backend behavior.
- Keep the CI failure-on-findings behavior aligned with the existing PR-style review output contract and result marker contract.
- Keep the legacy review entrypoint compatibility alias aligned with `ai-review` behavior and docs.

## Notes
- Update this file after the next significant milestone or direction change.
