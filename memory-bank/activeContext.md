# Active Context

## Current Status
- `pyjenkinsapi` PR #1 is merged into `main` on commit `9bf3ecd`.
- Local branch now moved to `pyjenkinsapi-v0.1.1` from the merged `main` tip.
- `rigor-cli` remains vendored under `tools/rigor-cli/` and is treated as read-only tooling.
- GitHub Actions CI and the review wrapper are now part of the shipped repo state.
- Azure helper scripts, plans, and review/docs work remain available for future follow-up.
- Helper naming cleanup is now implemented: repo-local helper scripts use `ai-*` names, and `rotate-secret` remains unprefixed.
- `ai-review` stdin input support is now implemented so piped review context can be combined with `--prompt` and `--prompt-file`.
- `ai-review` stdin help text is now a queued bug fix because the wrapper accepts piped input but does not explain it in `--help`.
- `ai-review` backend handoff is now blocked on a bug fix because the wrapper currently forwards an unsupported `--prompt-file` flag to the vendored backend.

## Current Focus
- Keep `main` protected again after the merge flow is complete.
- Keep the next branch lean and focused on the next queued task.
- Preserve compatibility for the legacy CLI and vendored tooling boundaries.
- Keep the helper naming cleanup aligned with the repo-local `bin/` surface and docs references.
- Keep the stdin-input support aligned with the existing `ai-review` prompt composition and redaction behavior.
- Keep the stdin-help bug fix aligned with the wrapper help text and README guidance.
- Keep the backend handoff fix aligned with the vendored `rigor review` CLI contract so the temp file remains internal to `ai-review`.

## Notes
- Update this file after the next significant milestone or direction change.
