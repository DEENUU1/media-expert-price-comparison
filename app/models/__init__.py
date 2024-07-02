from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .source import Source
from .price import Price
from .product import Product