from typing import Generic, TypeVar, Optional, List

from pydantic import BaseModel, field_validator
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class Error(BaseModel):
    """HTTP error representation."""
    code: int
    message: str


class DataModel(BaseModel):
    """Payload representation."""
    numbers: List[int]
    people: List[str]


class Response(GenericModel, Generic[DataT]):
    """HTTP Response representation."""

    data: Optional[DataT]
    error: Optional[Error]

    @field_validator('error', always=True)
    def check_consistency(cls, v, values):
        if v is not None and values['data'] is not None:
            raise ValueError('must not provide both data and error')
        if v is None and values.get('data') is None:
            raise ValueError('must provide data or error')
        return v
