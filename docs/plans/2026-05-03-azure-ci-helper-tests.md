# Plan: Tests for Azure CI helpers in `pyjenkinsapi`

**Date:** 2026-05-03  
**Branch:** `pyjenkinsapi-v0.1.0`  
**Scope:** `pyjenkinsapi` only  
**Related context:** Azure pipeline, branch policy, secret rotation, and review helper scripts

---

## Goal

Add test coverage for the new Azure automation helpers so the repo can validate:

1. repo-local bootstrap/lint/review wrappers
2. Azure pipeline YAML structure
3. Azure PR branch-policy helper behavior
4. Azure secret rotation helper behavior
5. Azure repo upload helper behavior

The tests should stay lightweight and avoid real Azure DevOps or Copilot side effects.

---

## What to Test

### Repo-local wrappers
- `bin/pyjenkinsapi-bootstrap`
  - help/usage output
  - missing backend handling
  - `--install` path with a stubbed installer
- `bin/pyjenkinsapi-lint`
  - default backend mapping
  - environment-variable overrides
  - argument pass-through to `rigor lint`
- `bin/pyjenkinsapi-review`
  - default prompt selection
  - `--prompt`
  - `--prompt-file`
  - `--model`
  - warning path for missing `.github/copilot-instructions.md`
- `bin/pyjenkinsapi-azure-upload`
  - option parsing and environment-variable fallback
  - interactive prompt for missing org/project
  - repo create-or-reuse behavior
  - remote URL update and push mode dispatch

### Azure pipeline YAML
- Validate the pipeline file parses cleanly.
- Confirm the expected stages and job names exist.
- Confirm the pipeline calls the new helper scripts in the intended order.

### Azure PR branch-policy helper
- Verify option parsing and environment-variable fallback.
- Mock `az repos policy build ...` calls to confirm the helper can create or update the policy.
- Verify the helper can be re-run safely without duplicating intent.
- Verify dry-run or check mode if implemented.

### Azure secret rotation helper
- Verify option parsing and environment-variable fallback.
- Verify secret input can come from stdin or a prompt without being echoed.
- Mock Azure CLI/API calls to verify the helper updates the intended target.
- Verify the secret value is not written to stdout/stderr.

### Azure repo upload helper
- Verify option parsing and environment-variable fallback.
- Verify `--auto-detect` prefers existing Azure remote metadata and Azure CLI defaults before prompting.
- Verify interactive prompting fills in missing org/project values when stdin is a TTY.
- Verify non-interactive execution fails fast when org/project cannot be determined.
- Mock `az repos show` and `az repos create` calls to confirm the helper can create or reuse the repo.
- Verify the helper updates the local remote and dispatches the expected push mode.

---

## Constraints

- Do not use real Azure DevOps credentials in tests.
- Do not hit live Azure DevOps or Copilot services in unit tests.
- Keep the tests shell-friendly and easy to run locally.
- Prefer small stubs or fake executables over network calls.
- Do not expand the test scope into the vendored `tools/rigor-cli/` subtree.

---

## Proposed Test Shape

### Shell tests
- Add BATS coverage for the new `bin/` helper scripts.
- Use stub executables on `PATH` to verify command dispatch and arguments.
- Use temp files for prompt-file and secret-input scenarios.

### YAML validation
- Parse `azure-pipelines.yml` in a lightweight syntax test.
- Assert the stage/job names and script entrypoints match the plan.

### Command stubs
- Stub `az` for branch-policy and secret-rotation helper tests.
- Stub `copilot` or `rigor` only if needed for wrapper smoke tests.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but implementation will likely touch:

- `scripts/tests/` or a new BATS suite for Azure helpers
- `azure-pipelines.yml`
- `bin/pyjenkinsapi-bootstrap`
- `bin/pyjenkinsapi-lint`
- `bin/pyjenkinsapi-review`
- `bin/pyjenkinsapi-azure-policy` or the future branch-policy helper script
- `bin/pyjenkinsapi-azure-secret-rotate` or the future secret rotation helper script
- `bin/pyjenkinsapi-azure-upload`
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`

---

## Definition of Done for the Future Implementation

- The new Azure helper scripts have local test coverage.
- The Azure pipeline YAML is validated by a lightweight syntax or structure test.
- Tests use stubs/mocks instead of live Azure or Copilot calls.
- The test scope covers the repo-local wrappers and the Azure-specific helper behavior, including upload helper interactive prompting and non-interactive failure.
- Memory-bank entries describe the test plan and current branch state.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a planning doc only.
- The next implementation step should decide whether the helper tests live in a dedicated Azure-focused BATS file or are split by script area.
