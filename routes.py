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
    print("Received data:", data)  # Debugging incoming JSON

    query = data.get('query', '')
    sites = data.get('sites', [])
    print("Query:", query, type(query))         # Debugging query
    print("Sites:", sites, type(sites))         # Debugging sites

    grabber_result = grabber.scrapeNews(query,sites)
    print(grabber_result)

    model_result = model.getSentiments(grabber_result)
    print("final",model_result)

    filtered_scores = [model_result[sites] for site in sites]

        # Step 5: Return the final result
    return jsonify({
        'query': query,
        'sites': sites,
       'sentiment_totals': filtered_scores
     })



if __name__ == '__main__':
    app.run(debug=True)