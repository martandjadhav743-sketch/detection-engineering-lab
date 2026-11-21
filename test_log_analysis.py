from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT / "src"))

from log_analysis import (
    load_events,
    count_events,
    failed_logons_by_source_ip,
    identify_repeated_failed_logons,
)


def test_load_events_returns_dataframe():
    events = load_events()
    assert isinstance(events, pd.DataFrame)
    assert len(events) == 13


def test_count_events_returns_expected_counts():
    events = load_events()
    counts = count_events(events)
    assert counts["Failed Logon"] == 7
    assert counts["Successful Logon"] == 4
    assert counts["Account Locked Out"] == 1
    assert counts["Special Privileges Assigned"] == 1


def test_failed_logons_by_source_ip():
    events = load_events()
    failed_counts = failed_logons_by_source_ip(events)
    assert failed_counts["203.0.113.45"] == 5
    assert failed_counts["198.51.100.22"] == 2


def test_identify_repeated_failed_logons_default_threshold():
    events = load_events()
    repeated = identify_repeated_failed_logons(events)
    assert "203.0.113.45" in repeated.index
    assert "198.51.100.22" not in repeated.index


def test_identify_repeated_failed_logons_custom_threshold():
    events = load_events()
    repeated = identify_repeated_failed_logons(events, threshold=2)
    assert "203.0.113.45" in repeated.index
    assert "198.51.100.22" in repeated.index