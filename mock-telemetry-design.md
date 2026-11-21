# Mock Telemetry Design

## Purpose

This project uses mock, simulated security telemetry for defensive detection engineering
and threat-hunting practice.

The telemetry is synthetic. It does not contain real user data, real credentials, real
IP addresses, or real system activity. It is intended only for building and testing
defensive detection rules and documentation.

## Simulated environment

The simulated environment represents a small Windows-based client environment.

It includes:

- One simulated domain controller
- Two simulated Windows workstations
- Several simulated user accounts
- Simulated authentication events

## Log source

The primary mock log source is:

- `data/mock_windows_security_events.csv`

This file represents a simplified Windows Security event log focused on authentication
activity.

## Event types

| Event ID | Meaning | Defensive use |
|---|---|---|
| 4624 | Successful account logon | Baseline authentication activity |
| 4625 | Failed account logon | Possible invalid password, locked account, or credential guessing |
| 4740 | User account locked out | Repeated failed authentication or account-security control |
| 4672 | Special privileges assigned to a new logon | Privileged account activity |

## Important safety note

These events are simulated examples for analysis only.

No real attack activity, malware, exploit, credential theft, or network attack is
generated, executed, or encouraged by this project.