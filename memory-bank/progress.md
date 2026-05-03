# Progress

## Status
- Memory-bank structure now includes `activeContext.md` and `progress.md` alongside the existing durable docs.
- `rigor-cli` is vendored under `tools/rigor-cli/` on branch `pyjenkinsapi-v0.1.0`.
- Azure pipeline implementation has started with repo-local bootstrap, lint, and review wrappers; the pipeline YAML is still pending.

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
- Repo-local bootstrap/lint/review wrappers added under `bin/`.

## Next Steps
- Add Azure pipeline YAML to call the new wrappers and keep the review prompt contract aligned.
- Keep summaries brief and use linked docs for longer details.
