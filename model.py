#IMPORTS
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    # Decide sentiment as positive, negative, or neutral

    return sentiment_dict['compound']

def getSentiments(data):
    with open(data) as json_file:
        newsdata = json.load(json_file)
    newsdata = dict(newsdata)
    newsdata = newsdata["data"]

    data = []
    copycolumns = ['title', 'source', 'description']
    for article in newsdata:
        filterarticle = {key: article[key] for key in copycolumns}
        filterarticle['source'] = filterarticle['source'].split(" ")[0]
        data.append(filterarticle)


    for article in data:
        score1 = sentiment_scores(article['title'])
        score2 = sentiment_scores(article['description'])
        score = (score1+score2)/2
        article['score'] = score

    totals = dict()

    for article in data:
        score1 = sentiment_scores(article['title'])
        score2 = sentiment_scores(article['description'])
        score = (score1+score2)/2
        article['score'] = score

    for article in data:
        if article['source'] not in totals:
            totals[article['source']] = [0,0]
        #print(article['score'])
        totals[article['source']][0] += article['score']
        #print(totals[article['source']])
        totals[article['source']][1] += 1

    for news in totals:
        totals[news][0] = totals[news][0]/totals[news][1]
        totals[news] = totals[news][0]

    return totals
