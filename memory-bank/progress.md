# Progress

## Status
- `pyjenkinsapi` is at the post-merge handoff point after PR #1 landed on `main`.
- The current working branch is `pyjenkinsapi-v0.1.1`.
- Vendored `rigor-cli`, GitHub Actions CI, and the review wrapper are all in place.
- Helper naming cleanup is implemented: repo-local helper scripts now use `ai-*` names, while `rotate-secret` stays unprefixed.
- `ai-review` stdin input support is implemented so piped review context can be combined with `--prompt` and `--prompt-file`.
- `ai-review` stdin help text is now fixed and documented in `--help`.
- `ai-review` backend handoff now keeps its temp handling internal and passes only supported arguments to `rigor review`.
- Copilot review feedback for the `ai-review` wrapper contract is documented in `docs/bugs/2026-05-04-ai-review-wrapper-contract-regression.md` and resolved in `bf47e67`.
- CI now has an opt-in failure mode for review findings so `ai-review` can gate pipelines without breaking the default local workflow.
- The legacy `pyjenkinsapi-review` compatibility shim is restored and covered by tests.

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

## Next Steps
- Re-enable branch protection on `main`.
- Pick up the next scoped task on `pyjenkinsapi-v0.1.1`.
