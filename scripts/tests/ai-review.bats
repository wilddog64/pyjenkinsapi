#!/usr/bin/env bats

setup() {
  repo_root="$(cd "$BATS_TEST_DIRNAME/../.." && pwd)"
  export repo_root
}

make_stub_rigor() {
  local stub_dir="$1"
  cat >"$stub_dir/rigor" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

prompt=""
prompt_file=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    review)
      shift
      continue
      ;;
    --prompt)
      prompt="$2"
      shift 2
      continue
      ;;
    --prompt-file)
      prompt_file="$2"
      shift 2
      continue
      ;;
    *)
      shift
      ;;
  esac
done

if [[ -n "${RIGOR_STUB_OUTPUT:-}" ]]; then
  printf '%s\n' "$RIGOR_STUB_OUTPUT"
else
  printf 'PROMPT<<EOF\n%s\nEOF\n' "$prompt"
  if [[ -n "$prompt_file" ]]; then
    printf 'PROMPT_FILE<<EOF\n%s\nEOF\n' "$(cat "$prompt_file")"
  fi
fi
EOF
  chmod +x "$stub_dir/rigor"
}

@test "ai-review: redacts forbidden fragments from prompt and prompt-file" {
  stub_dir="$(mktemp -d)"
  make_stub_rigor "$stub_dir"

  prompt_file="$(mktemp)"
  cat >"$prompt_file" <<'EOF'
diff --git a/example.sh b/example.sh
--- a/example.sh
+++ b/example.sh
@@ -1,2 +1,2 @@
-shell(git push --force)
+shell(git push --force)
EOF

  run env \
    PYJENKINSAPI_RIGOR_BIN="$stub_dir/rigor" \
    PYJENKINSAPI_REVIEW_PROMPT="review shell(git push --force)" \
    PYJENKINSAPI_REVIEW_STREAM=off \
    "$repo_root/bin/ai-review" \
    --prompt-file "$prompt_file"

  [ "$status" -eq 0 ]
  [[ "$output" != *"shell(git push --force)"* ]]
  [[ "$output" == *"[redacted restricted shell fragment]"* ]]
  run cat "$prompt_file"
  [ "$status" -eq 0 ]
  [[ "$output" == *"shell(git push --force)"* ]]
}

@test "ai-review: sanitizes inline prompt-file mode" {
  stub_dir="$(mktemp -d)"
  make_stub_rigor "$stub_dir"

  prompt_file="$(mktemp)"
  cat >"$prompt_file" <<'EOF'
shell(git push --force)
EOF

  run env \
    PYJENKINSAPI_RIGOR_BIN="$stub_dir/rigor" \
    PYJENKINSAPI_REVIEW_INLINE_PROMPT_FILE=1 \
    PYJENKINSAPI_REVIEW_STREAM=off \
    "$repo_root/bin/ai-review" \
    --prompt "review these change" \
    --prompt-file "$prompt_file"

  [ "$status" -eq 0 ]
  [[ "$output" == *"[redacted restricted shell fragment]"* ]]
  [[ "$output" != *"shell(git push --force)"* ]]
}

@test "ai-review: accepts stdin review context" {
  stub_dir="$(mktemp -d)"
  make_stub_rigor "$stub_dir"

  stdin_file="$(mktemp)"
  cat >"$stdin_file" <<'EOF'
diff --git a/example.py b/example.py
--- a/example.py
+++ b/example.py
@@ -1,2 +1,2 @@
-shell(git push --force)
+shell(git push --force)
EOF

  run env \
    PYJENKINSAPI_RIGOR_BIN="$stub_dir/rigor" \
    PYJENKINSAPI_REVIEW_STREAM=off \
    AI_REVIEW_BIN="$repo_root/bin/ai-review" \
    bash -c 'cat "$1" | "$AI_REVIEW_BIN" --prompt "review these change"' _ "$stdin_file"

  [ "$status" -eq 0 ]
  [[ "$output" != *"PROMPT_FILE<<EOF"* ]]
  [[ "$output" == *"Review context from stdin:"* ]]
  [[ "$output" == *"[redacted restricted shell fragment]"* ]]
  [[ "$output" != *"shell(git push --force)"* ]]
}

