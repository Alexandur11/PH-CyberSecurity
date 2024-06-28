import requests
from dotenv import dotenv_values
env_vars = dotenv_values()
ABUSE_IPDB_KEY = env_vars.get('ABUSEIPDB_KEY')

def check_ip_threat(ip):

    """Retrieves information from abusepidb.com with the use of API key.

       returns:
            information about the IP address’s threat level and related details."""

    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '11'
    }
    headers = {
        'Accept': 'application/json',
        'Key': ABUSE_IPDB_KEY
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
