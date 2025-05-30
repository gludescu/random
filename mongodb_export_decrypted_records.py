import os
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import json_util
from cryptography.fernet import Fernet

load_dotenv()

fernet = Fernet(os.getenv("ENCRYPTION_KEY"))
mongo_uri = os.getenv("MONGO_URI")
database_name = os.getenv("DATABASE_NAME")
collection_name = os.getenv("COLLECTION_NAME")

client = MongoClient(mongo_uri)
collection = client[database_name][collection_name]

output = []
for doc in collection.find():
    try:
        doc['text'] = fernet.decrypt(doc['text'].encode()).decode()
        output.append(doc)
    except:
        continue

with open("mongodb_dump.json", "w") as f:
    f.write(json_util.dumps(output, indent=2))