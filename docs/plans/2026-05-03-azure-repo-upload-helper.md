# Plan: Azure DevOps repo upload helper for `pyjenkinsapi`

**Date:** 2026-05-03  
**Branch:** `pyjenkinsapi-v0.1.0`  
**Scope:** `pyjenkinsapi` only  
**Related context:** Azure DevOps repo bootstrap / upload automation

---

## Goal

Create a repo-local helper script under `bin/` that can upload the current `pyjenkinsapi` repository to an Azure DevOps Git repository.

The helper should make initial repo publication and later re-syncs repeatable from the command line, without manual Azure DevOps UI setup.

---

## Intended Behavior

- Accept configuration via command-line options and/or environment variables.
- Support an explicit `--auto-detect` mode that infers org/project automatically when `--org` and `--project` are omitted.
- Use Azure DevOps CLI integration to create the target repository when missing.
- Configure a local git remote pointing at the Azure DevOps repository.
- Push the repo content using a clear mode:
  - current branch only,
  - all local branches plus tags, or
  - mirror mode for full ref sync.
- Avoid printing secrets or tokens.
- Prefer idempotent behavior so the helper can be re-run safely.

---

## Constraints

- Use `bin/` for the helper script. Create `bin/` if it does not already exist in the target state.
- Do not duplicate generic shell plumbing that already exists in the vendored `lib-foundation` / `rigor-cli` subtree.
- Keep the upload helper separate from the lint/review runtime path.
- Keep the helper focused on repo upload and remote setup, not general Azure DevOps administration.

---

## Proposed Shape

### Script
- Add a repo-local script with a clear name such as `bin/pyjenkinsapi-azure-upload`.
- Support:
  - organization URL or name
  - project
  - repository name
  - local remote name
  - push mode selection
  - auto-detect mode for org/project inference when org/project are omitted
- Support a `--dry-run` or `--check` mode if practical.
- Prefer an ensure-style flow that creates the Azure repo when missing and reuses it on later runs.

### Azure CLI Integration
- Use `az repos show` to check for the repo and `az repos create` if it is missing.
- Keep authentication external to the script so it can be used in maintenance sessions or CI admin jobs.
- Make sure the helper works even if Azure CLI extension cache state is fresh, without requiring manual cleanup.

### Shared Helpers
- Reuse the vendored `lib-foundation` shell helpers from `tools/rigor-cli/scripts/lib/foundation/scripts/lib/system.sh` rather than reimplementing command checks, warnings, and command execution wrappers.
- If the helper needs additional generic shell functionality later, prefer adding it to `lib-foundation` only when it is broadly reusable.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but implementation will likely touch:

- `bin/` helper script
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`
- possibly `docs/issues/` or `docs/retro/` if the Azure repo model exposes an unexpected constraint

---

## Definition of Done for the Future Implementation

- A repo-local `bin/` helper exists for Azure DevOps repo upload and remote setup.
- The helper can create or reuse the Azure DevOps repository.
- The helper supports configuration via command-line options and/or environment variables.
- The helper supports an explicit `--auto-detect` mode for org/project discovery when org/project are omitted.
- The helper uses shared vendored shell helpers where practical instead of duplicating plumbing.
- The Azure repository can be created and populated without manual Azure DevOps UI editing.
- Memory-bank entries describe the helper and its intended use.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a planning doc only.
- This helper is distinct from the branch-policy helper, the secret rotation helper, and the pipeline wrapper scripts already added under `bin/`.
- The next implementation step should clarify whether the default push mode is current-branch-only or a broader all-branches/tags upload before coding.
