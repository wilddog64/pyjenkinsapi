# Progress

## Status
- `main` is synced and branch protection is re-enabled.
- The current working branch is `pyjenkinsapi-v0.1.3`.
- Vendored `rigor-cli`, repo-local `ai-*` helpers, the legacy `pyjenkinsapi-review` alias, and GitHub Actions CI are stable.
- Azure helper scripts and plans remain queued for the next milestone.
- Draft PR #3 now tracks the `pyjenkinsapi-v0.1.3` release branch.

## Milestones
- `activeContext.md` and `progress.md` are in use for current-state tracking.
- `tools/rigor-cli/` is vendored under the repo.
- Repo-local bootstrap/lint/review wrappers are implemented under `bin/`.
- GitHub Actions CI is split into lint and review jobs.
- Helper naming plan recorded in `docs/plans/2026-05-04-bin-ai-helpers-naming.md`.
- Helper rename implementation has been applied to the repo-local helper scripts and workflow/docs references.
- Stdin-input plan recorded in `docs/plans/2026-05-04-ai-review-stdin-input.md`.
- `ai-review` stdin input is covered by local BATS tests and direct stdin smoke validation.
- Stdin-help bug recorded in `docs/bugs/2026-05-04-ai-review-stdin-help-missing.md` and resolved in `bin/ai-review`.
- Backend-prompt-file leak bug recorded in `docs/bugs/2026-05-04-ai-review-backend-prompt-file-leak.md` and resolved in `bin/ai-review`.
- Wrapper-contract regression review feedback recorded in `docs/bugs/2026-05-04-ai-review-wrapper-contract-regression.md` and resolved in `bin/ai-review`.
- `ai-review` CI failure-on-findings behavior recorded in `docs/plans/2026-05-04-ai-review-fail-on-findings.md` and implemented in `bin/ai-review`.
- Legacy `pyjenkinsapi-review` compatibility alias bug recorded in `docs/bugs/2026-05-04-pyjenkinsapi-review-compatibility-alias-missing.md`.
- Legacy `pyjenkinsapi-review` compatibility alias bug resolved with `bin/pyjenkinsapi-review`.
- CI review-context generation now avoids `--binary` and trims oversized diff payloads before invoking Copilot review.
- CI BATS failure on `ai-review` was traced to a stale `PYJENKINSAPI_RIGOR_BIN` test override; the harness now uses `AI_RIGOR_BIN` and the fix landed in `4d1c063`.
- `pyjenkinsapi-v0.1.3` is the current release branch and is tracked by draft PR #3.
- Apache 2.0 licensing has been added at the repo root and mirrored in `setup.py`.
- The runtime dependency declaration now includes `jenkins-webapi==0.5.3` so `python setup.py install` can pull the package that provides `import jenkins`.

## Next Steps
- Pick up the next scoped task on `pyjenkinsapi-v0.1.3`.
