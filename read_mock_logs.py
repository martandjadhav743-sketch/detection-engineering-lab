import pandas as pd
from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data" / "mock_windows_security_events.csv"

df = pd.read_csv(data_path)

print("Rows loaded:", len(df))
print("\nEvent counts:")
print(df["event_name"].value_counts())

print("\nFailed logons by source IP:")
failed = df[df["event_id"] == 4625]
print(failed["source_ip"].value_counts())