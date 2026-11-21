# Mock Telemetry Baseline Report

## Date

21 November 2026

## Dataset

`data/mock_windows_security_events.csv`

## Purpose

This report records the initial baseline of the mock Windows Security-style telemetry
used in this defensive detection engineering project.

## Dataset summary

The dataset contains 13 simulated authentication events.

| Event type | Count |
|---|---:|
| Failed Logon | 7 |
| Successful Logon | 4 |
| Account Locked Out | 1 |
| Special Privileges Assigned | 1 |

## Failed logon observations

| Source IP | Failed logons |
|---|---:|
| 203.0.113.45 | 5 |
| 198.51.100.22 | 2 |

## Initial observations

1. The account `jsmith` experienced five failed logon attempts from `203.0.113.45`
   followed by an account lockout event.

2. The account `brown` experienced two failed logon attempts from `198.51.100.22`,
   followed by a successful logon from the same source IP.

3. The account `asmith` successfully logged on to `WS02` and received special
   privileges.

## Defensive analysis value

These observations provide a baseline for developing future detection rules,
including rules for repeated failed authentication, account lockouts, and
privileged logon activity.

## Safety note

All events are mock and simulated. No real user data, credentials, systems, or
harmful activity are involved.