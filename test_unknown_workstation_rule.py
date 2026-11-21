from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = PROJECT_ROOT / "rules"
RULE_PATH = RULES_PATH / "successful_logon_from_unknown_workstation.yml"


def test_unknown_workstation_rule_file_exists():
    assert RULE_PATH.exists()


def test_unknown_workstation_rule_has_expected_id():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    assert rule["id"] == "d6f3a8c2-47b1-4e59-8c26-9b7e3f1a5d84"


def test_unknown_workstation_rule_detects_event_4624():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    selection = rule["detection"]["selection"]

    assert selection["event_id"] == 4624
    assert selection["source_workstation"] == "UNKNOWN"


def test_unknown_workstation_rule_has_medium_severity():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    assert rule["level"] == "medium"