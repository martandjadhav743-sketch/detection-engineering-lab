# Real Telemetry Data Dictionary

## Dataset

**Dataset:** EVTX-ATTACK-SAMPLES

**Sample:** `Credential Access/kerberos_pwd_spray_4771.evtx`

**Local location:** `data/raw/kerberos_pwd_spray_4771.evtx`

**Primary detection focus:** Kerberos password spraying

**MITRE ATT&CK technique:** T1110.003 — Password Spraying

## Event summary

| Event ID | Count | Meaning |
|---|---:|---|
| 1102 | 1 | Security log was cleared |
| 4768 | 9 | Kerberos authentication ticket request |
| 4771 | 2 | Kerberos pre-authentication failed |

## Event ID 4768

Event ID 4768 records a Kerberos authentication ticket request. In this sample, multiple accounts experienced Kerberos pre-authentication failure from the same source IP address.

### Fields used for detection

| Field | Example value | Detection use |
|---|---|---|
| `EventID` | `4768` | Identifies a Kerberos ticket request |
| `TargetUserName` | `HD01`, `admin` | Identifies the account being targeted |
| `TargetDomainName` | `THREEBEESCO.COM` | Identifies the account domain |
| `Status` | `0x00000006` | Indicates Kerberos pre-authentication failure |
| `IpAddress` | `172.16.66.1` | Identifies the source IP address |
| `IpPort` | `55961` | Identifies the source port |
| `TimeCreated` | `2020-07-22 20:29:36` | Supports time-window correlation |
| `Computer` | `01566s-win16-ir.threebeesco.com` | Identifies the system that recorded the event |

## Event ID 4771

Event ID 4771 records a Kerberos pre-authentication failure. This event can also support password-spraying detection, but this sample contains only two `4771` events.

## Event ID 1102

Event ID 1102 records that the Windows Security log was cleared. This can be an indicator of defensive evasion or evidence destruction, but it requires context because administrators may also clear logs during authorized maintenance.

## Initial password-spraying evidence

The sample contains multiple Kerberos pre-authentication failures associated with different user accounts from the same source IP address:

| Target account | Source IP | Status |
|---|---|---|
| `HD01` | `172.16.66.1` | `0x00000006` |
| `admin` | `172.16.66.1` | `0x00000006` |

This pattern supports a hypothesis of password spraying: one source attempting authentication against multiple accounts.

## Detection implication

The existing password-spraying rule should be updated or supplemented with logic that detects multiple Event ID `4768` events with:

- `Status` equal to `0x00000006`
- The same `IpAddress`
- Multiple distinct `TargetUserName` values
- Events occurring within a defined time window

This is a correlation-style detection because it depends on a sequence or combination of events rather than one individual log line.