# Plan: Azure DevOps PR branch-policy helper for `pyjenkinsapi`

**Date:** 2026-05-03  
**Branch:** `pyjenkinsapi-v0.1.0`  
**Scope:** `pyjenkinsapi` only  
**Related context:** Azure DevOps PR validation / build policy

---

## Goal

Create a repo-local helper script under `bin/` that configures Azure DevOps branch policies so PR creation and PR updates automatically trigger the validation pipeline.

The helper should make policy creation and updates repeatable from the command line, without requiring manual Azure DevOps UI changes.

---

## Intended Behavior

- Accept configuration via command-line options and/or environment variables.
- Configure or update an Azure DevOps build validation policy for the target branch.
- Point the policy at the `pyjenkinsapi` Azure pipeline.
- Make PR validation fire automatically when a pull request is created or updated.
- Avoid printing secrets or tokens.
- Prefer idempotent behavior so the helper can be re-run safely.

---

## Constraints

- Use `bin/` for the helper script. Create `bin/` if it does not already exist in the target state.
- Do not duplicate generic shell plumbing that already exists in the vendored `lib-foundation` / `rigor-cli` subtree.
- Keep Azure CLI and branch-policy management separate from the lint/review runtime path.
- Keep the helper focused on PR branch policy setup, not general Azure DevOps administration.

---

## Proposed Shape

### Script
- Add a repo-local script with a clear name such as `bin/pyjenkinsapi-azure-policy`.
- Support:
  - organization URL / name
  - project
  - repository
  - target branch
  - pipeline definition or build definition ID
  - policy display name
- Support a `--dry-run` or `--check` mode if practical.
- Prefer an `ensure`-style flow that creates the policy when missing and updates it when present.

### Azure CLI Integration
- Use `az repos policy build create` / `update` / `list` as needed.
- Keep authentication external to the script so it can be used in maintenance sessions or CI admin jobs.
- Make the PR validation policy compatible with Azure Repos Git build validation.

### Shared Helpers
- Reuse the vendored `lib-foundation` shell helpers from `tools/rigor-cli/scripts/lib/foundation/scripts/lib/system.sh` rather than reimplementing command checks, warnings, and command execution wrappers.
- If the helper needs additional generic shell functionality later, prefer adding it to `lib-foundation` only when it is broadly reusable.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but implementation will likely touch:

- `bin/` helper script
- `azure-pipelines.yml` if the policy script needs pipeline metadata
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`
- possibly `docs/issues/` or `docs/retro/` if the Azure policy model exposes an unexpected constraint

---

## Definition of Done for the Future Implementation

- A repo-local `bin/` helper exists for Azure DevOps PR branch policy setup.
- The helper can create or update the build validation policy for `pyjenkinsapi`.
- The helper supports configuration via command-line options and/or environment variables.
- The helper uses shared vendored shell helpers where practical instead of duplicating plumbing.
- The PR validation policy can be set up without manual Azure DevOps UI editing.
- Memory-bank entries describe the helper and its intended use.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a planning doc only.
- This helper is distinct from the secret rotation helper and from the pipeline wrapper scripts already added under `bin/`.
- The next implementation step should clarify the exact Azure policy fields required by the target organization before coding.
