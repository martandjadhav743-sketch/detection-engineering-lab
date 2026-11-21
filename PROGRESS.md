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

## Phase 4: Sigma rule library — COMPLETE

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

### Real-telemetry onboarding

- Downloaded the EVTX-ATTACK-SAMPLES repository
- Inspected real EVTX telemetry for Security log clearing
- Validated the Security log-clearing rule against real telemetry
- Created `reports/security-log-clearing-real-telemetry-validation.md`
- Confirmed the sample contains a real Event ID `1102` Security log-clearing event
- Updated the password-spraying rule to use real Kerberos pre-authentication failure evidence from Event ID `4768`
- Reached 54 passing automated tests

### Real-telemetry validation

| Detection | Real telemetry sample | Evidence | Result |
|---|---|---|---|
| Security log clearing | `data/raw/kerberos_pwd_spray_4771.evtx` | Event ID `1102` | Confirmed |
| Password spraying | `data/raw/kerberos_pwd_spray_4771.evtx` | Event ID `4768` Kerberos pre-authentication failures | Confirmed |

### Test results

```text
54 passed
```

## Next phase

## Phase 5: Real-telemetry detection expansion — IN PROGRESS


### Completed


- Created `src/validate_kerberos_preauth_failure.py`
- Validated Kerberos pre-authentication failures using real EVTX telemetry
- Confirmed 2 Event ID `4771` events from source IP `172.16.66.1`
- Confirmed targeted accounts `Administrator` and `backdoor`
- Confirmed both events use Kerberos status `0x00000018`
- Created `reports/kerberos-preauth-failure-real-telemetry-validation.md`
- Created `rules/kerberos_preauth_failure_from_single_source.yml`
- Created `tests/test_kerberos_preauth_failure_rule.py`
- Added 3 automated tests for the new Sigma-style rule
- Updated `docs/attack-coverage-matrix.csv` with the new supporting rule ID
- Reached 64 passing automated tests
   

### Real-telemetry validation


| Detection | Real telemetry sample | Evidence | Result |
|---|---|---|---|
| Kerberos pre-authentication failures | `data/raw/kerberos_pwd_spray_4771.evtx` | 2 Event ID `4771` events from `172.16.66.1` | Confirmed |
| JScript ZIP creation and credential manager use | `data/raw/sysmon_zipexec.evtx` | Sysmon Event IDs `1` and `11`; `cscript.exe`, `lync.zip`, and `cmdkey.exe` ZipFolder use | Confirmed |

### JScript ZIP creation and credential manager use

- Downloaded `sysmon_zipexec.evtx` from the EVTX-ATTACK-SAMPLES repository
- Inspected real Sysmon telemetry and identified Event IDs `1` and `11`
- Confirmed `cscript.exe` executed JScript using the `//e:jscript` argument
- Confirmed `cscript.exe` created `lync.zip` in the user Temp directory
- Confirmed `cmdkey.exe` used the `Microsoft_Windows_Shell_ZipFolder` protocol
- Created `rules/suspicious_jscript_zip_creation_cmdkey.yml`
- Created `src/validate_jscript_zip_creation.py`
- Validated all three expected telemetry conditions against the real EVTX sample
- Added 7 automated tests in `tests/test_jscript_zip_creation_rule.py`
- Updated `docs/attack-coverage-matrix.csv` with:
  - `T1059.007` JavaScript/JScript
  - `T1105` Ingress Tool Transfer
- Created `reports/jscript-zip-creation-real-telemetry-validation.md`
- Created `reports/threat-hunt-kerberos-password-spray.md`
- Completed the first required threat hunt using validated Kerberos password-spray telemetry
- Created `reports/threat-hunt-jscript-zip-creation.md`
- Completed the second required threat hunt using validated JScript ZIP staging telemetry
- Completed the PRD requirement for two threat hunts
- Created `reports/incident-case-kerberos-password-spray.md`
- Completed the first required incident case report using validated Kerberos password-spray telemetry
- Created `reports/incident-case-jscript-zip-creation.md`
- Completed the second required incident case report using validated JScript ZIP staging telemetry
- Completed the PRD requirement for two incident case reports
- Created `reports/ir-playbook-kerberos-password-spray.md`
- Completed the first required incident-response playbook for Kerberos password spraying
- Created `reports/ir-playbook-jscript-zip-creation.md`
- Completed the second required incident-response playbook for JScript ZIP creation and credential manager use
- Created `reports/ir-playbook-suspicious-service-installation.md`
- Completed the third required incident-response playbook for suspicious service installation
- Completed the PRD requirement for three incident-response playbooks
- Created `reports/ioc-research-notes.md`
- Documented indicators from validated Kerberos password-spray and JScript ZIP staging telemetry
- Created `reports/executive-summary.md`
- Completed the executive summary report for the detection engineering lab
- Created `reports/methodology.md`
- Documented the repeatable detection engineering, validation, threat hunting, incident response, IOC research, and ATT&CK mapping methodology
- Added `rules/suspicious_powershell_download.yml`
- Added `rules/suspicious_scheduled_task_creation.yml`
- Added `rules/multiple_suspicious_processes_from_temp.yml`
- Expanded Sigma rule coverage to 15 rules
- Expanded Sigma rule coverage to 23 rules
- Expanded ATT&CK coverage matrix to 20 unique techniques
- Added detection coverage for PowerShell, scheduled tasks, LSASS access, rundll32, RDP, account creation, Registry Run keys, WMI, user execution, and Defender exclusion activity
- Created `reports/final-presentation.md`
- Completed the final presentation summarizing the detection engineering lab
- Completed final verification: 23 Sigma-style rules, 20 ATT&CK techniques, and 64 passing automated tests
- Completed final verification: 23 Sigma-style rules, 20 ATT&CK techniques, and 64 passing automated tests
- Updated `README.md` to document real-telemetry validation, completed deliverables, and final project status
- Created `reports/rule-tuning-notes.md`
- Documented false-positive tuning passes for three detection rules

### Test results


```text
64 passed
```

## Phase 6: Rule Quality & False Positive Tuning

- Created `reports/rule-tuning-notes.md`
- Documented false-positive tuning passes for three detection rules
- Added a justified true-positive closure classification to `reports/incident-case-kerberos-password-spray.md`
- Added a justified true-positive closure classification to `reports/incident-case-jscript-zip-creation.md`
- Confirmed that all incident case reports include justified closure classifications
- Added external references for key indicators and behaviors in `reports/ioc-research-notes.md`
- Added Not Covered coverage entries for ransomware impact, cloud-storage exfiltration, and credential-store access
- Updated the coverage-matrix test to correctly allow Not Covered entries without supporting rule IDs
- Expanded `docs/data-dictionary.md` to document four telemetry sources, including mock CSV, Windows Security EVTX, and Sysmon EVTX data