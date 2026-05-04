# Bug: `ai-review` forwards an unsupported `--prompt-file` flag to the backend

**Date:** 2026-05-04  
**Branch:** `pyjenkinsapi-v0.1.1`

---

## Problem

`bin/ai-review` accepts stdin and `--prompt-file` content, sanitizes them into a temp file, and then forwards that temp file to the vendored `rigor` backend using `--prompt-file`.

That is not supported by the backend path. When the wrapper is used with piped input, the backend fails with:

```text
error: unknown option '--prompt-file'
```

The temp file should stay internal to `ai-review`; the backend only understands `--prompt`.

---

## Actual Behavior

- `ai-review` reads stdin and/or `--prompt-file`.
- `ai-review` writes combined context into a temp file.
- `ai-review` forwards `--prompt-file <tempfile>` to `rigor review`.
- The backend rejects the unsupported option and exits non-zero.

---

## Expected Behavior

- `ai-review` should keep the combined context temp file internal.
- `ai-review` should pass only `--prompt` and supported `rigor review` arguments to the backend.
- Stdin and prompt-file content should still be merged for the wrapper’s internal prompt assembly.

---

## Recommended Fix

- Remove the forwarded `--prompt-file` argument from the backend invocation.
- Keep the combined temp file only as an internal wrapper artifact.
- Ensure the current redaction and PR-style output contract still apply.

---

## Validation Notes

Repro:

```bash
git diff ..main | bin/ai-review
```

Observed failure:

```text
error: unknown option '--prompt-file'
```

---

## Follow-Up

- Patch `bin/ai-review` to stop passing `--prompt-file` to the backend.
- Re-run the stdin smoke test and BATS coverage after the fix.
