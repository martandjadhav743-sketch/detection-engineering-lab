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

NAMESPACE = {"event": "http://schemas.microsoft.com/win/2004/08/events/event"}

MINIMUM_ACCOUNTS = 3


def get_event_data(xml_root, field_name):
    for data in xml_root.findall(".//event:EventData/event:Data", NAMESPACE):
        if data.get("Name") == field_name:
            return data.text

    return None


def main():
    accounts_by_source_ip = defaultdict(set)
    matching_event_count = 0

    with Evtx(str(EVTX_PATH)) as event_log:
        for record in event_log.records():
            xml_root = ET.fromstring(record.xml())

            event_id = xml_root.find(".//event:System/event:EventID", NAMESPACE)

            if event_id is None or event_id.text != "4768":
                continue

            status = get_event_data(xml_root, "Status")

            if status != "0x00000006":
                continue

            source_ip = get_event_data(xml_root, "IpAddress")
            target_user = get_event_data(xml_root, "TargetUserName")

            if source_ip is None or target_user is None:
                continue

            matching_event_count += 1
            accounts_by_source_ip[source_ip].add(target_user)

    print("Password spraying validation")
    print("=" * 40)
    print(f"EVTX file: {EVTX_PATH}")
    print(f"Matching Event ID 4768 events: {matching_event_count}")

    for source_ip, accounts in accounts_by_source_ip.items():
        print(f"\nSource IP: {source_ip}")
        print(f"Distinct targeted accounts: {len(accounts)}")
        print(f"Accounts: {', '.join(sorted(accounts))}")

        if len(accounts) >= MINIMUM_ACCOUNTS:
            print("Result: Password spraying pattern detected")
        else:
            print(
                "Result: Pattern not detected because the sample does not "
                f"contain at least {MINIMUM_ACCOUNTS} distinct accounts"
            )


if __name__ == "__main__":
    main()