from flask import Flask, render_template, request, jsonify
import json
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

from flask import Flask, request, jsonify, render_template
import random  # For demo purposes

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

    model_result = model.get_sentiments(grabber_result)
    print(model_result)
    
    sentiment_totals = {util.renameSource(key) : model_result[key]['average'] for key in model_result.keys()}
    print("final",sentiment_totals)

    #Remove Empty Function: If it's not present, then remove it from sites
    sites = [i for i in sites if i in sentiment_totals]
    scores = []
    for i in sentiment_totals:
        scores.append((sentiment_totals[i])*5)

    print(sites)

    return jsonify({
        'query': query,
        'sites': sites,
       'scores': scores
     })

if __name__ == '__main__':
    app.run(debug=True)