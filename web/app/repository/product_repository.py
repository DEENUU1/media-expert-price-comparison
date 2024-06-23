from typing import List, Optional

from models.product import Product
from config.database import get_collection
from bson import ObjectId


async def get_product_list() -> List[Product]:
    collection = get_collection("products")

    cursor = collection.find()
    products = await cursor.to_list(length=None)
    return [Product(**product) for product in products]


async def get_product(product_id: str) -> Optional[Product]:
    collection = get_collection("products")

    if not await product_exists(product_id):
        return None
    product = await collection.find_one({"_id": ObjectId(product_id)})
    return Product(**product) if product else None


async def product_exists(product_id: str) -> bool:
    collection = get_collection("products")

    product = await collection.find_one({"_id": ObjectId(product_id)})
    return bool(product)
