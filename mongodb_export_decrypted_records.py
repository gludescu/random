import base64
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import json_util

load_dotenv()
KEY = os.getenv("ENCRYPTION_KEY").encode()
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

def decrypt_base64(encoded_text, key):
    decoded = base64.b64decode(encoded_text.encode())
    return decoded[len(key):].decode()

client = MongoClient(MONGO_URI)
collection = client[DATABASE_NAME][COLLECTION_NAME]

output = []
for doc in collection.find():
    try:
        doc['text'] = decrypt_base64(doc['text'], KEY)
        output.append(doc)
    except:
        continue

with open("mongodb_dump.json", "w") as f:
    f.write(json_util.dumps(output, indent=2))