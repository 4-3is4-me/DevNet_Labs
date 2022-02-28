import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = 'https://192.168.56.101/restconf/data/ietf-interfaces:interfaces'

# dictionary of headers
headers = {'Content-Type': 'application/yang-data+json',
              'Accept': 'application/yang-data+json'}

# tuple of username and password
basicauth = ('cisco', 'cisco123!')

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)

resp_json = resp.json()
print(json.dumps(resp_json, indent=4))
