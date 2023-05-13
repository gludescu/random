"""
This script demonstrates how to connect to a MongoDB database, search for documents containing a specific word, and print the results. The script uses the pymongo library to establish a connection with a MongoDB instance and perform the search operation.

Usage:

1. Ensure that you have MongoDB installed and running on your machine, and the pymongo library installed.
2. Replace the 'localhost' and 27017 in the MongoDB() instantiation with your MongoDB host and port, if different.
3. Replace 'l' in the mongodb.search() function call with your target database name and collection name, respectively.
4. Run the script.
5. Enter the search word when prompted.

How the script works:

- The script defines a MongoDB class that initializes a MongoClient instance using the provided host and port.
- The search() method of the class takes a database name, collection name, and search word as input, and searches the collection for documents containing the search word (case-insensitive) in the 'text' field.
- The script then creates an instance of the MongoDB class, prompting the user to input a search word.
- The script performs the search in the specified database and collection, and prints the documents containing the search word.

Example:

What to search? Apple
{'_id': ObjectId('1234567890abcdef12345678'), 'text': 'Apple is a famous tech company.'}
{'_id': ObjectId('1234567890abcdef12345679'), 'text': 'An apple a day keeps the doctor away.'}
"""


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
