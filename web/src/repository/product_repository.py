from typing import List, Optional

from models.product import Product
from config.database import get_collection


class ProductRepository:
    def __init__(self, collection: str = "products"):
        self.collection = get_collection(collection)

    def get_product_list(self) -> List[Product]:
        products = self.collection.find()
        return [Product(**product) for product in products]

    def get_product(self, product_id: str) -> Optional[Product]:
        if not self.product_exists(product_id):
            return None
        product = self.collection.find_one({"_id": product_id})
        return Product(**product) if product else None

    def product_exists(self, product_id: str) -> bool:
        product = self.collection.find_one({"_id": product_id})
        return bool(product)
