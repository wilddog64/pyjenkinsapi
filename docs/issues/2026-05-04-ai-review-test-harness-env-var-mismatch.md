# ai-review test harness env var mismatch

## What was tested
- GitHub Actions PR CI for `pyjenkinsapi-v0.1.3`
- `bats scripts/tests/ai-review.bats`

## Actual output
```text
Run set -euo pipefail
1..8
not ok 1 ai-review: redacts forbidden fragments from prompt and prompt-file
# (in test file scripts/tests/ai-review.bats, line 72)
#   `[ "$status" -eq 0 ]' failed
not ok 2 ai-review: redacts forbidden fragments from prompt-file mode
# (in test file scripts/tests/ai-review.bats, line 96)
#   `[ "$status" -eq 0 ]' failed
not ok 3 ai-review: accepts stdin review context
# (in test file scripts/tests/ai-review.bats, line 121)
#   `[ "$status" -eq 0 ]' failed
not ok 4 ai-review: combines stdin and prompt-file context
# (in test file scripts/tests/ai-review.bats, line 158)
#   `[ "$status" -eq 0 ]' failed
not ok 5 ai-review: fail-on-findings returns 1 when marker says findings
# (in test file scripts/tests/ai-review.bats, line 179)
#   `[[ "$output" == *"Findings"* ]]' failed
not ok 6 ai-review: fail-on-findings returns 0 when marker says no-findings
# (in test file scripts/tests/ai-review.bats, line 195)
#   `[ "$status" -eq 0 ]' failed
not ok 7 pyjenkinsapi-review compatibility alias preserves stdin
# (in test file scripts/tests/ai-review.bats, line 219)
#   `[ "$status" -eq 0 ]' failed
not ok 8 pyjenkinsapi-review compatibility alias preserves fail-on-findings
# (in test file scripts/tests/ai-review.bats, line 235)
#   `[[ "$output" == *"Findings"* ]]' failed
Error: Process completed with exit code 1.
```

## Root cause
- The BATS suite was still exporting `PYJENKINSAPI_RIGOR_BIN`.
- `bin/ai-review` reads `AI_RIGOR_BIN`, so the suite was not invoking the stubbed backend.
- As a result, the tests fell through to the vendored `rigor` binary path instead of the local stub.

## Recommended follow-up
- Keep the test harness aligned with the wrapper's current `AI_RIGOR_BIN` contract.
- Add a lightweight regression check if the backend override contract changes again.
