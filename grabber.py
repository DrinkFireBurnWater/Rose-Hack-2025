import requests
import json
#import query from 

#Temp Query
query = "environment"

url = 'https://newsapi.org/v2/everything?'

params = {
    'q': query,
    'from': '2024-12-25',
    'to': '2025-01-25',
    'sortBy': 'popularity',
    'pageSize': 100,
    'apiKey': '7934d4a579f84cac8bf18ff57452553b'
}

response = requests.get(url=url,params=params)

print(response.json())

with open('newsdata.json', 'w') as file:
    json.dump(response.json(), file, indent=4)
