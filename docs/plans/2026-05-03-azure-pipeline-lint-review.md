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

The pipeline should **not** introduce tests, deployment steps, packaging work, or any broader release automation in this phase.

---

## Constraints

- Do not modify `tools/rigor-cli/` directly unless refreshing the subtree intentionally.
- Keep the pipeline focused on lint and review only.
- Preserve the existing `pyjenkinsapi` runtime and CLI behavior.
- Treat `copilot-instructions.md` as repo-local guidance under the project root `.github/`.

---

## Proposed Shape

### Lint
- Use `rigor lint` for Python-oriented lint coverage.
- Keep the backend mapping explicit so the pipeline only runs the checks the repo expects.
- Prefer deterministic failure for lint issues.

### Review
- Use `rigor review` as a separate pipeline step.
- Pass enough diff/context for useful review feedback.
- Treat review output as advisory unless later requirements say otherwise.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but the implementation will likely touch:

- Azure pipeline definition for the repo
- `.github/copilot-instructions.md`
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`

---

## Definition of Done for the Future Implementation

- Azure pipeline runs lint successfully on the repository.
- Azure pipeline runs `rigor review` successfully on the repository.
- The pipeline does not require direct edits to the vendored `tools/rigor-cli/` subtree.
- Memory-bank entries describe the pipeline behavior and current branch state.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a planning doc only.
- No implementation work has started yet.
- The next step is to design the exact Azure workflow and review context once this plan is approved.
