# Progress

## Status
- `pyjenkinsapi` is at the post-merge handoff point after PR #1 landed on `main`.
- The current working branch is `pyjenkinsapi-v0.1.1`.
- Vendored `rigor-cli`, GitHub Actions CI, and the review wrapper are all in place.
- Helper naming cleanup is implemented: repo-local helper scripts now use `ai-*` names, while `rotate-secret` stays unprefixed.
- `ai-review` stdin input support is implemented so piped review context can be combined with `--prompt` and `--prompt-file`.
- `ai-review` stdin help text is missing and tracked as a bug doc so the wrapper can explain its piped-input behavior.
- `ai-review` backend handoff is broken when stdin or prompt-file context is present because the wrapper forwards an unsupported `--prompt-file` flag to `rigor review`.

## Milestones
- `activeContext.md` and `progress.md` are in use for current-state tracking.
- `tools/rigor-cli/` is vendored under the repo.
- Repo-local bootstrap/lint/review wrappers are implemented under `bin/`.
- GitHub Actions CI is split into lint and review jobs.
- Helper naming plan recorded in `docs/plans/2026-05-04-bin-ai-helpers-naming.md`.
- Helper rename implementation has been applied to the repo-local helper scripts and workflow/docs references.
- Stdin-input plan recorded in `docs/plans/2026-05-04-ai-review-stdin-input.md`.
- `ai-review` stdin input is covered by local BATS tests and direct stdin smoke validation.
- Stdin-help bug recorded in `docs/bugs/2026-05-04-ai-review-stdin-help-missing.md`.
- Backend-prompt-file leak bug recorded in `docs/bugs/2026-05-04-ai-review-backend-prompt-file-leak.md`.

## Next Steps
- Re-enable branch protection on `main`.
- Pick up the next scoped task on `pyjenkinsapi-v0.1.1`.
