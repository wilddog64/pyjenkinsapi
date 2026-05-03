# Active Context

## Current Status
- Repository memory-bank now includes current-state tracking files to match the current Cline template.
- `rigor-cli` is now vendored under `tools/rigor-cli/` on branch `pyjenkinsapi-v0.1.0` (subtree import at `a6d83d6`).
- Azure pipeline implementation has started: repo-local bootstrap, lint, and review wrappers were added, and `azure-pipelines.yml` now wires them together.
- Azure PR branch-policy helper planning is now queued to automate Azure Repos build validation from `bin/`.
- Azure secret rotation helper planning remains queued as a separate maintenance command, similar in spirit to `bin/rotate-ghcr-pat`.

## Current Focus
- Keep `pyjenkinsapi` behavior stable while preserving the legacy-compatible CLI and module layout.
- Treat `tools/rigor-cli/` as read-only vendored tooling unless the task explicitly refreshes the subtree.
- Next task: implement the Azure PR branch-policy helper plan in `docs/plans/2026-05-03-azure-pr-branch-policy-helper.md` after approval.
- Keep the Azure secret rotation helper plan aligned with the same `bin/` maintenance-command style.
- Use this file for the next task's immediate context, recent decisions, and next steps.

## Notes
- Update this file after significant milestones or when the task direction changes.
- Keep it concise and focused on the current work, not as a full history.
