import requests
import json
from dotenv import load_dotenv
import os
import util

def scrape_news(query, sites):
    #sites = [util.renameSourceForSearch(site) for site in sites]

    '''returns 100 articles searching for query from certain sites
    currently only changes news_data.json and returns the path'''
    api_key = os.getenv('MEDIA_STACK_KEY')
    #api_key = 'c69425308e63c259754667ba581bf645'
    url = 'http://api.mediastack.com/v1/news'
    sources = ','.join(sites)
    print(sources)
    #'cnn,bbc,foxnews,nytimes,time,guardian,nbc'

    params = {
        'access_key': api_key,
        'keywords': query,
        'sort': 'published_desc',
        'limit': 100,
        'sources' : sources,
        #'categories' : 'general',  save for TESTING
        'languages': 'en','-es'
        'date':'2024-01-01,2025-01-25',
    }

    response = requests.get(url=url,params=params)

    with open('news_data.json', 'w') as file:
        json.dump(response.json(), file, indent=4)


    return response.json()
