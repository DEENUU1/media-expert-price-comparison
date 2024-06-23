from models.price import Price
from models.product import Product
from config.database import get_collection


class ProductRepository:
    def __init__(self, collection: str = "products"):
        self.collection = get_collection(collection)

    def create_product(self, product: Product) -> str:
        if self.product_exists_by_shop_id(product.shop_id):
            self.add_price_to_existing_product(product.shop_id, product.prices[0])
            return str(product.shop_id)
        product = self.collection.insert_one(product.dict())
        return str(product.inserted_id)

    def product_exists_by_shop_id(self, shop_id: int) -> bool:
        product = self.collection.find_one({"shop_id": shop_id})
        return product is not None

    def get_product_by_shop_id(self, shop_id: int) -> Product:
        product = self.collection.find_one({"shop_id": shop_id})
        return Product(**product) if product else None

    def add_price_to_existing_product(self, shop_id: int, new_price: Price):
        existing_product = self.get_product_by_shop_id(shop_id)
        if existing_product:
            existing_product.prices.append(new_price)
            self.collection.update_one(
                {"shop_id": shop_id},
                {"$set": {"prices": [price.dict() for price in existing_product.prices]}}
            )
