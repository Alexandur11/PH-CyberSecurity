import pytest

from network_threat_checker.threat_intelligence import check_ip_threat


def test_network_threat_checker_flow(mocker):
    mocker.patch('network_threat_checker.network.get_network_connections', mocker.MagicMock(return_value = MOCK_CONNECTIONS))

    unique_ips = {conn['remote_ip'] for conn in MOCK_CONNECTIONS}

    for ip in unique_ips:
        result = check_ip_threat(ip)



MOCK_CONNECTIONS = [
    {
        'local_ip': '192.168.1.100',
        'local_port': '12345',
        'remote_ip': '203.0.113.1',
        'remote_port': '54321',
        'status': 'ESTABLISHED'
    },
    {
        'local_ip': '192.168.1.101',
        'local_port': '54321',
        'remote_ip': '198.51.100.1',
        'remote_port': '9876',
        'status': 'ESTABLISHED'
    },
    {
        'local_ip': '192.168.1.102',
        'local_port': '80',
        'remote_ip': '192.0.2.1',
        'remote_port': '34567',
        'status': 'LISTEN'
    },
    {
        'local_ip': '192.168.1.103',
        'local_port': '22',
        'remote_ip': '10.0.0.1',
        'remote_port': '1234',
        'status': 'ESTABLISHED'
    },
]
