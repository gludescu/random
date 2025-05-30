import base64
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("ENCRYPTION_KEY").encode()
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

def encrypt_base64(text, key):
    combined = key + text.encode()
    return base64.b64encode(combined).decode()

client = MongoClient(MONGO_URI)
collection = client[DATABASE_NAME][COLLECTION_NAME]

for doc in collection.find():
    try:
        if isinstance(doc['text'], str) and not doc['text'].startswith(base64.b64encode(key).decode()[:5]):
            encrypted_text = encrypt_base64(doc['text'], key)
            collection.update_one({'_id': doc['_id']}, {'$set': {'text': encrypted_text}})
    except:
        continue