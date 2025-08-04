# db.py
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGO_DB, MONGO_URI
from pymongo.errors import ConnectionFailure

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]

class Database:
    client: AsyncIOMotorClient = None
    db = None


db_instance = Database()


async def connect_to_mongo():
    try:
        db_instance.client = AsyncIOMotorClient(MONGO_URI)
        db_instance.db = db_instance.client[MONGO_DB]
        await db_instance.db.command("ping")
        print("Connected to MongoDB!")
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")


async def close_mongo_connection():
    if db_instance.client:
        db_instance.client.close()
        print("MongoDB connection closed.")

def get_user_collection():
    if db_instance.db is not None:
        return db_instance.db["users"]
    else:
        raise Exception("Database connection not established.")
    
def get_profile_info_collection():
    if db_instance.db is not None:
        return db_instance.db["profile_info"]
    else:
        raise Exception("Database connection not established.")

def get_skill_collection():
    if db_instance.db is not None:
        return db_instance.db["skills"]
    else:
        raise Exception("Database connection not established.")

def get_project_collection():
    if db_instance.db is not None:
        return db_instance.db["projects"]
    else:
        raise Exception("Database connection not established.")