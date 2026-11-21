from pathlib import Path

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = PROJECT_ROOT / "rules"
MATRIX_PATH = PROJECT_ROOT / "docs" / "attack-coverage-matrix.csv"


def test_coverage_matrix_exists():
    assert MATRIX_PATH.exists()


def test_coverage_matrix_has_expected_columns():
    df = pd.read_csv(MATRIX_PATH)
    expected_columns = [
        "tactic",
        "technique_id",
        "technique_name",
        "coverage_status",
        "supporting_rule_id",
        "notes",
    ]
    assert list(df.columns) == expected_columns


def test_every_supporting_rule_id_has_a_sigma_rule():
    df = pd.read_csv(MATRIX_PATH)

    for _, row in df.iterrows():
        rule_id = row["supporting_rule_id"]

        if row["coverage_status"] == "Not Covered" or pd.isna(rule_id):
            continue

        matching_files = list(RULES_PATH.glob("*.yml"))
        found = False

        for rule_file in matching_files:
            with rule_file.open("r", encoding="utf-8") as file:
                rule = yaml.safe_load(file)

            if rule.get("id") == rule_id:
                found = True
                break

        assert found, f"No Sigma rule found for rule ID: {rule_id}"