# Plan: Azure secret rotation helper for `pyjenkinsapi`

**Date:** 2026-05-03  
**Branch:** `pyjenkinsapi-v0.1.0`  
**Scope:** `pyjenkinsapi` only  
**Related context:** Azure pipeline bootstrap / secret management

---

## Goal

Create a repo-local script with a role similar to `bin/rotate-ghcr-pat`, but for Azure DevOps secret variables or variable groups.

The helper should make secret updates easy for maintainers without requiring manual UI edits. It should feel like a normal maintenance command, not a special one-off admin procedure.

---

## Intended Behavior

- Read a new secret from a safe input path, such as stdin or a prompt.
- Update the chosen Azure DevOps secret target:
  - a pipeline secret variable, or
  - a variable group secret, or
  - another approved Azure secret store if that becomes the selected source of truth.
- Avoid printing the secret value in logs or terminal output.
- Provide a repeatable command for maintainers to rotate the value.

---

## Constraints

- Do not bake the secret into repo files.
- Do not couple the helper to the lint/review pipeline step itself.
- Keep the helper focused on secret rotation, not general Azure DevOps administration.
- Prefer the smallest surface that still makes repeated secret updates easy.

---

## Proposed Shape

### Script
- Add a repo-local `bin/` helper with a name that clearly signals secret rotation, similar in spirit to `bin/rotate-ghcr-pat`.
- Accept a target name and a secret input method.
- Support a dry-run or confirmation mode if practical.

### Azure Integration
- Update the relevant Azure DevOps secret store using a script-friendly API or CLI path.
- Keep auth external to the helper, so the script can run non-interactively in maintenance workflows.
- Prefer command-line options and environment variables over interactive-only flows, so the helper is usable in local admin shells and scripted maintenance sessions.

### Safety
- Ensure no secret value is echoed back to the terminal.
- Fail clearly if the target variable or group cannot be resolved.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but implementation will likely touch:

- `bin/` helper script
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`
- possibly `docs/retro/` or `docs/issues/` if the helper design exposes an unexpected constraint

---

## Definition of Done for the Future Implementation

- A documented repo-local helper exists for Azure secret rotation and is comparable in usability to `bin/rotate-ghcr-pat`.
- The helper can update the intended Azure secret target without manual UI editing.
- The helper does not print secret contents.
- Memory-bank entries describe the helper and its intended use.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a planning doc only.
- The exact Azure target format is intentionally left open until implementation planning clarifies whether the repo should update a variable group, a pipeline variable, or a Key Vault-backed source.
