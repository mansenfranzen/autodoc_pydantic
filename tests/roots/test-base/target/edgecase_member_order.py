"""Module doc string."""

from pydantic import BaseModel


class C(BaseModel):
    """Class C"""
    field: int


class D:
    """Class D"""
    field: int = 1


class A(BaseModel):
    """Class A"""
    field: int


class B:
    """Class B"""
    field: int = 1
