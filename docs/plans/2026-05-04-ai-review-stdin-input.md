# Plan: Let `ai-review` accept stdin review context

**Date:** 2026-05-04  
**Branch:** `pyjenkinsapi-v0.1.1`

---

## Goal

Teach `bin/ai-review` to accept review context from standard input when data is piped in, alongside the existing `--prompt` and `--prompt-file` inputs.

This should let local shell usage work naturally:

```bash
git diff main...HEAD | bin/ai-review
```

and still preserve the current prompt composition and redaction behavior.

---

## Desired Behavior

- Keep `--prompt` as the review instruction.
- Keep `--prompt-file` as file-based review context.
- If stdin is not a TTY and contains data, read it as additional review context.
- Combine stdin content with `--prompt` and `--prompt-file` into the final review prompt.
- Continue redacting forbidden shell fragments from all prompt sources before invoking `rigor review`.
- Avoid reading from stdin when it is an interactive terminal.

---

## Constraints

- Do not mutate prompt-file content on disk.
- Preserve the PR-style output contract already built into `ai-review`.
- Keep the wrapper shell-friendly and local-first.
- Do not modify `tools/rigor-cli/`.

---

## Files Expected in the Implementation Phase

- `bin/ai-review`
- `scripts/tests/ai-review.bats`
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`
- `memory-bank/change-log.md`

---

## Definition of Done

- Piped stdin is accepted as review context.
- `--prompt`, `--prompt-file`, and stdin can be combined in one review run.
- Existing redaction tests still pass.
- A new local test covers stdin input behavior.
- Memory-bank entries reflect the new stdin-input support.
- The implementation is committed and pushed on `pyjenkinsapi-v0.1.1`.

---

## Notes

- A plain interactive terminal should not be consumed accidentally.
- stdin should behave like an extra context source, not a replacement for the existing prompt contract.
