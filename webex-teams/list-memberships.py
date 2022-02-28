# Fill in this file with the membership code from the Webex Teams exercise
import json
import requests

access_token = 'NTY1Y2I2ODctMGFiOC00ODkxLWJlZDItMzUzZThiNGY3ZjBlNWMxYjQ3ZmQtZjBi_PE93_230463a1-5812-4f42-9411-a7901256c3a1'

url = 'https://webexapis.com/v1/memberships/'

# headers
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type':'application/json'}
# params
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vYmU5ZDAxYjAtODBmYi0xMWVjLTljZjctMDE4MDc5NTEwOGE2'
params = {'roomId': room_id}

response = requests.get(url, headers=headers, params=params)
print(json.dumps(response.json(), indent=4))