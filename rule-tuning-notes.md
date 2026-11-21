# Rule Tuning Notes

## Purpose

This document records false-positive tuning passes for selected detection rules. Each tuning pass documents an observed false-positive scenario, the logic change made to reduce false positives, and the trade-off accepted.

## Tuning pass 1: Successful logon from unfamiliar source

### Rule

```text
rules/successful_logon_from_unfamiliar_source.yml
```

### Observed false-positive scenario

A user may legitimately sign in from a new IP address after traveling, changing networks, or using a new device.

### Tuning change

The rule focuses on successful logon activity from an unfamiliar source IP address rather than treating every new source IP as malicious.

### Trade-off accepted

The rule may still generate alerts for legitimate travel or new-device activity. Analysts should review account context, prior source IP history, and successful logon timing before escalation.

## Tuning pass 2: Successful logon after failed logons

### Rule

```text
rules/successful_logon_after_failed_logons.yml
```

### Observed false-positive scenario

A user may enter an incorrect password several times and then successfully authenticate.

### Tuning change

The rule correlates repeated failed logons with a subsequent successful logon rather than alerting on failed logons alone.

### Trade-off accepted

The rule may still generate alerts for legitimate user error. Analysts should review source IP consistency, account type, time window, and whether the successful logon originated from the same source.

## Tuning pass 3: Multiple suspicious processes from Temp

### Rule

```text
rules/multiple_suspicious_processes_from_temp.yml
```

### Observed false-positive scenario

Legitimate software installers, update utilities, and browser-related processes may execute files from the user Temp directory.

### Tuning change

The rule excludes common system processes and requires multiple process executions from Temp within a 10-minute timeframe.

### Trade-off accepted

The rule may still generate alerts for legitimate software installation activity. Analysts should review the parent process, file path, command line, and whether the activity aligns with approved software deployment.

## Conclusion

These tuning passes improve detection precision while preserving visibility into potentially suspicious activity. Each rule retains an explicit false-positive discussion and requires analyst review of surrounding context before escalation.