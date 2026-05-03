# Development Playbook

## Principles for Safe Changes
1. Confirm current behavior in source before editing.
2. Make minimal, targeted edits.
3. Re-scan related call sites for consistency.
4. Validate with the smallest meaningful checks.

## Editing Boundaries
- Do not rename package/module structure without explicit request.
- Preserve `jenkinsapi.core.Jenkins` public interface.
- Preserve CLI group and command naming (`jenkins`, `views`, `jobs`) unless requested.
- Avoid introducing new runtime dependencies unless necessary.

## Configuration & Secrets Handling
- Keep config-driven behavior through `jenkins.ini` and `config_section_map(...)`.
- Do not commit hardcoded credentials/URLs/tokens.
- Do not print plaintext passwords in logs or CLI output.

## Lightweight Validation Checklist
Use when touching relevant files:

1. **Syntax sanity (touched modules)**
   ```bash
   python -m py_compile <touched_file.py>
   ```
2. **CLI smoke test (if CLI code edited)**
   ```bash
   python -m jenkinsapi.scripts.jenkins_cli --help
   ```
3. **Behavior notes**
   - If behavior changes, document old vs. new behavior in PR/commit notes.

## Refactor Pattern
1. Isolate bug or improvement.
2. Patch only required lines.
3. Check related code paths with grep/search.
4. Re-run minimal validation.
