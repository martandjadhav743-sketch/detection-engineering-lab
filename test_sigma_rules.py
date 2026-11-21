from pathlib import Path

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = PROJECT_ROOT / "rules"
DATA_PATH = PROJECT_ROOT / "data" / "mock_windows_security_events.csv"


def load_rule(filename):
    rule_path = RULES_PATH / filename
    with rule_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def get_rule_matches(rule, df):
    target_event_id = rule["detection"]["selection"]["event_id"]
    return df[df["event_id"] == target_event_id]


def test_repeated_failed_logons_rule_exists():
    rule = load_rule("repeated_failed_logons.yml")
    assert rule["title"] == "Repeated Failed Logons from Same Source IP"


def test_repeated_failed_logons_rule_has_attack_mapping():
    rule = load_rule("repeated_failed_logons.yml")
    assert "attack.t1110" in rule["tags"]


def test_repeated_failed_logons_rule_matches_mock_data():
    rule = load_rule("repeated_failed_logons.yml")
    df = pd.read_csv(DATA_PATH)
    matches = get_rule_matches(rule, df)
    assert len(matches) == 7


def test_account_lockout_rule_exists():
    rule = load_rule("account_lockout.yml")
    assert rule["title"] == "User Account Locked Out"


def test_account_lockout_rule_has_attack_mapping():
    rule = load_rule("account_lockout.yml")
    assert "attack.t1110" in rule["tags"]


def test_account_lockout_rule_matches_mock_data():
    rule = load_rule("account_lockout.yml")
    df = pd.read_csv(DATA_PATH)
    matches = get_rule_matches(rule, df)
    assert len(matches) == 1

def test_privileged_logon_rule_exists():
    rule = load_rule("privileged_logon.yml")
    assert rule["title"] == "Special Privileges Assigned to New Logon"


def test_privileged_logon_rule_has_attack_mapping():
    rule = load_rule("privileged_logon.yml")
    assert "attack.t1078" in rule["tags"]


def test_privileged_logon_rule_matches_mock_data():
    rule = load_rule("privileged_logon.yml")
    df = pd.read_csv(DATA_PATH)
    matches = get_rule_matches(rule, df)
    assert len(matches) == 1

def test_unfamiliar_source_logon_rule_exists():
    rule = load_rule("successful_logon_from_unfamiliar_source.yml")
    assert rule["title"] == "Successful Logon from Unfamiliar Source IP"


def test_unfamiliar_source_logon_rule_has_attack_mapping():
    rule = load_rule("successful_logon_from_unfamiliar_source.yml")
    assert "attack.t1078" in rule["tags"]


def test_unfamiliar_source_logon_rule_matches_mock_data():
    rule = load_rule("successful_logon_from_unfamiliar_source.yml")
    df = pd.read_csv(DATA_PATH)

    matches = df[
        (df["event_id"] == 4624)
        & (
            df["source_ip"].str.startswith("203.")
            | df["source_ip"].str.startswith("198.")
        )
    ]

    assert len(matches) == 1

def test_successful_logon_after_failed_logons_rule_exists():
    rule = load_rule("successful_logon_after_failed_logons.yml")
    assert rule["title"] == "Successful Logon After Failed Logons from Same Source IP"


def test_successful_logon_after_failed_logons_rule_has_attack_mapping():
    rule = load_rule("successful_logon_after_failed_logons.yml")
    assert "attack.t1110" in rule["tags"]


def test_successful_logon_after_failed_logons_rule_matches_mock_data():
    df = pd.read_csv(DATA_PATH)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    failed = df[df["event_id"] == 4625]
    successful = df[df["event_id"] == 4624]

    correlated = []

    for _, success_event in successful.iterrows():
        matching_failures = failed[
            (failed["source_ip"] == success_event["source_ip"])
            & (failed["timestamp"] < success_event["timestamp"])
        ]

        if not matching_failures.empty:
            correlated.append(success_event)

    assert len(correlated) == 1
    assert correlated[0]["account_name"] == "brown"

def test_account_lockout_after_repeated_failures_rule_exists():
    rule = load_rule("account_lockout_after_repeated_failures.yml")
    assert rule["title"] == "Account Lockout After Repeated Failed Logons"


def test_account_lockout_after_repeated_failures_rule_has_attack_mapping():
    rule = load_rule("account_lockout_after_repeated_failures.yml")
    assert "attack.t1110" in rule["tags"]


def test_account_lockout_after_repeated_failures_rule_matches_mock_data():
    df = pd.read_csv(DATA_PATH)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    failed = df[df["event_id"] == 4625]
    lockouts = df[df["event_id"] == 4740]

    correlated = []

    for _, lockout in lockouts.iterrows():
        matching_failures = failed[
            (failed["account_name"] == lockout["account_name"])
            & (failed["timestamp"] < lockout["timestamp"])
        ]

        if len(matching_failures) >= 3:
            correlated.append(lockout)

    assert len(correlated) == 1
    assert correlated[0]["account_name"] == "jsmith"

def test_password_spraying_rule_exists():
    rule = load_rule("password_spraying_multiple_accounts.yml")
    assert rule["title"] == "Kerberos Password Spraying Across Multiple Accounts"


def test_password_spraying_rule_has_attack_mapping():
    rule = load_rule("password_spraying_multiple_accounts.yml")
    assert "attack.t1110.003" in rule["tags"]


def test_password_spraying_rule_matches_mock_data():
    df = pd.read_csv(DATA_PATH)

    failed = df[df["event_id"] == 4625]
    accounts_by_source_ip = failed.groupby("source_ip")["account_name"].nunique()

    spraying_sources = accounts_by_source_ip[accounts_by_source_ip > 1]

    assert len(spraying_sources) == 0