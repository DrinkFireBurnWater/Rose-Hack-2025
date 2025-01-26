from flask import Flask, render_template, request, jsonify
import grabber
import model
import util
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods = ['POST'])
def test():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    print("data:", data)

    query = data.get('query', '')
    sites = data.get('sites', [])
    print("Query:", query)
    print("Sites:", sites)

    grabber_result = grabber.scrape_news(query, sites)
    print(f'grabber_result:{grabber_result}')

    model_result, top3, top3_scores, bottom3, bot3_scores = model.get_sentiments(grabber_result)
    print(model_result)
    
    sentiment_totals = {util.renameSource(key) : model_result[key]['average'] for key in model_result.keys()}
    print("final",sentiment_totals)

    sites = [i for i in sites if i in sentiment_totals]
    scores = []
    for i in sentiment_totals:
        scores.append((sentiment_totals[i])*5)

    print(sites)

    blue_sky_result = grabber.scrape_bluesky(query)
    blue_sky_sent = model.get_bluesky_sentiments(blue_sky_result) * 5

    top3_titles = [x['title'] for x in top3]
    top3_source = [x['source'] for x in top3]
    bottom3_titles = [x['title'] for x in bottom3]
    bottom3_source = [x['source'] for x in bottom3]
    top3_scores = [x[0] * 5 for x in top3_scores]
    bot3_scores = [x[0] * -5 for x in bot3_scores]
    print(bot3_scores)
    print(bottom3_source)


    return jsonify({
        'query': query,
        'sites': sites,
       'scores': scores,
        'blue_sky_score' : blue_sky_sent,
        'top3_titles':top3_titles,
        'top3_source' : top3_source,
        'top3_scores' : top3_scores,
        'bottom3_titles' : bottom3_titles,
        'bottom3_source' : bottom3_source,
        'bot3_scores' : bot3_scores

     })

if __name__ == '__main__':
    app.run(debug=True)