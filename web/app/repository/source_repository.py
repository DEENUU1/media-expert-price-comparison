from typing import List

from models.source import SourceInput, SourceOutput
from config.database import get_collection
from fastapi import HTTPException
from bson import ObjectId


async def source_exists_by_url(url: str) -> bool:
    collection = get_collection("sources")

    source = await collection.find_one({"url": url})
    return bool(source)


async def create_source(source: SourceInput) -> SourceOutput:
    collection = get_collection("sources")

    if await source_exists_by_url(source.url):
        raise HTTPException(
            status_code=409, detail=f"Source with url {source.url} already exists"
        )
    result = await collection.insert_one(source.dict())
    return SourceOutput(id=str(result.inserted_id), url=source.url)


async def source_exists_by_id(_id: str) -> bool:
    collection = get_collection("sources")

    source = await collection.find_one({"_id": ObjectId(_id)})
    return bool(source)


async def get_sources() -> List[SourceOutput]:
    collection = get_collection("sources")
    cursor = collection.find()
    sources = await cursor.to_list(length=None)
    return [SourceOutput(id=str(source["_id"]), url=source["url"]) for source in sources]


async def delete_source(source_id: str) -> None:
    collection = get_collection("sources")

    if not await source_exists_by_id(source_id):
        raise HTTPException(status_code=404, detail="Source not found")
    await collection.delete_one({"_id": ObjectId(source_id)})
