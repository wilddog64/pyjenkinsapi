# Copilot Instructions for `pyjenkinsapi`

## Role
- Review this repository as a compatibility-sensitive Jenkins client and CLI project.
- Prefer repo-specific, actionable review comments over generic style notes.
- Use the prompt for the current change set as the primary source of review context.

## Review Priorities
- Preserve backward compatibility, especially `jenkinsapi.core.Jenkins` and existing import paths.
- Keep CLI entrypoints, command names, and flag meanings stable unless the task explicitly changes them.
- Favor minimal, surgical edits over broad rewrites.
- Treat config-driven Jenkins auth as the default pattern.
- Never hardcode credentials, tokens, org/project names, or Jenkins URLs.
- Review behavior changes before style-only suggestions.
- Call out missing tests or docs when behavior changes.

## Repository Boundaries
- Treat `tools/rigor-cli/` as vendored tooling.
- Do not suggest editing `tools/rigor-cli/` unless the task is explicitly a subtree refresh.
- Treat files under `bin/` as repo-local maintenance and pipeline helpers unless the task says otherwise.
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
