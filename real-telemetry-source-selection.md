# Real Telemetry Source Selection

## Selected dataset

**Dataset:** EVTX-ATTACK-SAMPLES

**Repository:** https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES

**Selected sample:** `Credential Access/kerberos_pwd_spray_4771.evtx`

**Primary event ID:** 4771

**Primary MITRE ATT&CK technique:** T1110.003 — Password Spraying

## Why this sample was selected

This sample was selected because it contains real Windows Security event data associated with Kerberos pre-authentication failures.

Event ID 4771 records a Kerberos authentication ticket request that failed pre-authentication. Multiple failed Kerberos authentication attempts can indicate password spraying, where an attacker attempts a small number of common passwords against many user accounts.

This sample directly supports the existing Sigma rule:

```text
rules/password_spraying_multiple_accounts.yml
```

## Detection focus

The initial detection focus is:

- Repeated Kerberos pre-authentication failures
- Password spraying against multiple user accounts
- Credential Access activity
- MITRE ATT&CK technique T1110.003

## Scope and limitations

This dataset will be used for defensive detection engineering, threat hunting, and incident-analysis practice only.

No malware will be executed, no offensive tooling will be deployed, and no live production systems will be accessed.

The sample represents a specific simulated attack scenario and may not include the full range of benign enterprise activity. Detection logic must therefore be tuned carefully to avoid false positives.

## Next steps

1. Download the selected EVTX sample.
2. Convert or inspect the EVTX events to identify available fields.
3. Create a data dictionary for Event ID 4771.
4. Analyze the sample for repeated failures across multiple accounts.
5. Validate the existing password-spraying Sigma rule against the real sample.
6. Document the match results and any required tuning.