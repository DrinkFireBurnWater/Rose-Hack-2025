import requests
import json

def scrapeNews(query,sites):
    '''returns 100 articles searching for query from certain sites
    currently only changes newsdata.json and returns the path'''
    #harded coded api key :hmm:
    api_key = '11c95fbfdd920bf9ef287b95a3bb92fe'
    url = 'http://api.mediastack.com/v1/news'
    sources = ','.join(sites)
    print(sources)
    #'cnn,bbc,reuters,foxnews,nytimes,mnbc,ap'
    #cnn,bbc,latimes,foxnews,nytimes

    params = {
        'access_key': api_key,
        'keywords': query,
        'sort': 'published_desc',
        'limit': 100,
        'sources' : sources,
        #'categories' : 'general', 
        'languages': 'en','-es'
        'date':'2024-01-01,2025-01-25',
    }

    response = requests.get(url=url,params=params)
    print(response.json())

    with open('newsdata.json', 'w') as file:
        json.dump(response.json(), file, indent=4)

    return 'newsdata.json'
