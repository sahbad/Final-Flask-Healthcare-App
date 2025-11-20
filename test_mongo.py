from pymongo import MongoClient
from config import MONGO_URI

print("=== Starting Mongo test script ===")
print("MONGO_URI is:", MONGO_URI)

client = MongoClient(MONGO_URI)

# Use the same DB and collection names you see in Atlas
db = client["healthcare_survey"]
collection = db["responses"]

print("Databases on server:", client.list_database_names())
print("Collections in healthcare_survey:", db.list_collection_names())

try:
    result = collection.insert_one({"test_connection": True})
    print("Inserted test document with _id:", result.inserted_id)
except Exception as e:
    print("ERROR inserting test document:", e)

print("=== Finished Mongo test script ===")
