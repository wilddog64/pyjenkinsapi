# Active Context

## Current Status
- Repository memory-bank now includes current-state tracking files to match the current Cline template.
- `rigor-cli` is now vendored under `tools/rigor-cli/` on branch `pyjenkinsapi-v0.1.0` (subtree import at `a6d83d6`).
- Azure pipeline planning for `pyjenkinsapi` is now queued: dependency/bootstrap, lint, and code review stages; a separate Azure secret rotation helper and review prompt plan are now planned; no implementation yet.

## Current Focus
- Keep `pyjenkinsapi` behavior stable while preserving the legacy-compatible CLI and module layout.
- Treat `tools/rigor-cli/` as read-only vendored tooling unless the task explicitly refreshes the subtree.
- Next task: implement the Azure pipeline plan in `docs/plans/2026-05-03-azure-pipeline-lint-review.md` after approval, then follow with the Azure secret rotation helper plan in `docs/plans/2026-05-03-azure-secret-rotation-helper.md` and the review prompt plan in `docs/plans/2026-05-03-azure-review-instructions-and-prompt.md`.
- Use this file for the next task's immediate context, recent decisions, and next steps.

## Notes
- Update this file after significant milestones or when the task direction changes.
- Keep it concise and focused on the current work, not as a full history.
