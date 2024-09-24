from pydantic import Field
from pydantic.dataclasses import dataclass

def _add_type_field(cls):
    cls.__annotations__['type'] = str
    cls.type = Field(cls.__name__, description='The type of the class')
    return cls


@dataclass
@_add_type_field
class DataclassWithAddedField:
    """Dataclass with added field"""

    field: str = Field(description='The field')
