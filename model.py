#IMPORTS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

with open('newsdata.json') as json_file:
    newsdata = json.load(json_file)
newsdata = dict(newsdata)
newsdata = newsdata["data"]

data = []
copycolumns = ['title', 'source', 'description']
for article in newsdata:
    filterarticle = {key: article[key] for key in copycolumns}
    data.append(filterarticle)

#SENTIMENT FUNCTION
def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    # Decide sentiment as positive, negative, or neutral

    return sentiment_dict['compound']

for article in data:
    score1 = sentiment_scores(article['title'])
    score2 = sentiment_scores(article['description'])
    score = (score1+score2)/2
    article['score'] = score
