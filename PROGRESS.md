# Project Progress

## Phase 1: Project foundation — COMPLETE

### Completed

- Created project folder: `C:\Users\marta\Desktop\detection-engineering-lab`
- Created folders: `src`, `data`, `docs`, `rules`, `reports`, `screenshots`, `tests`
- Created Python virtual environment: `.venv`
- Created `README.md`
- Created `PROGRESS.md`
- Created `.gitignore`
- Created `requirements.txt`
- Installed `pandas` and `pytest`
- Verified Python 3.14.7 and pip 26.2.1
- Verified `pandas 3.1.1` can be imported
- Verified `pytest 9.2.0` runs correctly
- Uploaded Phase 1 files to GitHub

## Phase 2: Mock telemetry design — COMPLETE

### Completed

- Created `docs/mock-telemetry-design.md`
- Created `data/mock_windows_security_events.csv`
- Created `src/read_mock_logs.py`
- Created `docs/data-dictionary.md`
- Created `reports/mock-telemetry-baseline.md`
- Added 4 automated tests in `tests/test_mock_logs.py`
- Verified Python can read all 13 mock events
- Verified all 4 tests pass
- Took Phase 2 screenshot: `screenshots/phase2-mock-telemetry-design.png`

### Mock telemetry summary

| Event type | Count |
|---|---:|
| Failed Logon | 7 |
| Successful Logon | 4 |
| Account Locked Out | 1 |
| Special Privileges Assigned | 1 |

### Failed logons by source IP

| Source IP | Failed logons |
|---|---:|
| 203.0.113.45 | 5 |
| 198.51.100.22 | 2 |

### Test results

```text
4 passed
```

## Next phase

Phase 3: Log analysis utilities
# Project Progress

## Phase 1: Project foundation — COMPLETE

### Completed

- Created project folder: `C:\Users\marta\Desktop\detection-engineering-lab`
- Created folders: `src`, `data`, `docs`, `rules`, `reports`, `screenshots`, `tests`
- Created Python virtual environment: `.venv`
- Created `README.md`
- Created `PROGRESS.md`
- Created `.gitignore`
- Created `requirements.txt`
- Installed `pandas` and `pytest`
- Verified Python 3.14.7 and pip 26.2.1
- Verified `pandas 3.1.1` can be imported
- Verified `pytest 9.2.0` runs correctly
- Uploaded Phase 1 files to GitHub

## Phase 2: Mock telemetry design — COMPLETE

### Completed

- Created `docs/mock-telemetry-design.md`
- Created `data/mock_windows_security_events.csv`
- Created `src/read_mock_logs.py`
- Created `docs/data-dictionary.md`
- Created `reports/mock-telemetry-baseline.md`
- Added 4 automated tests in `tests/test_mock_logs.py`
- Verified Python can read all 13 mock events
- Verified all 4 tests pass
- Took Phase 2 screenshot: `screenshots/phase2-mock-telemetry-design.png`
- Uploaded Phase 2 files to GitHub

## Phase 3: Log analysis utilities — COMPLETE

### Completed

- Created `src/log_analysis.py`
- Added functions to load events, count events, group failed logons by source IP, and identify repeated failed logons
- Added 5 automated tests in `tests/test_log_analysis.py`
- Verified all 9 automated tests pass
- Updated `README.md` with analysis and testing instructions
- Took Phase 3 screenshot: `screenshots/phase3-log-analysis-utilities.png`

### Analysis results

| Metric | Result |
|---|---:|
| Total mock events | 13 |
| Failed logons | 7 |
| Successful logons | 4 |
| Account lockouts | 1 |
| Special-privilege assignments | 1 |
| Source IPs with 3 or more failed logons | 1 |

### Test results

```text
9 passed
```

## Phase 4: Sigma rule library — IN PROGRESS


### Completed


- Created Sigma-style rules for repeated failed logons, password spraying, privileged logons, unfamiliar-source successful logons, unknown-workstation logons, and suspicious service installations
- Created `docs/attack-coverage-matrix.csv`
- Added automated tests for Sigma rule structure, IDs, ATT&CK tags, severity, and detection logic
- Added Python detection functions and tests for:
  - Repeated failed logons
  - Password spraying
  - Unfamiliar-source successful logons
  - Unknown-workstation logons
  - Suspicious service installations
- Created mock logs for unknown-workstation logons and suspicious service installations
- Added `pytest.ini` with `pythonpath = .` and `testpaths = tests`
- Reached 49 passing automated tests


### Important scope note


The rules and detection logic developed in Phase 4 were validated against locally created mock telemetry.


This work is useful for learning detection engineering and building a repeatable local validation workflow, but it does not yet satisfy the PRD requirement to test rules against real, publicly available security telemetry.


## Next phase


Phase 5: Real telemetry onboarding and PRD alignment