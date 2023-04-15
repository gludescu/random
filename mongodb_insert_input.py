"""
This script demonstrates how to connect to a MongoDB database and insert documents into a collection using the pymongo library. The script establishes a connection with a MongoDB instance, takes input from the user, and inserts the data into the specified collection.

Usage:

Ensure that you have MongoDB installed and running on your machine, and the pymongo library installed.
Replace 'l' in the __init__ method of the Database class with your target database and collection names, if different.
Run the script.
Enter text for the entry when prompted. To quit, type 'q' and press Enter.
How the script works:

The script defines a Database class that initializes a MongoClient instance, connects to a database, and selects a collection.
The insert_data() method of the class takes text input from the user and inserts it into the collection as a new document with a 'date' field containing the current timestamp and a 'text' field containing the user-provided text.
The script creates an instance of the Database class and calls the insert_data() method to start taking user input and inserting it into the collection.
Example:
Entry: This is a sample entry.
Entry: Another entry for the collection.
Entry: q
Bye!
"""


import pymongo
from datetime import datetime


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.l
        self.data = self.db.l

    def insert_data(self):
        while True:
            text = input("Entry: ")

            if text == "q":
                print("Bye!")
                break

            if not text:
                print("Write something...")
                continue

            entry = {"date": datetime.now(), "text": text}
            self.data.insert_one(entry)


if __name__ == "__main__":
    db = Database()
    db.insert_data()
