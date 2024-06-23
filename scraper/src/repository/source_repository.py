from typing import List

from models.source import Source
from config.database import get_collection


class SourceRepository:
    def __init__(self, collection: str = "sources"):
        self.collection = get_collection(collection)

    def get_sources(self) -> List[Source]:
        sources = self.collection.find()
        return [Source(**source) for source in sources]
