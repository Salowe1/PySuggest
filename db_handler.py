from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['techdoc_scraper']
collection = db['python_tutorials']

def save_to_db(data):
    if data:
        collection.insert_many(data)
