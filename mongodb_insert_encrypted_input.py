from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from zoneinfo import ZoneInfo
import os
from cryptography.fernet import Fernet


def connect_to_mongodb(database_name, collection_name, mongo_uri):
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    return client, collection


def create_document(inputs):
    fernet = Fernet(os.getenv("ENCRYPTION_KEY"))
    text = "\n".join(inputs)
    encrypted_text = fernet.encrypt(text.encode()).decode()
    doc = {
        'text': encrypted_text,
        'timestamp': datetime.now(ZoneInfo("Europe/Bucharest"))
    }
    return doc


def insert_documents(collection):
    inputs = []
    while True:
        input_data = input()
        if input_data.lower() == 'e':
            break
        elif input_data.lower() == 'i':
            if inputs:
                doc = create_document(inputs)
                collection.insert_one(doc)
                inputs = []
        else:
            inputs.append(input_data)


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
