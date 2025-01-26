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

def get_sentiments(json_or_path, ispath = False):
    if ispath:
        with open(json_or_path) as json_file:
            news_data = json.load(json_file)
    else:
        news_data = json_or_path

    news_data = dict(news_data)
    news_data = news_data["data"]

    #filters for needed text
    article_dict_list = []
    text_categories = ['title', 'source', 'description']
    for article in news_data:
        article_dict = {key: article[key] for key in text_categories}
        article_dict['source'] = article_dict['source'].split(" ")[0]
        if article_dict['source'] == 'The': article_dict['source'] = "nytimes"
        article_dict_list.append(article_dict)

    #scores it
    for article in article_dict_list:
        score1 = sentiment_scores(article['title'])
        score2 = sentiment_scores(article['description'])
        score = (score1+score2)/2
        article['score'] = score

    analyzed_sources = dict()

    #adds it up for multiple articles
    for article in article_dict_list:
        news_source = article['source']
        if news_source not in analyzed_sources:
            analyzed_sources[news_source] = {'total': 0, 'count':0}
        analyzed_sources[news_source]['total'] += article['score']
        analyzed_sources[news_source]['count'] += 1

    #averages it
    for news_source in analyzed_sources:
        total = analyzed_sources[news_source]['total']
        count = analyzed_sources[news_source]['count']
        analyzed_sources[news_source]['average'] = total/count

    return analyzed_sources
