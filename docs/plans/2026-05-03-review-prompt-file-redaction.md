# Plan: Redact forbidden fragments from `pyjenkinsapi-review` prompt-file input

**Date:** 2026-05-03  
**Branch:** `pyjenkinsapi-v0.1.0`  
**Scope:** `pyjenkinsapi` only  
**Related context:** local `rigor review` wrapper prompt hygiene

---

## Goal

Teach `bin/pyjenkinsapi-review` to sanitize prompt-file content before it reaches the vendored `rigor-cli` prompt guard.

The wrapper should keep the current PR-style review UX, but ensure that review diffs containing blocked shell fragments are redacted before Copilot sees them.

---

## Desired Behavior

- `--prompt-file` should still be accepted as review context.
- The wrapper should redact exact forbidden fragments from both:
  - the explicit `--prompt` text, and
  - the `--prompt-file` content.
- Sanitized content should be passed to `rigor review` instead of the raw prompt-file body.
- The original prompt-file on disk must remain unchanged.
- The review flow should still work for large diffs and keep PR-style terminal output visible.
- The wrapper should continue to warn when `.github/copilot-instructions.md` is missing.

---

## Proposed Shape

### Sanitization
- Mirror the vendored `rigor-cli` forbidden fragment list for prompt hygiene.
- Replace exact matches with neutral redaction text that does not itself trip the guard.
- Apply the sanitizer deterministically so the same input produces the same sanitized prompt.

### Prompt-file handling
- Read `--prompt-file` input, sanitize it, and write the result to a temporary file.
- Pass the sanitized temporary file to `rigor review` instead of the original prompt-file path.
- Clean up any temporary file on exit.
- Keep the current large-diff behavior intact, but sanitize before passing review context onward.

### Prompt handling
- Sanitize `--prompt` text before composing the final review prompt.
- Preserve the existing PR-style review preamble and structured output request.
- Keep `--model` and pass-through review arguments working as before.

---

## Constraints

- Do not modify `tools/rigor-cli/` for this change.
- Do not change the vendored prompt guard itself.
- Keep the wrapper shell-only and local to `pyjenkinsapi`.
- Do not mutate the caller’s prompt-file on disk.
- Avoid adding new external runtime dependencies unless the shell implementation truly needs them.

---

## Files Expected in the Implementation Phase

This plan does not modify them yet, but implementation will likely touch:

- `bin/pyjenkinsapi-review`
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`
- `memory-bank/change-log.md`
- `scripts/tests/rigor.bats` or a new repo-local wrapper smoke test file

---

## Definition of Done for the Future Implementation

- `bin/pyjenkinsapi-review` redacts forbidden fragments from prompt text and prompt-file content before invoking `rigor review`.
- The wrapper passes a sanitized temporary file to `rigor review` when `--prompt-file` is used.
- The original prompt-file remains unchanged.
- A prompt-file containing blocked fragments no longer trips the vendored prompt guard.
- A review run still produces visible PR-style output for sanitized diffs.
- Validation includes shellcheck plus a smoke test that exercises redaction behavior.
- Memory-bank entries describe the sanitization behavior.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.0`.

---

## Notes

- This is a wrapper-only hygiene change, not a vendored `rigor-cli` change.
- If the sanitization list ever changes upstream, the wrapper should be updated to match.
