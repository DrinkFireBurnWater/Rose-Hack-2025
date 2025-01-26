import requests
import json
from dotenv import load_dotenv
import os

def scrape_news(query, sites):
    '''returns 100 articles searching for query from certain sites
    currently only changes news_data.json and returns the path'''
    api_key = os.getenv('MEDIA_STACK_KEY')
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

    with open('news_data.json', 'w') as file:
        json.dump(response.json(), file, indent=4)


    return response.json()
