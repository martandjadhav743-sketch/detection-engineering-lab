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