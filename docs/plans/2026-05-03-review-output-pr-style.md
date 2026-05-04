# Plan: GitHub PR-style review output for `pyjenkinsapi-review`

**Date:** 2026-05-03  
**Branch:** `pyjenkinsapi-v0.1.0`  
**Scope:** `pyjenkinsapi` only  
**Related context:** local `rigor review` wrapper UX

---

## Goal

Make `bin/pyjenkinsapi-review` produce review output that is easier to read like a GitHub PR review:

- combine the user prompt with `--prompt-file` context by referencing the file path instead of replacing one with the other
- ask Copilot for a structured review response with a short summary and findings
- keep the terminal output visible and actionable for local review runs

This is a wrapper UX change, not a change to the vendored `rigor-cli` subtree.

---

## Desired Behavior

- `--prompt` should provide the review instruction or question.
- `--prompt-file` should provide the change context, such as a diff or review notes.
- Both inputs should be combined into one final review prompt when both are provided.
- Large diff files should be referenced by path rather than inlined to keep the review prompt small enough for visible terminal output.
- The wrapper should ask for a PR-style response format, such as:
  - `Summary`
  - `Findings`
  - `Notes` or `Suggestions`
- If there are no findings, the response should say so explicitly instead of returning a blank-looking run.
- The wrapper should remain useful for CI and local runs.

---

## Proposed Shape

### Prompt composition
- Treat `--prompt` as the human instruction.
- Treat `--prompt-file` as context that should be appended or embedded in the final prompt.
- Do not let `--prompt-file` silently override `--prompt`.
- Keep the prompt readable and deterministic so review runs are repeatable.
- Prefer a file-reference prompt for large diffs; inline only when the prompt-file contents are small enough to stay readable.

### Output contract
- Add a stable review-output preamble that asks for a GitHub PR-style summary.
- Prefer concise bullets with file/line references when the backend can infer them.
- Ask for an explicit `No findings` style response when appropriate.

### Wrapper behavior
- Keep the existing `rigor review` backend path intact.
- Preserve support for `--model` and pass-through review arguments.
- Continue warning when `.github/copilot-instructions.md` is missing.

---

## Constraints

- Do not modify `tools/rigor-cli/` for this change.
- Do not add network dependencies or post-process review results into a separate service.
- Keep the wrapper shell-friendly and simple enough to run locally from the terminal.
- Do not turn the wrapper into a full parser for Copilot output.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but implementation will likely touch:

- `bin/pyjenkinsapi-review`
- `.github/copilot-instructions.md` if the prompt contract needs reinforcement
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`
- `memory-bank/change-log.md`

---

## Definition of Done for the Future Implementation

- `bin/pyjenkinsapi-review` combines `--prompt` and `--prompt-file` into one final prompt instead of replacing one with the other.
- The final prompt requests a PR-style review response with a short summary and explicit findings.
- Local review runs produce visible, structured output that is easier to read than an empty success code.
- Large `--prompt-file` inputs are referenced by path to keep the prompt size manageable.
- Memory-bank entries describe the new review-output behavior.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a planning doc only.
- The wrapper should stay lightweight; if we later need richer formatting, that can be added incrementally.
