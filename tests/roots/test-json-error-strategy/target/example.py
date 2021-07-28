from pydantic import BaseModel


class NonSerializable(BaseModel):
    """NonSerializable

    """

    field: object = object()
    """Field"""

    class Config:
        arbitrary_types_allowed = True
