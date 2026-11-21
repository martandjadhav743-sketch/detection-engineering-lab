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