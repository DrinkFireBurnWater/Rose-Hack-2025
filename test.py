import requests
import json
import datetime

url = 'https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts'
search_term = 'trump'
params = {
    'q': search_term,
    'sort': 'top',
    'since': '2025-01-01T00:00:00.000Z',
    'until': '2025-01-25T00:00:00.000Z',
    'lang' : 'en',
    'limit': '50'
}

response = requests.get(url = url, params = params)
with open('bluesky_data.json', 'w') as file:
    json.dump(response.json(), file, indent = 4)

print(dict(response.json()))