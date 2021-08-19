from pydantic import BaseModel


class MyBase(BaseModel):
    """MyBase"""

    field_on_base: str
    """Base Field"""


class MySubclass(MyBase):
    """MySubClass"""

    field_on_subclass: str
    """Subclass field"""
