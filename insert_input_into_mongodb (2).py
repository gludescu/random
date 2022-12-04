# Import the necessary libraries.
from datetime import datetime
from pymongo import MongoClient

# Create a new MongoClient instance.
client = MongoClient()

# Connect to the "l" database.
db = client["l"]

# Use the "l" collection.
collection = db["l"]

while True:
    # Prompt the user for some data.
    data = input("")

    # Break out of the loop if the user enters "q".
    if data.lower() == "q":
        print("Bye!")
        break

    # Insert the data into the collection with the current timestamp.
    result = collection.insert_one({
        "date": datetime.now(),
        "text": data
    })

    # Print the ObjectId of the inserted document.
    print("Inserted document with ObjectId:", result.inserted_id)
