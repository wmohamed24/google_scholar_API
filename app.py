from flask import Flask, request, jsonify
from get_articles import retrieve_articles
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/get_articles', methods=['GET'])
def get_articles():
    # Extract string from request
    data = request.args
    search_query = data['search_query']

    # Call the process_input function from processor.py
    articles = retrieve_articles(search_query)

    # Return the array as a JSON response
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
