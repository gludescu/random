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
