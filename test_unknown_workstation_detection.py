from src.log_analysis import detect_unknown_workstation_logons


def test_detects_unknown_workstation_logons():
    log_lines = [
        "2026-11-20T09:00:00.000Z INFO auth_service Successful logon event_id=4624 user=svc_backup source_ip=10.10.10.50 source_workstation=UNKNOWN",
        "2026-11-20T09:05:00.000Z INFO auth_service Successful logon event_id=4624 user=jdoe source_ip=10.10.10.51 source_workstation=UNKNOWN",
    ]

    matches = detect_unknown_workstation_logons(log_lines)

    assert len(matches) == 2

    assert matches[0]["user"] == "svc_backup"
    assert matches[0]["source_ip"] == "10.10.10.50"
    assert matches[0]["source_workstation"] == "UNKNOWN"

    assert matches[1]["user"] == "jdoe"
    assert matches[1]["source_ip"] == "10.10.10.51"
    assert matches[1]["source_workstation"] == "UNKNOWN"


def test_does_not_detect_known_workstation_logons():
    log_lines = [
        "2026-11-20T09:00:00.000Z INFO auth_service Successful logon event_id=4624 user=jdoe source_ip=10.10.10.10 source_workstation=WORKSTATION01",
    ]

    matches = detect_unknown_workstation_logons(log_lines)

    assert matches == []


def test_does_not_detect_failed_logons_from_unknown_workstation():
    log_lines = [
        "2026-11-20T09:00:00.000Z WARNING auth_service Failed logon event_id=4625 user=jdoe source_ip=10.10.10.99 source_workstation=UNKNOWN",
    ]

    matches = detect_unknown_workstation_logons(log_lines)

    assert matches == []