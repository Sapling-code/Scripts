import json
from pprint import pprint
with open('output.txt') as data_file:
	data = json.load(data_file)
results = data
for rs in results:
	if rs['positives'] > 8:
		print rs['positives']
		print rs['url']
