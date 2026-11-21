from src.log_analysis import detect_suspicious_service_installations


def test_detects_service_installed_in_temp():
    log_lines = [
        "2026-11-20T10:00:00.000Z WARNING service_control_manager Service installed event_id=7045 service_name=UpdateHelper image_path=C:\\Temp\\update_helper.exe",
    ]

    matches = detect_suspicious_service_installations(log_lines)

    assert len(matches) == 1
    assert matches[0]["service_name"] == "UpdateHelper"
    assert matches[0]["image_path"] == "C:\\Temp\\update_helper.exe"


def test_detects_service_installed_in_users_public():
    log_lines = [
        "2026-11-20T10:05:00.000Z WARNING service_control_manager Service installed event_id=7045 service_name=SystemTask image_path=C:\\Users\\Public\\system_task.exe",
    ]

    matches = detect_suspicious_service_installations(log_lines)

    assert len(matches) == 1
    assert matches[0]["service_name"] == "SystemTask"
    assert matches[0]["image_path"] == "C:\\Users\\Public\\system_task.exe"


def test_does_not_detect_legitimate_service_installation():
    log_lines = [
        "2026-11-20T10:10:00.000Z INFO service_control_manager Service installed event_id=7045 service_name=LegitimateService image_path=C:\\Program Files\\LegitimateService\\service.exe",
    ]

    matches = detect_suspicious_service_installations(log_lines)

    assert matches == []


def test_does_not_detect_non_service_events():
    log_lines = [
        "2026-11-20T10:15:00.000Z WARNING service_control_manager Service stopped event_id=7036 service_name=UpdateHelper image_path=C:\\Temp\\update_helper.exe",
    ]

    matches = detect_suspicious_service_installations(log_lines)

    assert matches == []