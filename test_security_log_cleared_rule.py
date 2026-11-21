from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = PROJECT_ROOT / "rules"
RULE_PATH = RULES_PATH / "security_log_cleared.yml"


def test_security_log_cleared_rule_file_exists():
    assert RULE_PATH.exists()


def test_security_log_cleared_rule_has_expected_id():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    assert rule["id"] == "f4c8b2e9-63d7-4a15-8e92-7b1d5c4a6f83"


def test_security_log_cleared_rule_detects_event_1102():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    selection = rule["detection"]["selection"]

    assert selection["EventID"] == 1102


def test_security_log_cleared_rule_maps_to_t1070_001():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    assert "attack.t1070.001" in rule["tags"]


def test_security_log_cleared_rule_has_high_severity():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    assert rule["level"] == "high"