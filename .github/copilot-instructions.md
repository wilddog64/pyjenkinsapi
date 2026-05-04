# Copilot Instructions for `pyjenkinsapi`

## Role
- Treat this as a compatibility-sensitive Jenkins client and CLI project.
- Prefer repo-specific, actionable guidance over generic style notes.
- When making code changes, think of this as a code + tooling + CI system; changes can cascade across build/review/pipeline.
- When reviewing, use the prompt for the current change set as the primary source of review context.

## CLI Entrypoints (Stable)
The two public CLI entrypoints must remain stable—changing names, flags, or output format is a breaking change:
- `jenkins-cmd` — primary Jenkins view/job inspector (see `jenkinsapi.scripts.jenkins_cli:jenkins`)
- `serverlist` — legacy server list helper (see `jenkinsapi.scripts.serverlist:main`)

## Code Change Priorities
- Preserve backward compatibility, especially `jenkinsapi.core.Jenkins` and existing import paths.
- Treat config-driven Jenkins auth (via `jenkins.ini`) as the default pattern—never hardcode credentials, tokens, org/project names, or Jenkins URLs.
- Use `jenkinsapi.config.core.config_section_map()` to parse config sections; example: `config = config_section_map('lcjenkins')` yields `{'url': '...', 'user': '...', 'password': '...'}`
- Favor minimal, surgical edits over broad rewrites.
- Do not log or print plaintext secrets.
- Preserve legacy Python patterns (e.g., `from __future__ import print_function`) unless explicitly requested.

## Review Priorities
- Preserve backward compatibility and CLI stability as noted above.
- Review behavior changes before style-only suggestions.
- Call out missing tests or docs when behavior changes.

## Build and Validation Pipeline

### Critical Dependency: `bin/`, `tools/rigor-cli/`, and `.github/copilot-instructions.md`

These three components form a tightly-coupled unit used by Azure CI and local development:

**`bin/pyjenkinsapi-lint`** — Runs `tools/rigor-cli/bin/rigor lint` with Python backend (ruff). Hard-coded path at line 36.

**`bin/pyjenkinsapi-review`** — Runs `tools/rigor-cli/bin/rigor review` with repo-specific guidance. Hard-coded path at lines 31, 115. Reads `.github/copilot-instructions.md` and passes it to the review tool. **Deleting the instructions file will break this script.**

**Azure Pipeline** (`azure-pipelines.yml` lines 44–65) — Calls `bin/pyjenkinsapi-lint` and `bin/pyjenkinsapi-review` as CI stages. Requires `.github/copilot-instructions.md` to exist.

**Do not delete or rename:**
- `tools/rigor-cli/` — vendored subtree; do not edit directly unless the task is explicitly a subtree refresh
- `.github/copilot-instructions.md` — required by both `bin/pyjenkinsapi-review` and Azure CI
- The hard-coded paths in `bin/pyjenkinsapi-lint` and `bin/pyjenkinsapi-review`

If you need to change or remove any of these, update all three files together and verify the Azure pipeline still works.

## Repository Boundaries
- Treat `tools/rigor-cli/` as read-only vendored tooling (see **Critical Dependency** above).
- Treat files under `bin/` as repo-local maintenance and pipeline helpers integral to CI (see **Critical Dependency** above).
- Keep Azure helper scripts aligned with their documented prompt/fail-fast behavior.

## What to Flag
- Breaking changes to public APIs, CLI flags, or output formats.
- Config parsing regressions.
- Authentication or credential-handling problems.
- Changes that make existing Jenkins or CI integrations harder to use.
- Missing tests, docs, or memory-bank updates when behavior changes.
- Any place where a new helper or wrapper duplicates functionality that already exists in `tools/rigor-cli/` or shared shell helpers.

## Review Style
- Start with compatibility and correctness risks.
- Keep feedback concise, concrete, and tied to the changed lines.
- Prefer one comment per real issue.
- If something is only a style preference, state it as advisory.

## CI / Prompt Context
- When `rigor review` runs from CI, assume the prompt already describes the diff or the current change set.
- Use `.github/copilot-instructions.md` for stable repo policy only.
- Use the run-specific prompt for task-specific scope and emphasis.
