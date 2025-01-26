from flask import Flask, render_template, request, jsonify
import json
import subprocess
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
    print(grabber_result[0])

    model_result = model.getSentiments(grabber_result)

    sentiment_totals = json.loads(model_result.stdout)

        # Step 5: Return the final result
    return jsonify({
        'query': query,
        'sites': sites,
       'sentiment_totals': sentiment_totals
     })



if __name__ == '__main__':
    app.run(debug=True)