# Progress

## Status
- `pyjenkinsapi` is at the post-merge handoff point after PR #1 landed on `main`.
- The current working branch is `pyjenkinsapi-v0.1.1`.
- Vendored `rigor-cli`, GitHub Actions CI, and the review wrapper are all in place.
- Helper naming cleanup is implemented: repo-local helper scripts now use `ai-*` names, while `rotate-secret` stays unprefixed.

## Milestones
- `activeContext.md` and `progress.md` are in use for current-state tracking.
- `tools/rigor-cli/` is vendored under the repo.
- Repo-local bootstrap/lint/review wrappers are implemented under `bin/`.
- GitHub Actions CI is split into lint and review jobs.
- Helper naming plan recorded in `docs/plans/2026-05-04-bin-ai-helpers-naming.md`.
- Helper rename implementation has been applied to the repo-local helper scripts and workflow/docs references.

## Next Steps
- Re-enable branch protection on `main`.
- Pick up the next scoped task on `pyjenkinsapi-v0.1.1`.
