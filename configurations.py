
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://benjaminjael205_db_user:9zyCwJ6qFNm0fZqB@jael-coder.inomfza.mongodb.net/?appName=Jael-coder"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db
collection = db["todo_data"]


