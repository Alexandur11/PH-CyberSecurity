import requests
from dotenv import dotenv_values
env_vars = dotenv_values()
ABUSE_IPDB_KEY = env_vars.get('ABUSEIPDB_KEY')

def check_ip_threat(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': ABUSE_IPDB_KEY
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
