# Bug: `ai-review` accepts stdin but does not document it in `--help`

**Date:** 2026-05-04  
**Branch:** `pyjenkinsapi-v0.1.1`

---

## Problem

`bin/ai-review` accepts review context from piped stdin, but the usage/help text does not mention that behavior. Users can discover the feature only by reading the script or by trial and error.

That makes the interface misleading because the wrapper now supports:

```bash
git diff main...HEAD | bin/ai-review
```

but the help text still only lists `--prompt`, `--prompt-file`, and `--model`.

---

## Actual Behavior

- `ai-review` reads stdin when input is piped in.
- `ai-review --help` does not mention stdin support.
- The README mentions stdin support, but the command-line help is the primary discoverability surface for the wrapper.

---

## Expected Behavior

- `ai-review --help` should explain that piped stdin is accepted as review context.
- The usage text should show stdin as an input source alongside `--prompt` and `--prompt-file`.
- The help text should briefly show an example invocation.

---

## Recommended Fix

- Update the `Usage:` line to mention stdin support.
- Add a short help note that stdin is accepted when piped in.
- Add an example like `git diff main...HEAD | bin/ai-review`.

---

## Validation Notes

To confirm the gap:

```bash
bin/ai-review --help
```

The output currently omits stdin usage guidance.

---

## Follow-Up

- Update `bin/ai-review` help text.
- Adjust README wording if needed so the CLI help and docs stay aligned.
