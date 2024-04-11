from __future__ import annotations

from pydantic import BaseModel


class ProductCategory(BaseModel):
    """Product category representation."""

    id: int
    name: str


class Product(BaseModel):
    """Product representation."""

    id: int
    name: str
    category: ProductCategory


class Customer(BaseModel):
    """Customer representation."""

    id: int
    name: str


class Order(BaseModel):
    """Order representation."""

    id: int
    customer: Customer
    products: list[Product]
    total: float
