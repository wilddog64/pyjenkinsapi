# Plan: Copilot review instructions and configurable prompt for Azure review

**Date:** 2026-05-03  
**Branch:** `pyjenkinsapi-v0.1.0`  
**Scope:** `pyjenkinsapi` only  
**Related context:** Azure pipeline review stage

---

## Goal

Define how `rigor review` should work in Azure for this repo by:

1. adding a repo-local `copilot-instructions.md`
2. defining a stable default review prompt template
3. allowing a controlled prompt override for special review runs

This plan focuses on review behavior and prompt design only. It does not implement the pipeline yet.

---

## Desired Review Model

- `copilot-instructions.md` should hold durable repo-specific review guidance.
- The pipeline or wrapper should supply a default prompt that explains the current review goal.
- Special cases may override the prompt, but only in a controlled way.
- The prompt should remain dynamic per run; the instructions file should remain stable.

---

## Proposed `copilot-instructions.md` Content

The file should be concise and repo-specific. It should emphasize:

- backward compatibility for `jenkinsapi.core.Jenkins`
- preserving CLI entrypoints unless explicitly asked to change them
- config-driven credential handling
- avoiding hardcoded secrets or URLs
- minimal, surgical changes
- compatibility and regression risk over style-only comments
- treating vendored `tools/rigor-cli/` as read-only unless a subtree refresh is the task

The file should guide Copilot to raise attention on correctness and compatibility first, then maintainability.

---

## Prompt Design

### Default prompt
- Review the current diff for correctness, compatibility, maintainability, and secret handling.
- Prioritize breaking changes and behavior regressions.
- Call out missing tests or docs when behavior changes.

### Configurable override
- Allow a controlled override for special runs, such as:
  - Azure pipeline changes
  - release-only reviews
  - narrow compatibility checks
- Keep overrides additive or replacement-based, but documented and intentional.
- Do not make the prompt fully free-form without a default template.

---

## Constraints

- Do not replace `copilot-instructions.md` with per-run prompt content.
- Do not make prompt overrides so open-ended that the review behavior becomes inconsistent.
- Keep the review flow separate from dependency/bootstrap and lint stages.
- Do not edit `tools/rigor-cli/` directly for this plan.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but implementation will likely touch:

- `.github/copilot-instructions.md`
- Azure pipeline definition for the repo
- the review prompt source in the repo-local wrapper or pipeline definition
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`

---

## Definition of Done for the Future Implementation

- A repo-local `.github/copilot-instructions.md` exists with review guidance.
- A default review prompt template exists and is documented.
- The prompt can be overridden in a controlled way when needed.
- `rigor review` can consume both the repo instructions and the prompt design.
- Memory-bank entries describe the review policy and prompt model.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a planning doc only.
- The next implementation step should align this plan with the Azure pipeline design and the secret rotation helper plan.
