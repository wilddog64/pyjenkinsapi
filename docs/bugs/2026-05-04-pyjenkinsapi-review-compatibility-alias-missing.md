# Bug: legacy `pyjenkinsapi-review` entrypoint no longer has a compatibility alias

**Status:** Resolved
**Branch:** `pyjenkinsapi-v0.1.1`
**Files:** `bin/pyjenkinsapi-review` (missing), `bin/ai-review`, `README.md`

---

## Problem

The repo-local review wrapper was renamed to `bin/ai-review`, but there is no backward-compatible `bin/pyjenkinsapi-review` alias for older scripts, local habits, or CI jobs that still invoke the original name.

That leaves the rename slightly more disruptive than intended, even though the new wrapper behavior itself is now compatible with stdin and CI failure modes.

## Expected Behavior

- `bin/ai-review` should remain the primary entrypoint.
- `bin/pyjenkinsapi-review` should remain available as a thin compatibility shim.
- The alias should preserve stdin review context and opt-in CI failure mode by delegating to `bin/ai-review` unchanged.

## Why This Matters

The review comments specifically called out a missing compatibility path. Without an alias, the rename forces every caller to switch at once, which is avoidable friction for a repo-local helper.

## Resolution

`bin/pyjenkinsapi-review` now exists as a thin wrapper around `bin/ai-review`, and the local test suite exercises the compatibility alias with stdin and CI failure mode behavior.
