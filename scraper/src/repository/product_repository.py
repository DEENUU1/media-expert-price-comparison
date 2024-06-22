from typing import List
from models.product import Product
from config.database import get_collection


class ProductRepository:
    def __init__(self, collection: str = "products"):
        self.collection = get_collection(collection)

    def create_product(self, product: Product) -> str:
        product = self.collection.insert_one(product.dict())
        return str(product.inserted_id)

    def get_product_list(self) -> List[Product]:
        products = self.collection.find()
        return [Product(**product) for product in products]
