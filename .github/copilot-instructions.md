# Copilot Instructions for `pyjenkinsapi`

## Review Priorities
- Preserve backward compatibility, especially `jenkinsapi.core.Jenkins`.
- Keep CLI entrypoints and command names stable unless the task explicitly changes them.
- Favor minimal, surgical edits over broad rewrites.
- Treat config-driven Jenkins auth as the default pattern.
- Never hardcode credentials, tokens, or Jenkins URLs.
- Review behavior changes before style-only suggestions.
- Call out missing tests or docs when behavior changes.
- Treat `tools/rigor-cli/` as vendored tooling and do not suggest editing it unless the task is a subtree refresh.

## Review Style
- Prefer actionable, repo-specific comments.
- Flag compatibility risks first.
- Keep feedback concise and focused on correctness, maintainability, and operational safety.

## Azure Review Context
- When `rigor review` is run from Azure Pipelines or another CI system, assume the prompt will describe the current change set.
- Use the prompt to focus the review; keep these instructions stable across runs.
