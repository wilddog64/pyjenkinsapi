# Project Overview: `pyjenkinsapi`

## Purpose
`pyjenkinsapi` is a Python package that wraps Jenkins interactions and exposes lightweight CLI tooling for listing views/jobs and exporting job configs.

## Core Domain Concepts
- **Jenkins connection**: URL, user, password used to instantiate Jenkins API client.
- **Views**: named Jenkins views containing jobs.
- **Jobs**: Jenkins jobs, optionally exported as XML config files.
- **Config section**: named section in `jenkins.ini` resolved through `config_section_map(...)`.

## Runtime / Packaging
- Package name: `jenkinsapi`
- Version: `0.1` (from `setup.py`)
- Python dependencies (declared):
  - `Click`
  - `pathlib2`
  - `jenkins-webapi==0.5.3`
  - `click==6.7`
  - `xmltodict==0.11.0`

## Entrypoints
- `jenkins-cmd=jenkinsapi.scripts.jenkins_cli:jenkins`
- `serverlist=jenkinsapi.scripts.serverlist:main`

## Important Backward-Compatibility Surface
- Public class: `jenkinsapi.core.Jenkins`
- CLI command group: `jenkins` in `jenkinsapi.scripts.jenkins_cli`
- Existing module layout should be preserved unless explicitly requested.

## Configuration Behavior
- Credentials and URL are intended to be config-driven via `jenkins.ini` + `config_section_map(...)`.
- CLI options can override config defaults.
- Password values are sensitive and should never be printed/logged in plaintext.
