# Fill in this file with the authentication code from the Webex Teams exercise

import requests
import json

access_token = 'NTY1Y2I2ODctMGFiOC00ODkxLWJlZDItMzUzZThiNGY3ZjBlNWMxYjQ3ZmQtZjBi_PE93_230463a1-5812-4f42-9411-a7901256c3a1'

url = 'https://webexapis.com/v1/people/me'

# headers
headers = {
    'Authorization': 'Bearer {}'.format(access_token)}

response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))

