from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = PROJECT_ROOT / "rules"
RULE_PATH = RULES_PATH / "suspicious_service_installation.yml"


def test_service_installation_rule_file_exists():
    assert RULE_PATH.exists()


def test_service_installation_rule_has_expected_id():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    assert rule["id"] == "e8a2c7d4-91b6-4f38-8d57-2c6a9f4b1e73"


def test_service_installation_rule_detects_event_7045():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    selection = rule["detection"]["selection"]

    assert selection["event_id"] == 7045


def test_service_installation_rule_checks_suspicious_paths():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    suspicious_path = rule["detection"]["suspicious_path"]

    assert "C:\\Temp\\" in suspicious_path["image_path|contains"]
    assert "C:\\Users\\Public\\" in suspicious_path["image_path|contains"]
    assert "AppData\\Local\\Temp\\" in suspicious_path["image_path|contains"]


def test_service_installation_rule_has_high_severity():
    with RULE_PATH.open("r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    assert rule["level"] == "high"