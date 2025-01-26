import grabber
from dotenv import load_dotenv

query = 'climate'
sources = 'nbc'

print(grabber.scrape_news(query, sources))