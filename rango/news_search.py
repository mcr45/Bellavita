import requests
import json

apikey="405b78bb676ca97ebe4d1fa84723853b"

'''url = "https://gnews.io/api/v4/search"
parameters={
"q":'Twitter',
"token":apikey,
"lang":'en',
"country":'us',
"max":6}
response=requests.get(url,params=parameters)
print(response.status_code) 
print('siva')
print(response.json()['articles'])'''

def queryt(seq):
	url = "https://gnews.io/api/v4/search"
	parameters={
		"q":seq,
		"token":apikey,
		"lang":'en',
		"country":'us',
		"max":6}
	response=requests.get(url,params=parameters)
	res=response.json()
	results=[]
	for result in res['articles']:
		results.append({'title':result['title'],
		'url':result['url'],
		'par':result['description']
		})
	return results