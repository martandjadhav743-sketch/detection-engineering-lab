from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "mock_windows_security_events.csv"

EXPECTED_COLUMNS = [
    "timestamp",
    "computer",
    "event_id",
    "event_name",
    "account_name",
    "account_domain",
    "logon_type",
    "source_ip",
    "source_workstation",
    "status",
    "result",
]


def test_mock_log_file_exists():
    assert DATA_PATH.exists()


def test_mock_log_loads_successfully():
    df = pd.read_csv(DATA_PATH)
    assert len(df) == 13


def test_mock_log_has_expected_columns():
    df = pd.read_csv(DATA_PATH)
    assert list(df.columns) == EXPECTED_COLUMNS


def test_mock_log_contains_expected_event_types():
    df = pd.read_csv(DATA_PATH)
    event_ids = set(df["event_id"])
    assert {4624, 4625, 4740, 4672}.issubset(event_ids)