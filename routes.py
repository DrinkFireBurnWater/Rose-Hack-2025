from flask import Flask, render_template, request, jsonify
import json
import grabber
import model

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
    print("Query:", query, type(query))
    print("Sites:", sites, type(sites))

    grabber_result = grabber.scrapeNews(query,sites)
    print(f'grabber_result:{grabber_result}')

    model_result = model.get_sentiments(grabber_result)
    sentiment_totals = {key : model_result[key]['average'] for key in model_result.keys()}
    print("final",model_result)

    return jsonify({
        'query': query,
        'sites': sites,
       'sentiment_totals': sentiment_totals
     })

if __name__ == '__main__':
    app.run(debug=True)