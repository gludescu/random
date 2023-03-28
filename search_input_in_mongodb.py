"""
This script demonstrates how to connect to a MongoDB database, search for documents containing a specific word, and print the results. The script uses the pymongo library to establish a connection with a MongoDB instance and perform the search operation.

Usage:

1. Ensure that you have MongoDB installed and running on your machine, and the pymongo library installed.
2. Replace the 'localhost' and 27017 in the MongoDB() instantiation with your MongoDB host and port, if different.
3. Replace 'l' in the mongodb.search() function call with your target database name and collection name, respectively.
4. Run the script.
5. Enter the search word when prompted.

How the script works:

The script defines a MongoDB class that initializes a MongoClient instance using the provided host and port.
The search() method of the class takes a database name, collection name, and search word as input, and searches the collection for documents containing the search word (case-insensitive) in the 'text' field.
The script then creates an instance of the MongoDB class, prompting the user to input a search word.
The script performs the search in the specified database and collection, and prints the documents containing the search word.
Example:
What to search? Apple
{'_id': ObjectId('1234567890abcdef12345678'), 'text': 'Apple is a famous tech company.'}
{'_id': ObjectId('1234567890abcdef12345679'), 'text': 'An apple a day keeps the doctor away.'}
"""


from pymongo import MongoClient


class MongoDB:
    def __init__(self, host, port):
        self.client = MongoClient(host, port)

    def search(self, db_name, collection_name, search_word):
        db = self.client[db_name]
        collection = db[collection_name]
        return collection.find({'text': {'$regex': search_word, '$options': 'i'}})


# Create an instance of the MongoDB class.
mongodb = MongoDB('localhost', 27017)

# Enter what to search.
word = input("What to search? ")

# Search for the word entered in the "l" collection of the "l" database.
results = mongodb.search('l', 'l', f'{word}')

# Print the documents.
for result in results:
    print(result)
