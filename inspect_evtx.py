from pathlib import Path

from Evtx.Evtx import Evtx

EVTX_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "kerberos_pwd_spray_4771.evtx"


def main():
    event_counts = {}
    sample_events = []

    with Evtx(str(EVTX_PATH)) as event_log:
        for record in event_log.records():
            xml = record.xml()

            event_id = None

            for line in xml.splitlines():
                if 'EventID' in line:
                    start = line.find(">") + 1
                    end = line.find("</EventID>")
                    event_id = line[start:end]
                    break

            if event_id is None:
                continue

            event_counts[event_id] = event_counts.get(event_id, 0) + 1

            if len(sample_events) < 3:
                sample_events.append(xml)

    print("EVTX file:")
    print(EVTX_PATH)

    print("\nEvent counts:")
    for event_id, count in sorted(event_counts.items()):
        print(f"Event ID {event_id}: {count}")

    print("\nFirst 3 event records:")
    for xml in sample_events:
        print(xml)
        print("-" * 80)


if __name__ == "__main__":
    main()