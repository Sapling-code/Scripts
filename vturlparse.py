import json
from pprint import pprint
with open('output.txt') as data_file:
	data = json.load(data_file)
results = data
for rs in results:
	if rs['positives'] > 8:
		with open('newoutput.txt','a+') as outfile:
			outfile.write(str(rs['url']))
			outfile.write("\n")
