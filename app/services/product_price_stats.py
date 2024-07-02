from schemas.product_schemas import ProductOutputSchema


def get_max_product_price(product: ProductOutputSchema) -> float:
    prices = product.prices
    if not prices:
        return 0.0

    return max(price.price for price in prices)


def get_min_product_price(product: ProductOutputSchema) -> float:
    prices = product.prices
    if not prices:
        return 0.0

    return min(price.price for price in prices)


def get_avg_product_price(product: ProductOutputSchema) -> float:
    prices = product.prices
    if not prices:
        return 0.0

    return sum(price.price for price in prices) / len(prices)
