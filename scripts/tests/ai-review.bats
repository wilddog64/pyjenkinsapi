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

printf 'PROMPT<<EOF\n%s\nEOF\n' "$prompt"
if [[ -n "$prompt_file" ]]; then
  printf 'PROMPT_FILE<<EOF\n%s\nEOF\n' "$(cat "$prompt_file")"
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
