from typing import Any, Mapping, Union

from pymongo import MongoClient
from pymongo.database import Database

from .settings import settings
import logging


logger = logging.getLogger(__name__)


def get_db() -> Database[Union[Mapping[str, Any], Any]]:
    client = MongoClient(settings.MONGO_CONNECTION_STRING)
    return client[settings.MONGO_DATABASE_NAME]


def get_collection(collection_name: str) -> Any:
    try:
        return get_db()[collection_name]
    except KeyError:
        logger.error(f"Invalid collection name: {collection_name}")
        raise KeyError("Invalid collection name")
    except Exception as e:
        logger.error(f"Error getting collection: {e}")
        return None
