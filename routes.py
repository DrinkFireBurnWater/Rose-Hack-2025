from flask import current_app as app
from flask import render_template, request, jsonify, make_response


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/test", methods = ['POST'])
def test():
    test_dict = {'test': 'test'}
    test_response = make_response(jsonify(test_dict))
    test_response.status_code = 200
    return test_response


if __name__ == '__main__':
    app.run(debug=True)