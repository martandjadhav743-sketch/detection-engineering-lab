# Incident Case Report: Kerberos Password Spraying

## Incident summary

A potential Kerberos password-spraying incident was identified after two Kerberos pre-authentication failure events were observed from the same source IP address against two different user accounts.

## Incident details

| Field | Value |
|---|---|
| Incident type | Potential password spraying |
| ATT&CK technique | T1110.003 - Password Spraying |
| Data source | `data/raw/kerberos_pwd_spray_4771.evtx` |
| Source IP address | `172.16.66.1` |
| Targeted accounts | `Administrator`, `backdoor` |
| Relevant event ID | `4771` |
| Kerberos status | `0x00000018` |
| Detection rule | `rules/kerberos_preauth_failure_from_single_source.yml` |

## Timeline

| Time | Activity |
|---|---|
| Sample timeframe | Two Event ID `4771` Kerberos pre-authentication failure events were recorded from `172.16.66.1` |
| Sample timeframe | The events targeted the `Administrator` and `backdoor` accounts |
| Sample timeframe | Both events used Kerberos status `0x00000018`, indicating invalid pre-authentication information |

## Evidence

- The EVTX sample contains two Event ID `4771` Kerberos pre-authentication failure events.
- Both events originated from source IP address `172.16.66.1`.
- The source IP targeted two separate accounts.
- Both events used Kerberos status `0x00000018`.
- The activity matches the password-spraying pattern of repeated authentication failures from one source against multiple accounts.

## Impact assessment

The observed activity indicates a potential attempt to gain unauthorized access through password spraying. No successful logon event was present in the analyzed sample, so account compromise cannot be confirmed from this evidence alone.

## Recommended actions

1. Review all authentication activity from source IP address `172.16.66.1`.
2. Review successful and failed logon activity for the `Administrator` and `backdoor` accounts.
3. Check for unusual privilege use, new logon locations, or suspicious account changes.
4. Block or restrict the source IP address if it is confirmed to be unauthorized.
5. Reset passwords for affected accounts if compromise is suspected.
6. Preserve relevant authentication logs and escalate the incident according to the incident-response process.

## Closure classification

**Closure classification:** True positive

**Justification:** The EVTX sample contains two Kerberos pre-authentication failure events from the same source IP address targeting two separate accounts. Both events used Kerberos status `0x00000018`, which is consistent with password-spraying behavior. The password-spraying activity is therefore confirmed as a true positive.

The available evidence does not show a successful logon or confirm account compromise. Further investigation would be required to determine whether any authentication attempt succeeded.

## Conclusion

The evidence supports a confirmed Kerberos password-spraying incident. Further investigation is required to determine whether any authentication attempt succeeded or whether either targeted account was compromised.