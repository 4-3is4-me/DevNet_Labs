# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = 'NTY1Y2I2ODctMGFiOC00ODkxLWJlZDItMzUzZThiNGY3ZjBlNWMxYjQ3ZmQtZjBi_PE93_230463a1-5812-4f42-9411-a7901256c3a1'

url = 'https://webexapis.com/v1/people/'

# headers
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type':'application/json'}

# params
#params = {
#    'email': 'user@example.com'}
params = {
    'displayName': 'Tim',
    'max': '10'}


response = requests.get(url, headers=headers, params=params)
print(json.dumps(response.json(), indent=4))


'''
jsonresponse = response.json()
person_id = '{}'.format(jsonresponse['items'][0]['id'])
#print(person_id)

idparams = {
    'id': person_id}

idresponse = requests.get(url, headers=headers, params=idparams)
print(json.dumps(idresponse.json(), indent=4))
'''