import base64
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

def decrypt_base64(encoded_text, key):
    decoded = base64.b64decode(encoded_text.encode())
    return decoded[len(key):].decode()

class MongoDB:
    def __init__(self, mongo_srv):
        self.client = MongoClient(mongo_srv)

    def search(self, db_name, collection_name, search_word):
        db = self.client[db_name]
        collection = db[collection_name]
        results = []
        for doc in collection.find():
            try:
                decrypted = fernet.decrypt(doc['text'].encode()).decode()
                if search_word.lower() in decrypted.lower():
                    doc['text'] = decrypted
                    results.append(doc)
            except:
                continue
        return results


word = input("What to search? ")

database_name = os.getenv('DATABASE_NAME')
collection_name = os.getenv('COLLECTION_NAME')
mongo_uri = os.getenv('MONGO_URI')
fernet = Fernet(os.getenv("ENCRYPTION_KEY"))

mongodb = MongoDB(mongo_uri)
results = mongodb.search(database_name, collection_name, word)

for result in results:
    print(f"ID: {result['_id']}")
    print(f"Text: {result['text']}")
    print(f"Timestamp: {result['timestamp']}\n")