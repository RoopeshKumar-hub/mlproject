import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")

if not mongodb_uri:
    print("MONGODB_URI not found in .env file")
    exit()

try:
    client = MongoClient(mongodb_uri)

    client.admin.command("ping")

    print("MongoDB connection successful!")

    db = client["mlproject_db"]
    collection = db["predictions"]

    print("Database:", db.name)
    print("Collection:", collection.name)

    client.close()

except Exception as e:
    print("MongoDB connection failed!")
    print("Error:", e)