import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = 'https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback2'

# dictionary of headers
headers = {'Content-Type': 'application/yang-data+json',
                'Accept': 'application/yang-data+json'}

# tuple of username and password
basicauth = ('cisco', 'cisco123!')

# dictionary of data to be sent in the body of the request
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "This is a second loopback interface",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

# send the request
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if (resp.status_code >= 200 and resp.status_code <= 299):
    print("Status OK: {}".format(resp.status_code))
else:
    print("Error: {} \nError Message: {}".format(resp.status_code, resp.json()))
