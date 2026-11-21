import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from Evtx.Evtx import Evtx


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = PROJECT_ROOT / "rules"
EVTX_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "kerberos_pwd_spray_4771.evtx"
)

NAMESPACE = {
    "event": "http://schemas.microsoft.com/win/2004/08/events/event"
}


def load_rule():
    rule_path = RULES_PATH / "kerberos_preauth_failure_from_single_source.yml"

    with rule_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def get_event_data(xml_root, field_name):
    for data in xml_root.findall(
        ".//event:EventData/event:Data", NAMESPACE
    ):
        if data.get("Name") == field_name:
            return data.text

    return None


def count_matching_real_events():
    matching_events = 0

    with Evtx(str(EVTX_PATH)) as event_log:
        for record in event_log.records():
            xml_root = ET.fromstring(record.xml())

            event_id = xml_root.find(
                ".//event:System/event:EventID", NAMESPACE
            )

            if event_id is None or event_id.text != "4771":
                continue

            status = get_event_data(xml_root, "Status")

            if status == "0x00000018":
                matching_events += 1

    return matching_events


def test_kerberos_preauth_failure_rule_exists():
    rule = load_rule()

    assert rule["title"] == (
        "Repeated Kerberos Pre-Authentication Failures from Single Source"
    )


def test_kerberos_preauth_failure_rule_has_attack_mapping():
    rule = load_rule()

    assert "attack.t1110.003" in rule["tags"]


def test_kerberos_preauth_failure_rule_matches_real_telemetry():
    assert count_matching_real_events() == 2