# Active Context

## Current Status
- `main` is synced and branch protection is re-enabled.
- Current working branch is `pyjenkinsapi-v0.1.3`.
- `rigor-cli` remains vendored under `tools/rigor-cli/` and is treated as read-only tooling.
- Repo-local `ai-*` helpers, the legacy `pyjenkinsapi-review` alias, and GitHub Actions CI are in place.
- Azure helper scripts, plans, and review/docs work remain available for future follow-up.
- A fresh draft PR now exists for `pyjenkinsapi-v0.1.3` at `https://github.com/wilddog64/pyjenkinsapi/pull/3`.
- The `ai-review` CI failure from the stale `PYJENKINSAPI_RIGOR_BIN` override was fixed in commit `4d1c063` and the BATS harness now uses `AI_RIGOR_BIN`.
- Apache 2.0 licensing has now been added at the repo root and surfaced in `setup.py`.

## Current Focus
- Keep the next branch lean and focused on the next queued task.
- Preserve compatibility for the legacy CLI and vendored tooling boundaries.
- Keep the helper naming cleanup aligned with the repo-local `bin/` surface and docs references.
- Keep the stdin-input support aligned with the existing `ai-review` prompt composition and redaction behavior.
- Keep the stdin-help and backend handoff fixes aligned with the wrapper help text, README guidance, and vendored `rigor review` CLI contract.
- Keep the recorded wrapper-contract review feedback aligned with the current `ai-review` stdin and backend behavior.
- Keep the CI failure-on-findings behavior aligned with the existing PR-style review output contract and result marker contract.
- Keep the legacy review entrypoint compatibility alias aligned with `ai-review` behavior and docs.
- Keep the CI review-context size guard aligned with the current diff generation approach.
- Keep the new `pyjenkinsapi-v0.1.3` release branch aligned with the current shipped `main` state.
- Keep branch protection on `main` enabled after the merge and release handoff.
- The current CI failure on `scripts/tests/ai-review.bats` was traced to a stale `PYJENKINSAPI_RIGOR_BIN` test override; the wrapper expects `AI_RIGOR_BIN`, and that mismatch was fixed in `4d1c063`.

## Notes
- Update this file after the next significant milestone or direction change.
