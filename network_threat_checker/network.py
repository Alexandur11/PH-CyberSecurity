import subprocess


def get_network_connections():
    result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    connection_info = []
    for line in lines:
        if 'ESTABLISHED' in line or 'LISTEN' in line:
            parts = line.split()
            local_address = parts[3]
            remote_address = parts[4]
            status = parts[5] if len(parts) > 5 else 'LISTEN'

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
