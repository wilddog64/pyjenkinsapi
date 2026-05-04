# Bug: `ai-review` wrapper must keep stdin support and avoid forwarding unsupported backend flags

**Status:** Resolved in `bf47e67`
**Branch:** `pyjenkinsapi-v0.1.1`
**Files:** `bin/ai-review`, `scripts/tests/ai-review.bats`

---

## Problem

Copilot review feedback flagged two regressions in the review wrapper:

- the wrapper still forwarded `--prompt-file` to the vendored backend, even though the backend only accepts `--prompt`
- the wrapper appeared to drop stdin-based review context, which would break `git diff ... | bin/ai-review` usage

The intended behavior is that `ai-review` may accept stdin and prompt-file input locally, but any temp handling must remain internal to the wrapper and only supported backend flags should reach `rigor review`.

## Expected Behavior

- `bin/ai-review` should keep stdin review context working.
- `bin/ai-review` should keep `--prompt-file` as an input source only, not as a forwarded backend flag.
- The vendored backend should receive only supported `rigor review` arguments.

## Root Cause

The wrapper implementation initially mixed local temp-file handling with backend argument forwarding. That created a contract mismatch with the vendored `rigor review` CLI and risked breaking piped stdin workflows.

## Resolution

`bf47e67` fixes the wrapper so stdin and prompt-file content stay inline in the review prompt and no unsupported `--prompt-file` flag is forwarded to the backend. The local BATS suite now covers both stdin-only and stdin-plus-prompt-file cases.

## Evidence

Direct smoke validation after the fix showed:

- `bin/ai-review` accepted piped stdin input
- the backend saw only `--prompt`
- no `unknown option '--prompt-file'` failure occurred