@test "ai-review: combines stdin and prompt-file context" {
  stub_dir="$(mktemp -d)"
  make_stub_rigor "$stub_dir"

  prompt_file="$(mktemp)"
  cat >"$prompt_file" <<'EOF'
diff --git a/prompt-file.py b/prompt-file.py
--- a/prompt-file.py
+++ b/prompt-file.py
@@ -1 +1 @@
-prompt-file content
+prompt-file content
EOF

  stdin_file="$(mktemp)"
  cat >"$stdin_file" <<'EOF'
diff --git a/stdin.py b/stdin.py
--- a/stdin.py
+++ b/stdin.py
@@ -1 +1 @@
-stdin content
+stdin content
EOF

  run env \
    PYJENKINSAPI_RIGOR_BIN="$stub_dir/rigor" \
    PYJENKINSAPI_REVIEW_STREAM=off \
    AI_REVIEW_BIN="$repo_root/bin/ai-review" \
    bash -c 'cat "$1" | "$AI_REVIEW_BIN" --prompt "review these change" --prompt-file "$2"' _ "$stdin_file" "$prompt_file"

  [ "$status" -eq 0 ]
  [[ "$output" != *"PROMPT_FILE<<EOF"* ]]
  [[ "$output" == *"prompt-file content"* ]]
  [[ "$output" == *"stdin content"* ]]
  [[ "$output" == *"Review context from --prompt-file"* ]]
  [[ "$output" == *"Review context from stdin:"* ]]
}

@test "ai-review: fail-on-findings returns 1 when marker says findings" {
  stub_dir="$(mktemp -d)"
  make_stub_rigor "$stub_dir"

  run env \
    PYJENKINSAPI_RIGOR_BIN="$stub_dir/rigor" \
    PYJENKINSAPI_REVIEW_STREAM=off \
    RIGOR_STUB_OUTPUT=$'Summary\n\nFindings\n- one issue\n\nAI_REVIEW_RESULT: findings' \
    "$repo_root/bin/ai-review" \
    --exit-code \
    --prompt "review these change"

  [ "$status" -eq 1 ]
  [[ "$output" == *"Findings"* ]]
  [[ "$output" == *"AI_REVIEW_RESULT: findings"* ]]
}

@test "ai-review: fail-on-findings returns 0 when marker says no-findings" {
  stub_dir="$(mktemp -d)"
  make_stub_rigor "$stub_dir"

  run env \
    PYJENKINSAPI_RIGOR_BIN="$stub_dir/rigor" \
    PYJENKINSAPI_REVIEW_FAIL_ON_FINDINGS=1 \
    PYJENKINSAPI_REVIEW_STREAM=off \
    RIGOR_STUB_OUTPUT=$'Summary\n\nNo findings\n\nAI_REVIEW_RESULT: no-findings' \
    "$repo_root/bin/ai-review" \
    --prompt "review these change"

  [ "$status" -eq 0 ]
  [[ "$output" == *"No findings"* ]]
  [[ "$output" == *"AI_REVIEW_RESULT: no-findings"* ]]
}

@test "pyjenkinsapi-review compatibility alias preserves stdin" {
  stub_dir="$(mktemp -d)"
  make_stub_rigor "$stub_dir"

  stdin_file="$(mktemp)"
  cat >"$stdin_file" <<'EOF'
diff --git a/legacy.py b/legacy.py
--- a/legacy.py
+++ b/legacy.py
@@ -1 +1 @@
-legacy content
+legacy content
EOF

  run env \
    PYJENKINSAPI_RIGOR_BIN="$stub_dir/rigor" \
    PYJENKINSAPI_REVIEW_STREAM=off \
    bash -c 'cd "$1" && cat "$2" | ./bin/pyjenkinsapi-review --prompt "review these change"' _ "$repo_root" "$stdin_file"

  [ "$status" -eq 0 ]
  [[ "$output" == *"Review context from stdin:"* ]]
  [[ "$output" != *"PROMPT_FILE<<EOF"* ]]
}

@test "pyjenkinsapi-review compatibility alias preserves fail-on-findings" {
  stub_dir="$(mktemp -d)"
  make_stub_rigor "$stub_dir"

  run env \
    PYJENKINSAPI_RIGOR_BIN="$stub_dir/rigor" \
    PYJENKINSAPI_REVIEW_STREAM=off \
    RIGOR_STUB_OUTPUT=$'Summary\n\nFindings\n- one issue\n\nAI_REVIEW_RESULT: findings' \
    bash -c 'cd "$1" && ./bin/pyjenkinsapi-review --exit-code --prompt "review these change"' _ "$repo_root"

  [ "$status" -eq 1 ]
  [[ "$output" == *"Findings"* ]]
  [[ "$output" == *"AI_REVIEW_RESULT: findings"* ]]
}
