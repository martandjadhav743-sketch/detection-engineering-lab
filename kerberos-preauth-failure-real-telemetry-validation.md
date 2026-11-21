# Kerberos Pre-Authentication Failure — Real Telemetry Validation

## Purpose

This report validates a detection concept for repeated Kerberos pre-authentication failures from a single source IP address.

The detection is based on Windows Security Event ID `4771`, which records a Kerberos pre-authentication failure.

## Dataset

- **Dataset:** EVTX-ATTACK-SAMPLES
- **Sample:** `Credential Access/kerberos_pwd_spray_4771.evtx`
- **Local file:** `data/raw/kerberos_pwd_spray_4771.evtx`
- **Validation script:** `src/validate_kerberos_preauth_failure.py`

## MITRE ATT&CK Mapping

- **Technique:** `T1110.003 — Password Spraying`
- **Tactic:** Credential Access

Repeated authentication failures from one source IP can indicate an attempt to guess or spray credentials. This sample contains only two failure events, so the result supports detection validation rather than a confirmed security incident.

## Validation method

The validation script reads the real EVTX file and selects Event ID `4771`.

For each matching event, it extracts:

- `TargetUserName`
- `Status`
- `IpAddress`
- `TimeCreated` from the event System section

It groups failures by source IP address and flags a source IP when it has at least two Kerberos pre-authentication failures.

## Real telemetry evidence

The sample contains **2 Event ID 4771 events**.

| Time created | Target account | Source IP | Status |
|---|---|---|---|
| 2020-07-22 20:29:36.425364+00:00 | Administrator | 172.16.66.1 | 0x00000018 |
| 2020-07-22 20:29:36.425838+00:00 | backdoor | 172.16.66.1 | 0x00000018 |

## Validation result

**Result: Repeated Kerberos pre-authentication failure pattern detected.**

The source IP `172.16.66.1` generated two Kerberos pre-authentication failures within the same second. Both events used status code `0x00000018`.

## Detection implication

A detection rule can identify repeated Event ID `4771` events where:

- The same `IpAddress` appears in multiple events
- The `Status` is `0x00000018`
- At least two failures occur from that source IP

## False-positive considerations

Legitimate authentication failures can occur when:

- A user enters an incorrect password
- A service uses an expired or changed password
- A misconfigured application repeatedly attempts authentication
- A user account is locked or disabled

A production rule should include a time window, source-IP threshold, and account-context review to reduce alert noise.

## Limitations

This validation uses only two Event ID `4771` events. It demonstrates that the required fields and failure pattern exist in real telemetry, but it does not prove that the activity was malicious.

The existing password-spraying validation uses Event ID `4768`, while this validation uses Event ID `4771`. The two detections are related but use different event types.