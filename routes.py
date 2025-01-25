from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test():
    return render_template('index.html')

from flask import Flask, request, jsonify, render_template
import random  # For demo purposes

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    query = data.get('query', '')
    sites = data.get('sites', [])

    # Simulate sentiment analysis
    sentiment_scores = {
        'cnn': random.uniform(-5, 5),
        'bbc': random.uniform(-5, 5),
        'reuters': random.uniform(-5, 5),
        'nyt': random.uniform(-5, 5),
        'fox': random.uniform(-5, 5),
        'msnbc': random.uniform(-5, 5),
        'ap': random.uniform(-5, 5)
    }

    filtered_scores = [sentiment_scores[site] for site in sites]

    return jsonify({
        'sites': sites,
        'scores': filtered_scores,
        'query': query
    })

if __name__ == '__main__':
    app.run(debug=True)