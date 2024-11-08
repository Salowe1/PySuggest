# db_handler.py

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['techdoc_scraper']
collection = db['mdn_js_tutorials']

def save_to_db(data):
    if data:
        collection.insert_many(data)
