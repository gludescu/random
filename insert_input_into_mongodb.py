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
