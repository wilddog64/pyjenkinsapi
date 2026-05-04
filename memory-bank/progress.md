# Progress

## Status
- `main` is synced and branch protection is re-enabled.
- Current working branch is `pyjenkinsapi-v0.1.2`.
- Vendored `rigor-cli`, repo-local `ai-*` helpers, the legacy `pyjenkinsapi-review` alias, and GitHub Actions CI are stable.
- Azure helper scripts and plans remain queued for the next milestone.

## Milestones
- Project overview documented in `memory-bank/project-overview.md`.
- Architecture notes documented in `memory-bank/architecture-notes.md`.
- Development workflow documented in `memory-bank/development-playbook.md`.
- Change history captured in `memory-bank/change-log.md`.
- Vendored tooling imported under `tools/rigor-cli/`.
- Azure helper plans remain queued for follow-up.
- `ai-review` stdin input, prompt-file redaction, and fail-on-findings behavior are covered by local tests.
- The legacy `pyjenkinsapi-review` alias is preserved and tested.
- GitHub Actions CI remains split into lint and review jobs.
- Repo-local `bin/ai-*` helpers are implemented.

## Next Steps
- Implement the Azure PR branch-policy helper when ready.
