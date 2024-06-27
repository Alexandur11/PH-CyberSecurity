import subprocess
import pandas as pd
from scapy.all import rdpcap
from network_threat_checker.threat_intelligence import check_ip_threat


def get_network_connections():
    """
    Retrieves information about active network connections and listening ports
    on the local system using the 'netstat -an' command.

    Returns:
        A list of dictionaries, where each dictionary represents a network
        connection with the following keys:
            - 'local_ip': Local IP address of the connection.
            - 'local_port': Local port number of the connection.
            - 'remote_ip': Remote IP address of the connection.
            - 'remote_port': Remote port number of the connection.
            - 'status': Status of the connection ('ESTABLISHED' or 'LISTEN').
    """

    result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    connection_info = []
    for line in lines:
        if 'ESTABLISHED' in line or 'LISTEN' in line:
            parts = line.split()
            local_address = parts[3]
            remote_address = parts[4]
            status = parts[5]

            local_ip, local_port = local_address.rsplit('.', 1)
            remote_ip, remote_port = remote_address.rsplit('.', 1)

            connection_info.append({
                'local_ip': local_ip,
                'local_port': local_port,
                'remote_ip': remote_ip,
                'remote_port': remote_port,
                'status': status
            })

    return connection_info


def get_historical_connections():

    """
    Retrieves information about past network connections from a WireShark pre-saved file.
    Returns:
        A list of IP addresses.
    """

    pcap = rdpcap('old_connections.pcapng')
    destinations = set()
    try:
        for packet in pcap:
            destination = packet['IP'].dst
            destinations.add(destination)
    except Exception as e:
        print(f"One packet skipped, due to absence of IP address to parse : {e}")

    return destinations

def display_current_connections():

    """Retrieves information for each IP from abuseIPDB.

       Displays: essential details for each IP address, including its public accessibility, geographic location,
        ISP, and abuse confidence score,"""

    current_connections = get_network_connections()
    unique_ips = {conn['remote_ip'] for conn in current_connections}
    print('Currently active connections list')
    for ip in unique_ips:
        result = check_ip_threat(ip)
        df = pd.DataFrame(result)
        print("-----------------------------------------------------------------")
        print(df)

def display_historical_connections():
    """Retrieves information for each IP from abuseIPDB.

      Displays: essential details for each IP address, including its public accessibility, geographic location,
       ISP, and abuse confidence score,"""

    unique_ips = get_historical_connections()
    print('Connections from the past list')
    for ip in unique_ips:
        result = check_ip_threat(ip)
        df = pd.DataFrame(result)
        print("-----------------------------------------------------------------")
        print(df)

