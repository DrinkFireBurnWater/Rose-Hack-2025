from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

with open('temp.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    # Decide sentiment as positive, negative, or neutral

    return sentiment_dict['compound']

print(sentiment_scores(lines))