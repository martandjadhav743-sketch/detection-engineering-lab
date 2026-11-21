# Data Dictionary

## Telemetry sources

This project uses the following telemetry sources:

| Source | File | Event format | Primary use |
|---|---|---|---|
| Mock Windows Security events | `data/mock_windows_security_events.csv` | CSV | Baseline authentication detection testing |
| Windows Security event log | `data/raw/kerberos_pwd_spray_4771.evtx` | Windows EVTX | Kerberos pre-authentication failure and password-spraying analysis |
| Windows Security event log | `data/raw/security_log_cleared_1102.evtx` | Windows EVTX | Security log-clearing detection validation |
| Sysmon event log | `data/raw/sysmon_zipexec.evtx` | Windows EVTX | JScript execution, ZIP creation, and process-parent analysis |

## Mock Windows Security events

### File

`data/mock_windows_security_events.csv`

## Purpose

This file contains mock, simulated Windows Security-style authentication events for
defensive detection engineering and threat-hunting practice.

The data is synthetic and does not represent real users, systems, credentials, or
network activity.

## Fields

| Field | Meaning | Detection relevance |
|---|---|---|
| `timestamp` | Date and time when the simulated event occurred | Used to build event timelines and identify repeated activity |
| `computer` | Name of the simulated computer that generated the event | Identifies the affected or reporting host |
| `event_id` | Numeric Windows Security event identifier | Primary field for selecting authentication events |
| `event_name` | Human-readable name for the event | Helps analysts understand the event type |
| `account_name` | Simulated user account involved in the event | Identifies the account being used or targeted |
| `account_domain` | Simulated domain for the account | Helps distinguish domain and local accounts |
| `logon_type` | Type of logon, such as interactive or network | Helps distinguish normal workstation use from remote authentication |
| `source_ip` | Simulated IP address associated with the event | Useful for identifying repeated authentication attempts |
| `source_workstation` | Simulated source workstation name | Useful for identifying unfamiliar or unexpected sources |
| `status` | Windows-style status code | Can indicate the reason for a failed logon |
| `result` | Simple success or failure indicator | Useful for quick filtering and validation |

## Event IDs

| Event ID | Event name | Defensive meaning |
|---|---|---|
| 4624 | Successful Logon | A simulated account successfully authenticated |
| 4625 | Failed Logon | A simulated authentication attempt failed |
| 4740 | Account Locked Out | A simulated account was locked after repeated failures |
| 4672 | Special Privileges Assigned | A simulated logon received privileged rights |

## Current dataset

The current mock dataset contains 13 events:

- 7 failed logons
- 4 successful logons
- 1 account lockout
- 1 special-privilege assignment

## Safety note

This dataset is for defensive analysis only. No harmful activity, malware, exploit,
credential theft, or network attack is created, executed, or encouraged.