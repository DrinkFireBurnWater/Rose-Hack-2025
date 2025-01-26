import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import heapq


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


    top3heap = []
    lowest3heap = []

    #scores it
    for index, article in enumerate(article_dict_list):
        score1 = sentiment_scores(article['title'])
        score2 = sentiment_scores(article['description'])
        score = (score1+score2)/2
        article['score'] = score

        heapq.heappush(top3heap, (score,index))
        heapq.heappush(lowest3heap, (-score, index))

        if len(top3heap) > 3:
            heapq.heappop(top3heap)
        if len(lowest3heap) > 3:
            heapq.heappop(lowest3heap)


        top3_indexes = [index for _, index in sorted(top3heap, reverse = True)]
        lowest3_indexes = [index for _, index in sorted(lowest3heap)]

    top3_articles = [news_data[x] for x in top3_indexes]
    lowest3_articles = [news_data[x] for x in lowest3_indexes]


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

    return analyzed_sources,top3_articles, sorted(top3heap, reverse = True), lowest3_articles, sorted(lowest3heap)

def get_bluesky_sentiments(json_or_path, ispath = False):
    if ispath:
        with open(json_or_path) as json_file:
            data = json.load(json_file)
    else:
        data = json_or_path

    print(data)
    data = dict(data)
    text_data = []
    for post in data['posts']:
        text_data.append(post['record']['text'])
    scores = []
    for post in text_data:
        scores.append(sentiment_scores(post))

    avg = sum(scores) / len(scores)

    return avg


