# api.py

from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client['techdoc_scraper']
collection = db['mdn_js_tutorials']

@app.route('/')
def home():
    return "<h1>Welcome to the TechDoc Scraper API</h1><p>Use the /tutorials endpoint to search for documentation.</p>"

@app.route('/tutorials', methods=['GET'])
def get_tutorials():
    query = request.args.get('query')
    if query:
        results = collection.find({"title": {"$regex": query, "$options": "i"}})
    else:
        results = collection.find()
    tutorials = [{"title": doc["title"], "link": doc["link"]} for doc in results]
    return jsonify(tutorials)

if __name__ == "__main__":
    app.run(debug=True)
