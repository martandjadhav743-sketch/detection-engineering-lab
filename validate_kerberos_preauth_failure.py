import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from Evtx.Evtx import Evtx


EVTX_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "kerberos_pwd_spray_4771.evtx"
)

NAMESPACE = {
    "event": "http://schemas.microsoft.com/win/2004/08/events/event"
}

MINIMUM_FAILURES = 2


def get_event_data(xml_root, field_name):
    for data in xml_root.findall(
        ".//event:EventData/event:Data", NAMESPACE
    ):
        if data.get("Name") == field_name:
            return data.text

    return None

def get_system_time(xml_root):
    time_created = xml_root.find(
        ".//event:System/event:TimeCreated", NAMESPACE
    )

    if time_created is None:
        return None

    return time_created.get("SystemTime")

def main():
    failures_by_source_ip = defaultdict(list)
    matching_event_count = 0

    with Evtx(str(EVTX_PATH)) as event_log:
        for record in event_log.records():
            xml_root = ET.fromstring(record.xml())

            event_id = xml_root.find(
                ".//event:System/event:EventID", NAMESPACE
            )

            if event_id is None or event_id.text != "4771":
                continue

            status = get_event_data(xml_root, "Status")
            source_ip = get_event_data(xml_root, "IpAddress")
            target_user = get_event_data(xml_root, "TargetUserName")
            event_time = get_system_time(xml_root)

            if source_ip is None or target_user is None:
                continue

            matching_event_count += 1
            failures_by_source_ip[source_ip].append(
                {
                    "target_user": target_user,
                    "status": status,
                    "event_time": event_time,
                }
            )

    print("Kerberos pre-authentication failure validation")
    print("=" * 50)
    print(f"EVTX file: {EVTX_PATH}")
    print(f"Matching Event ID 4771 events: {matching_event_count}")

    for source_ip, failures in failures_by_source_ip.items():
        print(f"\nSource IP: {source_ip}")
        print(f"Kerberos pre-authentication failures: {len(failures)}")

        for failure in failures:
            print(
                f"- {failure['event_time']} | "
                f"{failure['target_user']} | "
                f"Status: {failure['status']}"
            )

        if len(failures) >= MINIMUM_FAILURES:
            print(
                "Result: Repeated Kerberos pre-authentication "
                "failure pattern detected"
            )
        else:
            print(
                "Result: Pattern not detected because the sample does "
                f"not contain at least {MINIMUM_FAILURES} failures "
                "from this source IP"
            )


if __name__ == "__main__":
    main()