import pytest
from network_threat_checker.threat_intelligence import check_ip_threat
from tests.mocked_data import MOCK_CONNECTIONS


def test_network_threat_checker_for_active_connections(mocker):
    # Arrange
    mocker.patch('network_threat_checker.network.get_network_connections',
                 mocker.MagicMock(return_value=MOCK_CONNECTIONS))
    unique_ips = {conn['remote_ip'] for conn in MOCK_CONNECTIONS}

    # Act & Assert
    for ip in unique_ips:
        result = check_ip_threat(ip)
        assert result is not None


def test_network_threat_checker_for_historical_connections(mocker):
    # Arrange
    mocker.patch('network_threat_checker.network.get_historical_connections',
                 mocker.MagicMock(return_value=MOCK_CONNECTIONS))
    unique_ips = {conn['remote_ip'] for conn in MOCK_CONNECTIONS}

    # Act & Assert
    for ip in unique_ips:
        result = check_ip_threat(ip)
        assert result is not None
