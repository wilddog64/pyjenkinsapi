# Plan: Let `ai-review` optionally fail CI on review findings

**Branch:** `pyjenkinsapi-v0.1.1`  
**Scope:** `bin/ai-review`, `scripts/tests/ai-review.bats`, README/docs references, memory-bank

---

## Problem

`bin/ai-review` is useful as a human-facing review helper, but CI also needs a way to treat review findings as a failing signal. The default behavior should remain non-fatal for local use, but an explicit opt-in mode should let pipelines fail when review findings are present.

## Proposed Behavior

- Default behavior remains unchanged:
  - successful review execution returns `0`
  - findings are still visible in the output
- Opt-in CI mode adds a failure signal when findings are present:
  - support `--fail-on-findings`
  - support `--exit-code` as a compatibility alias if needed
  - when enabled, the wrapper asks the reviewer to emit a machine-readable result marker
  - if the marker says findings are present, the wrapper exits non-zero after printing the review output
- Backend errors still pass through as actual command failures.

## Result Marker Contract

When CI mode is enabled, the wrapper should append a small prompt instruction that asks the reviewer to end with a marker such as:

- `AI_REVIEW_RESULT: no-findings`
- `AI_REVIEW_RESULT: findings`

The wrapper can then inspect the backend output after execution and decide whether to return `0` or `1`.

## Files to Update

- `bin/ai-review`
- `scripts/tests/ai-review.bats`
- `README.md`
- memory-bank files

## Validation

- `shellcheck -S warning bin/ai-bootstrap bin/ai-lint bin/ai-review bin/ai-upload`
- `bats scripts/tests/ai-review.bats`
- direct smoke test with a stubbed `rigor` backend that emits findings and no-findings markers

## Done When

- Local review behavior is unchanged by default.
- CI opt-in failure-on-findings behavior works and is documented.
- Tests cover both marker outcomes.
- Memory-bank records the new CI-review contract.

