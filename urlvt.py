import requests
import json
params = {'apikey': 'apikey'}
response = requests.post('https://www.virustotal.com/vtapi/v2/url/distribution', params=params)
response_json = response.json()
with open('output.txt','w') as outfile:
	json.dump(response_json, outfile)
