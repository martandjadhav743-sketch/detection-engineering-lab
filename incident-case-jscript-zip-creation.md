# Incident Case Report: JScript ZIP Creation and Credential Manager Use

## Incident summary

A potential archive-based execution or staging incident was identified after `cscript.exe` executed JScript, created a ZIP archive in the user Temp directory, and `cmdkey.exe` used the Windows Shell ZipFolder protocol.

## Incident details

| Field | Value |
|---|---|
| Incident type | Potential JScript-based ZIP staging |
| ATT&CK techniques | T1059.007 - JavaScript/JScript; T1105 - Ingress Tool Transfer |
| Data source | `data/raw/sysmon_zipexec.evtx` |
| Relevant event IDs | `1`, `11` |
| Executing process | `cscript.exe` |
| ZIP archive | `lync.zip` |
| ZIP location | `C:\Users\bouss\AppData\Local\Temp\lync.zip` |
| Credential Manager process | `cmdkey.exe` |
| Detection rule | `rules/suspicious_jscript_zip_creation_cmdkey.yml` |

## Timeline

| Time | Activity |
|---|---|
| 2021-10-21 16:27:02 UTC | `cscript.exe` executed JScript using the `//e:jscript` argument |
| 2021-10-21 16:27:02 UTC | `cmdkey.exe` used the `Microsoft_Windows_Shell_ZipFolder` protocol with `lync.zip` |
| 2021-10-21 16:27:03 UTC | Sysmon recorded creation of `lync.zip` in the user Temp directory |

## Evidence

- Sysmon Event ID `1` recorded `cscript.exe` executing JScript with `//e:jscript`.
- Sysmon Event ID `11` recorded `cscript.exe` creating `lync.zip` in `AppData\Local\Temp`.
- Sysmon Event ID `1` recorded `cmdkey.exe` using the `Microsoft_Windows_Shell_ZipFolder` protocol.
- The `cmdkey.exe` process had `cscript.exe` as its parent process.
- The activity matches a potential archive-based execution or staging pattern.

## Impact assessment

The observed activity indicates potential JScript-based archive staging. The evidence does not confirm data exfiltration, malware execution, or credential compromise, so further investigation is required.

## Recommended actions

1. Review the full command line and parent process for `cscript.exe`.
2. Identify the origin and contents of `lync.zip`.
3. Determine whether the ZIP archive was downloaded, created locally, or extracted from another location.
4. Review process activity occurring after the ZIP archive was created.
5. Check whether `cmdkey.exe` stored credentials or accessed sensitive material.
6. Isolate the endpoint if malicious JScript execution or unauthorized archive activity is confirmed.
7. Preserve the Sysmon events, ZIP file metadata, and related process activity for investigation.

## Closure classification

**Closure classification:** True positive

**Justification:** The Sysmon evidence confirms that `cscript.exe` executed JScript, created `lync.zip` in the user Temp directory, and launched `cmdkey.exe` using the Windows Shell ZipFolder protocol. The detection rule therefore correctly identified the suspicious JScript-based ZIP staging behavior.

The available evidence does not confirm malware execution, data exfiltration, or credential compromise. Further investigation is required to determine whether the activity was malicious and whether sensitive data or credentials were accessed.

## Conclusion

The evidence supports a confirmed JScript-based ZIP staging incident. Further investigation is required to determine whether the activity was malicious and whether any sensitive data or credentials were accessed.