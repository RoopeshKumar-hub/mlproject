import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongodb_uri)

db = client["mlproject_db"]
collection = db["predictions"]


def save_prediction(data):
    collection.insert_one(data)
    print("Prediction saved successfully!")


def get_predictions():
    predictions = collection.find().sort("_id", -1)
    return list(predictions)