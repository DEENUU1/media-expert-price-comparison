from typing import List, Optional

from models.product import Product
from config.database import get_collection
from bson import ObjectId


async def get_product_list() -> List[Product]:
    collection = get_collection("products")

    cursor = collection.find()
    products = await cursor.to_list(length=None)

    valid_products = []
    for product in products:
        if '_id' in product:
            product['id'] = str(product['_id'])
            del product['_id']
        valid_products.append(Product(**product))

    return valid_products


async def get_product(product_id: str) -> Optional[dict]:
    collection = get_collection("products")

    if not await product_exists(product_id):
        return None
    product = await collection.find_one({"_id": ObjectId(product_id)})
    if '_id' in product:
        product['id'] = str(product['_id'])
        del product['_id']
    return Product(**product).dict() if product else None


async def product_exists(product_id: str) -> bool:
    collection = get_collection("products")

    product = await collection.find_one({"_id": ObjectId(product_id)})
    return bool(product)
