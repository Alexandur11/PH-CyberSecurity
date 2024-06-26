import subprocess
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
