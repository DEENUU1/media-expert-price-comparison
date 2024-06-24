from typing import List
from config.database import get_collection


class SourceRepository:
    def __init__(self, collection: str = "sources"):
        self.collection = get_collection(collection)

    def get_sources(self) -> List[str]:
        sources = self.collection.find()
        return [source.get("url") for source in sources]
