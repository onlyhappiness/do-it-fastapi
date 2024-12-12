from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

# method for start Mongo connection
async def connect_to_mongo(app: FastAPI):
    mongo_uri = os.getenv("MONGO_URI")
    database_name = os.getenv("DATABASE_NAME")
    app.mongodb_client = AsyncIOMotorClient(mongo_uri)
    app.mongodb = app.mongodb_client.get_database(database_name)
    print("MongoDB connected.")


# method to close database connection
async def close_mongo_connect(app: FastAPI):
    app.mongodb_client.close()
    print('Database disconnected')
