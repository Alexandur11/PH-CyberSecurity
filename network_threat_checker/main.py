from network_threat_checker.network import get_network_connections
from network_threat_checker.threat_intelligence import check_ip_threat
import pandas as pd



connections = get_network_connections()
unique_ips = {conn['remote_ip'] for conn in connections}

for ip in unique_ips:
    result = check_ip_threat(ip)
    df = pd.DataFrame(result)
    print("-----------------------------------------------------------------")
    print(df)



