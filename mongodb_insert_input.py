from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from zoneinfo import ZoneInfo
import os


def connect_to_mongodb(database_name, collection_name, mongo_uri):
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    return client, collection


# Include every new line in the same record.
def create_document(inputs):
    doc = {
        'text': "\n".join(inputs),
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


# Insert every line as a new record.
# def create_document(input_data):
#     doc = {
#         'text': input_data,
#         'timestamp': datetime.now(ZoneInfo("Europe/Bucharest"))
#     }
#     return doc


# def insert_documents(collection):
#     while True:
#         input_data = input()
#         if input_data.lower() == 'e':
#             break
#
#         doc = create_document(input_data)
#         collection.insert_one(doc)


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
