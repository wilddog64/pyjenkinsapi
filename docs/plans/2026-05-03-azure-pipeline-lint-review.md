# Plan: Azure Pipeline for lint and code review

**Date:** 2026-05-03  
**Branch:** `pyjenkinsapi-v0.1.0`  
**Scope:** `pyjenkinsapi` only  
**Related tooling:** `tools/rigor-cli/`

---

## Goal

Add an Azure DevOps pipeline that uses the vendored `rigor-cli` subtree to run:

1. lint checks
2. AI-assisted code review

As part of the pipeline design, add a small wrapper/bootstrap layer to ensure the selected lint backend is available before `rigor lint` runs. Keep that wrapper separate from `rigor-cli` itself.

The pipeline should **not** introduce tests, deployment steps, packaging work, or any broader release automation in this phase.

---

## Constraints

- Do not modify `tools/rigor-cli/` directly unless refreshing the subtree intentionally.
- Keep the pipeline focused on lint and review only.
- Preserve the existing `pyjenkinsapi` runtime and CLI behavior.
- Treat `copilot-instructions.md` as repo-local guidance under the project root `.github/`.
- Keep backend installation policy out of `rigor-cli` unless a future requirement explicitly moves it there.

---

## Proposed Shape

### Lint
- Use `rigor lint` for Python-oriented lint coverage.
- Keep the backend mapping explicit so the pipeline only runs the checks the repo expects.
- Prefer deterministic failure for lint issues.
- Introduce a thin bootstrap wrapper that:
  - verifies the backend command exists
  - installs it when missing, if the pipeline/environment supports that
  - exports the final `RIGOR_LINT_BACKENDS` mapping before invoking `rigor lint`

### Shared helpers
- If the install/existence logic becomes useful across repos, factor the command-checking and normalization primitives into `lib-foundation/scripts/system.sh`.
- Keep `lib-foundation` limited to reusable shell plumbing, not repo-specific package manager policy.

### Review
- Use `rigor review` as a separate pipeline step.
- Pass enough diff/context for useful review feedback.
- Treat review output as advisory unless later requirements say otherwise.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but the implementation will likely touch:

- Azure pipeline definition for the repo
- one repo-local wrapper/bootstrap script or pipeline step for lint backend setup
- `.github/copilot-instructions.md`
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`

---

## Definition of Done for the Future Implementation

- Azure pipeline runs lint successfully on the repository.
- Azure pipeline runs `rigor review` successfully on the repository.
- The pipeline does not require direct edits to the vendored `tools/rigor-cli/` subtree.
- The pipeline or wrapper ensures lint backends are available before `rigor lint` executes.
- If shared helpers are added, they live in `lib-foundation/scripts/system.sh` only as generic shell primitives.
- Memory-bank entries describe the pipeline behavior and current branch state.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a planning doc only.
- No implementation work has started yet.
- The next step is to design the exact Azure workflow and review context once this plan is approved.
