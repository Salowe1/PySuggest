from flask import Flask, jsonify, request
from pymongo import MongoClient

# Set up Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['techdoc_scraper']
collection = db['python_tutorials']

@app.route('/')
def home():
    return """
    Welcome to the TechDoc Scraper API<br><br>
    Use the /tutorials endpoint to search for documentation.
    """

@app.route('/tutorials', methods=['GET'])
def get_tutorials():
    query = request.args.get('query')
    platform = request.args.get('platform')
    
    # Create search filter
    search_filter = {}
    if query:
        search_filter["title"] = {"$regex": query, "$options": "i"}
    if platform:
        search_filter["platform"] = platform
    
    # Fetch tutorials from MongoDB
    results = collection.find(search_filter)
    tutorials = [{"title": doc["title"], "link": doc["link"], "platform": doc.get("platform")} for doc in results]
    
    return jsonify(tutorials)

if __name__ == "__main__":
    app.run(debug=True)
