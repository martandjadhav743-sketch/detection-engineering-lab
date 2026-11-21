# IOC Research Notes

## Purpose

This document records indicators of compromise observed during real-telemetry validation and threat hunting. These indicators should be used for investigation and detection tuning, not as standalone proof of compromise.

## Kerberos password spraying indicators

| Indicator type | Indicator | Context | Confidence |
|---|---|---|---|
| IP address | `172.16.66.1` | Source IP address associated with two Kerberos pre-authentication failures | Medium |
| Account name | `Administrator` | Targeted account in the Kerberos pre-authentication failure events | Low |
| Account name | `backdoor` | Targeted account in the Kerberos pre-authentication failure events | Low |
| Event ID | `4771` | Kerberos pre-authentication failure event | Informational |
| Kerberos status | `0x00000018` | Indicates pre-authentication information was invalid | Informational |

### Investigation guidance

- Review whether `172.16.66.1` is an authorized internal system.
- Review authentication activity involving the targeted accounts.
- Look for successful logons after the failed authentication attempts.
- Do not treat the account names alone as malicious indicators; they should be investigated in context.

## JScript ZIP creation indicators

| Indicator type | Indicator | Context | Confidence |
|---|---|---|---|
| Process name | `cscript.exe` | Used to execute JScript with the `//e:jscript` argument | Low |
| Command-line pattern | `//e:jscript` | Indicates explicit JScript execution through `cscript.exe` | Medium |
| File name | `lync.zip` | ZIP archive created in the user Temp directory | Medium |
| File path pattern | `\AppData\Local\Temp\*.zip` | ZIP archive creation location observed in the sample | Low |
| Process name | `cmdkey.exe` | Used the Windows Shell ZipFolder protocol | Low |
| Command-line pattern | `Microsoft_Windows_Shell_ZipFolder` | Indicates use of the Windows Shell ZipFolder protocol | Medium |
| Event ID | `1` | Sysmon process-creation event | Informational |
| Event ID | `11` | Sysmon file-create event | Informational |

### Investigation guidance

- Review the parent process and full command line for `cscript.exe`.
- Determine whether the ZIP archive was expected, authorized, or downloaded from an unknown source.
- Review activity after the ZIP archive was created.
- Do not treat `cscript.exe`, `cmdkey.exe`, or ZIP files alone as malicious; investigate the complete activity chain.

## Detection mapping

| Indicator or behavior | Related detection | Related ATT&CK technique |
|---|---|---|
| Repeated Kerberos pre-authentication failures from one source IP | `rules/kerberos_preauth_failure_from_single_source.yml` | T1110.003 |
| JScript execution through `cscript.exe` | `rules/suspicious_jscript_zip_creation_cmdkey.yml` | T1059.007 |
| ZIP creation in user Temp directory | `rules/suspicious_jscript_zip_creation_cmdkey.yml` | T1105 |
| Windows Shell ZipFolder protocol use | `rules/suspicious_jscript_zip_creation_cmdkey.yml` | T1105 |

## External references

- MITRE ATT&CK T1110.003, Password Spraying: https://attack.mitre.org/techniques/T1110/003/
- MITRE ATT&CK T1059.007, JavaScript/JScript: https://attack.mitre.org/techniques/T1059/007/
- MITRE ATT&CK T1105, Ingress Tool Transfer: https://attack.mitre.org/techniques/T1105/
- Microsoft security auditing documentation for Event ID 4771, Kerberos pre-authentication failed: https://learn.microsoft.com/windows/security/threat-protection/auditing/event-4771
- Microsoft documentation for Kerberos status code `0x18`, `KDC_ERR_PREAUTH_FAILED`: https://learn.microsoft.com/openspecs/windows_protocols/ms-kile/1c1d2cae-27f3-4f0b-a2b0-84c0d1c2b2c0
- Microsoft documentation for `cscript.exe`: https://learn.microsoft.com/windows-server/administration/windows-commands/cscript
- Microsoft documentation for `cmdkey.exe`: https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey
- Sysmon Event ID 1, process creation: https://learn.microsoft.com/sysinternals/downloads/sysmon#event-id-1-process-creation
- Sysmon Event ID 11, file create: https://learn.microsoft.com/sysinternals/downloads/sysmon#event-id-11-file-create

## Conclusion

The indicators above are based on validated real-telemetry samples and should be used to support investigation, detection tuning, and threat hunting. Contextual review is required before treating any single indicator as proof of malicious activity.