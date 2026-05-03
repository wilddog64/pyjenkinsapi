# Progress

## Status
- Memory-bank structure now includes `activeContext.md` and `progress.md` alongside the existing durable docs.
- `rigor-cli` is vendored under `tools/rigor-cli/` on branch `pyjenkinsapi-v0.1.0`.
- Azure pipeline implementation has started with repo-local bootstrap, lint, and review wrappers plus `azure-pipelines.yml`.
- Azure PR branch-policy helper planning is queued for Azure DevOps PR validation automation.
- Azure secret rotation helper planning remains queued as a `bin/` maintenance command.
- Azure CI helper test planning is queued for the new wrappers and Azure-specific helper scripts.
- Azure repo upload helper is implemented for publishing `pyjenkinsapi` into Azure DevOps Git from `bin/`.

## Milestones
- Project overview documented in `memory-bank/project-overview.md`.
- Architecture notes documented in `memory-bank/architecture-notes.md`.
- Development workflow documented in `memory-bank/development-playbook.md`.
- Change history captured in `memory-bank/change-log.md`.
- Vendored tooling imported under `tools/rigor-cli/`.
- Azure pipeline plan recorded in `docs/plans/2026-05-03-azure-pipeline-lint-review.md`.
- Dependency/bootstrap stage recorded as part of the Azure pipeline plan.
- Azure secret rotation helper plan recorded in `docs/plans/2026-05-03-azure-secret-rotation-helper.md`.
- Azure review instructions/prompt plan recorded in `docs/plans/2026-05-03-azure-review-instructions-and-prompt.md`.
- Azure PR branch-policy helper plan recorded in `docs/plans/2026-05-03-azure-pr-branch-policy-helper.md`.
- Azure CI helper test plan recorded in `docs/plans/2026-05-03-azure-ci-helper-tests.md`.
- Azure repo upload helper plan recorded in `docs/plans/2026-05-03-azure-repo-upload-helper.md`; helper now added under `bin/`.
- Repo-local bootstrap/lint/review wrappers added under `bin/`.
- Azure pipeline YAML added at `azure-pipelines.yml`.
- The Azure secret rotation helper is intended to mirror the usability of `bin/rotate-ghcr-pat`.

## Next Steps
- Await approval to implement the Azure PR branch-policy helper plan, then keep the pipeline/review helpers aligned as needed.
- Await approval to implement the Azure CI helper tests plan once the Azure helper scripts are in their final shape.
- Revisit the Azure repo upload helper after the first Azure DevOps import to confirm whether all-branches/tags or current-branch mode should be the default.
- Keep summaries brief and use linked docs for longer details.
