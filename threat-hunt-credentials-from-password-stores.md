# Threat Hunt: Credentials from Password Stores

## Objective

Hunt for evidence of attempts to access credentials stored in browser password stores, Windows Credential Manager, or other local credential-storage mechanisms.

## ATT&CK technique

- T1555 - Credentials from Password Stores

## Coverage gap

This technique is currently marked as `Not Covered` in `docs/attack-coverage-matrix.csv`. No existing Sigma detection rule specifically identifies access to browser password stores, credential managers, or password vaults.

## Hunt hypothesis

An attacker may attempt to access stored credentials by executing credential-access tools, querying Windows Credential Manager, or accessing browser credential databases. This activity may support lateral movement, privilege escalation, or persistence.

## Data sources

| Data source | Relevant telemetry |
|---|---|
| Sysmon Event ID 1 | Process creation, command-line arguments, and parent-child process relationships |
| Sysmon Event ID 3 | Network connections initiated by suspicious credential-access processes |
| Sysmon Event ID 11 | File creation or modification involving browser credential databases |
| Windows Security Event ID 4688 | Process creation and command-line activity |
| Windows Security Event ID 4624 | Successful logons that may follow credential access |

## Hunt queries

### Suspicious credential-access process activity

Search Sysmon Event ID 1 or Windows Security Event ID 4688 records for process names or command-line patterns associated with credential access, including:

- `mimikatz`
- `secretsdump`
- `pypykatz`
- `BrowserExport`
- `ChromePass`
- `WebBrowserPassView`
- `dpapi`
- `vaultcmd`

### Windows Credential Manager activity

Search for execution of:

```text
cmdkey.exe /list
```

Also review unexpected execution of `cmdkey.exe` with arguments that add, delete, or enumerate stored credentials.

### Browser credential-store access

Search Sysmon Event ID 11 records for file paths associated with browser credential storage, including:

```text
\Login Data
\Cookies
\Web Data
\Local State
```

Review whether these files were accessed or copied by unusual processes, especially processes executing from user-writable directories.

## Expected findings

A positive hunt result would include:

- Execution of a known credential-access tool
- Unusual access to browser credential databases
- Unexpected enumeration of Windows Credential Manager entries
- Credential-access activity followed by network connections or successful authentication from an unfamiliar source
- File-copy activity involving browser credential databases

## Current findings

No dedicated telemetry sample for credential-store access was available in the current dataset. The hunt establishes the required detection logic, data sources, and investigation workflow for future telemetry collection.

## Recommended actions

1. Collect Sysmon Event ID 1, Event ID 3, and Event ID 11 telemetry from endpoints.
2. Retain Windows Security Event ID 4688 process-creation telemetry where available.
3. Review endpoint activity for unexpected credential-access tools or browser credential-database access.
4. Create a detection rule if repeated credential-store access activity is observed.
5. Update the ATT&CK coverage matrix if a validated detection rule is added.

## Conclusion

This threat hunt documents an active hunt for credential-store access, a technique not currently covered by the existing detection ruleset. Additional endpoint telemetry is required to execute the hunt against production or realistic sample data.