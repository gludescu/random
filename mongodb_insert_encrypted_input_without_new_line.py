from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from zoneinfo import ZoneInfo
import os
import base64


def connect_to_mongodb(database_name, collection_name, mongo_uri):
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    return client, collection


def encrypt_base64(text, key):
    combined = key + text.encode()
    encoded = base64.b64encode(combined).decode()
    return encoded


def create_document(input_data):
    key = os.getenv("ENCRYPTION_KEY").encode()
    encrypted_text = encrypt_base64(input_data, key)
    doc = {
        'text': encrypted_text,
        'timestamp': datetime.now(ZoneInfo("Europe/Bucharest"))
    }
    return doc


def insert_documents(collection):
    while True:
        input_data = input()
        if input_data.lower() == 'e':
            break

        doc = create_document(input_data)
        collection.insert_one(doc)


def main():
    load_dotenv()

    database_name = os.getenv('DATABASE_NAME')
    collection_name = os.getenv('COLLECTION_NAME')
    mongo_uri = os.getenv('MONGO_URI')

    client, collection = connect_to_mongodb(
        database_name, collection_name, mongo_uri)
    insert_documents(collection)
    client.close()


if __name__ == '__main__':
    main()
