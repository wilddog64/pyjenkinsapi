# Plan: Rename repo-local helper scripts to `ai-*`

**Date:** 2026-05-04  
**Branch:** `pyjenkinsapi-v0.1.1`

---

## Goal

Normalize the repo-local helper names in `bin/` so they read cleanly in a single-repo context.

Current intent:
- `bin/ai-bootstrap`
- `bin/ai-lint`
- `bin/ai-review`
- `bin/ai-upload`
- `bin/rotate-secret`

This replaces the verbose `pyjenkinsapi-*` prefix for AI/review automation while keeping the standalone secret rotation helper unprefixed.

---

## Scope

Update all repo references that currently point at:
- `bin/pyjenkinsapi-bootstrap`
- `bin/pyjenkinsapi-lint`
- `bin/pyjenkinsapi-review`
- `bin/pyjenkinsapi-azure-upload`

Keep `bin/rotate-secret` as the only unprefixed maintenance command in this group.

---

## DoD

- Helper scripts renamed consistently in `bin/`
- Workflow and docs references updated
- Memory-bank entries updated to reflect the final helper names
- Validation passes on renamed entrypoints

---

## Notes

- This is a naming cleanup only.
- It should not change helper behavior.
- Any follow-up cleanup for CI docs or memory-bank phrasing should stay aligned with the renamed commands.
