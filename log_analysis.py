import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "mock_windows_security_events.csv"


def load_events():
    return pd.read_csv(DATA_PATH)


def count_events(df):
    return df["event_name"].value_counts()


def failed_logons_by_source_ip(df):
    failed = df[df["event_id"] == 4625]
    return failed["source_ip"].value_counts()


def identify_repeated_failed_logons(df, threshold=3):
    failed_counts = failed_logons_by_source_ip(df)
    return failed_counts[failed_counts >= threshold]


if __name__ == "__main__":
    events = load_events()
    print("Total events:", len(events))
    print("\nEvent counts:")
    print(count_events(events))
    print("\nFailed logons by source IP:")
    print(failed_logons_by_source_ip(events))
    print("\nSource IPs with 3 or more failed logons:")
    print(identify_repeated_failed_logons(events))


def detect_unknown_workstation_logons(log_lines):
    matches = []

    for line in log_lines:
        if "event_id=4624" not in line:
            continue

        if "source_workstation=UNKNOWN" not in line:
            continue

        user = None
        source_ip = None
        source_workstation = None

        for part in line.split():
            if part.startswith("user="):
                user = part.removeprefix("user=")
            elif part.startswith("source_ip="):
                source_ip = part.removeprefix("source_ip=")
            elif part.startswith("source_workstation="):
                source_workstation = part.removeprefix("source_workstation=")

        matches.append(
            {
                "user": user,
                "source_ip": source_ip,
                "source_workstation": source_workstation,
            }
        )

    return matches

def detect_suspicious_service_installations(log_lines):
    suspicious_paths = [
        "C:\\Temp\\",
        "C:\\Users\\Public\\",
        "AppData\\Local\\Temp\\",
    ]

    matches = []

    for line in log_lines:
        if "event_id=7045" not in line:
            continue

        image_path = None
        service_name = None

        for part in line.split():
            if part.startswith("image_path="):
                image_path = part.removeprefix("image_path=")
            elif part.startswith("service_name="):
                service_name = part.removeprefix("service_name=")

        if image_path is None:
            continue

        is_suspicious = any(
            suspicious_path in image_path
            for suspicious_path in suspicious_paths
        )

        if is_suspicious:
            matches.append(
                {
                    "service_name": service_name,
                    "image_path": image_path,
                }
            )

    return matches