from typing import List

from models.source import SourceInput, SourceOutput
from config.database import get_collection
from fastapi import HTTPException


class SourceRepository:
    def __init__(self, collection: str = "sources"):
        self.collection = get_collection(collection)

    def create_source(self, source: SourceInput) -> SourceOutput:
        if self.source_exists_by_url(source.url):
            raise HTTPException(
                status_code=409, detail=f"Source with url {source.url} already exists"
            )
        result = self.collection.insert_one(source.dict())
        return SourceOutput(id=str(result.inserted_id), url=source.url)

    def source_exists_by_url(self, url: str) -> bool:
        source = self.collection.find_one({"url": url})
        return bool(source)

    def source_exists_by_id(self, _id: str) -> bool:
        source = self.collection.find_one({"_id": _id})
        return bool(source)

    def get_sources(self) -> List[SourceOutput]:
        sources = self.collection.find()
        return [SourceOutput(id=str(source["_id"]), url=source["url"]) for source in sources]

    def delete_source(self, source_id: str) -> None:
        if not self.source_exists_by_id(source_id):
            raise HTTPException(status_code=404, detail="Source not found")
        self.collection.delete_one({"_id": source_id})

