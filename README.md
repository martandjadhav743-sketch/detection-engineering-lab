# Detection Engineering & Threat Hunting Lab

A beginner-friendly, defensive cybersecurity project based on the Cyberion Defense Labs
Detection Engineering & Threat Hunting engagement.

This project uses safe, clearly labeled mock/simulated security telemetry to practice:

- Log analysis
- Sigma-style detection rule engineering
- MITRE ATT&CK mapping
- Threat hunting
- Incident investigation and reporting
- Incident response playbook writing

## Safety

This project is defensive only.

It does not create, execute, distribute, or encourage malware, exploits, credential theft,
network attacks, ransomware, or any harmful activity. All telemetry is mock/simulated and
intended for detection engineering, analysis, and documentation practice.

## Project structure

- `src/` — Python analysis and rule-testing code
- `data/` — mock/simulated log data
- `docs/` — methodology, data dictionary, and supporting documentation
- `rules/` — Sigma-style detection rules
- `reports/` — threat hunt, incident, IOC, and executive reports
- `screenshots/` — project evidence screenshots
- `tests/` — automated tests

## How to run

1. Open Command Prompt or PowerShell.
2. Go to the project folder:

```powershell
cd C:\Users\marta\Desktop\detection-engineering-lab
```

3. Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

4. Install dependencies after they are added:

```powershell
pip install -r requirements.txt
```

## Status

See `PROGRESS.md` for the current project status.