"""
This Python script allows you to insert multiple documents into a MongoDB localhost database. Each document will contain user input as 'text' and the current date and time as 'timestamp'. The script uses a loop to continuously prompt the user for input until they choose to exit.

To use the script:

1. Ensure you have the pymongo library installed. If not, install it using the following command:
   pip install pymongo

2. Replace 'your_database_name' and 'your_collection_name' with the appropriate names for your MongoDB database and collection.

3. Run the script. It will prompt you for input. Enter the text you want to store in the 'text' field.

4. Press Enter to insert the document and continue entering more documents.

5. To exit the loop and stop inserting documents, type 'e' and press Enter. The script will print a message indicating that all documents have been inserted successfully.

6. The inserted documents will have the following structure:
   {
       "text": <your_input>,
       "timestamp": <current_date_and_time>
   }

7. To insert more documents, simply run the script again and follow the prompts.
"""


from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os


def connect_to_mongodb(database_name, collection_name, mongo_uri):
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    return client, collection


def create_document(input_data):
    doc = {
        'text': input_data,
        'timestamp': datetime.utcnow()
    }
    return doc


def insert_documents(collection):
    while True:
        input_data = input("Enter the text, or type 'e' to exit:\n")
        if input_data.lower() == 'e':
            break

        doc = create_document(input_data)
        collection.insert_one(doc)
    print("All documents inserted successfully.")


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
