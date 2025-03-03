from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

Mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(Mongo_url)

db = client['fastapi_db']

students_collection = db['students']
