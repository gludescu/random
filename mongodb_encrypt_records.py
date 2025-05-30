import base64
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

fernet = Fernet(os.getenv("ENCRYPTION_KEY"))
mongo_uri = os.getenv("MONGO_URI")
database_name = os.getenv("DATABASE_NAME")
collection_name = os.getenv("COLLECTION_NAME")

def encrypt_base64(text, key):
    combined = key + text.encode()
    return base64.b64encode(combined).decode()

client = MongoClient(mongo_uri)
collection = client[database_name][collection_name]

for doc in collection.find():
    try:
        if isinstance(doc['text'], str):
            encrypted_text = fernet.encrypt(doc['text'].encode()).decode()
            collection.update_one({'_id': doc['_id']}, {'$set': {'text': encrypted_text}})
            print(f"Encrypted {doc['_id']}.")
    except:
        continue