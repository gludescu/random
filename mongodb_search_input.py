from pymongo import MongoClient
from dotenv import load_dotenv
import os


class MongoDB:
    def __init__(self, mongo_srv):
        self.client = MongoClient(mongo_srv)

    def search(self, db_name, collection_name, search_word):
        db = self.client[db_name]
        collection = db[collection_name]
        return collection.find({'text': {'$regex': search_word, '$options': 'i'}})


# Enter what to search.
word = input("What to search? ")

# Load the environment variables.
load_dotenv()

# Get the environment variables.
database_name = os.getenv('DATABASE_NAME')
collection_name = os.getenv('COLLECTION_NAME')
mongo_uri = os.getenv('MONGO_URI')

# Create an instance of the MongoDB class.
mongodb = MongoDB(mongo_uri)

# Search for the word entered in the "COLLECTION_NAME" collection of the "DATABASE_NAME" database.
results = mongodb.search(database_name, collection_name, f'{word}')

# Print the documents.
for result in results:
    print(result)
