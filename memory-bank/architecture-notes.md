# Architecture Notes

## High-Level Module Responsibilities

### `jenkinsapi/core.py`
- Defines `Jenkins` class, the primary wrapper around Jenkins server access.
- Builds underlying Jenkins client (`jenkins.Jenkins(...)`) and derives view/job accessors.
- Exposes convenience properties such as `jobs` and `views`.

### `jenkinsapi/views.py`
- Holds project-specific view abstractions/containers used by `Jenkins` wrapper.

### `jenkinsapi/config/core.py`
- Provides config-reading utility (`config_section_map(...)`) used to resolve Jenkins credentials and URL from `jenkins.ini`.

### `jenkinsapi/scripts/jenkins_cli.py`
- Click-based CLI command group `jenkins`.
- Handles user-facing options, config resolution, output formatting, and file export side effects.

### `jenkinsapi/scripts/serverlist.py`
- Secondary CLI entrypoint (`serverlist`) for server list workflows.

## Data / Control Flow (CLI Path)
1. User invokes `jenkins-cmd ...`.
2. Click group function resolves config values via `config_section_map(...)`.
3. CLI creates `jenkinsapi.core.Jenkins(...)` and stores it in `ctx.obj`.
4. Subcommands (`views`, `jobs`) use wrapper properties to query/display data.
5. Optional path-based export writes job XML files to disk.

## Design Constraints
- Keep reusable logic outside command handlers where possible.
- Keep command names and option compatibility stable unless explicitly changed.
- Preserve legacy-compatible style where already present.

## Known Improvement Areas (Track Carefully)
- Several modules appear to contain legacy inconsistencies (e.g., property signatures and config variable usage). Any fixes should be **surgical** and validated against CLI behavior to avoid breaking compatibility.
