# Retrospective — feat/rigor-cli-ai-helpers

**Date:** 2026-05-08
**Milestone:** Replace standalone ai-* scripts with rigor-cli symlinks
**PR:** #5 — merged to main (`65621642`)
**Participants:** Claude, Gemini, Copilot

## What Went Well
- Symlink refactor clean — three files replaced, .rigor/review-prompt added
- CI correctly updated to skip shellcheck/BATS on symlinks (pending subtree pull)
- Copilot dependency ordering concern acknowledged and thread resolved

## What Went Wrong
- Older Codex PR #2 (pyjenkinsapi-v0.1.1) open with merge conflicts — blocked PR creation; closed as superseded

## Process Rules Added
None this milestone.

## Decisions Made
- Symlinks point to ../tools/rigor-cli/bin/ — subtree pull required after rigor-cli v0.1.5 merges
- .rigor/review-prompt contains pyjenkinsapi-specific review prompt

## Theme
Short refactor PR replacing pyjenkinsapi standalone ai-* scripts with symlinks to canonical rigor-cli implementations. Merge order dependency respected: rigor-cli v0.1.5 first, then subtree pull activates symlinks.
