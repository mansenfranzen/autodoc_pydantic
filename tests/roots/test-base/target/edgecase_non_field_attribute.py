from pydantic import BaseModel
from typing import ClassVar


class ClassAttribute(BaseModel):
    """FooBar."""

    class_attribute: ClassVar[str] = None
    """Dummy"""
