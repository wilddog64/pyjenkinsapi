# Active Context

## Current Status
- Repository memory-bank now includes current-state tracking files to match the current Cline template.
- `rigor-cli` is now vendored under `tools/rigor-cli/` on branch `pyjenkinsapi-v0.1.0` (subtree import at `a6d83d6`).
- Azure pipeline implementation has started: repo-local bootstrap, lint, and review wrappers were added; the pipeline YAML itself is still pending.

## Current Focus
- Keep `pyjenkinsapi` behavior stable while preserving the legacy-compatible CLI and module layout.
- Treat `tools/rigor-cli/` as read-only vendored tooling unless the task explicitly refreshes the subtree.
- Next task: wire the new wrappers into the Azure pipeline plan in `docs/plans/2026-05-03-azure-pipeline-lint-review.md`, then follow with the secret rotation helper plan and review prompt plan if additional adjustments are needed.
- Use this file for the next task's immediate context, recent decisions, and next steps.

## Notes
- Update this file after significant milestones or when the task direction changes.
- Keep it concise and focused on the current work, not as a full history.
