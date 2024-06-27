from motor.motor_asyncio import AsyncIOMotorClient

from .settings import settings
import logging
from typing import Any, Mapping, Union

from pymongo import MongoClient
from pymongo.database import Database

logger = logging.getLogger(__name__)


def get_db_async() -> Any:
    try:
        client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
        client.admin.command("ping")
        logger.info("Pinged your deployment. You successfully connected to MongoDB!")
        database = client[settings.MONGO_DATABASE_NAME]
        return database
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        return None


def get_collection(collection_name: str) -> Any:
    try:
        db = get_db_async()
        if db is None:
            raise ValueError("Database connection failed")
        collection = db[collection_name]
        if collection is None:
            raise ValueError(f"Collection '{collection_name}' not found")
        return collection
    except KeyError:
        logger.error(f"Invalid collection name: {collection_name}")
        raise KeyError("Invalid collection name")
    except Exception as e:
        logger.error(f"Error getting collection: {e}")
        return None


def get_db_sync() -> Database[Union[Mapping[str, Any], Any]]:
    client = MongoClient(settings.MONGO_CONNECTION_STRING)
    return client[settings.MONGO_DATABASE_NAME]


def get_collection_sync(collection_name: str) -> Any:
    try:
        return get_db_sync()[collection_name]
    except KeyError:
        logger.error(f"Invalid collection name: {collection_name}")
        raise KeyError("Invalid collection name")
    except Exception as e:
        logger.error(f"Error getting collection: {e}")
        return None
