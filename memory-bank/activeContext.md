# Active Context

## Current Status
- Repository memory-bank now includes current-state tracking files to match the current Cline template.
- `rigor-cli` is now vendored under `tools/rigor-cli/` on branch `pyjenkinsapi-v0.1.0` (subtree import at `a6d83d6`).
- Azure pipeline implementation has started: repo-local bootstrap, lint, and review wrappers were added, and `azure-pipelines.yml` now wires them together.
- Azure PR branch-policy helper planning is now queued to automate Azure Repos build validation from `bin/`.
- Azure secret rotation helper planning remains queued as a separate maintenance command, similar in spirit to `bin/rotate-ghcr-pat`.
- Azure CI helper test planning is now queued for the new wrappers, pipeline YAML, and Azure-specific helper scripts.
- Azure repo upload helper is now implemented to publish `pyjenkinsapi` into Azure DevOps Git from `bin/`.
- Azure repo upload helper now supports `--auto-detect` for detection-first org/project lookup and fails fast if org/project still cannot be inferred.
- `.github/copilot-instructions.md` has been rewritten to focus on compatibility, repo boundaries, and CI review behavior.
- `bin/pyjenkinsapi-review` now combines prompt instruction and `--prompt-file` diff context into a PR-style terminal review prompt, referencing large files by path instead of inlining them.

## Current Focus
- Keep `pyjenkinsapi` behavior stable while preserving the legacy-compatible CLI and module layout.
- Treat `tools/rigor-cli/` as read-only vendored tooling unless the task explicitly refreshes the subtree.
- Next task: implement the Azure PR branch-policy helper plan in `docs/plans/2026-05-03-azure-pr-branch-policy-helper.md` after approval.
- Keep the Azure secret rotation helper plan aligned with the same `bin/` maintenance-command style.
- Keep the Azure CI helper test plan aligned with the helper scripts and pipeline wiring.
- Keep the Azure repo upload helper aligned with the same `bin/` maintenance-command style and confirm the branch upload mode before future changes.
- Keep the Azure repo upload helper's detection-first behavior aligned with Azure CLI defaults and existing Azure remotes when values are not provided.
- Keep `.github/copilot-instructions.md` aligned with the repository's compatibility surface and vendored tooling boundaries.
- Keep `bin/pyjenkinsapi-review` aligned with the PR-style review output plan in `docs/plans/2026-05-03-review-output-pr-style.md`, especially the file-reference behavior for large diffs.
- Use this file for the next task's immediate context, recent decisions, and next steps.

## Notes
- Update this file after significant milestones or when the task direction changes.
- Keep it concise and focused on the current work, not as a full history.
